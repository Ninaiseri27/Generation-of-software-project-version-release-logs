from __future__ import annotations

import json
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

from ..models import EnreEntity, EnreRelation, FUNCTION_LIKE_KINDS, NormalizedEnreGraph


PARSER_NAME = "enre-normalizer-v2"
NORMALIZE_TOKEN_RE = re.compile(r"[^a-z0-9]+")
IMPLEMENTATION_SUFFIXES = {".c", ".cc", ".cpp", ".cxx"}


@dataclass(slots=True)
class ParsedEnreRoot:
    variables: list[dict[str, object]]
    relations: list[dict[str, object]]
    raw_entity_count: int
    raw_relation_count: int


class EnreParser:
    def parse_json_file(self, path: str | Path) -> NormalizedEnreGraph:
        input_path = Path(path)
        raw_payload = json.loads(input_path.read_text(encoding="utf-8"))
        return self.parse_payload(raw_payload, input_path=input_path)

    def parse_payload(
        self,
        raw_payload: object,
        *,
        input_path: str | Path | None = None,
    ) -> NormalizedEnreGraph:
        parsed = self._coerce_root(raw_payload)
        raw_entity_kind_counts = dict(
            sorted(Counter(self._normalize_token(str(item.get("entityType", "unknown"))) for item in parsed.variables).items())
        )
        raw_relation_type_counts = dict(
            sorted(Counter(self._normalize_token(str(item.get("type", "unknown"))) for item in parsed.relations).items())
        )
        entities = self._parse_entities(parsed.variables)
        entity_index = {item.id: item for item in entities}
        relations, dropped_relation_count, deduplicated_relation_count = self._parse_relations(
            parsed.relations,
            entity_index,
        )

        entity_kind_counts = dict(sorted(Counter(item.kind for item in entities).items()))
        relation_type_counts = dict(sorted(Counter(item.type for item in relations).items()))

        return NormalizedEnreGraph(
            parser=PARSER_NAME,
            input_path=str(input_path) if input_path is not None else None,
            entities=entities,
            relations=relations,
            raw_entity_count=parsed.raw_entity_count,
            dropped_entity_count=max(parsed.raw_entity_count - len(entities), 0),
            raw_relation_count=parsed.raw_relation_count,
            dropped_relation_count=dropped_relation_count,
            deduplicated_relation_count=deduplicated_relation_count,
            raw_entity_kind_counts=raw_entity_kind_counts,
            raw_relation_type_counts=raw_relation_type_counts,
            entity_kind_counts=entity_kind_counts,
            relation_type_counts=relation_type_counts,
        )

    @staticmethod
    def _coerce_root(raw_payload: object) -> ParsedEnreRoot:
        if isinstance(raw_payload, dict):
            return EnreParser._coerce_graph_object(raw_payload)

        if isinstance(raw_payload, list):
            if len(raw_payload) != 1:
                raise ValueError(
                    "Expected the ENRE JSON top level to be a single-item list. "
                    f"Received {len(raw_payload)} items."
                )
            item = raw_payload[0]
            if not isinstance(item, dict):
                raise ValueError("Expected the ENRE JSON list item to be an object.")
            return EnreParser._coerce_graph_object(item)

        raise ValueError("Unsupported ENRE payload: expected an object or single-item list.")

    @staticmethod
    def _coerce_graph_object(raw_graph: dict[str, object]) -> ParsedEnreRoot:
        variables = raw_graph.get("variables")
        relations = raw_graph.get("relations")
        if not isinstance(variables, list):
            raise ValueError("The ENRE payload must contain a list field named 'variables'.")
        if not isinstance(relations, list):
            raise ValueError("The ENRE payload must contain a list field named 'relations'.")
        return ParsedEnreRoot(
            variables=[item for item in variables if isinstance(item, dict)],
            relations=[item for item in relations if isinstance(item, dict)],
            raw_entity_count=len(variables),
            raw_relation_count=len(relations),
        )

    def _parse_entities(self, raw_entities: list[dict[str, object]]) -> list[EnreEntity]:
        interim: list[EnreEntity] = []
        for item in raw_entities:
            entity_id = self._require_int(item, "id")
            raw_kind = str(item.get("entityType", "unknown"))
            qualified_name = str(item.get("qualifiedName", ""))
            file_path = self._clean_path(item.get("entityFile"))
            entity = EnreEntity(
                id=entity_id,
                name=self._derive_name(qualified_name, file_path, raw_kind),
                qualified_name=qualified_name,
                kind=self._normalize_token(raw_kind),
                raw_kind=raw_kind,
                is_user_defined=False,
                file_path=file_path,
                start_line=self._clean_optional_int(item.get("startLine")),
                end_line=self._clean_optional_int(item.get("endLine")),
                start_column=self._clean_optional_int(item.get("startColumn")),
                end_column=self._clean_optional_int(item.get("endColumn")),
                parent_id=self._clean_optional_parent_id(item.get("parentID")),
                raw_scale=self._clean_optional_int(item.get("scale")),
            )
            interim.append(entity)

        by_id = {item.id: item for item in interim}
        parsed: list[EnreEntity] = []
        for item in sorted(interim, key=lambda value: value.id):
            if item.kind not in FUNCTION_LIKE_KINDS:
                continue
            parent_qualified_name = None
            if item.parent_id is not None:
                parent_qualified_name = by_id.get(item.parent_id).qualified_name if by_id.get(item.parent_id) else None
            parsed.append(
                EnreEntity(
                    id=item.id,
                    name=item.name,
                    qualified_name=item.qualified_name,
                    kind=item.kind,
                    raw_kind=item.raw_kind,
                    is_user_defined=self._infer_user_defined(item.file_path),
                    file_path=item.file_path,
                    start_line=item.start_line,
                    end_line=item.end_line,
                    start_column=item.start_column,
                    end_column=item.end_column,
                    parent_id=item.parent_id,
                    parent_qualified_name=parent_qualified_name,
                    raw_scale=item.raw_scale,
                )
            )

        return parsed

    def _parse_relations(
        self,
        raw_relations: list[dict[str, object]],
        entity_index: dict[int, EnreEntity],
    ) -> tuple[list[EnreRelation], int, int]:
        dropped_relation_count = 0
        deduplicated_relation_count = 0
        aggregated: dict[tuple[str, int, int], EnreRelation] = {}

        for item in raw_relations:
            raw_type = str(item.get("type", "unknown"))
            relation_type = self._normalize_token(raw_type)
            if relation_type != "call":
                dropped_relation_count += 1
                continue
            source_id = self._clean_optional_int(item.get("src"))
            target_id = self._clean_optional_int(item.get("dest"))

            if source_id is None or target_id is None:
                dropped_relation_count += 1
                continue
            if source_id not in entity_index or target_id not in entity_index:
                dropped_relation_count += 1
                continue

            key = (relation_type, source_id, target_id)
            existing = aggregated.get(key)
            if existing is None:
                aggregated[key] = EnreRelation(
                    type=relation_type,
                    source_id=source_id,
                    target_id=target_id,
                    occurrence_count=1,
                    raw_types=[raw_type],
                )
                continue

            existing.occurrence_count += 1
            deduplicated_relation_count += 1
            if raw_type not in existing.raw_types:
                existing.raw_types.append(raw_type)

        parsed = sorted(aggregated.values(), key=lambda item: (item.type, item.source_id, item.target_id))
        for item in parsed:
            item.raw_types.sort()
        return parsed, dropped_relation_count, deduplicated_relation_count

    @staticmethod
    def _derive_name(qualified_name: str, file_path: str | None, raw_kind: str) -> str:
        if EnreParser._normalize_token(raw_kind) == "file":
            if file_path:
                return Path(file_path).name
            if qualified_name:
                return Path(qualified_name).name
            return ""

        if "::" in qualified_name:
            return qualified_name.rsplit("::", maxsplit=1)[-1]
        if qualified_name:
            return qualified_name
        if file_path:
            return Path(file_path).name
        return ""

    @staticmethod
    def _normalize_token(value: str) -> str:
        normalized = NORMALIZE_TOKEN_RE.sub("_", value.strip().lower()).strip("_")
        return normalized or "unknown"

    @staticmethod
    def _infer_user_defined(file_path: str | None) -> bool:
        if not file_path:
            return False
        return Path(file_path).suffix.lower() in IMPLEMENTATION_SUFFIXES

    @staticmethod
    def _clean_path(value: object) -> str | None:
        if value is None:
            return None
        text = str(value).strip()
        if not text or text == "-1":
            return None
        return text.replace("\\", "/")

    @staticmethod
    def _clean_optional_parent_id(value: object) -> int | None:
        parsed = EnreParser._clean_optional_int(value)
        if parsed is None or parsed < 0:
            return None
        return parsed

    @staticmethod
    def _clean_optional_int(value: object) -> int | None:
        if value is None:
            return None
        parsed = int(value)
        if parsed < 0:
            return None
        return parsed

    @staticmethod
    def _require_int(item: dict[str, object], key: str) -> int:
        if key not in item:
            raise ValueError(f"The ENRE entity is missing required field: {key}")
        return int(item[key])

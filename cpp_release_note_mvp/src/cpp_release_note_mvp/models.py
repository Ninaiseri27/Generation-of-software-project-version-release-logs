from __future__ import annotations

from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Any


@dataclass(slots=True)
class VersionPair:
    repo_path: Path
    ref_version: str
    tgt_version: str


@dataclass(slots=True)
class DiffHunk:
    file_path: str
    old_start: int
    old_count: int
    new_start: int
    new_count: int
    lines: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class CodeSymbol:
    name: str
    signature: str
    file_path: str
    start_line: int
    end_line: int
    raw_header: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class ChangedFunction:
    symbol: str
    signature: str
    file_path: str
    change_type: str
    start_line: int
    end_line: int
    diff_hunks: list[DiffHunk] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        payload = asdict(self)
        payload["diff_hunks"] = [hunk.to_dict() for hunk in self.diff_hunks]
        return payload


@dataclass(slots=True)
class EnreEntity:
    id: int
    name: str
    qualified_name: str
    kind: str
    raw_kind: str
    is_user_defined: bool
    file_path: str | None
    start_line: int | None
    end_line: int | None
    start_column: int | None
    end_column: int | None
    parent_id: int | None
    parent_qualified_name: str | None = None
    raw_scale: int | None = None

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class EnreRelation:
    type: str
    source_id: int
    target_id: int
    occurrence_count: int = 1
    raw_types: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass(slots=True)
class NormalizedEnreGraph:
    parser: str
    input_path: str | None
    entities: list[EnreEntity] = field(default_factory=list)
    relations: list[EnreRelation] = field(default_factory=list)
    raw_entity_count: int = 0
    dropped_entity_count: int = 0
    raw_relation_count: int = 0
    dropped_relation_count: int = 0
    deduplicated_relation_count: int = 0
    raw_entity_kind_counts: dict[str, int] = field(default_factory=dict)
    raw_relation_type_counts: dict[str, int] = field(default_factory=dict)
    entity_kind_counts: dict[str, int] = field(default_factory=dict)
    relation_type_counts: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        function_like_count = sum(1 for item in self.entities if item.kind in FUNCTION_LIKE_KINDS)
        user_defined_function_count = sum(1 for item in self.entities if item.is_user_defined)
        call_relation_count = sum(1 for item in self.relations if item.type == "call")
        return {
            "source": {
                "parser": self.parser,
                "input_path": self.input_path,
            },
            "summary": {
                "raw_entity_count": self.raw_entity_count,
                "normalized_entity_count": len(self.entities),
                "dropped_entity_count": self.dropped_entity_count,
                "raw_relation_count": self.raw_relation_count,
                "normalized_relation_count": len(self.relations),
                "dropped_relation_count": self.dropped_relation_count,
                "deduplicated_relation_count": self.deduplicated_relation_count,
                "function_like_entity_count": function_like_count,
                "user_defined_function_count": user_defined_function_count,
                "call_relation_count": call_relation_count,
                "raw_entity_kind_counts": self.raw_entity_kind_counts,
                "raw_relation_type_counts": self.raw_relation_type_counts,
                "entity_kind_counts": self.entity_kind_counts,
                "relation_type_counts": self.relation_type_counts,
            },
            "entities": [item.to_dict() for item in self.entities],
            "relations": [item.to_dict() for item in self.relations],
        }

    def entity_index(self) -> dict[int, EnreEntity]:
        return {item.id: item for item in self.entities}

    def function_like_entities(self) -> list[EnreEntity]:
        return [item for item in self.entities if item.kind in FUNCTION_LIKE_KINDS]

    def call_relations(self) -> list[EnreRelation]:
        return [item for item in self.relations if item.type == "call"]


FUNCTION_LIKE_KINDS = frozenset({"function", "method", "constructor", "destructor"})

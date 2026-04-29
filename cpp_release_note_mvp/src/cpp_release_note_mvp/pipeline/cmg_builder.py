from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CALL_LIKE_RE = re.compile(r"(?<![A-Za-z0-9_])([A-Za-z_][A-Za-z0-9_]*(?:::[A-Za-z_][A-Za-z0-9_]*)*)\s*\(")
IDENTIFIER_RE = re.compile(r"\b[A-Za-z_][A-Za-z0-9_]*\b")
CALL_EXCLUDE = {
    "alignof",
    "catch",
    "const_cast",
    "decltype",
    "delete",
    "dynamic_cast",
    "for",
    "if",
    "new",
    "reinterpret_cast",
    "return",
    "sizeof",
    "static_assert",
    "static_cast",
    "switch",
    "throw",
    "typeid",
    "while",
}
GENERIC_EXTERNAL_CALLS = {
    "close",
    "free",
    "lseek",
    "malloc",
    "memcpy",
    "memset",
    "open",
    "printf",
    "read",
    "write",
}
IDENTIFIER_EXCLUDE = CALL_EXCLUDE | {
    "auto",
    "bool",
    "break",
    "case",
    "char",
    "class",
    "const",
    "continue",
    "default",
    "double",
    "else",
    "enum",
    "false",
    "float",
    "int",
    "long",
    "nullptr",
    "private",
    "protected",
    "public",
    "short",
    "signed",
    "static",
    "string",
    "std",
    "struct",
    "true",
    "typedef",
    "typename",
    "unsigned",
    "using",
    "void",
    "volatile",
}


@dataclass(slots=True)
class EntityMatchResult:
    entity_id: int | None
    level: str | None
    graph_side: str
    notes: list[str]


class CmgBuilder:
    def __init__(
        self,
        *,
        changed_functions: list[dict[str, object]],
        ref_normalized_graph: dict[str, object],
        tgt_normalized_graph: dict[str, object],
        version_pair: dict[str, object] | None = None,
        strategy: str = "adaptive",
        matching_view: str = "strict",
        context_hops: int = 1,
        matched_hops: int = 1,
        sparse_matched_hops: int = 2,
        unmatched_expand_hops: int = 1,
        unmatched_expand_from_diff_calls: bool = True,
        min_edges_for_sparse: int = 1,
        include_parent_context: bool = True,
        include_diff_calls: bool = True,
        max_nodes: int = 30,
        max_edges: int = 60,
    ) -> None:
        self.changed_functions = changed_functions
        self.ref_graph = ref_normalized_graph
        self.tgt_graph = tgt_normalized_graph
        self.version_pair = version_pair or {}
        self.strategy = strategy
        self.matching_view = matching_view
        self.context_hops = context_hops
        self.matched_hops = matched_hops
        self.sparse_matched_hops = sparse_matched_hops
        self.unmatched_expand_hops = unmatched_expand_hops
        self.unmatched_expand_from_diff_calls = unmatched_expand_from_diff_calls
        self.min_edges_for_sparse = min_edges_for_sparse
        self.include_parent_context = include_parent_context
        self.include_diff_calls = include_diff_calls
        self.max_nodes = max_nodes
        self.max_edges = max_edges

        self._ref_entities = self._entity_map(self.ref_graph)
        self._tgt_entities = self._entity_map(self.tgt_graph)
        self._ref_edges = self._call_edges(self.ref_graph)
        self._tgt_edges = self._call_edges(self.tgt_graph)

    def build_payload(self) -> dict[str, object]:
        entries: list[dict[str, object]] = []
        unmatched_symbols: list[str] = []

        for changed in self.changed_functions:
            graph_side = self._graph_side_for_change(changed)
            graph = self.tgt_graph if graph_side == "tgt" else self.ref_graph
            entity_map = self._tgt_entities if graph_side == "tgt" else self._ref_entities
            call_edges = self._tgt_edges if graph_side == "tgt" else self._ref_edges

            match = self._match_entity(changed, graph, graph_side=graph_side)
            diff_calls = self._extract_diff_called_symbols(changed) if self.include_diff_calls else []
            if self.strategy == "strict_1hop":
                cmg = {"nodes": [], "edges": [], "provenance": {"strategy": "strict_1hop"}}
                if match.entity_id is not None:
                    cmg = self._slice_hop_cmg(
                        seed_ids=[match.entity_id],
                        entity_map=entity_map,
                        call_edges=call_edges,
                        hops=1,
                        provenance={"strategy": "strict_1hop", "changed_node_id": match.entity_id},
                    )
            elif match.entity_id is not None:
                cmg = self._build_adaptive_matched_cmg(
                    changed=changed,
                    entity_id=match.entity_id,
                    entity_map=entity_map,
                    call_edges=call_edges,
                    diff_calls=diff_calls,
                )
            else:
                cmg = self._build_synthetic_cmg(
                    changed=changed,
                    entity_map=entity_map,
                    call_edges=call_edges,
                    diff_calls=diff_calls,
                )

            if match.entity_id is None:
                unmatched_symbols.append(str(changed.get("symbol", "")))
            fallback_context = self._build_fallback_context(
                changed=changed,
                match=match,
                cmg=cmg,
                entity_map=entity_map,
                diff_calls=diff_calls,
            )

            entries.append(
                {
                    "symbol": str(changed.get("symbol", "")),
                    "signature": str(changed.get("signature", "")),
                    "file_path": str(changed.get("file_path", "")),
                    "change_type": str(changed.get("change_type", "")),
                    "start_line": changed.get("start_line"),
                    "end_line": changed.get("end_line"),
                    "diff_hunks": changed.get("diff_hunks", []),
                    "change_notes": changed.get("notes", []),
                    "graph_side": graph_side,
                    "matched_entity_id": match.entity_id,
                    "match_level": match.level,
                    "match_notes": match.notes,
                    "cmg": cmg,
                    "fallback_context": fallback_context,
                }
            )

        matched_count = sum(1 for entry in entries if entry["matched_entity_id"] is not None)
        fallback_context_count = sum(1 for entry in entries if entry.get("fallback_context"))
        synthetic_entry_count = sum(
            1
            for entry in entries
            if any(
                str(node.get("entity_source", "")).startswith("synthetic:")
                for node in self._list_of_dicts(entry.get("cmg", {}).get("nodes") if isinstance(entry.get("cmg"), dict) else None)
            )
        )
        diff_call_edge_count = sum(
            1
            for entry in entries
            for edge in self._list_of_dicts(entry.get("cmg", {}).get("edges") if isinstance(entry.get("cmg"), dict) else None)
            if str(edge.get("provenance", "")) == "diff-derived"
        )
        return {
            "source": {
                "builder": "cmg-builder-v3",
                "strategy": self.strategy,
                "matching_view": self.matching_view,
                "context_hops": self.context_hops,
                "matched_hops": self.matched_hops,
                "sparse_matched_hops": self.sparse_matched_hops,
                "unmatched_expand_hops": self.unmatched_expand_hops,
                "unmatched_expand_from_diff_calls": self.unmatched_expand_from_diff_calls,
                "min_edges_for_sparse": self.min_edges_for_sparse,
                "include_parent_context": self.include_parent_context,
                "include_diff_calls": self.include_diff_calls,
                "max_nodes": self.max_nodes,
                "max_edges": self.max_edges,
            },
            "summary": {
                "entry_count": len(entries),
                "matched_entry_count": matched_count,
                "unmatched_entry_count": len(entries) - matched_count,
                "fallback_context_entry_count": fallback_context_count,
                "synthetic_entry_count": synthetic_entry_count,
                "diff_call_edge_count": diff_call_edge_count,
            },
            "version_pair": {
                "ref": self.version_pair.get("ref_version"),
                "tgt": self.version_pair.get("tgt_version"),
            },
            "entries": entries,
            "unmatched_symbols": self._dedupe_preserve_order_text(unmatched_symbols),
        }

    def _match_entity(
        self,
        changed: dict[str, object],
        graph: dict[str, object],
        *,
        graph_side: str,
    ) -> EntityMatchResult:
        symbol = str(changed.get("symbol", "")).strip()
        file_path = str(changed.get("file_path", "")).replace("\\", "/")
        basename = Path(file_path).name
        symbol_leaf = symbol.rsplit("::", maxsplit=1)[-1]
        start_line = self._optional_int(changed.get("start_line"))
        end_line = self._optional_int(changed.get("end_line"))

        entities = graph.get("entities", [])
        if not isinstance(entities, list):
            return EntityMatchResult(None, None, graph_side, ["The normalized graph has no usable entities list."])

        exact_path_candidates = [
            entity
            for entity in entities
            if self._path_matches(file_path, entity)
            and self._symbol_matches(symbol, symbol_leaf, entity)
        ]
        if exact_path_candidates:
            selected = self._select_best_candidate(exact_path_candidates, start_line, end_line)
            notes = [f"Matched on full path and symbol in the {graph_side} graph."]
            if len(exact_path_candidates) > 1:
                notes.append(f"{len(exact_path_candidates)} candidates found; tie-broken by line overlap or distance.")
            return EntityMatchResult(int(selected["id"]), "path+symbol", graph_side, notes)

        basename_candidates = [
            entity
            for entity in entities
            if self._basename_matches(basename, entity)
            and self._symbol_matches(symbol, symbol_leaf, entity)
        ]
        if basename_candidates:
            selected = self._select_best_candidate(basename_candidates, start_line, end_line)
            notes = [f"Matched on basename and symbol in the {graph_side} graph."]
            if len(basename_candidates) > 1:
                notes.append(f"{len(basename_candidates)} candidates found; tie-broken by line overlap or distance.")
            return EntityMatchResult(int(selected["id"]), "basename+symbol", graph_side, notes)

        overlap_candidates = [
            entity
            for entity in entities
            if self._symbol_matches(symbol, symbol_leaf, entity)
            and self._line_ranges_overlap(start_line, end_line, entity)
        ]
        if overlap_candidates:
            selected = self._select_best_candidate(overlap_candidates, start_line, end_line)
            notes = [f"Matched on symbol plus mandatory line overlap in the {graph_side} graph."]
            if len(overlap_candidates) > 1:
                notes.append(f"{len(overlap_candidates)} candidates found; tie-broken by distance and qualified name.")
            return EntityMatchResult(int(selected["id"]), "symbol+overlap", graph_side, notes)

        return EntityMatchResult(
            None,
            None,
            graph_side,
            [f"No entity matched symbol={symbol!r} file_path={file_path!r} in the {graph_side} graph."],
        )

    def _slice_1_hop_cmg(
        self,
        entity_id: int,
        entity_map: dict[int, dict[str, object]],
        call_edges: list[dict[str, object]],
    ) -> dict[str, object]:
        return self._slice_hop_cmg(
            seed_ids=[entity_id],
            entity_map=entity_map,
            call_edges=call_edges,
            hops=1,
            provenance={"strategy": "strict_1hop", "changed_node_id": entity_id},
        )

    def _slice_hop_cmg(
        self,
        *,
        seed_ids: list[int],
        entity_map: dict[int, dict[str, object]],
        call_edges: list[dict[str, object]],
        hops: int,
        provenance: dict[str, object],
    ) -> dict[str, object]:
        ordered_node_ids = self._dedupe_preserve_order(seed_ids)
        frontier = set(ordered_node_ids)

        for _ in range(max(hops, 0)):
            next_frontier: set[int] = set()
            current_nodes = set(ordered_node_ids)
            for edge in call_edges:
                source_id = int(edge["source_id"])
                target_id = int(edge["target_id"])
                if source_id in frontier and target_id not in current_nodes:
                    next_frontier.add(target_id)
                if target_id in frontier and source_id not in current_nodes:
                    next_frontier.add(source_id)
            if not next_frontier:
                break
            for node_id in sorted(next_frontier):
                if node_id not in ordered_node_ids:
                    ordered_node_ids.append(node_id)
            frontier = next_frontier

        if len(ordered_node_ids) > self.max_nodes:
            ordered_node_ids = ordered_node_ids[: self.max_nodes]
        node_set = set(ordered_node_ids)

        nodes = [entity_map[node_id] for node_id in ordered_node_ids if node_id in entity_map]
        edges = [
            edge
            for edge in call_edges
            if int(edge["source_id"]) in node_set and int(edge["target_id"]) in node_set
        ]
        edges.sort(key=lambda item: (int(item["source_id"]), int(item["target_id"])))
        if len(edges) > self.max_edges:
            edges = edges[: self.max_edges]

        return {
            "nodes": nodes,
            "edges": edges,
            "provenance": {
                **provenance,
                "hop_count": hops,
                "truncated_nodes": len(node_set) >= self.max_nodes,
                "truncated_edges": len(edges) >= self.max_edges,
            },
        }

    def _build_adaptive_matched_cmg(
        self,
        *,
        changed: dict[str, object],
        entity_id: int,
        entity_map: dict[int, dict[str, object]],
        call_edges: list[dict[str, object]],
        diff_calls: list[dict[str, object]],
    ) -> dict[str, object]:
        cmg = self._slice_hop_cmg(
            seed_ids=[entity_id],
            entity_map=entity_map,
            call_edges=call_edges,
            hops=self.matched_hops,
            provenance={
                "strategy": "adaptive",
                "changed_node_id": entity_id,
                "changed_node_source": "enre",
                "expansion_reason": "matched",
            },
        )

        if len(self._list_of_dicts(cmg.get("edges"))) < self.min_edges_for_sparse:
            cmg = self._slice_hop_cmg(
                seed_ids=[entity_id],
                entity_map=entity_map,
                call_edges=call_edges,
                hops=self.sparse_matched_hops,
                provenance={
                    "strategy": "adaptive",
                    "changed_node_id": entity_id,
                    "changed_node_source": "enre",
                    "expansion_reason": "sparse_matched_graph",
                },
            )

        if diff_calls and len(self._list_of_dicts(cmg.get("edges"))) < self.min_edges_for_sparse:
            self._add_diff_call_context(
                cmg=cmg,
                source_id=entity_id,
                source_is_synthetic=False,
                diff_calls=diff_calls,
                entity_map=entity_map,
                call_edges=call_edges,
                expand_hops=0,
            )

        return self._truncate_cmg(cmg, changed_node_id=entity_id)

    def _build_synthetic_cmg(
        self,
        *,
        changed: dict[str, object],
        entity_map: dict[int, dict[str, object]],
        call_edges: list[dict[str, object]],
        diff_calls: list[dict[str, object]],
    ) -> dict[str, object]:
        synthetic_id = self._synthetic_node_id(changed)
        synthetic_node = self._build_synthetic_node(changed, synthetic_id)
        cmg: dict[str, object] = {
            "nodes": [synthetic_node],
            "edges": [],
            "provenance": {
                "strategy": "adaptive",
                "changed_node_id": synthetic_id,
                "changed_node_source": synthetic_node["entity_source"],
                "expansion_reason": "unmatched_synthetic_node",
                "hop_count": 0,
            },
        }

        if self.unmatched_expand_from_diff_calls and diff_calls:
            self._add_diff_call_context(
                cmg=cmg,
                source_id=synthetic_id,
                source_is_synthetic=True,
                diff_calls=diff_calls,
                entity_map=entity_map,
                call_edges=call_edges,
                expand_hops=self.unmatched_expand_hops,
            )

        return self._truncate_cmg(cmg, changed_node_id=synthetic_id)

    def _add_diff_call_context(
        self,
        *,
        cmg: dict[str, object],
        source_id: int | str,
        source_is_synthetic: bool,
        diff_calls: list[dict[str, object]],
        entity_map: dict[int, dict[str, object]],
        call_edges: list[dict[str, object]],
        expand_hops: int,
    ) -> None:
        nodes = self._list_of_dicts(cmg.get("nodes"))
        edges = self._list_of_dicts(cmg.get("edges"))
        provenance = cmg.setdefault("provenance", {})
        if not isinstance(provenance, dict):
            provenance = {}
            cmg["provenance"] = provenance

        node_by_id = {self._node_id_key(node.get("id")): node for node in nodes}
        skipped_expansions: list[dict[str, object]] = []

        for call in diff_calls:
            name = str(call.get("name", "")).strip()
            if not name:
                continue

            resolved_entities = self._resolve_diff_call_entities(name, entity_map)
            if resolved_entities:
                for entity in resolved_entities:
                    target_id = int(entity["id"])
                    target_key = self._node_id_key(target_id)
                    if target_key not in node_by_id:
                        node = dict(entity)
                        node["entity_source"] = "enre_diff_call"
                        nodes.append(node)
                        node_by_id[target_key] = node
                    edges.append(
                        self._build_diff_call_edge(
                            source_id=source_id,
                            target_id=target_id,
                            call=call,
                            source_is_synthetic=source_is_synthetic,
                        )
                    )

                    if expand_hops > 0 and self._should_expand_resolved_call(entity, call_edges):
                        self._append_limited_call_neighbors(
                            nodes=nodes,
                            edges=edges,
                            node_by_id=node_by_id,
                            seed_id=target_id,
                            entity_map=entity_map,
                            call_edges=call_edges,
                            hops=expand_hops,
                        )
                    elif expand_hops > 0:
                        skipped_expansions.append(
                            {
                                "name": name,
                                "reason": "too_many_neighbors_or_external",
                                "entity_id": target_id,
                            }
                        )
                continue

            unresolved_node = self._build_unresolved_call_node(name, call)
            unresolved_key = self._node_id_key(unresolved_node["id"])
            if unresolved_key not in node_by_id:
                nodes.append(unresolved_node)
                node_by_id[unresolved_key] = unresolved_node
            edges.append(
                self._build_diff_call_edge(
                    source_id=source_id,
                    target_id=unresolved_node["id"],
                    call=call,
                    source_is_synthetic=source_is_synthetic,
                )
            )

        cmg["nodes"] = nodes
        cmg["edges"] = self._dedupe_edges(edges)
        provenance["diff_call_context_added"] = True
        if skipped_expansions:
            provenance["skipped_diff_call_expansions"] = skipped_expansions[:20]

    def _append_limited_call_neighbors(
        self,
        *,
        nodes: list[dict[str, object]],
        edges: list[dict[str, object]],
        node_by_id: dict[str, dict[str, object]],
        seed_id: int,
        entity_map: dict[int, dict[str, object]],
        call_edges: list[dict[str, object]],
        hops: int,
    ) -> None:
        frontier = {seed_id}
        for _ in range(max(hops, 0)):
            next_frontier: set[int] = set()
            for edge in call_edges:
                source_id = int(edge["source_id"])
                target_id = int(edge["target_id"])
                if source_id not in frontier:
                    continue
                target_entity = entity_map.get(target_id)
                if target_entity is None:
                    continue
                target_key = self._node_id_key(target_id)
                if target_key not in node_by_id:
                    node = dict(target_entity)
                    node["entity_source"] = "enre_neighbor"
                    nodes.append(node)
                    node_by_id[target_key] = node
                edges.append(dict(edge))
                next_frontier.add(target_id)
                if len(nodes) >= self.max_nodes or len(edges) >= self.max_edges:
                    return
            if not next_frontier:
                return
            frontier = next_frontier

    def _should_expand_resolved_call(
        self,
        entity: dict[str, object],
        call_edges: list[dict[str, object]],
    ) -> bool:
        if not bool(entity.get("is_user_defined")):
            return False
        entity_id = int(entity["id"])
        neighbor_count = sum(
            1
            for edge in call_edges
            if int(edge["source_id"]) == entity_id or int(edge["target_id"]) == entity_id
        )
        return 0 < neighbor_count <= 10

    def _resolve_diff_call_entities(
        self,
        name: str,
        entity_map: dict[int, dict[str, object]],
    ) -> list[dict[str, object]]:
        leaf = name.rsplit("::", maxsplit=1)[-1]
        if leaf in GENERIC_EXTERNAL_CALLS:
            return []

        candidates = [
            entity
            for entity in entity_map.values()
            if self._diff_call_matches_entity(name, leaf, entity)
        ]
        compact_candidates = [
            item for item in candidates if len(str(item.get("qualified_name", ""))) <= 180
        ]
        candidates = compact_candidates or candidates
        selected = sorted(
            candidates,
            key=lambda item: (
                str(item.get("name", "")) not in {name, leaf},
                str(item.get("qualified_name", "")).count("::"),
                len(str(item.get("qualified_name", ""))),
                not bool(item.get("is_user_defined")),
                int(item.get("id", 0)),
            ),
        )

        result: list[dict[str, object]] = []
        seen_labels: set[str] = set()
        for item in selected:
            qualified_name = self._compact_qualified_name(str(item.get("qualified_name", "")))
            if qualified_name in seen_labels:
                continue
            seen_labels.add(qualified_name)
            result.append(item)
            if len(result) >= 3:
                break
        return result

    def _truncate_cmg(
        self,
        cmg: dict[str, object],
        *,
        changed_node_id: int | str,
    ) -> dict[str, object]:
        nodes = self._list_of_dicts(cmg.get("nodes"))
        edges = self._dedupe_edges(self._list_of_dicts(cmg.get("edges")))
        original_node_count = len(nodes)
        original_edge_count = len(edges)

        ranked_nodes = sorted(
            nodes,
            key=lambda item: self._node_rank(item, changed_node_id),
        )
        kept_nodes = ranked_nodes[: self.max_nodes]
        kept_node_keys = {self._node_id_key(node.get("id")) for node in kept_nodes}
        kept_edges = [
            edge
            for edge in edges
            if self._node_id_key(edge.get("source_id")) in kept_node_keys
            and self._node_id_key(edge.get("target_id")) in kept_node_keys
        ][: self.max_edges]

        provenance = cmg.setdefault("provenance", {})
        if not isinstance(provenance, dict):
            provenance = {}
        provenance["changed_node_id"] = changed_node_id
        provenance["truncated_nodes"] = original_node_count > len(kept_nodes)
        provenance["truncated_edges"] = original_edge_count > len(kept_edges)
        provenance["original_node_count"] = original_node_count
        provenance["original_edge_count"] = original_edge_count

        return {
            "nodes": kept_nodes,
            "edges": kept_edges,
            "provenance": provenance,
        }

    def _node_rank(self, node: dict[str, object], changed_node_id: int | str) -> tuple[int, str]:
        node_id = self._node_id_key(node.get("id"))
        if node_id == self._node_id_key(changed_node_id):
            return (0, node_id)

        entity_source = str(node.get("entity_source", "enre"))
        if entity_source == "enre_diff_call":
            return (10, node_id)
        if entity_source == "enre_neighbor":
            return (20, node_id)
        if entity_source == "diff_call_unresolved":
            return (30, node_id)
        if bool(node.get("is_user_defined")):
            return (40, node_id)
        return (50, node_id)

    @staticmethod
    def _build_diff_call_edge(
        *,
        source_id: int | str,
        target_id: int | str,
        call: dict[str, object],
        source_is_synthetic: bool,
    ) -> dict[str, object]:
        return {
            "type": "call",
            "source_id": source_id,
            "target_id": target_id,
            "occurrence_count": call.get("occurrence_count", 1),
            "raw_types": ["DiffCall"],
            "provenance": "diff-derived",
            "source_is_synthetic": source_is_synthetic,
        }

    @staticmethod
    def _build_unresolved_call_node(
        name: str,
        call: dict[str, object],
    ) -> dict[str, object]:
        return {
            "id": f"unresolved-call:{name}",
            "name": name.rsplit("::", maxsplit=1)[-1],
            "qualified_name": name,
            "kind": "external_call",
            "raw_kind": "DiffCall",
            "is_user_defined": False,
            "file_path": None,
            "start_line": None,
            "end_line": None,
            "start_column": None,
            "end_column": None,
            "parent_id": None,
            "parent_qualified_name": None,
            "raw_scale": None,
            "entity_source": "diff_call_unresolved",
            "occurrence_count": call.get("occurrence_count", 1),
        }

    @staticmethod
    def _synthetic_node_id(changed: dict[str, object]) -> str:
        symbol = str(changed.get("symbol", "unknown")).replace(" ", "_")
        file_path = str(changed.get("file_path", "unknown")).replace("\\", "/")
        start_line = changed.get("start_line", "?")
        return f"synthetic:{file_path}:{symbol}:{start_line}"

    @staticmethod
    def _build_synthetic_node(
        changed: dict[str, object],
        synthetic_id: str,
    ) -> dict[str, object]:
        signature = str(changed.get("signature", ""))
        symbol = str(changed.get("symbol", ""))
        source = "synthetic:macro_test" if signature.startswith("HWTEST_") else "synthetic:tree_sitter"
        return {
            "id": synthetic_id,
            "name": symbol.rsplit("::", maxsplit=1)[-1],
            "qualified_name": symbol,
            "kind": "synthetic_changed_function",
            "raw_kind": "SyntheticChangedFunction",
            "is_user_defined": True,
            "file_path": str(changed.get("file_path", "")),
            "start_line": changed.get("start_line"),
            "end_line": changed.get("end_line"),
            "start_column": None,
            "end_column": None,
            "parent_id": None,
            "parent_qualified_name": None,
            "raw_scale": None,
            "entity_source": source,
            "signature": signature,
            "change_type": str(changed.get("change_type", "")),
        }

    def _build_fallback_context(
        self,
        *,
        changed: dict[str, object],
        match: EntityMatchResult,
        cmg: dict[str, object],
        entity_map: dict[int, dict[str, object]],
        diff_calls: list[dict[str, object]],
    ) -> dict[str, object]:
        nodes = cmg.get("nodes", [])
        edges = cmg.get("edges", [])
        node_count = len(nodes) if isinstance(nodes, list) else 0
        edge_count = len(edges) if isinstance(edges, list) else 0

        reason = "supplemental"
        if match.entity_id is None:
            reason = "unmatched"
        elif edge_count == 0:
            reason = "sparse_cmg"

        pseudo_node = {
            "symbol": str(changed.get("symbol", "")),
            "signature": str(changed.get("signature", "")),
            "file_path": str(changed.get("file_path", "")),
            "change_type": str(changed.get("change_type", "")),
            "start_line": changed.get("start_line"),
            "end_line": changed.get("end_line"),
            "matched_entity_id": match.entity_id,
        }

        context: dict[str, object] = {
            "reason": reason,
            "pseudo_changed_node": pseudo_node,
            "cmg_node_count": node_count,
            "cmg_edge_count": edge_count,
        }

        if self.include_parent_context and match.entity_id is not None:
            matched_entity = entity_map.get(match.entity_id)
            if matched_entity is not None:
                context["parent_context"] = {
                    "parent_id": matched_entity.get("parent_id"),
                    "parent_qualified_name": matched_entity.get("parent_qualified_name"),
                    "entity_qualified_name": matched_entity.get("qualified_name"),
                    "entity_file_path": matched_entity.get("file_path"),
                }

        if self.include_diff_calls:
            context["diff_called_symbols"] = diff_calls
            context["resolved_diff_calls"] = self._resolve_diff_calls(diff_calls, entity_map)
            context["diff_identifiers"] = self._extract_diff_identifiers(changed)

        return context

    def _extract_diff_called_symbols(self, changed: dict[str, object]) -> list[dict[str, object]]:
        diff_hunks = changed.get("diff_hunks")
        if not isinstance(diff_hunks, list):
            return []

        changed_symbol = str(changed.get("symbol", "")).rsplit("::", maxsplit=1)[-1]
        calls: dict[str, dict[str, object]] = {}
        for hunk in diff_hunks:
            if not isinstance(hunk, dict):
                continue
            for line_number, prefix, code in self._iter_diff_code_lines(hunk):
                if prefix not in {"+", "-", " "}:
                    continue
                for match in CALL_LIKE_RE.finditer(code):
                    name = match.group(1)
                    if not self._is_useful_call_name(name, code, match.start(), changed_symbol):
                        continue
                    payload = calls.setdefault(
                        name,
                        {
                            "name": name,
                            "occurrence_count": 0,
                            "added_count": 0,
                            "removed_count": 0,
                            "context_count": 0,
                            "line_samples": [],
                        },
                    )
                    payload["occurrence_count"] = int(payload["occurrence_count"]) + 1
                    if prefix == "+":
                        payload["added_count"] = int(payload["added_count"]) + 1
                    elif prefix == "-":
                        payload["removed_count"] = int(payload["removed_count"]) + 1
                    else:
                        payload["context_count"] = int(payload["context_count"]) + 1
                    samples = payload["line_samples"]
                    if isinstance(samples, list) and len(samples) < 3:
                        location = f"L{line_number}" if line_number is not None else "L?"
                        samples.append(f"{location} {prefix}{code.strip()}")

        return sorted(
            calls.values(),
            key=lambda item: (
                -int(item["added_count"]),
                -int(item["occurrence_count"]),
                str(item["name"]),
            ),
        )[:20]

    def _resolve_diff_calls(
        self,
        diff_calls: list[dict[str, object]],
        entity_map: dict[int, dict[str, object]],
    ) -> list[dict[str, object]]:
        resolved: list[dict[str, object]] = []
        for call in diff_calls[:20]:
            name = str(call.get("name", ""))
            selected = self._resolve_diff_call_entities(name, entity_map)
            if not selected:
                continue
            matched_entities: list[dict[str, object]] = []
            seen_labels: set[str] = set()
            for item in selected:
                qualified_name = self._compact_qualified_name(str(item.get("qualified_name", "")))
                file_path = item.get("file_path")
                if qualified_name in seen_labels:
                    continue
                seen_labels.add(qualified_name)
                matched_entities.append(
                    {
                        "id": item.get("id"),
                        "qualified_name": qualified_name,
                        "file_path": file_path,
                        "is_user_defined": item.get("is_user_defined"),
                    }
                )
                if len(matched_entities) >= 3:
                    break
            resolved.append(
                {
                    "name": name,
                    "occurrence_count": call.get("occurrence_count", 0),
                    "matched_entities": matched_entities,
                }
            )
        return resolved[:12]

    def _extract_diff_identifiers(self, changed: dict[str, object]) -> list[dict[str, object]]:
        diff_hunks = changed.get("diff_hunks")
        if not isinstance(diff_hunks, list):
            return []

        counts: Counter[str] = Counter()
        added_counts: Counter[str] = Counter()
        removed_counts: Counter[str] = Counter()
        changed_symbol_leaf = str(changed.get("symbol", "")).rsplit("::", maxsplit=1)[-1]
        for hunk in diff_hunks:
            if not isinstance(hunk, dict):
                continue
            for _, prefix, code in self._iter_diff_code_lines(hunk):
                if prefix not in {"+", "-"}:
                    continue
                for match in IDENTIFIER_RE.finditer(code):
                    token = match.group(0)
                    normalized = token.lower()
                    if normalized in IDENTIFIER_EXCLUDE:
                        continue
                    if token == changed_symbol_leaf:
                        continue
                    if len(token) <= 1:
                        continue
                    counts[token] += 1
                    if prefix == "+":
                        added_counts[token] += 1
                    else:
                        removed_counts[token] += 1

        result: list[dict[str, object]] = []
        for name, count in counts.most_common(20):
            result.append(
                {
                    "name": name,
                    "occurrence_count": count,
                    "added_count": added_counts[name],
                    "removed_count": removed_counts[name],
                }
            )
        return result

    @staticmethod
    def _iter_diff_code_lines(hunk: dict[str, object]) -> list[tuple[int | None, str, str]]:
        raw_lines = hunk.get("lines", [])
        if not isinstance(raw_lines, list):
            return []

        old_line = CmgBuilder._optional_int(hunk.get("old_start")) or 0
        new_line = CmgBuilder._optional_int(hunk.get("new_start")) or 0
        result: list[tuple[int | None, str, str]] = []
        for raw_line in raw_lines:
            text = str(raw_line)
            prefix = text[:1] if text[:1] in {"+", "-", " "} else " "
            code = text[1:] if text[:1] in {"+", "-", " "} else text
            if prefix == "+":
                result.append((new_line if new_line > 0 else None, prefix, code))
                new_line += 1
            elif prefix == "-":
                result.append((old_line if old_line > 0 else None, prefix, code))
                old_line += 1
            else:
                result.append((new_line if new_line > 0 else None, prefix, code))
                old_line += 1
                new_line += 1
        return result

    @staticmethod
    def _is_useful_call_name(
        name: str,
        code: str,
        start_index: int,
        changed_symbol_leaf: str,
    ) -> bool:
        if not name:
            return False
        if name == changed_symbol_leaf or name.rsplit("::", maxsplit=1)[-1] == changed_symbol_leaf:
            return False
        if name.lower() in CALL_EXCLUDE:
            return False
        previous = code[:start_index].rstrip()
        if previous.endswith(".") or previous.endswith("->"):
            return False
        return True

    @staticmethod
    def _diff_call_matches_entity(
        name: str,
        leaf: str,
        entity: dict[str, object],
    ) -> bool:
        entity_name = str(entity.get("name", ""))
        qualified_name = str(entity.get("qualified_name", ""))
        if entity_name in {name, leaf}:
            return True
        if qualified_name in {name, leaf}:
            return True
        if "::" in name and qualified_name.endswith(f"::{name}"):
            return True
        if qualified_name.endswith(f"::{leaf}"):
            return True
        return False

    @staticmethod
    def _compact_qualified_name(value: str, max_length: int = 160) -> str:
        if len(value) <= max_length:
            return value
        keep = max_length - 3
        return "..." + value[-keep:]

    @staticmethod
    def _entity_map(graph: dict[str, object]) -> dict[int, dict[str, object]]:
        entities = graph.get("entities", [])
        if not isinstance(entities, list):
            return {}
        result: dict[int, dict[str, object]] = {}
        for entity in entities:
            if not isinstance(entity, dict):
                continue
            entity_id = entity.get("id")
            if entity_id is None:
                continue
            result[int(entity_id)] = entity
        return result

    @staticmethod
    def _call_edges(graph: dict[str, object]) -> list[dict[str, object]]:
        relations = graph.get("relations", [])
        if not isinstance(relations, list):
            return []
        return [
            relation
            for relation in relations
            if isinstance(relation, dict) and str(relation.get("type", "")) == "call"
        ]

    @staticmethod
    def _graph_side_for_change(changed: dict[str, object]) -> str:
        change_type = str(changed.get("change_type", "")).lower()
        if change_type == "deleted":
            return "ref"
        return "tgt"

    @staticmethod
    def _path_matches(file_path: str, entity: dict[str, object]) -> bool:
        entity_path = str(entity.get("file_path", "")).replace("\\", "/")
        return bool(entity_path) and (entity_path == file_path or entity_path.endswith(file_path))

    @staticmethod
    def _basename_matches(basename: str, entity: dict[str, object]) -> bool:
        entity_path = str(entity.get("file_path", "")).replace("\\", "/")
        return bool(entity_path) and Path(entity_path).name == basename

    @staticmethod
    def _symbol_matches(symbol: str, symbol_leaf: str, entity: dict[str, object]) -> bool:
        name = str(entity.get("name", ""))
        qualified_name = str(entity.get("qualified_name", ""))
        candidates = {symbol, symbol_leaf}
        for candidate in candidates:
            if not candidate:
                continue
            if candidate == name:
                return True
            if candidate in qualified_name:
                return True
            if name and name in candidate:
                return True
        return False

    def _select_best_candidate(
        self,
        candidates: list[dict[str, object]],
        start_line: int | None,
        end_line: int | None,
    ) -> dict[str, object]:
        overlapping = [
            candidate for candidate in candidates if self._line_ranges_overlap(start_line, end_line, candidate)
        ]
        if overlapping:
            return sorted(
                overlapping,
                key=lambda item: (
                    self._distance_to_candidate(start_line, end_line, item),
                    str(item.get("qualified_name", "")),
                    int(item.get("id", 0)),
                ),
            )[0]

        return sorted(
            candidates,
            key=lambda item: (
                self._distance_to_candidate(start_line, end_line, item),
                str(item.get("qualified_name", "")),
                int(item.get("id", 0)),
            ),
        )[0]

    @staticmethod
    def _line_ranges_overlap(
        start_line: int | None,
        end_line: int | None,
        entity: dict[str, object],
    ) -> bool:
        if start_line is None or end_line is None:
            return False
        entity_start = CmgBuilder._optional_int(entity.get("start_line"))
        entity_end = CmgBuilder._optional_int(entity.get("end_line"))
        if entity_start is None:
            return False
        if entity_end is None:
            entity_end = entity_start
        return not (end_line < entity_start or start_line > entity_end)

    @staticmethod
    def _distance_to_candidate(
        start_line: int | None,
        end_line: int | None,
        entity: dict[str, object],
    ) -> int:
        entity_start = CmgBuilder._optional_int(entity.get("start_line"))
        entity_end = CmgBuilder._optional_int(entity.get("end_line"))
        if entity_start is None:
            return 10**9
        if entity_end is None:
            entity_end = entity_start
        if start_line is None or end_line is None:
            return entity_start
        if not (end_line < entity_start or start_line > entity_end):
            return 0
        if end_line < entity_start:
            return entity_start - end_line
        return start_line - entity_end

    @staticmethod
    def _dedupe_preserve_order(values: list[int]) -> list[int]:
        seen: set[int] = set()
        result: list[int] = []
        for value in values:
            if value in seen:
                continue
            seen.add(value)
            result.append(value)
        return result

    @staticmethod
    def _dedupe_preserve_order_text(values: list[str]) -> list[str]:
        seen: set[str] = set()
        result: list[str] = []
        for value in values:
            if value in seen:
                continue
            seen.add(value)
            result.append(value)
        return result

    @staticmethod
    def _dedupe_edges(edges: list[dict[str, object]]) -> list[dict[str, object]]:
        seen: set[tuple[str, str, str, str]] = set()
        result: list[dict[str, object]] = []
        for edge in edges:
            key = (
                str(edge.get("type", "")),
                CmgBuilder._node_id_key(edge.get("source_id")),
                CmgBuilder._node_id_key(edge.get("target_id")),
                str(edge.get("provenance", "")),
            )
            if key in seen:
                continue
            seen.add(key)
            result.append(edge)
        return result

    @staticmethod
    def _node_id_key(value: object) -> str:
        return str(value)

    @staticmethod
    def _list_of_dicts(raw: object) -> list[dict[str, object]]:
        if not isinstance(raw, list):
            return []
        return [item for item in raw if isinstance(item, dict)]

    @staticmethod
    def _optional_int(value: object) -> int | None:
        if value is None:
            return None
        return int(value)

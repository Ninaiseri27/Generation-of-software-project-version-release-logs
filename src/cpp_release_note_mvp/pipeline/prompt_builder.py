from __future__ import annotations

from pathlib import Path
from typing import Any

from ..config import AppConfig


SUPPORTED_PROMPT_VARIANTS = ("text_only", "diff_only", "no_graph", "no_fallback", "full")


class PromptBuilder:
    def __init__(
        self,
        *,
        project_name: str | None = None,
        project_description: str | None = None,
        version_pair: dict[str, object] | None = None,
        commit_messages: list[str] | None = None,
        changed_files: list[str] | None = None,
        prompt_variant: str = "full",
    ) -> None:
        self.project_name = project_name or "Unknown C/C++ Project"
        self.project_description = project_description
        self.version_pair = version_pair or {}
        self.commit_messages = commit_messages or []
        self.changed_files = changed_files or []
        self.prompt_variant = _normalize_prompt_variant(prompt_variant)

    def build_system_prompt(self) -> str:
        evidence_scope = {
            "text_only": "version metadata and commit-message evidence",
            "diff_only": "function-level diff evidence",
            "no_graph": "function-level diff evidence and commit-message evidence",
            "no_fallback": "function-level diff evidence, ENRE call-graph context, and commit-message evidence",
            "full": "function-level diff evidence, call-graph context, fallback context, and commit-message evidence",
        }[self.prompt_variant]
        return (
            "You are a C/C++ software release-note expert. "
            f"Analyze {evidence_scope}. "
            "Infer the functional intent of the change conservatively. "
            "Prefer accurate, user-relevant, concise descriptions. "
            "Do not invent behavior that is not supported by the provided evidence. "
            "Return exactly one JSON object with the keys "
            "`section`, `title`, and `summary`. "
            "`section` must be one of: Features, Bug Fixes, Performance, Reliability, Testing, Internal. "
            "`title` must be short plain text without markdown or a trailing period. "
            "`summary` must be one plain-text sentence without markdown."
        )

    def build_user_prompt(self, entry: dict[str, object]) -> str:
        sections: list[str] = []
        sections.append("Project")
        sections.append(self._format_project_section())

        changed_files_section = self._format_changed_files()
        if changed_files_section and self.prompt_variant != "diff_only":
            sections.append("")
            sections.append("Changed Files")
            sections.append(changed_files_section)

        if self.prompt_variant != "text_only":
            sections.append("")
            sections.append("Changed Function")
            sections.append(self._format_changed_function_section(entry))

        if self.prompt_variant in {"diff_only", "no_graph", "no_fallback", "full"}:
            diff_section = self._format_diff_code(entry)
            sections.append("")
            sections.append("Diff")
            sections.append(diff_section)

        if self.prompt_variant in {"no_fallback", "full"}:
            graph_section = self._format_cmg_graph(entry)
            sections.append("")
            if self.prompt_variant == "no_fallback":
                sections.append("Graph Context")
            else:
                sections.append("Graph and Fallback Context")
            sections.append(graph_section)

        if self.prompt_variant in {"text_only", "no_graph", "no_fallback", "full"}:
            commit_section = self._format_commit_messages()
        else:
            commit_section = ""
        if commit_section:
            sections.append("")
            sections.append("Commit Messages")
            sections.append(commit_section)

        sections.append("")
        sections.append("Task")
        sections.append(self._format_task_instruction())

        return "\n".join(sections).strip()

    def _format_project_section(self) -> str:
        lines = [f"Project: {self.project_name}"]
        ref_version = self.version_pair.get("ref") or self.version_pair.get("ref_version")
        tgt_version = self.version_pair.get("tgt") or self.version_pair.get("tgt_version")
        if ref_version or tgt_version:
            lines.append(f"Version Pair: {ref_version or '?'} -> {tgt_version or '?'}")
        if self.project_description:
            lines.append(f"Description: {self.project_description}")
        return "\n".join(lines)

    def _format_changed_files(self) -> str:
        if not self.changed_files:
            return ""
        return "\n".join(f"- {path}" for path in self.changed_files[:30])

    def _format_changed_function_section(self, entry: dict[str, object]) -> str:
        lines = [
            f"Symbol: {entry.get('symbol', '')}",
            f"Signature: {entry.get('signature', '')}",
            f"File: {entry.get('file_path', '')}",
            f"Change Type: {entry.get('change_type', '')}",
        ]

        start_line = entry.get("start_line")
        end_line = entry.get("end_line")
        if start_line is not None and end_line is not None:
            lines.append(f"Changed Range: {start_line}-{end_line}")

        matched_entity_id = entry.get("matched_entity_id")
        lines.append(f"Matched Entity ID: {matched_entity_id if matched_entity_id is not None else 'unmatched'}")

        match_level = entry.get("match_level")
        if match_level:
            lines.append(f"Match Level: {match_level}")

        match_notes = entry.get("match_notes")
        if isinstance(match_notes, list) and match_notes:
            lines.append("Match Notes:")
            lines.extend(f"- {note}" for note in match_notes)

        change_notes = entry.get("change_notes")
        if isinstance(change_notes, list) and change_notes:
            lines.append("Change Detection Notes:")
            lines.extend(f"- {note}" for note in change_notes)

        return "\n".join(lines)

    def _format_diff_code(self, entry: dict[str, object]) -> str:
        diff_hunks = entry.get("diff_hunks")
        if not isinstance(diff_hunks, list) or not diff_hunks:
            return "No function-level diff hunk is available."

        blocks: list[str] = []
        for index, hunk in enumerate(diff_hunks, start=1):
            if not isinstance(hunk, dict):
                continue
            header = (
                f"Hunk {index}: "
                f"{hunk.get('file_path', entry.get('file_path', ''))} "
                f"(old {hunk.get('old_start', '?')}+{hunk.get('old_count', '?')}, "
                f"new {hunk.get('new_start', '?')}+{hunk.get('new_count', '?')})"
            )
            lines = hunk.get("lines", [])
            if not isinstance(lines, list):
                lines = []
            block = "\n".join(str(line) for line in lines)
            blocks.append(f"{header}\n```diff\n{block}\n```")

        return "\n\n".join(blocks) if blocks else "No function-level diff hunk is available."

    def _format_cmg_graph(self, entry: dict[str, object]) -> str:
        cmg = entry.get("cmg")
        if not isinstance(cmg, dict):
            return self._format_fallback_context(entry) or "No CMG is available."

        nodes = cmg.get("nodes")
        edges = cmg.get("edges")
        if not isinstance(edges, list):
            edges = []
        if not isinstance(nodes, list) or not nodes:
            fallback = self._format_fallback_context(entry)
            if fallback:
                return "No ENRE CMG nodes are available.\n" + fallback
            return "No CMG nodes are available."

        provenance = cmg.get("provenance")
        if not isinstance(provenance, dict):
            provenance = {}
        matched_entity_id = entry.get("matched_entity_id")
        changed_node_id = matched_entity_id
        if changed_node_id is None:
            changed_node_id = provenance.get("changed_node_id")
        callers: list[dict[str, object]] = []
        changed_node: dict[str, object] | None = None
        callees: list[dict[str, object]] = []

        for node in nodes:
            if not isinstance(node, dict):
                continue
            node_id = node.get("id")
            if changed_node_id is not None and self._node_id_key(node_id) == self._node_id_key(changed_node_id):
                changed_node = node
                continue

            is_caller = any(
                isinstance(edge, dict)
                and self._node_id_key(edge.get("source_id")) == self._node_id_key(node_id)
                and self._node_id_key(edge.get("target_id")) == self._node_id_key(changed_node_id)
                for edge in edges
            )
            is_callee = any(
                isinstance(edge, dict)
                and self._node_id_key(edge.get("source_id")) == self._node_id_key(changed_node_id)
                and self._node_id_key(edge.get("target_id")) == self._node_id_key(node_id)
                for edge in edges
            )
            if is_caller:
                callers.append(node)
            elif is_callee:
                callees.append(node)

        ordered_nodes: list[tuple[str, dict[str, object]]] = []
        ordered_nodes.extend(("Caller", node) for node in callers)
        if changed_node is not None:
            ordered_nodes.append(("Changed", changed_node))
        ordered_nodes.extend(("Callee", node) for node in callees)
        ordered_node_ids = {self._node_id_key(node.get("id")) for _, node in ordered_nodes}
        ordered_nodes.extend(
            ("Context", node)
            for node in nodes
            if isinstance(node, dict) and self._node_id_key(node.get("id")) not in ordered_node_ids
        )

        if not ordered_nodes:
            ordered_nodes.extend(("Node", node) for node in nodes if isinstance(node, dict))

        node_index: dict[str, int] = {}
        lines: list[str] = []
        for index, (label, node) in enumerate(ordered_nodes, start=1):
            node_id = self._node_id_key(node.get("id"))
            node_index[node_id] = index
            lines.append(f"[{label}] {index}. {self._format_graph_node(node)}")

        relation_parts: list[str] = []
        for edge in edges:
            if not isinstance(edge, dict):
                continue
            source_id = self._node_id_key(edge.get("source_id"))
            target_id = self._node_id_key(edge.get("target_id"))
            if source_id not in node_index or target_id not in node_index:
                continue
            relation_parts.append(f"{node_index[source_id]} calls {node_index[target_id]}")

        if relation_parts:
            lines.append(f"Relations: {'; '.join(relation_parts)}")
        else:
            lines.append("Relations: none")

        fallback = self._format_fallback_context(entry)
        if fallback:
            lines.append("")
            lines.append(fallback)

        return "\n".join(lines)

    def _format_fallback_context(self, entry: dict[str, object]) -> str:
        fallback = entry.get("fallback_context")
        if not isinstance(fallback, dict) or not fallback:
            return ""

        lines: list[str] = ["Fallback Evidence:"]
        reason = fallback.get("reason")
        if reason:
            lines.append(f"- Reason: {reason}")

        pseudo_node = fallback.get("pseudo_changed_node")
        if isinstance(pseudo_node, dict):
            symbol = pseudo_node.get("symbol", entry.get("symbol", ""))
            file_path = pseudo_node.get("file_path", entry.get("file_path", ""))
            start_line = pseudo_node.get("start_line")
            end_line = pseudo_node.get("end_line")
            location = ""
            if start_line is not None and end_line is not None:
                location = f":{start_line}-{end_line}"
            lines.append(f"- Pseudo Changed Node: {symbol} ({file_path}{location})")

        parent_context = fallback.get("parent_context")
        if isinstance(parent_context, dict):
            entity_name = parent_context.get("entity_qualified_name")
            parent_name = parent_context.get("parent_qualified_name")
            if entity_name:
                lines.append(f"- Matched Entity: {entity_name}")
            if parent_name:
                lines.append(f"- Parent Context: {parent_name}")

        diff_calls = fallback.get("diff_called_symbols")
        if isinstance(diff_calls, list) and diff_calls:
            lines.append("- Diff-Derived Calls:")
            for item in diff_calls[:12]:
                if not isinstance(item, dict):
                    continue
                name = item.get("name")
                added = item.get("added_count", 0)
                removed = item.get("removed_count", 0)
                total = item.get("occurrence_count", 0)
                lines.append(f"  - {name} (total={total}, added={added}, removed={removed})")

        resolved_calls = fallback.get("resolved_diff_calls")
        if isinstance(resolved_calls, list) and resolved_calls:
            lines.append("- Resolved Diff Calls:")
            for item in resolved_calls[:8]:
                if not isinstance(item, dict):
                    continue
                name = item.get("name")
                matched_entities = item.get("matched_entities")
                if not isinstance(matched_entities, list) or not matched_entities:
                    continue
                labels = []
                for entity in matched_entities[:2]:
                    if not isinstance(entity, dict):
                        continue
                    qualified_name = self._compact_label(str(entity.get("qualified_name", "")))
                    file_path = entity.get("file_path")
                    file_label = Path(str(file_path)).name if file_path else "unknown-file"
                    labels.append(f"{qualified_name} ({file_label})")
                if labels:
                    lines.append(f"  - {name} -> {'; '.join(labels)}")

        identifiers = fallback.get("diff_identifiers")
        if isinstance(identifiers, list) and identifiers:
            names = [
                str(item.get("name"))
                for item in identifiers[:12]
                if isinstance(item, dict) and item.get("name")
            ]
            if names:
                lines.append(f"- Diff Identifiers: {', '.join(names)}")

        return "\n".join(lines)

    def _format_commit_messages(self) -> str:
        if not self.commit_messages:
            return ""
        limited = [message.strip() for message in self.commit_messages if message.strip()][:10]
        if not limited:
            return ""
        return "\n".join(f"- {message}" for message in limited)

    def _format_task_instruction(self) -> str:
        if self.prompt_variant == "text_only":
            return (
                "Write one structured release-note entry for this version pair using only the project metadata, "
                "changed-file list, and commit messages above. If the evidence is too broad, summarize the most "
                "important supported change conservatively. Return exactly one JSON object with this shape: "
                '{"section":"Bug Fixes","title":"Short evidence-based title","summary":"One sentence grounded in the provided evidence."} '
                "Do not wrap the JSON in markdown fences."
            )

        evidence_hint = {
            "diff_only": "Use only the changed-function metadata and diff evidence. Ignore graph and commit-message context.",
            "no_graph": "Use changed-function metadata, diff evidence, and commit messages. Ignore graph context.",
            "no_fallback": "Use changed-function metadata, diff evidence, ENRE graph context, and commit messages. Ignore fallback, synthetic-node, and diff-derived-call context.",
            "full": "Use changed-function metadata, diff evidence, graph/fallback context, and commit messages.",
        }[self.prompt_variant]
        return (
            "Write one structured release-note entry for this change. "
            f"{evidence_hint} "
            "Focus on externally visible behavior, bug fixes, compatibility implications, testing impact, "
            "or reliability impact. If the evidence is weak, be conservative and say only what is justified. "
            "Return exactly one JSON object with this shape: "
            '{"section":"Bug Fixes","title":"Short evidence-based title","summary":"One sentence grounded in the provided evidence."} '
            "Do not wrap the JSON in markdown fences."
        )

    @staticmethod
    def _format_graph_node(node: dict[str, object]) -> str:
        qualified_name = str(node.get("qualified_name", ""))
        raw_file_path = node.get("file_path")
        file_path = str(raw_file_path) if raw_file_path else ""
        file_label = Path(file_path).name if file_path else "unknown-file"
        user_defined = "user-defined" if bool(node.get("is_user_defined")) else "external-or-header"
        source = str(node.get("entity_source", "enre"))
        return f"{PromptBuilder._compact_label(qualified_name)} ({file_label}, {user_defined}, {source})"

    @staticmethod
    def _compact_label(value: str, max_length: int = 120) -> str:
        if len(value) <= max_length:
            return value
        keep = max_length - 3
        return "..." + value[-keep:]

    @staticmethod
    def _node_id_key(value: object) -> str:
        return str(value)


class PromptBundleBuilder:
    def __init__(
        self,
        *,
        project_name: str,
        project_description: str | None = None,
        max_commit_messages: int = 10,
        include_unmatched_entries: bool = True,
        prompt_variant: str = "full",
    ) -> None:
        self.project_name = project_name
        self.project_description = project_description
        self.max_commit_messages = max_commit_messages
        self.include_unmatched_entries = include_unmatched_entries
        self.prompt_variant = _normalize_prompt_variant(prompt_variant)

    @classmethod
    def from_app_config(cls, config: AppConfig) -> "PromptBundleBuilder":
        project_name = config.version_pair.repo_path.name
        project_description = None

        if config.enre is not None and config.enre.project_name:
            project_name = config.enre.project_name
        if config.project is not None:
            project_name = config.project.name or project_name
            project_description = config.project.description

        return cls(
            project_name=project_name,
            project_description=project_description,
        )

    def build_prompt_input_payload(
        self,
        *,
        changed_payload: dict[str, object],
        cmg_payload: dict[str, object],
    ) -> dict[str, object]:
        version_pair = self._build_version_pair(changed_payload, cmg_payload)
        changed_files = self._list_text(changed_payload.get("changed_files"))
        commit_messages = self._limited_commit_messages(changed_payload)
        source_commit_count = len(self._list_text(changed_payload.get("commit_messages")))

        if self.prompt_variant == "text_only":
            prompt_entries = [
                {
                    "entry_id": "entry-text-only-001",
                    "symbol": "release-level",
                    "signature": "",
                    "file_path": "",
                    "change_type": "release",
                    "graph_side": "",
                    "match_status": "not_applicable",
                    "matched_entity_id": None,
                    "match_level": None,
                    "start_line": None,
                    "end_line": None,
                    "diff_hunks": [],
                    "change_notes": [],
                    "match_notes": ["text_only baseline uses only project, changed-file, and commit-message evidence"],
                    "cmg": {"nodes": [], "edges": [], "provenance": {}},
                    "cmg_summary": self._build_cmg_summary(None),
                    "fallback_context": {},
                }
            ]
        else:
            source_entries = self._filtered_entries(cmg_payload)
            prompt_entries = []
            for index, entry in enumerate(source_entries, start=1):
                normalized_cmg = self._normalize_cmg(
                    entry.get("cmg"),
                    include_fallback_context=self.prompt_variant != "no_fallback",
                )
                prompt_entries.append(
                    {
                        "entry_id": f"entry-{index:03d}",
                        "symbol": str(entry.get("symbol", "")),
                        "signature": str(entry.get("signature", "")),
                        "file_path": str(entry.get("file_path", "")),
                        "change_type": str(entry.get("change_type", "")),
                        "graph_side": str(entry.get("graph_side", "")),
                        "match_status": "matched" if entry.get("matched_entity_id") is not None else "unmatched",
                        "matched_entity_id": entry.get("matched_entity_id"),
                        "match_level": entry.get("match_level"),
                        "start_line": entry.get("start_line"),
                        "end_line": entry.get("end_line"),
                        "diff_hunks": self._list_of_dicts(entry.get("diff_hunks")),
                        "change_notes": self._list_text(entry.get("change_notes")),
                        "match_notes": self._list_text(entry.get("match_notes")),
                        "cmg": normalized_cmg,
                        "cmg_summary": self._build_cmg_summary(normalized_cmg),
                        "fallback_context": (
                            {}
                            if self.prompt_variant == "no_fallback"
                            else self._normalize_fallback_context(entry.get("fallback_context"))
                        ),
                    }
                )

        matched_count = sum(1 for entry in prompt_entries if entry["match_status"] == "matched")
        unmatched_count = sum(1 for entry in prompt_entries if entry["match_status"] == "unmatched")
        not_applicable_count = sum(
            1 for entry in prompt_entries if entry["match_status"] == "not_applicable"
        )
        unmatched_symbols = [
            str(item)
            for item in cmg_payload.get("unmatched_symbols", [])
            if isinstance(item, str)
        ]

        return {
            "source": {
                "builder": "prompt-input-builder-v4",
                "prompt_variant": self.prompt_variant,
            },
            "project": {
                "name": self.project_name,
                "description": self.project_description,
            },
            "version_pair": version_pair,
            "context": {
                "changed_files": changed_files,
                "commit_messages": commit_messages,
                "source_commit_message_count": source_commit_count,
            },
            "summary": {
                "entry_count": len(prompt_entries),
                "matched_entry_count": matched_count,
                "unmatched_entry_count": unmatched_count,
                "not_applicable_entry_count": not_applicable_count,
                "fallback_context_entry_count": sum(
                    1 for entry in prompt_entries if entry.get("fallback_context")
                ),
                "synthetic_entry_count": sum(
                    1
                    for entry in prompt_entries
                    if any(
                        str(node.get("entity_source", "")).startswith("synthetic:")
                        for node in self._list_of_dicts(entry.get("cmg", {}).get("nodes") if isinstance(entry.get("cmg"), dict) else None)
                    )
                ),
                "filtered_unmatched_entries": not self.include_unmatched_entries,
                "prompt_variant": self.prompt_variant,
            },
            "entries": prompt_entries,
            "unmatched_symbols": unmatched_symbols,
        }

    def build_prompt_bundle_payload(
        self,
        *,
        prompt_input_payload: dict[str, object],
    ) -> dict[str, object]:
        version_pair = prompt_input_payload.get("version_pair")
        context = prompt_input_payload.get("context")
        commit_messages = []
        if isinstance(context, dict):
            commit_messages = self._list_text(context.get("commit_messages"))
            changed_files = self._list_text(context.get("changed_files"))
        else:
            changed_files = []

        if self.prompt_variant == "diff_only":
            commit_messages = []

        prompt_builder = PromptBuilder(
            project_name=self.project_name,
            project_description=self.project_description,
            version_pair=version_pair if isinstance(version_pair, dict) else None,
            commit_messages=commit_messages,
            changed_files=changed_files,
            prompt_variant=self.prompt_variant,
        )
        system_prompt = prompt_builder.build_system_prompt()

        bundle_entries: list[dict[str, object]] = []
        for entry in self._list_of_dicts(prompt_input_payload.get("entries")):
            bundle_entries.append(
                {
                    "entry_id": entry.get("entry_id"),
                    "symbol": entry.get("symbol"),
                    "change_type": entry.get("change_type"),
                    "match_status": entry.get("match_status"),
                    "matched_entity_id": entry.get("matched_entity_id"),
                    "system_prompt": system_prompt,
                    "user_prompt": prompt_builder.build_user_prompt(entry),
                }
            )

        return {
            "source": {
                "builder": "prompt-bundle-builder-v4",
                "prompt_variant": self.prompt_variant,
            },
            "project": prompt_input_payload.get("project"),
            "version_pair": prompt_input_payload.get("version_pair"),
            "summary": prompt_input_payload.get("summary"),
            "entries": bundle_entries,
            "unmatched_symbols": prompt_input_payload.get("unmatched_symbols", []),
        }

    def _filtered_entries(self, cmg_payload: dict[str, object]) -> list[dict[str, object]]:
        entries = self._list_of_dicts(cmg_payload.get("entries"))
        if self.include_unmatched_entries:
            return entries
        return [entry for entry in entries if entry.get("matched_entity_id") is not None]

    def _build_version_pair(
        self,
        changed_payload: dict[str, object],
        cmg_payload: dict[str, object],
    ) -> dict[str, object]:
        raw = changed_payload.get("version_pair")
        if isinstance(raw, dict):
            return {
                "repo_path": raw.get("repo_path"),
                "ref": raw.get("ref") or raw.get("ref_version"),
                "tgt": raw.get("tgt") or raw.get("tgt_version"),
            }
        raw = cmg_payload.get("version_pair")
        if isinstance(raw, dict):
            return {
                "repo_path": None,
                "ref": raw.get("ref"),
                "tgt": raw.get("tgt"),
            }
        return {
            "repo_path": None,
            "ref": None,
            "tgt": None,
        }

    @staticmethod
    def _normalize_cmg(
        raw: object,
        *,
        include_fallback_context: bool = True,
    ) -> dict[str, object]:
        if not isinstance(raw, dict):
            return {"nodes": [], "edges": []}
        nodes = PromptBundleBuilder._list_of_dicts(raw.get("nodes"))
        edges = PromptBundleBuilder._list_of_dicts(raw.get("edges"))
        provenance = raw.get("provenance")

        if not include_fallback_context:
            kept_node_ids = {
                str(node.get("id"))
                for node in nodes
                if PromptBundleBuilder._is_enre_original_node(node)
            }
            nodes = [node for node in nodes if str(node.get("id")) in kept_node_ids]
            edges = [
                edge
                for edge in edges
                if str(edge.get("provenance", "")) != "diff-derived"
                and str(edge.get("source_id")) in kept_node_ids
                and str(edge.get("target_id")) in kept_node_ids
            ]
            normalized_provenance = dict(provenance) if isinstance(provenance, dict) else {}
            normalized_provenance["prompt_graph_filter"] = "enre_only_no_fallback"
            provenance = normalized_provenance

        return {
            "nodes": nodes,
            "edges": edges,
            "provenance": provenance if isinstance(provenance, dict) else {},
        }

    @staticmethod
    def _is_enre_original_node(node: dict[str, object]) -> bool:
        source = str(node.get("entity_source", "")).strip()
        return source in {"", "enre"}

    @staticmethod
    def _normalize_fallback_context(raw: object) -> dict[str, object]:
        if not isinstance(raw, dict):
            return {}
        return raw

    @staticmethod
    def _build_cmg_summary(raw: object) -> dict[str, object]:
        if not isinstance(raw, dict):
            return {
                "node_count": 0,
                "edge_count": 0,
                "user_defined_node_count": 0,
                "external_node_count": 0,
            }
        nodes = PromptBundleBuilder._list_of_dicts(raw.get("nodes"))
        edges = PromptBundleBuilder._list_of_dicts(raw.get("edges"))
        return {
            "node_count": len(nodes),
            "edge_count": len(edges),
            "synthetic_node_count": sum(
                1 for node in nodes if str(node.get("entity_source", "")).startswith("synthetic:")
            ),
            "diff_call_node_count": sum(
                1 for node in nodes if str(node.get("entity_source", "")).startswith("diff_call")
            ),
            "user_defined_node_count": sum(
                1 for node in nodes if bool(node.get("is_user_defined"))
            ),
            "external_node_count": sum(
                1 for node in nodes if not bool(node.get("is_user_defined"))
            ),
        }

    def _limited_commit_messages(self, changed_payload: dict[str, object]) -> list[str]:
        messages = self._list_text(changed_payload.get("commit_messages"))
        return messages[: self.max_commit_messages]

    @staticmethod
    def _list_text(raw: object) -> list[str]:
        if not isinstance(raw, list):
            return []
        return [str(item) for item in raw if str(item).strip()]

    @staticmethod
    def _list_of_dicts(raw: object) -> list[dict[str, Any]]:
        if not isinstance(raw, list):
            return []
        return [item for item in raw if isinstance(item, dict)]


def _normalize_prompt_variant(raw: str) -> str:
    value = str(raw or "full").strip().lower().replace("-", "_")
    if value not in SUPPORTED_PROMPT_VARIANTS:
        allowed = ", ".join(SUPPORTED_PROMPT_VARIANTS)
        raise ValueError(f"prompt variant must be one of: {allowed}.")
    return value

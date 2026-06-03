from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class GroundTruthEvidenceBuilder:
    """Build a review packet for evidence-driven ground-truth drafting."""

    def __init__(
        self,
        *,
        metadata_path: str | Path,
        max_functions: int = 80,
        max_diff_lines_per_function: int = 12,
    ) -> None:
        self.metadata_path = Path(metadata_path)
        self.case_root = self.metadata_path.parent
        self.max_functions = max_functions
        self.max_diff_lines_per_function = max_diff_lines_per_function

    def build_markdown(self) -> str:
        metadata = self._read_json(self.metadata_path)
        changed_payload = self._read_json_if_exists(
            self._resolve_repo_path(metadata.get("screening", {}).get("stage1_output"))
        )
        cmg_payload = self._read_json_if_exists(
            self._resolve_repo_path(metadata.get("pipeline_artifacts", {}).get("cmg_output"))
            or self._resolve_repo_path(metadata.get("pipeline_artifacts", {}).get("cmg"))
        )
        release_note_payload = self._read_json_if_exists(
            self._resolve_repo_path(metadata.get("pipeline_artifacts", {}).get("release_note_mock_rule_family"))
            or self._resolve_repo_path(metadata.get("pipeline_artifacts", {}).get("mock_release_note"))
        )

        lines: list[str] = []
        lines.extend(self._render_header(metadata))
        lines.extend(self._render_evidence_sources(metadata))
        lines.extend(self._render_artifacts(metadata))
        lines.extend(self._render_pipeline_summary(metadata, changed_payload, cmg_payload, release_note_payload))
        lines.extend(self._render_commit_messages(changed_payload))
        lines.extend(self._render_changed_files(changed_payload))
        lines.extend(self._render_changed_functions(changed_payload, cmg_payload))
        lines.extend(self._render_mock_notes(release_note_payload))
        lines.extend(self._render_ground_truth_workspace())
        return "\n".join(lines).rstrip() + "\n"

    def _render_header(self, metadata: dict[str, Any]) -> list[str]:
        repository = metadata.get("repository", {})
        version_pair = metadata.get("version_pair", {})
        title = (
            f"# Evidence Pack: {repository.get('name', 'unknown')} "
            f"{version_pair.get('ref', '?')} -> {version_pair.get('tgt', '?')}"
        )
        return [
            title,
            "",
            "This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.",
            "",
            "## Case Overview",
            "",
            f"- Case ID: `{metadata.get('case_id', 'unknown')}`",
            f"- Repository: `{repository.get('name', 'unknown')}`",
            f"- Category: `{repository.get('category', 'unknown')}`",
            f"- Reference version: `{version_pair.get('ref', '?')}`",
            f"- Target version: `{version_pair.get('tgt', '?')}`",
            f"- Pipeline status: `{metadata.get('pipeline_status', 'unknown')}`",
            f"- Ground-truth status: `{metadata.get('ground_truth', {}).get('status', 'unknown')}`",
            "",
        ]

    def _render_evidence_sources(self, metadata: dict[str, Any]) -> list[str]:
        sources = metadata.get("ground_truth", {}).get("evidence_sources", [])
        lines = ["## Evidence Sources To Inspect", ""]
        if not sources:
            lines.append("- No evidence sources recorded in metadata.")
        else:
            lines.extend(f"- [ ] {source}" for source in sources)
        lines.append("")
        return lines

    def _render_artifacts(self, metadata: dict[str, Any]) -> list[str]:
        lines = ["## Local Artifacts", ""]
        screening = metadata.get("screening", {})
        artifacts = metadata.get("pipeline_artifacts", {})
        stage1 = screening.get("stage1_output")
        if stage1:
            lines.append(f"- Changed functions: `{stage1}`")
        for name, path in artifacts.items():
            lines.append(f"- {name}: `{path}`")
        if len(lines) == 2:
            lines.append("- No local artifact paths recorded.")
        lines.append("")
        return lines

    def _render_pipeline_summary(
        self,
        metadata: dict[str, Any],
        changed_payload: dict[str, Any] | None,
        cmg_payload: dict[str, Any] | None,
        release_note_payload: dict[str, Any] | None,
    ) -> list[str]:
        screening = metadata.get("screening", {})
        stage2 = metadata.get("stage2", {})
        stage3 = metadata.get("stage3", {})
        changed_items = changed_payload.get("items", []) if changed_payload else []
        cmg_summary = cmg_payload.get("summary", {}) if cmg_payload else {}
        release_summary = release_note_payload.get("summary", {}) if release_note_payload else {}

        return [
            "## Pipeline Summary",
            "",
            f"- Commit count: `{screening.get('commit_count', 'unknown')}`",
            f"- Changed C/C++ files: `{screening.get('changed_cpp_files', len(changed_payload.get('changed_files', [])) if changed_payload else 'unknown')}`",
            f"- Changed functions: `{screening.get('changed_functions', len(changed_items))}`",
            f"- Patch only: `{screening.get('patch_only', 'unknown')}`",
            f"- CMG matched entries: `{stage2.get('matched_entries', cmg_summary.get('matched_entry_count', 'unknown'))}`",
            f"- CMG unmatched entries: `{stage2.get('unmatched_entries', cmg_summary.get('unmatched_entry_count', 'unknown'))}`",
            f"- Fallback-context entries: `{stage2.get('fallback_context_entries', cmg_summary.get('fallback_context_entry_count', 'unknown'))}`",
            f"- Diff-derived call edges: `{stage2.get('diff_call_edges', cmg_summary.get('diff_call_edge_count', 'unknown'))}`",
            f"- Prompt entries: `{stage3.get('prompt_entries', release_summary.get('entry_count', 'unknown'))}`",
            f"- Mock generated entries: `{stage3.get('mock_generated_entries', release_summary.get('generated_entry_count', 'unknown'))}`",
            "",
        ]

    def _render_commit_messages(self, changed_payload: dict[str, Any] | None) -> list[str]:
        lines = ["## Commit Messages", ""]
        commit_messages = changed_payload.get("commit_messages", []) if changed_payload else []
        if not commit_messages:
            lines.append("- No commit messages available in `changed_functions.json`.")
        else:
            lines.extend(f"- {message}" for message in commit_messages)
        lines.append("")
        return lines

    def _render_changed_files(self, changed_payload: dict[str, Any] | None) -> list[str]:
        lines = ["## Changed C/C++ Files", ""]
        changed_files = changed_payload.get("changed_files", []) if changed_payload else []
        if not changed_files:
            lines.append("- No changed C/C++ files recorded.")
        else:
            lines.extend(f"- `{path}`" for path in changed_files)
        lines.append("")
        return lines

    def _render_changed_functions(
        self,
        changed_payload: dict[str, Any] | None,
        cmg_payload: dict[str, Any] | None,
    ) -> list[str]:
        changed_items = changed_payload.get("items", []) if changed_payload else []
        cmg_entries = cmg_payload.get("entries", []) if cmg_payload else []
        lines = ["## Changed Function Evidence", ""]

        if not changed_items:
            lines.append("- No changed functions available.")
            lines.append("")
            return lines

        lines.extend(
            [
                "| # | Symbol | Type | File | Lines | Match | Evidence Notes |",
                "| ---: | --- | --- | --- | --- | --- | --- |",
            ]
        )
        for index, item in enumerate(changed_items[: self.max_functions], start=1):
            cmg_entry = cmg_entries[index - 1] if index - 1 < len(cmg_entries) else {}
            symbol = self._escape_table(str(item.get("symbol", "")))
            change_type = self._escape_table(str(item.get("change_type", "")))
            file_path = self._escape_table(str(item.get("file_path", "")))
            start_line = item.get("start_line", "")
            end_line = item.get("end_line", "")
            match_level = cmg_entry.get("match_level") or "unmatched"
            matched = "matched" if cmg_entry.get("matched_entity_id") is not None else "unmatched"
            fallback = cmg_entry.get("fallback_context", {}) if isinstance(cmg_entry, dict) else {}
            fallback_calls = len(fallback.get("diff_call_symbols", [])) if isinstance(fallback, dict) else 0
            diff_hunks = len(item.get("diff_hunks", []))
            notes = f"{matched}; level={match_level}; diff_hunks={diff_hunks}; fallback_calls={fallback_calls}"
            lines.append(
                f"| {index} | `{symbol}` | `{change_type}` | `{file_path}` | "
                f"`{start_line}-{end_line}` | `{matched}` | {self._escape_table(notes)} |"
            )

        if len(changed_items) > self.max_functions:
            lines.append(
                f"| ... | ... | ... | ... | ... | ... | truncated at {self.max_functions} of {len(changed_items)} functions |"
            )
        lines.append("")
        lines.extend(self._render_diff_snippets(changed_items[: self.max_functions]))
        return lines

    def _render_diff_snippets(self, changed_items: list[dict[str, Any]]) -> list[str]:
        lines = ["## Function-Level Diff Snippets", ""]
        for index, item in enumerate(changed_items, start=1):
            symbol = str(item.get("symbol", "unknown"))
            file_path = str(item.get("file_path", "unknown"))
            diff_lines = self._flatten_diff_lines(item.get("diff_hunks", []))
            lines.append(f"### {index}. `{symbol}` in `{file_path}`")
            lines.append("")
            if not diff_lines:
                lines.append("No function-level diff lines recorded.")
                lines.append("")
                continue
            shown = diff_lines[: self.max_diff_lines_per_function]
            lines.append("```diff")
            lines.extend(shown)
            if len(diff_lines) > len(shown):
                lines.append(f"... truncated {len(diff_lines) - len(shown)} additional diff lines ...")
            lines.append("```")
            lines.append("")
        return lines

    def _render_mock_notes(self, release_note_payload: dict[str, Any] | None) -> list[str]:
        lines = ["## Mock Release-Note Drafts", ""]
        if not release_note_payload:
            lines.append("- No mock release-note output available.")
            lines.append("")
            return lines

        notes = release_note_payload.get("aggregated_release_notes") or release_note_payload.get(
            "deduplicated_release_notes", []
        )
        if not notes:
            lines.append("- Mock backend generated no release-note drafts.")
        else:
            for index, note in enumerate(notes, start=1):
                section = note.get("section", "Unknown")
                title = note.get("title", "")
                summary = note.get("summary", note.get("text", ""))
                lines.append(f"{index}. [{section}] {title}: {summary}")
        lines.append("")
        lines.append("These drafts are generated evidence only. Do not copy them as ground truth without review.")
        lines.append("")
        return lines

    @staticmethod
    def _render_ground_truth_workspace() -> list[str]:
        return [
            "## Ground-Truth Drafting Workspace",
            "",
            "| GT ID | Section | Semantic Release-Note Entry | Supporting Evidence | Decision |",
            "| --- | --- | --- | --- | --- |",
            "| GT-001 |  |  |  | pending |",
            "",
            "## Excluded Or Low-Level Changes",
            "",
            "| Item | Reason For Exclusion | Evidence |",
            "| --- | --- | --- |",
            "|  |  |  |",
            "",
            "## Reviewer Notes",
            "",
            "- Record uncertainty, alternative interpretations, and final consensus here.",
            "",
        ]

    @staticmethod
    def _flatten_diff_lines(diff_hunks: list[dict[str, Any]]) -> list[str]:
        lines: list[str] = []
        for hunk in diff_hunks:
            lines.extend(str(line) for line in hunk.get("lines", []))
        return lines

    @staticmethod
    def _read_json(path: Path) -> dict[str, Any]:
        return json.loads(path.read_text(encoding="utf-8"))

    def _read_json_if_exists(self, path: Path | None) -> dict[str, Any] | None:
        if path is None or not path.exists():
            return None
        return self._read_json(path)

    def _resolve_repo_path(self, value: object) -> Path | None:
        if not value:
            return None
        raw = Path(str(value))
        if raw.is_absolute():
            return raw
        return self._repo_root() / raw

    def _repo_root(self) -> Path:
        current = self.metadata_path.resolve()
        for parent in [current.parent, *current.parents]:
            if (parent / "cpp_release_note_mvp").exists() and (parent / "PROJECT_CONTEXT.md").exists():
                return parent
        return Path.cwd()

    @staticmethod
    def _escape_table(value: str) -> str:
        return value.replace("|", "\\|").replace("\n", " ")

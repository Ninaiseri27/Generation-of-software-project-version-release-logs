from __future__ import annotations

import html
import json
import shutil
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class DemoCase:
    case_id: str
    project_name: str
    ref_version: str
    tgt_version: str
    config_path: Path
    output_root: Path
    release_note_json: Path
    release_note_markdown: Path


DEFAULT_SQLITE_CASE = DemoCase(
    case_id="sqlite_v6_0_0_2_to_v6_1",
    project_name="third_party_sqlite",
    ref_version="OpenHarmony-v6.0.0.2-Release",
    tgt_version="OpenHarmony-v6.1-Release",
    config_path=Path("configs/benchmark/third_party_sqlite_v6_0_0_2_to_v6_1.json"),
    output_root=Path(
        "outputs/benchmark/third_party_sqlite/"
        "OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release"
    ),
    release_note_json=Path(
        "outputs/benchmark/third_party_sqlite/"
        "OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/"
        "baselines_deepseek_v4_flash/full/release_note.json"
    ),
    release_note_markdown=Path(
        "outputs/benchmark/third_party_sqlite/"
        "OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/"
        "baselines_deepseek_v4_flash/full/release_note.md"
    ),
)


class DemoReportBuilder:
    """Build a stable browser demo from cached pipeline artifacts."""

    def __init__(
        self,
        *,
        case: str = "sqlite",
        mode: str = "cached",
        output_dir: str | Path = "outputs/demo/sqlite_demo",
        benchmark_root: str | Path = "benchmark",
        source_root: str | Path = ".",
        demo_case: DemoCase | None = None,
    ) -> None:
        if mode != "cached":
            raise ValueError("Only cached demo mode is implemented. Use --mode cached.")
        if case != "sqlite" and demo_case is None:
            raise ValueError("Only the sqlite cached demo case is bundled by default.")

        self.case = case
        self.mode = mode
        self.output_dir = Path(output_dir)
        self.benchmark_root = self._resolve(Path(source_root), Path(benchmark_root))
        self.source_root = Path(source_root)
        self.demo_case = demo_case or DEFAULT_SQLITE_CASE

    def build(self) -> dict[str, object]:
        case = self.demo_case
        output_dir = self.output_dir
        artifact_dir = output_dir / "artifacts"
        artifact_dir.mkdir(parents=True, exist_ok=True)

        paths = self._artifact_paths(case)
        copied_artifacts = self._copy_artifacts(paths, artifact_dir)

        changed_payload = self._read_json(paths["changed_functions"])
        cmg_payload = self._read_json(paths["cmg"])
        prompt_payload = self._read_json(paths["prompt_bundle"])
        release_payload = self._read_json(paths["release_note_json"])
        matrix_payload = self._read_json(self.benchmark_root / "core5_experiment_matrix.json")
        coverage_payload = self._read_json(self.benchmark_root / "cmg_coverage_core5.json")

        payload = {
            "source": {
                "builder": "demo-report-builder-v1",
                "mode": self.mode,
                "generated_at": datetime.now().isoformat(timespec="seconds"),
            },
            "case": {
                "case_id": case.case_id,
                "project_name": case.project_name,
                "ref_version": case.ref_version,
                "tgt_version": case.tgt_version,
            },
            "artifacts": copied_artifacts,
            "stage1": self._summarize_changed_functions(changed_payload),
            "stage2": self._summarize_cmg(cmg_payload, coverage_payload, case.case_id),
            "stage3": self._summarize_prompt_and_generation(prompt_payload, release_payload),
            "experiment": self._summarize_experiment(matrix_payload, coverage_payload),
        }

        payload_path = output_dir / "demo_payload.json"
        payload_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        (output_dir / "run_log.md").write_text(self.render_run_log(payload), encoding="utf-8")
        (output_dir / "index.html").write_text(self.render_html(payload), encoding="utf-8")
        return payload

    def render_run_log(self, payload: dict[str, object]) -> str:
        source = payload.get("source") if isinstance(payload.get("source"), dict) else {}
        case = payload.get("case") if isinstance(payload.get("case"), dict) else {}
        stage1 = payload.get("stage1") if isinstance(payload.get("stage1"), dict) else {}
        stage2 = payload.get("stage2") if isinstance(payload.get("stage2"), dict) else {}
        stage3 = payload.get("stage3") if isinstance(payload.get("stage3"), dict) else {}
        return "\n".join(
            [
                "# Cached Demo Run Log",
                "",
                f"- Generated at: {source.get('generated_at', '')}",
                f"- Mode: {source.get('mode', 'cached')}",
                f"- Case: {case.get('case_id', '')}",
                f"- Version pair: {case.get('ref_version', '')} -> {case.get('tgt_version', '')}",
                f"- Changed functions: {stage1.get('changed_function_count', 0)}",
                f"- CMG matches: {stage2.get('matched_entry_count', 0)}/{stage2.get('entry_count', 0)}",
                f"- Generated entries: {stage3.get('generated_entry_count', 0)}",
                f"- Final release-note entries: {stage3.get('final_note_count', 0)}",
                "",
                "## Reproduce This Demo",
                "",
                "```powershell",
                (
                    ".\\cpp_release_note_mvp\\.venv\\Scripts\\python.exe -m cpp_release_note_mvp "
                    "build-demo --case sqlite --output cpp_release_note_mvp\\outputs\\demo\\sqlite_demo"
                ),
                "```",
                "",
                "This demo is generated from cached artifacts. It does not rerun Git diff, ENRE, or LLM calls.",
            ]
        )

    def render_html(self, payload: dict[str, object]) -> str:
        case = payload.get("case") if isinstance(payload.get("case"), dict) else {}
        stage1 = payload.get("stage1") if isinstance(payload.get("stage1"), dict) else {}
        stage2 = payload.get("stage2") if isinstance(payload.get("stage2"), dict) else {}
        stage3 = payload.get("stage3") if isinstance(payload.get("stage3"), dict) else {}
        experiment = payload.get("experiment") if isinstance(payload.get("experiment"), dict) else {}
        artifacts = payload.get("artifacts") if isinstance(payload.get("artifacts"), dict) else {}

        title = "C/C++ Release Note Generation Demo"
        return "\n".join(
            [
                "<!doctype html>",
                '<html lang="en">',
                "<head>",
                '<meta charset="utf-8">',
                '<meta name="viewport" content="width=device-width, initial-scale=1">',
                f"<title>{title}</title>",
                "<style>",
                self._style(),
                "</style>",
                "</head>",
                "<body>",
                "<main>",
                f"<h1>{title}</h1>",
                '<p class="lead">A cached, advisor-facing walkthrough of the prototype pipeline and experiment evidence.</p>',
                self._render_cards(case, stage1, stage2, stage3, experiment),
                self._render_pipeline(),
                self._render_artifacts(artifacts),
                self._render_stage1(stage1),
                self._render_stage2(stage2),
                self._render_stage3(stage3),
                self._render_experiment(experiment),
                "</main>",
                "</body>",
                "</html>",
            ]
        )

    def _artifact_paths(self, case: DemoCase) -> dict[str, Path]:
        return {
            "config": self._resolve(self.source_root, case.config_path),
            "changed_functions": self._resolve(self.source_root, case.output_root / "changed_functions.json"),
            "cmg": self._resolve(self.source_root, case.output_root / "cmg.json"),
            "prompt_bundle": self._resolve(self.source_root, case.output_root / "prompt_bundle.json"),
            "prompt_input": self._resolve(self.source_root, case.output_root / "prompt_input.json"),
            "release_note_json": self._resolve(self.source_root, case.release_note_json),
            "release_note_markdown": self._resolve(self.source_root, case.release_note_markdown),
        }

    def _copy_artifacts(self, paths: dict[str, Path], artifact_dir: Path) -> dict[str, str]:
        copied: dict[str, str] = {}
        name_map = {
            "config": "config.json",
            "changed_functions": "changed_functions.json",
            "cmg": "cmg.json",
            "prompt_bundle": "prompt_bundle.json",
            "prompt_input": "prompt_input.json",
            "release_note_json": "release_note.json",
            "release_note_markdown": "release_note.md",
        }
        for key, source_path in paths.items():
            target = artifact_dir / name_map[key]
            if source_path.exists():
                shutil.copy2(source_path, target)
                copied[key] = self._html_path(target.relative_to(self.output_dir))
            else:
                copied[key] = f"missing: {source_path}"
        return copied

    def _summarize_changed_functions(self, payload: dict[str, object]) -> dict[str, object]:
        items = self._list_of_dicts(payload.get("items"))
        changed_files = payload.get("changed_files") if isinstance(payload.get("changed_files"), list) else []
        commit_messages = payload.get("commit_messages") if isinstance(payload.get("commit_messages"), list) else []
        sample_items = []
        for item in items[:8]:
            sample_items.append(
                {
                    "symbol": item.get("symbol"),
                    "file_path": item.get("file_path"),
                    "change_type": item.get("change_type"),
                    "line_range": self._line_range(item),
                }
            )
        return {
            "changed_function_count": len(items),
            "changed_file_count": len(changed_files),
            "changed_files": changed_files[:12],
            "commit_message_count": len(commit_messages),
            "commit_messages": commit_messages[:10],
            "sample_items": sample_items,
            "diff_sample": self._build_diff_sample(items),
        }

    def _summarize_cmg(
        self,
        cmg_payload: dict[str, object],
        coverage_payload: dict[str, object],
        case_id: str,
    ) -> dict[str, object]:
        summary = cmg_payload.get("summary") if isinstance(cmg_payload.get("summary"), dict) else {}
        entries = self._list_of_dicts(cmg_payload.get("entries"))
        matched_entries = [entry for entry in entries if entry.get("matched_entity_id") is not None]
        sample_entry = self._pick_cmg_sample(matched_entries or entries)
        case_coverage = self._coverage_for_case(coverage_payload, case_id)
        return {
            "entry_count": self._int(summary.get("entry_count"), len(entries)),
            "matched_entry_count": self._int(summary.get("matched_entry_count"), len(matched_entries)),
            "unmatched_entry_count": self._int(
                summary.get("unmatched_entry_count"),
                len(entries) - len(matched_entries),
            ),
            "fallback_context_entry_count": self._int(summary.get("fallback_context_entry_count"), 0),
            "diff_call_edge_count": self._int(summary.get("diff_call_edge_count"), 0),
            "case_coverage": case_coverage,
            "sample": sample_entry,
        }

    def _summarize_prompt_and_generation(
        self,
        prompt_payload: dict[str, object],
        release_payload: dict[str, object],
    ) -> dict[str, object]:
        prompt_entries = self._list_of_dicts(prompt_payload.get("entries"))
        release_summary = release_payload.get("summary") if isinstance(release_payload.get("summary"), dict) else {}
        final_notes = self._list_of_dicts(release_payload.get("aggregated_release_notes"))
        if not final_notes:
            final_notes = self._list_of_dicts(release_payload.get("structured_release_notes"))
        prompt_sample = ""
        if prompt_entries:
            prompt_sample = self._prompt_excerpt(str(prompt_entries[0].get("user_prompt", "")))
        return {
            "prompt_entry_count": len(prompt_entries),
            "prompt_sample": prompt_sample,
            "entry_count": self._int(release_summary.get("entry_count"), len(prompt_entries)),
            "generated_entry_count": self._int(release_summary.get("generated_entry_count"), 0),
            "failed_entry_count": self._int(release_summary.get("failed_entry_count"), 0),
            "aggregation_strategy": release_summary.get("aggregation_strategy"),
            "final_note_count": self._int(
                release_summary.get("deduplicated_release_note_count"),
                len(final_notes),
            ),
            "sample_release_notes": final_notes[:8],
        }

    def _summarize_experiment(
        self,
        matrix_payload: dict[str, object],
        coverage_payload: dict[str, object],
    ) -> dict[str, object]:
        rows = self._list_of_dicts(matrix_payload.get("rows"))
        highlighted = [
            row
            for row in rows
            if row.get("method_id")
            in {
                "diff_only",
                "full_adaptive_rule_family",
                "full_strict_1hop",
                "full_similarity_family",
                "full_evidence_similarity_family",
            }
        ]
        coverage_rows = self._list_of_dicts(coverage_payload.get("rows"))
        return {
            "rows": highlighted or rows,
            "interpretation": matrix_payload.get("interpretation", {}),
            "coverage_totals": self._coverage_totals(coverage_rows),
            "coverage_interpretation": coverage_payload.get("interpretation", []),
        }

    def _pick_cmg_sample(self, entries: list[dict[str, object]]) -> dict[str, object]:
        if not entries:
            return {}
        selected = entries[0]
        for entry in entries:
            cmg = entry.get("cmg") if isinstance(entry.get("cmg"), dict) else {}
            if self._list_of_dicts(cmg.get("edges")):
                selected = entry
                break
        cmg = selected.get("cmg") if isinstance(selected.get("cmg"), dict) else {}
        nodes = self._list_of_dicts(cmg.get("nodes"))[:12]
        edges = self._list_of_dicts(cmg.get("edges"))[:16]
        node_labels = {
            node.get("id"): self._short_symbol(
                str(node.get("qualified_name") or node.get("name") or node.get("id", ""))
            )
            for node in nodes
        }
        return {
            "symbol": selected.get("symbol"),
            "file_path": selected.get("file_path"),
            "match_level": selected.get("match_level"),
            "matched_entity_id": selected.get("matched_entity_id"),
            "node_count": len(self._list_of_dicts(cmg.get("nodes"))),
            "edge_count": len(self._list_of_dicts(cmg.get("edges"))),
            "nodes": [
                {
                    "id": node.get("id"),
                    "label": node_labels.get(node.get("id")),
                    "file_path": node.get("file_path"),
                    "origin": node.get("origin") or node.get("source") or node.get("raw_kind"),
                }
                for node in nodes
            ],
            "edges": [
                {
                    "source": node_labels.get(edge.get("source_id"), str(edge.get("source_id"))),
                    "target": node_labels.get(edge.get("target_id"), str(edge.get("target_id"))),
                    "type": edge.get("type", "call"),
                }
                for edge in edges
            ],
        }

    def _build_diff_sample(self, items: list[dict[str, object]]) -> dict[str, object]:
        for item in items:
            hunks = self._list_of_dicts(item.get("diff_hunks"))
            if hunks:
                lines = hunks[0].get("lines") if isinstance(hunks[0].get("lines"), list) else []
                return {
                    "symbol": item.get("symbol"),
                    "file_path": item.get("file_path"),
                    "lines": lines[:20],
                }
        return {}

    @staticmethod
    def _prompt_excerpt(text: str) -> str:
        if not text:
            return ""
        marker = "Graph and Fallback Context"
        index = text.find(marker)
        if index >= 0:
            return text[index : index + 1400]
        return text[:1400]

    @staticmethod
    def _coverage_for_case(payload: dict[str, object], case_id: str) -> dict[str, object]:
        rows = payload.get("rows") if isinstance(payload.get("rows"), list) else []
        for row in rows:
            if isinstance(row, dict) and row.get("case_id") == case_id:
                return row
        return {}

    @staticmethod
    def _coverage_totals(rows: list[dict[str, object]]) -> dict[str, int]:
        keys = [
            "entry_count",
            "compact_prompt_matches",
            "rich_prompt_matches",
            "projected_prompt_matches",
            "matching_graph_hits",
        ]
        return {key: sum(DemoReportBuilder._int(row.get(key), 0) for row in rows) for key in keys}

    @staticmethod
    def _render_cards(
        case: dict[str, object],
        stage1: dict[str, object],
        stage2: dict[str, object],
        stage3: dict[str, object],
        experiment: dict[str, object],
    ) -> str:
        rows = DemoReportBuilder._list_of_dicts(experiment.get("rows"))
        diff_row = next((row for row in rows if row.get("method_id") == "diff_only"), {})
        cards = [
            ("Case", case.get("case_id", "")),
            ("Version Pair", f"{case.get('ref_version', '')} -> {case.get('tgt_version', '')}"),
            ("Changed Functions", stage1.get("changed_function_count", 0)),
            ("CMG Matches", f"{stage2.get('matched_entry_count', 0)}/{stage2.get('entry_count', 0)}"),
            ("Final Notes", stage3.get("final_note_count", 0)),
            ("Best Baseline F1", DemoReportBuilder._fmt(diff_row.get("f1"))),
        ]
        return '<div class="cards">' + "".join(
            '<div class="card">'
            f'<div class="label">{html.escape(str(label))}</div>'
            f'<div class="value">{html.escape(str(value))}</div>'
            "</div>"
            for label, value in cards
        ) + "</div>"

    @staticmethod
    def _render_pipeline() -> str:
        steps = [
            ("Stage 1", "Git unified diff and function-level changed-symbol localization."),
            ("Stage 2", "ENRE call graph normalization, CMG slicing, and fallback context construction."),
            ("Stage 3", "Prompt bundle construction, LLM generation, aggregation, and evaluation."),
        ]
        return (
            "<section><h2>Pipeline Walkthrough</h2><div class=\"pipeline\">"
            + "".join(
                '<div class="step">'
                f"<strong>{html.escape(title)}</strong>"
                f"<p>{html.escape(text)}</p>"
                "</div>"
                for title, text in steps
            )
            + "</div></section>"
        )

    @staticmethod
    def _render_artifacts(artifacts: dict[str, object]) -> str:
        rows = []
        for key, value in artifacts.items():
            value_str = str(value)
            if not value_str.startswith("missing:"):
                value_html = f'<a href="{html.escape(value_str)}">{html.escape(value_str)}</a>'
            else:
                value_html = html.escape(value_str)
            rows.append(f"<tr><td>{html.escape(key)}</td><td>{value_html}</td></tr>")
        return (
            "<section><h2>Packaged Artifacts</h2>"
            "<table><thead><tr><th>Artifact</th><th>Local Link</th></tr></thead><tbody>"
            + "".join(rows)
            + "</tbody></table></section>"
        )

    @staticmethod
    def _render_stage1(stage1: dict[str, object]) -> str:
        sample_rows = []
        for item in DemoReportBuilder._list_of_dicts(stage1.get("sample_items")):
            sample_rows.append(
                "<tr>"
                f"<td>{html.escape(str(item.get('symbol', '')))}</td>"
                f"<td>{html.escape(str(item.get('file_path', '')))}</td>"
                f"<td>{html.escape(str(item.get('change_type', '')))}</td>"
                f"<td>{html.escape(str(item.get('line_range', '')))}</td>"
                "</tr>"
            )
        diff_sample = stage1.get("diff_sample") if isinstance(stage1.get("diff_sample"), dict) else {}
        diff_lines = diff_sample.get("lines") if isinstance(diff_sample.get("lines"), list) else []
        return (
            "<section><h2>Stage 1: Function-Level Change Localization</h2>"
            f"<p>{stage1.get('changed_function_count', 0)} changed functions across "
            f"{stage1.get('changed_file_count', 0)} files. Commit messages observed: "
            f"{stage1.get('commit_message_count', 0)}.</p>"
            "<table><thead><tr><th>Symbol</th><th>File</th><th>Type</th><th>Lines</th></tr></thead><tbody>"
            + "".join(sample_rows)
            + "</tbody></table>"
            f"<h3>Unified Diff Sample: {html.escape(str(diff_sample.get('symbol', '')))}</h3>"
            f"<pre>{html.escape(chr(10).join(str(line) for line in diff_lines))}</pre>"
            "</section>"
        )

    @staticmethod
    def _render_stage2(stage2: dict[str, object]) -> str:
        sample = stage2.get("sample") if isinstance(stage2.get("sample"), dict) else {}
        coverage = stage2.get("case_coverage") if isinstance(stage2.get("case_coverage"), dict) else {}
        node_tags = "".join(
            f'<span class="node">{html.escape(str(node.get("label", "")))}</span>'
            for node in DemoReportBuilder._list_of_dicts(sample.get("nodes"))
        )
        edge_rows = "".join(
            "<tr>"
            f"<td>{html.escape(str(edge.get('source', '')))}</td>"
            f"<td>{html.escape(str(edge.get('type', 'call')))}</td>"
            f"<td>{html.escape(str(edge.get('target', '')))}</td>"
            "</tr>"
            for edge in DemoReportBuilder._list_of_dicts(sample.get("edges"))
        )
        coverage_text = (
            f"Compact: {coverage.get('compact_prompt_matches', 'n/a')}/{coverage.get('entry_count', 'n/a')}; "
            f"Rich: {coverage.get('rich_prompt_matches', 'n/a')}/{coverage.get('entry_count', 'n/a')}; "
            f"Projected: {coverage.get('projected_prompt_matches', 'n/a')}/{coverage.get('entry_count', 'n/a')}."
        )
        return (
            "<section><h2>Stage 2: ENRE Call Graph and CMG Construction</h2>"
            f"<p>Matched {stage2.get('matched_entry_count', 0)} of {stage2.get('entry_count', 0)} entries; "
            f"fallback context exists for {stage2.get('fallback_context_entry_count', 0)} entries. "
            f"{html.escape(coverage_text)}</p>"
            f"<h3>CMG Sample: {html.escape(str(sample.get('symbol', '')))}</h3>"
            f"<p>Match level: {html.escape(str(sample.get('match_level', '')))}; "
            f"nodes: {sample.get('node_count', 0)}; edges: {sample.get('edge_count', 0)}.</p>"
            f"<div>{node_tags}</div>"
            "<table><thead><tr><th>Source</th><th>Relation</th><th>Target</th></tr></thead><tbody>"
            + edge_rows
            + "</tbody></table></section>"
        )

    @staticmethod
    def _render_stage3(stage3: dict[str, object]) -> str:
        notes = []
        for note in DemoReportBuilder._list_of_dicts(stage3.get("sample_release_notes")):
            section = html.escape(str(note.get("section", "")))
            title = html.escape(str(note.get("title", "")))
            summary = html.escape(str(note.get("summary", "")))
            notes.append(f"<li><strong>[{section}] {title}</strong>: {summary}</li>")
        return (
            "<section><h2>Stage 3: Prompting and Structured Release Notes</h2>"
            f"<p>Prompt entries: {stage3.get('prompt_entry_count', 0)}; generated: "
            f"{stage3.get('generated_entry_count', 0)}; failed: {stage3.get('failed_entry_count', 0)}; "
            f"aggregation: {html.escape(str(stage3.get('aggregation_strategy', '')))}.</p>"
            "<h3>Prompt Context Excerpt</h3>"
            f"<pre>{html.escape(str(stage3.get('prompt_sample', '')))}</pre>"
            "<h3>Generated Release-Note Samples</h3>"
            "<ol>"
            + "".join(notes)
            + "</ol></section>"
        )

    @staticmethod
    def _render_experiment(experiment: dict[str, object]) -> str:
        rows = DemoReportBuilder._list_of_dicts(experiment.get("rows"))
        table_rows = []
        for row in rows:
            table_rows.append(
                "<tr>"
                f"<td>{html.escape(str(row.get('method_id', '')))}</td>"
                f"<td>{DemoReportBuilder._fmt(row.get('precision'))}</td>"
                f"<td>{DemoReportBuilder._fmt(row.get('recall'))}</td>"
                f"<td>{DemoReportBuilder._fmt(row.get('f1'))}</td>"
                f"<td>{DemoReportBuilder._fmt(row.get('micro_f1'))}</td>"
                f"<td>{DemoReportBuilder._fmt(row.get('micro_redundancy_per_gt'))}</td>"
                f"<td>{DemoReportBuilder._fmt(row.get('avg_reduction_rate'))}</td>"
                "</tr>"
            )
        totals = experiment.get("coverage_totals") if isinstance(experiment.get("coverage_totals"), dict) else {}
        return (
            "<section><h2>Experiment Evidence</h2>"
            "<table><thead><tr><th>Method</th><th>P</th><th>R</th><th>Macro F1</th>"
            "<th>Micro F1</th><th>Extra/GT</th><th>Reduction</th></tr></thead><tbody>"
            + "".join(table_rows)
            + "</tbody></table>"
            "<h3>Core5 CMG Coverage Totals</h3>"
            f"<p>Compact {totals.get('compact_prompt_matches', 0)}/{totals.get('entry_count', 0)}, "
            f"rich {totals.get('rich_prompt_matches', 0)}/{totals.get('entry_count', 0)}, "
            f"projected {totals.get('projected_prompt_matches', 0)}/{totals.get('entry_count', 0)}, "
            f"matching graph hits {totals.get('matching_graph_hits', 0)}/{totals.get('entry_count', 0)}.</p>"
            "</section>"
        )

    @staticmethod
    def _style() -> str:
        return """
:root {
  --bg: #f4efe6;
  --paper: #fffaf2;
  --ink: #1f2328;
  --muted: #6b6259;
  --line: #d8cdbc;
  --accent: #145c52;
  --accent-2: #a64623;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: linear-gradient(135deg, #f8f1e3 0%, #edf2ed 100%);
  color: var(--ink);
  font-family: "Segoe UI", "Microsoft YaHei", sans-serif;
}
main { max-width: 1180px; margin: 0 auto; padding: 34px 28px 72px; }
h1 { margin: 0; font-size: 34px; letter-spacing: -0.02em; }
h2 { margin: 0 0 14px; font-size: 22px; }
h3 { margin: 18px 0 10px; font-size: 16px; }
.lead { color: var(--muted); margin: 8px 0 22px; }
.cards, .pipeline { display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 12px; }
.card, section, .step {
  background: rgba(255, 250, 242, 0.95);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 14px 34px rgba(52, 41, 27, 0.08);
}
.card { padding: 16px; }
.label { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.08em; }
.value { margin-top: 7px; font-size: 20px; font-weight: 700; }
section { margin-top: 18px; padding: 20px; }
.step { padding: 14px; box-shadow: none; }
.step p { margin: 7px 0 0; color: var(--muted); line-height: 1.45; }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td { border-bottom: 1px solid var(--line); padding: 9px 8px; text-align: left; vertical-align: top; }
th { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
pre {
  overflow: auto;
  max-height: 420px;
  margin: 0;
  padding: 14px;
  border-radius: 14px;
  background: #1f2328;
  color: #f2f5f7;
  font-size: 13px;
  line-height: 1.45;
}
a { color: var(--accent); }
.node {
  display: inline-block;
  margin: 4px 5px 4px 0;
  padding: 7px 10px;
  border-radius: 999px;
  border: 1px solid var(--line);
  background: #fffdf8;
  font-size: 13px;
}
ol { padding-left: 22px; }
li { margin: 8px 0; line-height: 1.5; }
""".strip()

    @staticmethod
    def _resolve(root: Path, path: Path) -> Path:
        if path.is_absolute():
            return path
        return root / path

    @staticmethod
    def _read_json(path: Path) -> dict[str, object]:
        if not path.exists():
            return {}
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(payload, dict):
            return {}
        return payload

    @staticmethod
    def _list_of_dicts(value: object) -> list[dict[str, object]]:
        if not isinstance(value, list):
            return []
        return [item for item in value if isinstance(item, dict)]

    @staticmethod
    def _line_range(item: dict[str, object]) -> str:
        start = item.get("start_line")
        end = item.get("end_line")
        if start is None and end is None:
            return ""
        if start == end or end is None:
            return str(start)
        return f"{start}-{end}"

    @staticmethod
    def _short_symbol(value: str, max_length: int = 72) -> str:
        if "::" in value:
            value = value.split("::")[-1]
        if len(value) <= max_length:
            return value
        return "..." + value[-max_length + 3 :]

    @staticmethod
    def _fmt(value: object, digits: int = 4) -> str:
        try:
            return f"{float(value):.{digits}f}"
        except (TypeError, ValueError):
            return "n/a"

    @staticmethod
    def _int(value: object, default: int = 0) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return default

    @staticmethod
    def _html_path(path: Path) -> str:
        return path.as_posix()

from __future__ import annotations

import html
import json
from pathlib import Path
from typing import Any


class VisualReportBuilder:
    """Build a self-contained HTML report from existing benchmark artifacts."""

    def __init__(
        self,
        *,
        benchmark_root: str | Path = "benchmark",
        title: str = "C/C++ Release Note Generation Experiment Report",
        matrix_input: str | Path | None = None,
        cmg_input: str | Path | None = None,
        cmg_coverage_input: str | Path | None = None,
    ) -> None:
        self.benchmark_root = Path(benchmark_root)
        self.title = title
        self.matrix_input = Path(matrix_input) if matrix_input else None
        self.cmg_input = Path(cmg_input) if cmg_input else None
        self.cmg_coverage_input = Path(cmg_coverage_input) if cmg_coverage_input else None

    def build_payload(self) -> dict[str, object]:
        explicit_matrix = self._read_json(self.matrix_input) if self.matrix_input else {}
        final_matrix = self._read_json(self.benchmark_root / "final_all_variant_matrix.json")
        matrix = self._read_json(self.benchmark_root / "core5_experiment_matrix.json")
        per_case = self._read_json(self.benchmark_root / "core5_per_case_results.json")
        cmg_payload = self._read_json(self.cmg_input) if self.cmg_input else {}

        expanded_comparison_rows: list[dict[str, object]] = []
        if self._is_expanded_matrix(explicit_matrix):
            matrix_rows = self._normalize_expanded_matrix_rows(explicit_matrix)
            expanded_comparison_rows = self._normalize_expanded_comparison_rows(explicit_matrix)
            per_case_rows = self._list_of_dicts(explicit_matrix.get("per_case_rows"))
            medium_rows = []
            interpretation = self._expanded_matrix_interpretation(matrix_rows, explicit_matrix)
            thesis_interpretation = self._expanded_matrix_thesis_notes()
            validity_threats = self._expanded_matrix_validity_notes()
            matrix_source = str(self.matrix_input)
        elif self._list_of_dicts(explicit_matrix.get("macro_micro_by_method")):
            matrix_rows = self._normalize_final_matrix_rows(explicit_matrix)
            per_case_rows = self._list_of_dicts(explicit_matrix.get("per_case_rows"))
            medium_rows = []
            interpretation = self._final_matrix_interpretation(matrix_rows, explicit_matrix)
            thesis_interpretation = self._final_matrix_thesis_notes()
            validity_threats = self._final_matrix_validity_notes()
            matrix_source = str(self.matrix_input)
        elif self._list_of_dicts(final_matrix.get("macro_micro_by_method")):
            matrix_rows = self._normalize_final_matrix_rows(final_matrix)
            per_case_rows = self._list_of_dicts(final_matrix.get("per_case_rows"))
            medium_rows = []
            interpretation = self._final_matrix_interpretation(matrix_rows, final_matrix)
            thesis_interpretation = self._final_matrix_thesis_notes()
            validity_threats = self._final_matrix_validity_notes()
            matrix_source = "final_all_variant_matrix.json"
        else:
            matrix_rows = self._list_of_dicts(matrix.get("rows"))
            per_case_rows = self._list_of_dicts(per_case.get("rows"))
            medium_rows = self._list_of_dicts(per_case.get("medium_case_macro"))
            interpretation = matrix.get("interpretation", {})
            per_case_interpretation = (
                per_case.get("interpretation") if isinstance(per_case.get("interpretation"), dict) else {}
            )
            thesis_interpretation = per_case_interpretation.get("result_narrative", [])
            validity_threats = per_case_interpretation.get("validity_threats", [])
            matrix_source = "core5_experiment_matrix.json"
        cmg_summary = self._build_cmg_summary(cmg_payload)
        cmg_coverage = self._read_json(self.cmg_coverage_input) if self.cmg_coverage_input else {}

        return {
            "source": {
                "builder": "visual-report-builder-v1",
                "benchmark_root": str(self.benchmark_root),
                "matrix_source": matrix_source,
                "matrix_input": str(self.matrix_input) if self.matrix_input else None,
                "cmg_input": str(self.cmg_input) if self.cmg_input else None,
                "cmg_coverage_input": str(self.cmg_coverage_input) if self.cmg_coverage_input else None,
            },
            "title": self.title,
            "interpretation": interpretation,
            "matrix_rows": matrix_rows,
            "expanded_comparison_rows": expanded_comparison_rows,
            "per_case_rows": per_case_rows,
            "medium_case_rows": medium_rows,
            "thesis_interpretation": thesis_interpretation,
            "validity_threats": validity_threats,
            "cmg_summary": cmg_summary,
            "cmg_coverage_rows": self._list_of_dicts(cmg_coverage.get("rows")),
            "cmg_coverage_interpretation": cmg_coverage.get("interpretation", []),
        }

    def render_html(self, payload: dict[str, object]) -> str:
        title = html.escape(str(payload.get("title", self.title)))
        matrix_rows = self._list_of_dicts(payload.get("matrix_rows"))
        expanded_comparison_rows = self._list_of_dicts(payload.get("expanded_comparison_rows"))
        medium_rows = self._list_of_dicts(payload.get("medium_case_rows"))
        cmg_coverage_rows = self._list_of_dicts(payload.get("cmg_coverage_rows"))
        cmg_summary = payload.get("cmg_summary") if isinstance(payload.get("cmg_summary"), dict) else {}
        interpretation = payload.get("interpretation") if isinstance(payload.get("interpretation"), dict) else {}

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
                self._render_cards(interpretation, matrix_rows, cmg_summary),
                self._render_pipeline(),
                self._render_bar_section("Macro F1", matrix_rows, "f1", max_value=1.0),
                self._render_bar_section("Extra Matches Per GT", matrix_rows, "micro_redundancy_per_gt"),
                self._render_token_section(matrix_rows),
                self._render_matrix_table(matrix_rows),
                self._render_expanded_comparison_table(expanded_comparison_rows),
                self._render_medium_table(medium_rows),
                self._render_cmg_coverage(cmg_coverage_rows, payload.get("cmg_coverage_interpretation")),
                self._render_cmg(cmg_summary),
                self._render_bullets("Thesis Interpretation", payload.get("thesis_interpretation")),
                self._render_bullets("Validity Threats", payload.get("validity_threats")),
                "</main>",
                "</body>",
                "</html>",
            ]
        )

    @staticmethod
    def _style() -> str:
        return """
:root {
  --bg: #f7f1e6;
  --ink: #211b15;
  --muted: #6f6559;
  --card: #fffaf0;
  --line: #d9cdbb;
  --accent: #0f6b5f;
  --accent-2: #b65f2a;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: radial-gradient(circle at 20% 0%, #fff6dc 0, transparent 36rem), var(--bg);
  color: var(--ink);
  font-family: Georgia, "Times New Roman", serif;
}
main { max-width: 1180px; margin: 0 auto; padding: 36px 28px 64px; }
h1 { font-size: 34px; margin: 0 0 24px; letter-spacing: -0.02em; }
h2 { font-size: 22px; margin: 32px 0 14px; }
.grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(210px, 1fr)); gap: 14px; }
.card, section {
  background: rgba(255, 250, 240, 0.92);
  border: 1px solid var(--line);
  border-radius: 18px;
  box-shadow: 0 12px 28px rgba(63, 48, 31, 0.08);
}
.card { padding: 16px; }
.label { color: var(--muted); font-size: 13px; text-transform: uppercase; letter-spacing: 0.08em; }
.value { margin-top: 8px; font-size: 22px; font-weight: 700; }
section { padding: 18px; margin-top: 18px; }
.pipeline { display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 10px; }
.step { border: 1px dashed var(--line); border-radius: 14px; padding: 12px; background: #fffdf7; }
.bar-row { display: grid; grid-template-columns: minmax(180px, 260px) 1fr 90px; gap: 12px; align-items: center; margin: 10px 0; }
.bar { height: 22px; border-radius: 999px; background: #eadfcd; overflow: hidden; }
.fill { height: 100%; background: linear-gradient(90deg, var(--accent), #55a994); }
.fill.warn { background: linear-gradient(90deg, var(--accent-2), #d79763); }
table { width: 100%; border-collapse: collapse; font-size: 14px; }
th, td { border-bottom: 1px solid var(--line); padding: 9px 8px; text-align: right; }
th:first-child, td:first-child { text-align: left; }
th { color: var(--muted); font-size: 12px; text-transform: uppercase; letter-spacing: 0.06em; }
ul { margin: 0; padding-left: 20px; }
li { margin: 7px 0; }
.cmg-node { display: inline-block; margin: 4px; padding: 7px 10px; border-radius: 999px; border: 1px solid var(--line); background: #fffdf7; }
.cmg-edge { color: var(--muted); font-family: Consolas, monospace; margin: 4px 0; }
""".strip()

    def _render_cards(
        self,
        interpretation: dict[str, object],
        rows: list[dict[str, object]],
        cmg_summary: dict[str, object],
    ) -> str:
        best_f1 = interpretation.get("best_f1_method", self._best_row(rows, "f1").get("method_id"))
        best_micro = interpretation.get("best_micro_f1_method", self._best_row(rows, "micro_f1").get("method_id"))
        compression = interpretation.get(
            "strongest_compression_method",
            self._best_row(rows, "avg_reduction_rate").get("method_id"),
        )
        matched = cmg_summary.get("matched_entry_count", "n/a")
        total = cmg_summary.get("entry_count", "n/a")
        cards = [
            ("Best Macro F1", best_f1),
            ("Best Micro F1", best_micro),
            ("Strongest Compression", compression),
            ("CMG Matched Entries", f"{matched}/{total}"),
        ]
        return '<div class="grid">' + "".join(
            f'<div class="card"><div class="label">{html.escape(label)}</div><div class="value">{html.escape(str(value))}</div></div>'
            for label, value in cards
        ) + "</div>"

    @staticmethod
    def _render_pipeline() -> str:
        steps = [
            "Version-pair diff",
            "Function-level change localization",
            "ENRE graph normalization",
            "CMG and fallback context",
            "Structured prompt",
            "LLM generation",
            "Aggregation and evaluation",
        ]
        return (
            "<section><h2>Pipeline Overview</h2><div class=\"pipeline\">"
            + "".join(f'<div class="step">{idx}. {html.escape(step)}</div>' for idx, step in enumerate(steps, 1))
            + "</div></section>"
        )

    def _render_bar_section(
        self,
        title: str,
        rows: list[dict[str, object]],
        metric: str,
        *,
        max_value: float | None = None,
    ) -> str:
        numeric_values = [self._float(row.get(metric)) for row in rows]
        denominator = max_value if max_value is not None else max(numeric_values or [1.0])
        if denominator <= 0:
            denominator = 1.0
        body = []
        for row in rows:
            value = self._float(row.get(metric))
            width = max(0.0, min(100.0, value / denominator * 100.0))
            fill_class = "fill warn" if metric in {"micro_redundancy_per_gt", "avg_total_tokens"} else "fill"
            body.append(
                '<div class="bar-row">'
                f'<div>{html.escape(str(row.get("method_id", "")))}</div>'
                f'<div class="bar"><div class="{fill_class}" style="width:{width:.2f}%"></div></div>'
                f"<div>{value:.4f}</div>"
                "</div>"
            )
        return f"<section><h2>{html.escape(title)}</h2>{''.join(body)}</section>"

    def _render_token_section(self, rows: list[dict[str, object]]) -> str:
        if not any(self._float(row.get("avg_total_tokens")) > 0 for row in rows):
            return ""
        return self._render_bar_section("Average Token Cost", rows, "avg_total_tokens")

    def _render_matrix_table(self, rows: list[dict[str, object]]) -> str:
        include_reduction = any(row.get("avg_reduction_rate") is not None for row in rows)
        include_tokens = any(row.get("avg_total_tokens") is not None for row in rows)
        headers = ["Method", "P", "R", "Macro F1", "Micro F1", "Unsupported", "Extra/GT"]
        if include_reduction:
            headers.append("Reduction")
        if include_tokens:
            headers.append("Tokens")
        body = []
        for row in rows:
            values = [
                row.get("method_id", ""),
                self._fmt(row.get("precision")),
                self._fmt(row.get("recall")),
                self._fmt(row.get("f1")),
                self._fmt(row.get("micro_f1")),
                self._fmt(row.get("unsupported_claim_rate")),
                self._fmt(row.get("micro_redundancy_per_gt")),
            ]
            if include_reduction:
                values.append(self._fmt(row.get("avg_reduction_rate")))
            if include_tokens:
                values.append(self._fmt(row.get("avg_total_tokens"), digits=1))
            body.append("<tr>" + "".join(f"<td>{html.escape(str(value))}</td>" for value in values) + "</tr>")
        return (
            "<section><h2>Main Result Matrix</h2><table><thead><tr>"
            + "".join(f"<th>{html.escape(item)}</th>" for item in headers)
            + "</tr></thead><tbody>"
            + "".join(body)
            + "</tbody></table></section>"
        )

    def _render_expanded_comparison_table(self, rows: list[dict[str, object]]) -> str:
        if not rows:
            return ""
        headers = ["Method", "82 Macro F1", "55 Macro F1", "137 Macro F1", "82 Micro F1", "55 Micro F1", "137 Micro F1"]
        body = []
        for row in rows:
            values = [
                row.get("method_id", ""),
                self._fmt(row.get("core_82gt_macro_f1")),
                self._fmt(row.get("extension_55gt_macro_f1")),
                self._fmt(row.get("expanded_137gt_macro_f1")),
                self._fmt(row.get("core_82gt_micro_f1")),
                self._fmt(row.get("extension_55gt_micro_f1")),
                self._fmt(row.get("expanded_137gt_micro_f1")),
            ]
            body.append("<tr>" + "".join(f"<td>{html.escape(str(value))}</td>" for value in values) + "</tr>")
        return (
            "<section><h2>Expanded 137-GT Robustness Check</h2>"
            "<p>The 137-GT view combines the controlled 82-GT matrix with the human-audited Git 2.53 and PCRE2 full-scope extension.</p>"
            "<table><thead><tr>"
            + "".join(f"<th>{html.escape(item)}</th>" for item in headers)
            + "</tr></thead><tbody>"
            + "".join(body)
            + "</tbody></table></section>"
        )

    def _render_medium_table(self, rows: list[dict[str, object]]) -> str:
        if not rows:
            return ""
        headers = ["Method", "Cases", "Avg F1", "Avg Unsupported", "Avg Extra/GT", "Avg Tokens"]
        body = []
        for row in rows:
            values = [
                row.get("method_id", ""),
                row.get("case_count", row.get("cases", "")),
                self._fmt(row.get("f1")),
                self._fmt(row.get("unsupported_claim_rate")),
                self._fmt(row.get("extra_per_gt")),
                self._fmt(row.get("total_tokens"), digits=1),
            ]
            body.append("<tr>" + "".join(f"<td>{html.escape(str(value))}</td>" for value in values) + "</tr>")
        return (
            "<section><h2>Medium-Case View</h2><table><thead><tr>"
            + "".join(f"<th>{html.escape(item)}</th>" for item in headers)
            + "</tr></thead><tbody>"
            + "".join(body)
            + "</tbody></table></section>"
        )

    def _render_cmg_coverage(self, rows: list[dict[str, object]], interpretation: object) -> str:
        if not rows:
            return ""
        headers = [
            "Case",
            "Entries",
            "Compact",
            "Rich",
            "Projected",
            "Graph Hits",
            "Matching-Only",
        ]
        body = []
        for row in rows:
            values = [
                row.get("case_id", ""),
                self._int_text(row.get("entry_count")),
                self._int_text(row.get("compact_prompt_matches")),
                self._int_text(row.get("rich_prompt_matches")),
                self._int_text(row.get("projected_prompt_matches")),
                self._int_text(row.get("matching_graph_hits")),
                self._int_text(row.get("matching_only_after_projection")),
            ]
            body.append("<tr>" + "".join(f"<td>{html.escape(str(value))}</td>" for value in values) + "</tr>")

        totals = self._sum_cmg_coverage(rows)
        bars = ""
        if totals["entry_count"] > 0:
            bars = (
                "<div class=\"coverage-bars\">"
                + self._render_coverage_bar("Compact prompt matches", totals["compact_prompt_matches"], totals["entry_count"])
                + self._render_coverage_bar("Rich prompt matches", totals["rich_prompt_matches"], totals["entry_count"])
                + self._render_coverage_bar(
                    "Conservative projection matches",
                    totals["projected_prompt_matches"],
                    totals["entry_count"],
                )
                + self._render_coverage_bar("Rich graph hits", totals["matching_graph_hits"], totals["entry_count"])
                + "</div>"
            )

        return (
            "<section><h2>CMG Coverage Optimization</h2>"
            "<p>Stage 2 coverage is reported separately from final LLM quality. "
            "The rich graph is used only for matching and projection, while prompt-side CMG remains compact.</p>"
            + bars
            + "<table><thead><tr>"
            + "".join(f"<th>{html.escape(item)}</th>" for item in headers)
            + "</tr></thead><tbody>"
            + "".join(body)
            + "</tbody></table>"
            + self._render_inline_bullets(interpretation)
            + "</section>"
        )

    def _render_coverage_bar(self, label: str, value: int, total: int) -> str:
        ratio = value / total if total else 0.0
        width = max(0.0, min(100.0, ratio * 100.0))
        return (
            '<div class="bar-row">'
            f"<div>{html.escape(label)}</div>"
            f'<div class="bar"><div class="fill" style="width:{width:.2f}%"></div></div>'
            f"<div>{value}/{total}</div>"
            "</div>"
        )

    def _render_cmg(self, cmg_summary: dict[str, object]) -> str:
        if not cmg_summary:
            return ""
        nodes = self._list_of_dicts(cmg_summary.get("sample_nodes"))
        edges = self._list_of_dicts(cmg_summary.get("sample_edges"))
        node_html = "".join(
            f'<span class="cmg-node">{html.escape(str(node.get("qualified_name", node.get("name", node.get("id", "")))))}</span>'
            for node in nodes[:18]
        )
        edge_html = "".join(
            '<div class="cmg-edge">'
            + html.escape(f'{edge.get("source_id")} -> {edge.get("target_id")} ({edge.get("type", "call")})')
            + "</div>"
            for edge in edges[:24]
        )
        return (
            "<section><h2>CMG Sample</h2>"
            f"<p>Sample entry: {html.escape(str(cmg_summary.get('sample_symbol', 'n/a')))}</p>"
            f"<p>Matched entries: {html.escape(str(cmg_summary.get('matched_entry_count', 'n/a')))} / "
            f"{html.escape(str(cmg_summary.get('entry_count', 'n/a')))}</p>"
            f"<div>{node_html}</div>{edge_html}</section>"
        )

    @staticmethod
    def _render_bullets(title: str, items: object) -> str:
        if not isinstance(items, list) or not items:
            return ""
        return (
            f"<section><h2>{html.escape(title)}</h2><ul>"
            + "".join(f"<li>{html.escape(str(item))}</li>" for item in items)
            + "</ul></section>"
        )

    @staticmethod
    def _render_inline_bullets(items: object) -> str:
        if not isinstance(items, list) or not items:
            return ""
        return "<ul>" + "".join(f"<li>{html.escape(str(item))}</li>" for item in items) + "</ul>"

    @staticmethod
    def _build_cmg_summary(cmg_payload: dict[str, object]) -> dict[str, object]:
        if not cmg_payload:
            return {}
        entries = VisualReportBuilder._list_of_dicts(cmg_payload.get("entries"))
        sample = next(
            (
                entry
                for entry in entries
                if isinstance(entry.get("cmg"), dict)
                and VisualReportBuilder._list_of_dicts(entry.get("cmg", {}).get("nodes"))
            ),
            entries[0] if entries else {},
        )
        cmg = sample.get("cmg") if isinstance(sample.get("cmg"), dict) else {}
        summary = cmg_payload.get("summary") if isinstance(cmg_payload.get("summary"), dict) else {}
        return {
            "entry_count": summary.get("entry_count", len(entries)),
            "matched_entry_count": summary.get("matched_entry_count"),
            "matching_graph_matched_entry_count": summary.get("matching_graph_matched_entry_count"),
            "sample_symbol": sample.get("symbol"),
            "sample_nodes": VisualReportBuilder._list_of_dicts(cmg.get("nodes")) if isinstance(cmg, dict) else [],
            "sample_edges": VisualReportBuilder._list_of_dicts(cmg.get("edges")) if isinstance(cmg, dict) else [],
        }

    @staticmethod
    def _normalize_final_matrix_rows(final_matrix: dict[str, object]) -> list[dict[str, object]]:
        rows = []
        for row in VisualReportBuilder._list_of_dicts(final_matrix.get("macro_micro_by_method")):
            rows.append(
                {
                    "method_id": row.get("method"),
                    "case_count": row.get("evaluated_cases"),
                    "ground_truth_count": row.get("ground_truth_count"),
                    "generated_count": row.get("generated_count"),
                    "precision": row.get("micro_precision"),
                    "recall": row.get("micro_recall"),
                    "f1": row.get("macro_f1"),
                    "micro_f1": row.get("micro_f1"),
                    "unsupported_claim_rate": row.get("unsupported_rate_micro"),
                    "matches_per_gt": row.get("matches_per_gt"),
                    "micro_redundancy_per_gt": row.get("extra_per_gt"),
                    "avg_final_notes": row.get("avg_final_notes"),
                    "backend_failed_entries": row.get("backend_failed_entries"),
                }
            )
        return rows

    @staticmethod
    def _is_expanded_matrix(matrix: dict[str, object]) -> bool:
        rows = VisualReportBuilder._list_of_dicts(matrix.get("matrix_rows"))
        return bool(rows and "expanded_137gt_macro_f1" in rows[0])

    @staticmethod
    def _normalize_expanded_matrix_rows(expanded_matrix: dict[str, object]) -> list[dict[str, object]]:
        rows = []
        for row in VisualReportBuilder._list_of_dicts(expanded_matrix.get("matrix_rows")):
            rows.append(
                {
                    "method_id": row.get("method"),
                    "case_count": expanded_matrix.get("summary", {}).get("case_count")
                    if isinstance(expanded_matrix.get("summary"), dict)
                    else None,
                    "ground_truth_count": expanded_matrix.get("summary", {}).get("ground_truth_count")
                    if isinstance(expanded_matrix.get("summary"), dict)
                    else None,
                    "generated_count": row.get("expanded_generated_count"),
                    "precision": row.get("expanded_micro_precision"),
                    "recall": row.get("expanded_micro_recall"),
                    "f1": row.get("expanded_137gt_macro_f1"),
                    "micro_f1": row.get("expanded_137gt_micro_f1"),
                    "unsupported_claim_rate": row.get("expanded_unsupported_rate"),
                    "matches_per_gt": row.get("expanded_matches_per_gt"),
                    "micro_redundancy_per_gt": row.get("expanded_extra_per_gt"),
                    "avg_final_notes": row.get("expanded_avg_final_notes"),
                    "avg_reduction_rate": row.get("expanded_reduction_rate"),
                    "avg_total_tokens": row.get("expanded_avg_total_tokens"),
                    "backend_failed_entries": 0,
                }
            )
        return rows

    @staticmethod
    def _normalize_expanded_comparison_rows(expanded_matrix: dict[str, object]) -> list[dict[str, object]]:
        rows = []
        for row in VisualReportBuilder._list_of_dicts(expanded_matrix.get("matrix_rows")):
            rows.append(
                {
                    "method_id": row.get("method"),
                    "core_82gt_macro_f1": row.get("core_82gt_macro_f1"),
                    "extension_55gt_macro_f1": row.get("extension_55gt_macro_f1"),
                    "expanded_137gt_macro_f1": row.get("expanded_137gt_macro_f1"),
                    "core_82gt_micro_f1": row.get("core_82gt_micro_f1"),
                    "extension_55gt_micro_f1": row.get("extension_55gt_micro_f1"),
                    "expanded_137gt_micro_f1": row.get("expanded_137gt_micro_f1"),
                }
            )
        return rows

    @staticmethod
    def _final_matrix_interpretation(
        rows: list[dict[str, object]],
        final_matrix: dict[str, object],
    ) -> dict[str, object]:
        summary = final_matrix.get("summary") if isinstance(final_matrix.get("summary"), dict) else {}
        non_text_rows = [row for row in rows if row.get("method_id") != "text_only"]
        compression_row = min(non_text_rows, key=lambda row: VisualReportBuilder._float(row.get("avg_final_notes")))
        return {
            "best_f1_method": VisualReportBuilder._best_row(rows, "f1").get("method_id"),
            "best_micro_f1_method": VisualReportBuilder._best_row(rows, "micro_f1").get("method_id"),
            "strongest_compression_method": compression_row.get("method_id"),
            "case_count": summary.get("case_count"),
            "gt_count": summary.get("gt_count"),
        }

    @staticmethod
    def _expanded_matrix_interpretation(
        rows: list[dict[str, object]],
        expanded_matrix: dict[str, object],
    ) -> dict[str, object]:
        summary = expanded_matrix.get("summary") if isinstance(expanded_matrix.get("summary"), dict) else {}
        non_text_rows = [row for row in rows if row.get("method_id") != "text_only"]
        compression_row = min(non_text_rows, key=lambda row: VisualReportBuilder._float(row.get("avg_final_notes")))
        return {
            "best_f1_method": VisualReportBuilder._best_row(rows, "f1").get("method_id"),
            "best_micro_f1_method": VisualReportBuilder._best_row(rows, "micro_f1").get("method_id"),
            "strongest_compression_method": compression_row.get("method_id"),
            "case_count": summary.get("case_count"),
            "gt_count": summary.get("ground_truth_count"),
        }

    @staticmethod
    def _final_matrix_thesis_notes() -> list[str]:
        return [
            "The final selected benchmark contains 82 reviewed semantic GT entries across 11 case-version pairs.",
            "All selected cases have the same eight method variants, strict semantic matches, and evaluation files.",
            "Similarity-family aggregation has the best Macro/Micro F1 in the final matrix, while strict 1-hop is the strongest graph-context ablation.",
            "The main remaining quality issue is redundancy and unsupported generated statements under evidence-rich variants.",
        ]

    @staticmethod
    def _final_matrix_validity_notes() -> list[str]:
        return [
            "The GT is semantic release-note-level evidence, not one-to-one commit or function evidence.",
            "PCRE2 and Git 2.53 are sampled stress scopes and must be described as fixed-scope sampled cases.",
            "High recall partly depends on the current semantic GT granularity; finer GT splitting may reduce recall.",
            "Strict matching remains judgment-sensitive and should be reported as manually audited semantic matching.",
        ]

    @staticmethod
    def _expanded_matrix_thesis_notes() -> list[str]:
        return [
            "The expanded robustness view contains 137 semantic GT entries across 13 case-version pairs.",
            "The 137-GT view combines the controlled 82-GT matrix with a 55-GT full-scope extension for Git 2.53 and PCRE2.",
            "Similarity-family aggregation remains strongest by Macro/Micro F1, but absolute precision drops under large full-scope releases.",
            "The extension should be used as scale/robustness evidence, not as a silent replacement for the controlled 82-GT main table.",
        ]

    @staticmethod
    def _expanded_matrix_validity_notes() -> list[str]:
        return [
            "The full-scope extension has much larger generated-output volume, so unsupported rate becomes central to interpretation.",
            "Git 2.53 and PCRE2 full-scope matches were close-to-manual audited, but user sign-off is still recommended before final thesis labels.",
            "The controlled 82-GT and expanded 137-GT tables answer different questions: controlled method comparison versus large-release robustness.",
            "Do not overfit the conclusion to one large release; report ranking stability and absolute-score degradation together.",
        ]

    @staticmethod
    def _best_row(rows: list[dict[str, object]], metric: str) -> dict[str, object]:
        if not rows:
            return {}
        return max(rows, key=lambda row: VisualReportBuilder._float(row.get(metric)))

    @staticmethod
    def _sum_cmg_coverage(rows: list[dict[str, object]]) -> dict[str, int]:
        keys = [
            "entry_count",
            "compact_prompt_matches",
            "rich_prompt_matches",
            "projected_prompt_matches",
            "matching_graph_hits",
            "matching_only_after_projection",
        ]
        return {key: sum(VisualReportBuilder._int(row.get(key)) for row in rows) for key in keys}

    @staticmethod
    def _read_json(path: str | Path | None) -> dict[str, object]:
        if path is None:
            return {}
        target = Path(path)
        if not target.exists():
            return {}
        payload = json.loads(target.read_text(encoding="utf-8-sig"))
        return payload if isinstance(payload, dict) else {}

    @staticmethod
    def _list_of_dicts(raw: object) -> list[dict[str, object]]:
        if not isinstance(raw, list):
            return []
        return [item for item in raw if isinstance(item, dict)]

    @staticmethod
    def _float(value: object) -> float:
        try:
            return float(value)
        except (TypeError, ValueError):
            return 0.0

    @staticmethod
    def _int(value: object) -> int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return 0

    @staticmethod
    def _int_text(value: object) -> str:
        return str(VisualReportBuilder._int(value))

    @staticmethod
    def _fmt(value: object, *, digits: int = 4) -> str:
        try:
            return f"{float(value):.{digits}f}"
        except (TypeError, ValueError):
            return ""

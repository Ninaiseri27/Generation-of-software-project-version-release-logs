from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ExperimentSpec:
    method_id: str
    method_group: str
    description: str
    evaluation_summary: str
    output_summary: str
    evaluation_variant: str
    output_variant: str


CORE5_EXPERIMENT_SPECS = (
    ExperimentSpec(
        method_id="text_only",
        method_group="prompt_baseline",
        description="Release-level prompt with metadata and commit text only.",
        evaluation_summary="evaluation_strict_core5_summary.json",
        output_summary="baseline_core5_output_summary.json",
        evaluation_variant="text_only",
        output_variant="text_only",
    ),
    ExperimentSpec(
        method_id="diff_only",
        method_group="prompt_baseline",
        description="Function-level diff evidence only.",
        evaluation_summary="evaluation_strict_core5_summary.json",
        output_summary="baseline_core5_output_summary.json",
        evaluation_variant="diff_only",
        output_variant="diff_only",
    ),
    ExperimentSpec(
        method_id="no_graph",
        method_group="prompt_baseline",
        description="Diff and metadata without CMG graph context.",
        evaluation_summary="evaluation_strict_core5_summary.json",
        output_summary="baseline_core5_output_summary.json",
        evaluation_variant="no_graph",
        output_variant="no_graph",
    ),
    ExperimentSpec(
        method_id="full_adaptive_rule_family",
        method_group="main_method",
        description="Adaptive CMG/fallback context with rule-family aggregation.",
        evaluation_summary="evaluation_strict_core5_summary.json",
        output_summary="baseline_core5_output_summary.json",
        evaluation_variant="full",
        output_variant="full",
    ),
    ExperimentSpec(
        method_id="full_no_fallback",
        method_group="fallback_ablation",
        description="Full prompt without synthetic/fallback context.",
        evaluation_summary="fallback_ablation_core5_evaluation_summary.json",
        output_summary="fallback_ablation_core5_output_summary.json",
        evaluation_variant="no_fallback",
        output_variant="no_fallback",
    ),
    ExperimentSpec(
        method_id="full_strict_1hop",
        method_group="cmg_ablation",
        description="Strict 1-hop CMG context with the full prompt variant.",
        evaluation_summary="cmg_strict_1hop_core5_evaluation_summary.json",
        output_summary="cmg_strict_1hop_core5_output_summary.json",
        evaluation_variant="full",
        output_variant="full",
    ),
    ExperimentSpec(
        method_id="full_evidence_similarity_family",
        method_group="aggregation_ablation",
        description="Adaptive full outputs rewritten with evidence-gated similarity aggregation.",
        evaluation_summary="aggregation_evidence_similarity_full_core5_evaluation_summary.json",
        output_summary="aggregation_evidence_similarity_full_core5_output_summary.json",
        evaluation_variant="full",
        output_variant="full",
    ),
    ExperimentSpec(
        method_id="full_similarity_family",
        method_group="aggregation_ablation",
        description="Adaptive full outputs rewritten with similarity-family aggregation.",
        evaluation_summary="aggregation_similarity_full_core5_evaluation_summary.json",
        output_summary="aggregation_similarity_full_core5_output_summary.json",
        evaluation_variant="full",
        output_variant="full",
    ),
)


class ExperimentReportBuilder:
    MEDIUM_GT_THRESHOLD = 4

    def __init__(self, *, benchmark_root: str | Path) -> None:
        self.benchmark_root = Path(benchmark_root)

    def build_payload(self) -> dict[str, object]:
        rows = [self._build_row(spec) for spec in CORE5_EXPERIMENT_SPECS]
        return {
            "source": {
                "builder": "experiment-report-builder-v1",
                "benchmark_root": str(self.benchmark_root),
            },
            "rows": rows,
            "interpretation": self._build_interpretation(rows),
        }

    def build_case_payload(self) -> dict[str, object]:
        rows = self._build_case_rows()
        medium_rows = [
            row
            for row in rows
            if self._numeric(row.get("ground_truth_count")) >= self.MEDIUM_GT_THRESHOLD
        ]
        return {
            "source": {
                "builder": "experiment-case-report-builder-v1",
                "benchmark_root": str(self.benchmark_root),
                "medium_gt_threshold": self.MEDIUM_GT_THRESHOLD,
            },
            "rows": rows,
            "medium_case_macro": self._method_macro(medium_rows),
            "interpretation": self._build_case_interpretation(rows, medium_rows),
        }

    def _build_row(self, spec: ExperimentSpec) -> dict[str, object]:
        evaluation_payload = self._read_json(self.benchmark_root / spec.evaluation_summary)
        output_payload = self._read_json(self.benchmark_root / spec.output_summary)
        evaluation_macro = self._macro_row(evaluation_payload, spec.evaluation_variant)
        evaluation_micro = self._micro_row(evaluation_payload, spec.evaluation_variant)
        evaluation_rollup = self._evaluation_rollup(evaluation_payload, spec.evaluation_variant)
        output_macro = self._macro_row(output_payload, spec.output_variant)

        return {
            "method_id": spec.method_id,
            "method_group": spec.method_group,
            "description": spec.description,
            "evaluated_cases": evaluation_macro.get("evaluated_cases"),
            "summarized_cases": output_macro.get("summarized_cases"),
            "precision": evaluation_macro.get("precision"),
            "recall": evaluation_macro.get("recall"),
            "f1": evaluation_macro.get("f1"),
            "micro_precision": evaluation_micro.get("precision"),
            "micro_recall": evaluation_micro.get("recall"),
            "micro_f1": evaluation_micro.get("f1"),
            "unsupported_claim_rate": evaluation_macro.get("unsupported_claim_rate"),
            "avg_redundancy_count": evaluation_macro.get("avg_redundancy_count"),
            "total_ground_truth_count": evaluation_rollup.get("total_ground_truth_count"),
            "total_valid_match_count": evaluation_rollup.get("total_valid_match_count"),
            "total_redundancy_count": evaluation_rollup.get("total_redundancy_count"),
            "micro_redundancy_per_gt": evaluation_rollup.get("micro_redundancy_per_gt"),
            "micro_matches_per_gt": evaluation_rollup.get("micro_matches_per_gt"),
            "structural_valid_rate": evaluation_macro.get("structural_valid_rate"),
            "avg_generated_entry_count": output_macro.get("avg_generated_entry_count"),
            "avg_final_note_count": output_macro.get("avg_deduplicated_release_note_count"),
            "avg_compression_ratio": output_macro.get("avg_compression_ratio"),
            "avg_reduction_rate": output_macro.get("avg_reduction_rate"),
            "avg_total_tokens": output_macro.get("avg_total_tokens"),
            "evaluation_summary_path": str(self.benchmark_root / spec.evaluation_summary),
            "output_summary_path": str(self.benchmark_root / spec.output_summary),
        }

    def _build_case_rows(self) -> list[dict[str, object]]:
        rows: list[dict[str, object]] = []
        case_order: list[str] = []
        for spec in CORE5_EXPERIMENT_SPECS:
            evaluation_payload = self._read_json(self.benchmark_root / spec.evaluation_summary)
            output_payload = self._read_json(self.benchmark_root / spec.output_summary)
            evaluation_rows = self._evaluation_rows(evaluation_payload, spec.evaluation_variant)
            output_rows = self._output_rows_by_case(output_payload, spec.output_variant)
            for evaluation_row in evaluation_rows:
                case_id = str(evaluation_row.get("case_id", ""))
                if case_id not in case_order:
                    case_order.append(case_id)
                output_row = output_rows.get(case_id, {})
                rows.append(
                    {
                        "case_id": case_id,
                        "case_group": self._case_group(evaluation_row),
                        "method_id": spec.method_id,
                        "method_group": spec.method_group,
                        "ground_truth_count": evaluation_row.get("ground_truth_count"),
                        "generated_count": evaluation_row.get("generated_count"),
                        "precision": evaluation_row.get("precision"),
                        "recall": evaluation_row.get("recall"),
                        "f1": evaluation_row.get("f1"),
                        "unsupported_claim_rate": evaluation_row.get("unsupported_claim_rate"),
                        "matches_per_gt": evaluation_row.get("avg_matches_per_gt"),
                        "extra_per_gt": evaluation_row.get("redundancy_per_gt"),
                        "final_note_count": output_row.get("deduplicated_release_note_count"),
                        "reduction_rate": output_row.get("reduction_rate"),
                        "total_tokens": output_row.get("total_tokens"),
                    }
                )
        method_order = [spec.method_id for spec in CORE5_EXPERIMENT_SPECS]
        return sorted(
            rows,
            key=lambda row: (
                self._ordered_index(case_order, str(row.get("case_id", ""))),
                self._ordered_index(method_order, str(row.get("method_id", ""))),
            ),
        )

    @staticmethod
    def render_markdown(payload: dict[str, object]) -> str:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            rows = []
        lines = [
            "# Core5 Experiment Matrix",
            "",
            "| Method | Group | P | R | Macro F1 | Micro F1 | Unsupported | Matches/GT | Extra/GT | Final Notes | Reduction | Tokens |",
            "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            if not isinstance(row, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('method_id', '')}`",
                        f"`{row.get('method_group', '')}`",
                        ExperimentReportBuilder._format_cell(row.get("precision")),
                        ExperimentReportBuilder._format_cell(row.get("recall")),
                        ExperimentReportBuilder._format_cell(row.get("f1")),
                        ExperimentReportBuilder._format_cell(row.get("micro_f1")),
                        ExperimentReportBuilder._format_cell(row.get("unsupported_claim_rate")),
                        ExperimentReportBuilder._format_cell(row.get("micro_matches_per_gt")),
                        ExperimentReportBuilder._format_cell(row.get("micro_redundancy_per_gt")),
                        ExperimentReportBuilder._format_cell(row.get("avg_final_note_count")),
                        ExperimentReportBuilder._format_cell(row.get("avg_reduction_rate")),
                        ExperimentReportBuilder._format_cell(row.get("avg_total_tokens")),
                    ]
                )
                + " |"
            )

        interpretation = payload.get("interpretation")
        if isinstance(interpretation, dict):
            lines.extend(
                [
                    "",
                    "## Interpretation",
                    "",
                    f"- Best macro F1: `{interpretation.get('best_f1_method', '')}`.",
                    f"- Best micro F1: `{interpretation.get('best_micro_f1_method', '')}`.",
                    f"- Lowest token cost: `{interpretation.get('lowest_token_method', '')}`.",
                    f"- Strongest compression: `{interpretation.get('strongest_compression_method', '')}`.",
                    f"- Lowest unsupported-claim rate: `{interpretation.get('lowest_unsupported_method', '')}`.",
                    "",
                    "The matrix is intended for thesis tables. It should be read as a tradeoff view, not a single-score ranking.",
                    "`Micro F1` is computed from total matched/generated/GT counts across all core5 cases, so it is less sensitive to tiny low-GT cases than unweighted macro F1.",
                    "`Matches/GT` is valid semantic matches divided by total GT entries. `Extra/GT` is redundant matches beyond the first match per GT, divided by total GT entries.",
                ]
            )

        return "\n".join(lines) + "\n"

    @staticmethod
    def render_case_markdown(payload: dict[str, object]) -> str:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            rows = []
        medium_case_macro = payload.get("medium_case_macro")
        if not isinstance(medium_case_macro, list):
            medium_case_macro = []
        interpretation = payload.get("interpretation")
        if not isinstance(interpretation, dict):
            interpretation = {}

        lines = [
            "# Core5 Per-Case Results",
            "",
            "This report supports thesis result interpretation beyond the aggregate matrix.",
            "It keeps low-GT cases visible while preventing them from silently dominating macro-level claims.",
            "",
            "## Per-Case Table",
            "",
            "| Case | Group | Method | GT | P | R | F1 | Unsupported | Matches/GT | Extra/GT | Final Notes | Reduction | Tokens |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            if not isinstance(row, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('case_id', '')}`",
                        f"`{row.get('case_group', '')}`",
                        f"`{row.get('method_id', '')}`",
                        ExperimentReportBuilder._format_cell(row.get("ground_truth_count")),
                        ExperimentReportBuilder._format_cell(row.get("precision")),
                        ExperimentReportBuilder._format_cell(row.get("recall")),
                        ExperimentReportBuilder._format_cell(row.get("f1")),
                        ExperimentReportBuilder._format_cell(row.get("unsupported_claim_rate")),
                        ExperimentReportBuilder._format_cell(row.get("matches_per_gt")),
                        ExperimentReportBuilder._format_cell(row.get("extra_per_gt")),
                        ExperimentReportBuilder._format_cell(row.get("final_note_count")),
                        ExperimentReportBuilder._format_cell(row.get("reduction_rate")),
                        ExperimentReportBuilder._format_cell(row.get("total_tokens")),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Medium-Case View",
                "",
                "Medium cases are defined as cases with at least 4 reviewed GT entries.",
                "This view is used as a robustness check against low-GT zlib/cJSON effects.",
                "",
                "| Method | Cases | Avg P | Avg R | Avg F1 | Avg Unsupported | Avg Extra/GT | Avg Tokens |",
                "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
            ]
        )
        for row in medium_case_macro:
            if not isinstance(row, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('method_id', '')}`",
                        ExperimentReportBuilder._format_cell(row.get("case_count")),
                        ExperimentReportBuilder._format_cell(row.get("precision")),
                        ExperimentReportBuilder._format_cell(row.get("recall")),
                        ExperimentReportBuilder._format_cell(row.get("f1")),
                        ExperimentReportBuilder._format_cell(row.get("unsupported_claim_rate")),
                        ExperimentReportBuilder._format_cell(row.get("extra_per_gt")),
                        ExperimentReportBuilder._format_cell(row.get("total_tokens")),
                    ]
                )
                + " |"
            )

        lines.extend(
            [
                "",
                "## Thesis-Ready Interpretation",
                "",
            ]
        )
        for note in interpretation.get("result_narrative", []):
            lines.append(f"- {note}")
        lines.extend(
            [
                "",
                "## Threats To Validity",
                "",
            ]
        )
        for note in interpretation.get("validity_threats", []):
            lines.append(f"- {note}")
        lines.extend(
            [
                "",
                "## Reporting Rule",
                "",
                "- Use the aggregate matrix as the main result table.",
                "- Use this per-case report to explain method behavior and low-GT sensitivity.",
                "- Do not claim that graph context universally improves F1; report it as a context/cost/redundancy tradeoff.",
            ]
        )
        return "\n".join(lines) + "\n"

    @classmethod
    def _build_interpretation(cls, rows: list[dict[str, object]]) -> dict[str, object]:
        return {
            "best_f1_method": cls._best_row(rows, "f1", reverse=True),
            "best_micro_f1_method": cls._best_row(rows, "micro_f1", reverse=True),
            "lowest_token_method": cls._best_row(rows, "avg_total_tokens", reverse=False),
            "strongest_compression_method": cls._best_row(rows, "avg_reduction_rate", reverse=True),
            "lowest_unsupported_method": cls._best_row(rows, "unsupported_claim_rate", reverse=False),
        }

    @classmethod
    def _build_case_interpretation(
        cls,
        rows: list[dict[str, object]],
        medium_rows: list[dict[str, object]],
    ) -> dict[str, object]:
        medium_macro = cls._method_macro(medium_rows)
        best_medium = cls._best_row(medium_macro, "f1", reverse=True)
        full_strict = cls._find_method(medium_macro, "full_strict_1hop")
        full_adaptive = cls._find_method(medium_macro, "full_adaptive_rule_family")
        return {
            "result_narrative": [
                "The aggregate matrix and medium-case view both show that `diff_only` is a strong baseline; therefore the thesis should not claim that adding graph context always improves F1.",
                f"On medium cases, the best average F1 method is `{best_medium}`.",
                "`full_strict_1hop` is the strongest graph-context variant in the current core5 matrix, while adaptive context provides a broader evidence view at higher token cost.",
                f"Medium-case `full_strict_1hop` F1 is {cls._format_cell(full_strict.get('f1')) if full_strict else ''}; medium-case adaptive `full` F1 is {cls._format_cell(full_adaptive.get('f1')) if full_adaptive else ''}.",
                "`full_similarity_family` gives the strongest final-note compression, but its F1 drop means it should be reported as a compression-quality tradeoff.",
                "High `Extra/GT` values indicate that redundancy remains an important limitation and a natural target for aggregation improvements.",
            ],
            "validity_threats": [
                "zlib and cJSON have low reviewed-GT counts, so macro averages are sensitive to these cases.",
                "Several variants reach recall 1.0000 because GT entries are semantic release-note items rather than fine-grained code facts.",
                "Manual `matches_strict.json` judgments are necessary but introduce reviewer-decision risk; security/CVE-related matches require extra audit.",
                "Official OpenHarmony release notes for minor component updates are incomplete, so GT depends on evidence triangulation from commits and code diffs.",
                "Graph context should be interpreted as analyzable evidence, not as a guaranteed accuracy improvement over diff-only evidence.",
            ],
        }

    @staticmethod
    def _best_row(rows: list[dict[str, object]], key: str, *, reverse: bool) -> str | None:
        candidates = [
            row
            for row in rows
            if isinstance(row.get(key), (int, float))
        ]
        if not candidates:
            return None
        return str(sorted(candidates, key=lambda row: float(row[key]), reverse=reverse)[0].get("method_id"))

    @classmethod
    def _method_macro(cls, rows: list[dict[str, object]]) -> list[dict[str, object]]:
        method_ids = []
        for row in rows:
            method_id = str(row.get("method_id", ""))
            if method_id and method_id not in method_ids:
                method_ids.append(method_id)
        return [
            {
                "method_id": method_id,
                "case_count": len([row for row in rows if row.get("method_id") == method_id]),
                "precision": cls._mean_case_metric(rows, method_id, "precision"),
                "recall": cls._mean_case_metric(rows, method_id, "recall"),
                "f1": cls._mean_case_metric(rows, method_id, "f1"),
                "unsupported_claim_rate": cls._mean_case_metric(
                    rows,
                    method_id,
                    "unsupported_claim_rate",
                ),
                "extra_per_gt": cls._mean_case_metric(rows, method_id, "extra_per_gt"),
                "total_tokens": cls._mean_case_metric(rows, method_id, "total_tokens"),
            }
            for method_id in method_ids
        ]

    @staticmethod
    def _mean_case_metric(
        rows: list[dict[str, object]],
        method_id: str,
        key: str,
    ) -> float | None:
        values = [
            float(row[key])
            for row in rows
            if row.get("method_id") == method_id
            and isinstance(row.get(key), (int, float))
            and not isinstance(row.get(key), bool)
        ]
        if not values:
            return None
        return round(sum(values) / len(values), 4)

    @staticmethod
    def _find_method(rows: list[dict[str, object]], method_id: str) -> dict[str, object] | None:
        for row in rows:
            if row.get("method_id") == method_id:
                return row
        return None

    @staticmethod
    def _ordered_index(values: list[str], value: str) -> int:
        try:
            return values.index(value)
        except ValueError:
            return len(values)

    @classmethod
    def _case_group(cls, row: dict[str, object]) -> str:
        ground_truth_count = cls._numeric(row.get("ground_truth_count"))
        return "medium_gt" if ground_truth_count >= cls.MEDIUM_GT_THRESHOLD else "low_gt"

    @staticmethod
    def _macro_row(payload: dict[str, object], variant: str) -> dict[str, object]:
        macro_averages = payload.get("macro_averages")
        if not isinstance(macro_averages, list):
            raise ValueError("summary JSON is missing macro_averages.")
        for row in macro_averages:
            if isinstance(row, dict) and row.get("variant") == variant:
                return row
        raise ValueError(f"summary JSON is missing macro row for variant: {variant}")

    @staticmethod
    def _micro_row(payload: dict[str, object], variant: str) -> dict[str, object]:
        micro_averages = payload.get("micro_averages")
        if not isinstance(micro_averages, list):
            return {}
        for row in micro_averages:
            if isinstance(row, dict) and row.get("variant") == variant:
                return row
        return {}

    @staticmethod
    def _evaluation_rollup(payload: dict[str, object], variant: str) -> dict[str, object]:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            raise ValueError("evaluation summary JSON is missing rows.")
        selected_rows = [
            row
            for row in rows
            if isinstance(row, dict)
            and row.get("variant") == variant
            and row.get("status") == "evaluated"
        ]
        total_gt = sum(
            ExperimentReportBuilder._numeric(row.get("ground_truth_count"))
            for row in selected_rows
        )
        total_valid_matches = sum(
            ExperimentReportBuilder._numeric(row.get("valid_match_count"))
            for row in selected_rows
        )
        total_redundancy = sum(
            ExperimentReportBuilder._numeric(row.get("redundancy_count"))
            for row in selected_rows
        )
        return {
            "total_ground_truth_count": total_gt,
            "total_valid_match_count": total_valid_matches,
            "total_redundancy_count": total_redundancy,
            "micro_redundancy_per_gt": round(total_redundancy / total_gt, 4) if total_gt else None,
            "micro_matches_per_gt": round(total_valid_matches / total_gt, 4) if total_gt else None,
        }

    @staticmethod
    def _evaluation_rows(payload: dict[str, object], variant: str) -> list[dict[str, object]]:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            raise ValueError("evaluation summary JSON is missing rows.")
        return [
            row
            for row in rows
            if isinstance(row, dict)
            and row.get("variant") == variant
            and row.get("status") == "evaluated"
        ]

    @staticmethod
    def _output_rows_by_case(
        payload: dict[str, object],
        variant: str,
    ) -> dict[str, dict[str, object]]:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            raise ValueError("output summary JSON is missing rows.")
        result: dict[str, dict[str, object]] = {}
        for row in rows:
            if (
                isinstance(row, dict)
                and row.get("variant") == variant
                and row.get("status") == "summarized"
            ):
                result[str(row.get("case_id", ""))] = row
        return result

    @staticmethod
    def _numeric(value: object) -> float:
        if isinstance(value, bool):
            return 0.0
        if isinstance(value, (int, float)):
            return float(value)
        return 0.0

    @staticmethod
    def _read_json(path: Path) -> dict[str, object]:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(payload, dict):
            raise ValueError(f"JSON payload must be an object: {path}")
        return payload

    @staticmethod
    def _format_cell(value: object) -> str:
        if value is None:
            return ""
        if isinstance(value, float):
            return f"{value:.4f}"
        return str(value)

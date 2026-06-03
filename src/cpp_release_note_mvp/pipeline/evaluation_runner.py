from __future__ import annotations

import json
from pathlib import Path

from .evaluation import ReleaseNoteEvaluator
from .prompt_builder import SUPPORTED_PROMPT_VARIANTS
from .release_note_generation import ReleaseNoteGenerator


class BaselineEvaluationRunner:
    def __init__(
        self,
        *,
        metadata_paths: list[str | Path],
        variants: list[str] | None = None,
        matches_filename: str = "matches.json",
        evaluation_filename: str = "evaluation.json",
        match_template_filename: str = "match_template.json",
        baseline_root_name: str = "baselines",
    ) -> None:
        if not metadata_paths:
            raise ValueError("At least one case metadata path is required.")
        self.metadata_paths = [Path(path) for path in metadata_paths]
        self.variants = self._normalize_variants(variants)
        self.matches_filename = matches_filename
        self.evaluation_filename = evaluation_filename
        self.match_template_filename = match_template_filename
        self.baseline_root_name = baseline_root_name

    def run(self) -> dict[str, object]:
        results: list[dict[str, object]] = []
        for metadata_path in self.metadata_paths:
            metadata = self._read_json(metadata_path)
            case_id = str(metadata.get("case_id", metadata_path.parent.name))
            ground_truth_path = self._resolve_ground_truth_path(metadata_path, metadata)
            output_dir = self._resolve_output_dir(metadata_path, metadata)

            for variant in self.variants:
                variant_dir = output_dir / self.baseline_root_name / variant
                release_note_path = variant_dir / "release_note.json"
                evaluation_path = variant_dir / self.evaluation_filename
                match_template_path = variant_dir / self.match_template_filename
                matches_path = variant_dir / self.matches_filename
                usable_matches_path = (
                    matches_path
                    if matches_path.exists() and matches_path.stat().st_size > 0
                    else None
                )

                if not release_note_path.exists():
                    results.append(
                        {
                            "case_id": case_id,
                            "variant": variant,
                            "status": "missing_release_note",
                            "release_note_path": str(release_note_path),
                        }
                    )
                    continue

                evaluator = ReleaseNoteEvaluator(
                    ground_truth_path=ground_truth_path,
                    release_note_path=release_note_path,
                    matches_path=usable_matches_path,
                )
                payload = evaluator.build_payload()
                self._write_json(evaluation_path, payload)
                self._write_json(match_template_path, payload["match_template"])
                summary = payload.get("summary", {})
                results.append(
                    {
                        "case_id": case_id,
                        "variant": variant,
                        "status": self._summary_value(summary, "evaluation_status"),
                        "ground_truth_count": self._summary_value(summary, "ground_truth_count"),
                        "generated_count": self._summary_value(summary, "generated_count"),
                        "precision": self._summary_value(summary, "precision"),
                        "recall": self._summary_value(summary, "recall"),
                        "f1": self._summary_value(summary, "f1"),
                        "structural_valid_rate": self._summary_value(
                            summary,
                            "structural_valid_rate",
                        ),
                        "matches_path": str(matches_path),
                        "evaluation_path": str(evaluation_path),
                        "match_template_path": str(match_template_path),
                    }
                )

        return {
            "source": {
                "runner": "baseline-evaluation-runner-v1",
                "variants": self.variants,
            },
            "metadata_paths": [str(path) for path in self.metadata_paths],
            "results": results,
        }

    @staticmethod
    def _normalize_variants(variants: list[str] | None) -> list[str]:
        if not variants:
            return list(SUPPORTED_PROMPT_VARIANTS)
        normalized: list[str] = []
        for variant in variants:
            value = variant.strip().lower().replace("-", "_")
            if value not in SUPPORTED_PROMPT_VARIANTS:
                allowed = ", ".join(SUPPORTED_PROMPT_VARIANTS)
                raise ValueError(f"Unsupported baseline variant: {variant}. Expected one of: {allowed}.")
            if value not in normalized:
                normalized.append(value)
        return normalized

    @classmethod
    def _resolve_ground_truth_path(
        cls,
        metadata_path: Path,
        metadata: dict[str, object],
    ) -> Path:
        ground_truth = metadata.get("ground_truth")
        if isinstance(ground_truth, dict) and ground_truth.get("path"):
            return cls._resolve_repo_relative_path(metadata_path, str(ground_truth["path"]))
        raise ValueError(f"metadata is missing ground_truth.path: {metadata_path}")

    @classmethod
    def _resolve_output_dir(
        cls,
        metadata_path: Path,
        metadata: dict[str, object],
    ) -> Path:
        artifact_candidates: list[object] = []
        pipeline_artifacts = metadata.get("pipeline_artifacts")
        if isinstance(pipeline_artifacts, dict):
            output_dir = pipeline_artifacts.get("output_dir")
            if output_dir:
                return cls._resolve_repo_relative_path(metadata_path, str(output_dir))
            for key in (
                "sampled_cmg",
                "cmg",
                "sampled_prompt_bundle",
                "prompt_bundle",
                "sampled_mock_release_note",
                "mock_release_note",
            ):
                artifact_candidates.append(pipeline_artifacts.get(key))
        screening = metadata.get("screening")
        if isinstance(screening, dict):
            artifact_candidates.append(screening.get("stage1_output"))

        for candidate in artifact_candidates:
            if candidate:
                return cls._resolve_repo_relative_path(metadata_path, str(candidate)).parent
        raise ValueError(f"metadata is missing pipeline artifact paths: {metadata_path}")

    @staticmethod
    def _resolve_repo_relative_path(metadata_path: Path, raw_path: str) -> Path:
        path = Path(raw_path)
        if path.is_absolute():
            return path
        current = metadata_path.resolve()
        for parent in current.parents:
            if (parent / path).exists():
                return parent / path
        return Path.cwd() / path

    @staticmethod
    def _read_json(path: Path) -> dict[str, object]:
        if not path.exists():
            raise FileNotFoundError(f"Metadata file not found: {path}")
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
        if not isinstance(payload, dict):
            raise ValueError(f"JSON payload must be an object: {path}")
        return payload

    @staticmethod
    def _write_json(path: Path, payload: object) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def _summary_value(summary: object, key: str) -> object:
        if not isinstance(summary, dict):
            return None
        return summary.get(key)


class EvaluationSummaryBuilder:
    def __init__(
        self,
        *,
        metadata_paths: list[str | Path],
        variants: list[str] | None = None,
        evaluation_filename: str = "evaluation.json",
        baseline_root_name: str = "baselines",
    ) -> None:
        if not metadata_paths:
            raise ValueError("At least one case metadata path is required.")
        self.metadata_paths = [Path(path) for path in metadata_paths]
        self.variants = BaselineEvaluationRunner._normalize_variants(variants)
        self.evaluation_filename = evaluation_filename
        self.baseline_root_name = baseline_root_name

    def build_payload(self) -> dict[str, object]:
        rows: list[dict[str, object]] = []
        for metadata_path in self.metadata_paths:
            metadata = BaselineEvaluationRunner._read_json(metadata_path)
            case_id = str(metadata.get("case_id", metadata_path.parent.name))
            output_dir = BaselineEvaluationRunner._resolve_output_dir(metadata_path, metadata)
            for variant in self.variants:
                evaluation_path = output_dir / self.baseline_root_name / variant / self.evaluation_filename
                if not evaluation_path.exists():
                    rows.append(
                        {
                            "case_id": case_id,
                            "variant": variant,
                            "status": "missing_evaluation",
                            "ground_truth_count": None,
                            "generated_count": None,
                            "valid_match_count": None,
                            "matched_generated_count": None,
                            "matched_ground_truth_count": None,
                            "precision": None,
                            "recall": None,
                            "f1": None,
                            "unsupported_claim_rate": None,
                            "redundancy_count": None,
                            "redundancy_per_gt": None,
                            "avg_matches_per_gt": None,
                            "structural_valid_rate": None,
                            "evaluation_path": str(evaluation_path),
                        }
                    )
                    continue

                payload = BaselineEvaluationRunner._read_json(evaluation_path)
                summary = payload.get("summary")
                ground_truth_count = BaselineEvaluationRunner._summary_value(
                    summary,
                    "ground_truth_count",
                )
                valid_match_count = BaselineEvaluationRunner._summary_value(
                    summary,
                    "valid_match_count",
                )
                matched_generated_count = BaselineEvaluationRunner._summary_value(
                    summary,
                    "matched_generated_count",
                )
                matched_ground_truth_count = BaselineEvaluationRunner._summary_value(
                    summary,
                    "matched_ground_truth_count",
                )
                redundancy_count = BaselineEvaluationRunner._summary_value(
                    summary,
                    "redundancy_count",
                )
                redundancy_per_gt = BaselineEvaluationRunner._summary_value(
                    summary,
                    "redundancy_per_gt",
                )
                avg_matches_per_gt = BaselineEvaluationRunner._summary_value(
                    summary,
                    "avg_matches_per_gt",
                )
                if redundancy_per_gt is None:
                    redundancy_per_gt = self._ratio_or_none(
                        redundancy_count,
                        ground_truth_count,
                    )
                if avg_matches_per_gt is None:
                    avg_matches_per_gt = self._ratio_or_none(
                        valid_match_count,
                        ground_truth_count,
                    )
                rows.append(
                    {
                        "case_id": case_id,
                        "variant": variant,
                        "status": BaselineEvaluationRunner._summary_value(
                            summary,
                            "evaluation_status",
                        ),
                        "ground_truth_count": ground_truth_count,
                        "generated_count": BaselineEvaluationRunner._summary_value(
                            summary,
                            "generated_count",
                        ),
                        "valid_match_count": valid_match_count,
                        "matched_generated_count": matched_generated_count,
                        "matched_ground_truth_count": matched_ground_truth_count,
                        "precision": BaselineEvaluationRunner._summary_value(summary, "precision"),
                        "recall": BaselineEvaluationRunner._summary_value(summary, "recall"),
                        "f1": BaselineEvaluationRunner._summary_value(summary, "f1"),
                        "unsupported_claim_rate": BaselineEvaluationRunner._summary_value(
                            summary,
                            "unsupported_claim_rate",
                        ),
                        "redundancy_count": redundancy_count,
                        "redundancy_per_gt": redundancy_per_gt,
                        "avg_matches_per_gt": avg_matches_per_gt,
                        "structural_valid_rate": BaselineEvaluationRunner._summary_value(
                            summary,
                            "structural_valid_rate",
                        ),
                        "evaluation_path": str(evaluation_path),
                    }
                )

        return {
            "source": {
                "builder": "evaluation-summary-builder-v3",
                "variants": self.variants,
            },
            "metadata_paths": [str(path) for path in self.metadata_paths],
            "rows": rows,
            "macro_averages": self._build_macro_averages(rows),
            "micro_averages": self._build_micro_averages(rows),
        }

    @staticmethod
    def _ratio_or_none(numerator: object, denominator: object) -> float | None:
        if not isinstance(numerator, (int, float)) or isinstance(numerator, bool):
            return None
        if not isinstance(denominator, (int, float)) or isinstance(denominator, bool):
            return None
        if denominator == 0:
            return None
        return round(numerator / denominator, 4)

    @staticmethod
    def render_markdown(payload: dict[str, object]) -> str:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            rows = []
        lines = [
            "# Evaluation Summary",
            "",
            "| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |",
            "| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            if not isinstance(row, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('case_id', '')}`",
                        f"`{row.get('variant', '')}`",
                        f"`{row.get('status', '')}`",
                        EvaluationSummaryBuilder._format_cell(row.get("ground_truth_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("generated_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("precision")),
                        EvaluationSummaryBuilder._format_cell(row.get("recall")),
                        EvaluationSummaryBuilder._format_cell(row.get("f1")),
                        EvaluationSummaryBuilder._format_cell(row.get("unsupported_claim_rate")),
                        EvaluationSummaryBuilder._format_cell(row.get("avg_matches_per_gt")),
                        EvaluationSummaryBuilder._format_cell(row.get("redundancy_per_gt")),
                        EvaluationSummaryBuilder._format_cell(row.get("structural_valid_rate")),
                    ]
                )
                + " |"
            )

        macro_averages = payload.get("macro_averages")
        if isinstance(macro_averages, list) and macro_averages:
            lines.extend(
                [
                    "",
                    "## Macro Averages",
                    "",
                    "| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |",
                    "| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
                ]
            )
            for row in macro_averages:
                if not isinstance(row, dict):
                    continue
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            f"`{row.get('variant', '')}`",
                            EvaluationSummaryBuilder._format_cell(row.get("evaluated_cases")),
                            EvaluationSummaryBuilder._format_cell(row.get("precision")),
                            EvaluationSummaryBuilder._format_cell(row.get("recall")),
                            EvaluationSummaryBuilder._format_cell(row.get("f1")),
                            EvaluationSummaryBuilder._format_cell(row.get("unsupported_claim_rate")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_matches_per_gt")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_redundancy_per_gt")),
                            EvaluationSummaryBuilder._format_cell(row.get("structural_valid_rate")),
                        ]
                    )
                    + " |"
                )

        micro_averages = payload.get("micro_averages")
        if isinstance(micro_averages, list) and micro_averages:
            lines.extend(
                [
                    "",
                    "## Micro Averages",
                    "",
                    "| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |",
                    "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
                ]
            )
            for row in micro_averages:
                if not isinstance(row, dict):
                    continue
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            f"`{row.get('variant', '')}`",
                            EvaluationSummaryBuilder._format_cell(row.get("evaluated_cases")),
                            EvaluationSummaryBuilder._format_cell(row.get("precision")),
                            EvaluationSummaryBuilder._format_cell(row.get("recall")),
                            EvaluationSummaryBuilder._format_cell(row.get("f1")),
                            EvaluationSummaryBuilder._format_cell(row.get("matches_per_gt")),
                            EvaluationSummaryBuilder._format_cell(row.get("redundancy_per_gt")),
                        ]
                    )
                    + " |"
                )

        lines.extend(
            [
                "",
                "Notes:",
                "",
                "- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.",
                "- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.",
            ]
        )
        return "\n".join(lines) + "\n"

    def _build_macro_averages(self, rows: list[dict[str, object]]) -> list[dict[str, object]]:
        macro_rows: list[dict[str, object]] = []
        for variant in self.variants:
            evaluated_rows = [
                row
                for row in rows
                if row.get("variant") == variant and row.get("status") == "evaluated"
            ]
            macro_rows.append(
                {
                    "variant": variant,
                    "evaluated_cases": len(evaluated_rows),
                    "precision": self._mean_metric(evaluated_rows, "precision"),
                    "recall": self._mean_metric(evaluated_rows, "recall"),
                    "f1": self._mean_metric(evaluated_rows, "f1"),
                    "unsupported_claim_rate": self._mean_metric(
                        evaluated_rows,
                        "unsupported_claim_rate",
                    ),
                    "avg_redundancy_count": self._mean_metric(
                        evaluated_rows,
                        "redundancy_count",
                    ),
                    "avg_redundancy_per_gt": self._mean_metric(
                        evaluated_rows,
                        "redundancy_per_gt",
                    ),
                    "avg_matches_per_gt": self._mean_metric(
                        evaluated_rows,
                        "avg_matches_per_gt",
                    ),
                    "structural_valid_rate": self._mean_metric(
                        evaluated_rows,
                        "structural_valid_rate",
                    ),
                }
            )
        return macro_rows

    def _build_micro_averages(self, rows: list[dict[str, object]]) -> list[dict[str, object]]:
        micro_rows: list[dict[str, object]] = []
        for variant in self.variants:
            evaluated_rows = [
                row
                for row in rows
                if row.get("variant") == variant and row.get("status") == "evaluated"
            ]
            generated_count = self._sum_metric(evaluated_rows, "generated_count")
            ground_truth_count = self._sum_metric(evaluated_rows, "ground_truth_count")
            matched_generated_count = self._sum_metric(
                evaluated_rows,
                "matched_generated_count",
            )
            matched_ground_truth_count = self._sum_metric(
                evaluated_rows,
                "matched_ground_truth_count",
            )
            valid_match_count = self._sum_metric(evaluated_rows, "valid_match_count")
            redundancy_count = self._sum_metric(evaluated_rows, "redundancy_count")
            precision = (
                matched_generated_count / generated_count
                if generated_count
                else None
            )
            recall = (
                matched_ground_truth_count / ground_truth_count
                if ground_truth_count
                else None
            )
            f1 = (
                2 * precision * recall / (precision + recall)
                if precision is not None and recall is not None and precision + recall
                else None
            )
            micro_rows.append(
                {
                    "variant": variant,
                    "evaluated_cases": len(evaluated_rows),
                    "generated_count": generated_count,
                    "ground_truth_count": ground_truth_count,
                    "matched_generated_count": matched_generated_count,
                    "matched_ground_truth_count": matched_ground_truth_count,
                    "valid_match_count": valid_match_count,
                    "redundancy_count": redundancy_count,
                    "precision": round(precision, 4) if precision is not None else None,
                    "recall": round(recall, 4) if recall is not None else None,
                    "f1": round(f1, 4) if f1 is not None else None,
                    "matches_per_gt": (
                        round(valid_match_count / ground_truth_count, 4)
                        if ground_truth_count
                        else None
                    ),
                    "redundancy_per_gt": (
                        round(redundancy_count / ground_truth_count, 4)
                        if ground_truth_count
                        else None
                    ),
                }
            )
        return micro_rows

    @staticmethod
    def _mean_metric(rows: list[dict[str, object]], key: str) -> float | None:
        values: list[float] = []
        for row in rows:
            value = row.get(key)
            if isinstance(value, bool):
                continue
            if isinstance(value, (int, float)):
                values.append(float(value))
        if not values:
            return None
        return round(sum(values) / len(values), 4)

    @staticmethod
    def _sum_metric(rows: list[dict[str, object]], key: str) -> float:
        total = 0.0
        for row in rows:
            value = row.get(key)
            if isinstance(value, bool):
                continue
            if isinstance(value, (int, float)):
                total += float(value)
        return total

    @staticmethod
    def _format_cell(value: object) -> str:
        if value is None:
            return ""
        if isinstance(value, float):
            return f"{value:.4f}"
        return str(value)


class BaselineOutputSummaryBuilder:
    def __init__(
        self,
        *,
        metadata_paths: list[str | Path],
        variants: list[str] | None = None,
        baseline_root_name: str = "baselines",
    ) -> None:
        if not metadata_paths:
            raise ValueError("At least one case metadata path is required.")
        self.metadata_paths = [Path(path) for path in metadata_paths]
        self.variants = BaselineEvaluationRunner._normalize_variants(variants)
        self.baseline_root_name = baseline_root_name

    def build_payload(self) -> dict[str, object]:
        rows: list[dict[str, object]] = []
        for metadata_path in self.metadata_paths:
            metadata = BaselineEvaluationRunner._read_json(metadata_path)
            case_id = str(metadata.get("case_id", metadata_path.parent.name))
            output_dir = BaselineEvaluationRunner._resolve_output_dir(metadata_path, metadata)
            for variant in self.variants:
                variant_dir = output_dir / self.baseline_root_name / variant
                release_note_path = variant_dir / "release_note.json"
                prompt_input_path = variant_dir / "prompt_input.json"
                row = self._build_row(
                    case_id=case_id,
                    variant=variant,
                    release_note_path=release_note_path,
                    prompt_input_path=prompt_input_path,
                )
                rows.append(row)

        return {
            "source": {
                "builder": "baseline-output-summary-builder-v1",
                "variants": self.variants,
            },
            "metadata_paths": [str(path) for path in self.metadata_paths],
            "rows": rows,
            "macro_averages": self._build_macro_averages(rows),
        }

    def _build_row(
        self,
        *,
        case_id: str,
        variant: str,
        release_note_path: Path,
        prompt_input_path: Path,
    ) -> dict[str, object]:
        if not release_note_path.exists():
            return {
                "case_id": case_id,
                "variant": variant,
                "status": "missing_release_note",
                "release_note_path": str(release_note_path),
                "prompt_input_path": str(prompt_input_path),
            }

        payload = BaselineEvaluationRunner._read_json(release_note_path)
        summary = payload.get("summary")
        entries = payload.get("entries")
        generated_entries = entries if isinstance(entries, list) else []
        structured_release_notes = self._list_value(payload, "structured_release_notes")
        aggregated_release_notes = self._list_value(payload, "aggregated_release_notes")
        deduplicated_release_notes = self._list_value(payload, "deduplicated_release_notes")
        prompt_summary = self._read_prompt_summary(prompt_input_path)

        entry_count = self._int_value(summary, "entry_count", default=len(generated_entries))
        generated_entry_count = self._int_value(
            summary,
            "generated_entry_count",
            default=self._count_generated_entries(generated_entries),
        )
        release_note_count = self._int_value(
            summary,
            "deduplicated_release_note_count",
            default=len(deduplicated_release_notes),
        )
        usage = self._sum_usage(generated_entries)
        compression_ratio = self._ratio(release_note_count, generated_entry_count)
        reduction_rate = None if compression_ratio is None else round(1 - compression_ratio, 4)

        return {
            "case_id": case_id,
            "variant": variant,
            "status": "summarized",
            "aggregation_strategy": self._summary_value(summary, "aggregation_strategy"),
            "prompt_entry_count": self._summary_value(prompt_summary, "entry_count") or entry_count,
            "matched_entry_count": self._summary_value(prompt_summary, "matched_entry_count"),
            "unmatched_entry_count": self._summary_value(prompt_summary, "unmatched_entry_count"),
            "entry_count": entry_count,
            "generated_entry_count": generated_entry_count,
            "failed_entry_count": self._int_value(summary, "failed_entry_count", default=0),
            "structured_release_note_count": len(structured_release_notes),
            "aggregated_release_note_count": len(aggregated_release_notes),
            "deduplicated_release_note_count": release_note_count,
            "compression_ratio": compression_ratio,
            "reduction_rate": reduction_rate,
            "prompt_tokens": usage["prompt_tokens"],
            "completion_tokens": usage["completion_tokens"],
            "total_tokens": usage["total_tokens"],
            "release_note_path": str(release_note_path),
            "prompt_input_path": str(prompt_input_path),
        }

    @staticmethod
    def render_markdown(payload: dict[str, object]) -> str:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            rows = []
        lines = [
            "# Baseline Output Summary",
            "",
            "| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |",
            "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            if not isinstance(row, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('case_id', '')}`",
                        f"`{row.get('variant', '')}`",
                        f"`{row.get('status', '')}`",
                        f"`{row.get('aggregation_strategy', '')}`",
                        EvaluationSummaryBuilder._format_cell(row.get("prompt_entry_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("generated_entry_count")),
                        EvaluationSummaryBuilder._format_cell(
                            row.get("deduplicated_release_note_count")
                        ),
                        EvaluationSummaryBuilder._format_cell(row.get("compression_ratio")),
                        EvaluationSummaryBuilder._format_cell(row.get("reduction_rate")),
                        EvaluationSummaryBuilder._format_cell(row.get("total_tokens")),
                    ]
                )
                + " |"
            )

        macro_averages = payload.get("macro_averages")
        if isinstance(macro_averages, list) and macro_averages:
            lines.extend(
                [
                    "",
                    "## Macro Averages",
                    "",
                    "| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |",
                    "| --- | ---: | ---: | ---: | ---: | ---: | ---: |",
                ]
            )
            for row in macro_averages:
                if not isinstance(row, dict):
                    continue
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            f"`{row.get('variant', '')}`",
                            EvaluationSummaryBuilder._format_cell(row.get("summarized_cases")),
                            EvaluationSummaryBuilder._format_cell(
                                row.get("avg_generated_entry_count")
                            ),
                            EvaluationSummaryBuilder._format_cell(
                                row.get("avg_deduplicated_release_note_count")
                            ),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_compression_ratio")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_reduction_rate")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_total_tokens")),
                        ]
                    )
                    + " |"
                )

        lines.extend(
            [
                "",
                "Notes:",
                "",
                "- Compression is `final release-note count / generated entry count`; lower means more aggregation.",
                "- Reduction is `1 - compression`; higher means more generated entries were merged or removed.",
            ]
        )
        return "\n".join(lines) + "\n"

    def _build_macro_averages(self, rows: list[dict[str, object]]) -> list[dict[str, object]]:
        macro_rows: list[dict[str, object]] = []
        for variant in self.variants:
            summarized_rows = [
                row
                for row in rows
                if row.get("variant") == variant and row.get("status") == "summarized"
            ]
            macro_rows.append(
                {
                    "variant": variant,
                    "summarized_cases": len(summarized_rows),
                    "avg_generated_entry_count": EvaluationSummaryBuilder._mean_metric(
                        summarized_rows,
                        "generated_entry_count",
                    ),
                    "avg_deduplicated_release_note_count": EvaluationSummaryBuilder._mean_metric(
                        summarized_rows,
                        "deduplicated_release_note_count",
                    ),
                    "avg_compression_ratio": EvaluationSummaryBuilder._mean_metric(
                        summarized_rows,
                        "compression_ratio",
                    ),
                    "avg_reduction_rate": EvaluationSummaryBuilder._mean_metric(
                        summarized_rows,
                        "reduction_rate",
                    ),
                    "avg_total_tokens": EvaluationSummaryBuilder._mean_metric(
                        summarized_rows,
                        "total_tokens",
                    ),
                }
            )
        return macro_rows

    @staticmethod
    def _read_prompt_summary(path: Path) -> dict[str, object]:
        if not path.exists():
            return {}
        payload = BaselineEvaluationRunner._read_json(path)
        summary = payload.get("summary")
        return summary if isinstance(summary, dict) else {}

    @staticmethod
    def _sum_usage(entries: list[object]) -> dict[str, int]:
        totals = {
            "prompt_tokens": 0,
            "completion_tokens": 0,
            "total_tokens": 0,
        }
        for entry in entries:
            if not isinstance(entry, dict):
                continue
            usage = entry.get("usage")
            if not isinstance(usage, dict):
                continue
            for key in totals:
                value = usage.get(key)
                if isinstance(value, int):
                    totals[key] += value
        return totals

    @staticmethod
    def _list_value(payload: dict[str, object], key: str) -> list[object]:
        value = payload.get(key)
        return value if isinstance(value, list) else []

    @staticmethod
    def _count_generated_entries(entries: list[object]) -> int:
        return sum(
            1
            for entry in entries
            if isinstance(entry, dict) and entry.get("status") == "generated"
        )

    @staticmethod
    def _int_value(summary: object, key: str, *, default: int) -> int:
        value = BaselineOutputSummaryBuilder._summary_value(summary, key)
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        return default

    @staticmethod
    def _summary_value(summary: object, key: str) -> object:
        if not isinstance(summary, dict):
            return None
        return summary.get(key)

    @staticmethod
    def _ratio(numerator: int, denominator: int) -> float | None:
        if denominator == 0:
            return None
        return round(numerator / denominator, 4)


class AggregationComparisonBuilder:
    SUPPORTED_STRATEGIES = (
        "none",
        "exact",
        "rule_family",
        "similarity_family",
        "evidence_similarity_family",
        "salience_similarity_family",
    )

    def __init__(
        self,
        *,
        metadata_paths: list[str | Path],
        variants: list[str] | None = None,
        baseline_root_name: str = "baselines",
        strategies: list[str] | None = None,
    ) -> None:
        if not metadata_paths:
            raise ValueError("At least one case metadata path is required.")
        self.metadata_paths = [Path(path) for path in metadata_paths]
        self.variants = BaselineEvaluationRunner._normalize_variants(variants)
        self.baseline_root_name = baseline_root_name
        self.strategies = self._normalize_strategies(strategies)

    def build_payload(self) -> dict[str, object]:
        rows: list[dict[str, object]] = []
        for metadata_path in self.metadata_paths:
            metadata = BaselineEvaluationRunner._read_json(metadata_path)
            case_id = str(metadata.get("case_id", metadata_path.parent.name))
            output_dir = BaselineEvaluationRunner._resolve_output_dir(metadata_path, metadata)
            for variant in self.variants:
                release_note_path = output_dir / self.baseline_root_name / variant / "release_note.json"
                rows.extend(
                    self._build_rows_for_release_note(
                        case_id=case_id,
                        variant=variant,
                        release_note_path=release_note_path,
                    )
                )

        return {
            "source": {
                "builder": "aggregation-comparison-builder-v1",
                "variants": self.variants,
                "strategies": self.strategies,
                "baseline_root_name": self.baseline_root_name,
            },
            "metadata_paths": [str(path) for path in self.metadata_paths],
            "rows": rows,
            "macro_averages": self._build_macro_averages(rows),
        }

    def _build_rows_for_release_note(
        self,
        *,
        case_id: str,
        variant: str,
        release_note_path: Path,
    ) -> list[dict[str, object]]:
        if not release_note_path.exists():
            return [
                {
                    "case_id": case_id,
                    "variant": variant,
                    "strategy": strategy,
                    "status": "missing_release_note",
                    "release_note_path": str(release_note_path),
                }
                for strategy in self.strategies
            ]

        payload = BaselineEvaluationRunner._read_json(release_note_path)
        entries = payload.get("entries")
        generated_entries = entries if isinstance(entries, list) else []
        generated_count = sum(
            1
            for entry in generated_entries
            if isinstance(entry, dict) and entry.get("status") == "generated"
        )
        structured_notes = ReleaseNoteGenerator._aggregate_structured_notes(generated_entries)

        rows: list[dict[str, object]] = []
        for strategy in self.strategies:
            aggregated_notes = ReleaseNoteGenerator._build_release_notes_for_strategy(
                generated_entries=generated_entries,
                structured_notes=structured_notes,
                strategy=strategy,
            )
            final_count = len(aggregated_notes)
            compression_ratio = BaselineOutputSummaryBuilder._ratio(final_count, generated_count)
            reduction_rate = None if compression_ratio is None else round(1 - compression_ratio, 4)
            merged_groups = [
                note
                for note in aggregated_notes
                if isinstance(note, dict) and self._source_note_count(note) > 1
            ]
            rows.append(
                {
                    "case_id": case_id,
                    "variant": variant,
                    "strategy": strategy,
                    "status": "summarized",
                    "generated_entry_count": generated_count,
                    "exact_structured_note_count": len(structured_notes),
                    "final_release_note_count": final_count,
                    "compression_ratio": compression_ratio,
                    "reduction_rate": reduction_rate,
                    "merged_group_count": len(merged_groups),
                    "max_source_note_count": max(
                        [self._source_note_count(note) for note in aggregated_notes],
                        default=0,
                    ),
                    "release_note_path": str(release_note_path),
                }
            )
        return rows

    @staticmethod
    def render_markdown(payload: dict[str, object]) -> str:
        rows = payload.get("rows")
        if not isinstance(rows, list):
            rows = []
        lines = [
            "# Aggregation Strategy Summary",
            "",
            "| Case | Variant | Strategy | Status | Generated | Exact Notes | Final Notes | Compression | Reduction | Merged Groups | Max Group Size |",
            "| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
        ]
        for row in rows:
            if not isinstance(row, dict):
                continue
            lines.append(
                "| "
                + " | ".join(
                    [
                        f"`{row.get('case_id', '')}`",
                        f"`{row.get('variant', '')}`",
                        f"`{row.get('strategy', '')}`",
                        f"`{row.get('status', '')}`",
                        EvaluationSummaryBuilder._format_cell(row.get("generated_entry_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("exact_structured_note_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("final_release_note_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("compression_ratio")),
                        EvaluationSummaryBuilder._format_cell(row.get("reduction_rate")),
                        EvaluationSummaryBuilder._format_cell(row.get("merged_group_count")),
                        EvaluationSummaryBuilder._format_cell(row.get("max_source_note_count")),
                    ]
                )
                + " |"
            )

        macro_averages = payload.get("macro_averages")
        if isinstance(macro_averages, list) and macro_averages:
            lines.extend(
                [
                    "",
                    "## Macro Averages",
                    "",
                    "| Variant | Strategy | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Merged Groups | Avg Max Group Size |",
                    "| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |",
                ]
            )
            for row in macro_averages:
                if not isinstance(row, dict):
                    continue
                lines.append(
                    "| "
                    + " | ".join(
                        [
                            f"`{row.get('variant', '')}`",
                            f"`{row.get('strategy', '')}`",
                            EvaluationSummaryBuilder._format_cell(row.get("summarized_cases")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_generated_entry_count")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_final_release_note_count")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_compression_ratio")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_reduction_rate")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_merged_group_count")),
                            EvaluationSummaryBuilder._format_cell(row.get("avg_max_source_note_count")),
                        ]
                    )
                    + " |"
                )

        lines.extend(
            [
                "",
                "Notes:",
                "",
                "- `none` keeps one final note per generated entry.",
                "- `exact` merges only exactly identical structured notes.",
                "- `rule_family` applies the current heuristic family grouping.",
                "- `similarity_family` groups notes with conservative token and symbol overlap.",
                "- `evidence_similarity_family` additionally requires source-symbol, entity, or file evidence.",
                "- Compression is `final release-note count / generated entry count`; lower means stronger aggregation.",
            ]
        )
        return "\n".join(lines) + "\n"

    def _build_macro_averages(self, rows: list[dict[str, object]]) -> list[dict[str, object]]:
        macro_rows: list[dict[str, object]] = []
        for variant in self.variants:
            for strategy in self.strategies:
                summarized_rows = [
                    row
                    for row in rows
                    if row.get("variant") == variant
                    and row.get("strategy") == strategy
                    and row.get("status") == "summarized"
                ]
                macro_rows.append(
                    {
                        "variant": variant,
                        "strategy": strategy,
                        "summarized_cases": len(summarized_rows),
                        "avg_generated_entry_count": EvaluationSummaryBuilder._mean_metric(
                            summarized_rows,
                            "generated_entry_count",
                        ),
                        "avg_final_release_note_count": EvaluationSummaryBuilder._mean_metric(
                            summarized_rows,
                            "final_release_note_count",
                        ),
                        "avg_compression_ratio": EvaluationSummaryBuilder._mean_metric(
                            summarized_rows,
                            "compression_ratio",
                        ),
                        "avg_reduction_rate": EvaluationSummaryBuilder._mean_metric(
                            summarized_rows,
                            "reduction_rate",
                        ),
                        "avg_merged_group_count": EvaluationSummaryBuilder._mean_metric(
                            summarized_rows,
                            "merged_group_count",
                        ),
                        "avg_max_source_note_count": EvaluationSummaryBuilder._mean_metric(
                            summarized_rows,
                            "max_source_note_count",
                        ),
                    }
                )
        return macro_rows

    @classmethod
    def _normalize_strategies(cls, strategies: list[str] | None) -> list[str]:
        if not strategies:
            return list(cls.SUPPORTED_STRATEGIES)
        normalized: list[str] = []
        for strategy in strategies:
            value = strategy.strip().lower().replace("-", "_")
            if value not in cls.SUPPORTED_STRATEGIES:
                allowed = ", ".join(cls.SUPPORTED_STRATEGIES)
                raise ValueError(f"Unsupported aggregation strategy: {strategy}. Expected one of: {allowed}.")
            if value not in normalized:
                normalized.append(value)
        return normalized

    @staticmethod
    def _source_note_count(note: object) -> int:
        if not isinstance(note, dict):
            return 0
        value = note.get("source_note_count")
        if isinstance(value, int):
            return value
        source_entry_ids = note.get("source_entry_ids") or note.get("entry_ids")
        if isinstance(source_entry_ids, list):
            return len(source_entry_ids)
        return 1

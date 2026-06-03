from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import AppConfig
from .pipeline.baseline_runner import BaselineRunner
from .pipeline.change_detection import ChangeDetector
from .pipeline.change_sampling import ChangedFunctionSampler, load_changed_functions
from .pipeline.benchmark_screening import VersionPairScreener
from .pipeline.cmg_builder import CmgBuilder
from .pipeline.demo_report import DemoReportBuilder
from .pipeline.enre_parser import EnreParser
from .pipeline.enre_runner import EnreRunner
from .pipeline.evaluation import ReleaseNoteEvaluator
from .pipeline.evaluation_runner import (
    AggregationComparisonBuilder,
    BaselineEvaluationRunner,
    BaselineOutputSummaryBuilder,
    EvaluationSummaryBuilder,
)
from .pipeline.experiment_report import ExperimentReportBuilder
from .pipeline.ground_truth_evidence import GroundTruthEvidenceBuilder
from .pipeline.prompt_builder import SUPPORTED_PROMPT_VARIANTS, PromptBundleBuilder
from .pipeline.release_note_generation import ReleaseNoteGenerator
from .pipeline.version_snapshot import VersionSnapshotManager
from .pipeline.visual_report import VisualReportBuilder


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="C/C++ release note MVP CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    detect_parser = subparsers.add_parser("detect-changes", help="Detect changed functions for one version pair")
    detect_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    detect_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for changed_functions.json; defaults to <output_dir>/changed_functions.json",
    )

    sample_parser = subparsers.add_parser(
        "sample-changed-functions",
        help="Build a deterministic sampled changed_functions.json for large stress cases",
    )
    sample_parser.add_argument("--input", required=True, help="Path to the source changed_functions.json")
    sample_parser.add_argument("--output", required=True, help="Path to the sampled changed_functions.json")
    sample_parser.add_argument(
        "--summary-output",
        default=None,
        help="Optional Markdown summary path for the sampling result",
    )
    sample_parser.add_argument(
        "--max-functions",
        type=int,
        default=80,
        help="Maximum number of changed functions to keep; defaults to 80",
    )
    sample_parser.add_argument(
        "--max-per-file",
        type=int,
        default=5,
        help="Maximum sampled functions per file; defaults to 5",
    )
    sample_parser.add_argument(
        "--strategy",
        choices=("stratified_file_round_robin",),
        default="stratified_file_round_robin",
        help="Sampling strategy; defaults to deterministic file-stratified round robin",
    )

    screen_parser = subparsers.add_parser(
        "screen-version-pairs",
        help="Screen adjacent repository tags for benchmark candidate selection",
    )
    screen_parser.add_argument("--config", required=True, help="Path to a JSON config for the target repository")
    screen_parser.add_argument(
        "--tag-pattern",
        default="OpenHarmony-v*",
        help="Git tag pattern to screen; defaults to OpenHarmony-v*",
    )
    screen_parser.add_argument(
        "--recent-pairs",
        type=int,
        default=8,
        help="Number of latest adjacent tag pairs to screen; use 0 to screen all pairs",
    )
    screen_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for screening JSON; prints to stdout if omitted",
    )
    screen_parser.add_argument(
        "--max-symbols-per-pair",
        type=int,
        default=25,
        help="Maximum changed-symbol samples to keep for each screened pair",
    )

    snapshot_parser = subparsers.add_parser(
        "prepare-snapshots",
        help="Create or reuse git worktree snapshots for the configured ref/tgt versions",
    )
    snapshot_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    snapshot_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for snapshot metadata JSON; prints to stdout if omitted",
    )

    enre_parser = subparsers.add_parser(
        "run-enre",
        help="Run ENRE-CPP on prepared snapshots for ref, tgt, or both versions",
    )
    enre_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    enre_parser.add_argument(
        "--target",
        choices=("ref", "tgt", "both"),
        default="both",
        help="Which snapshot(s) to analyze",
    )
    enre_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for ENRE run metadata JSON; prints to stdout if omitted",
    )

    normalize_enre_parser = subparsers.add_parser(
        "parse-enre",
        help="Normalize one ENRE raw JSON file into the internal graph schema",
    )
    normalize_enre_parser.add_argument("--input", required=True, help="Path to the ENRE raw JSON file")
    normalize_enre_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for normalized ENRE JSON; defaults next to the input file",
    )

    cmg_parser = subparsers.add_parser(
        "build-cmg",
        help="Build 1-hop CMG entries by chaining change detection, ENRE execution, normalization, and matching",
    )
    cmg_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    cmg_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for cmg.json; defaults to <output_dir>/cmg.json",
    )
    cmg_parser.add_argument(
        "--cmg-strategy",
        choices=("strict_1hop", "adaptive"),
        default=None,
        help="Optional CMG strategy override for ablation runs.",
    )
    cmg_parser.add_argument(
        "--matching-view",
        choices=("strict", "rich"),
        default=None,
        help="Optional matching-view override. rich uses matching-only ENRE entities before prompt-graph slicing.",
    )
    cmg_parser.add_argument(
        "--changed-input",
        default=None,
        help="Optional existing changed_functions.json path; requires both normalized graph inputs.",
    )
    cmg_parser.add_argument(
        "--ref-normalized-graph-input",
        default=None,
        help="Optional existing normalized ENRE graph for the reference version.",
    )
    cmg_parser.add_argument(
        "--tgt-normalized-graph-input",
        default=None,
        help="Optional existing normalized ENRE graph for the target version.",
    )

    prompt_parser = subparsers.add_parser(
        "build-prompts",
        help="Build prompt_input.json and prompt_bundle.json from existing changed_functions.json and cmg.json",
    )
    prompt_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    prompt_parser.add_argument(
        "--changed-input",
        default=None,
        help="Optional input path for changed_functions.json; defaults to <output_dir>/changed_functions.json",
    )
    prompt_parser.add_argument(
        "--cmg-input",
        default=None,
        help="Optional input path for cmg.json; defaults to <output_dir>/cmg.json",
    )
    prompt_parser.add_argument(
        "--prompt-input-output",
        default=None,
        help="Optional output path for prompt_input.json; defaults to <output_dir>/prompt_input.json",
    )
    prompt_parser.add_argument(
        "--prompt-bundle-output",
        default=None,
        help="Optional output path for prompt_bundle.json; defaults to <output_dir>/prompt_bundle.json",
    )
    prompt_parser.add_argument(
        "--matched-only",
        action="store_true",
        help="Only generate prompts for matched CMG entries.",
    )
    prompt_parser.add_argument(
        "--prompt-variant",
        choices=SUPPORTED_PROMPT_VARIANTS,
        default="full",
        help=(
            "Prompt evidence variant for baseline/ablation runs: "
            "text_only, diff_only, no_graph, no_fallback, or full."
        ),
    )

    generation_parser = subparsers.add_parser(
        "generate-release-notes",
        help="Generate release_note.json and release_note.md from prompt_bundle.json",
    )
    generation_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    generation_parser.add_argument(
        "--prompt-bundle-input",
        default=None,
        help="Optional input path for prompt_bundle.json; defaults to <output_dir>/prompt_bundle.json",
    )
    generation_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional output path for release_note.json; defaults to <output_dir>/release_note.json",
    )
    generation_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional output path for release_note.md; defaults to <output_dir>/release_note.md",
    )
    generation_parser.add_argument(
        "--backend",
        choices=("mock", "openai", "openai-compatible"),
        default=None,
        help="Optional generation backend override.",
    )
    generation_parser.add_argument(
        "--model",
        default=None,
        help="Optional generation model override.",
    )
    generation_parser.add_argument(
        "--aggregation-strategy",
        choices=(
            "none",
            "exact",
            "rule_family",
            "similarity_family",
            "evidence_similarity_family",
            "salience_similarity_family",
        ),
        default=None,
        help="Optional release-note aggregation strategy override.",
    )

    reaggregate_parser = subparsers.add_parser(
        "rewrite-aggregation",
        help="Rewrite release_note.json aggregation fields without rerunning the LLM backend",
    )
    reaggregate_parser.add_argument("--input", required=True, help="Existing release_note.json path")
    reaggregate_parser.add_argument(
        "--aggregation-strategy",
        choices=(
            "none",
            "exact",
            "rule_family",
            "similarity_family",
            "evidence_similarity_family",
            "salience_similarity_family",
        ),
        required=True,
        help="Aggregation strategy to materialize.",
    )
    reaggregate_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional output path; defaults to release_note_<strategy>.json next to input.",
    )
    reaggregate_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional Markdown output path; defaults to release_note_<strategy>.md next to input.",
    )

    baseline_parser = subparsers.add_parser(
        "run-baselines",
        help="Build prompt bundles and release notes for baseline prompt variants",
    )
    baseline_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    baseline_parser.add_argument(
        "--variants",
        nargs="+",
        choices=SUPPORTED_PROMPT_VARIANTS,
        default=None,
        help="Baseline variants to run; defaults to all variants.",
    )
    baseline_parser.add_argument(
        "--changed-input",
        default=None,
        help="Optional input path for changed_functions.json; defaults to <output_dir>/changed_functions.json",
    )
    baseline_parser.add_argument(
        "--cmg-input",
        default=None,
        help="Optional input path for cmg.json; defaults to <output_dir>/cmg.json",
    )
    baseline_parser.add_argument(
        "--output-root",
        default=None,
        help="Output directory for variant subdirectories; defaults to <output_dir>/baselines",
    )
    baseline_parser.add_argument(
        "--summary-output",
        default=None,
        help="Optional output path for baseline_summary.json; defaults to <output-root>/baseline_summary.json",
    )
    baseline_parser.add_argument(
        "--backend",
        choices=("mock", "openai", "openai-compatible"),
        default=None,
        help="Optional generation backend override.",
    )
    baseline_parser.add_argument(
        "--model",
        default=None,
        help="Optional generation model override.",
    )
    baseline_parser.add_argument(
        "--aggregation-strategy",
        choices=(
            "none",
            "exact",
            "rule_family",
            "similarity_family",
            "evidence_similarity_family",
            "salience_similarity_family",
        ),
        default=None,
        help="Optional release-note aggregation strategy override.",
    )

    evidence_parser = subparsers.add_parser(
        "build-ground-truth-evidence",
        help="Build an evidence Markdown packet for ground-truth drafting",
    )
    evidence_parser.add_argument("--metadata", required=True, help="Path to benchmark case metadata.json")
    evidence_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path; defaults to evidence.md next to metadata.json",
    )
    evidence_parser.add_argument(
        "--max-functions",
        type=int,
        default=80,
        help="Maximum changed functions to include in the evidence table",
    )
    evidence_parser.add_argument(
        "--max-diff-lines-per-function",
        type=int,
        default=12,
        help="Maximum function-level diff lines to include per function",
    )

    evaluation_parser = subparsers.add_parser(
        "evaluate-release-notes",
        help="Prepare manual match templates or compute release-note evaluation metrics",
    )
    evaluation_parser.add_argument("--ground-truth", required=True, help="Path to ground_truth.md")
    evaluation_parser.add_argument("--release-note", required=True, help="Path to release_note.json")
    evaluation_parser.add_argument(
        "--matches",
        default=None,
        help="Optional manual matches JSON. If omitted, metrics are marked match_required.",
    )
    evaluation_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for evaluation JSON; defaults next to release_note.json",
    )
    evaluation_parser.add_argument(
        "--match-template-output",
        default=None,
        help="Optional output path for a standalone match template JSON.",
    )

    baseline_evaluation_parser = subparsers.add_parser(
        "evaluate-baselines",
        help="Prepare or compute evaluations for baseline outputs across benchmark cases",
    )
    baseline_evaluation_parser.add_argument(
        "--metadata",
        nargs="+",
        required=True,
        help="One or more benchmark case metadata.json paths.",
    )
    baseline_evaluation_parser.add_argument(
        "--variants",
        nargs="+",
        choices=SUPPORTED_PROMPT_VARIANTS,
        default=None,
        help="Baseline variants to evaluate; defaults to all variants.",
    )
    baseline_evaluation_parser.add_argument(
        "--matches-filename",
        default="matches.json",
        help="Manual match filename expected under each baseline variant directory.",
    )
    baseline_evaluation_parser.add_argument(
        "--evaluation-filename",
        default="evaluation.json",
        help="Evaluation output filename written under each baseline variant directory.",
    )
    baseline_evaluation_parser.add_argument(
        "--match-template-filename",
        default="match_template.json",
        help="Match-template filename written under each baseline variant directory.",
    )
    baseline_evaluation_parser.add_argument(
        "--baseline-root-name",
        default="baselines",
        help="Baseline root directory name under the case output dir.",
    )
    baseline_evaluation_parser.add_argument(
        "--summary-output",
        default=None,
        help="Optional batch summary JSON output path; prints summary only if omitted.",
    )

    evaluation_summary_parser = subparsers.add_parser(
        "summarize-evaluations",
        help="Build a JSON/Markdown summary table from baseline evaluation outputs",
    )
    evaluation_summary_parser.add_argument(
        "--metadata",
        nargs="+",
        required=True,
        help="One or more benchmark case metadata.json paths.",
    )
    evaluation_summary_parser.add_argument(
        "--variants",
        nargs="+",
        choices=SUPPORTED_PROMPT_VARIANTS,
        default=None,
        help="Baseline variants to summarize; defaults to all variants.",
    )
    evaluation_summary_parser.add_argument(
        "--evaluation-filename",
        default="evaluation.json",
        help="Evaluation filename under each baseline variant directory.",
    )
    evaluation_summary_parser.add_argument(
        "--baseline-root-name",
        default="baselines",
        help="Baseline root directory name under the case output dir.",
    )
    evaluation_summary_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional JSON summary output path.",
    )
    evaluation_summary_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional Markdown summary output path.",
    )

    baseline_summary_parser = subparsers.add_parser(
        "summarize-baseline-outputs",
        help="Build a JSON/Markdown summary table from generated baseline release-note outputs",
    )
    baseline_summary_parser.add_argument(
        "--metadata",
        nargs="+",
        required=True,
        help="One or more benchmark case metadata.json paths.",
    )
    baseline_summary_parser.add_argument(
        "--variants",
        nargs="+",
        choices=SUPPORTED_PROMPT_VARIANTS,
        default=None,
        help="Baseline variants to summarize; defaults to all variants.",
    )
    baseline_summary_parser.add_argument(
        "--baseline-root-name",
        default="baselines",
        help="Baseline root directory name under the case output dir.",
    )
    baseline_summary_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional JSON summary output path.",
    )
    baseline_summary_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional Markdown summary output path.",
    )

    aggregation_summary_parser = subparsers.add_parser(
        "summarize-aggregation",
        help="Compare aggregation strategies from existing release_note.json outputs without regenerating LLM text",
    )
    aggregation_summary_parser.add_argument(
        "--metadata",
        nargs="+",
        required=True,
        help="One or more benchmark case metadata.json paths.",
    )
    aggregation_summary_parser.add_argument(
        "--variants",
        nargs="+",
        choices=SUPPORTED_PROMPT_VARIANTS,
        default=None,
        help="Baseline variants to summarize; defaults to all variants.",
    )
    aggregation_summary_parser.add_argument(
        "--strategies",
        nargs="+",
        choices=AggregationComparisonBuilder.SUPPORTED_STRATEGIES,
        default=None,
        help=(
            "Aggregation strategies to compare; defaults to none, exact, rule_family, "
            "similarity_family, evidence_similarity_family, and salience_similarity_family."
        ),
    )
    aggregation_summary_parser.add_argument(
        "--baseline-root-name",
        default="baselines",
        help="Baseline root directory name under the case output dir.",
    )
    aggregation_summary_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional JSON summary output path.",
    )
    aggregation_summary_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional Markdown summary output path.",
    )

    experiment_matrix_parser = subparsers.add_parser(
        "summarize-experiments",
        help="Build a thesis-oriented core5 experiment matrix from existing summary JSON files",
    )
    experiment_matrix_parser.add_argument(
        "--benchmark-root",
        default="benchmark",
        help="Directory containing the core5 summary JSON files.",
    )
    experiment_matrix_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional JSON matrix output path.",
    )
    experiment_matrix_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional Markdown matrix output path.",
    )
    experiment_matrix_parser.add_argument(
        "--case-json-output",
        default=None,
        help="Optional JSON per-case result output path.",
    )
    experiment_matrix_parser.add_argument(
        "--case-markdown-output",
        default=None,
        help="Optional Markdown per-case result output path.",
    )

    visual_report_parser = subparsers.add_parser(
        "build-visual-report",
        help="Build a self-contained HTML report from benchmark result artifacts",
    )
    visual_report_parser.add_argument(
        "--benchmark-root",
        default="benchmark",
        help="Directory containing final_all_variant_matrix.json or core5_experiment_matrix.json.",
    )
    visual_report_parser.add_argument("--output", required=True, help="HTML report output path")
    visual_report_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional JSON payload output path for the rendered report.",
    )
    visual_report_parser.add_argument(
        "--matrix-input",
        default=None,
        help="Optional explicit matrix JSON path, for example benchmark/expanded_137gt_matrix.json.",
    )
    visual_report_parser.add_argument(
        "--cmg-input",
        default=None,
        help="Optional cmg.json path used to include a small CMG sample in the report.",
    )
    visual_report_parser.add_argument(
        "--cmg-coverage-input",
        default=None,
        help="Optional JSON file with Stage 2 CMG coverage comparison rows.",
    )
    visual_report_parser.add_argument(
        "--title",
        default="C/C++ Release Note Generation Experiment Report",
        help="Report title.",
    )

    demo_parser = subparsers.add_parser(
        "build-demo",
        help="Build a cached browser demo from existing pipeline artifacts",
    )
    demo_parser.add_argument(
        "--case",
        choices=("sqlite",),
        default="sqlite",
        help="Bundled demo case to render. Currently defaults to sqlite.",
    )
    demo_parser.add_argument(
        "--mode",
        choices=("cached",),
        default="cached",
        help="Demo execution mode. Cached mode does not rerun Git, ENRE, or LLM calls.",
    )
    demo_parser.add_argument(
        "--output",
        default="outputs/demo/sqlite_demo",
        help="Output directory for index.html, run_log.md, and packaged artifacts.",
    )
    demo_parser.add_argument(
        "--benchmark-root",
        default="benchmark",
        help="Directory containing core5_experiment_matrix.json and cmg_coverage_core5.json.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "detect-changes":
        config = AppConfig.from_json_file(args.config)
        detector = ChangeDetector(config)
        payload = detector.detect_as_payload()

        output_path = args.output
        if output_path is None:
            if config.output_dir is None:
                raise ValueError("Either --output or config.output_dir must be provided.")
            output_path = str(Path(config.output_dir) / "changed_functions.json")

        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    if args.command == "sample-changed-functions":
        source_path = Path(args.input)
        payload = load_changed_functions(source_path)
        sampler = ChangedFunctionSampler(
            payload,
            max_functions=args.max_functions,
            max_per_file=args.max_per_file,
            strategy=args.strategy,
        )
        sampled_payload = sampler.build_payload(source_path=str(source_path))

        output_path = Path(args.output)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps(sampled_payload, ensure_ascii=False, indent=2), encoding="utf-8")

        if args.summary_output:
            summary_path = Path(args.summary_output)
            summary_path.parent.mkdir(parents=True, exist_ok=True)
            summary_path.write_text(sampler.build_markdown_summary(sampled_payload), encoding="utf-8")

        print(
            json.dumps(
                {
                    "source_item_count": sampled_payload.get("sampling", {}).get("source_item_count"),
                    "sampled_item_count": sampled_payload.get("sampling", {}).get("sampled_item_count"),
                    "sampled_file_count": sampled_payload.get("sampling", {}).get("sampled_file_count"),
                    "output": str(output_path),
                    "summary_output": args.summary_output,
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "screen-version-pairs":
        config = AppConfig.from_json_file(args.config)
        recent_pairs = args.recent_pairs if args.recent_pairs and args.recent_pairs > 0 else None
        screener = VersionPairScreener(
            config,
            tag_pattern=args.tag_pattern,
            recent_pairs=recent_pairs,
            max_symbols_per_pair=max(args.max_symbols_per_pair, 0),
        )
        payload = screener.screen()

        if args.output:
            target = Path(args.output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "prepare-snapshots":
        config = AppConfig.from_json_file(args.config)
        manager = VersionSnapshotManager.from_app_config(config)
        payload = manager.ensure_version_pair_payload(config.version_pair)

        if args.output:
            target = Path(args.output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "run-enre":
        config = AppConfig.from_json_file(args.config)
        snapshot_manager = VersionSnapshotManager.from_app_config(config)
        snapshot_pair = snapshot_manager.ensure_version_pair(config.version_pair)
        runner = EnreRunner.from_app_config(config)
        payload = runner.run_for_pair(snapshot_pair, target=args.target)

        if args.output:
            target = Path(args.output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "parse-enre":
        parser = EnreParser()
        graph = parser.parse_json_file(args.input)
        payload = graph.to_dict()

        output_path = args.output
        if output_path is None:
            source_path = Path(args.input)
            output_path = str(source_path.with_name(f"{source_path.stem}_normalized.json"))

        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
        return

    if args.command == "build-cmg":
        config = AppConfig.from_json_file(args.config)
        if args.cmg_strategy:
            config.cmg.strategy = args.cmg_strategy
        if args.matching_view:
            config.cmg.matching_view = args.matching_view
        config.cmg.validate()
        if config.output_dir is None and args.output is None:
            raise ValueError("Either --output or config.output_dir must be provided for build-cmg.")

        artifact_inputs = [
            args.changed_input,
            args.ref_normalized_graph_input,
            args.tgt_normalized_graph_input,
        ]
        if any(artifact_inputs) and not all(artifact_inputs):
            raise ValueError(
                "--changed-input, --ref-normalized-graph-input, and "
                "--tgt-normalized-graph-input must be supplied together."
            )

        if args.changed_input:
            changed_output_path = Path(args.changed_input)
            changed_payload = _read_json(changed_output_path)
            normalized_paths = {
                "ref": Path(args.ref_normalized_graph_input),
                "tgt": Path(args.tgt_normalized_graph_input),
            }
            normalized_graphs = {
                "ref": _read_json(normalized_paths["ref"]),
                "tgt": _read_json(normalized_paths["tgt"]),
            }
        else:
            changed_payload = ChangeDetector(config).detect_as_payload()
            changed_output_path = _resolve_output_path(
                args_output=None,
                config_output_dir=config.output_dir,
                default_filename="changed_functions.json",
            )
            _write_json(changed_output_path, changed_payload)

            snapshot_manager = VersionSnapshotManager.from_app_config(config)
            snapshot_pair = snapshot_manager.ensure_version_pair(config.version_pair)
            runner = EnreRunner.from_app_config(config)
            run_payload = runner.run_for_pair(snapshot_pair, target="both")

            normalized_paths: dict[str, Path] = {}
            parser_impl = EnreParser()
            normalized_graphs: dict[str, dict[str, object]] = {}
            for side in ("ref", "tgt"):
                side_run = run_payload["runs"][side]
                raw_output_path = Path(str(side_run["output_json_path"]))
                graph = parser_impl.parse_json_file(raw_output_path)
                normalized_payload = graph.to_dict()
                normalized_path = raw_output_path.with_name(f"{raw_output_path.stem}_normalized.json")
                _write_json(normalized_path, normalized_payload)
                normalized_paths[side] = normalized_path
                normalized_graphs[side] = normalized_payload

        builder = CmgBuilder(
            changed_functions=list(changed_payload.get("items", [])),
            ref_normalized_graph=normalized_graphs["ref"],
            tgt_normalized_graph=normalized_graphs["tgt"],
            version_pair=changed_payload.get("version_pair") if isinstance(changed_payload, dict) else None,
            strategy=config.cmg.strategy,
            matching_view=config.cmg.matching_view,
            context_hops=config.cmg.context_hops,
            matched_hops=config.cmg.matched_hops,
            sparse_matched_hops=config.cmg.sparse_matched_hops,
            unmatched_expand_hops=config.cmg.unmatched_expand_hops,
            unmatched_expand_from_diff_calls=config.cmg.unmatched_expand_from_diff_calls,
            unmatched_source_window_lines=config.cmg.unmatched_source_window_lines,
            min_edges_for_sparse=config.cmg.min_edges_for_sparse,
            include_parent_context=config.cmg.include_parent_context,
            include_diff_calls=config.cmg.include_diff_calls,
            max_nodes=config.cmg.max_nodes,
            max_edges=config.cmg.max_edges,
        )
        cmg_payload = builder.build_payload()
        output_path = _resolve_output_path(
            args_output=args.output,
            config_output_dir=config.output_dir,
            default_filename="cmg.json",
        )
        _write_json(output_path, cmg_payload)

        matched_count = sum(1 for entry in cmg_payload["entries"] if entry["matched_entity_id"] is not None)
        matching_graph_matched_count = sum(
            1 for entry in cmg_payload["entries"] if entry.get("matched_matching_entity_id") is not None
        )
        unmatched_count = len(cmg_payload["unmatched_symbols"])
        print(
            "Matched prompt entries: "
            f"{matched_count}; matching-graph hits: {matching_graph_matched_count}; "
            f"unmatched symbols: {unmatched_count}."
        )
        print(
            json.dumps(
                {
                    "cmg_strategy": config.cmg.strategy,
                    "matching_view": config.cmg.matching_view,
                    "matched_count": matched_count,
                    "matching_graph_matched_count": matching_graph_matched_count,
                    "unmatched_count": unmatched_count,
                    "fallback_context_entry_count": cmg_payload.get("summary", {}).get(
                        "fallback_context_entry_count"
                    ),
                    "changed_functions_path": str(changed_output_path),
                    "ref_normalized_graph_path": str(normalized_paths["ref"]),
                    "tgt_normalized_graph_path": str(normalized_paths["tgt"]),
                    "cmg_output_path": str(output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "build-prompts":
        config = AppConfig.from_json_file(args.config)
        if config.output_dir is None and (
            args.changed_input is None
            or args.cmg_input is None
            or args.prompt_input_output is None
            or args.prompt_bundle_output is None
        ):
            raise ValueError(
                "config.output_dir is required unless all build-prompts input and output paths are provided."
            )

        changed_input_path = _resolve_output_path(
            args_output=args.changed_input,
            config_output_dir=config.output_dir,
            default_filename="changed_functions.json",
        )
        cmg_input_path = _resolve_output_path(
            args_output=args.cmg_input,
            config_output_dir=config.output_dir,
            default_filename="cmg.json",
        )
        prompt_input_output_path = _resolve_output_path(
            args_output=args.prompt_input_output,
            config_output_dir=config.output_dir,
            default_filename="prompt_input.json",
        )
        prompt_bundle_output_path = _resolve_output_path(
            args_output=args.prompt_bundle_output,
            config_output_dir=config.output_dir,
            default_filename="prompt_bundle.json",
        )

        if not changed_input_path.exists():
            raise FileNotFoundError(
                f"changed_functions.json not found: {changed_input_path}. Run detect-changes or build-cmg first."
            )
        if not cmg_input_path.exists():
            raise FileNotFoundError(f"cmg.json not found: {cmg_input_path}. Run build-cmg first.")

        changed_payload = json.loads(changed_input_path.read_text(encoding="utf-8"))
        cmg_payload = json.loads(cmg_input_path.read_text(encoding="utf-8"))

        bundle_builder = PromptBundleBuilder.from_app_config(config)
        bundle_builder.prompt_variant = args.prompt_variant
        if args.matched_only:
            bundle_builder.include_unmatched_entries = False

        prompt_input_payload = bundle_builder.build_prompt_input_payload(
            changed_payload=changed_payload,
            cmg_payload=cmg_payload,
        )
        prompt_bundle_payload = bundle_builder.build_prompt_bundle_payload(
            prompt_input_payload=prompt_input_payload,
        )

        _write_json(prompt_input_output_path, prompt_input_payload)
        _write_json(prompt_bundle_output_path, prompt_bundle_payload)

        print(
            json.dumps(
                {
                    "entry_count": prompt_input_payload["summary"]["entry_count"],
                    "matched_entry_count": prompt_input_payload["summary"]["matched_entry_count"],
                    "unmatched_entry_count": prompt_input_payload["summary"]["unmatched_entry_count"],
                    "prompt_variant": prompt_input_payload["summary"].get("prompt_variant"),
                    "changed_input_path": str(changed_input_path),
                    "cmg_input_path": str(cmg_input_path),
                    "prompt_input_output_path": str(prompt_input_output_path),
                    "prompt_bundle_output_path": str(prompt_bundle_output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "generate-release-notes":
        config = AppConfig.from_json_file(args.config)
        if config.output_dir is None and (
            args.prompt_bundle_input is None
            or args.json_output is None
            or args.markdown_output is None
        ):
            raise ValueError(
                "config.output_dir is required unless all generate-release-notes input and output paths are provided."
            )

        prompt_bundle_input_path = _resolve_output_path(
            args_output=args.prompt_bundle_input,
            config_output_dir=config.output_dir,
            default_filename="prompt_bundle.json",
        )
        json_output_path = _resolve_output_path(
            args_output=args.json_output,
            config_output_dir=config.output_dir,
            default_filename="release_note.json",
        )
        markdown_output_path = _resolve_output_path(
            args_output=args.markdown_output,
            config_output_dir=config.output_dir,
            default_filename="release_note.md",
        )

        if not prompt_bundle_input_path.exists():
            raise FileNotFoundError(
                f"prompt_bundle.json not found: {prompt_bundle_input_path}. Run build-prompts first."
            )

        prompt_bundle_payload = json.loads(prompt_bundle_input_path.read_text(encoding="utf-8"))
        generator = ReleaseNoteGenerator.from_app_config(
            config,
            backend_override=args.backend,
            model_override=args.model,
            aggregation_strategy_override=args.aggregation_strategy,
        )
        release_note_payload = generator.generate_payload(prompt_bundle_payload)
        release_note_markdown = generator.render_markdown(release_note_payload)

        _write_json(json_output_path, release_note_payload)
        markdown_output_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_output_path.write_text(release_note_markdown, encoding="utf-8")

        print(
            json.dumps(
                {
                    "generated_entry_count": release_note_payload["summary"]["generated_entry_count"],
                    "failed_entry_count": release_note_payload["summary"]["failed_entry_count"],
                    "deduplicated_release_note_count": release_note_payload["summary"][
                        "deduplicated_release_note_count"
                    ],
                    "aggregation_strategy": release_note_payload["summary"].get("aggregation_strategy"),
                    "backend": release_note_payload["backend"]["backend"],
                    "model": release_note_payload["backend"]["model"],
                    "prompt_bundle_input_path": str(prompt_bundle_input_path),
                    "json_output_path": str(json_output_path),
                    "markdown_output_path": str(markdown_output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "rewrite-aggregation":
        input_path = Path(args.input)
        release_note_payload = _read_json(input_path)
        rewritten_payload = ReleaseNoteGenerator.reaggregate_payload(
            release_note_payload,
            aggregation_strategy=args.aggregation_strategy,
        )
        markdown = ReleaseNoteGenerator().render_markdown(rewritten_payload)

        output_stem = f"release_note_{args.aggregation_strategy}"
        json_output_path = Path(args.json_output) if args.json_output else input_path.with_name(f"{output_stem}.json")
        markdown_output_path = (
            Path(args.markdown_output)
            if args.markdown_output
            else input_path.with_name(f"{output_stem}.md")
        )
        _write_json(json_output_path, rewritten_payload)
        markdown_output_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_output_path.write_text(markdown, encoding="utf-8")

        print(
            json.dumps(
                {
                    "aggregation_strategy": args.aggregation_strategy,
                    "deduplicated_release_note_count": rewritten_payload.get("summary", {}).get(
                        "deduplicated_release_note_count"
                    )
                    if isinstance(rewritten_payload.get("summary"), dict)
                    else None,
                    "json_output_path": str(json_output_path),
                    "markdown_output_path": str(markdown_output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "run-baselines":
        config = AppConfig.from_json_file(args.config)
        runner = BaselineRunner(
            config=config,
            variants=args.variants,
            changed_input_path=args.changed_input,
            cmg_input_path=args.cmg_input,
            output_root=args.output_root,
            backend_override=args.backend,
            model_override=args.model,
            aggregation_strategy_override=args.aggregation_strategy,
        )
        payload = runner.run()
        summary_output_path = (
            Path(args.summary_output)
            if args.summary_output
            else Path(str(payload["output_root"])) / "baseline_summary.json"
        )
        _write_json(summary_output_path, payload)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "build-ground-truth-evidence":
        builder = GroundTruthEvidenceBuilder(
            metadata_path=args.metadata,
            max_functions=max(args.max_functions, 0),
            max_diff_lines_per_function=max(args.max_diff_lines_per_function, 0),
        )
        output_path = Path(args.output) if args.output else Path(args.metadata).parent / "evidence.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(builder.build_markdown(), encoding="utf-8")
        print(
            json.dumps(
                {
                    "metadata_path": str(Path(args.metadata)),
                    "evidence_output_path": str(output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "evaluate-release-notes":
        evaluator = ReleaseNoteEvaluator(
            ground_truth_path=args.ground_truth,
            release_note_path=args.release_note,
            matches_path=args.matches,
        )
        payload = evaluator.build_payload()
        output_path = (
            Path(args.output)
            if args.output
            else Path(args.release_note).with_name("evaluation.json")
        )
        _write_json(output_path, payload)

        if args.match_template_output:
            _write_json(args.match_template_output, payload["match_template"])

        print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
        return

    if args.command == "evaluate-baselines":
        runner = BaselineEvaluationRunner(
            metadata_paths=args.metadata,
            variants=args.variants,
            matches_filename=args.matches_filename,
            evaluation_filename=args.evaluation_filename,
            match_template_filename=args.match_template_filename,
            baseline_root_name=args.baseline_root_name,
        )
        payload = runner.run()
        if args.summary_output:
            _write_json(args.summary_output, payload)
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "summarize-evaluations":
        builder = EvaluationSummaryBuilder(
            metadata_paths=args.metadata,
            variants=args.variants,
            evaluation_filename=args.evaluation_filename,
            baseline_root_name=args.baseline_root_name,
        )
        payload = builder.build_payload()
        if args.json_output:
            _write_json(args.json_output, payload)
        markdown = builder.render_markdown(payload)
        if args.markdown_output:
            target = Path(args.markdown_output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
        print(markdown)
        return

    if args.command == "summarize-baseline-outputs":
        builder = BaselineOutputSummaryBuilder(
            metadata_paths=args.metadata,
            variants=args.variants,
            baseline_root_name=args.baseline_root_name,
        )
        payload = builder.build_payload()
        if args.json_output:
            _write_json(args.json_output, payload)
        markdown = builder.render_markdown(payload)
        if args.markdown_output:
            target = Path(args.markdown_output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
        print(markdown)
        return

    if args.command == "summarize-aggregation":
        builder = AggregationComparisonBuilder(
            metadata_paths=args.metadata,
            variants=args.variants,
            baseline_root_name=args.baseline_root_name,
            strategies=args.strategies,
        )
        payload = builder.build_payload()
        if args.json_output:
            _write_json(args.json_output, payload)
        markdown = builder.render_markdown(payload)
        if args.markdown_output:
            target = Path(args.markdown_output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
        print(markdown)
        return

    if args.command == "summarize-experiments":
        builder = ExperimentReportBuilder(benchmark_root=args.benchmark_root)
        payload = builder.build_payload()
        if args.json_output:
            _write_json(args.json_output, payload)
        markdown = builder.render_markdown(payload)
        if args.markdown_output:
            target = Path(args.markdown_output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(markdown, encoding="utf-8")
        if args.case_json_output or args.case_markdown_output:
            case_payload = builder.build_case_payload()
            if args.case_json_output:
                _write_json(args.case_json_output, case_payload)
            if args.case_markdown_output:
                target = Path(args.case_markdown_output)
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(
                    builder.render_case_markdown(case_payload),
                    encoding="utf-8",
                )
        print(markdown)
        return

    if args.command == "build-visual-report":
        builder = VisualReportBuilder(
            benchmark_root=args.benchmark_root,
            title=args.title,
            matrix_input=args.matrix_input,
            cmg_input=args.cmg_input,
            cmg_coverage_input=args.cmg_coverage_input,
        )
        payload = builder.build_payload()
        if args.json_output:
            _write_json(args.json_output, payload)
        target = Path(args.output)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(builder.render_html(payload), encoding="utf-8")
        print(
            json.dumps(
                {
                    "html_output_path": str(target),
                    "json_output_path": args.json_output,
                    "matrix_row_count": len(payload.get("matrix_rows", []))
                    if isinstance(payload.get("matrix_rows"), list)
                    else 0,
                    "cmg_sample_included": bool(payload.get("cmg_summary")),
                    "cmg_coverage_included": bool(payload.get("cmg_coverage_rows")),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "build-demo":
        builder = DemoReportBuilder(
            case=args.case,
            mode=args.mode,
            output_dir=args.output,
            benchmark_root=args.benchmark_root,
        )
        payload = builder.build()
        stage1 = payload.get("stage1") if isinstance(payload.get("stage1"), dict) else {}
        stage2 = payload.get("stage2") if isinstance(payload.get("stage2"), dict) else {}
        stage3 = payload.get("stage3") if isinstance(payload.get("stage3"), dict) else {}
        output_dir = Path(args.output)
        print(
            json.dumps(
                {
                    "html_output_path": str(output_dir / "index.html"),
                    "run_log_path": str(output_dir / "run_log.md"),
                    "payload_path": str(output_dir / "demo_payload.json"),
                    "changed_function_count": stage1.get("changed_function_count", 0),
                    "cmg_matches": f"{stage2.get('matched_entry_count', 0)}/{stage2.get('entry_count', 0)}",
                    "final_note_count": stage3.get("final_note_count", 0),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return


def _resolve_output_path(
    *,
    args_output: str | None,
    config_output_dir: Path | None,
    default_filename: str,
) -> Path:
    if args_output is not None:
        return Path(args_output)
    if config_output_dir is None:
        raise ValueError("config.output_dir is required when no explicit --output path is provided.")
    return config_output_dir / default_filename


def _write_json(path: str | Path, payload: dict[str, object]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def _read_json(path: str | Path) -> dict[str, object]:
    target = Path(path)
    payload = json.loads(target.read_text(encoding="utf-8-sig"))
    if not isinstance(payload, dict):
        raise ValueError(f"JSON payload must be an object: {target}")
    return payload


if __name__ == "__main__":
    main()

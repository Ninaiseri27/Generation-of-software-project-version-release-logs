import json
from pathlib import Path

from cpp_release_note_mvp.pipeline.evaluation_runner import (
    AggregationComparisonBuilder,
    BaselineEvaluationRunner,
    BaselineOutputSummaryBuilder,
    EvaluationSummaryBuilder,
)


def _write_json(path: Path, payload: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def test_resolve_output_dir_prefers_explicit_pipeline_output_dir(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    metadata_path = repo_root / "benchmark" / "cases" / "demo" / "metadata.json"
    metadata_path.parent.mkdir(parents=True)
    metadata_path.write_text("{}", encoding="utf-8")

    output_dir = repo_root / "outputs" / "benchmark" / "demo_case"
    output_dir.mkdir(parents=True)
    evidence_path = repo_root / "benchmark" / "cases" / "demo" / "evidence.md"
    evidence_path.write_text("# Evidence\n", encoding="utf-8")

    metadata = {
        "pipeline_artifacts": {
            "sampled_evidence": "benchmark/cases/demo/evidence.md",
            "output_dir": "outputs/benchmark/demo_case",
        }
    }

    resolved = BaselineEvaluationRunner._resolve_output_dir(metadata_path, metadata)

    assert resolved == output_dir


def test_resolve_output_dir_falls_back_to_artifact_parent(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    metadata_path = repo_root / "benchmark" / "cases" / "demo" / "metadata.json"
    metadata_path.parent.mkdir(parents=True)
    metadata_path.write_text("{}", encoding="utf-8")

    cmg_path = repo_root / "outputs" / "benchmark" / "demo_case" / "cmg.json"
    cmg_path.parent.mkdir(parents=True)
    cmg_path.write_text("{}", encoding="utf-8")

    metadata = {
        "pipeline_artifacts": {
            "cmg": "outputs/benchmark/demo_case/cmg.json",
        }
    }

    resolved = BaselineEvaluationRunner._resolve_output_dir(metadata_path, metadata)

    assert resolved == cmg_path.parent


def test_evaluation_summary_builder_computes_macro_and_micro_metrics(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    metadata_paths: list[Path] = []
    case_summaries = [
        {
            "case_id": "case_a",
            "ground_truth_count": 2,
            "generated_count": 4,
            "valid_match_count": 3,
            "matched_generated_count": 2,
            "matched_ground_truth_count": 2,
            "precision": 0.5,
            "recall": 1.0,
            "f1": 0.6667,
            "unsupported_claim_rate": 0.5,
            "redundancy_count": 1,
            "redundancy_per_gt": 0.5,
            "avg_matches_per_gt": 1.5,
            "structural_valid_rate": 1.0,
        },
        {
            "case_id": "case_b",
            "ground_truth_count": 3,
            "generated_count": 6,
            "valid_match_count": 3,
            "matched_generated_count": 3,
            "matched_ground_truth_count": 2,
            "precision": 0.5,
            "recall": 0.6667,
            "f1": 0.5714,
            "unsupported_claim_rate": 0.5,
            "redundancy_count": 1,
            "redundancy_per_gt": 0.3333,
            "avg_matches_per_gt": 1.0,
            "structural_valid_rate": 0.8333,
        },
    ]

    for case_summary in case_summaries:
        case_id = str(case_summary["case_id"])
        metadata_path = repo_root / "benchmark" / "cases" / case_id / "metadata.json"
        output_dir = repo_root / "outputs" / "benchmark" / case_id
        _write_json(
            metadata_path,
            {
                "case_id": case_id,
                "pipeline_artifacts": {
                    "output_dir": f"outputs/benchmark/{case_id}",
                },
            },
        )
        summary_payload = dict(case_summary)
        summary_payload["evaluation_status"] = "evaluated"
        _write_json(
            output_dir / "baselines" / "full" / "evaluation.json",
            {"summary": summary_payload},
        )
        metadata_paths.append(metadata_path)

    payload = EvaluationSummaryBuilder(
        metadata_paths=metadata_paths,
        variants=["full"],
    ).build_payload()

    rows = payload["rows"]
    assert len(rows) == 2
    assert all(row["status"] == "evaluated" for row in rows)
    assert rows[0]["avg_matches_per_gt"] == 1.5
    assert rows[0]["redundancy_per_gt"] == 0.5

    macro = payload["macro_averages"][0]
    assert macro["evaluated_cases"] == 2
    assert macro["precision"] == 0.5
    assert macro["recall"] == 0.8334
    assert macro["f1"] == 0.619
    assert macro["avg_matches_per_gt"] == 1.25
    assert macro["avg_redundancy_per_gt"] == 0.4166

    micro = payload["micro_averages"][0]
    assert micro["generated_count"] == 10.0
    assert micro["ground_truth_count"] == 5.0
    assert micro["matched_generated_count"] == 5.0
    assert micro["matched_ground_truth_count"] == 4.0
    assert micro["precision"] == 0.5
    assert micro["recall"] == 0.8
    assert micro["f1"] == 0.6154
    assert micro["matches_per_gt"] == 1.2
    assert micro["redundancy_per_gt"] == 0.4

    markdown = EvaluationSummaryBuilder.render_markdown(payload)
    assert "Matches/GT" in markdown
    assert "Extra/GT" in markdown


def test_baseline_output_summary_builder_tracks_compression_and_tokens(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    metadata_path = repo_root / "benchmark" / "cases" / "case_a" / "metadata.json"
    output_dir = repo_root / "outputs" / "benchmark" / "case_a"
    variant_dir = output_dir / "baselines" / "full"

    _write_json(
        metadata_path,
        {
            "case_id": "case_a",
            "pipeline_artifacts": {
                "output_dir": "outputs/benchmark/case_a",
            },
        },
    )
    _write_json(
        variant_dir / "prompt_input.json",
        {
            "summary": {
                "entry_count": 3,
                "matched_entry_count": 2,
                "unmatched_entry_count": 1,
            }
        },
    )
    _write_json(
        variant_dir / "release_note.json",
        {
            "summary": {
                "entry_count": 3,
                "generated_entry_count": 2,
                "failed_entry_count": 1,
                "deduplicated_release_note_count": 1,
                "aggregation_strategy": "rule_family",
            },
            "entries": [
                {
                    "status": "generated",
                    "usage": {
                        "prompt_tokens": 10,
                        "completion_tokens": 3,
                        "total_tokens": 13,
                    },
                },
                {
                    "status": "generated",
                    "usage": {
                        "prompt_tokens": 20,
                        "completion_tokens": 5,
                        "total_tokens": 25,
                    },
                },
                {"status": "failed", "usage": None},
            ],
            "structured_release_notes": [{}, {}],
            "aggregated_release_notes": [{}],
            "deduplicated_release_notes": ["Merged note."],
        },
    )

    payload = BaselineOutputSummaryBuilder(
        metadata_paths=[metadata_path],
        variants=["full"],
    ).build_payload()

    row = payload["rows"][0]
    assert row["status"] == "summarized"
    assert row["prompt_entry_count"] == 3
    assert row["matched_entry_count"] == 2
    assert row["unmatched_entry_count"] == 1
    assert row["generated_entry_count"] == 2
    assert row["failed_entry_count"] == 1
    assert row["deduplicated_release_note_count"] == 1
    assert row["compression_ratio"] == 0.5
    assert row["reduction_rate"] == 0.5
    assert row["prompt_tokens"] == 30
    assert row["completion_tokens"] == 8
    assert row["total_tokens"] == 38

    macro = payload["macro_averages"][0]
    assert macro["avg_generated_entry_count"] == 2.0
    assert macro["avg_deduplicated_release_note_count"] == 1.0
    assert macro["avg_compression_ratio"] == 0.5
    assert macro["avg_total_tokens"] == 38.0

    markdown = BaselineOutputSummaryBuilder.render_markdown(payload)
    assert "Compression" in markdown
    assert "Total Tokens" in markdown


def test_aggregation_comparison_builder_tracks_strategy_compression(tmp_path: Path) -> None:
    repo_root = tmp_path / "repo"
    metadata_path = repo_root / "benchmark" / "cases" / "case_a" / "metadata.json"
    output_dir = repo_root / "outputs" / "benchmark" / "case_a"
    variant_dir = output_dir / "baselines" / "full"

    _write_json(
        metadata_path,
        {
            "case_id": "case_a",
            "pipeline_artifacts": {
                "output_dir": "outputs/benchmark/case_a",
            },
        },
    )
    _write_json(
        variant_dir / "release_note.json",
        {
            "entries": [
                {
                    "entry_id": "entry-001",
                    "symbol": "TestA",
                    "status": "generated",
                    "structured_note": {
                        "section": "Testing",
                        "title": "Add compressed database corruption test",
                        "summary": "Adds a regression test for compressed database corruption.",
                    },
                },
                {
                    "entry_id": "entry-002",
                    "symbol": "TestB",
                    "status": "generated",
                    "structured_note": {
                        "section": "Testing",
                        "title": "Add compressed database corruption I/O test",
                        "summary": "Adds another regression test for compressed database corruption.",
                    },
                },
                {
                    "entry_id": "entry-003",
                    "symbol": "Helper",
                    "status": "generated",
                    "structured_note": {
                        "section": "Internal",
                        "title": "Refactor helper",
                        "summary": "Refactors an internal helper.",
                    },
                },
            ],
        },
    )

    payload = AggregationComparisonBuilder(
        metadata_paths=[metadata_path],
        variants=["full"],
        strategies=["none", "rule_family"],
    ).build_payload()

    rows = {
        str(row["strategy"]): row
        for row in payload["rows"]
        if row["status"] == "summarized"
    }
    assert rows["none"]["generated_entry_count"] == 3
    assert rows["none"]["final_release_note_count"] == 3
    assert rows["none"]["compression_ratio"] == 1.0
    assert rows["none"]["merged_group_count"] == 0

    assert rows["rule_family"]["generated_entry_count"] == 3
    assert rows["rule_family"]["final_release_note_count"] == 2
    assert rows["rule_family"]["compression_ratio"] == 0.6667
    assert rows["rule_family"]["reduction_rate"] == 0.3333
    assert rows["rule_family"]["merged_group_count"] == 1
    assert rows["rule_family"]["max_source_note_count"] == 2

    macro_rows = {
        str(row["strategy"]): row
        for row in payload["macro_averages"]
    }
    assert macro_rows["rule_family"]["avg_final_release_note_count"] == 2.0
    assert macro_rows["rule_family"]["avg_compression_ratio"] == 0.6667

    markdown = AggregationComparisonBuilder.render_markdown(payload)
    assert "Aggregation Strategy Summary" in markdown
    assert "Max Group Size" in markdown

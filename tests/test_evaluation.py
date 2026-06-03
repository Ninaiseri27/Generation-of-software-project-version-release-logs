import json
from pathlib import Path

from cpp_release_note_mvp.pipeline.evaluation import ReleaseNoteEvaluator


def _write_json(path: Path, payload: object) -> None:
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def test_evaluator_computes_strict_metrics_and_redundancy(tmp_path: Path) -> None:
    ground_truth_path = tmp_path / "ground_truth.md"
    release_note_path = tmp_path / "release_note.json"
    matches_path = tmp_path / "matches.json"

    ground_truth_path.write_text(
        "\n".join(
            [
                "| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |",
                "| --- | --- | --- | --- | --- |",
                "| GT-001 | Feature | Add syntax support. | diff | reviewed |",
                "| GT-002 | Bug Fixes | Fix parser crash. | diff | reviewed |",
            ]
        ),
        encoding="utf-8",
    )
    _write_json(
        release_note_path,
        {
            "aggregated_release_notes": [
                {
                    "section": "Features",
                    "title": "Add syntax support",
                    "summary": "Adds syntax support.",
                },
                {
                    "section": "Features",
                    "title": "Add related syntax support",
                    "summary": "Adds related syntax support.",
                },
                {
                    "section": "Internal",
                    "title": "Refactor helper",
                    "summary": "Refactors an internal helper.",
                },
            ]
        },
    )
    _write_json(
        matches_path,
        {
            "matches": [
                {"generated_id": "GEN-001", "gt_id": "GT-001", "decision": "match"},
                {"generated_id": "GEN-002", "gt_id": "GT-001", "decision": "match"},
                {"generated_id": "GEN-003", "gt_id": "GT-002", "decision": "non_match"},
                {"generated_id": "GEN-999", "gt_id": "GT-002", "decision": "match"},
            ]
        },
    )

    payload = ReleaseNoteEvaluator(
        ground_truth_path=ground_truth_path,
        release_note_path=release_note_path,
        matches_path=matches_path,
    ).build_payload()

    summary = payload["summary"]
    assert summary["evaluation_status"] == "evaluated"
    assert summary["ground_truth_count"] == 2
    assert summary["generated_count"] == 3
    assert summary["valid_match_count"] == 2
    assert summary["invalid_match_count"] == 1
    assert summary["matched_generated_count"] == 2
    assert summary["matched_ground_truth_count"] == 1
    assert summary["precision"] == 0.6667
    assert summary["recall"] == 0.5
    assert summary["f1"] == 0.5714
    assert summary["unsupported_claim_count"] == 1
    assert summary["unsupported_claim_rate"] == 0.3333
    assert summary["redundancy_count"] == 1
    assert summary["redundancy_per_gt"] == 0.5
    assert summary["avg_matches_per_gt"] == 1.0
    assert summary["structural_valid_rate"] == 1.0


def test_evaluator_marks_metrics_as_required_without_matches(tmp_path: Path) -> None:
    ground_truth_path = tmp_path / "ground_truth.md"
    release_note_path = tmp_path / "release_note.json"

    ground_truth_path.write_text(
        "| GT-001 | Feature | Add syntax support. | diff | reviewed |\n",
        encoding="utf-8",
    )
    _write_json(
        release_note_path,
        {
            "aggregated_release_notes": [
                {
                    "section": "Features",
                    "title": "Add syntax support",
                    "summary": "Adds syntax support.",
                }
            ]
        },
    )

    payload = ReleaseNoteEvaluator(
        ground_truth_path=ground_truth_path,
        release_note_path=release_note_path,
    ).build_payload()

    summary = payload["summary"]
    assert summary["evaluation_status"] == "match_required"
    assert summary["ground_truth_count"] == 1
    assert summary["generated_count"] == 1
    assert summary["precision"] is None
    assert summary["recall"] is None
    assert summary["f1"] is None
    assert summary["structural_valid_rate"] == 1.0

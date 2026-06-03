import json

from cpp_release_note_mvp.pipeline.visual_report import VisualReportBuilder


def test_visual_report_renders_matrix_and_cmg_sample(tmp_path) -> None:
    benchmark_root = tmp_path / "benchmark"
    benchmark_root.mkdir()
    (benchmark_root / "core5_experiment_matrix.json").write_text(
        json.dumps(
            {
                "interpretation": {
                    "best_f1_method": "diff_only",
                    "best_micro_f1_method": "diff_only",
                    "strongest_compression_method": "full_similarity_family",
                },
                "rows": [
                    {
                        "method_id": "diff_only",
                        "precision": 0.9,
                        "recall": 1.0,
                        "f1": 0.94,
                        "micro_f1": 0.93,
                        "unsupported_claim_rate": 0.1,
                        "micro_redundancy_per_gt": 2.0,
                        "avg_reduction_rate": 0.1,
                        "avg_total_tokens": 1000,
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (benchmark_root / "core5_per_case_results.json").write_text(
        json.dumps(
            {
                "medium_case_macro": [
                    {
                        "method_id": "diff_only",
                        "case_count": 3,
                        "f1": 0.94,
                        "unsupported_claim_rate": 0.1,
                        "extra_per_gt": 2.0,
                        "total_tokens": 1000,
                    }
                ],
                "interpretation": {
                    "result_narrative": ["Diff is a strong baseline."],
                    "validity_threats": ["GT granularity can affect recall."],
                },
            }
        ),
        encoding="utf-8",
    )
    cmg_path = tmp_path / "cmg.json"
    cmg_path.write_text(
        json.dumps(
            {
                "summary": {"entry_count": 1, "matched_entry_count": 1},
                "entries": [
                    {
                        "symbol": "demo",
                        "cmg": {
                            "nodes": [{"id": 1, "qualified_name": "demo"}],
                            "edges": [{"source_id": 1, "target_id": 1, "type": "call"}],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    cmg_coverage_path = tmp_path / "cmg_coverage.json"
    cmg_coverage_path.write_text(
        json.dumps(
            {
                "rows": [
                    {
                        "case_id": "demo_case",
                        "entry_count": 10,
                        "compact_prompt_matches": 4,
                        "rich_prompt_matches": 5,
                        "projected_prompt_matches": 6,
                        "matching_graph_hits": 8,
                        "matching_only_after_projection": 2,
                    }
                ],
                "interpretation": ["Projection improves coverage without expanding prompt graph."],
            }
        ),
        encoding="utf-8",
    )

    builder = VisualReportBuilder(
        benchmark_root=benchmark_root,
        cmg_input=cmg_path,
        cmg_coverage_input=cmg_coverage_path,
    )
    payload = builder.build_payload()
    html = builder.render_html(payload)

    assert payload["cmg_summary"]["sample_symbol"] == "demo"
    assert payload["cmg_coverage_rows"][0]["case_id"] == "demo_case"
    assert "diff_only" in html
    assert "Pipeline Overview" in html
    assert "CMG Sample" in html
    assert "CMG Coverage Optimization" in html
    assert "Projected" in html
    assert "Projection improves coverage" in html
    assert "Diff is a strong baseline." in html


def test_visual_report_accepts_explicit_expanded_matrix(tmp_path) -> None:
    benchmark_root = tmp_path / "benchmark"
    benchmark_root.mkdir()
    expanded_matrix = benchmark_root / "expanded_137gt_matrix.json"
    expanded_matrix.write_text(
        json.dumps(
            {
                "summary": {"case_count": 13, "ground_truth_count": 137},
                "matrix_rows": [
                    {
                        "method": "full_similarity_family",
                        "core_82gt_macro_f1": 0.7237,
                        "extension_55gt_macro_f1": 0.1913,
                        "expanded_137gt_macro_f1": 0.6418,
                        "core_82gt_micro_f1": 0.6299,
                        "extension_55gt_micro_f1": 0.1971,
                        "expanded_137gt_micro_f1": 0.361,
                        "expanded_micro_precision": 0.2269,
                        "expanded_micro_recall": 0.8832,
                        "expanded_unsupported_rate": 0.7731,
                        "expanded_matches_per_gt": 2.2993,
                        "expanded_extra_per_gt": 1.4161,
                        "expanded_avg_final_notes": 99.0,
                        "expanded_reduction_rate": 0.5145,
                        "expanded_avg_total_tokens": 487262.8,
                        "expanded_generated_count": 1287,
                    }
                ],
                "per_case_rows": [],
            }
        ),
        encoding="utf-8",
    )

    builder = VisualReportBuilder(benchmark_root=benchmark_root, matrix_input=expanded_matrix)
    payload = builder.build_payload()
    html = builder.render_html(payload)

    assert payload["source"]["matrix_source"] == str(expanded_matrix)
    assert payload["matrix_rows"][0]["ground_truth_count"] == 137
    assert payload["matrix_rows"][0]["avg_reduction_rate"] == 0.5145
    assert payload["matrix_rows"][0]["avg_total_tokens"] == 487262.8
    assert payload["expanded_comparison_rows"][0]["expanded_137gt_macro_f1"] == 0.6418
    assert "Expanded 137-GT Robustness Check" in html
    assert "Average Token Cost" in html
    assert "Reduction" in html
    assert "full_similarity_family" in html

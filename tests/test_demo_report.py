import json
from pathlib import Path

from cpp_release_note_mvp.pipeline.demo_report import DemoCase, DemoReportBuilder


def test_demo_report_packages_cached_artifacts_and_renders_html(tmp_path: Path) -> None:
    source_root = tmp_path / "source"
    output_root = source_root / "outputs" / "case"
    output_root.mkdir(parents=True)
    release_root = output_root / "baselines_deepseek_v4_flash" / "full"
    release_root.mkdir(parents=True)
    benchmark_root = source_root / "benchmark"
    benchmark_root.mkdir()
    config_path = source_root / "configs" / "case.json"
    config_path.parent.mkdir(parents=True)

    config_path.write_text(json.dumps({"project": {"name": "demo_project"}}), encoding="utf-8")
    (output_root / "changed_functions.json").write_text(
        json.dumps(
            {
                "changed_files": ["src/demo.c"],
                "commit_messages": ["fix integer overflow"],
                "items": [
                    {
                        "symbol": "demo_func",
                        "file_path": "src/demo.c",
                        "change_type": "modified",
                        "start_line": 10,
                        "end_line": 14,
                        "diff_hunks": [
                            {
                                "lines": [
                                    "-  int n = a + b;",
                                    "+  int n = safe_add(a, b);",
                                ]
                            }
                        ],
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (output_root / "cmg.json").write_text(
        json.dumps(
            {
                "summary": {
                    "entry_count": 1,
                    "matched_entry_count": 1,
                    "unmatched_entry_count": 0,
                    "fallback_context_entry_count": 1,
                },
                "entries": [
                    {
                        "symbol": "demo_func",
                        "file_path": "src/demo.c",
                        "match_level": "path+symbol",
                        "matched_entity_id": 1,
                        "cmg": {
                            "nodes": [
                                {"id": 1, "qualified_name": "demo_func", "file_path": "src/demo.c"},
                                {"id": 2, "qualified_name": "safe_add", "file_path": "src/demo.c"},
                            ],
                            "edges": [{"source_id": 1, "target_id": 2, "type": "call"}],
                        },
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (output_root / "prompt_input.json").write_text(json.dumps({"entries": []}), encoding="utf-8")
    (output_root / "prompt_bundle.json").write_text(
        json.dumps(
            {
                "entries": [
                    {
                        "entry_id": "entry-001",
                        "user_prompt": "Project\nGraph and Fallback Context\n[Changed] demo_func\nRelations: 1 calls 2",
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (release_root / "release_note.json").write_text(
        json.dumps(
            {
                "summary": {
                    "entry_count": 1,
                    "generated_entry_count": 1,
                    "failed_entry_count": 0,
                    "deduplicated_release_note_count": 1,
                    "aggregation_strategy": "rule_family",
                },
                "aggregated_release_notes": [
                    {
                        "section": "Bug Fixes",
                        "title": "Fix demo overflow",
                        "summary": "Use safe addition in demo_func.",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )
    (release_root / "release_note.md").write_text("# Release Notes\n", encoding="utf-8")
    (benchmark_root / "core5_experiment_matrix.json").write_text(
        json.dumps(
            {
                "rows": [
                    {
                        "method_id": "diff_only",
                        "precision": 0.9,
                        "recall": 1.0,
                        "f1": 0.94,
                        "micro_f1": 0.93,
                        "micro_redundancy_per_gt": 1.2,
                        "avg_reduction_rate": 0.1,
                    }
                ]
            }
        ),
        encoding="utf-8",
    )
    (benchmark_root / "cmg_coverage_core5.json").write_text(
        json.dumps(
            {
                "rows": [
                    {
                        "case_id": "demo_case",
                        "entry_count": 1,
                        "compact_prompt_matches": 1,
                        "rich_prompt_matches": 1,
                        "projected_prompt_matches": 1,
                        "matching_graph_hits": 1,
                    }
                ]
            }
        ),
        encoding="utf-8",
    )

    demo_case = DemoCase(
        case_id="demo_case",
        project_name="demo_project",
        ref_version="v1",
        tgt_version="v2",
        config_path=Path("configs/case.json"),
        output_root=Path("outputs/case"),
        release_note_json=Path("outputs/case/baselines_deepseek_v4_flash/full/release_note.json"),
        release_note_markdown=Path("outputs/case/baselines_deepseek_v4_flash/full/release_note.md"),
    )
    output_dir = tmp_path / "demo"
    builder = DemoReportBuilder(
        source_root=source_root,
        benchmark_root=benchmark_root,
        output_dir=output_dir,
        demo_case=demo_case,
    )

    payload = builder.build()
    html = (output_dir / "index.html").read_text(encoding="utf-8")

    assert payload["stage1"]["changed_function_count"] == 1
    assert payload["stage2"]["matched_entry_count"] == 1
    assert payload["stage3"]["final_note_count"] == 1
    assert (output_dir / "artifacts" / "changed_functions.json").exists()
    assert (output_dir / "artifacts" / "release_note.md").exists()
    assert (output_dir / "run_log.md").exists()
    assert "Stage 1: Function-Level Change Localization" in html
    assert "demo_func" in html
    assert "Macro F1" in html
    assert "Fix demo overflow" in html

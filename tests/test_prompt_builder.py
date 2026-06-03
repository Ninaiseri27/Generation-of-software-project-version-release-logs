from cpp_release_note_mvp.pipeline.prompt_builder import PromptBundleBuilder


def _changed_payload() -> dict[str, object]:
    return {
        "version_pair": {
            "repo_path": "demo",
            "ref": "v1",
            "tgt": "v2",
        },
        "changed_files": ["src/demo.c"],
        "commit_messages": ["feat: add parser guard"],
    }


def _cmg_payload() -> dict[str, object]:
    return {
        "version_pair": {
            "ref": "v1",
            "tgt": "v2",
        },
        "entries": [
            {
                "symbol": "parse_demo",
                "signature": "int parse_demo(void)",
                "file_path": "src/demo.c",
                "change_type": "modified",
                "matched_entity_id": 1,
                "match_level": "basename+symbol",
                "start_line": 10,
                "end_line": 20,
                "diff_hunks": [
                    {
                        "file_path": "src/demo.c",
                        "old_start": 10,
                        "old_count": 1,
                        "new_start": 10,
                        "new_count": 2,
                        "lines": [
                            "- return parse(input);",
                            "+ return parse_checked(input);",
                        ],
                    }
                ],
                "change_notes": ["modified function body"],
                "match_notes": ["matched by file and symbol"],
                "cmg": {
                    "nodes": [
                        {
                            "id": 1,
                            "qualified_name": "parse_demo",
                            "file_path": "src/demo.c",
                            "is_user_defined": True,
                            "entity_source": "enre",
                        },
                        {
                            "id": 2,
                            "qualified_name": "parse_checked",
                            "file_path": "src/demo.c",
                            "is_user_defined": True,
                            "entity_source": "enre",
                        },
                        {
                            "id": "synthetic:parse_demo",
                            "qualified_name": "parse_demo",
                            "file_path": "src/demo.c",
                            "is_user_defined": True,
                            "entity_source": "synthetic:unmatched_changed_function",
                        },
                        {
                            "id": "diff_call:open",
                            "qualified_name": "open",
                            "file_path": "",
                            "is_user_defined": False,
                            "entity_source": "diff_call:unresolved",
                        },
                    ],
                    "edges": [
                        {
                            "source_id": 1,
                            "target_id": 2,
                            "type": "call",
                            "provenance": "enre",
                        },
                        {
                            "source_id": 1,
                            "target_id": "diff_call:open",
                            "type": "call",
                            "provenance": "diff-derived",
                        },
                    ],
                    "provenance": {
                        "changed_node_id": 1,
                    },
                },
                "fallback_context": {
                    "reason": "sparse graph",
                    "diff_called_symbols": [
                        {
                            "name": "open",
                            "occurrence_count": 1,
                            "added_count": 1,
                            "removed_count": 0,
                        }
                    ],
                },
            }
        ],
        "unmatched_symbols": [],
    }


def _builder(prompt_variant: str) -> PromptBundleBuilder:
    return PromptBundleBuilder(
        project_name="demo",
        project_description="Demo project",
        prompt_variant=prompt_variant,
    )


def test_full_prompt_variant_keeps_fallback_and_diff_derived_context() -> None:
    payload = _builder("full").build_prompt_input_payload(
        changed_payload=_changed_payload(),
        cmg_payload=_cmg_payload(),
    )

    entry = payload["entries"][0]
    cmg = entry["cmg"]
    assert payload["summary"]["fallback_context_entry_count"] == 1
    assert payload["summary"]["synthetic_entry_count"] == 1
    assert entry["fallback_context"]["reason"] == "sparse graph"
    assert any(str(edge.get("provenance")) == "diff-derived" for edge in cmg["edges"])
    assert any(str(node.get("entity_source")).startswith("synthetic:") for node in cmg["nodes"])

    bundle = _builder("full").build_prompt_bundle_payload(prompt_input_payload=payload)
    user_prompt = str(bundle["entries"][0]["user_prompt"])
    assert "Graph and Fallback Context" in user_prompt
    assert "Fallback Evidence" in user_prompt
    assert "Commit Messages" in user_prompt


def test_no_fallback_variant_removes_synthetic_diff_calls_and_fallback_text() -> None:
    payload = _builder("no_fallback").build_prompt_input_payload(
        changed_payload=_changed_payload(),
        cmg_payload=_cmg_payload(),
    )

    entry = payload["entries"][0]
    cmg = entry["cmg"]
    assert payload["summary"]["fallback_context_entry_count"] == 0
    assert payload["summary"]["synthetic_entry_count"] == 0
    assert entry["fallback_context"] == {}
    assert cmg["provenance"]["prompt_graph_filter"] == "enre_only_no_fallback"
    assert all(str(edge.get("provenance")) != "diff-derived" for edge in cmg["edges"])
    assert all(str(node.get("entity_source")) in {"", "enre"} for node in cmg["nodes"])

    bundle = _builder("no_fallback").build_prompt_bundle_payload(prompt_input_payload=payload)
    user_prompt = str(bundle["entries"][0]["user_prompt"])
    assert "Graph Context" in user_prompt
    assert "Fallback Evidence" not in user_prompt
    assert "Diff-Derived Calls" not in user_prompt
    assert "diff_call:open" not in user_prompt


def test_text_only_variant_builds_release_level_prompt_only() -> None:
    payload = _builder("text_only").build_prompt_input_payload(
        changed_payload=_changed_payload(),
        cmg_payload=_cmg_payload(),
    )

    assert payload["summary"]["entry_count"] == 1
    assert payload["summary"]["not_applicable_entry_count"] == 1
    assert payload["entries"][0]["symbol"] == "release-level"

    bundle = _builder("text_only").build_prompt_bundle_payload(prompt_input_payload=payload)
    user_prompt = str(bundle["entries"][0]["user_prompt"])
    assert "Changed Files" in user_prompt
    assert "Commit Messages" in user_prompt
    assert "Changed Function" not in user_prompt
    assert "Diff" not in user_prompt
    assert "Graph" not in user_prompt


def test_diff_only_and_no_graph_prompt_variants_keep_expected_evidence() -> None:
    diff_payload = _builder("diff_only").build_prompt_input_payload(
        changed_payload=_changed_payload(),
        cmg_payload=_cmg_payload(),
    )
    diff_bundle = _builder("diff_only").build_prompt_bundle_payload(prompt_input_payload=diff_payload)
    diff_prompt = str(diff_bundle["entries"][0]["user_prompt"])
    assert "Changed Function" in diff_prompt
    assert "Diff" in diff_prompt
    assert "Commit Messages" not in diff_prompt
    assert "Changed Files" not in diff_prompt
    assert "Graph" not in diff_prompt

    no_graph_payload = _builder("no_graph").build_prompt_input_payload(
        changed_payload=_changed_payload(),
        cmg_payload=_cmg_payload(),
    )
    no_graph_bundle = _builder("no_graph").build_prompt_bundle_payload(
        prompt_input_payload=no_graph_payload,
    )
    no_graph_prompt = str(no_graph_bundle["entries"][0]["user_prompt"])
    assert "Changed Function" in no_graph_prompt
    assert "Diff" in no_graph_prompt
    assert "Commit Messages" in no_graph_prompt
    assert "Changed Files" in no_graph_prompt
    assert "Graph Context" not in no_graph_prompt

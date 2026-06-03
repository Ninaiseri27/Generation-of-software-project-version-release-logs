from cpp_release_note_mvp.pipeline.cmg_builder import CmgBuilder
from cpp_release_note_mvp.pipeline.enre_parser import EnreParser


def _raw_enre_payload() -> dict[str, object]:
    return {
        "variables": [
            {
                "id": 1,
                "entityType": "Class",
                "qualifiedName": "DemoSuite",
                "entityFile": "tests/demo.cpp",
                "startLine": 1,
                "endLine": 80,
                "parentID": -1,
            },
            {
                "id": 2,
                "entityType": "Function",
                "qualifiedName": "DemoSuite::GeneratedTestBody",
                "entityFile": "tests/demo.cpp",
                "startLine": 10,
                "endLine": 30,
                "parentID": 1,
            },
            {
                "id": 3,
                "entityType": "Macro",
                "qualifiedName": "TEST_MACRO_CASE",
                "entityFile": "tests/demo.cpp",
                "startLine": 12,
                "endLine": 12,
                "parentID": 2,
            },
        ],
        "relations": [
            {"type": "Define", "src": 2, "dest": 3},
            {"type": "Call", "src": 2, "dest": 2},
        ],
    }


def test_enre_normalizer_keeps_prompt_and_matching_views_separate() -> None:
    graph = EnreParser().parse_payload(_raw_enre_payload()).to_dict()

    assert [entity["kind"] for entity in graph["entities"]] == ["function"]
    assert {entity["kind"] for entity in graph["matching_entities"]} == {"class", "function", "macro"}
    assert graph["summary"]["normalized_entity_count"] == 1
    assert graph["summary"]["matching_entity_count"] == 3
    assert graph["summary"]["matching_relation_type_counts"]["define"] == 1


def test_rich_matching_view_projects_matching_entity_to_prompt_graph_parent() -> None:
    graph = EnreParser().parse_payload(_raw_enre_payload()).to_dict()
    changed_functions = [
        {
            "symbol": "TEST_MACRO_CASE",
            "signature": "TEST_MACRO_CASE()",
            "file_path": "tests/demo.cpp",
            "change_type": "modified",
            "start_line": 12,
            "end_line": 12,
            "diff_hunks": [],
            "notes": [],
        }
    ]

    strict_payload = CmgBuilder(
        changed_functions=changed_functions,
        ref_normalized_graph=graph,
        tgt_normalized_graph=graph,
        matching_view="strict",
    ).build_payload()
    rich_payload = CmgBuilder(
        changed_functions=changed_functions,
        ref_normalized_graph=graph,
        tgt_normalized_graph=graph,
        matching_view="rich",
    ).build_payload()

    assert strict_payload["summary"]["matched_entry_count"] == 0
    assert strict_payload["summary"]["matching_graph_matched_entry_count"] == 0

    entry = rich_payload["entries"][0]
    assert rich_payload["summary"]["matched_entry_count"] == 1
    assert rich_payload["summary"]["matching_graph_matched_entry_count"] == 1
    assert entry["matched_entity_id"] == 2
    assert entry["matched_matching_entity_id"] == 3
    assert entry["matching_entity_kind"] == "macro"
    assert entry["match_level"] == "matching_graph:path+symbol->parent"


def test_rich_matching_view_projects_by_dominant_same_file_diff_call() -> None:
    graph = EnreParser().parse_payload(
        {
            "variables": [
                {
                    "id": 1,
                    "entityType": "Class Template",
                    "qualifiedName": "DemoCase001",
                    "entityFile": "tests/demo.cpp",
                    "startLine": 20,
                    "endLine": 20,
                    "parentID": -1,
                },
                {
                    "id": 2,
                    "entityType": "Function",
                    "qualifiedName": "Helper",
                    "entityFile": "tests/demo.cpp",
                    "startLine": 10,
                    "endLine": 10,
                    "parentID": -1,
                },
                {
                    "id": 3,
                    "entityType": "Function",
                    "qualifiedName": "OtherHelper",
                    "entityFile": "tests/demo.cpp",
                    "startLine": 12,
                    "endLine": 12,
                    "parentID": -1,
                },
            ],
            "relations": [],
        }
    ).to_dict()
    changed_functions = [
        {
            "symbol": "DemoCase001",
            "signature": "HWTEST_F(DemoCase, DemoCase001, TestSize.Level1)",
            "file_path": "tests/demo.cpp",
            "change_type": "modified",
            "start_line": 100,
            "end_line": 120,
            "diff_hunks": [
                {
                    "file_path": "tests/demo.cpp",
                    "old_start": 100,
                    "old_count": 4,
                    "new_start": 100,
                    "new_count": 4,
                    "lines": [
                        "+ Helper();",
                        "+ Helper();",
                        "+ OtherHelper();",
                    ],
                }
            ],
            "notes": [],
        }
    ]

    payload = CmgBuilder(
        changed_functions=changed_functions,
        ref_normalized_graph=graph,
        tgt_normalized_graph=graph,
        matching_view="rich",
    ).build_payload()

    entry = payload["entries"][0]
    assert payload["summary"]["matched_entry_count"] == 1
    assert entry["matched_entity_id"] == 2
    assert entry["matched_matching_entity_id"] == 1
    assert entry["match_level"] == "matching_graph:path+symbol->diff_call_anchor"

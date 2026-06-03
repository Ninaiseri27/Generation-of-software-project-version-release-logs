from cpp_release_note_mvp.pipeline.release_note_generation import ReleaseNoteGenerator


def test_rule_family_does_not_treat_generic_testing_helper_as_database_utility() -> None:
    family = ReleaseNoteGenerator._group_family(
        section="Testing",
        title="Add case_transform helper for testing case-mapping substitution",
        summary=(
            "Added a helper function that simulates Unicode case-mapping scenarios "
            "for substitution tests."
        ),
    )

    assert family != "database-file-corruption-utility"
    assert "database" not in family


def test_rule_family_keeps_database_corruption_utility_when_evidence_is_present() -> None:
    family = ReleaseNoteGenerator._group_family(
        section="Testing",
        title="Add database file corruption utility",
        summary=(
            "Added a helper function for corrupting database files at a selected "
            "offset in regression tests."
        ),
    )

    assert family == "database-file-corruption-utility"


def test_salience_filter_drops_test_only_helper_notes() -> None:
    keep, reason = ReleaseNoteGenerator._release_note_worthiness(
        {
            "section": "Testing",
            "title": "Add parser regression helper",
            "summary": "Adds a test helper fixture for parser regression tests.",
            "source_file_paths": ["tests/parser_regression_test.c"],
        }
    )

    assert keep is False
    assert reason == "testing-only"


def test_salience_filter_keeps_user_visible_api_or_cli_notes() -> None:
    keep, reason = ReleaseNoteGenerator._release_note_worthiness(
        {
            "section": "Features",
            "title": "Add --all option to unset config values",
            "summary": "Allows users to remove all matching configuration values with a new command-line option.",
            "source_file_paths": ["builtin/config.c"],
        }
    )

    assert keep is True
    assert reason == "strong-release-note-signal"


def test_salience_similarity_family_filters_before_grouping() -> None:
    payload = {
        "summary": {"generated_entry_count": 2, "entry_count": 2},
        "entries": [
            {
                "entry_id": "entry-001",
                "symbol": "parse_config",
                "file_path": "builtin/config.c",
                "matched_entity_id": 10,
                "status": "generated",
                "structured_note": {
                    "section": "Features",
                    "title": "Add --all option to unset config values",
                    "summary": (
                        "Allows users to remove all matching configuration values "
                        "with a new command-line option."
                    ),
                },
            },
            {
                "entry_id": "entry-002",
                "symbol": "parse_config_test",
                "file_path": "tests/config_test.c",
                "matched_entity_id": 11,
                "status": "generated",
                "structured_note": {
                    "section": "Testing",
                    "title": "Add parser regression helper",
                    "summary": "Adds a test helper fixture for parser regression tests.",
                },
            },
        ],
    }

    rewritten = ReleaseNoteGenerator.reaggregate_payload(
        payload,
        aggregation_strategy="salience_similarity_family",
    )

    notes = rewritten["aggregated_release_notes"]
    assert len(notes) == 1
    assert notes[0]["aggregation_strategy"] == "salience_similarity_family"
    assert notes[0]["source_entry_ids"] == ["entry-001"]
    assert rewritten["summary"]["deduplicated_release_note_count"] == 1

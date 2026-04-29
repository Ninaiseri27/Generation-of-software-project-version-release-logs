# Release Note Output Schema

This document defines the Stage 3 generation outputs produced from `prompt_bundle.json`.

## `release_note.json`

Top-level structure:

```json
{
  "source": {
    "generator": "release-note-generator-v4"
  },
  "backend": {
    "backend": "mock",
    "model": "mock-rule-based-v1"
  },
  "project": {
    "name": "third_party_sqlite",
    "description": "OpenHarmony third-party SQLite component."
  },
  "version_pair": {
    "ref": "OpenHarmony-v6.0-Release",
    "tgt": "OpenHarmony-v6.0.0.1-Release"
  },
  "summary": {
    "entry_count": 4,
    "generated_entry_count": 4,
    "failed_entry_count": 0,
    "deduplicated_release_note_count": 3
  },
  "entries": [],
  "structured_release_notes": [],
  "aggregated_release_notes": [],
  "deduplicated_release_notes": [],
  "unmatched_symbols": []
}
```

Each `entries[i]` item contains:

```json
{
  "entry_id": "entry-001",
  "symbol": "Common::DestroyDbFile",
  "change_type": "added",
  "match_status": "matched",
  "matched_entity_id": 36748,
  "raw_generated_text": "{\"section\":\"Testing\",\"title\":\"Add database file corruption utility\",\"summary\":\"Adds a helper function to intentionally corrupt database files at a specified offset for testing purposes.\"}",
  "generated_text": "Adds a helper function to intentionally corrupt database files at a specified offset for testing purposes.",
  "structured_note": {
    "section": "Testing",
    "title": "Add database file corruption utility",
    "summary": "Adds a helper function to intentionally corrupt database files at a specified offset for testing purposes."
  },
  "backend": "mock",
  "model": "mock-rule-based-v1",
  "status": "generated",
  "finish_reason": "stop",
  "usage": null,
  "error_message": null
}
```

Notes:

- `raw_generated_text` preserves the model's original response text.
- `generated_text` stores the normalized one-sentence summary used by later aggregation.
- `structured_note` is the normalized per-entry contract used for grouped Markdown rendering.
- `status` is `generated` or `failed`.
- `structured_release_notes` is the aggregated list of unique notes with `section`, `title`, `summary`, `symbols`, and `entry_ids`.
- `aggregated_release_notes` is the report-facing grouped list after deterministic clustering and title/summary merging.
- `deduplicated_release_notes` remains as a compatibility-friendly flattened string list derived from `aggregated_release_notes`.
- `usage` is populated when the backend returns token or request-usage metadata.
- `error_message` is populated when a single entry fails but the whole batch continues.

## `release_note.md`

Markdown structure:

```md
# Draft Release Notes

Project: third_party_sqlite
Version Pair: OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release
Generator: mock / mock-rule-based-v1

## Overview
- Generated Entries: 4 / 4
- Distilled Notes: 3
- Failed Entries: 0

## Testing
- Add database file corruption utility: Adds a helper function to intentionally corrupt database files at a specified offset for testing purposes.
- Expand compressed database corruption tests: Adds regression coverage for corrupted compressed databases, including NOTADB rejection during open and I/O error reporting during query execution.

## Bug Fixes
- Fix tombstone counter overflow: Updates the tombstone counter to use 64-bit values for safer tombstone calculations.
```

Notes:

- Markdown is now a grouped presentation layer derived from `structured_release_notes`.
- Final grouped Markdown prefers `aggregated_release_notes` when available and falls back to `structured_release_notes`.
- The current section order is `Features`, `Bug Fixes`, `Performance`, `Reliability`, `Testing`, `Internal`.
- Deterministic aggregation currently merges related notes by section-aware family heuristics, such as compressed-database corruption tests.
- If some entries fail, Markdown includes a warning line and keeps the successful drafts.

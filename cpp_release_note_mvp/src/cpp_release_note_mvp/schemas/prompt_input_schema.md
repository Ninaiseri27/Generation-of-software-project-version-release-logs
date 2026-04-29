# Prompt Input Schema

This document defines the Stage 3 prompt-facing payloads produced after `cmg.json` is available.

## Goals

- decouple prompt construction from raw `cmg.json`
- keep project metadata, version metadata, and commit metadata in a stable contract
- make later LLM backends consume one consistent schema
- preserve unmatched entries without crashing the pipeline

## `prompt_input.json`

Top-level structure:

```json
{
  "source": {
    "builder": "prompt-input-builder-v3"
  },
  "project": {
    "name": "third_party_sqlite",
    "description": "OpenHarmony third-party SQLite component."
  },
  "version_pair": {
    "repo_path": "D:/repo/path",
    "ref": "OpenHarmony-v6.0-Release",
    "tgt": "OpenHarmony-v6.0.0.1-Release"
  },
  "context": {
    "changed_files": ["src/sqlite3.c"],
    "commit_messages": ["Fix issue while open db"],
    "source_commit_message_count": 10
  },
  "summary": {
    "entry_count": 4,
    "matched_entry_count": 1,
    "unmatched_entry_count": 3,
    "fallback_context_entry_count": 4,
    "synthetic_entry_count": 3,
    "filtered_unmatched_entries": false
  },
  "entries": [],
  "unmatched_symbols": ["CompressTest013"]
}
```

Each `entries[i]` item contains:

```json
{
  "entry_id": "entry-001",
  "symbol": "Common::DestroyDbFile",
  "signature": "void Common::DestroyDbFile(...)",
  "file_path": "unittest/common.cpp",
  "change_type": "added",
  "graph_side": "tgt",
  "match_status": "matched",
  "matched_entity_id": 36748,
  "match_level": "path+symbol",
  "start_line": 101,
  "end_line": 107,
  "diff_hunks": [],
  "change_notes": [],
  "match_notes": [],
  "cmg": {
    "nodes": [],
    "edges": [],
    "provenance": {
      "strategy": "adaptive",
      "changed_node_id": "synthetic:unittest/test.cpp:CompressTest013:693",
      "changed_node_source": "synthetic:macro_test",
      "expansion_reason": "unmatched_synthetic_node"
    }
  },
  "cmg_summary": {
    "node_count": 1,
    "edge_count": 0,
    "synthetic_node_count": 0,
    "diff_call_node_count": 0,
    "user_defined_node_count": 1,
    "external_node_count": 0
  },
  "fallback_context": {
    "reason": "unmatched",
    "pseudo_changed_node": {},
    "diff_called_symbols": [],
    "resolved_diff_calls": [],
    "diff_identifiers": []
  }
}
```

Notes:

- `match_status` is `matched` or `unmatched`.
- `diff_hunks` is copied from Stage 1 / Stage 2 artifacts so prompts can cite real code evidence.
- `cmg` is always present. Under adaptive CMG it can include synthetic nodes and diff-derived call edges even when `match_status` is `unmatched`.
- `cmg_summary` gives a quick signal for later truncation or routing strategies.
- `cmg.provenance` records whether the graph came from strict ENRE matching or adaptive synthetic expansion.
- `fallback_context` is optional but normally present after `cmg-builder-v3`.
- `fallback_context.diff_called_symbols` is extracted from changed diff lines and is useful when ENRE has no matching entity.
- `fallback_context.resolved_diff_calls` stores compact ENRE matches for diff-derived calls when they can be resolved safely.

## `prompt_bundle.json`

This is the model-facing prompt artifact derived from `prompt_input.json`.

Top-level structure:

```json
{
  "source": {
    "builder": "prompt-bundle-builder-v3"
  },
  "project": {},
  "version_pair": {},
  "summary": {},
  "entries": [
    {
      "entry_id": "entry-001",
      "symbol": "Common::DestroyDbFile",
      "change_type": "added",
      "match_status": "matched",
      "matched_entity_id": 36748,
      "system_prompt": "...",
      "user_prompt": "..."
    }
  ],
  "unmatched_symbols": []
}
```

Notes:

- `prompt_bundle.json` is what later LLM backends should consume directly.
- The same `system_prompt` is repeated per entry for simple replay and debugging.
- A future aggregation stage may merge multiple entry-level generations into one final release note.

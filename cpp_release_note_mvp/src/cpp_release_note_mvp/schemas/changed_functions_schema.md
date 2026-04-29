# changed_functions.json Schema Notes

## Top-level fields

- `version_pair`
  - `repo_path`
  - `ref_version`
  - `tgt_version`
- `detector`
- `changed_files`
- `commit_messages`
- `items`

## Item fields

- `symbol`: short function name
- `signature`: normalized function signature string
- `file_path`: repository-relative path
- `change_type`: one of `added`, `modified`, `deleted`
- `start_line`
- `end_line`
- `diff_hunks`
- `notes`

## Diff hunk fields

- `file_path`
- `old_start`
- `old_count`
- `new_start`
- `new_count`
- `lines`

## Current guarantees

- Output is intended for stage-1 MVP use.
- Function identity is currently heuristic.
- Rename/refactor handling is not yet explicit.
- The schema is stable enough for downstream prompt building, but may gain extra provenance fields later.

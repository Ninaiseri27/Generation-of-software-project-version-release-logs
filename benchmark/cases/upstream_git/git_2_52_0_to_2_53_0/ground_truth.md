# Ground Truth: upstream Git v2.52.0 -> v2.53.0

Status: `reviewed_sampled_extension`

This file contains reviewed sampled GT entries for the upstream Git 2.53 extension/stress case. The entries are derived from the official Git 2.53 release notes, local commit messages, and Stage 1 function-level diffs.

## Admission Notes

- Role: `sampled_extension_eval` candidate.
- Official release-note source: `git show v2.53.0:Documentation/RelNotes/2.53.0.adoc`.
- Stage 1 output: `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/changed_functions.json`.
- Scale: `905` changed functions across `223` C/C++ files. This is a large extension/stress case, not a core-average case.
- Scope: prioritize release-note entries with direct C source evidence and user/developer-visible behavior, diagnostics, CLI, repository behavior, platform compatibility, or performance meaning.
- Exclusion policy: documentation-only, localization-only, build-only, CI-only, test-only, and pure refactoring entries are excluded from strict sampled GT unless they directly support a behavior entry.
- Review policy: entries are sampled for evidence quality rather than exhaustive coverage of every Git 2.53 release-note item.

## Reviewed Sampled Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-G201 | Feature | Add `git maintenance is-needed` so callers can ask whether configured maintenance tasks should run. | Official RelNotes: `git maintenance` learned `is-needed`; changed functions `maintenance_is_needed`, `cmd_maintenance`, and `pack_refs_condition` in `builtin/gc.c`. | User/developer-facing command behavior. |
| GT-G202 | Feature | Make experimental `git replay` perform transactional ref updates by default instead of only printing desired ref updates. | Official RelNotes: `git replay` learned to perform ref updates itself; changed functions `handle_ref_update`, `get_ref_action_mode`, `set_up_replay_mode`, `create_commit`, and `cmd_replay` in `builtin/replay.c`. | Experimental command workflow behavior. |
| GT-G203 | Feature | Add `git blame --diff-algorithm=<algo>` to control the diff algorithm used by blame. | Official RelNotes: `git blame` learned `--diff-algorithm`; changed functions `blame_diff_algorithm_minimal`, `blame_diff_algorithm_callback`, `git_blame_config`, and `cmd_blame` in `builtin/blame.c`. | User-facing command option. |
| GT-G204 | Feature | Extend `git repo info` and `git repo structure` output with `--all`, nul-format support, and additional object-database information. | Official RelNotes: `git repo info --all`, `git repo struct -z`, and additional object database information; changed functions `print_all_fields`, `cmd_repo_info`, `stats_table_setup_structure`, `stats_table_print_structure`, `structure_keyvalue_print`, and `cmd_repo_structure` in `builtin/repo.c`. | Grouped because the changes target the same repository-inspection command family. |
| GT-G205 | Feature | Teach `git apply` and `git diff` to detect and report the new whitespace error class `incomplete-line`. | Official RelNotes: `git apply` and `git diff` learned `incomplete-line`; changed functions `record_ws_error`, `adjust_incomplete`, `parse_fragment`, `check_preimage`, `emit_incomplete_line_marker`, and `checkdiff_consume` in `apply.c` and `diff.c`. | User-facing diagnostics and patch validation behavior. |
| GT-G206 | Feature | Add `git fast-import --signed-commits=strip-if-invalid` to drop invalid commit signatures during import. | Official RelNotes: `git fast-import` learned `--signed-commits=strip-if-invalid`; changed functions `handle_strip_if_invalid`, `finalize_commit_buffer`, `add_gpgsig_to_commit`, and `parse_new_commit` in `builtin/fast-import.c`. | Repository import behavior. |
| GT-G207 | Compatibility | Work around the macOS iconv bug for stateful ISO/IEC 2022 encoded strings. | Official RelNotes: macOS iconv workaround; changed function `reencode_string_iconv` in `utf8.c`. | Platform compatibility fix. |
| GT-G208 | Compatibility | Add upstream Windows symbolic-link support, including symlink creation, readlink handling, stat/lstat behavior, and symlink-aware filesystem operations. | Official RelNotes: upstream symbolic link support on Windows; changed functions `symlink`, `readlink`, `mingw_lstat`, `mingw_stat`, `mingw_unlink`, `mingw_rename`, `mingw_getcwd`, and related helpers in `compat/mingw.c`. | Platform behavior and filesystem compatibility. |
| GT-G209 | Reliability | Rewrite attribute macro expansion to avoid recursive expansion and uncontrolled stack exhaustion. | Official RelNotes: attribute macro expansion rewritten to avoid recursion; changed functions `attr_state_queue_push`, `attr_state_queue_pop`, `attr_state_queue_release`, `fill_one`, and removed recursive `macroexpand_one` in `attr.c`. | Runtime robustness in attribute processing. |
| GT-G210 | Fix | Reject `git submodule add` when the submodule uses a different object hash function. | Official RelNotes: submodule add now prevents adding repositories with a different hash function; changed functions `module_add` and `handle_submodule_head_ref` in `builtin/submodule--helper.c`. | Repository correctness and compatibility behavior. |
| GT-G211 | Fix | Correct display-width accounting for non-ASCII worktree paths in `git worktree list`. | Official RelNotes: `git worktree list` miscounted display columns for non-ASCII paths; changed functions `show_worktree`, `measure_widths`, and `list` in `builtin/worktree.c`. | User-facing output formatting. |
| GT-G212 | Fix | Fix an `ort` merge assertion failure for criss-cross histories involving directory and non-directory rename conflicts. | Official RelNotes: `ort` merge assertion failure corrected; changed functions `resolve_trivial_directory_merge`, `process_renames`, `collect_renames`, and `merge_ort_nonrecursive_internal` in `merge-ort.c`. | Merge correctness behavior. |
| GT-G213 | Fix | Diagnose invalid bundle URI configuration that lacks a URI entry instead of crashing. | Official RelNotes: invalid bundle-URI without URI entry is diagnosed instead of crashing; changed functions `bundle_uri_parse_config_format`, `summarize_bundle`, and `fetch_bundle_uri_internal` in `bundle-uri.c`. | Error handling and crash prevention. |
| GT-G214 | Fix | Prevent `git config get --path` from segfaulting on optional path values that do not exist. | Official RelNotes: `git config get --path` segfault with `:(optional)path` corrected; changed functions `git_config_pathname`, `git_configset_get_pathname`, and config get paths in `builtin/config.c` and `config.c`. | User-facing command robustness. |
| GT-G215 | Fix | Fix `git last-modified` corner cases, including uninitialized memory use and handling of `--` pathspec separators. | Official RelNotes: `last-modified` uninitialized memory and `--` pathspec handling corrected; changed functions `process_parent` and `cmd_last_modified` in `builtin/last-modified.c`. | User-facing command correctness. |

## Optional Or Excluded Entries

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| Documentation-only items, manual rewrites, and terminology clarifications | Excluded from strict sampled GT because they do not represent source behavior under the current function-level release-note evaluation target. | Official RelNotes documentation entries. |
| Localization-only items | Excluded because they affect translations, not the C/C++ behavior evaluated by this benchmark. | `l10n:*` commit messages. |
| Build, CI, test, and test-leak entries | Useful to maintainers but outside the core runtime/API/CLI release-note target. | Official RelNotes CI/test/build entries. |
| Broad object-database and packfile refactors without a stable user-visible claim | Excluded unless tied to a specific performance, crash, or command behavior entry. | Many `odb`, `packfile`, and `midx` internal commits. |
| Pure warning-suppression and code-style cleanups | Excluded unless they change runtime behavior or diagnostics visible to users/developers. | Mingw comma-warning rewrite, cleanup-only topics, comment updates. |

## Reviewer Notes

- This sampled extension set keeps `15` strict GT entries.
- The file intentionally samples high-evidence release-note facts rather than exhaustively annotating all Git 2.53 changes.
- This case should not be averaged into the core5 matrix. It is intended to raise the thesis-facing GT inventory and support extension/stress discussion after comparable generation outputs and strict matches are prepared.

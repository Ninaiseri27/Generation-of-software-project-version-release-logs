# Ground Truth: upstream Git v2.51.0 -> v2.51.1

Status: `reviewed_extension`

This file contains reviewed GT entries for the upstream Git extension case. The entries are derived from the official Git 2.51.1 release notes, local commit messages, and Stage 1 function-level diffs.

## Admission Notes

- Role: `extension_eval` candidate.
- Official release-note source: `git show v2.51.1:Documentation/RelNotes/2.51.1.adoc`.
- Stage 1 output: `outputs/benchmark/upstream_git/v2.51.0__v2.51.1/changed_functions.json`.
- Scope: prioritize release-note entries with direct C source evidence under Git's core implementation files.
- Exclusion policy: documentation-only, build-only, formatting-only, and test-only entries are excluded from strict GT unless they support a user/developer-visible behavior entry.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-G001 | UX | Update deprecated-command handling so deeply deprecated commands can show clearer "do you still use it?" guidance and alias alternatives. | Official RelNotes: deprecated-command message updated; commits `you-still-use-that??`, `git: add deprecated category`, and alias-shadowing changes; changed functions `you_still_use_that`, `handle_alias`, `list_cmds`, and `run_argv`. | User-facing command guidance. |
| GT-G002 | Compatibility | Safely cast `size_t` values to `curl_off_t` when interacting with curl APIs. | Official RelNotes: size_t-to-curl_off_t casts updated; commits `http: offer to cast size_t to curl_off_t safely` and `imap-send: be more careful when casting to curl_off_t`; changed `cast_size_t_to_curl_off_t`, `curl_setup_http`, and `curl_append_msgs_to_imap`. | Runtime robustness for HTTP/IMAP paths. |
| GT-G003 | Fix | Reset delayed-progress internal state so custom initial delay values larger than one second take effect. | Official RelNotes: `start_delayed_progress()` did not clear internal state; commit `progress: pay attention to (customized) delay time`; changed functions `display` and `get_default_delay` in `progress.c`. | User-visible progress display behavior. |
| GT-G004 | Fix | Allow interactive rebase to drop merge commits without failing. | Official RelNotes: interactive rebase `drop` on merge commit error corrected; commit `rebase -i: permit 'drop' of a merge commit`; changed sequencer functions including `check_merge_commit_insn`. | User-facing rebase behavior. |
| GT-G005 | Fix | Fix reflog migration bugs when moving reflog entries between reference backends. | Official RelNotes: `git refs migrate` reflog bugs squashed; commits around refs migration and reflog write support; changed `migrate_one_reflog_entry`, `migrate_one_reflog`, `repo_migrate_ref_storage_format`, and `ref_transaction_update_reflog`. | Ref-storage migration behavior. |
| GT-G006 | Fix | Report invalid pushes of non-existing objects as normal user errors instead of triggering `BUG()`. | Official RelNotes: `git push` code path led to `BUG()` but should be `die()`; commit `remote.c: remove BUG in show_push_unqualified_ref_name_error`; changed `show_push_unqualified_ref_name_error` in `remote.c`. | User-facing error handling. |
| GT-G007 | Fix | Correct rename and rename/delete handling in the `ort` merge strategy. | Official RelNotes: various rename handling bugs in `ort` fixed; commits around merge-ort rename and file handling; changed `handle_content_merge`, `path_in_way`, `handle_path_level_conflicts`, `compute_collisions`, `check_for_directory_rename`, `process_renames`, and `collect_renames`. | Merge correctness behavior. |
| GT-G008 | Fix | Correct `git diff --no-index` setup when run from a repository subdirectory or with stdin paths. | Official RelNotes: `git diff --no-index` setup corrected; commit `diff: --no-index should ignore the worktree`; changed `cmd_diff` and diff setup paths. | User-facing diff behavior. |
| GT-G009 | Fix | Make `git diff --name-only` and related modes behave consistently with whitespace/regex ignore options. | Official RelNotes: diff ignore options did not work well with `--name-only` and related modes; commit `diff: ensure consistent diff behavior with ignore options`; changed `quick_consume`, `builtin_diff`, `diff_flush_patch_quietly`, and `diff_flush`. | User-facing diff output behavior. |
| GT-G010 | Reliability | Fix fetch behavior that could incorrectly report existing objects as missing under repack races in partial clones. | Official RelNotes: fetch may mistakenly think present objects are missing under repack race, especially partial clones; commit `fetch-pack: re-scan when double-checking graph objects`; changed `deref_without_lazy_fetch` in `fetch-pack.c`. | Repository transfer reliability. |
| GT-G011 | Reliability | Prevent `upload-pack` from redundantly storing repeated object IDs from broken or malicious fetch clients. | Official RelNotes: broken/malicious fetch can repeat the same object many times and exhaust server memory; commit `upload-pack: don't ACK non-commits repeatedly in protocol v2`; changed `do_got_oid` in `upload-pack.c`. | Server-side robustness. |
| GT-G012 | Fix | Fix corner cases and crashes in multi-pack-index write-out code paths. | Official RelNotes: multiple crashes around midx write-out fixed; commits around `midx-write`; changed `midx_fanout_add_midx_fanout`, `compute_sorted_entries`, `write_midx_bitmap`, `fill_packs_from_midx`, and `write_midx_internal`. | Repository maintenance reliability. |
| GT-G013 | Fix | Correct corner cases in `git log -L` line history handling. | Official RelNotes: corner case bug in `git log -L...`; commits `line-log: fix assertion error` and `line-log: show all line ranges touched by the same diff range`; changed `range_set_difference`, `diff_ranges_filter_touched`, and `dump_diff_hacky_one`. | User-facing history query behavior. |
| GT-G014 | Fix | Make interactive add/patch commands respect `color.diff` and `color.ui` configuration. | Official RelNotes: `git add -p` and friends ignored color configuration; commits around add-interactive color handling; changed `init_color`, `check_color_config`, `init_add_i_state`, `render_hunk`, and `recolor_hunk`. | Interactive UI behavior. |
| GT-G015 | Fix | Clean up commit messages correctly when interactive rebase creates the final commit in a chain of `fixup` commands. | Official RelNotes: `git rebase -i` failed to clean commit log message for final fixup commit; commit `rebase -i: respect commit.cleanup when picking fixups`; changed `run_git_commit`, `try_to_commit`, and `do_pick_commit` in `sequencer.c`. | User-facing rebase commit-message behavior. |
| GT-G016 | Fix | Handle directory/file and file/directory conflicts more gracefully in the files ref backend. | Official RelNotes: files backend should fail only conflicting ref updates while allowing others; commits around `refs/files` conflict handling; changed `transaction_has_case_conflicting_update`, `lock_raw_ref`, `split_head_update`, `check_old_oid`, `lock_ref_for_update`, and `files_transaction_prepare`. | Reference-storage correctness. |

## Optional Or Excluded Entries

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| Documentation-only RelNotes entries | They are useful project documentation updates but do not produce source-level release-note behavior in this tool's function-level extractor. | gitk maintainer docs, MyFirstContribution, compatObjectFormat documentation, GGG instructions. |
| clang-format control macro update | Source-adjacent but formatting-oriented; not a release-note-level behavior change for users/developers. | `clang-format: exclude control macros from SpaceBeforeParens`; changed formatting configuration. |
| Makefile cargo-build serialization | Build-system improvement only; excluded from strict release-note behavior metrics. | `Makefile: build libgit-rs and libgit-sys serially`. |
| Test-only and cleanup commits | Useful evidence for implementation quality but not standalone GT. | t5530 modernization, test fixes, docs markup fixups, ODB wrapper cleanup. |

## Reviewer Notes

- This reviewed extension set keeps `16` strict GT entries.
- The selected entries all have official RelNotes support and direct C-source function evidence.
- Do not average this extension case into the existing core5 matrix until comparable real-backend outputs and `matches_strict` files are complete.

# Evidence Pack: upstream_git v2.51.0 -> v2.51.1

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `git_2_51_0_to_2_51_1`
- Repository: `upstream_git`
- Category: `version_control`
- Reference version: `v2.51.0`
- Target version: `v2.51.1`
- Pipeline status: `verified_stage1`
- Ground-truth status: `reviewed`

## Evidence Sources To Inspect

- [ ] official Git 2.51.1 release notes
- [ ] commit_messages
- [ ] function_level_diff
- [ ] changed_files

## Local Artifacts

- Changed functions: `outputs/benchmark/upstream_git/v2.51.0__v2.51.1/changed_functions.json`

## Pipeline Summary

- Commit count: `134`
- Changed C/C++ files: `42`
- Changed functions: `102`
- Patch only: `False`
- CMG matched entries: `unknown`
- CMG unmatched entries: `unknown`
- Fallback-context entries: `unknown`
- Diff-derived call edges: `unknown`
- Prompt entries: `unknown`
- Mock generated entries: `unknown`

## Commit Messages

- Git 2.51.1
- Merge branch 'kh/doc-patch-id-markup-fix' into maint-2.51
- Merge branch 'ja/doc-markup-attached-paragraph-fix' into maint-2.51
- Merge branch 'en/doc-merge-tree-describe-merge-base' into maint-2.51
- Merge branch 'mh/doc-credential-url-prefix' into maint-2.51
- Merge branch 'ps/odb-clean-stale-wrappers' into maint-2.51
- Merge branch 'ag/doc-sendmail-gmail-example-update' into maint-2.51
- Merge branch 'jc/doc-includeif-hasconfig-remote-url-fix' into maint-2.51
- Merge branch 'mm/worktree-doc-typofix' into maint-2.51
- Merge branch 'rs/object-name-extend-abbrev-len-update' into maint-2.51
- Merge branch 'kh/doc-markup-fixes' into maint-2.51
- Merge branch 'km/alias-doc-markup-fix' into maint-2.51
- Merge branch 'js/doc-sending-patch-via-thunderbird' into maint-2.51
- Merge branch 'kr/clone-synopsis-fix' into maint-2.51
- Merge branch 'rj/t6137-cygwin-fix' into maint-2.51
- Merge branch 'kh/doc-git-log-markup-fix' into maint-2.51
- Merge branch 'kn/refs-files-case-insensitive' into maint-2.51
- Merge branch 'pw/rebase-i-cleanup-fix' into maint-2.51
- Merge branch 'jk/add-i-color' into maint-2.51
- Merge branch 'sg/line-log-boundary-fixes' into maint-2.51
- Merge branch 'ps/upload-pack-oom-protection' into maint-2.51
- Merge branch 'ds/midx-write-fixes' into maint-2.51
- Merge branch 'ds/path-walk-repack-fix' into maint-2.51
- Merge branch 'jk/fetch-check-graph-objects-fix' into maint-2.51
- Merge branch 'ly/diff-name-only-with-diff-from-content' into maint-2.51
- Merge branch 'jc/diff-no-index-in-subdir' into maint-2.51
- Merge branch 'en/ort-rename-fixes' into maint-2.51
- Merge branch 'dl/push-missing-object-error' into maint-2.51
- Merge branch 'ps/reflog-migrate-fixes' into maint-2.51
- Merge branch 'js/rebase-i-allow-drop-on-a-merge' into maint-2.51
- RelNotes: minor fixups before 2.51.1
- Prepare for 2.51.1
- Merge branch 'ps/ci-avoid-broken-sudo-on-ubuntu' into maint-2.51
- Merge branch 'jk/curl-global-trace-components' into maint-2.51
- Merge branch 'kh/doc-fast-import-markup-fix' into maint-2.51
- Merge branch 'kh/doc-config-typofix' into maint-2.51
- Merge branch 'kh/doc-interpret-trailers-markup-fix' into maint-2.51
- Merge branch 'ds/doc-count-objects-fix' into maint-2.51
- Merge branch 'ja/asciidoc-doctor-verbatim-fixes' into maint-2.51
- Merge branch 'da/cargo-serialize' into maint-2.51
- Merge branch 'js/progress-delay-fix' into maint-2.51
- Merge branch 'js/curl-off-t-fixes' into maint-2.51
- Merge branch 'jt/clang-format-foreach-wo-space-before-parenthesis' into maint-2.51
- Merge branch 'ds/doc-ggg-pr-fork-clarify' into maint-2.51
- Merge branch 'js/doc-gitk-history' into maint-2.51
- Merge branch 'bc/doc-compat-object-format-not-working' into maint-2.51
- Merge branch 'kh/you-still-use-whatchanged-fix' into maint-2.51
- ci: fix broken jobs on Ubuntu 25.10 caused by switch to sudo-rs(1)
- doc: fix indentation of refStorage item in git-config(1)
- Documentation/git-merge-tree.adoc: clarify the --merge-base option
- docs/gitcredentials: describe URL prefix matching
- doc: patch-id: fix accidental literal blocks
- clang-format: exclude control macros from SpaceBeforeParens
- doc: change the markup of paragraphs following a nested list item
- http-push: avoid new compile error
- imap-send: be more careful when casting to `curl_off_t`
- http: offer to cast `size_t` to `curl_off_t` safely
- sequencer: remove VERBATIM_MSG flag
- rebase -i: respect commit.cleanup when picking fixups
- BreakingChanges: remove claim about whatchanged reports
- whatchanged: remove not-even-shorter clause
- whatchanged: hint about git-log(1) and aliasing
- you-still-use-that??: help the user help themselves
- t0014: test shadowing of aliases for a sample of builtins
- git: allow alias-shadowing deprecated builtins
- git: move seen-alias bookkeeping into handle_alias(...)
- git: add `deprecated` category to --list-cmds
- Makefile: don’t add whatchanged after it has been removed
- refs/files: handle D/F conflicts during locking
- refs/files: handle F/D conflicts in case-insensitive FS
- refs/files: use correct error type when lock exists
- refs/files: catch conflicts on case-insensitive file-systems
- odb: drop deprecated wrapper functions
- doc: fast-import: replace literal block with paragraph
- contrib/diff-highlight: mention interactive.diffFilter
- add-interactive: manually fall back color config to color.ui
- add-interactive: respect color.diff for diff coloring
- stash: pass --no-color to diff plumbing child processes
- upload-pack: don't ACK non-commits repeatedly in protocol v2
- t5530: modernize tests
- midx-write: simplify error cases
- midx-write: reenable signed comparison errors
- midx-write: use uint32_t for preferred_pack_idx
- midx-write: use cleanup when incremental midx fails
- midx-write: put failing response value back
- midx-write: only load initialized packs
- object-name: declare pointer type of extend_abbrev_len()'s 2nd parameter
- docs: fix typo in worktree.adoc 'extension'
- doc: remove extra backtick for inline-verbatim
- doc: add missing backtick for inline-verbatim
- doc: fix formatting of function-wrap shell alias
- curl: add support for curl_global_trace() components
- Makefile: build libgit-rs and libgit-sys serially
- docs: update sendmail docs to use more secure SMTP server for Gmail
- docs: note that extensions.compatobjectformat is incomplete
- progress: pay attention to (customized) delay time
- doc: config: replace backtick with apostrophe for possessive
- fetch-pack: re-scan when double-checking graph objects
- doc/format-patch: adjust Thunderbird MUA hint to new add-on
- doc: clarify which remotes can be used with GitGitGadget
- path-walk: create initializer for path lists
- path-walk: fix setup of pending objects
- doc: interpret-trailers: close all pairs of single quotes
- config: document includeIf conditions consistently
- doc: fix asciidoc format compatibility in pretty-formats.adoc
- line-log: show all line ranges touched by the same diff range
- line-log: fix assertion error
- doc/gitk: update reference to the external project
- count-objects: document count-objects pack
- docs: remove stray bracket from git-clone synopsis
- diff: --no-index should ignore the worktree
- t6137-*.sh: fix test failure on cygwin
- doc: git-log: fix description list
- remote.c: convert if-else ladder to switch
- remote.c: remove BUG in show_push_unqualified_ref_name_error()
- t5516: remove surrounding empty lines in test bodies
- diff: ensure consistent diff behavior with ignore options
- merge-ort: fix directory rename on top of source of other rename/delete
- merge-ort: fix incorrect file handling
- merge-ort: clarify the interning of strings in opt->priv->path
- t6423: fix missed staging of file in testcases 12i,12j,12k
- t6423: document two bugs with rename-to-self testcases
- merge-ort: drop unnecessary temporary in check_for_directory_rename()
- merge-ort: update comments to modern testfile location
- rebase -i: permit 'drop' of a merge commit
- refs: fix invalid old object IDs when migrating reflogs
- refs: stop unsetting REF_HAVE_OLD for log-only updates
- refs/files: detect race when generating reflog entry for HEAD
- refs: fix identity for migrated reflogs
- ident: fix type of string length parameter
- builtin/reflog: implement subcommand to write new entries
- refs: export `ref_transaction_update_reflog()`
- builtin/reflog: improve grouping of subcommands
- Documentation/git-reflog: convert to use synopsis type

## Changed C/C++ Files

- `add-interactive.c`
- `add-interactive.h`
- `add-patch.c`
- `builtin/diff.c`
- `builtin/fetch.c`
- `builtin/log.c`
- `builtin/pack-objects.c`
- `builtin/pack-redundant.c`
- `builtin/reflog.c`
- `builtin/stash.c`
- `diff.c`
- `diff.h`
- `fetch-pack.c`
- `git-compat-util.h`
- `git-curl-compat.h`
- `git.c`
- `http-push.c`
- `http.c`
- `http.h`
- `ident.c`
- `ident.h`
- `imap-send.c`
- `line-log.c`
- `merge-ort.c`
- `midx-write.c`
- `object-name.c`
- `odb.h`
- `pack-objects.c`
- `path-walk.c`
- `progress.c`
- `refs.c`
- `refs.h`
- `refs/files-backend.c`
- `refs/refs-internal.h`
- `refs/reftable-backend.c`
- `remote-curl.c`
- `remote.c`
- `sequencer.c`
- `t/helper/test-pack-deltas.c`
- `upload-pack.c`
- `usage.c`
- `xdiff-interface.h`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `init_color` | `added` | `add-interactive.c` | `23-37` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 2 | `init_color` | `deleted` | `add-interactive.c` | `23-37` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 3 | `check_color_config` | `added` | `add-interactive.c` | `39-58` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 4 | `init_add_i_state` | `modified` | `add-interactive.c` | `60-126` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 5 | `clear_add_i_state` | `modified` | `add-interactive.c` | `128-135` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 6 | `run_add_i` | `modified` | `add-interactive.c` | `1163-1262` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 7 | `err` | `modified` | `add-patch.c` | `295-305` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 8 | `parse_diff` | `modified` | `add-patch.c` | `414-651` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `render_hunk` | `modified` | `add-patch.c` | `667-728` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 10 | `recolor_hunk` | `modified` | `add-patch.c` | `1086-1116` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 11 | `patch_update_file` | `modified` | `add-patch.c` | `1411-1763` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `cmd_diff` | `modified` | `builtin/diff.c` | `399-651` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `ref_transaction_rejection_handler` | `modified` | `builtin/fetch.c` | `1651-1687` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 14 | `cmd_whatchanged` | `modified` | `builtin/log.c` | `521-562` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 15 | `show_object_pack_hint` | `modified` | `builtin/pack-objects.c` | `3771-3800` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 16 | `add_objects_by_path` | `modified` | `builtin/pack-objects.c` | `4573-4624` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 17 | `cmd_pack_redundant` | `modified` | `builtin/pack-redundant.c` | `592-699` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 18 | `cmd_reflog_write` | `added` | `builtin/reflog.c` | `409-460` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 19 | `cmd_reflog` | `modified` | `builtin/reflog.c` | `465-490` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 20 | `diff_tree_binary` | `modified` | `builtin/stash.c` | `370-384` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 21 | `stash_staged` | `modified` | `builtin/stash.c` | `1271-1302` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `stash_patch` | `modified` | `builtin/stash.c` | `1304-1366` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 23 | `do_push_stash` | `modified` | `builtin/stash.c` | `1594-1826` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 24 | `quick_consume` | `added` | `diff.c` | `2447-2454` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 25 | `builtin_diff` | `modified` | `diff.c` | `3543-3803` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 26 | `diff_flush_patch_quietly` | `added` | `diff.c` | `6176-6189` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 27 | `diff_flush` | `modified` | `diff.c` | `6799-6903` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 28 | `deref_without_lazy_fetch` | `modified` | `fetch-pack.c` | `136-179` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 29 | `list_cmds` | `modified` | `git.c` | `78-124` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 30 | `handle_options` | `modified` | `git.c` | `157-366` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 31 | `handle_alias` | `deleted` | `git.c` | `363-438` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 32 | `handle_alias` | `added` | `git.c` | `368-464` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 33 | `list_builtins` | `deleted` | `git.c` | `671-679` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 34 | `list_builtins` | `added` | `git.c` | `697-710` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 35 | `is_deprecated_command` | `added` | `git.c` | `827-831` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 36 | `run_argv` | `modified` | `git.c` | `833-912` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 37 | `curl_setup_http` | `modified` | `http-push.c` | `204-220` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 38 | `http_init` | `modified` | `http.c` | `1305-1426` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 39 | `cast_size_t_to_curl_off_t` | `added` | `http.h` | `99-106` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 40 | `split_ident_line` | `added` | `ident.c` | `275-350` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 41 | `split_ident_line` | `deleted` | `ident.c` | `275-350` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 42 | `curl_append_msgs_to_imap` | `modified` | `imap-send.c` | `1681-1741` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 43 | `range_set_difference` | `modified` | `line-log.c` | `190-230` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 44 | `diff_ranges_filter_touched` | `modified` | `line-log.c` | `402-425` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 45 | `dump_diff_hacky_one` | `modified` | `line-log.c` | `905-1010` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 46 | `handle_content_merge` | `modified` | `merge-ort.c` | `2128-2274` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 47 | `path_in_way` | `deleted` | `merge-ort.c` | `2316-2324` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 48 | `path_in_way` | `added` | `merge-ort.c` | `2321-2335` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 49 | `handle_path_level_conflicts` | `deleted` | `merge-ort.c` | `2332-2402` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 50 | `handle_path_level_conflicts` | `added` | `merge-ort.c` | `2343-2414` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 51 | `compute_collisions` | `modified` | `merge-ort.c` | `2511-2562` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 52 | `check_for_directory_rename` | `deleted` | `merge-ort.c` | `2573-2640` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 53 | `check_for_directory_rename` | `added` | `merge-ort.c` | `2585-2651` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 54 | `process_renames` | `modified` | `merge-ort.c` | `2862-3190` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 55 | `collect_renames` | `modified` | `merge-ort.c` | `3418-3478` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 56 | `midx_fanout_add_midx_fanout` | `added` | `midx-write.c` | `259-292` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 57 | `midx_fanout_add_midx_fanout` | `deleted` | `midx-write.c` | `260-293` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 58 | `compute_sorted_entries` | `modified` | `midx-write.c` | `330-397` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 59 | `write_midx_bitmap` | `modified` | `midx-write.c` | `838-914` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 60 | `fill_packs_from_midx` | `added` | `midx-write.c` | `923-942` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 61 | `fill_packs_from_midx` | `deleted` | `midx-write.c` | `923-962` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 62 | `write_midx_internal` | `modified` | `midx-write.c` | `1030-1506` | `unmatched` | unmatched; level=unmatched; diff_hunks=40; fallback_calls=0 |
| 63 | `extend_abbrev_len` | `added` | `object-name.c` | `699-710` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 64 | `extend_abbrev_len` | `deleted` | `object-name.c` | `699-711` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 65 | `oid_object_info_extended` | `deleted` | `odb.h` | `481-487` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 66 | `oid_object_info` | `deleted` | `odb.h` | `489-494` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 67 | `repo_read_object_file` | `deleted` | `odb.h` | `496-502` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 68 | `has_object` | `deleted` | `odb.h` | `504-509` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 69 | `add_path_to_list` | `added` | `path-walk.c` | `108-124` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 70 | `add_tree_entries` | `modified` | `path-walk.c` | `126-219` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 71 | `setup_pending_objects` | `modified` | `path-walk.c` | `331-449` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 72 | `display` | `modified` | `progress.c` | `112-173` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 73 | `get_default_delay` | `modified` | `progress.c` | `281-289` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 74 | `ref_transaction_maybe_set_rejected` | `modified` | `refs.c` | `1215-1249` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 75 | `ref_transaction_update_reflog` | `deleted` | `refs.c` | `1371-1408` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 76 | `ref_transaction_update_reflog` | `added` | `refs.c` | `1372-1405` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 77 | `migrate_one_reflog_entry` | `modified` | `refs.c` | `2993-3020` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 78 | `migrate_one_reflog` | `modified` | `refs.c` | `3022-3037` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 79 | `repo_migrate_ref_storage_format` | `modified` | `refs.c` | `3121-3311` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 80 | `ref_update_expects_existing_old_ref` | `modified` | `refs.c` | `3313-3320` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| ... | ... | ... | ... | ... | ... | truncated at 80 of 102 functions |

## Function-Level Diff Snippets

### 1. `init_color` in `add-interactive.c`

```diff
+static void init_color(struct repository *r, int use_color,
+	if (!use_color)
```

### 2. `init_color` in `add-interactive.c`

```diff
-static void init_color(struct repository *r, struct add_i_state *s,
-	if (!s->use_color)
```

### 3. `check_color_config` in `add-interactive.c`

```diff
+static int check_color_config(struct repository *r, const char *var)
+	int ret;
+
+	if (repo_config_get_value(r, var, &value))
+		ret = -1;
+	else
+		ret = git_config_colorbool(var, value);
+
+	/*
+	 * Do not rely on want_color() to fall back to color.ui for us. It uses
+	 * the value parsed by git_color_config(), which may not have been
+	 * called by the main command.
... truncated 5 additional diff lines ...
```

### 4. `init_add_i_state` in `add-interactive.c`

```diff
+void init_add_i_state(struct add_i_state *s, struct repository *r,
+		      struct add_p_opt *add_p_opt)
+{
-		   GIT_COLOR_BOLD_RED);
-
-	init_color(r, s, "diff.frag", s->fraginfo_color,
-		   diff_get_color(s->use_color, DIFF_FRAGINFO));
-	init_color(r, s, "diff.context", s->context_color, "fall back");
+	s->use_color_interactive = check_color_config(r, "color.interactive");
+
+	init_color(r, s->use_color_interactive, "interactive.header",
+		   s->header_color, GIT_COLOR_BOLD);
... truncated 33 additional diff lines ...
```

### 5. `clear_add_i_state` in `add-interactive.c`

```diff
+	s->use_color_interactive = -1;
+	s->use_color_diff = -1;
```

### 6. `run_add_i` in `add-interactive.c`

```diff
-	if (s.use_color) {
+	if (s.use_color_interactive) {
-		data.reset = s.reset_color;
+		data.reset = s.reset_color_interactive;
```

### 7. `err` in `add-patch.c`

```diff
-	puts(s->s.reset_color);
+	puts(s->s.reset_color_interactive);
```

### 8. `parse_diff` in `add-patch.c`

```diff
-	if (want_color_fd(1, -1)) {
+	if (want_color_fd(1, s->s.use_color_diff)) {
```

### 9. `render_hunk` in `add-patch.c`

```diff
-			strbuf_addf(out, "%s\n", s->s.reset_color);
+			strbuf_addf(out, "%s\n", s->s.reset_color_diff);
```

### 10. `recolor_hunk` in `add-patch.c`

```diff
-		strbuf_addstr(&s->colored, s->s.reset_color);
+		strbuf_addstr(&s->colored, s->s.reset_color_diff);
```

### 11. `patch_update_file` in `add-patch.c`

```diff
-		if (*s->s.reset_color)
-			fputs(s->s.reset_color, stdout);
+		if (*s->s.reset_color_interactive)
+			fputs(s->s.reset_color_interactive, stdout);
```

### 12. `cmd_diff` in `builtin/diff.c`

```diff
+
+	/*
+	 * If we are ignoring the fact that our current directory may
+	 * be part of a working tree controlled by a Git repository to
+	 * pretend to be a "better GNU diff", we should undo the
+	 * effect of the setup code that did a chdir() to the top of
+	 * the working tree.  Where we came from is recorded in the
+	 * prefix.
+	 */
+	if (no_index && prefix) {
+		if (chdir(prefix))
+			die(_("cannot come back to cwd"));
... truncated 3 additional diff lines ...
```

### 13. `ref_transaction_rejection_handler` in `builtin/fetch.c`

```diff
-	if (err == REF_TRANSACTION_ERROR_NAME_CONFLICT && !data->conflict_msg_shown) {
+	if (err == REF_TRANSACTION_ERROR_CASE_CONFLICT && ignore_case &&
+	    !data->case_sensitive_msg_shown) {
+		error(_("You're on a case-insensitive filesystem, and the remote you are\n"
+			"trying to fetch from has references that only differ in casing. It\n"
+			"is impossible to store such references with the 'files' backend. You\n"
+			"can either accept this as-is, in which case you won't be able to\n"
+			"store all remote references on disk. Or you can alternatively\n"
+			"migrate your repository to use the 'reftable' backend with the\n"
+			"following command:\n\n    git refs migrate --ref-format=reftable\n\n"
+			"Please keep in mind that not all implementations of Git support this\n"
+			"new format yet. So if you use tools other than Git to access this\n"
... truncated 6 additional diff lines ...
```

### 14. `cmd_whatchanged` in `builtin/log.c`

```diff
-		you_still_use_that("git whatchanged");
+		you_still_use_that("git whatchanged",
+				   _("\n"
+				     "hint: You can replace 'git whatchanged <opts>' with:\n"
+				     "hint:\tgit log <opts> --raw --no-merges\n"
+				     "hint: Or make an alias:\n"
+				     "hint:\tgit config set --global alias.whatchanged 'log --raw --no-merges'\n"
+				     "\n"));
```

### 15. `show_object_pack_hint` in `builtin/pack-objects.c`

```diff
-		    !has_object(the_repository, &object->oid, 0))
+		    !odb_has_object(the_repository->objects, &object->oid, 0))
```

### 16. `add_objects_by_path` in `builtin/pack-objects.c`

```diff
-		    oid_object_info_extended(the_repository, oid, &oi,
-					     OBJECT_INFO_FOR_PREFETCH) < 0)
+		    odb_read_object_info_extended(the_repository->objects, oid, &oi,
+						  OBJECT_INFO_FOR_PREFETCH) < 0)
```

### 17. `cmd_pack_redundant` in `builtin/pack-redundant.c`

```diff
-		you_still_use_that("git pack-redundant");
+		you_still_use_that("git pack-redundant", NULL);
```

### 18. `cmd_reflog_write` in `builtin/reflog.c`

```diff
+static int cmd_reflog_write(int argc, const char **argv, const char *prefix,
+			    struct repository *repo)
+{
+	const struct option options[] = {
+		OPT_END()
+	};
+	struct object_id old_oid, new_oid;
+	struct strbuf err = STRBUF_INIT;
+	struct ref_transaction *tx;
+	const char *ref, *message;
+	int ret;
+
... truncated 40 additional diff lines ...
```

### 19. `cmd_reflog` in `builtin/reflog.c`

```diff
+		OPT_SUBCOMMAND("write", &fn, cmd_reflog_write),
+		OPT_SUBCOMMAND("delete", &fn, cmd_reflog_delete),
+		OPT_SUBCOMMAND("expire", &fn, cmd_reflog_expire),
```

### 20. `diff_tree_binary` in `builtin/stash.c`

```diff
-	strvec_pushl(&cp.args, "diff-tree", "--binary", NULL);
+	strvec_pushl(&cp.args, "diff-tree", "--binary", "--no-color", NULL);
```

### 21. `stash_staged` in `builtin/stash.c`

```diff
+		     "--no-color",
```

### 22. `stash_patch` in `builtin/stash.c`

```diff
+		     "--no-color",
```

### 23. `do_push_stash` in `builtin/stash.c`

```diff
+				     "--no-color",
```

### 24. `quick_consume` in `diff.c`

```diff
+static int quick_consume(void *priv, char *line UNUSED, unsigned long len UNUSED)
+{
+	struct emit_callback *ecbdata = priv;
+	struct diff_options *o = ecbdata->opt;
+
+	o->found_changes = 1;
+	return 1;
+}
```

### 25. `builtin_diff` in `diff.c`

```diff
-		if (xdi_diff_outf(&mf1, &mf2, NULL, fn_out_consume,
-				  &ecbdata, &xpp, &xecfg))
+		if (o->dry_run) {
+			/*
+			 * Unlike the !dry_run case, we need to ignore the
+			 * return value from xdi_diff_outf() here, because
+			 * xdi_diff_outf() takes non-zero return from its
+			 * callback function as a sign of error and returns
+			 * early (which is why we return non-zero from our
+			 * callback, quick_consume()).  Unfortunately,
+			 * xdi_diff_outf() signals an error by returning
+			 * non-zero.
... truncated 5 additional diff lines ...
```

### 26. `diff_flush_patch_quietly` in `diff.c`

```diff
+static int diff_flush_patch_quietly(struct diff_filepair *p, struct diff_options *o)
+{
+	int saved_dry_run = o->dry_run;
+	int saved_found_changes = o->found_changes;
+	int ret;
+
+	o->dry_run = 1;
+	o->found_changes = 0;
+	diff_flush_patch(p, o);
+	ret = o->found_changes;
+	o->dry_run = saved_dry_run;
+	o->found_changes |= saved_found_changes;
... truncated 2 additional diff lines ...
```

### 27. `diff_flush` in `diff.c`

```diff
+
+			if (!check_pair_status(p))
+				continue;
+
+			if (options->flags.diff_from_contents &&
+			    !diff_flush_patch_quietly(p, options))
+				continue;
+
+			flush_one_pair(p, options);
-		/*
-		 * run diff_flush_patch for the exit status. setting
-		 * options->file to /dev/null should be safe, because we
... truncated 8 additional diff lines ...
```

### 28. `deref_without_lazy_fetch` in `fetch-pack.c`

```diff
-			if (!odb_has_object(the_repository->objects, oid, 0))
+			if (!odb_has_object(the_repository->objects, oid,
+					    HAS_OBJECT_RECHECK_PACKED))
```

### 29. `list_cmds` in `git.c`

```diff
-			list_builtins(&list, 0);
+			list_builtins(&list, 0, 0);
+		else if (match_token(spec, len, "deprecated"))
+			list_builtins(&list, DEPRECATED, 0);
```

### 30. `handle_options` in `git.c`

```diff
-				list_builtins(&list, NO_PARSEOPT);
+				list_builtins(&list, 0, NO_PARSEOPT);
```

### 31. `handle_alias` in `git.c`

```diff
-static int handle_alias(struct strvec *args)
```

### 32. `handle_alias` in `git.c`

```diff
+static int handle_alias(struct strvec *args, struct string_list *expanded_aliases)
+		struct string_list_item *seen;
+
+		string_list_append(expanded_aliases, alias_command);
+		seen = unsorted_string_list_lookup(expanded_aliases,
+						   new_argv[0]);
+
+		if (seen) {
+			struct strbuf sb = STRBUF_INIT;
+			for (size_t i = 0; i < expanded_aliases->nr; i++) {
+				struct string_list_item *item = &expanded_aliases->items[i];
+
... truncated 10 additional diff lines ...
```

### 33. `list_builtins` in `git.c`

```diff
-static void list_builtins(struct string_list *out, unsigned int exclude_option)
-		if (exclude_option &&
-		    (commands[i].option & exclude_option))
```

### 34. `list_builtins` in `git.c`

```diff
+static void list_builtins(struct string_list *out,
+			  unsigned int include_option,
+			  unsigned int exclude_option)
+	if (include_option && exclude_option)
+		BUG("'include_option' and 'exclude_option' are mutually exclusive");
+		if (include_option && !(commands[i].option & include_option))
+			continue;
+		if (exclude_option && (commands[i].option & exclude_option))
```

### 35. `is_deprecated_command` in `git.c`

```diff
+static int is_deprecated_command(const char *cmd)
+{
+	struct cmd_struct *builtin = get_builtin(cmd);
+	return builtin && (builtin->option & DEPRECATED);
+}
```

### 36. `run_argv` in `git.c`

```diff
+	struct string_list expanded_aliases = STRING_LIST_INIT_DUP;
+		/*
+		 * Allow deprecated commands to be overridden by aliases. This
+		 * creates a seamless path forward for people who want to keep
+		 * using the name after it is gone, but want to skip the
+		 * deprecation complaint in the meantime.
+		 */
+		if (is_deprecated_command(args->v[0]) &&
+		    handle_alias(args, &expanded_aliases)) {
+			done_alias = 1;
+			continue;
+		}
... truncated 22 additional diff lines ...
```

### 37. `curl_setup_http` in `http-push.c`

```diff
-	curl_easy_setopt(curl, CURLOPT_INFILESIZE, buffer->buf.len);
+	curl_easy_setopt(curl, CURLOPT_INFILESIZE_LARGE,
+			 cast_size_t_to_curl_off_t(buffer->buf.len));
```

### 38. `http_init` in `http.c`

```diff
+#ifdef GIT_CURL_HAVE_GLOBAL_TRACE
+	{
+		const char *comp = getenv("GIT_TRACE_CURL_COMPONENTS");
+		if (comp)
+			curl_global_trace(comp);
+	}
+#endif
+
```

### 39. `cast_size_t_to_curl_off_t` in `http.h`

```diff
+static inline curl_off_t cast_size_t_to_curl_off_t(size_t a)
+{
+	uintmax_t size = a;
+	if (size > maximum_signed_value_of_type(curl_off_t))
+		die(_("number too large to represent as curl_off_t "
+		      "on this platform: %"PRIuMAX), (uintmax_t)a);
+	return (curl_off_t)a;
+}
```

### 40. `split_ident_line` in `ident.c`

```diff
+int split_ident_line(struct ident_split *split, const char *line, size_t len)
```

### 41. `split_ident_line` in `ident.c`

```diff
-int split_ident_line(struct ident_split *split, const char *line, int len)
```

### 42. `curl_append_msgs_to_imap` in `imap-send.c`

```diff
-				 (curl_off_t)(msgbuf.buf.len-prev_len));
+				 cast_size_t_to_curl_off_t(msgbuf.buf.len-prev_len));
```

### 43. `range_set_difference` in `line-log.c`

```diff
-			if (j >= b->nr || end < b->ranges[j].start) {
+			if (j >= b->nr || end <= b->ranges[j].start) {
```

### 44. `diff_ranges_filter_touched` in `line-log.c`

```diff
-		while (diff->target.ranges[i].start > rs->ranges[j].end) {
+		while (diff->target.ranges[i].start >= rs->ranges[j].end) {
```

### 45. `dump_diff_hacky_one` in `line-log.c`

```diff
+		/*
+		 * If a diff range touches multiple line ranges, then all
+		 * those line ranges should be shown, so take a step back if
+		 * the current line range is still in the previous diff range
+		 * (even if only partially).
+		 */
+		if (j > 0 && diff->target.ranges[j-1].end > t_start)
+			j--;
+
-		if (j == diff->target.nr || diff->target.ranges[j].start > t_end)
+		if (j == diff->target.nr || diff->target.ranges[j].start >= t_end)
```

### 46. `handle_content_merge` in `merge-ort.c`

```diff
-		 * b->mode; that causes t6036 "check conflicting mode for
+		 * b->mode; that causes t6416 "check conflicting mode for
```

### 47. `path_in_way` in `merge-ort.c`

```diff
-static int path_in_way(struct strmap *paths, const char *path, unsigned side_mask)
-	return mi->clean || (side_mask & (ci->filemask | ci->dirmask));
```

### 48. `path_in_way` in `merge-ort.c`

```diff
+static int path_in_way(struct strmap *paths,
+		       const char *path,
+		       unsigned side_mask,
+		       struct diff_filepair *p)
+	return mi->clean || (side_mask & (ci->filemask | ci->dirmask))
+	  /* See testcases 12[npq] of t6423 for this next condition */
+			 || ((ci->filemask & 0x01) &&
+			     strcmp(p->one->path, path));
```

### 49. `handle_path_level_conflicts` in `merge-ort.c`

```diff
-	} else if (path_in_way(&opt->priv->paths, new_path, 1 << side_index)) {
```

### 50. `handle_path_level_conflicts` in `merge-ort.c`

```diff
+					 struct diff_filepair *p,
+	} else if (path_in_way(&opt->priv->paths, new_path, 1 << side_index, p)) {
```

### 51. `compute_collisions` in `merge-ort.c`

```diff
-	 * See testcases 9e and all of section 5 from t6043 for examples.
+	 * See testcases 9e and all of section 5 from t6423 for examples.
```

### 52. `check_for_directory_rename` in `merge-ort.c`

```diff
-	struct strmap_entry *otherinfo;
-	 * That's why otherinfo and dir_rename_exclusions is here.
-	 * confusion; See testcases 9c and 9d of t6043.
-	otherinfo = strmap_get_entry(dir_rename_exclusions, new_dir);
-	if (otherinfo) {
-	new_path = handle_path_level_conflicts(opt, path, side_index,
```

### 53. `check_for_directory_rename` in `merge-ort.c`

```diff
+					struct diff_filepair *p,
+	 * That's why dir_rename_exclusions is here.
+	 * confusion; See testcases 9c and 9d of t6423.
+	if (strmap_contains(dir_rename_exclusions, new_dir)) {
+	new_path = handle_path_level_conflicts(opt, path, side_index, p,
```

### 54. `process_renames` in `merge-ort.c`

```diff
+		/*
+		 * Directory renames can result in rename-to-self; the code
+		 * below assumes we have A->B with different A & B, and tries
+		 * to move all entries to path B.  If A & B are the same path,
+		 * the logic can get confused, so skip further processing when
+		 * A & B are already the same path.
+		 *
+		 * As a reminder, we can avoid strcmp here because all paths
+		 * are interned in opt->priv->paths; see the comment above
+		 * "paths" in struct merge_options_internal.
+		 */
+		if (oldpath == newpath)
... truncated 2 additional diff lines ...
```

### 55. `collect_renames` in `merge-ort.c`

```diff
-						      side_index,
+						      side_index, p,
```

### 56. `midx_fanout_add_midx_fanout` in `midx-write.c`

```diff
+					uint32_t preferred_pack)
+		if ((preferred_pack != NO_PREFERRED_PACK) &&
```

### 57. `midx_fanout_add_midx_fanout` in `midx-write.c`

```diff
-					int preferred_pack)
-		if ((preferred_pack > -1) &&
```

### 58. `compute_sorted_entries` in `midx-write.c`

```diff
-		if (-1 < ctx->preferred_pack_idx && ctx->preferred_pack_idx < start_pack)
+		if (ctx->preferred_pack_idx != NO_PREFERRED_PACK &&
+		    ctx->preferred_pack_idx < start_pack)
```

### 59. `write_midx_bitmap` in `midx-write.c`

```diff
-	int ret, i;
+	int ret;
-	for (i = 0; i < pdata->nr_objects; i++)
+	for (uint32_t i = 0; i < pdata->nr_objects; i++)
-	for (i = 0; i < pdata->nr_objects; i++)
+	for (uint32_t i = 0; i < pdata->nr_objects; i++)
```

### 60. `fill_packs_from_midx` in `midx-write.c`

```diff
+static int fill_packs_from_midx(struct write_midx_context *ctx)
+			if (prepare_midx_pack(ctx->repo, m,
+					      m->num_packs_in_base + i))
+				return error(_("could not load pack"));
+			ALLOC_GROW(ctx->info, ctx->nr + 1, ctx->alloc);
```

### 61. `fill_packs_from_midx` in `midx-write.c`

```diff
-static int fill_packs_from_midx(struct write_midx_context *ctx,
-				const char *preferred_pack_name, uint32_t flags)
-			ALLOC_GROW(ctx->info, ctx->nr + 1, ctx->alloc);
-
-			/*
-			 * If generating a reverse index, need to have
-			 * packed_git's loaded to compare their
-			 * mtimes and object count.
-			 *
-			 * If a preferred pack is specified, need to
-			 * have packed_git's loaded to ensure the chosen
-			 * preferred pack has a non-zero object count.
... truncated 13 additional diff lines ...
```

### 62. `write_midx_internal` in `midx-write.c`

```diff
-	uint32_t i, start_pack;
+	uint32_t start_pack;
-	struct write_midx_context ctx = { 0 };
+	struct write_midx_context ctx = {
+		.preferred_pack_idx = NO_PREFERRED_PACK,
+	 };
-	int result = 0;
+	int result = -1;
-				result = 1;
-	} else if (ctx.m && fill_packs_from_midx(&ctx, preferred_pack_name,
-						 flags) < 0) {
+	} else if (ctx.m && fill_packs_from_midx(&ctx)) {
... truncated 74 additional diff lines ...
```

### 63. `extend_abbrev_len` in `object-name.c`

```diff
+static int extend_abbrev_len(const struct object_id *oid,
+			     struct min_abbrev_data *mad)
```

### 64. `extend_abbrev_len` in `object-name.c`

```diff
-static int extend_abbrev_len(const struct object_id *oid, void *cb_data)
-	struct min_abbrev_data *mad = cb_data;
-
```

### 65. `oid_object_info_extended` in `odb.h`

```diff
-static inline int oid_object_info_extended(struct repository *r,
-					   const struct object_id *oid,
-					   struct object_info *oi,
-					   unsigned flags)
-{
-	return odb_read_object_info_extended(r->objects, oid, oi, flags);
-}
```

### 66. `oid_object_info` in `odb.h`

```diff
-static inline int oid_object_info(struct repository *r,
-				  const struct object_id *oid,
-				  unsigned long *sizep)
-{
-	return odb_read_object_info(r->objects, oid, sizep);
-}
```

### 67. `repo_read_object_file` in `odb.h`

```diff
-static inline void *repo_read_object_file(struct repository *r,
-					  const struct object_id *oid,
-					  enum object_type *type,
-					  unsigned long *size)
-{
-	return odb_read_object(r->objects, oid, type, size);
-}
```

### 68. `has_object` in `odb.h`

```diff
-static inline int has_object(struct repository *r,
-			     const struct object_id *oid,
-			     unsigned flags)
-{
-	return odb_has_object(r->objects, oid, flags);
-}
```

### 69. `add_path_to_list` in `path-walk.c`

```diff
+static void add_path_to_list(struct path_walk_context *ctx,
+			     const char *path,
+			     enum object_type type,
+			     struct object_id *oid,
+			     int interesting)
+{
+	struct type_and_oid_list *list = strmap_get(&ctx->paths_to_lists, path);
+
+	if (!list) {
+		CALLOC_ARRAY(list, 1);
+		list->type = type;
+		strmap_put(&ctx->paths_to_lists, path, list);
... truncated 5 additional diff lines ...
```

### 70. `add_tree_entries` in `path-walk.c`

```diff
-		struct type_and_oid_list *list;
-		if (!(list = strmap_get(&ctx->paths_to_lists, path.buf))) {
-			CALLOC_ARRAY(list, 1);
-			list->type = type;
-			strmap_put(&ctx->paths_to_lists, path.buf, list);
-		}
-		push_to_stack(ctx, path.buf);
-
-		if (!(o->flags & UNINTERESTING))
-			list->maybe_interesting = 1;
+		add_path_to_list(ctx, path.buf, type, &entry.oid,
+				 !(o->flags & UNINTERESTING));
... truncated 2 additional diff lines ...
```

### 71. `setup_pending_objects` in `path-walk.c`

```diff
-				struct type_and_oid_list *list;
-				if (!(list = strmap_get(&ctx->paths_to_lists, path))) {
-					CALLOC_ARRAY(list, 1);
-					list->type = OBJ_TREE;
-					strmap_put(&ctx->paths_to_lists, path, list);
-				}
-				oid_array_append(&list->oids, &obj->oid);
+				add_path_to_list(ctx, path, OBJ_TREE, &obj->oid, 1);
-			if (pending->path) {
-				struct type_and_oid_list *list;
-				char *path = pending->path;
-				if (!(list = strmap_get(&ctx->paths_to_lists, path))) {
... truncated 11 additional diff lines ...
```

### 72. `display` in `progress.c`

```diff
+	int update = !!progress_update;
-	if (progress->delay && (!progress_update || --progress->delay))
+	progress_update = 0;
+
+	if (progress->delay && (!update || --progress->delay))
-		if (percent != progress->last_percent || progress_update) {
+		if (percent != progress->last_percent || update) {
-	} else if (progress_update) {
+	} else if (update) {
-		progress_update = 0;
```

### 73. `get_default_delay` in `progress.c`

```diff
-		delay_in_secs = git_env_ulong("GIT_PROGRESS_DELAY", 2);
+		delay_in_secs = git_env_ulong("GIT_PROGRESS_DELAY", 1);
```

### 74. `ref_transaction_maybe_set_rejected` in `refs.c`

```diff
-		BUG("transaction not inititalized with failure support");
+		BUG("transaction not initialized with failure support");
+	/*
+	 * Rejected refnames shouldn't be considered in the availability
+	 * checks, so remove them from the list.
+	 */
+	string_list_remove(&transaction->refnames,
+			   transaction->updates[update_idx]->refname, 0);
+
```

### 75. `ref_transaction_update_reflog` in `refs.c`

```diff
-static int ref_transaction_update_reflog(struct ref_transaction *transaction,
-					 const char *refname,
-					 const struct object_id *new_oid,
-					 const struct object_id *old_oid,
-					 const char *committer_info,
-					 unsigned int flags,
-					 const char *msg,
-					 uint64_t index,
-					 struct strbuf *err)
-	flags |= REF_LOG_ONLY | REF_FORCE_CREATE_REFLOG | REF_NO_DEREF;
-	/*
-	 * While we do set the old_oid value, we unset the flag to skip
... truncated 3 additional diff lines ...
```

### 76. `ref_transaction_update_reflog` in `refs.c`

```diff
+int ref_transaction_update_reflog(struct ref_transaction *transaction,
+				  const char *refname,
+				  const struct object_id *new_oid,
+				  const struct object_id *old_oid,
+				  const char *committer_info,
+				  const char *msg,
+				  uint64_t index,
+				  struct strbuf *err)
+	unsigned int flags;
+	flags = REF_HAVE_OLD | REF_HAVE_NEW | REF_LOG_ONLY | REF_FORCE_CREATE_REFLOG | REF_NO_DEREF |
+		REF_LOG_USE_PROVIDED_OIDS;
```

### 77. `migrate_one_reflog_entry` in `refs.c`

```diff
+	struct ident_split ident;
+	if (split_ident_line(&ident, committer, strlen(committer)) < 0)
+		return -1;
+
+	strbuf_reset(data->name);
+	strbuf_add(data->name, ident.name_begin, ident.name_end - ident.name_begin);
+	strbuf_reset(data->mail);
+	strbuf_add(data->mail, ident.mail_begin, ident.mail_end - ident.mail_begin);
+
-	/* committer contains name and email */
-	strbuf_addstr(data->sb, fmt_ident("", committer, WANT_BLANK_IDENT, date, 0));
+	strbuf_addstr(data->sb, fmt_ident(data->name->buf, data->mail->buf, WANT_BLANK_IDENT, date, 0));
... truncated 3 additional diff lines ...
```

### 78. `migrate_one_reflog` in `refs.c`

```diff
+		.name = &migration_data->name,
+		.mail = &migration_data->mail,
```

### 79. `repo_migrate_ref_storage_format` in `refs.c`

```diff
+		.name = STRBUF_INIT,
+		.mail = STRBUF_INIT,
+	strbuf_release(&data.name);
+	strbuf_release(&data.mail);
```

### 80. `ref_update_expects_existing_old_ref` in `refs.c`

```diff
+	if (update->flags & REF_LOG_ONLY)
+		return 0;
+
```

## Mock Release-Note Drafts

- No mock release-note output available.

## Ground-Truth Drafting Workspace

| GT ID | Section | Semantic Release-Note Entry | Supporting Evidence | Decision |
| --- | --- | --- | --- | --- |
| GT-001 |  |  |  | pending |

## Excluded Or Low-Level Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
|  |  |  |

## Reviewer Notes

- Record uncertainty, alternative interpretations, and final consensus here.

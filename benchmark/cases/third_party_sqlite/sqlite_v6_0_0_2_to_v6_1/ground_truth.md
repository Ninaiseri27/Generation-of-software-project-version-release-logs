# Ground Truth: third_party_sqlite OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release

Status: `reviewed`

Evidence packet:

- `benchmark/cases/third_party_sqlite/sqlite_v6_0_0_2_to_v6_1/evidence.md`

## Evidence Checklist

- [ ] Inspect OpenHarmony v6.0 platform release notes.
- [ ] Inspect OpenHarmony v6.1 platform release notes if available.
- [x] Inspect `changed_functions.json` for changed-function inventory.
- [x] Run Stage 2/3 artifacts before final admission.
- [x] Inspect commit messages between the two tags.
- [ ] Inspect SQLite upstream changelog if entries can be mapped to the OpenHarmony component diff.

## Evidence Summary

- Pipeline status: `verified_full_pipeline_mock`.
- Changed functions: `42`.
- CMG matched entries: `18`.
- CMG unmatched entries: `24`.
- Fallback-context coverage: `42/42`.
- Current use: medium database case admitted for `core_eval` after excluding low-user-value compatibility and maintenance entries.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Security | Sync SQLite community fixes for integer-overflow and memory-safety issues in core SQL, shell, FTS, RTREE, and session/change-set handling. | Commit messages `fix sqlite community issue of OOB read and infinite loop`, `fix sqlite community issue of an integer overflow`, `fix sqlite community integer overflow issue`, `fix CVE-2025-7709`, `sync sqlite community fts3/fts5 issue`; changed functions `output_hex_blob`, `sqlite3VdbeExec`, `fts3IncrmergeWriter`, `rtreenode`, `sessionChangeHash`, `sessionChangesetBufferTblhdr`, `fts5DlidxLvlNext`, `fts5WriteDlidxAppend`. | This entry groups several upstream/community security and robustness fixes because the version pair contains many small SQLite engine changes. |
| GT-002 | Fix | Improve compressed-VFS corruption and busy-state handling so corrupt compressed database files return appropriate corrupt/busy/I/O errors instead of ambiguous success paths. | Commit messages `Return corrupt/busy through compressvfs`, `Check file before open compress db`, `Fix busy issue`, `Fix unexpected journal file generate while operate compress db`, `codec error return SQLITE_CORRUPT`; changed functions/tests `CompressTest014`, `CompressTest015`; patch changes in `0013-Bugfix-on-current-version.patch`. | Partly patch-file-driven; current function detector captures regression tests but not every patched implementation hunk. |
| GT-003 | Fix | Improve binlog replay reliability by adding rollback-on-failure behavior, skipping temporary databases, supporting batch binlog replay, and covering replay/interface edge cases with tests. | Commit messages `binlog replay add rollback on failure`, `fix binlog failed with single quotes`, `fix binlog not skip temp db`, `fix issus to add batch binlog replay`; changed functions/tests `UtPresetDb`, `BinlogReplayTest002`, `BinlogReplayTest003`, `BinlogInterfaceTest001`, `BinlogInterfaceTest002`; patch files `0006-Support-Binlog.patch` and `0013-Bugfix-on-current-version.patch`. | Developer-facing reliability change; much of the implementation evidence lives in patch files. |
| GT-004 | Fix | Enhance encrypted database rekey behavior and regression coverage across cipher, HMAC, KDF, page-size, WAL, and multiprocess scenarios. | Commit messages `enhance rekey`, `some fix of enhance rekey`, `fix rekey memory errors`, `fix rekey ios lock error`; changed helper/test functions `CreateTable`, `InsertRecords`, `QueryIndexInfo`, `GetRecordCount`, `PrepareDataForDb`, `QueryData`, `EncryptDbConfig`, `LibSQLiteRekeyTest001` through `LibSQLiteRekeyTest015`; patch `0012-enhance-rekey.patch`. | Should be reviewed against patch contents before final admission because many changed symbols are tests. |

## Excluded Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| Pure merge commits | Merge-only history entries do not add independent release-note semantics beyond their squashed child commits. | Commit messages beginning with `merge` or `Merge pull request`. |
| Large unittest helper additions when not tied to a behavior entry | Helper routines are evidence for GT-003/GT-004, not standalone user-facing release-note items. | Added helper functions in `sqlite_binlog_test.cpp` and `sqlite_codec_rekey_test.cpp`. |
| Patch reordering or apply-patch maintenance | Mechanism-level patch maintenance should not be counted as a separate release-note entry unless behavior changes are evident. | Commit `fix apply patch`; patch-file diffs. |
| zstd dependency redirection | Build/runtime dependency compatibility change affects integration environment but is almost invisible to final users and is not represented in `changed_functions.json`; exclude from P/R/F1 while mentioning as compatibility/build note if needed. | Former GT-005; commit message `zstd redirect to libzstd.z.so`. |
| Plugin/data visibility and DFX/logging/debug improvements | Pure maintenance and diagnostics changes for platform integration debugging; not a core developer/user-facing release-note target and would reward noisy generation if counted as ground truth. | Former GT-006; commit messages `add visibility path for plugins/data`, `Enhance dfx issue`, `Optimize log print`, `Add debug for dirsync`, `Fix error code missing`. |

## Reviewer Notes

- Drafted from commit messages, generated function-level evidence, and selected patch-stat inspection.
- This case intentionally exposes a method limitation: important SQLite behavior changes are often stored as `.patch` files, while Stage 1 currently extracts only C/C++ source/test functions.
- Second-pass review keeps GT-001 through GT-004 for core evaluation and excludes the former GT-005/GT-006 from P/R/F1.

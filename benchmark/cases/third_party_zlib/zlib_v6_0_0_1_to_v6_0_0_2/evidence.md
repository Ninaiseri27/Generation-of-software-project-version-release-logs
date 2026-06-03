# Evidence Pack: third_party_zlib OpenHarmony-v6.0.0.1-Release -> OpenHarmony-v6.0.0.2-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `zlib_v6_0_0_1_to_v6_0_0_2`
- Repository: `third_party_zlib`
- Category: `compression`
- Reference version: `OpenHarmony-v6.0.0.1-Release`
- Target version: `OpenHarmony-v6.0.0.2-Release`
- Pipeline status: `verified_full_pipeline_mock`
- Ground-truth status: `reviewed`

## Evidence Sources To Inspect

- [ ] commit_messages
- [ ] function_level_diff
- [ ] CVE or security advisory text if available
- [ ] OpenHarmony release notes if available

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/changed_functions.json`
- cmg_output: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/cmg.json`
- prompt_input: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/prompt_input.json`
- prompt_bundle: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/prompt_bundle.json`
- release_note_mock_none: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/release_note_mock_none.json`
- release_note_mock_exact: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/release_note_mock_exact.json`
- release_note_mock_rule_family: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/release_note_mock_rule_family.json`
- deepseek_v4_flash_baselines: `outputs/benchmark/third_party_zlib/OpenHarmony-v6.0.0.1-Release__OpenHarmony-v6.0.0.2-Release/baselines_deepseek_v4_flash`

## Pipeline Summary

- Commit count: `2`
- Changed C/C++ files: `2`
- Changed functions: `2`
- Patch only: `False`
- CMG matched entries: `2`
- CMG unmatched entries: `0`
- Fallback-context entries: `2`
- Diff-derived call edges: `0`
- Prompt entries: `2`
- Mock generated entries: `2`

## Commit Messages

- !103 merge r6 into OpenHarmony-6.0-Release
- fix cve-2026-27171

## Changed C/C++ Files

- `crc32.c`
- `zlib.h`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `crc32_combine64` | `modified` | `crc32.c` | `1032-1039` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 2 | `crc32_combine_gen64` | `modified` | `crc32.c` | `1047-1054` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `crc32_combine64` in `crc32.c`

```diff
+    if (len2 < 0)
+        return 0;
```

### 2. `crc32_combine_gen64` in `crc32.c`

```diff
+    if (len2 < 0)
+        return 0;
```

## Mock Release-Note Drafts

1. [Internal] Update the crc32_combine64 routine: Updated the crc32_combine64 routine.
2. [Internal] Update the crc32_combine_gen64 routine: Updated the crc32_combine_gen64 routine.

These drafts are generated evidence only. Do not copy them as ground truth without review.

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

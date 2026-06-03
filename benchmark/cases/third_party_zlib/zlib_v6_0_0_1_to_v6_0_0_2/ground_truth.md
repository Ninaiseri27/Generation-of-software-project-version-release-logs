# Ground Truth: third_party_zlib OpenHarmony-v6.0.0.1-Release -> OpenHarmony-v6.0.0.2-Release

Status: `reviewed`

Evidence packet:

- `benchmark/cases/third_party_zlib/zlib_v6_0_0_1_to_v6_0_0_2/evidence.md`

## Evidence Checklist

- [x] Inspect `changed_functions.json` for changed-function inventory.
- [x] Run Stage 2/3 before final admission.
- [x] Inspect commit messages between the two tags.
- [x] Check CVE/security advisory references if available.

## Evidence Summary

- Pipeline status: `verified_full_pipeline_mock`.
- Changed functions: `2`.
- CMG matched entries: `2`.
- CMG unmatched entries: `0`.
- Fallback-context coverage: `2/2`.
- Current use: compact compression/security-fix case admitted for `core_eval`.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Bug Fixes | Fix negative-length handling in zlib CRC32 combination APIs by returning zero when `len2` is negative, preventing invalid CRC combination behavior for `crc32_combine64` and `crc32_combine_gen64`. | Commit `fix cve-2026-27171`; changed functions `crc32_combine64`, `crc32_combine_gen64`; diff adds `if (len2 < 0) return 0;` guards and updates `zlib.h` API comments to document the zero return behavior. | Treated as one release-note-level fix because both function changes implement the same externally visible behavior. |

## Excluded Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| `zlib.h` comment wording as a separate entry | Documentation update is part of the same CRC32 negative-length behavior fix, not an independent release-note item. | Diff updates comments for `crc32_combine()` and `crc32_combine_gen()` to mention zero return on negative length. |

## Reviewer Notes

- Drafted from local commit messages, function-level diff evidence, and CMG artifacts.
- The case is small, so it mainly improves repository/category coverage rather than providing strong statistical power by itself.

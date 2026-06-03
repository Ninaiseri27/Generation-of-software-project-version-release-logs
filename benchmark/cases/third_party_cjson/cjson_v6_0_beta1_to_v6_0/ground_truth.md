# Ground Truth: third_party_cJSON OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release

Status: `reviewed`

Evidence packet:

- `benchmark/cases/third_party_cjson/cjson_v6_0_beta1_to_v6_0/evidence.md`

## Evidence Checklist

- [x] Inspect `changed_functions.json` for changed-function inventory.
- [x] Run Stage 2/3 smoke artifacts before final admission.
- [x] Inspect commit messages between the two tags.
- [x] Inspect implementation and test diffs.
- [x] Check upstream cJSON issue/changelog references if available.
- [x] Decide whether BUILD.gn tag change is release-note-worthy for this study.

## Evidence Summary

- Pipeline status: `verified_full_pipeline_mock`.
- Changed functions: `11`.
- CMG matched entries: `11`.
- CMG unmatched entries: `0`.
- Current use: fifth-repository case admitted for `core_eval`.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Reliability | Prevent stack exhaustion when duplicating circular or overly deep cJSON structures by adding recursion-depth protection to `cJSON_Duplicate`. | Commit `Added max recusrion depth for cJSONDuplicate to prevent stack exhaustion in case of circular reference`; changed functions `cJSON_Duplicate`, `cJSON_Duplicate_rec`; diff adds `CJSON_CIRCULAR_LIMIT`, wraps duplication through `cJSON_Duplicate_rec`, stops recursion at the configured limit, and adds `cjson_should_not_follow_too_deep_circular_references`. | Runtime behavior fix with explicit robustness/security relevance. |
| GT-002 | Testing | Add parser regression coverage for incomplete exact-size JSON buffers and large-number parsing cases to guard against heap-buffer-overflow and number-parsing regressions. | Changed tests `test15_should_not_heap_buffer_overflow`, `cjson_parse_big_numbers_should_not_report_error`, and `parse_number_should_parse_big_numbers`; diff exercises `cJSON_ParseWithLength` on non-null-terminated buffers and separates valid/invalid large-number parsing checks. | Kept as a testing/reliability entry because it targets parser robustness regressions, not just test renaming. |

## Excluded Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| BUILD.gn `innerapi_tags` update | Build metadata only unless the evaluation target includes platform packaging visibility. | Diff changes `chipsetsdk` to `chipsetsdk_sp`. |
| Test renaming from `a` to `parse_number_should_parse_big_numbers` as a standalone item | Name cleanup alone is not release-note-level behavior. | `tests/parse_number.c` rename. |
| Removing a duplicate null-termination assignment in `parse_number` as a standalone item | The diff is low-level cleanup and is only release-note-worthy as supporting evidence for parser robustness tests. | `cJSON.c` removes `number_c_string[i] = '\0';` after the buffer is already terminated by length. |

## Reviewer Notes

- This case expands repository diversity with a direct-source JSON parser update.
- Reviewed GT intentionally groups function-level and test-level evidence into two release-note-level entries to avoid over-counting low-level test helpers.

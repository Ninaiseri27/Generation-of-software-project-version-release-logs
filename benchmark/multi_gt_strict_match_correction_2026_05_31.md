# Multi-GT Strict-Match Correction (2026-05-31)

This record documents a targeted strict semantic audit of generated entries matched to multiple GT items. The correction removes secondary matches where a generated note mentions a nearby implementation detail but does not state the release-note-level behavior of the GT entry.

## Summary

- Planned removals: 21
- Removed in this run: 16
- Already absent from prior curl correction: 5
- Missing files: 0

## Removed Or Confirmed-Absent Matches

| Status | Case | Method | Generated | GT | Reason |
| --- | --- | --- | --- | --- | --- |
| `already_absent` | `curl_8_14_0_to_8_14_1` | `full_evidence_similarity_family` | `GEN-025` | `GT-C003` | no-buffer/NOPROGRESS setup-order note does not state upload-from-dot behavior. |
| `already_absent` | `curl_8_14_0_to_8_14_1` | `full_similarity_family` | `GEN-019` | `GT-C003` | no-buffer/NOPROGRESS setup-order note does not state upload-from-dot behavior. |
| `already_absent` | `curl_8_14_0_to_8_14_1` | `full_strict_1hop` | `GEN-062` | `GT-C003` | no-buffer/NOPROGRESS setup-order note does not state upload-from-dot behavior. |
| `already_absent` | `curl_v6_0_to_v6_0_0_1` | `full_evidence_similarity_family` | `GEN-007` | `GT-003` | backend-only TLCP/OpenHiTLS generated note does not state CLI/API encrypted cert/key option exposure. |
| `already_absent` | `curl_v6_0_to_v6_0_0_1` | `full_similarity_family` | `GEN-013` | `GT-003` | backend-only TLCP/OpenHiTLS generated note does not state CLI/API encrypted cert/key option exposure. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_evidence_similarity_family` | `GEN-027` | `GT-G009` | stash colored-output fix does not state diff --name-only ignore-options behavior. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_evidence_similarity_family` | `GEN-027` | `GT-G014` | stash colored-output fix does not state interactive add/patch color-config behavior. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_similarity_family` | `GEN-024` | `GT-G009` | stash colored-output fix does not state diff --name-only ignore-options behavior. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_similarity_family` | `GEN-024` | `GT-G014` | stash colored-output fix does not state interactive add/patch color-config behavior. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_similarity_family` | `GEN-071` | `GT-G012` | unused-function cleanup does not state MIDX crash behavior. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_similarity_family` | `GEN-071` | `GT-G014` | unused-function cleanup does not state interactive add/patch color-config behavior. |
| `removed` | `git_2_51_0_to_2_51_1` | `full_strict_1hop` | `GEN-023` | `GT-G009` | generated note can support interactive color behavior but not diff --name-only ignore-options behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_evidence_similarity_family` | `GEN-004` | `GT-S01` | parser/syntax note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_evidence_similarity_family` | `GEN-008` | `GT-S01` | scan-substring/extended-class note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_evidence_similarity_family` | `GEN-009` | `GT-S01` | Unicode/case/escape note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_similarity_family` | `GEN-003` | `GT-S01` | parser/syntax note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_similarity_family` | `GEN-008` | `GT-S01` | scan-substring/extended-class note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_similarity_family` | `GEN-009` | `GT-S01` | Unicode/case/escape note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_strict_1hop` | `GEN-010` | `GT-S01` | syntax/scan-substring note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_strict_1hop` | `GEN-011` | `GT-S01` | Unicode/case/escape note does not state CVE-2025-58050 read-past-end behavior. |
| `removed` | `pcre2_v6_0_0_2_to_v6_1` | `full_strict_1hop` | `GEN-013` | `GT-S01` | substitution/Unicode note does not state CVE-2025-58050 read-past-end behavior. |

## Review Standard

- A generated entry can match multiple GT entries only when it explicitly states each GT-level user/developer-visible behavior.
- Function, helper, syntax-parser, or setup-order proximity is not sufficient by itself.
- CVE/security GTs require the generated entry to state the actual security behavior, not only a related parser or helper change.

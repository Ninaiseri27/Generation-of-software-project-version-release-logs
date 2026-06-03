# Final Strict Match Audit

Last updated: 2026-05-31

This report flags strict-match rows that are most likely to affect thesis credibility before copying final metrics into the paper. A flag is not automatically an error; it marks rows that need semantic review.

## Summary

- case_variant_rows: `88`
- gt_count: `82`
- finding_count: `1099`
- high_severity_count: `7`
- review_severity_count: `1092`
- audited_case_count: `11`
- audited_method_count: `8`

## Main Interpretation

- The audit is intentionally conservative: security/CVE rows, helper/refactor-like generated notes, multi-GT matches, high-redundancy GT rows, and sampled Git 2.53 rows are flagged for review.
- The 2026-05-29 refresh downgraded over-broad mbedTLS hostname-security matches that did not explicitly state the release-note-level certificate-verification behavior.
- The 2026-05-31 cJSON review removed test-only matches to the runtime `cJSON_Duplicate` GT and one excluded `parse_number` cleanup match. The correction record is `benchmark/cjson_strict_match_correction_2026_05_31.md`.
- The 2026-05-31 curl review removed helper/test/refactor-only matches, fixed one wrong CVE attribution, and moved backend-only TLCP/OpenHiTLS matches to the backend-support GT. The correction record is `benchmark/curl_strict_match_correction_2026_05_31.md`.
- The 2026-05-31 mbedTLS high-severity review retained all seven flagged rows because they state the same hostname-verification or X.509/ASN.1 memory-safety facts as the reviewed GT entries. The review record is `benchmark/mbedtls_high_severity_review_2026_05_31.md`.
- The 2026-05-31 multi-GT review removed over-broad secondary matches where a generated note mentioned nearby implementation details but did not explicitly state the second GT-level behavior. The correction record is `benchmark/multi_gt_strict_match_correction_2026_05_31.md`.
- The high-severity rows remain listed by the conservative flagger, but the current manual decision is to keep the mbedTLS rows unless new contrary evidence appears.

## Case-Level Flag Counts

| Case | Flag Counts |
| --- | --- |
| `cjson_v6_0_beta1_to_v6_0` | helper_refactor_like_generated_note=36, security_cve_sensitive=15 |
| `curl_8_11_0_to_8_11_1` | helper_refactor_like_generated_note=45, high_redundancy_gt=5, security_cve_sensitive=25 |
| `curl_8_14_0_to_8_14_1` | helper_refactor_like_generated_note=60, high_redundancy_gt=6, multi_gt_generated_match=3, security_cve_sensitive=7 |
| `curl_v6_0_beta1_to_v6_0` | high_redundancy_gt=6, multi_gt_generated_match=6, security_cve_sensitive=3 |
| `curl_v6_0_to_v6_0_0_1` | helper_refactor_like_generated_note=26, high_redundancy_gt=11, multi_gt_generated_match=2, security_cve_sensitive=72 |
| `git_2_51_0_to_2_51_1` | helper_refactor_like_generated_note=102, high_redundancy_gt=15, multi_gt_generated_match=4, security_cve_sensitive=20 |
| `git_2_52_0_to_2_53_0` | helper_refactor_like_generated_note=85, high_redundancy_gt=16, sampled_git_2_53_scope=371, security_cve_sensitive=32 |
| `mbedtls_v6_0_beta1_to_v6_0` | helper_like_match_to_security_gt=7, helper_refactor_like_generated_note=12, high_redundancy_gt=4, multi_gt_generated_match=1, security_cve_sensitive=67 |
| `pcre2_v6_0_0_2_to_v6_1` | helper_refactor_like_generated_note=9, high_redundancy_gt=2, multi_gt_generated_match=15, security_cve_sensitive=2 |
| `sqlite_v6_0_0_2_to_v6_1` | helper_refactor_like_generated_note=115, high_redundancy_gt=12, security_cve_sensitive=53 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | security_cve_sensitive=6 |

## Method-Level Flag Counts

| Method | Flag Counts |
| --- | --- |
| `diff_only` | helper_like_match_to_security_gt=1, helper_refactor_like_generated_note=73, high_redundancy_gt=13, multi_gt_generated_match=3, sampled_git_2_53_scope=58, security_cve_sensitive=53 |
| `full_adaptive_rule_family` | helper_like_match_to_security_gt=3, helper_refactor_like_generated_note=74, high_redundancy_gt=11, multi_gt_generated_match=3, sampled_git_2_53_scope=55, security_cve_sensitive=40 |
| `full_evidence_similarity_family` | helper_refactor_like_generated_note=62, high_redundancy_gt=9, multi_gt_generated_match=7, sampled_git_2_53_scope=50, security_cve_sensitive=37 |
| `full_no_fallback` | helper_like_match_to_security_gt=1, helper_refactor_like_generated_note=70, high_redundancy_gt=13, multi_gt_generated_match=3, sampled_git_2_53_scope=55, security_cve_sensitive=43 |
| `full_similarity_family` | helper_refactor_like_generated_note=57, high_redundancy_gt=6, multi_gt_generated_match=8, sampled_git_2_53_scope=44, security_cve_sensitive=35 |
| `full_strict_1hop` | helper_like_match_to_security_gt=1, helper_refactor_like_generated_note=80, high_redundancy_gt=12, multi_gt_generated_match=6, sampled_git_2_53_scope=55, security_cve_sensitive=45 |
| `no_graph` | helper_like_match_to_security_gt=1, helper_refactor_like_generated_note=73, high_redundancy_gt=13, multi_gt_generated_match=1, sampled_git_2_53_scope=54, security_cve_sensitive=45 |
| `text_only` | helper_refactor_like_generated_note=1, security_cve_sensitive=4 |

## High-Severity Findings

| Case | Method | Generated | GT | Risk | Generated Title |
| --- | --- | --- | --- | --- | --- |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-010` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory leak and use-after-free in cert_req SAN directory name handling |
| `mbedtls_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-004` | `GT-001` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix certificate verification without hostname for client |
| `mbedtls_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-014` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management for directory name SAN entries in certificate writing |
| `mbedtls_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-015` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management in cert_req.c for directory name SANs |
| `mbedtls_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-016` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management in cert_req directory name handling |
| `mbedtls_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-011` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory leak and use-after-free in cert_write SAN directory name handling |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | `GEN-017` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management in certificate request SAN directory name handling |

## Review Queue

The full JSON contains every flagged row. The Markdown table below lists the first 80 review findings after high-severity rows.

| Severity | Case | Method | Generated | GT | Risk | Title |
| --- | --- | --- | --- | --- | --- | --- |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-010` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory leak and use-after-free in cert_req SAN directory name handling |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-004` | `GT-001` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix certificate verification without hostname for client |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-014` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management for directory name SAN entries in certificate writing |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-015` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management in cert_req.c for directory name SANs |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-016` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management in cert_req directory name handling |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-011` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory leak and use-after-free in cert_write SAN directory name handling |
| `high` | `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | `GEN-017` | `GT-002` | `helper_like_match_to_security_gt,helper_refactor_like_generated_note,security_cve_sensitive` | Fix memory management in certificate request SAN directory name handling |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-002` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix heap buffer overflow in cJSON_ParseWithLength |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-003` | `GT-001` | `helper_refactor_like_generated_note` | Prevent infinite recursion when duplicating deeply nested circular references |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-006` | `GT-001` | `helper_refactor_like_generated_note` | Add test for deep circular references |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-007` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for heap buffer overflow prevention |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-008` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `GEN-009` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers without error |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-001` | `GT-001` | `helper_refactor_like_generated_note` | Add test for circular reference depth limit in cJSONDuplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-002` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for heap buffer overflow in cJSON |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-003` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix heap buffer overflow in cJSON_ParseWithLength for truncated JSON strings |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-005` | `GT-001` | `security_cve_sensitive` | Fix stack exhaustion in cJSON_Duplicate due to circular references |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-007` | `GT-001` | `helper_refactor_like_generated_note` | Prevent stack exhaustion when duplicating deeply nested circular references |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-010` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_adaptive_rule_family` | `GEN-011` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers without error |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-001` | `GT-001` | `helper_refactor_like_generated_note` | Add test for circular reference depth limit in cJSONDuplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-002` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for heap buffer overflow in cJSON |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-003` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix heap buffer overflow in cJSON_ParseWithLength for truncated JSON strings |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-005` | `GT-001` | `security_cve_sensitive` | Fix stack exhaustion in cJSON_Duplicate due to circular references |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-006` | `GT-001` | `helper_refactor_like_generated_note` | Prevent stack exhaustion when duplicating deeply nested circular references |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-008` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_evidence_similarity_family` | `GEN-009` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers without error |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-002` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix heap buffer overflow in cJSON_ParseWithLength |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-003` | `GT-001` | `helper_refactor_like_generated_note` | Prevent stack exhaustion from circular references in cJSON_Duplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-008` | `GT-001` | `helper_refactor_like_generated_note` | Add test for circular reference depth limit in cJSONDuplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-009` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for heap buffer overflow prevention |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-010` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_no_fallback` | `GEN-011` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers without error |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_similarity_family` | `GEN-001` | `GT-001` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for circular reference depth limit in cJSONDuplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_similarity_family` | `GEN-002` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for heap buffer overflow in cJSON |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_similarity_family` | `GEN-005` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_similarity_family` | `GEN-006` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers without error |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-001` | `GT-001` | `helper_refactor_like_generated_note` | Add test for circular reference depth limit in cJSONDuplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-002` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Add test for heap buffer overflow in cJSON |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-003` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix heap buffer overflow in cJSON_ParseWithLength |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-005` | `GT-001` | `helper_refactor_like_generated_note` | Fix stack exhaustion from circular references in cJSON_Duplicate |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-010` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `full_strict_1hop` | `GEN-011` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers without error |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `no_graph` | `GEN-001` | `GT-002` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix heap buffer overflow in cJSON_ParseWithLength |
| `review` | `cjson_v6_0_beta1_to_v6_0` | `no_graph` | `GEN-010` | `GT-002` | `helper_refactor_like_generated_note` | Add test for parsing big numbers |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `` | `GT-U003` | `high_redundancy_gt` |  |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-019` | `GT-U016` | `helper_refactor_like_generated_note` | Added validation and compatibility handling for --range option |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-022` | `GT-U012` | `helper_refactor_like_generated_note` | Fix SFTP state and AIO cleanup for libssh > 0.11.0 |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-025` | `GT-U008` | `security_cve_sensitive` | Fix SSL certificate error message handling and AWS-LC compatibility |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-029` | `GT-U013` | `security_cve_sensitive` | Fix cnonce buffer size and encoding in digest authentication |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-038` | `GT-U006` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix integer overflow in precision and width parsing |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-046` | `GT-U015` | `helper_refactor_like_generated_note` | Fix memory leak in MIME reader close |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-068` | `GT-U002` | `helper_refactor_like_generated_note` | Fixed memory management in netrc parsing |
| `review` | `curl_8_11_0_to_8_11_1` | `diff_only` | `GEN-073` | `GT-U002` | `security_cve_sensitive` | Prevent control code injection from .netrc credentials |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `` | `GT-U003` | `high_redundancy_gt` |  |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `GEN-002` | `GT-U003` | `helper_refactor_like_generated_note` | Add Curl_nghttp2_free wrapper for nghttp2 memory deallocation |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `GEN-003` | `GT-U003` | `helper_refactor_like_generated_note` | Add Curl_nghttp2_malloc wrapper for nghttp2 memory allocation |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `GEN-025` | `GT-U012` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix SFTP state cleanup for libssh > 0.11.0 |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `GEN-028` | `GT-U008` | `security_cve_sensitive` | Fix SSL certificate error reporting and AWS-LC compatibility |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `GEN-047` | `GT-U015` | `helper_refactor_like_generated_note` | Fix memory leak in MIME reader cleanup |
| `review` | `curl_8_11_0_to_8_11_1` | `full_adaptive_rule_family` | `GEN-067` | `GT-U006` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fixed integer overflow checks in mprintf |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-002` | `GT-U003` | `helper_refactor_like_generated_note` | Add Curl_nghttp2_free wrapper for nghttp2 memory deallocation |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-003` | `GT-U003` | `helper_refactor_like_generated_note` | Add Curl_nghttp2_malloc wrapper for nghttp2 memory allocation |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-024` | `GT-U012` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix SFTP state cleanup for libssh > 0.11.0 |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-027` | `GT-U008` | `security_cve_sensitive` | Fix SSL certificate error reporting and AWS-LC compatibility |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-044` | `GT-U015` | `helper_refactor_like_generated_note` | Fix memory leak in MIME reader cleanup |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-064` | `GT-U006` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fixed integer overflow checks in mprintf |
| `review` | `curl_8_11_0_to_8_11_1` | `full_evidence_similarity_family` | `GEN-090` | `GT-U016` | `helper_refactor_like_generated_note` | Refactor option parsing into dedicated functions |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `` | `GT-U003` | `high_redundancy_gt` |  |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-004` | `GT-U003` | `helper_refactor_like_generated_note` | Add nghttp2 memory allocation wrapper |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-006` | `GT-U003` | `helper_refactor_like_generated_note` | Added nghttp2 memory allocation wrapper |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-007` | `GT-U003` | `helper_refactor_like_generated_note` | Added nghttp2 memory deallocation helper |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-008` | `GT-U003` | `helper_refactor_like_generated_note` | Added nghttp2 memory reallocation wrapper |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-021` | `GT-U012` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fix SFTP non-blocking state and async I/O cleanup for libssh >= 0.11.1 |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-023` | `GT-U008` | `security_cve_sensitive` | Fix SSL certificate error message handling in OpenSSL step2 |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-056` | `GT-U006` | `helper_refactor_like_generated_note,security_cve_sensitive` | Fixed integer overflow checks in mprintf |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-059` | `GT-U015` | `helper_refactor_like_generated_note` | Fixed memory leak in MIME reader cleanup |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-073` | `GT-U016` | `helper_refactor_like_generated_note` | Improved --range option validation and compatibility |
| `review` | `curl_8_11_0_to_8_11_1` | `full_no_fallback` | `GEN-076` | `GT-U016` | `helper_refactor_like_generated_note` | Refactor option parsing into dedicated functions |
| `review` | `curl_8_11_0_to_8_11_1` | `full_similarity_family` | `GEN-002` | `GT-U003` | `helper_refactor_like_generated_note` | Add Curl_nghttp2_free wrapper for nghttp2 memory deallocation |

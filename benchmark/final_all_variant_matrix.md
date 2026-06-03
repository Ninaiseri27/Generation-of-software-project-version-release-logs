# Final All-Variant Matrix

Last updated: 2026-05-31

This matrix summarizes the selected 82-GT benchmark after all 11 cases were run through all 8 required method variants and strict matches were completed. The 2026-05-31 refresh tightens cJSON, curl, mbedTLS high-severity review records, and broad multi-GT strict matches under the final semantic audit.

## Macro/Micro Summary

| Method | Cases | GT | Generated | Macro F1 | Micro F1 | Micro P | Micro R | Unsupported | Matches/GT | Extra/GT | Avg Final Notes | Failed |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 11 | 82 | 11 | 0.2909 | 0.1505 | 0.6364 | 0.0854 | 0.3636 | 0.0854 | 0.0000 | 1.0000 | 0 |
| `diff_only` | 11 | 82 | 612 | 0.6543 | 0.5677 | 0.4069 | 0.9390 | 0.5931 | 3.0732 | 2.1341 | 55.6364 | 0 |
| `no_graph` | 11 | 82 | 605 | 0.6397 | 0.5495 | 0.3950 | 0.9024 | 0.6050 | 2.9268 | 2.0244 | 55.0000 | 0 |
| `full_adaptive_rule_family` | 11 | 82 | 609 | 0.6419 | 0.5503 | 0.3892 | 0.9390 | 0.6108 | 2.9268 | 1.9878 | 55.3636 | 0 |
| `full_no_fallback` | 11 | 82 | 615 | 0.6228 | 0.5239 | 0.3691 | 0.9024 | 0.6309 | 2.8049 | 1.9024 | 55.9091 | 0 |
| `full_strict_1hop` | 11 | 82 | 607 | 0.6616 | 0.5585 | 0.4020 | 0.9146 | 0.5980 | 2.9878 | 2.0732 | 55.1818 | 0 |
| `full_similarity_family` | 11 | 82 | 415 | 0.7020 | 0.6046 | 0.4458 | 0.9390 | 0.5542 | 2.2683 | 1.3293 | 37.7273 | 0 |
| `full_evidence_similarity_family` | 11 | 82 | 532 | 0.6532 | 0.5555 | 0.3966 | 0.9268 | 0.6034 | 2.5854 | 1.6585 | 48.3636 | 0 |

## Per-Case Rows

| Case | Scope | Method | GT | Generated | P | R | F1 | Unsupported | Matches/GT | Extra/GT | Final Notes |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `core` | `text_only` | 4 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `diff_only` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `no_graph` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `full_adaptive_rule_family` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `full_no_fallback` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `full_strict_1hop` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `full_similarity_family` | 4 | 5 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.2500 | 0.2500 | 5 |
| `curl_v6_0_beta1_to_v6_0` | `core` | `full_evidence_similarity_family` | 4 | 11 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.0000 | 2.0000 | 11 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `text_only` | 4 | 1 | 1.0000 | 0.2500 | 0.4000 | 0.0000 | 0.2500 | 0.0000 | 1 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `diff_only` | 4 | 37 | 0.7297 | 1.0000 | 0.8437 | 0.2703 | 6.7500 | 5.7500 | 37 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `no_graph` | 4 | 36 | 0.7500 | 1.0000 | 0.8571 | 0.2500 | 6.7500 | 5.7500 | 36 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `full_adaptive_rule_family` | 4 | 34 | 0.7647 | 1.0000 | 0.8667 | 0.2353 | 6.5000 | 5.5000 | 34 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `full_no_fallback` | 4 | 38 | 0.7368 | 1.0000 | 0.8485 | 0.2632 | 7.0000 | 6.0000 | 38 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `full_strict_1hop` | 4 | 35 | 0.8000 | 1.0000 | 0.8889 | 0.2000 | 7.0000 | 6.0000 | 35 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `full_similarity_family` | 4 | 25 | 0.6400 | 1.0000 | 0.7805 | 0.3600 | 4.0000 | 3.0000 | 25 |
| `sqlite_v6_0_0_2_to_v6_1` | `core` | `full_evidence_similarity_family` | 4 | 30 | 0.6000 | 1.0000 | 0.7500 | 0.4000 | 4.5000 | 3.5000 | 30 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `text_only` | 6 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `diff_only` | 6 | 23 | 0.6522 | 1.0000 | 0.7895 | 0.3478 | 2.5000 | 1.5000 | 23 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `no_graph` | 6 | 22 | 0.4091 | 0.6667 | 0.5070 | 0.5909 | 1.5000 | 0.8333 | 22 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `full_adaptive_rule_family` | 6 | 22 | 0.5000 | 0.8333 | 0.6250 | 0.5000 | 1.8333 | 1.0000 | 22 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `full_no_fallback` | 6 | 22 | 0.3636 | 0.6667 | 0.4706 | 0.6364 | 1.3333 | 0.6667 | 22 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `full_strict_1hop` | 6 | 22 | 0.5455 | 0.6667 | 0.6000 | 0.4545 | 2.0000 | 1.3333 | 22 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `full_similarity_family` | 6 | 14 | 0.5714 | 1.0000 | 0.7273 | 0.4286 | 1.5000 | 0.5000 | 14 |
| `mbedtls_v6_0_beta1_to_v6_0` | `core` | `full_evidence_similarity_family` | 6 | 19 | 0.5263 | 0.8333 | 0.6452 | 0.4737 | 1.6667 | 0.8333 | 19 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `text_only` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `diff_only` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `no_graph` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `full_adaptive_rule_family` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `full_no_fallback` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `full_strict_1hop` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `full_similarity_family` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core` | `full_evidence_similarity_family` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `text_only` | 2 | 1 | 1.0000 | 0.5000 | 0.6667 | 0.0000 | 0.5000 | 0.0000 | 1 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `diff_only` | 2 | 11 | 0.4545 | 1.0000 | 0.6250 | 0.5455 | 2.5000 | 1.5000 | 11 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `no_graph` | 2 | 10 | 0.6000 | 1.0000 | 0.7500 | 0.4000 | 3.0000 | 2.0000 | 10 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `full_adaptive_rule_family` | 2 | 11 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 11 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `full_no_fallback` | 2 | 11 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 11 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `full_strict_1hop` | 2 | 11 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 11 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `full_similarity_family` | 2 | 7 | 0.5714 | 1.0000 | 0.7273 | 0.4286 | 2.0000 | 1.0000 | 7 |
| `cjson_v6_0_beta1_to_v6_0` | `core` | `full_evidence_similarity_family` | 2 | 10 | 0.5000 | 1.0000 | 0.6667 | 0.5000 | 2.5000 | 1.5000 | 10 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `text_only` | 3 | 1 | 1.0000 | 0.3333 | 0.5000 | 0.0000 | 0.3333 | 0.0000 | 1 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `diff_only` | 3 | 47 | 0.6596 | 0.6667 | 0.6631 | 0.3404 | 10.3333 | 9.6667 | 47 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `no_graph` | 3 | 45 | 0.6222 | 0.6667 | 0.6437 | 0.3778 | 9.3333 | 8.6667 | 45 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `full_adaptive_rule_family` | 3 | 47 | 0.4681 | 0.6667 | 0.5500 | 0.5319 | 7.3333 | 6.6667 | 47 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `full_no_fallback` | 3 | 46 | 0.5000 | 1.0000 | 0.6667 | 0.5000 | 7.6667 | 6.6667 | 46 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `full_strict_1hop` | 3 | 45 | 0.5333 | 1.0000 | 0.6957 | 0.4667 | 8.0000 | 7.0000 | 45 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `full_similarity_family` | 3 | 25 | 0.6800 | 1.0000 | 0.8095 | 0.3200 | 5.6667 | 4.6667 | 25 |
| `curl_v6_0_to_v6_0_0_1` | `openharmony_extension` | `full_evidence_similarity_family` | 3 | 37 | 0.5405 | 1.0000 | 0.7018 | 0.4595 | 6.6667 | 5.6667 | 37 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `text_only` | 5 | 1 | 1.0000 | 0.2000 | 0.3333 | 0.0000 | 0.2000 | 0.0000 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `diff_only` | 5 | 78 | 0.0513 | 0.8000 | 0.0964 | 0.9487 | 1.2000 | 0.4000 | 78 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `no_graph` | 5 | 79 | 0.0633 | 0.6000 | 0.1145 | 0.9367 | 1.0000 | 0.4000 | 79 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `full_adaptive_rule_family` | 5 | 79 | 0.0759 | 1.0000 | 0.1412 | 0.9241 | 1.6000 | 0.6000 | 79 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `full_no_fallback` | 5 | 79 | 0.0633 | 0.8000 | 0.1173 | 0.9367 | 1.4000 | 0.6000 | 79 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `full_strict_1hop` | 5 | 80 | 0.1875 | 0.8000 | 0.3038 | 0.8125 | 3.0000 | 2.2000 | 80 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `full_similarity_family` | 5 | 46 | 0.2609 | 0.8000 | 0.3934 | 0.7391 | 2.4000 | 1.6000 | 46 |
| `pcre2_v6_0_0_2_to_v6_1` | `sampled_stress` | `full_evidence_similarity_family` | 5 | 54 | 0.2037 | 0.8000 | 0.3247 | 0.7963 | 2.2000 | 1.4000 | 54 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `text_only` | 16 | 1 | 1.0000 | 0.0625 | 0.1176 | 0.0000 | 0.0625 | 0.0000 | 1 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `diff_only` | 16 | 99 | 0.2626 | 0.9375 | 0.4103 | 0.7374 | 1.6250 | 0.6875 | 99 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `no_graph` | 16 | 102 | 0.2451 | 0.9375 | 0.3886 | 0.7549 | 1.5625 | 0.6250 | 102 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `full_adaptive_rule_family` | 16 | 101 | 0.2574 | 0.9375 | 0.4039 | 0.7426 | 1.6250 | 0.6875 | 101 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `full_no_fallback` | 16 | 103 | 0.2427 | 0.8750 | 0.3800 | 0.7573 | 1.5625 | 0.6875 | 103 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `full_strict_1hop` | 16 | 101 | 0.2574 | 0.9375 | 0.4039 | 0.7426 | 1.6250 | 0.6875 | 101 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `full_similarity_family` | 16 | 82 | 0.2805 | 0.8750 | 0.4248 | 0.7195 | 1.4375 | 0.5625 | 82 |
| `curl_8_11_0_to_8_11_1` | `upstream_extension` | `full_evidence_similarity_family` | 16 | 96 | 0.2500 | 0.8750 | 0.3889 | 0.7500 | 1.5000 | 0.6250 | 96 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `text_only` | 10 | 1 | 1.0000 | 0.1000 | 0.1818 | 0.0000 | 0.1000 | 0.0000 | 1 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `diff_only` | 10 | 121 | 0.1901 | 0.8000 | 0.3072 | 0.8099 | 2.3000 | 1.5000 | 121 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `no_graph` | 10 | 118 | 0.2034 | 0.8000 | 0.3243 | 0.7966 | 2.4000 | 1.6000 | 118 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `full_adaptive_rule_family` | 10 | 119 | 0.2017 | 0.8000 | 0.3221 | 0.7983 | 2.4000 | 1.6000 | 119 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `full_no_fallback` | 10 | 120 | 0.1333 | 0.8000 | 0.2286 | 0.8667 | 1.6000 | 0.8000 | 120 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `full_strict_1hop` | 10 | 119 | 0.1345 | 0.8000 | 0.2302 | 0.8655 | 1.6000 | 0.8000 | 119 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `full_similarity_family` | 10 | 77 | 0.1688 | 0.8000 | 0.2788 | 0.8312 | 1.3000 | 0.5000 | 77 |
| `curl_8_14_0_to_8_14_1` | `upstream_extension` | `full_evidence_similarity_family` | 10 | 106 | 0.1509 | 0.8000 | 0.2540 | 0.8491 | 1.6000 | 0.8000 | 106 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `text_only` | 16 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `diff_only` | 16 | 102 | 0.4510 | 1.0000 | 0.6216 | 0.5490 | 2.8750 | 1.8750 | 102 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `no_graph` | 16 | 100 | 0.4700 | 1.0000 | 0.6395 | 0.5300 | 2.9375 | 1.9375 | 100 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `full_adaptive_rule_family` | 16 | 102 | 0.4608 | 1.0000 | 0.6309 | 0.5392 | 2.9375 | 1.9375 | 102 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `full_no_fallback` | 16 | 102 | 0.4608 | 0.9375 | 0.6179 | 0.5392 | 2.9375 | 2.0000 | 102 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `full_strict_1hop` | 16 | 100 | 0.4800 | 0.9375 | 0.6349 | 0.5200 | 3.0000 | 2.0625 | 100 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `full_similarity_family` | 16 | 75 | 0.5600 | 1.0000 | 0.7179 | 0.4400 | 2.6250 | 1.6250 | 75 |
| `git_2_51_0_to_2_51_1` | `upstream_extension` | `full_evidence_similarity_family` | 16 | 94 | 0.4787 | 1.0000 | 0.6475 | 0.5213 | 2.8125 | 1.8125 | 94 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `text_only` | 15 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `diff_only` | 15 | 80 | 0.7250 | 1.0000 | 0.8406 | 0.2750 | 3.8667 | 2.8667 | 80 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `no_graph` | 15 | 79 | 0.6835 | 1.0000 | 0.8120 | 0.3165 | 3.6000 | 2.6000 | 79 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `full_adaptive_rule_family` | 15 | 80 | 0.6875 | 1.0000 | 0.8148 | 0.3125 | 3.6667 | 2.6667 | 80 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `full_no_fallback` | 15 | 80 | 0.6875 | 1.0000 | 0.8148 | 0.3125 | 3.6667 | 2.6667 | 80 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `full_strict_1hop` | 15 | 80 | 0.6875 | 1.0000 | 0.8148 | 0.3125 | 3.6667 | 2.6667 | 80 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `full_similarity_family` | 15 | 58 | 0.7586 | 1.0000 | 0.8627 | 0.2414 | 2.9333 | 1.9333 | 58 |
| `git_2_52_0_to_2_53_0` | `sampled_upstream_extension` | `full_evidence_similarity_family` | 15 | 74 | 0.6757 | 1.0000 | 0.8065 | 0.3243 | 3.3333 | 2.3333 | 74 |

## Notes

- `Generated` and `Final Notes` count report-facing aggregated notes in each method output.
- `Matches/GT` is valid strict matches divided by GT count; `Extra/GT` subtracts first coverage matches and captures redundancy.
- This refresh includes cJSON test-only/runtime overmatches, curl helper/test/refactor-only overmatches, one wrong curl CVE attribution, mbedTLS high-severity review retention, and broad multi-GT secondary-match cleanup.

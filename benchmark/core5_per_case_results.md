# Core5 Per-Case Results

This report supports thesis result interpretation beyond the aggregate matrix.
It keeps low-GT cases visible while preventing them from silently dominating macro-level claims.

## Per-Case Table

| Case | Group | Method | GT | P | R | F1 | Unsupported | Matches/GT | Extra/GT | Final Notes | Reduction | Tokens |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `text_only` | 4 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1 | 0.0000 | 518 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `diff_only` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 | 0.0000 | 7212 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `no_graph` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 | 0.0000 | 9795 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `full_adaptive_rule_family` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 | 0.0000 | 15146 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `full_no_fallback` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 | 0.0000 | 10761 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `full_strict_1hop` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 12 | 0.0000 | 14665 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `full_evidence_similarity_family` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.0000 | 2.0000 | 11 | 0.0833 | 15146 |
| `curl_v6_0_beta1_to_v6_0` | `medium_gt` | `full_similarity_family` | 4 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.2500 | 0.2500 | 5 | 0.5833 | 15146 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `text_only` | 6 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1 | 0.0000 | 779 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `diff_only` | 6 | 0.6522 | 1.0000 | 0.7895 | 0.3478 | 2.5000 | 1.5000 | 23 | 0.0000 | 15466 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `no_graph` | 6 | 0.4091 | 0.6667 | 0.5070 | 0.5909 | 1.5000 | 0.8333 | 22 | 0.0435 | 25234 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `full_adaptive_rule_family` | 6 | 0.5000 | 0.8333 | 0.6250 | 0.5000 | 1.8333 | 1.0000 | 22 | 0.0435 | 31862 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `full_no_fallback` | 6 | 0.3636 | 0.6667 | 0.4706 | 0.6364 | 1.3333 | 0.6667 | 22 | 0.0435 | 26161 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `full_strict_1hop` | 6 | 0.5455 | 0.6667 | 0.6000 | 0.4545 | 2.0000 | 1.3333 | 22 | 0.0435 | 29766 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `full_evidence_similarity_family` | 6 | 0.5263 | 0.8333 | 0.6452 | 0.4737 | 1.6667 | 0.8333 | 19 | 0.1739 | 31862 |
| `mbedtls_v6_0_beta1_to_v6_0` | `medium_gt` | `full_similarity_family` | 6 | 0.5714 | 1.0000 | 0.7273 | 0.4286 | 1.5000 | 0.5000 | 14 | 0.3913 | 31862 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `text_only` | 4 | 1.0000 | 0.2500 | 0.4000 | 0.0000 | 0.2500 | 0.0000 | 1 | 0.0000 | 482 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `diff_only` | 4 | 0.7297 | 1.0000 | 0.8437 | 0.2703 | 6.7500 | 5.7500 | 37 | 0.1190 | 35086 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `no_graph` | 4 | 0.7500 | 1.0000 | 0.8571 | 0.2500 | 6.7500 | 5.7500 | 36 | 0.1429 | 42637 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `full_adaptive_rule_family` | 4 | 0.7647 | 1.0000 | 0.8667 | 0.2353 | 6.5000 | 5.5000 | 34 | 0.1905 | 83975 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `full_no_fallback` | 4 | 0.7368 | 1.0000 | 0.8485 | 0.2632 | 7.0000 | 6.0000 | 38 | 0.0952 | 47113 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `full_strict_1hop` | 4 | 0.8000 | 1.0000 | 0.8889 | 0.2000 | 7.0000 | 6.0000 | 35 | 0.1667 | 70737 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `full_evidence_similarity_family` | 4 | 0.6000 | 1.0000 | 0.7500 | 0.4000 | 4.5000 | 3.5000 | 30 | 0.2857 | 83975 |
| `sqlite_v6_0_0_2_to_v6_1` | `medium_gt` | `full_similarity_family` | 4 | 0.6400 | 1.0000 | 0.7805 | 0.3600 | 4.0000 | 3.0000 | 25 | 0.4048 | 83975 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `text_only` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1 | 0.0000 | 367 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `diff_only` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 | 0.0000 | 1015 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `no_graph` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 | 0.0000 | 1131 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `full_adaptive_rule_family` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 | 0.0000 | 1527 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `full_no_fallback` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 | 0.0000 | 1400 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `full_strict_1hop` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 2 | 0.0000 | 1510 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `full_evidence_similarity_family` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1 | 0.5000 | 1527 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `low_gt` | `full_similarity_family` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1 | 0.5000 | 1527 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `text_only` | 2 | 1.0000 | 0.5000 | 0.6667 | 0.0000 | 0.5000 | 0.0000 | 1 | 0.0000 | 505 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `diff_only` | 2 | 0.4545 | 1.0000 | 0.6250 | 0.5455 | 2.5000 | 1.5000 | 11 | 0.0000 | 5927 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `no_graph` | 2 | 0.6000 | 1.0000 | 0.7500 | 0.4000 | 3.0000 | 2.0000 | 10 | 0.0909 | 8147 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `full_adaptive_rule_family` | 2 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 11 | 0.0000 | 11463 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `full_no_fallback` | 2 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 11 | 0.0000 | 9726 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `full_strict_1hop` | 2 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 11 | 0.0000 | 11398 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `full_evidence_similarity_family` | 2 | 0.5000 | 1.0000 | 0.6667 | 0.5000 | 2.5000 | 1.5000 | 10 | 0.0909 | 11463 |
| `cjson_v6_0_beta1_to_v6_0` | `low_gt` | `full_similarity_family` | 2 | 0.5714 | 1.0000 | 0.7273 | 0.4286 | 2.0000 | 1.0000 | 7 | 0.3636 | 11463 |

## Medium-Case View

Medium cases are defined as cases with at least 4 reviewed GT entries.
This view is used as a robustness check against low-GT zlib/cJSON effects.

| Method | Cases | Avg P | Avg R | Avg F1 | Avg Unsupported | Avg Extra/GT | Avg Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 3 | 0.3333 | 0.0833 | 0.1333 | 0.6667 | 0.0000 | 593.0000 |
| `diff_only` | 3 | 0.7940 | 1.0000 | 0.8777 | 0.2060 | 3.1667 | 19254.6667 |
| `no_graph` | 3 | 0.7197 | 0.8889 | 0.7880 | 0.2803 | 2.9444 | 25888.6667 |
| `full_adaptive_rule_family` | 3 | 0.7549 | 0.9444 | 0.8306 | 0.2451 | 2.9167 | 43661.0000 |
| `full_no_fallback` | 3 | 0.7001 | 0.8889 | 0.7730 | 0.2999 | 2.9722 | 28011.6667 |
| `full_strict_1hop` | 3 | 0.7818 | 0.8889 | 0.8296 | 0.2182 | 3.1944 | 38389.3333 |
| `full_evidence_similarity_family` | 3 | 0.7088 | 0.9444 | 0.7984 | 0.2912 | 2.1111 | 43661.0000 |
| `full_similarity_family` | 3 | 0.7371 | 1.0000 | 0.8359 | 0.2629 | 1.2500 | 43661.0000 |

## Thesis-Ready Interpretation

- The aggregate matrix and medium-case view both show that `diff_only` is a strong baseline; therefore the thesis should not claim that adding graph context always improves F1.
- On medium cases, the best average F1 method is `diff_only`.
- `full_strict_1hop` is the strongest graph-context variant in the current core5 matrix, while adaptive context provides a broader evidence view at higher token cost.
- Medium-case `full_strict_1hop` F1 is 0.8296; medium-case adaptive `full` F1 is 0.8306.
- `full_similarity_family` gives the strongest final-note compression, but its F1 drop means it should be reported as a compression-quality tradeoff.
- High `Extra/GT` values indicate that redundancy remains an important limitation and a natural target for aggregation improvements.

## Threats To Validity

- zlib and cJSON have low reviewed-GT counts, so macro averages are sensitive to these cases.
- Several variants reach recall 1.0000 because GT entries are semantic release-note items rather than fine-grained code facts.
- Manual `matches_strict.json` judgments are necessary but introduce reviewer-decision risk; security/CVE-related matches require extra audit.
- Official OpenHarmony release notes for minor component updates are incomplete, so GT depends on evidence triangulation from commits and code diffs.
- Graph context should be interpreted as analyzable evidence, not as a guaranteed accuracy improvement over diff-only evidence.

## Reporting Rule

- Use the aggregate matrix as the main result table.
- Use this per-case report to explain method behavior and low-GT sensitivity.
- Do not claim that graph context universally improves F1; report it as a context/cost/redundancy tradeoff.

# Full-Scope First-Pass Matrix

Generated on: 2026-05-30

This report compares the two currently completed full-scope large cases: Git 2.53 and PCRE2 v6.1. It uses rule-assisted strict matches after a second-pass false-positive cleanup, not final manual adjudication. Use it to inspect scale and cross-case tendencies only.

## Case-Level Rows

| Case | Role | Variant | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `text_only` | 39 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `diff_only` | 39 | 878 | 0.0923 | 0.8462 | 0.1664 | 0.9077 | 2.0769 | 1.2308 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `no_graph` | 39 | 883 | 0.1031 | 0.8462 | 0.1837 | 0.8969 | 2.3333 | 1.4872 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `no_fallback` | 39 | 892 | 0.0964 | 0.7949 | 0.1720 | 0.9036 | 2.2051 | 1.4103 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_adaptive_rule_family` | 39 | 900 | 0.0978 | 0.7949 | 0.1741 | 0.9022 | 2.2564 | 1.4615 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_strict_1hop` | 39 | 902 | 0.1053 | 0.8718 | 0.1879 | 0.8947 | 2.4359 | 1.5641 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_similarity_family` | 39 | 490 | 0.1510 | 0.8205 | 0.2551 | 0.8490 | 1.8974 | 1.0769 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_evidence_similarity_family` | 39 | 682 | 0.1202 | 0.7949 | 0.2089 | 0.8798 | 2.1026 | 1.3077 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `text_only` | 16 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `diff_only` | 16 | 1082 | 0.0444 | 0.8125 | 0.0841 | 0.9556 | 4.0625 | 3.2500 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `no_graph` | 16 | 1078 | 0.0408 | 0.8125 | 0.0777 | 0.9592 | 3.8750 | 3.0625 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `no_fallback` | 16 | 1085 | 0.0442 | 0.7500 | 0.0836 | 0.9558 | 4.0000 | 3.2500 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_adaptive_rule_family` | 16 | 1104 | 0.0435 | 0.8125 | 0.0825 | 0.9565 | 4.3125 | 3.5000 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_strict_1hop` | 16 | 1097 | 0.0428 | 0.7500 | 0.0811 | 0.9572 | 3.8125 | 3.0625 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_similarity_family` | 16 | 382 | 0.0942 | 0.8125 | 0.1689 | 0.9058 | 3.7500 | 2.9375 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_evidence_similarity_family` | 16 | 459 | 0.0959 | 0.8125 | 0.1715 | 0.9041 | 4.2500 | 3.4375 |

## Aggregate By Variant

| Variant | Cases | Total GT | Total Generated | Macro F1 | Micro Precision | Micro Recall | Micro F1 | Avg Unsupported Rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 2 | 55 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 |
| `diff_only` | 2 | 55 | 1960 | 0.1253 | 0.0658 | 0.8364 | 0.1220 | 0.9316 |
| `no_graph` | 2 | 55 | 1961 | 0.1307 | 0.0688 | 0.8364 | 0.1272 | 0.9281 |
| `no_fallback` | 2 | 55 | 1977 | 0.1278 | 0.0678 | 0.7818 | 0.1247 | 0.9297 |
| `full_adaptive_rule_family` | 2 | 55 | 2004 | 0.1283 | 0.0679 | 0.8000 | 0.1251 | 0.9294 |
| `full_strict_1hop` | 2 | 55 | 1999 | 0.1345 | 0.0710 | 0.8364 | 0.1309 | 0.9260 |
| `full_similarity_family` | 2 | 55 | 872 | 0.2120 | 0.1261 | 0.8182 | 0.2186 | 0.8774 |
| `full_evidence_similarity_family` | 2 | 55 | 1141 | 0.1902 | 0.1104 | 0.8000 | 0.1941 | 0.8920 |

## Interpretation Boundary

- This is not the final thesis main-result table. It combines only two large/full-scope cases and still uses rule-assisted matching, although clear false positives have been removed in a second-pass audit.
- The table is useful for checking whether full function-level coverage creates systematic redundancy and unsupported-claim pressure across different repositories.
- Final thesis conclusions should keep the 82-GT manually reviewed benchmark as the primary table and report these two cases as a separate full-scope stress/extension experiment unless a complete manual adjudication pass is performed.

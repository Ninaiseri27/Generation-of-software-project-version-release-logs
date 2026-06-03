# Full-Scope Human-Audited Matrix

Generated on: 2026-05-30

This matrix uses `matches_strict_human_audited.json` and `evaluation_strict_human_audited.json` for the two large/full-scope cases. The audit applies direct GT-semantic criteria and removes malformed raw-JSON notes, display-only leakage, and helper-only notes that do not express the release-note-level fact. Treat this as close-to-manual audit by Codex; user sign-off is still recommended before thesis-final labels.

## Case-Level Rows

| Case | Role | Variant | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `text_only` | 39 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `diff_only` | 39 | 878 | 0.0809 | 0.7436 | 0.1459 | 0.9191 | 1.8205 | 1.0769 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `no_graph` | 39 | 883 | 0.0861 | 0.7692 | 0.1548 | 0.9139 | 1.9487 | 1.1795 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `no_fallback` | 39 | 892 | 0.0852 | 0.7436 | 0.1529 | 0.9148 | 1.9487 | 1.2051 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_adaptive_rule_family` | 39 | 900 | 0.0878 | 0.7436 | 0.1570 | 0.9122 | 2.0256 | 1.2821 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_strict_1hop` | 39 | 902 | 0.0909 | 0.8205 | 0.1637 | 0.9091 | 2.1026 | 1.2821 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_similarity_family` | 39 | 490 | 0.1347 | 0.7692 | 0.2292 | 0.8653 | 1.6923 | 0.9231 |
| `upstream_git_2_52_to_2_53` | rich release / broad source coverage | `full_evidence_similarity_family` | 39 | 682 | 0.1100 | 0.7436 | 0.1916 | 0.8900 | 1.9231 | 1.1795 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `text_only` | 16 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `diff_only` | 16 | 1082 | 0.0407 | 0.7500 | 0.0771 | 0.9593 | 3.3750 | 2.6250 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `no_graph` | 16 | 1078 | 0.0390 | 0.7500 | 0.0741 | 0.9610 | 3.3125 | 2.5625 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `no_fallback` | 16 | 1085 | 0.0406 | 0.6875 | 0.0766 | 0.9594 | 3.4375 | 2.7500 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_adaptive_rule_family` | 16 | 1104 | 0.0389 | 0.7500 | 0.0741 | 0.9611 | 3.5000 | 2.7500 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_strict_1hop` | 16 | 1097 | 0.0383 | 0.7500 | 0.0729 | 0.9617 | 3.1875 | 2.4375 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_similarity_family` | 16 | 382 | 0.0864 | 0.6875 | 0.1535 | 0.9136 | 3.0000 | 2.3125 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | large stress / JIT-SLJIT churn | `full_evidence_similarity_family` | 16 | 459 | 0.0871 | 0.7500 | 0.1561 | 0.9129 | 3.4375 | 2.6875 |

## Aggregate By Variant

| Variant | Cases | Total GT | Total Generated | Macro F1 | Micro Precision | Micro Recall | Micro F1 | Avg Unsupported Rate | Avg Matches/GT | Avg Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 2 | 55 | 2 | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `diff_only` | 2 | 55 | 1960 | 0.1115 | 0.0587 | 0.7455 | 0.1088 | 0.9392 | 2.5978 | 1.8510 |
| `no_graph` | 2 | 55 | 1961 | 0.1144 | 0.0602 | 0.7636 | 0.1116 | 0.9375 | 2.6306 | 1.8710 |
| `no_fallback` | 2 | 55 | 1977 | 0.1148 | 0.0607 | 0.7273 | 0.1120 | 0.9371 | 2.6931 | 1.9775 |
| `full_adaptive_rule_family` | 2 | 55 | 2004 | 0.1155 | 0.0609 | 0.7455 | 0.1126 | 0.9366 | 2.7628 | 2.0160 |
| `full_strict_1hop` | 2 | 55 | 1999 | 0.1183 | 0.0620 | 0.8000 | 0.1151 | 0.9354 | 2.6450 | 1.8598 |
| `full_similarity_family` | 2 | 55 | 872 | 0.1913 | 0.1135 | 0.7455 | 0.1971 | 0.8894 | 2.3461 | 1.6178 |
| `full_evidence_similarity_family` | 2 | 55 | 1141 | 0.1739 | 0.1008 | 0.7455 | 0.1776 | 0.9015 | 2.6803 | 1.9335 |

## Interpretation Boundary

- This matrix is stricter than `full_scope_first_pass_matrix.md` and should be preferred when discussing whether the two large cases can be merged.
- Even after human-style cleanup, unsupported rates remain high because full function-level coverage generates hundreds or thousands of entries while GT is release-note-granular.
- The large cases can be used in an expanded benchmark table only if the paper clearly labels the protocol as `82-GT core + 55-GT full-scope extension`; they should not silently replace the 82-GT primary table.

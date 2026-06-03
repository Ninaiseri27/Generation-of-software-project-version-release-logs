# Full-Scope Salience Aggregation Projection

This report is an offline projection over existing human-audited large-case matches. It does not rerun the LLM and should be treated as a candidate-filtering experiment until manually audited.

## Aggregate Rows

| Variant | GT | Final Notes | Kept Salient | Filtered | P | R | F1 | Unsupported | Reduction | Macro F1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `diff_only` | 55 | 439 | 685 | 1342 | 0.1526 | 0.6182 | 0.2448 | 0.8474 | 0.7627 | 0.2820 |
| `no_graph` | 55 | 419 | 641 | 1386 | 0.1766 | 0.6545 | 0.2782 | 0.8234 | 0.7745 | 0.3080 |
| `no_fallback` | 55 | 373 | 550 | 1477 | 0.1877 | 0.6000 | 0.2859 | 0.8123 | 0.8013 | 0.3116 |
| `full_adaptive_rule_family` | 55 | 419 | 652 | 1376 | 0.1671 | 0.6364 | 0.2647 | 0.8329 | 0.7792 | 0.2830 |
| `full_strict_1hop` | 55 | 395 | 613 | 1413 | 0.1722 | 0.6909 | 0.2756 | 0.8278 | 0.7916 | 0.2962 |
| `full_similarity_family` | 55 | 419 | 652 | 1376 | 0.1838 | 0.6545 | 0.2870 | 0.8162 | 0.5387 | 0.3058 |
| `full_evidence_similarity_family` | 55 | 419 | 652 | 1376 | 0.1885 | 0.6545 | 0.2928 | 0.8115 | 0.6512 | 0.3111 |

## Per-Case Rows

| Case | Variant | Source Notes | Salient | Filtered | Projected Notes | P | R | F1 | Unsupported | Reduction |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `upstream_git_2_52_to_2_53` | `diff_only` | 878 | 509 | 395 | 321 | 0.1153 | 0.5897 | 0.1928 | 0.8847 | 0.6344 |
| `upstream_git_2_52_to_2_53` | `no_graph` | 883 | 443 | 462 | 304 | 0.1480 | 0.6154 | 0.2386 | 0.8520 | 0.6557 |
| `upstream_git_2_52_to_2_53` | `no_fallback` | 892 | 386 | 519 | 269 | 0.1561 | 0.5897 | 0.2469 | 0.8439 | 0.6984 |
| `upstream_git_2_52_to_2_53` | `full_adaptive_rule_family` | 900 | 479 | 426 | 302 | 0.1490 | 0.6154 | 0.2399 | 0.8510 | 0.6644 |
| `upstream_git_2_52_to_2_53` | `full_strict_1hop` | 902 | 460 | 445 | 288 | 0.1458 | 0.7179 | 0.2424 | 0.8542 | 0.6807 |
| `upstream_git_2_52_to_2_53` | `full_similarity_family` | 490 | 479 | 426 | 302 | 0.1589 | 0.6667 | 0.2567 | 0.8411 | 0.3837 |
| `upstream_git_2_52_to_2_53` | `full_evidence_similarity_family` | 682 | 479 | 426 | 302 | 0.1689 | 0.6410 | 0.2673 | 0.8311 | 0.5572 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `diff_only` | 1082 | 176 | 947 | 118 | 0.2542 | 0.6875 | 0.3712 | 0.7458 | 0.8909 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `no_graph` | 1078 | 198 | 924 | 115 | 0.2522 | 0.7500 | 0.3774 | 0.7478 | 0.8933 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | 1085 | 164 | 958 | 104 | 0.2692 | 0.6250 | 0.3763 | 0.7308 | 0.9041 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `full_adaptive_rule_family` | 1104 | 173 | 950 | 117 | 0.2137 | 0.6875 | 0.3260 | 0.7863 | 0.8940 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `full_strict_1hop` | 1097 | 153 | 968 | 107 | 0.2430 | 0.6250 | 0.3499 | 0.7570 | 0.9025 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `full_similarity_family` | 382 | 173 | 950 | 117 | 0.2479 | 0.6250 | 0.3550 | 0.7521 | 0.6937 |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | `full_evidence_similarity_family` | 459 | 173 | 950 | 117 | 0.2393 | 0.6875 | 0.3550 | 0.7607 | 0.7451 |

## Interpretation

- The salience filter is intentionally conservative and deterministic; it removes test-only, internal-maintenance, build, documentation, logging, and helper-only notes before similarity grouping.
- The metrics above are projected from source-entry matches, not manually re-audited final generated notes. Use them to decide whether a full manual audit is worthwhile.
- If recall drops sharply, the rule set is too aggressive for thesis-final use and should be reported as a failed or exploratory optimization rather than merged into the main result.

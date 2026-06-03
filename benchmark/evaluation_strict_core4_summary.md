# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Redundancy | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 4 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 6 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 6 | 23 | 0.9565 | 1.0000 | 0.9778 | 0.0435 | 16 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 6 | 22 | 0.5455 | 0.8333 | 0.6593 | 0.4545 | 7 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 22 | 0.7273 | 0.8333 | 0.7767 | 0.2727 | 11 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | `evaluated` | 4 | 1 | 1.0000 | 0.2500 | 0.4000 | 0.0000 | 0 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | `evaluated` | 4 | 37 | 0.7297 | 1.0000 | 0.8437 | 0.2703 | 23 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | `evaluated` | 4 | 36 | 0.7500 | 1.0000 | 0.8571 | 0.2500 | 23 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 34 | 0.7647 | 1.0000 | 0.8667 | 0.2353 | 22 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `text_only` | `evaluated` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `diff_only` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `no_graph` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Redundancy | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 4 | 0.5000 | 0.3125 | 0.3500 | 0.5000 | 0.0000 | 1.0000 |
| `diff_only` | 4 | 0.9216 | 1.0000 | 0.9554 | 0.0784 | 12.2500 | 1.0000 |
| `no_graph` | 4 | 0.8239 | 0.9583 | 0.8791 | 0.1761 | 10.0000 | 1.0000 |
| `full` | 4 | 0.8730 | 0.9583 | 0.9108 | 0.1270 | 10.7500 | 1.0000 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, and redundancy remain blank until manual matches are supplied.
- The zlib case has only one reviewed GT item, so its perfect scores should be treated as repository/category coverage evidence, not as strong method-performance evidence.
- The main method-comparison signal should still come from the medium curl, sqlite, and mbedtls cases.

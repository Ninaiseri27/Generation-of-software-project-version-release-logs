# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 4 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 6 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 6 | 23 | 0.6522 | 1.0000 | 0.7895 | 0.3478 | 2.5000 | 1.5000 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 6 | 22 | 0.4091 | 0.6667 | 0.5070 | 0.5909 | 1.5000 | 0.8333 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 22 | 0.5000 | 0.8333 | 0.6250 | 0.5000 | 1.8333 | 1.0000 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | `evaluated` | 4 | 1 | 1.0000 | 0.2500 | 0.4000 | 0.0000 | 0.2500 | 0.0000 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | `evaluated` | 4 | 37 | 0.7297 | 1.0000 | 0.8437 | 0.2703 | 6.7500 | 5.7500 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | `evaluated` | 4 | 36 | 0.7500 | 1.0000 | 0.8571 | 0.2500 | 6.7500 | 5.7500 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 34 | 0.7647 | 1.0000 | 0.8667 | 0.2353 | 6.5000 | 5.5000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `text_only` | `evaluated` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `diff_only` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `no_graph` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 2 | 1 | 1.0000 | 0.5000 | 0.6667 | 0.0000 | 0.5000 | 0.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 2 | 11 | 0.4545 | 1.0000 | 0.6250 | 0.5455 | 2.5000 | 1.5000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 2 | 10 | 0.6000 | 1.0000 | 0.7500 | 0.4000 | 3.0000 | 2.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 2 | 11 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 5 | 0.6000 | 0.3500 | 0.4133 | 0.4000 | 0.3500 | 0.0000 | 1.0000 |
| `diff_only` | 5 | 0.7673 | 1.0000 | 0.8516 | 0.2327 | 3.4000 | 2.4000 | 1.0000 |
| `no_graph` | 5 | 0.7518 | 0.9333 | 0.8228 | 0.2482 | 3.3000 | 2.3667 | 1.0000 |
| `full` | 5 | 0.7620 | 0.9667 | 0.8395 | 0.2380 | 3.3167 | 2.3500 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 5 | 0.6000 | 0.1765 | 0.2727 | 0.1765 | 0.0000 |
| `diff_only` | 5 | 0.7176 | 1.0000 | 0.8356 | 3.6471 | 2.6471 |
| `no_graph` | 5 | 0.6829 | 0.8824 | 0.7699 | 3.3529 | 2.4706 |
| `full` | 5 | 0.7037 | 0.9412 | 0.8053 | 3.4118 | 2.4706 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

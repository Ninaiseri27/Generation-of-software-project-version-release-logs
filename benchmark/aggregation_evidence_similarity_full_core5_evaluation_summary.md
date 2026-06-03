# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 11 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.0000 | 2.0000 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 19 | 0.5263 | 0.8333 | 0.6452 | 0.4737 | 1.6667 | 0.8333 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 30 | 0.6000 | 1.0000 | 0.7500 | 0.4000 | 4.5000 | 3.5000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `evaluated` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 2 | 10 | 0.5000 | 1.0000 | 0.6667 | 0.5000 | 2.5000 | 1.5000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 0.7253 | 0.9667 | 0.8124 | 0.2747 | 2.5333 | 1.5667 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 0.6338 | 0.9412 | 0.7575 | 2.7059 | 1.7647 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 22 | 0.5455 | 0.6667 | 0.6000 | 0.4545 | 2.0000 | 1.3333 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 35 | 0.8000 | 1.0000 | 0.8889 | 0.2000 | 7.0000 | 6.0000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 2 | 11 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 0.7782 | 0.9333 | 0.8390 | 0.2218 | 3.4500 | 2.5167 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 0.7317 | 0.8824 | 0.8000 | 3.5882 | 2.7059 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

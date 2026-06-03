# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 5 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.2500 | 0.2500 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 14 | 0.5714 | 1.0000 | 0.7273 | 0.4286 | 1.5000 | 0.5000 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 25 | 0.6400 | 1.0000 | 0.7805 | 0.3600 | 4.0000 | 3.0000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `evaluated` | 1 | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 1.0000 | 0.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 2 | 7 | 0.5714 | 1.0000 | 0.7273 | 0.4286 | 2.0000 | 1.0000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 0.7566 | 1.0000 | 0.8470 | 0.2434 | 1.9500 | 0.9500 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 0.6538 | 1.0000 | 0.7907 | 2.0588 | 1.0588 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

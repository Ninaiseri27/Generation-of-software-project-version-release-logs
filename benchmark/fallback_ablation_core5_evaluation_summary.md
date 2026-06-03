# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `no_fallback` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 3.2500 | 2.2500 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_fallback` | `evaluated` | 6 | 22 | 0.3636 | 0.6667 | 0.4706 | 0.6364 | 1.3333 | 0.6667 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_fallback` | `evaluated` | 4 | 38 | 0.7368 | 1.0000 | 0.8485 | 0.2632 | 7.0000 | 6.0000 | 1.0000 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `no_fallback` | `evaluated` | 1 | 2 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 2.0000 | 1.0000 | 1.0000 |
| `cjson_v6_0_beta1_to_v6_0` | `no_fallback` | `evaluated` | 2 | 11 | 0.5455 | 1.0000 | 0.7059 | 0.4545 | 3.0000 | 2.0000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 5 | 0.7292 | 0.9333 | 0.8050 | 0.2708 | 3.3167 | 2.3833 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 5 | 0.6588 | 0.8824 | 0.7544 | 3.3529 | 2.4706 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

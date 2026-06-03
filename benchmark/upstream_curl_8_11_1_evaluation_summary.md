# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_8_11_0_to_8_11_1` | `text_only` | `evaluated` | 16 | 1 | 1.0000 | 0.0625 | 0.1176 | 0.0000 | 0.0625 | 0.0000 | 1.0000 |
| `curl_8_11_0_to_8_11_1` | `diff_only` | `evaluated` | 16 | 99 | 0.2929 | 1.0000 | 0.4531 | 0.7071 | 1.8125 | 0.8125 | 1.0000 |
| `curl_8_11_0_to_8_11_1` | `no_graph` | `evaluated` | 16 | 102 | 0.2745 | 1.0000 | 0.4308 | 0.7255 | 1.7500 | 0.7500 | 1.0000 |
| `curl_8_11_0_to_8_11_1` | `full` | `evaluated` | 16 | 101 | 0.2871 | 1.0000 | 0.4462 | 0.7129 | 1.8125 | 0.8125 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 0.0625 | 0.1176 | 0.0000 | 0.0625 | 0.0000 | 1.0000 |
| `diff_only` | 1 | 0.2929 | 1.0000 | 0.4531 | 0.7071 | 1.8125 | 0.8125 | 1.0000 |
| `no_graph` | 1 | 0.2745 | 1.0000 | 0.4308 | 0.7255 | 1.7500 | 0.7500 | 1.0000 |
| `full` | 1 | 0.2871 | 1.0000 | 0.4462 | 0.7129 | 1.8125 | 0.8125 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 0.0625 | 0.1176 | 0.0625 | 0.0000 |
| `diff_only` | 1 | 0.2929 | 1.0000 | 0.4531 | 1.8125 | 0.8125 |
| `no_graph` | 1 | 0.2745 | 1.0000 | 0.4308 | 1.7500 | 0.7500 |
| `full` | 1 | 0.2871 | 1.0000 | 0.4462 | 1.8125 | 0.8125 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

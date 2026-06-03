# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_8_14_0_to_8_14_1` | `text_only` | `evaluated` | 10 | 1 | 1.0000 | 0.1000 | 0.1818 | 0.0000 | 0.1000 | 0.0000 | 1.0000 |
| `curl_8_14_0_to_8_14_1` | `diff_only` | `evaluated` | 10 | 121 | 0.1901 | 0.8000 | 0.3072 | 0.8099 | 2.3000 | 1.5000 | 1.0000 |
| `curl_8_14_0_to_8_14_1` | `no_graph` | `evaluated` | 10 | 118 | 0.2034 | 0.8000 | 0.3243 | 0.7966 | 2.4000 | 1.6000 | 1.0000 |
| `curl_8_14_0_to_8_14_1` | `full` | `evaluated` | 10 | 119 | 0.2017 | 0.8000 | 0.3221 | 0.7983 | 2.4000 | 1.6000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 0.1000 | 0.1818 | 0.0000 | 0.1000 | 0.0000 | 1.0000 |
| `diff_only` | 1 | 0.1901 | 0.8000 | 0.3072 | 0.8099 | 2.3000 | 1.5000 | 1.0000 |
| `no_graph` | 1 | 0.2034 | 0.8000 | 0.3243 | 0.7966 | 2.4000 | 1.6000 | 1.0000 |
| `full` | 1 | 0.2017 | 0.8000 | 0.3221 | 0.7983 | 2.4000 | 1.6000 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 0.1000 | 0.1818 | 0.1000 | 0.0000 |
| `diff_only` | 1 | 0.1901 | 0.8000 | 0.3072 | 2.3000 | 1.5000 |
| `no_graph` | 1 | 0.2034 | 0.8000 | 0.3243 | 2.4000 | 1.6000 |
| `full` | 1 | 0.2017 | 0.8000 | 0.3221 | 2.4000 | 1.6000 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

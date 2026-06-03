# Evaluation Summary

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `evaluated` | 5 | 1 | 1.0000 | 0.2000 | 0.3333 | 0.0000 | 0.2000 | 0.0000 | 1.0000 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `evaluated` | 5 | 78 | 0.0513 | 0.8000 | 0.0964 | 0.9487 | 1.2000 | 0.4000 | 1.0000 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `evaluated` | 5 | 79 | 0.0633 | 0.6000 | 0.1145 | 0.9367 | 1.0000 | 0.4000 | 1.0000 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `evaluated` | 5 | 79 | 0.0633 | 0.8000 | 0.1173 | 0.9367 | 1.4000 | 0.6000 | 1.0000 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 5 | 79 | 0.0759 | 1.0000 | 0.1412 | 0.9241 | 1.6000 | 0.6000 | 1.0000 |

## Macro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Unsupported Rate | Avg Matches/GT | Avg Extra/GT | Structural Valid |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 0.2000 | 0.3333 | 0.0000 | 0.2000 | 0.0000 | 1.0000 |
| `diff_only` | 1 | 0.0513 | 0.8000 | 0.0964 | 0.9487 | 1.2000 | 0.4000 | 1.0000 |
| `no_graph` | 1 | 0.0633 | 0.6000 | 0.1145 | 0.9367 | 1.0000 | 0.4000 | 1.0000 |
| `no_fallback` | 1 | 0.0633 | 0.8000 | 0.1173 | 0.9367 | 1.4000 | 0.6000 | 1.0000 |
| `full` | 1 | 0.0759 | 1.0000 | 0.1412 | 0.9241 | 1.6000 | 0.6000 | 1.0000 |

## Micro Averages

| Variant | Evaluated Cases | Precision | Recall | F1 | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 0.2000 | 0.3333 | 0.2000 | 0.0000 |
| `diff_only` | 1 | 0.0513 | 0.8000 | 0.0964 | 1.2000 | 0.4000 |
| `no_graph` | 1 | 0.0633 | 0.6000 | 0.1145 | 1.0000 | 0.4000 |
| `no_fallback` | 1 | 0.0633 | 0.8000 | 0.1173 | 1.4000 | 0.6000 |
| `full` | 1 | 0.0759 | 1.0000 | 0.1412 | 1.6000 | 0.6000 |

Notes:

- `match_required` means the generated notes and ground truth were loaded, but no reviewer `matches.json` file was found.
- Precision, recall, F1, unsupported rate, `Matches/GT`, and `Extra/GT` remain blank until manual matches are supplied.

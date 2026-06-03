# Core5 Experiment Matrix

| Method | Group | P | R | Macro F1 | Micro F1 | Unsupported | Matches/GT | Extra/GT | Final Notes | Reduction | Tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | `prompt_baseline` | 0.6000 | 0.3500 | 0.4133 | 0.2727 | 0.4000 | 0.1765 | 0.0000 | 1.0000 | 0.0000 | 530.2000 |
| `diff_only` | `prompt_baseline` | 0.7673 | 1.0000 | 0.8516 | 0.8356 | 0.2327 | 3.6471 | 2.6471 | 17.0000 | 0.0238 | 12941.2000 |
| `no_graph` | `prompt_baseline` | 0.7518 | 0.9333 | 0.8228 | 0.7699 | 0.2482 | 3.3529 | 2.4706 | 16.4000 | 0.0555 | 17388.8000 |
| `full_adaptive_rule_family` | `main_method` | 0.7620 | 0.9667 | 0.8395 | 0.8053 | 0.2380 | 3.4118 | 2.4706 | 16.2000 | 0.0468 | 28794.6000 |
| `full_no_fallback` | `fallback_ablation` | 0.7292 | 0.9333 | 0.8050 | 0.7544 | 0.2708 | 3.3529 | 2.4706 | 17.0000 | 0.0277 | 19032.2000 |
| `full_strict_1hop` | `cmg_ablation` | 0.7782 | 0.9333 | 0.8390 | 0.8000 | 0.2218 | 3.5882 | 2.7059 | 16.4000 | 0.0420 | 25615.2000 |
| `full_evidence_similarity_family` | `aggregation_ablation` | 0.7253 | 0.9667 | 0.8124 | 0.7575 | 0.2747 | 2.7059 | 1.7647 | 14.2000 | 0.2268 | 28794.6000 |
| `full_similarity_family` | `aggregation_ablation` | 0.7566 | 1.0000 | 0.8470 | 0.7907 | 0.2434 | 2.0588 | 1.0588 | 10.4000 | 0.4486 | 28794.6000 |

## Interpretation

- Best macro F1: `diff_only`.
- Best micro F1: `diff_only`.
- Lowest token cost: `text_only`.
- Strongest compression: `full_similarity_family`.
- Lowest unsupported-claim rate: `full_strict_1hop`.

The matrix is intended for thesis tables. It should be read as a tradeoff view, not a single-score ranking.
`Micro F1` is computed from total matched/generated/GT counts across all core5 cases, so it is less sensitive to tiny low-GT cases than unweighted macro F1.
`Matches/GT` is valid semantic matches divided by total GT entries. `Extra/GT` is redundant matches beyond the first match per GT, divided by total GT entries.

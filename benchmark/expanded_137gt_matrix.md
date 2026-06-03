# Expanded 137-GT Experiment Matrix

This file combines the controlled 82-GT matrix with the human-standard audited 55-GT full-scope extension. The extension covers Git 2.53 and PCRE2 full-scope releases. It is suitable for robustness and scale discussion, while the original 82-GT matrix remains the cleaner controlled comparison.

## Scope

| Scope | Cases | GT | Case-variant cells | Use in thesis |
| --- | ---: | ---: | ---: | --- |
| Controlled matrix | 11 | 82 | 88 | Primary controlled comparison |
| Full-scope extension | 2 | 55 | 16 | Scale/robustness extension after human-standard audit |
| Expanded matrix | 13 | 137 | 104 | Combined trend check, not the only conclusion source |

## Quality Matrix

| Method | 82 Macro F1 | 55 Macro F1 | 137 Macro F1 | 82 Micro F1 | 55 Micro F1 | 137 Micro F1 |
| --- | --- | --- | --- | --- | --- | --- |
| Text-only | 0.2909 | 0.0000 | 0.2461 | 0.1505 | 0.0000 | 0.0933 |
| Diff-only | 0.6543 | 0.1115 | 0.5708 | 0.5677 | 0.1088 | 0.2431 |
| No-Graph | 0.6397 | 0.1144 | 0.5589 | 0.5495 | 0.1116 | 0.2390 |
| Full adaptive | 0.6419 | 0.1155 | 0.5609 | 0.5503 | 0.1126 | 0.2370 |
| No-Fallback | 0.6228 | 0.1148 | 0.5446 | 0.5239 | 0.1120 | 0.2306 |
| Strict 1-hop | 0.6616 | 0.1183 | 0.5781 | 0.5585 | 0.1151 | 0.2429 |
| Similarity family | 0.7020 | 0.1913 | 0.6235 | 0.6046 | 0.1971 | 0.3513 |
| Evidence similarity | 0.6532 | 0.1739 | 0.5795 | 0.5555 | 0.1776 | 0.3173 |

## Expanded 137-GT Tradeoff Metrics

| Method | Micro P | Micro R | Unsupported | Matches/GT | Extra/GT | Avg notes | Reduction | Avg tokens |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Text-only | 0.5385 | 0.0511 | 0.4615 | 0.0511 | 0.0000 | 1.0 | 0.0000 | 633.7 |
| Diff-only | 0.1415 | 0.8613 | 0.8585 | 2.7518 | 1.8905 | 197.8 | 0.0298 | 196155.4 |
| No-Graph | 0.1391 | 0.8467 | 0.8609 | 2.6934 | 1.8467 | 197.4 | 0.0321 | 283941.7 |
| Full adaptive | 0.1374 | 0.8613 | 0.8626 | 2.7372 | 1.8759 | 201.0 | 0.0143 | 487262.8 |
| No-Fallback | 0.1339 | 0.8321 | 0.8661 | 2.6350 | 1.8029 | 199.4 | 0.0223 | 300877.8 |
| Strict 1-hop | 0.1412 | 0.8686 | 0.8588 | 2.7591 | 1.8905 | 200.5 | 0.0170 | 444067.6 |
| Similarity family | 0.2207 | 0.8613 | 0.7793 | 2.1898 | 1.3285 | 99.0 | 0.5145 | 487262.8 |
| Evidence similarity | 0.1949 | 0.8540 | 0.8051 | 2.4964 | 1.6423 | 128.7 | 0.3689 | 487262.8 |

## Cost And Compression Metrics

| Method | 82 Reduction | 55 Reduction | 137 Reduction | 82 Avg Tokens | 55 Avg Tokens | 137 Avg Tokens |
| --- | --- | --- | --- | --- | --- | --- |
| Text-only | 0.0000 | 0.0000 | 0.0000 | 613.3 | 746.0 | 633.7 |
| Diff-only | 0.0177 | 0.0335 | 0.0298 | 58106.6 | 955423.5 | 196155.4 |
| No-Graph | 0.0289 | 0.0330 | 0.0321 | 79091.5 | 1410618.0 | 283941.7 |
| Full adaptive | 0.0225 | 0.0118 | 0.0143 | 123989.7 | 2485265.0 | 487262.8 |
| No-Fallback | 0.0128 | 0.0251 | 0.0223 | 83799.6 | 1494808.0 | 300877.8 |
| Strict 1-hop | 0.0257 | 0.0143 | 0.0170 | 116048.6 | 2248172.0 | 444067.6 |
| Similarity family | 0.3339 | 0.5700 | 0.5145 | 123989.7 | 2485265.0 | 487262.8 |
| Evidence similarity | 0.1461 | 0.4374 | 0.3689 | 123989.7 | 2485265.0 | 487262.8 |

Definitions:

- `Reduction` is `1 - final_note_count / pre_aggregation_note_count` over the selected scope.
- `Avg tokens` is the mean case-level sum of `usage.total_tokens` from `release_note.json` entries.
- Re-aggregation variants reuse the same LLM calls as their source generation, so their token cost can match the corresponding full-context generation while their reduction differs.

## Expanded Ranking

| Rank | By 137 Macro F1 | Macro F1 | By 137 Micro F1 | Micro F1 |
| --- | --- | --- | --- | --- |
| 1 | Similarity family | 0.6235 | Similarity family | 0.3513 |
| 2 | Evidence similarity | 0.5795 | Evidence similarity | 0.3173 |
| 3 | Strict 1-hop | 0.5781 | Diff-only | 0.2431 |
| 4 | Diff-only | 0.5708 | Strict 1-hop | 0.2429 |
| 5 | Full adaptive | 0.5609 | No-Graph | 0.2390 |
| 6 | No-Graph | 0.5589 | Full adaptive | 0.2370 |
| 7 | No-Fallback | 0.5446 | No-Fallback | 0.2306 |
| 8 | Text-only | 0.2461 | Text-only | 0.0933 |

## Interpretation

- `full_similarity_family` remains the strongest method under the expanded 137-GT view by both Macro F1 and Micro F1.
- Adding full-scope Git and PCRE2 sharply lowers absolute F1 and precision because these cases contain hundreds to thousands of generated function-level notes. This confirms the advisor-facing concern that large releases expose redundancy and unsupported-claim risk more clearly than the smaller controlled cases.
- The expanded result should not be used as a replacement for the 82-GT controlled table. The defensible thesis framing is: use the 82-GT matrix as the main controlled benchmark, then use the 137-GT matrix as a scale/robustness extension showing whether trends survive under larger releases.
- High recall in the evidence-rich variants remains meaningful, but it must be reported together with unsupported rate, Matches/GT, Extra/GT, average final notes, reduction, and token cost.

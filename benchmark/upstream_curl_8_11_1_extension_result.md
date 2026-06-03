# Upstream curl 8.11.1 Extension Result

Last updated: 2026-05-28

## Case

- Case ID: `curl_8_11_0_to_8_11_1`
- Role: extension/stress evidence, not core-average replacement.
- GT count: `16`
- Stage 1: `103` changed functions across `67` C/C++ files, with `117` commit messages.
- Stage 2 CMG: `87/103` prompt-node matches, `16` unmatched symbols, and `103` entries with fallback context.

## Generation Setup

Command family:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli run-baselines `
  --config configs\benchmark\upstream_curl_8_11_0_to_8_11_1.json `
  --variants text_only diff_only no_graph full `
  --backend openai-compatible `
  --model deepseek-chat `
  --aggregation-strategy rule_family
```

All four variants completed with `0` generation failures.

## Strict Evaluation

| Variant | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 16 | 1 | 1.0000 | 0.0625 | 0.1176 | 0.0000 | 0.0625 | 0.0000 |
| `diff_only` | 16 | 99 | 0.2929 | 1.0000 | 0.4531 | 0.7071 | 1.8125 | 0.8125 |
| `no_graph` | 16 | 102 | 0.2745 | 1.0000 | 0.4308 | 0.7255 | 1.7500 | 0.7500 |
| `full` | 16 | 101 | 0.2871 | 1.0000 | 0.4462 | 0.7129 | 1.8125 | 0.8125 |

Source summaries:

- `benchmark/upstream_curl_8_11_1_evaluation_summary.md`
- `benchmark/upstream_curl_8_11_1_output_summary.md`

## Output Scale

| Variant | Prompt Entries | Generated | Final Notes | Reduction | Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1 | 1 | 0.0000 | 633 |
| `diff_only` | 103 | 103 | 99 | 0.0388 | 78164 |
| `no_graph` | 103 | 103 | 102 | 0.0097 | 113490 |
| `full` | 103 | 103 | 101 | 0.0194 | 170746 |

## Interpretation

- This case is a useful second extension row because it has more GT items than the core5 cases and a comparable four-variant generation/evaluation protocol.
- Evidence-rich variants reach full recall under strict semantic matching, showing that source-level evidence can cover the reviewed release-note topics.
- Precision remains low and unsupported rate remains above `0.70`, which means the model generates many function-local or internal-maintenance notes that are not release-note-level facts.
- `diff_only` is strongest on F1 in this case, while `full` has much higher token cost. This supports a cautious conclusion: graph context is useful as explainable context and an ablation factor, but it is not automatically better than direct diff evidence for every upstream release.
- The result strengthens the thesis argument that the key remaining problem is release-note-level filtering and aggregation, not simply collecting more low-level context.

## Match Policy Notes

- Matches were accepted only when the generated note described the same user- or developer-visible behavior as the reviewed GT entry.
- Test-only, comment-only, documentation-only, helper-refactor, and unsupported security claims were left unmatched.
- Broad generated statements were not mapped to a GT entry unless the release-note-level behavior was explicit.

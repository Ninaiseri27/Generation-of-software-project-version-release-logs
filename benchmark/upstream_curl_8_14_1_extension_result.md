# Upstream curl 8.14.1 Extension Result

Last updated: 2026-05-28

## Case

- Case ID: `curl_8_14_0_to_8_14_1`
- Role: extension/stress evidence, not core-average replacement.
- GT count: `10`
- Stage 1: `121` changed functions across `109` C/C++ files.
- Stage 2 CMG: `115/121` prompt-node matches, `6` unmatched symbols, and `121` entries with fallback context.

## Generation Setup

Command family:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli run-baselines `
  --config configs\benchmark\upstream_curl_8_14_0_to_8_14_1.json `
  --variants text_only diff_only no_graph full `
  --backend openai-compatible `
  --model deepseek-chat `
  --aggregation-strategy rule_family
```

All four variants completed with `0` generation failures.

## Strict Evaluation

| Variant | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 10 | 1 | 1.0000 | 0.1000 | 0.1818 | 0.0000 | 0.1000 | 0.0000 |
| `diff_only` | 10 | 121 | 0.1901 | 0.8000 | 0.3072 | 0.8099 | 2.3000 | 1.5000 |
| `no_graph` | 10 | 118 | 0.2034 | 0.8000 | 0.3243 | 0.7966 | 2.4000 | 1.6000 |
| `full` | 10 | 119 | 0.2017 | 0.8000 | 0.3221 | 0.7983 | 2.4000 | 1.6000 |

Source summaries:

- `benchmark/upstream_curl_8_14_1_evaluation_summary.md`
- `benchmark/upstream_curl_8_14_1_output_summary.md`

## Interpretation

- This case confirms that the pipeline scales to an upstream release with more than one hundred changed functions and can produce structurally valid release notes.
- Recall is high enough to show that source-level evidence captures most reviewed GT topics.
- Precision is low because the model emits many function-local notes for comments, tests, helper refactors, and internal diagnostics that are not release-note-level GT.
- `no_graph` and `full` are slightly above `diff_only` on F1 here, but the difference is small. The stronger conclusion is not that graph context universally wins; it is that richer context does not solve release-note granularity by itself.
- The result supports the thesis limitation and future-work argument: generation needs stronger release-note-level filtering or aggregation, not just more code context.

## Match Policy Notes

- `GT-C003` (`upload from '.'`) and `GT-C008` (`--no-anyauth`) were not force-matched because the generated notes did not state these release-note-level behaviors clearly.
- WebSocket entries were matched only when they described protocol validation, blocked-send/error handling, automatic ping/pong behavior, or diagnostics in `lib/ws.c`.
- WebSocket test-only helpers and debug-only mask forcing were excluded from strict matches.
- Comment-only, spelling-only, build-only, and test-only generated notes were left unmatched.

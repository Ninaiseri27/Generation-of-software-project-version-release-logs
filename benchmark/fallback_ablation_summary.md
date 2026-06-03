# Fallback Context Ablation Summary

This document records the controlled prompt-level fallback-context ablation. It was first run over the reviewed medium benchmark slice and has now been extended to the core5 benchmark set.

The purpose is to isolate fallback evidence from graph evidence:

- `no_graph`: diff plus commit-message evidence, without CMG or fallback context.
- `no_fallback`: diff plus commit-message evidence and ENRE-original CMG only.
- `full`: diff plus commit-message evidence, adaptive CMG, synthetic nodes, diff-derived call edges, and fallback context.

## Implementation

The `no_fallback` prompt variant filters prompt-side graph evidence before prompt construction:

- keeps ENRE-original CMG nodes and ENRE call edges.
- removes synthetic changed nodes.
- removes diff-derived call nodes and edges.
- removes `fallback_context`.
- keeps the same changed-function granularity as `diff_only`, `no_graph`, and `full`.

This means `no_fallback` is stricter than `full` but more informative than `no_graph`.

## Command

```powershell
python -m cpp_release_note_mvp run-baselines `
  --config <case-config.json> `
  --variants no_fallback `
  --backend openai `
  --model deepseek-v4-flash `
  --aggregation-strategy rule_family `
  --output-root <case-output-dir>\ablations\no_fallback\baselines_deepseek_v4_flash `
  --summary-output <case-output-dir>\ablations\no_fallback\baselines_deepseek_v4_flash\baseline_summary.json
```

Then prepare strict-review templates and compute metrics after `matches_strict.json` is filled:

```powershell
python -m cpp_release_note_mvp evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --variants no_fallback `
  --baseline-root-name ablations\no_fallback\baselines_deepseek_v4_flash `
  --matches-filename matches_strict.json `
  --evaluation-filename evaluation_strict.json `
  --match-template-filename match_template_strict.json
```

## Prompt Filtering Smoke Result

The mock smoke run confirmed that filtering is active:

| Case | Entries | Matched | Unmatched | Fallback Entries | Synthetic Entries | Diff-Derived Edges |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | 12 | 10 | 2 | 0 | 0 | 0 |
| `sqlite_v6_0_0_2_to_v6_1` | 42 | 18 | 24 | 0 | 0 | 0 |
| `mbedtls_v6_0_beta1_to_v6_0` | 23 | 6 | 17 | 0 | 0 | 0 |

## Real Backend Output Summary

All `no_fallback` DeepSeek runs completed with `0` failed entries.

| Case | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | 12 | 12 | 12 | 1.0000 | 0.0000 | 10761 |
| `sqlite_v6_0_0_2_to_v6_1` | 42 | 42 | 38 | 0.9048 | 0.0952 | 47113 |
| `mbedtls_v6_0_beta1_to_v6_0` | 23 | 23 | 22 | 0.9565 | 0.0435 | 26161 |

| Variant | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 25.6667 | 24.0000 | 0.9538 | 0.0462 | 28011.6667 |

## Strict Semantic Evaluation

The `matches_strict.json` files have been filled under the same strict rule as the main DeepSeek matrix:

- Helper-only and setup-only notes are not counted as matches.
- Wrong CVE attribution is counted as a strict semantic error even when the function family is related.
- All three evaluation files have `invalid_match_count = 0`.

| Case | Generated | Precision | Recall | F1 | Unsupported Rate | Redundancy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 |
| `sqlite_v6_0_0_2_to_v6_1` | 38 | 0.7368 | 1.0000 | 0.8485 | 0.2632 | 24 |
| `mbedtls_v6_0_beta1_to_v6_0` | 22 | 0.5000 | 0.6667 | 0.5714 | 0.5000 | 7 |

| Variant | Precision | Recall | F1 | Unsupported Rate | Avg Redundancy |
| --- | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 0.7456 | 0.8889 | 0.8066 | 0.2544 | 13.3333 |

## Core5 Extension

The ablation was extended on 2026-05-13 by adding:

- `zlib_v6_0_0_1_to_v6_0_0_2`
- `cjson_v6_0_beta1_to_v6_0`

Summary files:

- `benchmark/fallback_ablation_core5_evaluation_summary.md`
- `benchmark/fallback_ablation_core5_evaluation_summary.json`
- `benchmark/fallback_ablation_core5_output_summary.md`
- `benchmark/fallback_ablation_core5_output_summary.json`

Core5 output summary:

| Variant | Cases | Avg Generated | Avg Final Notes | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 5 | 18.0000 | 17.0000 | 0.0277 | 19032.2000 |

Core5 strict semantic evaluation:

| Variant | Cases | Precision | Recall | F1 | Unsupported Rate | Avg Redundancy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 5 | 0.7928 | 0.9333 | 0.8524 | 0.2072 | 9.4000 |

Core5 comparison against the main baseline matrix:

| Variant | Core5 F1 | Note |
| --- | ---: | --- |
| `diff_only` | 0.9199 | Highest current macro F1, but with high redundancy. |
| `full` | 0.8971 | Better than `no_graph` and `no_fallback`, but still not dominant over `diff_only`. |
| `no_graph` | 0.8533 | Very close to `no_fallback`, showing ENRE-only graph context is not sufficient by itself. |
| `no_fallback` | 0.8524 | Removing fallback/synthetic/diff-derived context weakens the full method. |

## Output-Level Comparison

| Variant | Avg Final Notes | Avg Reduction | Avg Total Tokens | Current Strict F1 |
| --- | ---: | ---: | ---: | ---: |
| `diff_only` | 24.0000 | 0.0397 | 19254.6667 | 0.9405 |
| `no_graph` | 23.3333 | 0.0621 | 25888.6667 | 0.8388 |
| `no_fallback` | 24.0000 | 0.0462 | 28011.6667 | 0.8066 |
| `full` | 22.6667 | 0.0780 | 43661.0000 | 0.8811 |

## Current Interpretation

At the output level, `no_fallback` costs more than `no_graph` because it keeps ENRE graph context, but it compresses less than `full` because it removes synthetic and diff-derived fallback evidence. Semantically, `no_fallback` underperforms both `no_graph` and `full` on this slice, mainly because the mbedtls output keeps many related low-level function summaries but loses enough fallback/contextual signal to preserve the correct CVE grouping.

The core5 extension keeps the same qualitative conclusion: `no_fallback` is almost tied with `no_graph` but remains below `full`. This suggests that ENRE-only graph context is not enough; the useful signal comes from combining graph context with fallback evidence and better aggregation/prompt control.

This supports two thesis-facing points:

- Fallback context is not just extra text; for security changes it can help preserve release-note-level grouping and reduce unsupported low-level claims.
- More context still has a cost: `full` uses substantially more tokens than `no_fallback`, so the result should be reported as a quality/cost tradeoff rather than a free improvement.

## Review Files

Reviewed `matches_strict.json` files live next to each template:

| Case | Template |
| --- | --- |
| `curl_v6_0_beta1_to_v6_0` | `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/ablations/no_fallback/baselines_deepseek_v4_flash/no_fallback/match_template_strict.json` |
| `sqlite_v6_0_0_2_to_v6_1` | `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/ablations/no_fallback/baselines_deepseek_v4_flash/no_fallback/match_template_strict.json` |
| `mbedtls_v6_0_beta1_to_v6_0` | `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/ablations/no_fallback/baselines_deepseek_v4_flash/no_fallback/match_template_strict.json` |

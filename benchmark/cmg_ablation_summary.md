# CMG Ablation Summary

This document records the controlled CMG-strategy ablation. It was first run over the reviewed medium benchmark slice and has now been extended to the core5 benchmark set.

The purpose is to compare:

- `adaptive`: current full pipeline CMG with synthetic nodes and diff-derived call edges.
- `strict_1hop`: ENRE-only 1-hop CMG without synthetic nodes or diff-derived call edges.

## Controlled Setup

All strict-CMG runs reuse the existing `changed_functions.json` and normalized ENRE graphs. This keeps change detection and ENRE output fixed, so only CMG slicing changes.

Example command:

```powershell
python -m cpp_release_note_mvp build-cmg `
  --config configs\benchmark\third_party_curl_v6_0_beta1_to_v6_0.json `
  --cmg-strategy strict_1hop `
  --changed-input outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\changed_functions.json `
  --ref-normalized-graph-input outputs\enre_raw\third_party_curl\OpenHarmony-v6.0-Beta1\third_party_curl__OpenHarmony-v6.0-Beta1_out_normalized.json `
  --tgt-normalized-graph-input outputs\enre_raw\third_party_curl\OpenHarmony-v6.0-Release\third_party_curl__OpenHarmony-v6.0-Release_out_normalized.json `
  --output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\ablations\cmg_strict_1hop\cmg.json
```

Generation uses the same real backend setting as the main DeepSeek matrix:

```powershell
python -m cpp_release_note_mvp run-baselines `
  --config <case-config.json> `
  --variants full `
  --changed-input <case-output>\changed_functions.json `
  --cmg-input <case-output>\ablations\cmg_strict_1hop\cmg.json `
  --backend openai `
  --model deepseek-v4-flash `
  --aggregation-strategy rule_family `
  --output-root <case-output>\ablations\cmg_strict_1hop\baselines_deepseek_v4_flash
```

## CMG Structure Comparison

| Case | Strategy | Entries | Matched | Unmatched | Total Nodes | Total Edges | Entries With Edges | Synthetic Entries | Diff-Derived Call Edges |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `adaptive` | 12 | 10 | 2 | 23 | 11 | 9 | 2 | 11 |
| `curl_v6_0_beta1_to_v6_0` | `strict_1hop` | 12 | 10 | 2 | 10 | 0 | 0 | 0 | 0 |
| `sqlite_v6_0_0_2_to_v6_1` | `adaptive` | 42 | 18 | 24 | 384 | 350 | 38 | 24 | 239 |
| `sqlite_v6_0_0_2_to_v6_1` | `strict_1hop` | 42 | 18 | 24 | 58 | 44 | 9 | 0 | 0 |
| `mbedtls_v6_0_beta1_to_v6_0` | `adaptive` | 23 | 6 | 17 | 68 | 45 | 19 | 17 | 41 |
| `mbedtls_v6_0_beta1_to_v6_0` | `strict_1hop` | 23 | 6 | 17 | 6 | 0 | 0 | 0 | 0 |

## Generation Output Comparison

`adaptive/full` is the already reviewed DeepSeek baseline root. `strict_1hop/full` is the new ablation root under each case's `ablations/cmg_strict_1hop/` directory.

| Strategy | Case | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `adaptive` | `curl_v6_0_beta1_to_v6_0` | 12 | 12 | 1.0000 | 0.0000 | 15146 |
| `adaptive` | `sqlite_v6_0_0_2_to_v6_1` | 42 | 34 | 0.8095 | 0.1905 | 83975 |
| `adaptive` | `mbedtls_v6_0_beta1_to_v6_0` | 23 | 22 | 0.9565 | 0.0435 | 31862 |
| `strict_1hop` | `curl_v6_0_beta1_to_v6_0` | 12 | 12 | 1.0000 | 0.0000 | 14665 |
| `strict_1hop` | `sqlite_v6_0_0_2_to_v6_1` | 42 | 35 | 0.8333 | 0.1667 | 70737 |
| `strict_1hop` | `mbedtls_v6_0_beta1_to_v6_0` | 23 | 22 | 0.9565 | 0.0435 | 29766 |

| Strategy | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| `adaptive` | 25.6667 | 22.6667 | 0.9220 | 0.0780 | 43661.0000 |
| `strict_1hop` | 25.6667 | 23.0000 | 0.9299 | 0.0701 | 38389.3333 |

## Strict Semantic Evaluation

After strict review tightening, both CMG strategies have valid manual match files and `invalid_match_count = 0`.

| Strategy | Case | Precision | Recall | F1 | Unsupported Rate | Redundancy |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `adaptive` | `curl_v6_0_beta1_to_v6_0` | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 |
| `adaptive` | `sqlite_v6_0_0_2_to_v6_1` | 0.7647 | 1.0000 | 0.8667 | 0.2353 | 22 |
| `adaptive` | `mbedtls_v6_0_beta1_to_v6_0` | 0.7273 | 0.8333 | 0.7767 | 0.2727 | 11 |
| `strict_1hop` | `curl_v6_0_beta1_to_v6_0` | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 |
| `strict_1hop` | `sqlite_v6_0_0_2_to_v6_1` | 0.8000 | 1.0000 | 0.8889 | 0.2000 | 24 |
| `strict_1hop` | `mbedtls_v6_0_beta1_to_v6_0` | 0.7273 | 0.8333 | 0.7767 | 0.2727 | 11 |

| Strategy | Precision | Recall | F1 | Unsupported Rate | Avg Redundancy |
| --- | ---: | ---: | ---: | ---: | ---: |
| `adaptive/full` | 0.8307 | 0.9444 | 0.8811 | 0.1693 | 14.0000 |
| `strict_1hop/full` | 0.8424 | 0.9444 | 0.8885 | 0.1576 | 14.6667 |

## Core5 Extension

The ablation was extended on 2026-05-13 by adding:

- `zlib_v6_0_0_1_to_v6_0_0_2`
- `cjson_v6_0_beta1_to_v6_0`

Summary files:

- `benchmark/cmg_strict_1hop_core5_evaluation_summary.md`
- `benchmark/cmg_strict_1hop_core5_evaluation_summary.json`
- `benchmark/cmg_strict_1hop_core5_output_summary.md`
- `benchmark/cmg_strict_1hop_core5_output_summary.json`
- `benchmark/adaptive_full_core5_output_summary.md`
- `benchmark/adaptive_full_core5_output_summary.json`

Core5 strict semantic evaluation:

| Strategy | Cases | Precision | Recall | F1 | Unsupported Rate | Avg Redundancy |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `adaptive/full` | 5 | 0.8439 | 0.9667 | 0.8971 | 0.1561 | 9.8000 |
| `strict_1hop/full` | 5 | 0.8509 | 0.9667 | 0.9015 | 0.1491 | 10.2000 |

Core5 output-level comparison:

| Strategy | Avg Generated | Avg Final Notes | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: |
| `adaptive/full` | 18.0000 | 16.2000 | 0.0468 | 28794.6000 |
| `strict_1hop/full` | 18.0000 | 16.4000 | 0.0420 | 25615.2000 |

## Current Interpretation

The adaptive CMG substantially increases graph context coverage, especially for sqlite and mbedtls where strict ENRE-only matching leaves many entries with no useful graph edges.

The current strict semantic result shows a tradeoff:

- `adaptive` gives slightly stronger aggregation reduction and much richer prompt-side graph evidence.
- `strict_1hop` has lower token cost and slightly higher F1 on this three-case slice, mainly because the sqlite run produced fewer unsupported notes.
- The result does not justify abandoning adaptive CMG. It shows that richer context must be controlled by prompt and aggregation design rather than assumed to improve every metric automatically.

The core5 extension keeps the same conclusion. `strict_1hop/full` is slightly better on macro F1 and token cost, while `adaptive/full` has slightly better final-note reduction. This makes the CMG result a tradeoff rather than a one-sided win: adaptive context is useful for coverage and aggregation, but the prompt/aggregation layer must suppress low-level unsupported claims.

## Reviewed Match Files

The following `matches_strict.json` files have been filled and tightened:

| Case | Template |
| --- | --- |
| `curl_v6_0_beta1_to_v6_0` | `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/ablations/cmg_strict_1hop/baselines_deepseek_v4_flash/full/match_template_strict.json` |
| `sqlite_v6_0_0_2_to_v6_1` | `outputs/benchmark/third_party_sqlite/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/ablations/cmg_strict_1hop/baselines_deepseek_v4_flash/full/match_template_strict.json` |
| `mbedtls_v6_0_beta1_to_v6_0` | `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/ablations/cmg_strict_1hop/baselines_deepseek_v4_flash/full/match_template_strict.json` |

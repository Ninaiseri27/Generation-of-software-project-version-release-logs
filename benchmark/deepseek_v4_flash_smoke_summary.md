# DeepSeek V4 Flash Smoke Summary

This file records the first real-backend baseline matrix after reviewed ground truth and strict/trace evaluation modes were separated.

Generated outputs live under `outputs/` and are intentionally ignored by Git. This tracked document preserves commands, counts, and token usage for reporting.

## Backend

| Field | Value |
| --- | --- |
| Backend adapter | `openai` / OpenAI-compatible HTTP |
| Provider base URL | `https://api.deepseek.com` |
| Model | `deepseek-v4-flash` |
| Thinking mode | disabled through `generation.extra_body.thinking.type = disabled` |
| API key source | `DEEPSEEK_API_KEY` environment variable |

## Command Pattern

```powershell
python -m cpp_release_note_mvp run-baselines `
  --config <benchmark-config.json> `
  --variants text_only diff_only no_graph full `
  --backend openai `
  --model deepseek-v4-flash `
  --aggregation-strategy rule_family `
  --output-root <case-output-dir>\baselines_deepseek_v4_flash `
  --summary-output <case-output-dir>\baselines_deepseek_v4_flash\baseline_summary.json
```

Then evaluate reviewed strict manual-match files:

```powershell
python -m cpp_release_note_mvp evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --variants text_only diff_only no_graph full `
  --baseline-root-name baselines_deepseek_v4_flash `
  --matches-filename matches_strict.json `
  --evaluation-filename evaluation_strict.json `
  --match-template-filename match_template_strict.json `
  --summary-output outputs\benchmark\evaluation_deepseek_v4_flash_all_variants_summary.json
```

## Results

| Case | Variant | Prompt Entries | Generated | Failed | Distilled Notes | Prompt Tokens | Completion Tokens | Total Tokens |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | 1 | 1 | 0 | 1 | 470 | 48 | 518 |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | 12 | 12 | 0 | 12 | 6489 | 723 | 7212 |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | 12 | 12 | 0 | 12 | 9045 | 750 | 9795 |
| `curl_v6_0_beta1_to_v6_0` | `full` | 12 | 12 | 0 | 12 | 14267 | 879 | 15146 |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | 1 | 1 | 0 | 1 | 441 | 41 | 482 |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | 42 | 42 | 0 | 37 | 32545 | 2541 | 35086 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | 42 | 42 | 0 | 36 | 40063 | 2574 | 42637 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | 42 | 42 | 0 | 34 | 81090 | 2885 | 83975 |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | 1 | 1 | 0 | 1 | 672 | 107 | 779 |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | 23 | 23 | 0 | 23 | 14143 | 1323 | 15466 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | 23 | 23 | 0 | 22 | 23573 | 1661 | 25234 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | 23 | 23 | 0 | 22 | 30137 | 1725 | 31862 |

## Strict Evaluation Results

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Redundancy | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 4 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | `evaluated` | 4 | 1 | 1.0000 | 0.2500 | 0.4000 | 0.0000 | 0 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | `evaluated` | 4 | 37 | 0.7297 | 1.0000 | 0.8437 | 0.2703 | 23 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | `evaluated` | 4 | 36 | 0.7500 | 1.0000 | 0.8571 | 0.2500 | 23 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 34 | 0.7647 | 1.0000 | 0.8667 | 0.2353 | 22 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | `evaluated` | 6 | 1 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | `evaluated` | 6 | 23 | 0.9565 | 1.0000 | 0.9778 | 0.0435 | 16 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | `evaluated` | 6 | 22 | 0.5455 | 0.8333 | 0.6593 | 0.4545 | 7 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 22 | 0.7273 | 0.8333 | 0.7767 | 0.2727 | 11 | 1.0000 |

## Macro Averages

| Variant | Precision | Recall | F1 | Unsupported Rate | Avg Redundancy |
| --- | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 0.3333 | 0.0833 | 0.1333 | 0.6667 | 0.0000 |
| `diff_only` | 0.8954 | 1.0000 | 0.9405 | 0.1046 | 16.0000 |
| `no_graph` | 0.7652 | 0.9444 | 0.8388 | 0.2348 | 13.0000 |
| `full` | 0.8307 | 0.9444 | 0.8811 | 0.1693 | 14.0000 |

## Aggregation Summary

The baseline-output summary command records how many function-level generated notes survive into final release-note items after aggregation.

```powershell
python -m cpp_release_note_mvp summarize-baseline-outputs `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --variants text_only diff_only no_graph full `
  --baseline-root-name baselines_deepseek_v4_flash `
  --json-output outputs\benchmark\baseline_outputs_deepseek_v4_flash_summary.json `
  --markdown-output outputs\benchmark\baseline_outputs_deepseek_v4_flash_summary.md
```

| Variant | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 593.0000 |
| `diff_only` | 25.6667 | 24.0000 | 0.9603 | 0.0397 | 19254.6667 |
| `no_graph` | 25.6667 | 23.3333 | 0.9379 | 0.0621 | 25888.6667 |
| `full` | 25.6667 | 22.6667 | 0.9220 | 0.0780 | 43661.0000 |

## CMG Strategy Ablation Smoke

The `build-cmg` command now supports `--cmg-strategy` and artifact inputs, so CMG strategy ablations can reuse existing `changed_functions.json` and normalized ENRE graphs without rerunning ENRE.

Detailed results are tracked in `benchmark/cmg_ablation_summary.md`.
Fallback-context ablation results are tracked in `benchmark/fallback_ablation_summary.md`.

Initial smoke result on `curl_v6_0_beta1_to_v6_0`:

| Strategy | Entries | Matched Entries | Unmatched Entries | Total CMG Nodes | Total CMG Edges | Entries With Edges | Synthetic Entries | Diff-Derived Call Edges |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `strict_1hop` | 12 | 10 | 2 | 10 | 0 | 0 | 0 | 0 |
| `adaptive` | 12 | 10 | 2 | 23 | 11 | 9 | 2 | 11 |

## Interpretation

The real backend is operational for the first reviewed benchmark slice. All twelve runs completed without generation failures, all strict match files have been reviewed and tightened, and all generated notes are structurally valid.

The current results show that `text_only` lacks enough evidence for reliable coverage. `diff_only` reaches the highest macro F1 on this small reviewed slice after strict semantic tightening, while `full` still reduces final-note count under `rule_family` and remains competitive on F1. `no_graph` drops sharply on the security case because several wrong-CVE or helper-only notes are penalized. Treat CMG/fallback context as an evaluated tradeoff rather than an automatically superior setting.

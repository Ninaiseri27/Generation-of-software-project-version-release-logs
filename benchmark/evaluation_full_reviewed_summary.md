# Reviewed Full-Variant Evaluation Summary

This file records the first evaluation run after the three medium benchmark candidates were marked as reviewed.

Generated `evaluation*.json`, `matches_*.json`, and summary JSON files live under `outputs/` and are intentionally ignored by Git. This tracked document preserves the report-facing result and interpretation.

## Ground Truth Scope

| Case | Core GT Entries | Review Decision |
| --- | ---: | --- |
| `curl_v6_0_beta1_to_v6_0` | 4 | Keep all reviewed entries. |
| `sqlite_v6_0_0_2_to_v6_1` | 4 | Keep GT-001 through GT-004; exclude former GT-005 zstd dependency redirection and former GT-006 DFX/logging/debug maintenance entry from P/R/F1. |
| `mbedtls_v6_0_beta1_to_v6_0` | 6 | Keep all reviewed entries. |

## Command

```powershell
python -m cpp_release_note_mvp evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --variants full `
  --matches-filename matches_trace.json `
  --evaluation-filename evaluation_trace.json `
  --summary-output outputs\benchmark\evaluation_full_reviewed_summary.json
```

```powershell
python -m cpp_release_note_mvp summarize-evaluations `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --variants full `
  --evaluation-filename evaluation_trace.json `
  --json-output outputs\benchmark\evaluation_full_reviewed_summary_table.json `
  --markdown-output outputs\benchmark\evaluation_full_reviewed_summary_table.md
```

## Trace-Match Result

Trace matching treats function-level generated entries as matched when they point to code evidence belonging to a ground-truth entry. This mode validates traceability and wiring; it is not final semantic release-note quality.

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Redundancy | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 12 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 9 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 42 | 0.9762 | 1.0000 | 0.9880 | 0.0238 | 37 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 23 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 17 | 1.0000 |

## Strict Semantic Result

Strict matching only accepts generated entries that state the release-note-level behavior. The deterministic mock backend produces function-level traces, so the expected strict result is near zero.

| Case | Variant | Status | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Redundancy | Structural Valid |
| --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 4 | 12 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evaluated` | 4 | 42 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evaluated` | 6 | 23 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0 | 1.0000 |

## Interpretation

This run validates that reviewed ground truth, manual match files, and the evaluator are wired correctly. All three trace evaluations have zero invalid matches after removing sqlite's excluded GT-006 match.

Report `matches_trace.json` results as pipeline traceability only. Report `matches_strict.json` or stricter manually reviewed real-backend matches for final P/R/F1. The high trace redundancy counts are expected and should be used as evidence that later aggregation and strict semantic judging are necessary.

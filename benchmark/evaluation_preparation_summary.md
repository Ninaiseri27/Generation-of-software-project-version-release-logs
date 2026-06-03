# Evaluation Preparation Summary

This file records the first batch evaluation-preparation run for the three medium benchmark candidates.

Generated `evaluation.json` and `match_template.json` files live under `outputs/` and are intentionally ignored by Git.

## Command

```powershell
python -m cpp_release_note_mvp evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --summary-output outputs\benchmark\evaluation_preparation_summary.json
```

## Results

| Case | Variant | Ground Truth | Generated | Status | Structural Valid Rate |
| --- | --- | ---: | ---: | --- | ---: |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | 4 | 1 | `match_required` | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | 4 | 12 | `match_required` | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | 4 | 12 | `match_required` | 1.0000 |
| `curl_v6_0_beta1_to_v6_0` | `full` | 4 | 12 | `match_required` | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | 6 | 1 | `match_required` | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | 6 | 42 | `match_required` | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | 6 | 42 | `match_required` | 1.0000 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | 6 | 42 | `match_required` | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | 6 | 1 | `match_required` | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | 6 | 23 | `match_required` | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | 6 | 23 | `match_required` | 1.0000 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | 6 | 23 | `match_required` | 1.0000 |

## Interpretation

- The evaluation wiring is ready for all current medium candidates and baseline variants.
- The next blocking task is not more pipeline code; it is reviewer matching through `matches.json`.
- `match_required` means no reviewer match file was found for that case and variant.
- Structural validity is already stable for the mock backend, so future differences should focus on semantic precision, recall, unsupported claims, and redundancy.

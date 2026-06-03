# Baseline Smoke Summary

This file records the repeatable P2 baseline smoke tests for the first three medium benchmark candidates.

Generated output artifacts under `outputs/` are intentionally ignored by Git. This summary keeps the experiment commands and counts in the repository.

## Command Pattern

```powershell
python -m cpp_release_note_mvp run-baselines --config <config.json> --backend mock --aggregation-strategy none
```

The command writes:

- `<output_dir>/baselines/baseline_summary.json`
- `<output_dir>/baselines/<variant>/prompt_input.json`
- `<output_dir>/baselines/<variant>/prompt_bundle.json`
- `<output_dir>/baselines/<variant>/release_note.json`
- `<output_dir>/baselines/<variant>/release_note.md`

## Variants

| Variant | Evidence Scope | Granularity |
| --- | --- | --- |
| `text_only` | Project/version metadata, changed files, commit messages | one release-level prompt |
| `diff_only` | Changed-function metadata and diff hunks | one prompt per changed entry |
| `no_graph` | Diff hunks plus commit messages, without CMG/fallback context | one prompt per changed entry |
| `no_fallback` | Diff hunks, commit messages, and ENRE-original CMG only; synthetic and diff-derived fallback evidence removed | one prompt per changed entry |
| `full` | Diff hunks, CMG/fallback context, and commit messages | one prompt per changed entry |

## Results

| Case | Variant | Prompt Entries | Matched | Unmatched | N/A | Generated | Failed | Notes |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | 1 | 0 | 0 | 1 | 1 | 0 | release-level baseline |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | 12 | 10 | 2 | 0 | 12 | 0 | function-level baseline |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | 12 | 10 | 2 | 0 | 12 | 0 | graph removed |
| `curl_v6_0_beta1_to_v6_0` | `full` | 12 | 10 | 2 | 0 | 12 | 0 | full method input |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | 1 | 0 | 0 | 1 | 1 | 0 | release-level baseline |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | 42 | 18 | 24 | 0 | 42 | 0 | function-level baseline |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | 42 | 18 | 24 | 0 | 42 | 0 | graph removed |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | 42 | 18 | 24 | 0 | 42 | 0 | full method input |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | 1 | 0 | 0 | 1 | 1 | 0 | release-level baseline |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | 23 | 6 | 17 | 0 | 23 | 0 | function-level baseline |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | 23 | 6 | 17 | 0 | 23 | 0 | graph removed |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | 23 | 6 | 17 | 0 | 23 | 0 | full method input |

## Interpretation

- The baseline runner is now usable for repeated mock or real-backend experiments.
- `text_only` is intentionally release-level, so its graph match status is not applicable rather than unmatched.
- `diff_only`, `no_graph`, `no_fallback`, and `full` keep the same entry granularity, so later evaluation can compare the effect of adding commit messages, ENRE graph context, and fallback context.
- These are wiring tests using the deterministic mock backend. Final quantitative conclusions should use reviewed ground truth and selected real LLM outputs or a documented evaluation protocol.

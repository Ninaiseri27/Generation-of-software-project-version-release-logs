# cJSON Strict Match Correction

Date: 2026-05-31

This audit tightens the final strict-match labels for `cjson_v6_0_beta1_to_v6_0`.

## Policy

- Remove matches where the generated note is only a test/helper note but is matched to `GT-001`, which is a runtime reliability fix for `cJSON_Duplicate`.
- Remove the `parse_number` null-termination cleanup match to `GT-002`, because that cleanup is explicitly excluded as a standalone ground-truth fact.
- Keep parser-regression test matches to `GT-002`, because `GT-002` is explicitly defined as a testing/regression-coverage entry.

## Removed Matches

| Method | Removed | New P | New R | New F1 | Reason |
| --- | ---: | ---: | ---: | ---: | --- |
| `diff_only` | 2 | 0.4545 | 1.0000 | 0.6250 | Test-only circular-reference notes were mapped to runtime `GT-001`. |
| `full_adaptive_rule_family` | 2 | 0.5455 | 1.0000 | 0.7059 | Test-only circular-reference notes were mapped to runtime `GT-001`. |
| `full_no_fallback` | 2 | 0.5455 | 1.0000 | 0.7059 | Test-only circular-reference notes were mapped to runtime `GT-001`. |
| `full_strict_1hop` | 2 | 0.5455 | 1.0000 | 0.7059 | Test-only circular-reference notes were mapped to runtime `GT-001`. |
| `full_similarity_family` | 1 | 0.5714 | 1.0000 | 0.7273 | Excluded `parse_number` cleanup was mapped to `GT-002`. |
| `full_evidence_similarity_family` | 2 | 0.5000 | 1.0000 | 0.6667 | Test-only circular-reference notes were mapped to runtime `GT-001`. |

## Result Impact

- The cJSON case still keeps recall `1.0000` for all affected evidence-rich variants.
- Precision and F1 decrease because previously counted test-only helper matches are now treated as unsupported for the runtime reliability GT.
- The final 82-GT and expanded 137-GT matrices have been refreshed after this correction.

## Machine-Readable Record

- `benchmark/cjson_strict_match_correction_2026_05_31.json`

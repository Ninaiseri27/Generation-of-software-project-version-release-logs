# Evaluation Smoke Summary

This file records the first P3 evaluation smoke test.

## Case

- Case: `curl_v6_0_beta1_to_v6_0`
- Variant: `full`
- Backend: `mock`
- Aggregation strategy: `none`
- Ground truth: `benchmark/cases/third_party_curl/curl_v6_0_beta1_to_v6_0/ground_truth.md`
- Generated output: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines/full/release_note.json`
- Match file: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines/full/matches_strict_empty.json`

## Command

```powershell
python -m cpp_release_note_mvp evaluate-release-notes `
  --ground-truth benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\ground_truth.md `
  --release-note outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\baselines\full\release_note.json `
  --matches outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\baselines\full\matches_strict_empty.json `
  --output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\baselines\full\evaluation_strict_empty.json
```

## Result

| Metric | Value |
| --- | ---: |
| Ground-truth entries | 4 |
| Generated entries | 12 |
| Valid matches | 0 |
| Precision | 0.0000 |
| Recall | 0.0000 |
| F1 | 0.0000 |
| Unsupported-claim count | 12 |
| Unsupported-claim rate | 1.0000 |
| Structural-valid count | 12 |
| Structural-valid rate | 1.0000 |

## Interpretation

The deterministic mock backend produced structurally valid JSON notes, but the notes mostly say that individual functions were added or updated. Under the strict semantic matching rule, those function-level descriptions do not cover the reviewed release-note ground truth such as OHOS network handover, MMS default-port preservation, HTTP header-count limiting, or FTP parser hardening.

This result is expected and useful: it validates the evaluation workflow while showing that mock generation should remain a wiring test, not a quality baseline for thesis conclusions.

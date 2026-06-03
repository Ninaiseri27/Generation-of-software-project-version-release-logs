# P2 Recent Screening Summary

Last updated: 2026-05-17

This note records the P2 benchmark-extension screening run after the core5 result scope was stabilized.

## Commands

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli screen-version-pairs `
  --config configs\benchmark\third_party_pcre2_v6_0_beta1_to_v6_0.json `
  --recent-pairs 8 `
  --output outputs\screening\third_party_pcre2_recent8.json

python -m cpp_release_note_mvp.cli screen-version-pairs `
  --config configs\benchmark\third_party_jsoncpp_v6_0_beta1_to_v6_0.json `
  --recent-pairs 8 `
  --output outputs\screening\third_party_jsoncpp_recent8.json

python -m cpp_release_note_mvp.cli screen-version-pairs `
  --config configs\benchmark\third_party_libjpeg_turbo_v6_0_beta1_to_v6_0.json `
  --recent-pairs 8 `
  --output outputs\screening\third_party_libjpeg_turbo_recent8.json
```

## Result

| Repository | Screened Pairs | Direct Large | Direct Medium/Small | Patch-Only | Empty/Metadata | Decision |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| `third_party_pcre2` | 8 | 2 | 0 | 2 | 4 | Keep as stress-test candidate only. |
| `third_party_jsoncpp` | 8 | 0 | 0 | 3 | 5 | Keep as patch-challenge/metadata case. |
| `third_party_libjpeg-turbo` | 8 | 0 | 0 | 5 | 3 | Keep as patch-challenge case. |

Important candidate:

| Case | Commits | Changed Files | Changed C/C++ Files | Changed Functions | Bucket | Decision |
| --- | ---: | ---: | ---: | ---: | --- | --- |
| `pcre2_v5_0_3_to_v5_1_0` | 10 | 256 | 70 | 981 | `large` | Possible stress case, older release line. |
| `pcre2_v6_0_0_2_to_v6_1` | 12 | 360 | 77 | 1123 | `large` | Preferred stress candidate because it is on the current v6 line. |

## Interpretation

The screening result supports the current benchmark policy:

- Do not add `jsoncpp` or `libjpeg-turbo` to the direct-source core matrix under the current method. Their recent pairs are patch-only or metadata-only, so they require patch-aware extraction before fair comparison.
- Do not run full pcre2 ENRE/LLM generation by default. The `pcre2_v6_0_0_2_to_v6_1` pair has 1123 changed functions, which is useful for scalability or stress analysis but too large for full manual GT and strict matching without sampling.
- Keep core5 as the main thesis matrix. Use pcre2 only if a separate sampled/stress protocol is explicitly introduced.

## Next Gate

The pcre2 sampled gate has now passed:

1. Fixed sampling protocol is defined.
2. Evidence packet is generated only for the sampled scope.
3. Reviewed sampled GT-S01 through GT-S05 is separated into `ground_truth_strict.md`.
4. Real DeepSeek generation and strict matching are complete.
5. The case remains stress-test evidence and is not included in the core5 average.

## Sampled Stress Protocol

The first deterministic pcre2 sample has been materialized:

- Full input: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/changed_functions.json`
- Sampled input: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_changed_functions.json`
- Sample summary: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_changed_functions_summary.md`
- Evidence packet: `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/evidence.md`
- Source functions: `1123`
- Sampled functions: `80`
- Sampled files: `62`
- Strategy: `stratified_file_round_robin`
- Max per file: `5`

The sample is deterministic and file-stratified. It ranks files by changed-function volume and diff size, ranks functions within files by diff size and hunk count, then performs round-robin selection across ranked files. This preserves cross-file coverage and prevents a few large files from dominating the stress evidence packet.

This sample is allowed for evidence drafting and stress analysis. It is not allowed to change the core5 average unless the thesis explicitly introduces sampled-stress metrics.

The evidence packet has been generated from the sampled input, and sampled GT entries are recorded in `ground_truth.md`. The default sampled strict-evaluation set is GT-S01 through GT-S05. GT-S06 and GT-S07 are retained as optional stress notes but excluded from sampled P/R/F1 unless they are split and reviewed separately.

Sampled Stage 2/3 smoke execution is complete:

- sampled CMG: `80` entries, `49` matched, `31` unmatched, `80` fallback-context entries.
- sampled mock baselines: `text_only=1`, `diff_only=80`, `no_graph=80`, `full=80`; all generated with `0` failures.
- sampled DeepSeek baselines on `deepseek-chat`: `text_only=1`, `diff_only=80`, `no_graph=80`, `no_fallback=80`, `full=80`; all generated with `0` failures.
- sampled strict evaluation over GT-S01 through GT-S05: `full` recall is `1.0000`, but precision is only `0.0759` because the sampled run emits many low-level internal/JIT/backend notes.
- detailed note: `benchmark/pcre2_sampled_stress_analysis.md`.

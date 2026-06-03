# Core6 Candidate Audit: curl_v6_0_to_v6_0_0_1

Last updated: 2026-05-16

This note records the controlled admission status for `third_party_curl`
`OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release`.

## Decision

Keep this case as a `core6_candidate`, not as an admitted `core_eval` case yet.

Reasons:

- The case has useful scale: 47 changed functions across 17 C/C++ files.
- The drafted GT entries cover a coherent security and network/TLS feature cluster.
- Real DeepSeek outputs and strict evaluations now exist for `text_only`, `diff_only`, `no_graph`, and `full`.
- The current strict results are useful for stress analysis, but not strong enough for direct core admission because no evidence-rich variant covers GT-001 and all evidence-rich variants remain highly redundant.

## Ground Truth Status

Current GT status remains `draft_candidate`.

Drafted semantic entries:

| GT ID | Topic | Source Strength | Current Decision |
| --- | --- | --- | --- |
| `GT-001` | CVE-2025-9086 cookie path hardening. | Strong | Keep. The wording must stay tied to secure-cookie path comparison and out-of-bounds read behavior. |
| `GT-002` | OpenHiTLS/TLCP 1.1 backend support. | Medium | Keep as a candidate. It is supported by OpenHarmony commits and broad backend diffs, but no independent upstream release-note entry has been mapped. |
| `GT-003` | TLCP encrypted certificate/key options through libcurl and CLI. | Medium | Keep separate from GT-002. It represents user/developer-facing API and CLI exposure rather than only backend implementation. |

## Available Artifacts

Pipeline artifacts:

- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/changed_functions.json`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/cmg.json`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/prompt_bundle.json`

Real baseline artifacts:

- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/baselines_deepseek_v4_flash/<variant>/release_note.json`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/baselines_deepseek_v4_flash/<variant>/matches_strict.json`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/baselines_deepseek_v4_flash/<variant>/evaluation_strict.json`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/evaluation_deepseek_v4_flash_table.md`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/baseline_output_deepseek_v4_flash_table.md`
- `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/aggregation_deepseek_v4_flash_table.md`
- `benchmark/core6_candidate_stress_analysis.md`

## Current Real-Backend Result

Strict evaluation with `deepseek-v4-flash`:

| Variant | GT | Generated | Final Notes | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 3 | 1 | 1 | 1.0000 | 0.3333 | 0.5000 | 0.0000 | 0.3333 | 0.0000 | 561 |
| `diff_only` | 3 | 47 | 47 | 0.6596 | 0.6667 | 0.6631 | 0.3404 | 10.3333 | 9.6667 | 30450 |
| `no_graph` | 3 | 45 | 45 | 0.6222 | 0.6667 | 0.6437 | 0.3778 | 9.3333 | 8.6667 | 42926 |
| `full` | 3 | 47 | 47 | 0.4681 | 0.6667 | 0.5500 | 0.5319 | 7.3333 | 6.6667 | 73440 |

Interpretation:

- `text_only` covers only GT-001 by exact CVE identifier and misses the two OpenHiTLS/TLCP feature entries.
- `diff_only`, `no_graph`, and `full` cover GT-002 and GT-003, but do not cover GT-001 under strict semantics.
- `diff_only` is the best variant on this candidate (`F1=0.6631`) and has lower token cost than `no_graph` and `full`.
- `full` has the highest token cost and the lowest F1 among evidence-rich variants, which supports the existing thesis observation that extra context can introduce noise.
- Evidence-rich variants are highly redundant: `diff_only` has `Extra/GT=9.6667`, `no_graph` has `8.6667`, and `full` has `6.6667`.
- Incorrect CVE attributions in evidence-rich outputs are intentionally left unmatched and should be cited as unsupported security-claim examples.
- Aggregation stress analysis shows that `rule_family` is too weak on this case, while `similarity_family` can reduce `full` from 47 notes to 25 and `evidence_similarity_family` reduces it to 37 with stronger traceability.

## Next Controlled Steps

Do not merge this case into the main core matrix until these steps are complete:

1. Decide whether the three GT entries should be marked `reviewed`.
2. Decide whether the strict match policy for CVE-only generated notes is acceptable for final reporting.
3. Compare this candidate with the core5 matrix as a secondary stress case.
4. Admit as `core6` only if the thesis needs larger external-validity evidence and the added redundancy/noise is explicitly discussed.

Executed command for the missing real variants:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli run-baselines `
  --config configs\third_party_curl_v6_0_to_v6_0_0_1_deepseek.json `
  --variants text_only diff_only no_graph `
  --backend openai `
  --model deepseek-v4-flash `
  --aggregation-strategy rule_family `
  --output-root outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash `
  --summary-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash\baseline_summary_missing_variants.json
```

Executed command for strict evaluation:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_to_v6_0_0_1\metadata.json `
  --variants text_only diff_only no_graph full `
  --baseline-root-name baselines_deepseek_v4_flash `
  --matches-filename matches_strict.json `
  --evaluation-filename evaluation_strict.json `
  --match-template-filename match_template_strict.json `
  --summary-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\evaluation_deepseek_v4_flash_summary.json
```

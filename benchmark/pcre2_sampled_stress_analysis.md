# PCRE2 Sampled Stress Analysis

Last updated: 2026-05-17

This document records the sampled stress pipeline for
`third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release`.

The case is not part of `core_eval`. It is a secondary stress case used to test
whether the pipeline can handle a large direct-source update through a fixed
sampling protocol.

## Position

| Item | Value |
| --- | --- |
| Case ID | `pcre2_v6_0_0_2_to_v6_1` |
| Repository | `third_party_pcre2` |
| Version Pair | `OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release` |
| Full Changed Functions | 1123 |
| Full Changed C/C++ Files | 77 |
| Sampled Functions | 80 |
| Sampled Files | 62 |
| Default Sampled GT | GT-S01 through GT-S05 |
| Optional/Excluded GT | GT-S06 and GT-S07 |
| Current Role | sampled stress case |

## Sampling Result

Sampling command:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli sample-changed-functions `
  --input outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\changed_functions.json `
  --output outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_changed_functions.json `
  --summary-output outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_changed_functions_summary.md `
  --max-functions 80 `
  --max-per-file 5
```

Result:

| Metric | Value |
| --- | ---: |
| Source functions | 1123 |
| Sampled functions | 80 |
| Sampled files | 62 |
| Added functions | 9 |
| Deleted functions | 48 |
| Modified functions | 23 |

The sampler uses deterministic file-stratified round-robin selection. It ranks
files by changed-function count and diff size, ranks functions by diff size and
hunk count, and caps each file at five sampled functions.

## ENRE And Normalization

ENRE was run on both full version snapshots. The sampled CMG then reuses the
normalized graphs while using only `sampled_changed_functions.json` as the
changed-function input.

| Graph | Raw Entities | Normalized Function Entities | Raw Relations | Normalized Call Relations |
| --- | ---: | ---: | ---: | ---: |
| ref | 12989 | 958 | 52387 | 201 |
| tgt | 5019 | 243 | 21138 | 204 |

The large ref/tgt graph difference reinforces why this case should be treated as
a stress case rather than a normal core-eval case.

## Sampled CMG Result

| Metric | Value |
| --- | ---: |
| Sampled entries | 80 |
| Matched entries | 49 |
| Unmatched entries | 31 |
| Unique unmatched symbols | 24 |
| Fallback-context entries | 80 |
| Synthetic entries | 31 |
| Diff-derived call edges | 764 |

Interpretation:

- The sampled CMG has moderate ENRE match coverage: `49/80` sampled entries.
- Fallback context covers all sampled entries, so prompt construction remains complete even for unmatched functions.
- The high `diff_call_edge_count` suggests pcre2 contains dense local call evidence in the sampled functions.

## Sampled Stage 3 Mock Result

Prompt generation and mock generation were run to validate the sampled stress wiring. Mock output is not a quality result.

| Variant | Prompt Entries | Generated | Failed | Final Notes |
| --- | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1 | 0 | 1 |
| `diff_only` | 80 | 80 | 0 | 58 |
| `no_graph` | 80 | 80 | 0 | 58 |
| `full` | 80 | 80 | 0 | 58 |

Standalone `full` mock run:

| Metric | Value |
| --- | ---: |
| Prompt entries | 80 |
| Generated entries | 80 |
| Failed entries | 0 |
| Final notes after `rule_family` | 58 |

## Real DeepSeek Sampled Result

Real generation was run with `deepseek-chat` on the fixed 80-function sample.
This is still a sampled stress experiment and must not be averaged into core5.

Command:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli run-baselines `
  --config configs\benchmark\third_party_pcre2_v6_0_0_2_to_v6_1.json `
  --variants text_only diff_only no_graph no_fallback full `
  --changed-input outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_changed_functions.json `
  --cmg-input outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_cmg.json `
  --backend openai `
  --model deepseek-chat `
  --aggregation-strategy rule_family `
  --output-root outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_baselines_deepseek_chat `
  --summary-output outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_baselines_deepseek_chat\baseline_summary.json
```

Result:

| Variant | Prompt Entries | Generated | Failed | Final Notes | Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1 | 0 | 1 | 796 |
| `diff_only` | 80 | 80 | 0 | 78 | 244504 |
| `no_graph` | 80 | 80 | 0 | 79 | 283732 |
| `no_fallback` | 80 | 80 | 0 | 79 | 289843 |
| `full` | 80 | 80 | 0 | 79 | 346520 |

The full variant has the highest context cost. The generated-note count remains
near one note per sampled function, which means this case is useful for testing
redundancy and aggregation pressure.

## Strict Sampled Evaluation

Strict evaluation uses only GT-S01 through GT-S05 from
`ground_truth_strict.md`. GT-S06 and GT-S07 remain excluded by default.

Summary:

| Variant | GT | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 5 | 1 | 1.0000 | 0.2000 | 0.3333 | 0.0000 | 0.2000 | 0.0000 |
| `diff_only` | 5 | 78 | 0.0513 | 0.8000 | 0.0964 | 0.9487 | 1.2000 | 0.4000 |
| `no_graph` | 5 | 79 | 0.0633 | 0.6000 | 0.1145 | 0.9367 | 1.0000 | 0.4000 |
| `no_fallback` | 5 | 79 | 0.0633 | 0.8000 | 0.1173 | 0.9367 | 1.4000 | 0.6000 |
| `full` | 5 | 79 | 0.0759 | 1.0000 | 0.1412 | 0.9241 | 1.6000 | 0.6000 |

Interpretation:

- `full` reaches the highest recall on the sampled GT set, but precision remains low because the sample still generates many low-level JIT/backend/internal notes.
- GT-S01 is only weakly recovered as a broad PCRE2 10.46 update; no variant generated a precise CVE-2025-58050 security note.
- The result supports using pcre2 as a stress case for scale, redundancy, and context-cost analysis, not as a normal quality row.

## Aggregation Stress Observation

Aggregation comparison can be computed from the same generated entries without
rerunning the LLM:

| Variant | Strategy | Final Notes | Compression | Reduction | Max Group Size |
| --- | --- | ---: | ---: | ---: | ---: |
| `diff_only` | `rule_family` | 78 | 0.9750 | 0.0250 | 2 |
| `diff_only` | `similarity_family` | 49 | 0.6125 | 0.3875 | 4 |
| `diff_only` | `evidence_similarity_family` | 55 | 0.6875 | 0.3125 | 4 |
| `full` | `rule_family` | 79 | 0.9875 | 0.0125 | 2 |
| `full` | `similarity_family` | 46 | 0.5750 | 0.4250 | 4 |
| `full` | `evidence_similarity_family` | 54 | 0.6750 | 0.3250 | 4 |

During this review, the original `rule_family` logic showed a concrete
overfitting bug: a generic testing helper entry could be renamed as a sqlite
database-corruption utility. The rule has been tightened so the database helper
family requires database-corruption evidence rather than any generic helper
wording.

## Ground Truth Scope

The default sampled GT set is:

- GT-S01: PCRE2 10.46 / CVE-2025-58050 read-past-end fix.
- GT-S02: 10.45 pattern-syntax features.
- GT-S03: Unicode, case-handling, and escape-parsing behavior.
- GT-S04: API controls and JIT unsupported-feature reporting.
- GT-S05: substitution replacement extensions.

GT-S06 and GT-S07 are intentionally excluded from sampled P/R/F1 by default:

- GT-S06 mixes JIT performance, generated-code size, SLJIT submodule/build integration, and architecture backend details.
- GT-S07 is partly tooling/test behavior and can make strict release-note matching inconsistent.

## Current Decision

Do not merge this case into core5 or a core6 average.

The real DeepSeek sampled run and strict matching are complete, but they should
remain separate sampled-stress evidence. The thesis can use it to discuss
scalability, sampling, fallback coverage, large-update noise, and aggregation
pressure, but not as a direct replacement for the reviewed core5 matrix.

## Key Artifacts

- `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/ground_truth.md`
- `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/ground_truth_strict.md`
- `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/matches_strict_deepseek_chat/`
- `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/evidence.md`
- `benchmark/pcre2_sampled_deepseek_evaluation_summary.md`
- `benchmark/pcre2_sampled_deepseek_output_summary.md`
- `benchmark/pcre2_sampled_deepseek_aggregation_summary.md`
- `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_changed_functions.json`
- `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_cmg.json`
- `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_prompt_bundle.json`
- `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_baselines_mock/baseline_summary.json`
- `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_baselines_deepseek_chat/`

# Evaluation Protocol

This document defines the first usable P3 evaluation workflow.

The project uses manually reviewed semantic matches between generated release-note entries and ground-truth entries. This follows the benchmark design principle that release-note correctness is semantic and evidence-based, not a verbatim string match.

## Inputs

Required files:

- `ground_truth.md`: reviewed or drafted semantic ground-truth entries.
- `release_note.json`: generated release-note output for one method variant.

Optional file:

- `matches_strict.json`: manual strict semantic matches for final-quality evaluation.
- `matches_trace.json`: optional trace/evidence matches for pipeline debugging.
- `matches.json`: legacy/default filename; avoid using it for final reports unless its matching rule is explicitly documented.

## Prepare A Match Template

```powershell
python -m cpp_release_note_mvp evaluate-release-notes `
  --ground-truth benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\ground_truth.md `
  --release-note outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\baselines\full\release_note.json `
  --output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\baselines\full\evaluation.json `
  --match-template-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\baselines\full\match_template.json
```

The template contains:

- ground-truth entries with `GT-*` IDs.
- generated entries with `GEN-*` IDs.
- an editable `matches` list.

## Fill Manual Matches

Example:

```json
{
  "matches": [
    {
      "generated_id": "GEN-001",
      "gt_id": "GT-001",
      "decision": "match",
      "notes": "Generated entry covers the OHOS handover option and socket binding behavior."
    }
  ]
}
```

Only `decision = match` contributes to precision and recall. Unsupported or uncertain generated notes should be left unmatched.

Use the following distinction when reviewing outputs:

- Strict semantic match: the generated entry states the user/developer-visible change captured by the ground-truth entry. This is the preferred mode for final thesis results.
- Trace/evidence match: the generated entry names a function or test that is evidence for a ground-truth entry, but does not explain the release-note-level behavior. This is useful for wiring checks, but should not be treated as final release-note quality.

## Compute Metrics

```powershell
python -m cpp_release_note_mvp evaluate-release-notes `
  --ground-truth <case>\ground_truth.md `
  --release-note <variant>\release_note.json `
  --matches <variant>\matches.json `
  --output <variant>\evaluation.json
```

Metrics:

- Precision: matched generated notes / total generated notes.
- Recall: matched ground-truth entries / total ground-truth entries.
- F1: harmonic mean of precision and recall.
- Unsupported-claim count/rate: generated notes without a valid ground-truth match.
- Redundancy count: extra generated notes that map to an already matched ground-truth entry.
- Structural validity: generated notes with non-empty `section`, `title`, and `summary`.

## Batch Baseline Evaluation

After `run-baselines` has produced baseline outputs, prepare evaluation files for all variants with:

```powershell
python -m cpp_release_note_mvp evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --summary-output outputs\benchmark\evaluation_preparation_summary.json
```

For each case and variant, this writes:

- `<output_dir>/baselines/<variant>/evaluation.json`
- `<output_dir>/baselines/<variant>/match_template.json`

If `<output_dir>/baselines/<variant>/matches.json` exists, metrics are computed. Otherwise, the evaluation status remains `match_required`.

Prefer explicit filenames once both matching modes are used:

```powershell
python -m cpp_release_note_mvp evaluate-baselines `
  --metadata <case>\metadata.json `
  --variants full `
  --matches-filename matches_strict.json `
  --evaluation-filename evaluation_strict.json
```

## Summarize Evaluations

```powershell
python -m cpp_release_note_mvp summarize-evaluations `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --json-output outputs\benchmark\evaluation_summary.json `
  --markdown-output outputs\benchmark\evaluation_summary.md
```

This produces a report-facing table with status, ground-truth count, generated count, precision, recall, F1, unsupported-claim rate, redundancy count, and structural validity.

## Summarize Baseline Outputs

Use this command before or alongside semantic evaluation when the goal is to compare generation cost and aggregation behavior:

```powershell
python -m cpp_release_note_mvp summarize-baseline-outputs `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_beta1_to_v6_0\metadata.json `
             benchmark\cases\third_party_sqlite\sqlite_v6_0_0_2_to_v6_1\metadata.json `
             benchmark\cases\third_party_mbedtls\mbedtls_v6_0_beta1_to_v6_0\metadata.json `
  --baseline-root-name baselines_deepseek_v4_flash `
  --json-output outputs\benchmark\baseline_outputs_deepseek_v4_flash_summary.json `
  --markdown-output outputs\benchmark\baseline_outputs_deepseek_v4_flash_summary.md
```

This produces a report-facing table with generated entry count, final release-note count, aggregation compression, aggregation reduction, and token usage.

Use the compression and reduction columns to discuss whether a method reduces function-level redundancy:

- Compression: final release-note count / generated entry count.
- Reduction: 1 - compression.

## CMG Strategy Ablation

For CMG strategy ablation, reuse existing `changed_functions.json` and normalized ENRE graph files so only CMG slicing changes. This avoids rerunning ENRE and keeps the comparison controlled.

Example for the curl medium case:

```powershell
python -m cpp_release_note_mvp build-cmg `
  --config configs\benchmark\third_party_curl_v6_0_beta1_to_v6_0.json `
  --cmg-strategy strict_1hop `
  --changed-input outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\changed_functions.json `
  --ref-normalized-graph-input outputs\enre_raw\third_party_curl\OpenHarmony-v6.0-Beta1\third_party_curl__OpenHarmony-v6.0-Beta1_out_normalized.json `
  --tgt-normalized-graph-input outputs\enre_raw\third_party_curl\OpenHarmony-v6.0-Release\third_party_curl__OpenHarmony-v6.0-Release_out_normalized.json `
  --output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release\ablations\cmg_strict_1hop\cmg.json
```

Then run `run-baselines` with `--cmg-input` pointing to the ablation CMG file and a separate `--output-root`. Use the same backend/model and variants as the adaptive run.

## Fallback Context Ablation

Use the `no_fallback` prompt variant to isolate fallback evidence from ENRE graph evidence. It keeps changed-function metadata, diff hunks, commit messages, and ENRE-original CMG nodes/edges, but filters synthetic changed nodes, diff-derived call edges, and `fallback_context`.

```powershell
python -m cpp_release_note_mvp run-baselines `
  --config <case-config.json> `
  --variants no_fallback `
  --backend openai `
  --model deepseek-v4-flash `
  --aggregation-strategy rule_family `
  --output-root <case-output-dir>\ablations\no_fallback\baselines_deepseek_v4_flash `
  --summary-output <case-output-dir>\ablations\no_fallback\baselines_deepseek_v4_flash\baseline_summary.json
```

After generation, run `evaluate-baselines` with `--variants no_fallback` to create strict match templates. Fill `matches_strict.json` before reporting P/R/F1.

## Current Limitation

This workflow does not perform automatic semantic judging. That is intentional for the first evaluation stage: generated release notes should be matched by a reviewer using the evidence packet and ground truth.

The deterministic `mock` backend usually produces function-level entries such as "Updated Foo". Those entries may be traceable to ground truth, but they are often not strict semantic release notes. Report mock evaluations as pipeline validation unless the match file was filled under the strict semantic rule.

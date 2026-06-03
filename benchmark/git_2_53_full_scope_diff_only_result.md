# Git 2.53 Full-Scope diff_only Result

Generated on: 2026-05-29

This report records the first full-scope real-backend run for `upstream_git v2.52.0 -> v2.53.0` against the expanded 39-entry full-scope GT candidate.

## Inputs

| Item | Path |
| --- | --- |
| Full-scope GT candidate | `benchmark/cases/upstream_git/git_2_52_0_to_2_53_0/ground_truth_full_candidate.md` |
| Full changed functions | `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/changed_functions.json` |
| Full CMG | `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/cmg.json` |
| Full `diff_only` prompt bundle | `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/prompt_bundle_diff_only.json` |

## Generation

Command:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli generate-release-notes `
  --config configs/benchmark/upstream_git_2_52_0_to_2_53_0.json `
  --prompt-bundle-input outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/prompt_bundle_diff_only.json `
  --json-output outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note.json `
  --markdown-output outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note.md `
  --backend openai `
  --model deepseek-chat `
  --aggregation-strategy rule_family
```

Result:

| Metric | Value |
| --- | ---: |
| Prompt entries | 905 |
| Generated entries | 905 |
| Failed entries | 0 |
| Rule-family final notes | 878 |
| Backend | `openai` compatible DeepSeek endpoint |
| Model | `deepseek-chat` |

Output paths:

- `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note.json`
- `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note.md`

## Strict Matching

A lexical/symbol candidate-review packet was generated to make the 878-note output reviewable:

- `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/match_review_candidates.json`
- `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/match_review_candidates.md`

The first `matches_strict.json` is conservative. It records only generated entries that directly support a GT entry and intentionally leaves several weakly generated GT items unmatched.

Evaluation command:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli evaluate-release-notes `
  --ground-truth benchmark/cases/upstream_git/git_2_52_0_to_2_53_0/ground_truth_full_candidate.md `
  --release-note outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note.json `
  --matches outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/matches_strict.json `
  --output outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/evaluation_strict.json
```

Strict result:

| Metric | Value |
| --- | ---: |
| GT entries | 39 |
| Generated final notes | 878 |
| Valid matches | 80 |
| Matched generated notes | 80 |
| Matched GT entries | 33 |
| Precision | 0.0911 |
| Recall | 0.8462 |
| F1 | 0.1645 |
| Unsupported claim rate | 0.9089 |
| Avg matches per GT | 2.0513 |
| Extra/GT | 1.2051 |
| Structural valid rate | 1.0000 |

Unmatched GT under the conservative review:

- `GT-G216`: generated notes mention replay/onto setup but not the specific bad `--onto` diagnostic clearly.
- `GT-G219`: generated notes mention `spanhash`/`MEMZERO_ARRAY` but not the artificial-filepair memory/speed claim clearly.
- `GT-G222`: generated notes remove `mktemp` or fix a test-helper leak but do not state insecure `mktemp`/TOCTOU risk.
- `GT-G223`: generated notes mention promisor handling but not blob-parsing enumeration optimization clearly.
- `GT-G227`: generated notes add config-unset options but do not state help-text correction.
- `GT-G237`: generated notes mention MIDX cleanup/rewrite but not wrong-checksum reuse clearly.

## Aggregation Check

The same generated entries were re-aggregated with `similarity_family` without another LLM call.

Command:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli rewrite-aggregation `
  --input outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note.json `
  --aggregation-strategy similarity_family `
  --json-output outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note_similarity_family.json `
  --markdown-output outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/diff_only/release_note_similarity_family.md
```

Result:

| Aggregation | Final notes | Reduction from 905 generated entries |
| --- | ---: | ---: |
| `rule_family` | 878 | 2.98% |
| `similarity_family` | 510 | 43.65% |

The similarity aggregation result still needs its own strict-match file because generated IDs and merged note content differ after aggregation.

Projected strict matching was then derived from the conservative rule-family matches through `source_entry_ids`. This is a draft projection, not a final human-audited match file.

Projected similarity-family strict result:

| Metric | Value |
| --- | ---: |
| GT entries | 39 |
| Generated final notes | 510 |
| Valid matches | 67 |
| Matched generated notes | 66 |
| Matched GT entries | 33 |
| Precision | 0.1294 |
| Recall | 0.8462 |
| F1 | 0.2245 |
| Unsupported claim rate | 0.8706 |
| Avg matches per GT | 1.7179 |
| Extra/GT | 0.8718 |
| Structural valid rate | 1.0000 |

## Interpretation

Full-scope `diff_only` confirms that the method can scale to a 905-function release pair with no LLM failures. It also shows why full-scope benchmark expansion must be evaluated carefully:

- Recall is high, so function-level diff evidence can cover many official release-note facts.
- Precision is very low because one function-level note is generated for nearly every changed function.
- Redundancy remains high even under conservative matching.
- Aggregation becomes necessary at full-release scale; rule-based aggregation is too weak for this case, while similarity aggregation substantially reduces output size and improves F1 from `0.1645` to `0.2245` under the draft projected match file.

Recommended next step:

1. Audit the conservative `matches_strict.json` once more before thesis use.
2. Audit `matches_strict_similarity_family.json`, because it is currently projected from `source_entry_ids` rather than manually judged note by note.
3. Run `full_strict_1hop` or `full` real generation only if the similarity-aggregated `diff_only` result remains useful after strict evaluation.

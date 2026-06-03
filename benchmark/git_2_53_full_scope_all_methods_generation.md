# Git 2.53 Full-Scope All-Method Generation

Generated on: 2026-05-29

This report records the full-scope generation coverage for `upstream_git v2.52.0 -> v2.53.0`. It intentionally reports generation scale and artifact readiness only. Method-quality conclusions should wait until strict matches are completed for all variants.

## Scope

| Item | Value |
| --- | ---: |
| Full changed functions | 905 |
| Full-scope GT candidates | 39 |
| CMG prompt-node matches | 900 |
| CMG unmatched entries | 5 |
| Real backend | DeepSeek via OpenAI-compatible backend |
| Model | `deepseek-chat` |

## Generation Matrix

| Variant | Prompt entries | Generated | Failed | Final notes | Aggregation | Total tokens |
| --- | ---: | ---: | ---: | ---: | --- | ---: |
| `text_only` | 1 | 1 | 0 | 1 | `rule_family` | 699 |
| `diff_only` | 905 | 905 | 0 | 878 | `rule_family` | 577099 |
| `no_graph` | 905 | 905 | 0 | 883 | `rule_family` | 937874 |
| `no_fallback` | 905 | 905 | 0 | 892 | `rule_family` | 1018033 |
| `full_adaptive_rule_family` | 905 | 905 | 0 | 900 | `rule_family` | 2016276 |
| `full_strict_1hop` | 905 | 905 | 0 | 902 | `rule_family` | 1883078 |
| `full_similarity_family` | 905 | 905 | 0 | 490 | `similarity_family` | 2016276 |
| `full_evidence_similarity_family` | 905 | 905 | 0 | 682 | `evidence_similarity_family` | 2016276 |

## Artifact Paths

All release-note outputs are under:

- `outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/`

Variant subdirectories:

- `text_only/`
- `diff_only/`
- `no_graph/`
- `no_fallback/`
- `full_adaptive_rule_family/`
- `full_strict_1hop/`
- `full_similarity_family/`
- `full_evidence_similarity_family/`

For each variant, `release_note.json`, `release_note.md`, `evaluation_prepare.json`, and `matches_strict_template.json` are available.

Candidate-review packets are also available for each variant:

- `match_review_candidates.json`
- `match_review_candidates.md`

These packets rank likely generated-note matches for each GT entry using lexical and source-symbol overlap. They are an audit aid only and must not be treated as final semantic matches without review.

Manual/projection strict matching previously existed for:

- `diff_only/matches_strict.json`
- `diff_only/matches_strict_similarity_family.json` for the separately re-aggregated `diff_only` similarity output

Rule-assisted strict first-pass matching now also exists for every variant:

- `matches_strict_rule_aided.json`
- `evaluation_strict_rule_aided.json`

This rule-assisted pass uses the candidate-review packets plus GT-specific semantic rules. It is useful for running the full method matrix, but it should be spot-audited before being used as thesis-final evidence.

## Rule-Assisted Strict First-Pass Matrix

The table below reflects the second-pass strict cleanup of clear false positives. It is still rule-assisted and should be treated as stress/extension evidence rather than final manual adjudication.

| Variant | Generated | Valid matches | Matched GT | Precision | Recall | F1 | Unsupported rate | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `diff_only` | 878 | 81 | 33 | 0.0923 | 0.8462 | 0.1664 | 0.9077 | 2.0769 | 1.2308 |
| `no_graph` | 883 | 91 | 33 | 0.1031 | 0.8462 | 0.1837 | 0.8969 | 2.3333 | 1.4872 |
| `no_fallback` | 892 | 86 | 31 | 0.0964 | 0.7949 | 0.1720 | 0.9036 | 2.2051 | 1.4103 |
| `full_adaptive_rule_family` | 900 | 88 | 31 | 0.0978 | 0.7949 | 0.1741 | 0.9022 | 2.2564 | 1.4615 |
| `full_strict_1hop` | 902 | 95 | 34 | 0.1053 | 0.8718 | 0.1879 | 0.8947 | 2.4359 | 1.5641 |
| `full_similarity_family` | 490 | 74 | 32 | 0.1510 | 0.8205 | 0.2551 | 0.8490 | 1.8974 | 1.0769 |
| `full_evidence_similarity_family` | 682 | 82 | 31 | 0.1202 | 0.7949 | 0.2089 | 0.8798 | 2.1026 | 1.3077 |

Unmatched GT IDs by variant:

| Variant | Unmatched GT IDs |
| --- | --- |
| `text_only` | all 39 GT entries |
| `diff_only` | `GT-G216`, `GT-G219`, `GT-G222`, `GT-G223`, `GT-G227`, `GT-G237` |
| `no_graph` | `GT-G216`, `GT-G219`, `GT-G222`, `GT-G223`, `GT-G227`, `GT-G237` |
| `no_fallback` | `GT-G212`, `GT-G215`, `GT-G216`, `GT-G219`, `GT-G222`, `GT-G223`, `GT-G227`, `GT-G237` |
| `full_adaptive_rule_family` | `GT-G215`, `GT-G216`, `GT-G219`, `GT-G220`, `GT-G222`, `GT-G223`, `GT-G227`, `GT-G237` |
| `full_strict_1hop` | `GT-G216`, `GT-G219`, `GT-G222`, `GT-G227`, `GT-G237` |
| `full_similarity_family` | `GT-G215`, `GT-G216`, `GT-G219`, `GT-G220`, `GT-G223`, `GT-G227`, `GT-G237` |
| `full_evidence_similarity_family` | `GT-G215`, `GT-G216`, `GT-G219`, `GT-G220`, `GT-G222`, `GT-G223`, `GT-G227`, `GT-G237` |

## Commands Used

The base command pattern was:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli generate-release-notes `
  --config configs/benchmark/upstream_git_2_52_0_to_2_53_0.json `
  --prompt-bundle-input <prompt_bundle_path> `
  --json-output <variant_output_dir>/release_note.json `
  --markdown-output <variant_output_dir>/release_note.md `
  --backend openai `
  --model deepseek-chat `
  --aggregation-strategy rule_family
```

The `full_similarity_family` and `full_evidence_similarity_family` outputs were produced from `full_adaptive_rule_family/release_note.json` with:

```powershell
python -m cpp_release_note_mvp.cli rewrite-aggregation `
  --input outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/deepseek_chat/full_adaptive_rule_family/release_note.json `
  --aggregation-strategy <similarity_family|evidence_similarity_family> `
  --json-output <variant_output_dir>/release_note.json `
  --markdown-output <variant_output_dir>/release_note.md
```

## Current Interpretation Boundary

Do not treat the rule-assisted matrix as final method-quality evidence yet. It proves that all variants can run on the full 905-function release pair and that a comparable first-pass strict-evaluation matrix can be produced. Final interpretation should wait until this first-pass matrix is spot-audited and compared with other full/large cases.

Valid next step:

1. Keep this case as a full-scope stress/extension result unless a complete manual adjudication pass is performed.
2. Compare it with PCRE2 and the 82-GT main matrix to discuss scale, redundancy, and aggregation behavior.
3. Do not merge it directly into the primary 82-GT table as an equal-weight case without explicitly changing the experimental protocol.

# PCRE2 Full-Scope All-Method Status

Generated on: 2026-05-29

Updated on: 2026-05-30

This report records the current full-scope all-method status for `third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release`. It is a full-matrix execution and first-pass evaluation report. It must not be used alone to draw final method-quality conclusions.

## Scope

| Item | Value |
| --- | ---: |
| Full changed functions | 1123 |
| Full-scope GT candidates | 16 |
| Adaptive CMG prompt-node matches | 806 |
| Strict 1-hop CMG prompt-node matches | 806 |
| Unique unmatched symbols | 241 |

## Full Prompt Matrix

| Variant | Prompt entries | Bundle size | Approx input tokens | Avg chars/entry | Max chars/entry |
| --- | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 0.01 MB | 599 | 2397.0 | 2397 |
| `diff_only` | 1123 | 4.17 MB | 984964 | 3508.3 | 39715 |
| `no_graph` | 1123 | 5.54 MB | 1322426 | 4710.3 | 40917 |
| `no_fallback` | 1123 | 5.82 MB | 1394108 | 4965.7 | 41328 |
| `full_adaptive_rule_family` | 1123 | 8.41 MB | 2067651 | 7364.7 | 42310 |
| `full_strict_1hop` | 1123 | 7.47 MB | 1823007 | 6493.3 | 42310 |

Prompt artifacts are under:

- `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/`

## Real Backend Execution Status

DeepSeek:

- `text_only`: completed, `1/1` generated.
- `diff_only`: completed, `1123/1123` generated. The earlier `HTTP 402 Insufficient Balance` interruption was recovered by retrying only the failed entries and merging the successful retry output.
- `no_graph`: completed, `1123/1123` generated.
- `no_fallback`: completed, `1123/1123` generated.
- `full_adaptive_rule_family`: completed, `1123/1123` generated.
- `full_strict_1hop`: completed, `1123/1123` generated.
- `full_similarity_family`: materialized by reaggregating `full_adaptive_rule_family`.
- `full_evidence_similarity_family`: materialized by reaggregating `full_adaptive_rule_family`.

OpenAI:

- `text_only` smoke test failed.
- Failure reason: `HTTP 429 insufficient_quota`.
- Config added: `configs/benchmark/third_party_pcre2_v6_0_0_2_to_v6_1_openai.json`.

The admitted full-scope execution matrix uses DeepSeek only, keeping provider/model constant across all variants.

## Generation Matrix

| Variant | Prompt entries | Generated | Failed | Final notes | Aggregation |
| --- | ---: | ---: | ---: | ---: | --- |
| `text_only` | 1 | 1 | 0 | 1 | `rule_family` |
| `diff_only` | 1123 | 1123 | 0 | 1082 | `rule_family` |
| `no_graph` | 1123 | 1123 | 0 | 1078 | `rule_family` |
| `no_fallback` | 1123 | 1123 | 0 | 1085 | `rule_family` |
| `full_adaptive_rule_family` | 1123 | 1123 | 0 | 1104 | `rule_family` |
| `full_strict_1hop` | 1123 | 1123 | 0 | 1097 | `rule_family` |
| `full_similarity_family` | 1123 | 1123 | 0 | 382 | `similarity_family` |
| `full_evidence_similarity_family` | 1123 | 1123 | 0 | 459 | `evidence_similarity_family` |

## Rule-Assisted Strict First-Pass Matrix

The table below reflects the second-pass strict cleanup of clear false positives. It is still rule-assisted and should be treated as stress/extension evidence rather than final manual adjudication.

| Variant | Generated | Valid matches | Matched GT | Precision | Recall | F1 | Unsupported rate | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 0 | 0 | 0.0000 | 0.0000 | 0.0000 | 1.0000 | 0.0000 | 0.0000 |
| `diff_only` | 1082 | 65 | 13 | 0.0444 | 0.8125 | 0.0841 | 0.9556 | 4.0625 | 3.2500 |
| `no_graph` | 1078 | 62 | 13 | 0.0408 | 0.8125 | 0.0777 | 0.9592 | 3.8750 | 3.0625 |
| `no_fallback` | 1085 | 64 | 12 | 0.0442 | 0.7500 | 0.0836 | 0.9558 | 4.0000 | 3.2500 |
| `full_adaptive_rule_family` | 1104 | 69 | 13 | 0.0435 | 0.8125 | 0.0825 | 0.9565 | 4.3125 | 3.5000 |
| `full_strict_1hop` | 1097 | 61 | 12 | 0.0428 | 0.7500 | 0.0811 | 0.9572 | 3.8125 | 3.0625 |
| `full_similarity_family` | 382 | 60 | 13 | 0.0942 | 0.8125 | 0.1689 | 0.9058 | 3.7500 | 2.9375 |
| `full_evidence_similarity_family` | 459 | 68 | 13 | 0.0959 | 0.8125 | 0.1715 | 0.9041 | 4.2500 | 3.4375 |

Unmatched GT IDs by variant:

| Variant | Unmatched GT IDs |
| --- | --- |
| `text_only` | all 16 GT entries |
| `diff_only` | `GT-P201`, `GT-P205`, `GT-P212` |
| `no_graph` | `GT-P201`, `GT-P205`, `GT-P212` |
| `no_fallback` | `GT-P201`, `GT-P205`, `GT-P208`, `GT-P212` |
| `full_adaptive_rule_family` | `GT-P201`, `GT-P205`, `GT-P212` |
| `full_strict_1hop` | `GT-P201`, `GT-P205`, `GT-P208`, `GT-P212` |
| `full_similarity_family` | `GT-P201`, `GT-P205`, `GT-P212` |
| `full_evidence_similarity_family` | `GT-P201`, `GT-P205`, `GT-P212` |

## Interpretation Boundary

Do not treat the rule-assisted matrix as final manual adjudication. It is a comparable first-pass matrix used to inspect whether a large PCRE2 release behaves similarly to Git 2.53 and the existing 82-GT benchmark.

Main observations to verify with manual spot-audit:

1. Function-level full coverage creates heavy redundancy for PCRE2 because the version pair includes broad SLJIT/JIT churn and many deleted backend functions.
2. Similarity aggregation reduces final notes strongly, from `1104` adaptive full notes to `382` similarity-family notes, but unsupported rate remains high in the first-pass matrix.
3. `GT-P201` CVE-2025-58050 and `GT-P205` UCD 16 remain consistently unmatched because the generated function-level notes rarely state those exact release-note facts.
4. Final thesis conclusions should compare this PCRE2 matrix with Git 2.53 and the existing 82-GT matrix, rather than using PCRE2 alone.

## Next Step

Use this case as a full-scope stress/extension result, not as a replacement for the manually reviewed 82-GT main matrix. If it is promoted into a thesis-final table, perform a complete manual adjudication pass over `matches_strict_rule_aided.json` first.

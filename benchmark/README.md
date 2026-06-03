# OpenHarmony C/C++ Benchmark

This directory defines the benchmark used by the C/C++ release-note generation prototype.

The benchmark follows a five-layer design adapted from release-note generation literature such as VerLog:

1. Candidate repository pool.
2. Version-pair screening.
3. Ground-truth admission.
4. Experiment stratification.
5. Unified evaluation.

The purpose is to keep engineering demos separate from final evaluation data. A version pair can be useful for development without being admitted into the final benchmark.

Current final-standard note: the selected GT target is now 82 semantic entries.
Added GT entries must be handled with the same standard as the original 17 core
entries. A case enters the final quantitative matrix only after all required
method variants have generated outputs, completed `matches_strict.json`, and
`evaluation_strict.json`.

Current full-coverage tracker:

- `final_all_variant_coverage_audit.md`
- `full_coverage_trial_report.md`

## Layer 1: Candidate Repository Pool

Candidate repositories must satisfy:

- OpenHarmony official or ecosystem repository.
- C/C++ dominant third-party or native component.
- Public Git repository and release tags.
- Source snapshots can be analyzed without requiring a full build.

Recorded in:

- `openharmony_cpp_benchmark.json`

Current repository coverage:

- `core_eval`: `third_party_curl`, `third_party_sqlite`, `third_party_mbedtls`, `third_party_zlib`, `third_party_cJSON`.
- `candidate`: screened same-repository alternates such as larger curl/sqlite/mbedtls pairs.
- `patch_challenge`: `third_party_libpng`, `third_party_libxml2`.
- `patch_challenge`: `third_party_jsoncpp`, `third_party_libjpeg-turbo`.
- `stress_test`: `third_party_pcre2`, `third_party_openssl`.

The current core set reaches five repository categories or component families: network, database/storage, security/crypto, compression, and JSON parsing. The compression case is intentionally marked as low statistical weight because it contains one reviewed semantic GT item.

`third_party_cJSON` is now admitted as the fifth `core_eval` repository. Its `OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release` pair has 11 direct-source changed functions, 11/11 CMG matches, reviewed ground truth, and real DeepSeek strict evaluation.

## Layer 2: Version-Pair Screening

Each adjacent tag pair is screened before expensive ENRE and LLM runs.

Required screening fields:

- `ref` and `tgt` tags.
- commit count.
- changed C/C++ file count.
- changed function count.
- whether changes are direct source changes or patch-only changes.
- whether Stage 1 succeeded.

Screening outputs should be generated through `detect-changes`.

Recent expanded screening snapshots:

- `screening/third_party_sqlite_recent12.json`
- `screening/third_party_mbedtls_recent12.json`
- `outputs/screening/third_party_curl_recent12.json`
- `outputs/screening/third_party_zlib_recent12.json`
- `outputs/screening/third_party_libpng_recent12.json`
- `outputs/screening/third_party_libxml2_recent12.json`
- `outputs/screening/third_party_pcre2_recent8.json`
- `outputs/screening/third_party_jsoncpp_recent8.json`
- `outputs/screening/third_party_libjpeg_turbo_recent8.json`

Current screening decision:

- Continue using medium direct-source cases for the main metric table.
- Keep tiny cases only as coverage or edge-case samples unless they are semantically important, such as the zlib CVE-style fix.
- Keep patch-only cases out of `core_eval` until patch-aware extraction is implemented.
- Keep the newly screened pcre2 `OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release` pair as a large stress candidate unless full-scope GT and strict matches are completed. It has 1123 changed functions; full CMG and prompt construction have been tested, but fair admission still depends on reviewed semantic GT and strict evaluation.
- The first pcre2 sampled-stress artifact is generated with `sample-changed-functions`: 80 sampled functions across 62 files, plus a sampled evidence packet for GT drafting.

Recent P2 screening note:

- `p2_recent_screening_summary.md`

## Layer 3: Ground-Truth Admission

A version pair enters the final evaluation set only after a ground truth can be curated from reliable evidence.

Preferred evidence sources:

- official release notes or changelog entries.
- tag messages.
- patch descriptions.
- commit messages.
- PR/MR summaries if available.
- inspected code diffs.

Ground truth must be written as semantic release-note entries rather than copied commit messages.

## Layer 4: Experiment Stratification

Cases are assigned to one of these roles:

- `candidate`: screened case that may become a core evaluation case after Stage 2/3 and ground-truth review.
- `dev_demo`: useful for pipeline development and reporting, but not necessarily final evaluation.
- `core_eval`: admitted to the main benchmark after ground-truth curation.
- `patch_challenge`: patch-file based updates that require patch-aware extraction before fair evaluation.
- `stress_test`: large repositories or large version pairs used mainly for scalability and cost analysis.

Recommended case diversity:

- database/storage.
- network.
- compression.
- security/crypto.
- media or image codec.
- XML/parser or native system component.

Current admitted `core_eval` cases:

- `curl_v6_0_beta1_to_v6_0`
- `sqlite_v6_0_0_2_to_v6_1`
- `mbedtls_v6_0_beta1_to_v6_0`
- `zlib_v6_0_0_1_to_v6_0_0_2`
- `cjson_v6_0_beta1_to_v6_0`

The medium cases should drive most claims. The zlib and cJSON cases improve repository diversity, but they should not be over-weighted in conclusions because they have low reviewed-GT counts (`1` and `2` entries).

## Layer 5: Unified Evaluation

All admitted `core_eval` cases should run the same method variants:

- `text_only`: commit messages and metadata only.
- `diff_only`: raw or function-level diff only.
- `no_graph`: diff plus metadata without CMG.
- `no_fallback`: diff plus metadata plus ENRE-original CMG, excluding synthetic and diff-derived fallback context.
- `full`: diff plus CMG plus commit messages.

Recommended ablations:

- strict CMG vs adaptive CMG.
- with vs without fallback context.
- with vs without commit messages.
- aggregation strategy: `none`, `exact`, `rule_family`, `similarity_family`, `evidence_similarity_family`.

Evaluation should report:

- semantic precision, recall, and F1 against ground truth.
- unsupported-claim rate.
- redundancy as normalized `Matches/GT` and `Extra/GT`.
- output structural validity.
- token usage and runtime.
- human ratings for completeness, accuracy, readability, and overall usefulness when possible.

Current final strict DeepSeek matrix:

- `final_all_variant_matrix.md`
- `final_all_variant_matrix.json`
- `final_all_variant_coverage_audit.md`
- `final_match_completion_report.md`

Final selected benchmark result:

- 11 case-version pairs.
- 82 reviewed semantic GT entries.
- 8 required method variants per case.
- 88 completed case-variant cells.
- 656 completed GT-variant cells.
- 0 missing release-note outputs, strict matches, or strict evaluations in the selected matrix.

Final Macro/Micro F1 summary:

| Method | Macro F1 | Micro F1 | Unsupported | Extra/GT |
| --- | ---: | ---: | ---: | ---: |
| `text_only` | 0.2909 | 0.1505 | 0.3636 | 0.0000 |
| `diff_only` | 0.6543 | 0.5677 | 0.5931 | 2.1341 |
| `no_graph` | 0.6397 | 0.5495 | 0.6050 | 2.0244 |
| `full_adaptive_rule_family` | 0.6419 | 0.5503 | 0.6108 | 1.9878 |
| `full_no_fallback` | 0.6228 | 0.5239 | 0.6309 | 1.9024 |
| `full_strict_1hop` | 0.6616 | 0.5585 | 0.5980 | 2.0732 |
| `full_similarity_family` | 0.7020 | 0.6046 | 0.5542 | 1.3293 |
| `full_evidence_similarity_family` | 0.6532 | 0.5555 | 0.6034 | 1.6585 |

Final interpretation:

- `full_similarity_family` has the best Macro F1 and Micro F1 in the completed 82-GT matrix, while also reducing average final notes to `37.7273`.
- `full_strict_1hop` is the strongest graph-context ablation after the final targeted strict-match audits, outperforming `no_graph`, `full_adaptive_rule_family`, and `full_no_fallback` on both Macro F1 and Micro F1.
- `diff_only` remains a strong direct-evidence baseline. The thesis should not claim that more context always improves quality.
- Redundancy is still high across evidence-rich methods. `Extra/GT` should be treated as a central limitation and a target for aggregation, not as a secondary detail.
- PCRE2 and Git 2.53 full-scope coverage is now feasible at Stage 2/3 prompt construction, but the final matrix should not be changed until the corresponding full-scope GT, real generation, strict matches, and evaluations are completed.

Historical core5 summaries are still kept for regression and audit:

- `core5_experiment_matrix.md`
- `core5_experiment_matrix.json`
- `core5_per_case_results.md`
- `core5_per_case_results.json`
- `evaluation_strict_core5_summary.md`
- `baseline_core5_output_summary.md`
- `fallback_ablation_core5_evaluation_summary.md`
- `cmg_strict_1hop_core5_evaluation_summary.md`
- `aggregation_*_core5_*.md/json`

Interpretation caveats:

- Several variants reach recall `1.0000`; this is plausible at the current semantic-entry GT granularity, but should be treated as a validity threat because finer-grained GT splitting could lower recall.
- `no_graph` performs below `diff_only` even though it includes more metadata. This supports the context-noise interpretation: commit messages and project metadata can introduce plausible but unsupported or weakly matched claims.
- All evidence-rich variants still have high redundancy. This should be reported as a limitation and an aggregation-target metric, not hidden behind F1.
- Macro F1 is sensitive to low-GT cases such as zlib and cJSON. Thesis tables should include per-case results and the newly reported `Micro F1` view before drawing final method conclusions.
- Strict semantic matching requires audit. Known sqlite, mbedTLS, cJSON, curl, and broad multi-GT issues involving over-loose matches, helper-only matches, unsupported secondary GT links, and incorrect CVE attribution have been corrected; future changes to `matches_strict.json` should preserve the same review standard.
- The matrix should be used as a tradeoff view across quality, context cost, redundancy, and aggregation strength, not as evidence that more context is always better.

## Case Metadata

Each screened version pair should have:

- `cases/<repository>/<version_pair_id>/metadata.json`
- `cases/<repository>/<version_pair_id>/ground_truth.md`

The metadata contract is documented in `case_schema.md`.

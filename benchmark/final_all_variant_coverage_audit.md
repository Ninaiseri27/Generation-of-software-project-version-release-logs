# Final All-Variant Coverage Audit

Last updated: 2026-05-29

This audit fixes the final experiment standard after the advisor feedback:
newly added GT entries must receive the same treatment as the original core 17
GT entries. A case can enter the final quantitative matrix only when it has:

- reviewed GT entries under the unified GT protocol;
- generated outputs for every required method variant;
- `matches_strict.json` filled under the same semantic matching rule;
- `evaluation_strict.json` produced from those strict matches.

Current status: complete for the selected 82-GT benchmark.

The 2026-05-29 refresh tightened mbedTLS hostname-security matches: generated
notes that only described SSL hostname cleanup, pointer access, or internal
state handling were downgraded unless they explicitly stated the GT-level
behavior that certificate verification fails when a hostname is required but
missing.

## Required Method Variants

The final comparable matrix uses eight method variants:

| Method ID | Meaning |
| --- | --- |
| `text_only` | Commit/release metadata without diff or graph evidence. |
| `diff_only` | Function-level diff evidence only. |
| `no_graph` | Diff plus project/commit metadata, without CMG. |
| `full_adaptive_rule_family` | Diff plus adaptive CMG/fallback context and default aggregation. |
| `full_no_fallback` | Full prompt without fallback/synthetic context. |
| `full_strict_1hop` | Full prompt using strict 1-hop CMG. |
| `full_similarity_family` | Full output aggregated by similarity-family grouping. |
| `full_evidence_similarity_family` | Full output aggregated by evidence-gated similarity-family grouping. |

The two similarity-family variants reuse existing `full` generation, but they
still have materialized release-note outputs, strict matches, and evaluation
files.

## Current Coverage

| Case | Scope | GT Count | Current Coverage | Missing Method Variants |
| --- | --- | ---: | ---: | --- |
| `curl_v6_0_beta1_to_v6_0` | core | 4 | 8/8 | none |
| `sqlite_v6_0_0_2_to_v6_1` | core | 4 | 8/8 | none |
| `mbedtls_v6_0_beta1_to_v6_0` | core | 6 | 8/8 | none |
| `zlib_v6_0_0_1_to_v6_0_0_2` | core | 1 | 8/8 | none |
| `cjson_v6_0_beta1_to_v6_0` | core | 2 | 8/8 | none |
| `curl_v6_0_to_v6_0_0_1` | OpenHarmony extension | 3 | 8/8 | none |
| `pcre2_v6_0_0_2_to_v6_1` | sampled stress | 5 | 8/8 | none |
| `curl_8_11_0_to_8_11_1` | upstream extension | 16 | 8/8 | none |
| `curl_8_14_0_to_8_14_1` | upstream extension | 10 | 8/8 | none |
| `git_2_51_0_to_2_51_1` | upstream extension | 16 | 8/8 | none |
| `git_2_52_0_to_2_53_0` | sampled upstream extension | 15 | 8/8 | none |

Summary:

- Final selected GT entries: `82`.
- Required case-variant cells: `88`.
- Completed case-variant cells: `88`.
- Missing case-variant cells: `0`.
- Required GT-variant cells: `656`.
- Completed GT-variant cells: `656`.
- Missing GT-variant cells: `0`.

## GT Status Gate

All selected cases are now reviewed, reviewed sampled strict, or reviewed
extension cases under the unified GT protocol. The OpenHarmony curl
`OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release` case has been
promoted from `draft_candidate` to `reviewed_extension`.

## Final Outputs

- Final all-variant matrix: `benchmark/final_all_variant_matrix.md`
- Final all-variant matrix JSON: `benchmark/final_all_variant_matrix.json`
- Match completion report: `benchmark/final_match_completion_report.md`
- Final visual report: `benchmark/visual_report_final_82gt.html`
- Final strict-match audit: `benchmark/final_strict_match_audit.md`

## Remaining Review Notes

The full matrix is complete, but strict matching still remains the most
judgment-sensitive part of the experiment. Before copying final numbers into the
thesis, re-audit:

- security/CVE rows;
- aggregated rows where one generated note maps to multiple GT entries;
- helper/refactor-like generated notes near GT evidence functions;
- sampled Git 2.53 rows, because the sample is GT-evidence-first rather than a
  random sample.

## Thesis Rule

The final paper may now state:

> 本文最终实验数据集包含 82 条经过统一协议审核的语义级 GT 条目。所有纳入最终定量比较的用例均已在相同方法变体下生成结果，并依据同一严格语义匹配规则填写 `matches_strict.json` 后计算指标。

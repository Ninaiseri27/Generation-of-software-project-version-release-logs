# Full-Scope Match Quality Audit

Audit date: 2026-05-30

This note records the second-pass quality audit for the two large/full-scope experiment cases:

- `upstream_git_2_52_to_2_53`
- `third_party_pcre2_v6_0_0_2_to_v6_1`

The audit covers `matches_strict_rule_aided.json` for all eight method variants. It does not convert the files into final manual adjudication; it removes clear false positives from the rule-assisted first pass so the stress-case table is not inflated by obvious semantic mistakes.

## Audit Rule

The second pass uses a stricter semantic rule than lexical/source-symbol matching:

- A generated entry is counted only if it expresses the release-note-level GT fact, not merely a changed helper function.
- Cleanup-only, removal-only, memory-leak-only, debug-printer-only, or unrelated internal-refactor notes are removed when the GT describes user/developer-visible behavior.
- Broad aggregated notes can still match multiple GT entries only when the generated title or summary explicitly covers those GT facts.
- Remaining files are still labeled `rule-assisted`; final thesis claims should not describe them as fully manual unless another complete adjudication pass is performed.

## Removed Matches

| Case | Removed Matches | Main Removed Categories |
| --- | ---: | --- |
| `upstream_git_2_52_to_2_53` | 61 | repo-info vs ODB streaming confusion; incomplete-line whitespace vs symref/fsck newline confusion; macro-expansion behavior vs helper/removal-only rows; worktree display-width behavior vs memory-leak/removal-only rows |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | 10 | runtime regex behavior vs debug-printer rows; substitute case transformation vs pcre2test formatting/type-cast rows; caseless-restrict behavior vs removal-only `match_ref` row |
| Total | 71 | Clear false positives only |

Detailed removed pairs are stored in:

- `benchmark/full_scope_second_pass_removed_matches.json`

One initially removed Git repo-info match was restored after manual review because the generated note directly stated repo-info object-size output.

## Updated Case Metrics

Git 2.53:

| Variant | F1 Before | F1 After | Note |
| --- | ---: | ---: | --- |
| `text_only` | 0.0000 | 0.0000 | unchanged |
| `diff_only` | 0.1829 | 0.1664 | stricter helper/refactor filtering |
| `no_graph` | 0.1980 | 0.1837 | stricter helper/refactor filtering |
| `no_fallback` | 0.1843 | 0.1720 | stricter helper/refactor filtering |
| `full_adaptive_rule_family` | 0.1898 | 0.1741 | stricter helper/refactor filtering |
| `full_strict_1hop` | 0.2019 | 0.1879 | stricter helper/refactor filtering |
| `full_similarity_family` | 0.2780 | 0.2551 | aggregation remains strongest but less inflated |
| `full_evidence_similarity_family` | 0.2285 | 0.2089 | aggregation remains useful but less inflated |

PCRE2:

| Variant | F1 Before | F1 After | Note |
| --- | ---: | ---: | --- |
| `text_only` | 0.0000 | 0.0000 | unchanged |
| `diff_only` | 0.0858 | 0.0841 | debug-printer false positive removed |
| `no_graph` | 0.0794 | 0.0777 | debug-printer false positive removed |
| `no_fallback` | 0.0836 | 0.0836 | one unrelated pcre2test row removed; rounded F1 unchanged |
| `full_adaptive_rule_family` | 0.0842 | 0.0825 | debug-printer false positive removed |
| `full_strict_1hop` | 0.0827 | 0.0811 | removal-only and unrelated pcre2test rows removed |
| `full_similarity_family` | 0.1731 | 0.1689 | debug-printer and unrelated tooling rows removed |
| `full_evidence_similarity_family` | 0.1750 | 0.1715 | debug-printer false positive removed |

Cross-case aggregate after cleanup:

| Variant | Macro F1 | Micro F1 | Total GT | Total Generated | Avg Unsupported Rate |
| --- | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 0.0000 | 0.0000 | 55 | 2 | 1.0000 |
| `diff_only` | 0.1253 | 0.1220 | 55 | 1960 | 0.9316 |
| `no_graph` | 0.1307 | 0.1272 | 55 | 1961 | 0.9281 |
| `no_fallback` | 0.1278 | 0.1247 | 55 | 1977 | 0.9297 |
| `full_adaptive_rule_family` | 0.1283 | 0.1251 | 55 | 2004 | 0.9294 |
| `full_strict_1hop` | 0.1345 | 0.1309 | 55 | 1999 | 0.9260 |
| `full_similarity_family` | 0.2120 | 0.2186 | 55 | 872 | 0.8774 |
| `full_evidence_similarity_family` | 0.1902 | 0.1941 | 55 | 1141 | 0.8920 |

The updated matrix files are:

- `benchmark/full_scope_first_pass_matrix.md`
- `benchmark/full_scope_first_pass_matrix.json`

## Remaining Risk

The second-pass cleanup does not eliminate all uncertainty:

- PCRE2 still has many broad generated entries that legitimately combine several regex features, so multi-GT matches are common.
- Git 2.53 still contains internal but developer-facing ODB-streaming and credential-helper entries, where strictness depends on whether the thesis treats developer-facing internal API work as release-note-worthy.
- Both large cases have very high unsupported rates because function-level full coverage generates hundreds or thousands of notes while GT stays at semantic release-note granularity.

## Table Admission Recommendation

Do not merge Git 2.53 full-scope and PCRE2 full-scope directly into the primary 82-GT main experiment table as equal cases.

Update after human-standard audit: a stricter close-to-manual audit has now been added in `benchmark/full_scope_human_standard_audit.md`, with detailed results in `benchmark/full_scope_human_audited_matrix.md`. Prefer those files for the final merge decision. Under that stricter audit, the two large cases are suitable as a separately labeled `82-GT core + 55-GT full-scope extension` result, but still should not silently replace the primary 82-GT controlled table.

Recommended thesis structure:

- Main table: keep the unified 82-GT manually reviewed benchmark as the primary result.
- Extension/stress table: report Git 2.53 and PCRE2 full-scope together to show scaling behavior, redundancy pressure, and aggregation effects.
- Optional appendix: provide an all-cases combined table only as supplementary evidence, with a clear note that it mixes manually reviewed core cases and rule-assisted stress cases.

Reasoning:

- The 82-GT benchmark and the two full-scope stress cases currently use different match-finality levels.
- Git 2.53 and PCRE2 are much larger than the other cases and would dominate micro metrics and generated-note counts.
- The stress cases are most useful for validating the scalability limitation and the need for aggregation, not for replacing the controlled main comparison.

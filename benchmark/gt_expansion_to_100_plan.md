# GT Expansion To 100 Plan

Last updated: 2026-05-28

This document replaces the earlier assumption that the 17-entry core5 set is sufficient for the final thesis. The revised target is to build a thesis-facing benchmark inventory with about 80-100 reviewed or clearly scoped GT entries, while keeping strict metric reporting statistically honest.

## Motivation

The current core5 benchmark has strong traceability, but only 17 reviewed semantic release-note entries. This is too small for a confident main conclusion, especially because zlib and cJSON have only 1 and 2 GT entries. Following the evaluation logic used by VerLog, the benchmark should keep one unified human-reviewed semantic matching protocol, but increase the number of release-note-level GT entries.

The target is not to maximize raw case count. The target is to add high-quality release-note facts backed by official changelogs, release notes, commits, and inspected diffs. The 80-100 count is now the final selected benchmark target, not just a loose inventory. All entries follow the same GT protocol, and the final quantitative matrix must run every selected case through the same required method variants before averaging.

## Current Count

| Group | Cases | Strict GT Count | Reporting Role |
| --- | --- | ---: | --- |
| Core reviewed set | curl beta1->v6.0, sqlite v6.0.0.2->v6.1, mbedTLS beta1->v6.0, zlib v6.0.0.1->v6.0.0.2, cJSON beta1->v6.0 | 17 | Main strict matrix, but with explicit small-sample caveat. |
| OpenHarmony curl extension | curl v6.0->v6.0.0.1 | 3 | Medium extension/stress row after GT status is finalized. |
| PCRE2 sampled stress | pcre2 v6.0.0.2->v6.1 fixed sampled scope | 5 | Large sampled stress row using the same GT protocol; report scope explicitly. |
| Upstream curl reviewed extension | curl 8.11.0->8.11.1 | 16 | Reviewed from official curl RELEASE-NOTES and Stage 1 function-level evidence; two weak refactor/cleanup drafts are excluded. |
| Upstream Git reviewed extension | Git 2.51.0->2.51.1 | 16 | Reviewed from official Git RelNotes and Stage 1 function-level evidence. |
| Upstream Git sampled extension | Git 2.52.0->2.53.0 | 15 | Reviewed sampled extension from official Git RelNotes and Stage 1 function-level evidence; report scope explicitly. |
| Upstream curl reviewed extension | curl 8.14.0->8.14.1 | 10 | Reviewed from official curl RELEASE-NOTES and Stage 1 function-level evidence. |
| Current selected strict benchmark | core + extension + sampled strict scopes | 82 | Fully covered by the required eight method variants under one GT protocol. |

Target status: reached the 80-100 thesis-facing GT range and completed full method-variant coverage for the selected cases. See `final_all_variant_coverage_audit.md` and `final_all_variant_matrix.md`.

## Revised Benchmark Layers

| Layer | Purpose | Inclusion Rule | Metric Policy |
| --- | --- | --- | --- |
| Core reviewed set | Stable strict comparison across variants. | Unified reviewed GT and comparable outputs for all main variants. | May be averaged as core matrix. |
| Extension set | Increase external validity with richer release notes. | Unified reviewed GT and the full required method set generated for final quantitative reporting. | Report as extension table during development; merge into final comparison only after full method coverage and strict matches exist. |
| Sampled stress set | Show large-update behavior and cost/redundancy pressure. | Unified reviewed GT after a fixed changed-function sampling scope and the full required method set generated for that sampled scope. | Report with explicit sampling scope; merge only if the same method coverage exists. |
| Patch challenge set | Show current method boundary. | Patch-only or metadata-only C/C++ changes. | Qualitative limitation only until patch-aware extraction is implemented. |

## Candidate Priorities

### P0: Promote Existing Evidence Without Mixing Averages

1. Keep core5 as the strict baseline matrix.
2. Mark curl v6.0->v6.0.0.1 as a medium extension case if its 3 GT entries are accepted as reviewed.
3. Keep pcre2 sampled GT-S01 through GT-S05 as the large sampled stress set.
4. Report these two additions as secondary rows, not as part of the core5 macro average.

Expected thesis-facing GT inventory after P0: 25 entries.

### P1: Add One Upstream Release Pair With Rich Official Notes

Preferred candidates:

| Candidate | Why It Fits | Expected GT | Risk |
| --- | --- | ---: | --- |
| Git v2.44.0->v2.45.0 or nearby | C project; official `Documentation/RelNotes`; release notes are structured and rich. | 10-15 | Some notes are documentation/tooling rather than C behavior. |
| Upstream curl adjacent 8.x release | C project; official changelog/release table; current pipeline already works well on curl-like code. | 8-12 | Some release-note entries may map to tests, docs, or platform-specific paths. |
| OpenSSL 3.x adjacent minor/patch release | C project; official changelog; security/API content is rich. | 8-15 | Macro-heavy code and large diffs may require sampling. |
| PostgreSQL 17.x patch or 17.0 major release | C project; official release notes are very rich. | 10-20 | Very large repository; likely needs sampling and careful scope control. |

Recommended first attempt: Git or upstream curl. They are more manageable than OpenSSL/PostgreSQL and have strong official release-note sources.

Current status: two upstream curl release pairs and two upstream Git release pairs have already been added as reviewed extension candidates. This raises the selected strict inventory to 82 entries.

### P2: Add A Second And Third Upstream Release Pair If Needed

After one upstream pair is complete, add one or two more from the remaining candidates. Prefer pairs that add repository diversity:

- If P1 uses Git, choose curl or OpenSSL.
- If P1 uses curl, choose Git or OpenSSL.
- Use PostgreSQL only if a fixed sampling scope is acceptable, because full evaluation is likely too large.

Current thesis-facing GT inventory is already in the 80-100 range. Add more cases only if a later thesis argument needs additional repository diversity, not merely to increase the count.

### P3: Reach 80-100 With One More Sampled Stress Pair

If the next rich upstream case does not reach the target range, add one more sampled stress pair from OpenSSL, PostgreSQL, or an expanded PCRE2 scope. This final addition should focus on official release-note coverage and stress behavior rather than core-average F1.

Expected thesis-facing GT inventory after P3: 80-100 entries.

## Admission Protocol For New Upstream Cases

Each new case must pass the same evidence-driven gate:

1. Clone or register the upstream repository under `cpp_release_note_mvp/workspaces/`.
2. Create a benchmark config with the selected adjacent tags.
3. Run `detect-changes` and record changed-function count.
4. Reject or sample the pair if changed functions exceed the manageable range.
5. Build a GT evidence packet from official release notes, commits, and changed functions.
6. Draft `ground_truth.md` as semantic release-note entries.
7. Keep optional or excluded entries in the exclusion/notes section, but do not use a different GT protocol.
8. Run the full required method set: `text_only`, `diff_only`, `no_graph`, `full_adaptive_rule_family`, `full_no_fallback`, `full_strict_1hop`, `full_similarity_family`, and `full_evidence_similarity_family`.
9. Fill strict semantic matches for every variant.
10. Evaluate and report the case in the correct layer.

## Pair Selection Rules

Prefer:

- Official changelog or release notes with multiple user/developer-visible entries.
- C/C++ dominant codebase.
- Adjacent release tags.
- 30-150 changed functions for unsampled evaluation.
- Clear mapping between release-note topics and changed files/functions.

Avoid for main metrics:

- Patch-only updates that do not modify direct source files.
- Metadata-only releases.
- Releases dominated by documentation, CI, formatting, or vendored dependency refreshes.
- Large changes without a fixed sampling scope.

## Thesis Reporting Policy

The final thesis should avoid saying "the dataset has only 17 entries." Use this structure instead:

- Unified GT protocol: all entries use the same semantic release-note fact definition, evidence admission standard, exclusion standard, and strict matching rule.
- Core reviewed set: 17 GT entries for stable controlled comparison.
- Extension set: medium/rich release-note cases added for external validity.
- Sampled stress set: large pcre2-style case for scalability, redundancy, and token-cost analysis under an explicit sampling scope.
- Total selected GT benchmark: target about 80-100 entries, with table columns showing source/scope and method-output coverage.

Metrics should be averaged only over cases that have the same method-output coverage. For the final thesis result, the intended endpoint is full selected-case coverage rather than an inventory-only count.

## Immediate TODO

1. Stop count-driven GT expansion unless a specific repository-diversity gap remains.
2. Use `final_all_variant_matrix.md` as the final selected benchmark matrix source.
3. Audit `matches_strict.json` rows for security/CVE claims, helper/refactor-like generated notes, and aggregated multi-GT matches before thesis insertion.
4. Refresh visual reports and thesis tables from the final matrix.
5. Do not inflate counts by splitting one coherent release-note fact into many near-duplicate GT rows.

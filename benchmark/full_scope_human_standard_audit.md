# Full-Scope Human-Standard Audit

Audit date: 2026-05-30

This report records a stricter, close-to-manual semantic audit over the two large/full-scope cases after the earlier second-pass cleanup.

Audited cases:

- `upstream_git_2_52_to_2_53`: 39 GT entries, 905 changed functions.
- `third_party_pcre2_v6_0_0_2_to_v6_1`: 16 GT entries, 1123 changed functions.

Generated human-audited files exist locally under each variant output directory:

- `matches_strict_human_audited.json`
- `evaluation_strict_human_audited.json`

## Audit Criteria

- Count a match only when the generated title or summary directly expresses the GT-level release-note fact.
- Remove helper-only, cleanup-only, debug-output-only, display-only, or malformed raw-JSON entries when they do not state the GT behavior.
- Keep broad aggregated notes only when the relevant GT semantics are explicitly present and not merely inferred from a function name.
- Treat source symbols as supporting evidence, not as sufficient proof by themselves.

## Additional Removals

After the previous second-pass cleanup, this audit removed `149` more matches and restored `1` synonym-boundary match.

| Case | Additional Removed Matches | Main Reasons |
| --- | ---: | --- |
| `upstream_git_2_52_to_2_53` | 72 | signed-tag rows counted as signed-commit import; generic merge-ort rows counted as the criss-cross assertion fix; helper-only keychain rows; config/diff/fetch rows missing the exact user-visible condition |
| `third_party_pcre2_v6_0_0_2_to_v6_1` | 77 | malformed raw JSON notes; display-only `show_compile_extra_options` rows counted as API/options GT; generic class/JIT rows counted as UTS#18 or Perl-compatible behavior |

Detailed removed/restored pairs are stored in:

- `benchmark/full_scope_human_audit_removed_matches.json`

## Human-Audited Aggregate

| Variant | Macro F1 | Micro F1 | Micro Precision | Micro Recall | Total Generated | Avg Unsupported Rate |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 0.0000 | 0.0000 | 0.0000 | 0.0000 | 2 | 1.0000 |
| `diff_only` | 0.1115 | 0.1088 | 0.0587 | 0.7455 | 1960 | 0.9392 |
| `no_graph` | 0.1144 | 0.1116 | 0.0602 | 0.7636 | 1961 | 0.9375 |
| `no_fallback` | 0.1148 | 0.1120 | 0.0607 | 0.7273 | 1977 | 0.9371 |
| `full_adaptive_rule_family` | 0.1155 | 0.1126 | 0.0609 | 0.7455 | 2004 | 0.9366 |
| `full_strict_1hop` | 0.1183 | 0.1151 | 0.0620 | 0.8000 | 1999 | 0.9354 |
| `full_similarity_family` | 0.1913 | 0.1971 | 0.1135 | 0.7455 | 872 | 0.8894 |
| `full_evidence_similarity_family` | 0.1739 | 0.1776 | 0.1008 | 0.7455 | 1141 | 0.9015 |

The detailed matrix is:

- `benchmark/full_scope_human_audited_matrix.md`
- `benchmark/full_scope_human_audited_matrix.json`

## Merge Decision

Under this stricter audit, the two large cases are credible enough to be reported as an expanded benchmark extension, but they should not be silently merged into the original 82-GT main table as if the experimental scope were unchanged.

Recommended thesis layout:

- Primary result: keep the original 82-GT manually reviewed benchmark as the controlled main table.
- Expanded result: add a second table named `82-GT core + 55-GT full-scope extension`, totaling 137 GT entries, using the human-audited full-scope labels.
- Stress analysis: discuss that Git/PCRE2 full-scope cases sharply increase unsupported rate and redundancy, while similarity aggregation remains the strongest compression/quality tradeoff.

Reason: Git and PCRE2 full-scope are intentionally much larger than the earlier cases. They are valuable because they test scalability and redundancy pressure, but if merged without separation they will dominate micro metrics and make the original controlled benchmark harder to interpret.

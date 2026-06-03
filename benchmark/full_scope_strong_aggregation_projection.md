# Full-Scope Strong Aggregation Projection

Generated on: 2026-05-30

This report tests whether applying the existing strongest aggregation strategy, `similarity_family`, to large full-scope version pairs can further improve result quality. It covers:

- `upstream_git_2_52_to_2_53`
- `third_party_pcre2_v6_0_0_2_to_v6_1`

## Protocol Boundary

This is a source-entry projection over already human-audited matches:

- Existing `release_note.json` files are re-aggregated with `similarity_family`.
- Existing human-audited matches are projected through `source_entry_ids`.
- The result is useful for trend analysis, but it is not a replacement for final human semantic audit.

## Aggregate Result

| Source variant re-aggregated by `similarity_family` | Final notes | Precision | Recall | F1 | Unsupported | Macro F1 | Reduction |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| `diff_only` | 904 | 0.1095 | 0.7455 | 0.1910 | 0.8905 | 0.1868 | 0.4191 / 0.6359 |
| `no_graph` | 891 | 0.1066 | 0.7636 | 0.1871 | 0.8934 | 0.1820 | 0.4145 / 0.6531 |
| `no_fallback` | 872 | 0.1124 | 0.7273 | 0.1947 | 0.8876 | 0.1885 | 0.4395 / 0.6571 |
| `full_adaptive_rule_family` | 872 | 0.1032 | 0.7455 | 0.1813 | 0.8968 | 0.1762 | 0.4556 / 0.6540 |
| `full_strict_1hop` | 866 | 0.1097 | 0.8000 | 0.1929 | 0.8903 | 0.1876 | 0.4590 / 0.6554 |
| `full_evidence_similarity_family` | 872 | 0.1181 | 0.7455 | 0.2039 | 0.8819 | 0.1986 | 0.2815 / 0.1678 |
| `full_similarity_family` human-audited | 872 | 0.1135 | 0.7455 | 0.1971 | 0.8865 | 0.1913 | n/a |

The two reduction values correspond to Git 2.53 and PCRE2 respectively.

## Interpretation

Strong aggregation substantially reduces output size in large full-scope releases, but it does not fully solve unsupported claims.

The main reason is that many unsupported entries are not duplicate phrasings of the same valid release-note fact. They are distinct low-level, test-related, helper-related, or implementation-detail claims. Similarity-based aggregation can merge near-duplicate claims, but it cannot decide whether a unique low-level claim deserves inclusion in a release note.

Therefore, stronger aggregation alone is insufficient. The next technical boundary is release-note-level salience filtering before or during aggregation.

## Candidate Technical Paths

1. Add a release-note-worthiness classifier before aggregation.

   Each generated function-level note should be classified as `release_note_worthy`, `internal_detail`, `test_only`, `build_only`, `diagnostic_only`, or `unsupported_security_claim`. Only worthy notes enter final aggregation.

2. Use two-stage hierarchical summarization.

   First group function-level notes by file, subsystem, command, API, or evidence family. Then summarize each group into one candidate release-note fact and validate it against diff/commit evidence.

3. Separate evidence coverage from final note selection.

   Keep high recall in the internal evidence layer, but use a stricter final selection layer to suppress low-value claims.

4. Add GT-style salience rules to aggregation.

   Examples: prefer public API, command-line behavior, security behavior, compatibility, user-visible behavior, and documented upstream changelog topics; demote tests, helper cleanup, logging-only changes, and build-only adjustments.

5. Use LLM-as-judge or rule-plus-LLM verification after aggregation.

   Ask a verifier whether each final note is directly supported by evidence and whether it is release-note-worthy. This should be optional and evaluated as a separate variant because it adds cost and possible judge bias.


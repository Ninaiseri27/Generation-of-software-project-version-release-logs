# Strict Match Audit

This document audits the manually reviewed `matches_strict.json` files for the first DeepSeek baseline matrix and the first `strict_1hop` CMG ablation.

Audit date: 2026-05-11

## Scope

Audited files:

- Main DeepSeek baseline matrix: `3` cases x `4` variants = `12` files.
- CMG ablation matrix: `3` cases x `full` variant = `3` files.

Mock/backend-wiring `baselines/full/matches_strict.json` files are excluded from final-quality judgement. They are useful for pipeline validation but should not be used as final semantic P/R/F1 evidence.

## Structural Validation

All `15` real DeepSeek strict-match files are structurally valid under the current evaluator:

- `invalid_match_count = 0` for every evaluated file.
- No duplicate `(generated_id, gt_id)` pairs were found.
- All files rerun to `evaluation_status = evaluated`.

Current metric outputs are therefore mechanically valid. The remaining issue is semantic strictness.

## Applied Status

The recommendations in this audit have been applied to the local strict review artifacts:

- `34` generated-to-GT pairs were changed from `match` to `non_match`.
- The changed pairs cover sqlite helper/setup-only matches and mbedtls helper-only or wrong-CVE matches.
- The main DeepSeek baseline matrix and the `strict_1hop/full` CMG ablation were rerun.
- All `15` evaluated strict files still report `invalid_match_count = 0`.

The tightened results are recorded in:

- `benchmark/deepseek_v4_flash_smoke_summary.md`
- `benchmark/cmg_ablation_summary.md`

## Audit Rule

For strict release-note-level evaluation, a match should be counted only when the generated note expresses the same user/developer-visible behavior as the ground-truth entry.

The following should normally be marked as non-matches:

- Pure test setup, helper, schema, or teardown changes that do not describe the release-note behavior.
- Notes that only mention implementation scaffolding rather than the ground-truth behavior.
- Notes with wrong CVE IDs or wrong vulnerability attribution, even if they touch a related function family.

## Case-Level Findings

### curl

Verdict: acceptable as filled.

Rationale:

- The matched generated notes consistently map to the four reviewed curl GT entries.
- The one generated entry mapped to both `GT-001` and `GT-002` explicitly mentions both the handover/network-binding options and the MMS reserved-default-port option, so the one-to-many match is justified.
- Redundancy remains high, but this is already reflected by the redundancy metric and is not a match-file error.

Recommended action:

- Keep curl `matches_strict.json` files unchanged.

### sqlite

Verdict: mostly acceptable, but several helper/setup-only matches are too lenient for strict semantic evaluation.

Recommended non-match candidates:

| Variant | Generated ID | Current GT | Reason |
| --- | --- | --- | --- |
| `diff_only` | `GEN-006` | `GT-001` | SQLite log teardown/reset is test hygiene, not the memory-safety/security behavior in `GT-001`. |
| `diff_only` | `GEN-001` | `GT-003` | Adding an extra BLOB column to a test schema is supporting setup, not binlog replay reliability behavior. |
| `diff_only` | `GEN-002` | `GT-004` | Cleaning test database files before each test is test setup, not encrypted database rekey behavior. |
| `diff_only` | `GEN-013` | `GT-004` | `CreateTable` helper creation is scaffolding for rekey tests, not release-note behavior. |
| `diff_only` | `GEN-037` | `GT-004` | Test suite setup/log directory creation is scaffolding. |
| `no_graph` | `GEN-036` | `GT-003` | Updating a test schema with an extra BLOB column is setup evidence, not binlog replay behavior. |
| `no_graph` | `GEN-012` | `GT-004` | `CreateTable` helper creation is scaffolding. |
| `no_graph` | `GEN-017` | `GT-004` | Cleanup setup for tests is scaffolding. |
| `no_graph` | `GEN-019` | `GT-004` | Data verification helper is supporting test code, not rekey behavior itself. |
| `no_graph` | `GEN-035` | `GT-004` | Test setup/log directory creation is scaffolding. |
| `full` | `GEN-021` | `GT-003` | Extra BLOB test schema update is setup evidence, not binlog replay behavior. |

Recommended action:

- If the thesis uses strict release-note semantics, change these rows to non-match decisions or remove them from `matches`.
- Keep sqlite entries that describe concrete behavior checks, such as binlog replay failure/recovery, `SQLITE_MISUSE`, `SQLITE_BUSY`, corrupt/busy compressed-VFS behavior, or rekey success/failure scenarios.

### mbedtls

Verdict: structurally valid, but semantically over-optimistic. This is the highest-risk case.

Main issue:

- Several generated notes are assigned to a GT entry because they touch the same function family, but the generated text either only describes a helper/cleanup function or cites the wrong CVE IDs.
- Wrong CVE attribution should be treated as a strict semantic error. Otherwise precision will look artificially perfect even when the release note contains false security metadata.

High-confidence non-match candidates:

| Variant | Generated ID | Current GT | Reason |
| --- | --- | --- | --- |
| `diff_only` | `GEN-002` | `GT-001` | Helper-only note; does not state the certificate-verification-without-hostname behavior. |
| `full` | `GEN-001` | `GT-001` | Helper-only and speculative wording: "likely to support"; not strict release-note behavior. |
| `full` | `GEN-002` | `GT-003` | Wrong CVE IDs in title for the LMS/LM-OTS GT. |
| `full` | `GEN-003` | `GT-005` | Wrong CVE attribution for the PEM integer-underflow GT. |
| `strict_1hop/full` | `GEN-001` | `GT-001` | Helper-only and vague CVE wording. |
| `strict_1hop/full` | `GEN-003` | `GT-005` | Wrong CVE attribution for the PEM integer-underflow GT. |

Additional rows needing reviewer decision:

| Variant | Generated IDs | Current GT | Concern |
| --- | --- | --- | --- |
| `no_graph` | `GEN-003`, `GEN-004`, `GEN-005`, `GEN-006`, `GEN-010`, `GEN-011` | `GT-001` | Many notes mention the wrong CVE family for hostname verification. If strict accuracy includes CVE correctness, mark them non-match. |
| `no_graph` | `GEN-012`, `GEN-019`, `GEN-022` | `GT-003` | LMS/LM-OTS behavior is related, but generated summaries cite the wrong CVE family. |
| `no_graph` | `GEN-001` | `GT-005` | PEM behavior is related, but generated summary cites the wrong CVE family. |
| `full` | `GEN-007`, `GEN-010` | `GT-001` | Behavior is related to hostname handling, but generated summaries cite the wrong CVE family. |
| `full` | `GEN-020` | `GT-003` | LMS behavior is related, but generated summary cites the wrong CVE family. |
| `strict_1hop/full` | `GEN-004`, `GEN-007`, `GEN-008`, `GEN-017` | `GT-001` | Behavior is related to hostname handling, but generated summaries cite wrong or unsupported security details. |

Recommended action:

- For strict final metrics, prefer marking wrong-CVE generated entries as non-matches.
- If you want to preserve behavior matching separately from CVE correctness, add a separate manual label later, such as `match_with_unsupported_detail`; do not count those as clean strict matches in the main P/R/F1 table.

## Suggested Interpretation For Thesis

The current strict files are good enough to show that the evaluator wiring works and that many outputs map to the intended semantic families.

For defensible final results, tighten the semantic review before reporting final P/R/F1:

- curl can remain as-is.
- sqlite should remove helper/setup-only matches.
- mbedtls should penalize wrong CVE attribution and helper-only hostname notes.

This makes the evaluation less flattering but more credible. It also creates a useful thesis finding: security-component release notes require not only behavior matching but also precise vulnerability metadata, which the current prompt/backend combination does not always preserve.

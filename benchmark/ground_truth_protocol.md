# Ground-Truth Protocol

This document defines the ground-truth construction process for all C/C++ release-note benchmark cases in this project.

The protocol follows the evaluation spirit of VerLog: ground truth is a reviewed semantic summary built from shared evidence, not a direct copy of commit messages or generated model output.

All cases use the same GT entry definition, evidence admission standard, exclusion standard, and strict semantic matching rule. Core, extension, and sampled scopes are reporting scopes only; they do not represent different GT protocols. See `benchmark/unified_ground_truth_protocol.md`.

## Quality Criteria

A reviewed ground-truth release-note entry should satisfy:

- Completeness: covers a meaningful user-facing, developer-facing, compatibility, security, or behavior change.
- Accuracy: supported by code diff, commit messages, release notes, changelog entries, or inspected artifacts.
- Readability: concise enough to be used as a release note, not a low-level implementation trace.
- Traceability: links back to evidence items such as changed functions, commits, or official notes.

## Evidence Priority

Use evidence in this order:

- Official OpenHarmony platform release notes, when available.
- Component or upstream changelogs, such as curl `CHANGES`, mbedtls `ChangeLog`, or zlib `ChangeLog`.
- Commit messages between the selected tags.
- Function-level diff evidence from `changed_functions.json`.
- CMG and fallback evidence from `cmg.json`.
- Generated mock or LLM release notes only as drafting aids, never as authoritative ground truth.

## Per-Case Files

Each benchmark case should contain:

- `metadata.json`: machine-readable case state and artifact paths.
- `ground_truth.md`: reviewed semantic ground-truth entries and exclusions.
- `evidence.md`: generated evidence packet used to draft and review ground truth.

Generate `evidence.md` with:

```powershell
python -m cpp_release_note_mvp.cli build-ground-truth-evidence --metadata <case>\metadata.json
```

## Review Procedure

1. Generate or refresh `evidence.md`.
2. Inspect official release notes and component changelogs listed in the evidence checklist.
3. Inspect commit messages and function-level diff evidence.
4. Draft semantic release-note entries in `ground_truth.md`.
5. Move low-level implementation details to `Excluded Changes`.
6. Record uncertainty and disagreements in `Reviewer Notes`.
7. Mark `ground_truth.status` as `drafted` only after entries are filled.
8. Mark `ground_truth.status` as `reviewed` only after a second pass checks evidence support.
9. Mark `evaluation.eligible_for_core_eval` as `true` only after ground truth is reviewed.

## Entry Format

Use a table in `ground_truth.md`:

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Fix | ... | commit message; changed functions; official note | ... |

Recommended sections:

- Feature
- Fix
- Security
- Compatibility
- Performance
- Testing
- Maintenance

## Evaluation Use

During evaluation, generated release-note entries should be matched to ground-truth entries by semantic correspondence.

Primary metrics:

- Precision: matched generated entries divided by total generated entries.
- Recall: matched ground-truth entries divided by total ground-truth entries.
- F1: harmonic mean of precision and recall.

Additional metrics:

- Unsupported-claim rate.
- Redundancy rate.
- Structural validity.
- Runtime and token cost for real LLM backends.

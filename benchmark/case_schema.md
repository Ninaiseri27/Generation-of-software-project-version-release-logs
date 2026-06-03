# Benchmark Case Schema

Each benchmark case is one repository version pair.

Canonical path:

```text
benchmark/cases/<repository>/<version_pair_id>/metadata.json
```

## Required Fields

- `case_id`: stable identifier, usually `<repo>_<ref>_to_<tgt>` with normalized tag names.
- `repository.name`: repository name.
- `repository.url`: upstream repository URL.
- `repository.category`: domain category such as `database`, `network`, `compression`, or `security_crypto`.
- `version_pair.ref`: reference tag.
- `version_pair.tgt`: target tag.
- `benchmark_role`: one of `dev_demo`, `core_eval`, `patch_challenge`, `stress_test`, or `candidate`.
- `pipeline_status`: current pipeline state.
- `screening.stage1_status`: `not_started`, `passed`, `failed`, or `patch_only`.
- `screening.changed_cpp_files`: number of directly changed C/C++ files detected by Stage 1.
- `screening.changed_functions`: number of changed functions detected by Stage 1.
- `ground_truth.status`: one of `not_started`, `draft_required`, `drafted`, `reviewed`, or `admitted`.
- `ground_truth.path`: path to the case ground-truth Markdown file.
- `evaluation.eligible_for_core_eval`: whether this case is currently eligible for final evaluation.

## Recommended Fields

- `screening.commit_count`: number of commits between the two tags.
- `screening.patch_only`: whether the meaningful code changes are carried by patch files rather than direct source changes.
- `screening.stage1_output`: path to the generated `changed_functions.json`.
- `pipeline_artifacts`: paths to later outputs such as `cmg.json`, `prompt_bundle.json`, and `release_note.json`.
- `ground_truth.evidence_sources`: list of evidence sources that should be inspected.
- `ground_truth.evidence_path`: path to the generated `evidence.md` review packet.
- `baseline_plan`: method variants to run.
- `ablation_plan`: component ablations to run.
- `notes`: rationale, risks, and current decisions.

## Admission Rule

A case should not be marked as `core_eval` unless:

- Stage 1 has passed or the case has a patch-aware extraction path.
- Ground truth has at least one reviewed semantic release-note entry.
- The same input evidence can be used by all baseline and ablation variants.
- The case is not dominated by repository metadata or build-script-only changes unless that is the intended study target.

## Ground-Truth Evidence Packet

Each intended `core_eval` case should generate an `evidence.md` file before manual ground-truth drafting.

```powershell
python -m cpp_release_note_mvp.cli build-ground-truth-evidence --metadata benchmark/cases/<repository>/<version_pair_id>/metadata.json
```

The evidence packet is not itself ground truth. It is a review aid that consolidates case metadata, commit messages, changed functions, CMG matching status, diff snippets, and mock release-note drafts.

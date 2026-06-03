# C/C++ Release Note MVP

This repository contains a research prototype for automated release note generation on C/C++ repositories.

## Current Status

- Stage 1 is runnable.
- Stage 2 snapshot management is runnable.
- Stage 2 ENRE runner is runnable.
- Stage 2 ENRE normalization is runnable.
- Stage 2 CMG building is runnable.
- Stage 3 prompt building for single CMG entries is runnable in code.
- Stage 3 prompt-input and prompt-bundle generation are runnable.
- Stage 3 release-note generation is runnable with the mock backend.
- Stage 3 release-note generation is runnable with OpenAI-compatible real backends.
- Final selected benchmark is complete: 82 semantic GT entries, 11 case-version pairs, 8 method variants, and 88 evaluated case-variant cells.
- Final experiment matrix:
  - `benchmark/final_all_variant_matrix.md`
  - `benchmark/final_all_variant_matrix.json`
- Expanded robustness matrix is complete: 137 semantic GT entries, 13 case-version pairs, 8 method variants, and 104 evaluated case-variant cells.
- Expanded experiment matrix:
  - `benchmark/expanded_137gt_matrix.md`
  - `benchmark/expanded_137gt_matrix.json`
- First verified target repository: `openharmony/third_party_sqlite`
- First verified version pair:
  - `OpenHarmony-v6.0-Release`
  - `OpenHarmony-v6.0.0.1-Release`
- Second verified version pair:
  - `OpenHarmony-v5.0.1-Release`
  - `OpenHarmony-v5.0.2-Release`
- Current verified output:
  - `outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/changed_functions.json`
  - `outputs/third_party_sqlite/OpenHarmony-v5.0.1-Release__OpenHarmony-v5.0.2-Release/changed_functions.json`
- Benchmark expansion has started:
  - manifest: `benchmark/openharmony_cpp_benchmark.json`
  - methodology: `benchmark/README.md`
  - case schema: `benchmark/case_schema.md`
  - case metadata: `benchmark/cases/`
  - first additional Stage 1 candidates include `third_party_curl`, `third_party_zlib`, and `third_party_mbedtls`
- Current verified ENRE raw output:
  - `outputs/enre_raw/third_party_sqlite/OpenHarmony-v6.0-Release/third_party_sqlite__OpenHarmony-v6.0-Release_out.json`
  - `outputs/enre_raw/third_party_sqlite/OpenHarmony-v6.0.0.1-Release/third_party_sqlite__OpenHarmony-v6.0.0.1-Release_out.json`

## Scope

Current scope covers the end-to-end prototype pipeline:

- version-pair configuration
- Git diff collection
- C/C++ function extraction
- diff-hunk to function matching
- changed-function JSON generation
- ENRE graph extraction and normalization
- CMG/fallback context construction
- structured prompt construction
- LLM-based release note generation
- baseline, ablation, aggregation, and evaluation outputs

## Current Layout

- `configs/`: example configs
- `benchmark/`: benchmark manifests and candidate version-pair metadata
- `outputs/`: generated artifacts (ignored by Git)
- `prompts/`: generation prompts
- `samples/`: small sample inputs or snapshots
- `src/`: Python package source

## Development Setup

Install runtime dependencies and development tools into the project virtual environment:

```bash
python -m pip install -e ".[dev]"
```

Run lightweight validation:

```bash
python -m pytest
python -m compileall -q src\cpp_release_note_mvp
```

## Intended Usage

Recommended on this Windows workspace:

```bash
python -m cpp_release_note_mvp detect-changes --config configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Snapshot preparation for Stage 2:

```bash
python -m cpp_release_note_mvp prepare-snapshots --config configs/third_party_sqlite_head_to_master_smoke.json
```

ENRE execution for Stage 2:

```bash
python -m cpp_release_note_mvp run-enre --config configs/third_party_sqlite_v6_0_to_v6_0_0_1.json --target both
```

ENRE normalization for Stage 2:

```bash
python -m cpp_release_note_mvp parse-enre --input outputs/enre_raw/third_party_sqlite/OpenHarmony-v6.0-Release/third_party_sqlite__OpenHarmony-v6.0-Release_out.json
```

CMG building for Stage 2:

```bash
python -m cpp_release_note_mvp build-cmg --config configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

To enable the richer matching-only graph while keeping prompt-side CMG compact:

```bash
python -m cpp_release_note_mvp build-cmg --config configs/benchmark/third_party_curl_v6_0_beta1_to_v6_0.json --matching-view rich
```

Optional CMG tuning fields can be added under `cmg` in the JSON config:

```json
{
  "cmg": {
    "strategy": "adaptive",
    "matching_view": "strict",
    "context_hops": 1,
    "matched_hops": 1,
    "sparse_matched_hops": 2,
    "unmatched_expand_hops": 1,
    "unmatched_source_window_lines": 80,
    "unmatched_expand_from_diff_calls": true,
    "min_edges_for_sparse": 1,
    "include_parent_context": true,
    "include_diff_calls": true,
    "max_nodes": 30,
    "max_edges": 60
  }
}
```

Prompt preparation for Stage 3:

```bash
python -m cpp_release_note_mvp build-prompts --config configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Prompt evidence can be switched for baseline and ablation runs:

```bash
python -m cpp_release_note_mvp build-prompts --config configs/benchmark/third_party_curl_v6_0_beta1_to_v6_0.json --prompt-variant diff_only --prompt-input-output outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines/diff_only_prompt_input.json --prompt-bundle-output outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines/diff_only_prompt_bundle.json
```

Supported variants are `text_only`, `diff_only`, `no_graph`, `no_fallback`, and `full`.

To run all baseline variants for a prepared case:

```bash
python -m cpp_release_note_mvp run-baselines --config configs/benchmark/third_party_curl_v6_0_beta1_to_v6_0.json --backend mock --aggregation-strategy none
```

This writes `prompt_input.json`, `prompt_bundle.json`, `release_note.json`, and `release_note.md` under `<output_dir>/baselines/<variant>/`, plus `<output_dir>/baselines/baseline_summary.json`.

Evaluation template and metric computation:

```bash
python -m cpp_release_note_mvp evaluate-release-notes --ground-truth benchmark/cases/third_party_curl/curl_v6_0_beta1_to_v6_0/ground_truth.md --release-note outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines/full/release_note.json --match-template-output outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines/full/match_template.json
```

See `benchmark/evaluation_protocol.md` for the manual-match workflow and metric definitions.

To prepare evaluation templates for all baseline variants across the current medium cases:

```bash
python -m cpp_release_note_mvp evaluate-baselines --metadata benchmark/cases/third_party_curl/curl_v6_0_beta1_to_v6_0/metadata.json benchmark/cases/third_party_sqlite/sqlite_v6_0_0_2_to_v6_1/metadata.json benchmark/cases/third_party_mbedtls/mbedtls_v6_0_beta1_to_v6_0/metadata.json --summary-output outputs/benchmark/evaluation_preparation_summary.json
```

To build a report-facing evaluation table:

```bash
python -m cpp_release_note_mvp summarize-evaluations --metadata benchmark/cases/third_party_curl/curl_v6_0_beta1_to_v6_0/metadata.json benchmark/cases/third_party_sqlite/sqlite_v6_0_0_2_to_v6_1/metadata.json benchmark/cases/third_party_mbedtls/mbedtls_v6_0_beta1_to_v6_0/metadata.json --json-output outputs/benchmark/evaluation_summary.json --markdown-output outputs/benchmark/evaluation_summary.md
```

To build a self-contained HTML report for thesis slides or advisor review:

```bash
python -m cpp_release_note_mvp build-visual-report --benchmark-root benchmark --cmg-input outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/cmg.json --cmg-coverage-input benchmark/cmg_coverage_core5.json --output benchmark/visual_report_final_82gt.html --json-output benchmark/visual_report_final_82gt.json --title "Final 82-GT C/C++ Release Note Experiment Report"
```

When `benchmark/final_all_variant_matrix.json` exists, this command uses the final 82-GT matrix automatically. The older core5 matrix is used only as a fallback.

To build a report from the expanded 137-GT robustness matrix:

```bash
python -m cpp_release_note_mvp build-visual-report --benchmark-root benchmark --matrix-input benchmark/expanded_137gt_matrix.json --output benchmark/visual_report_expanded_137gt.html --json-output benchmark/visual_report_expanded_137gt.json --title "Expanded 137-GT C/C++ Release Note Experiment Report"
```

To build a stable browser demo for advisor presentation from cached artifacts:

```bash
python -m cpp_release_note_mvp build-demo --case sqlite --output outputs/demo/sqlite_demo
```

This writes `index.html`, `run_log.md`, `demo_payload.json`, and a packaged `artifacts/` directory. The default demo is cached and does not rerun Git diff, ENRE, or LLM calls, so it is suitable for live presentation.

Release-note generation for Stage 3:

```bash
python -m cpp_release_note_mvp generate-release-notes --config configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Aggregation strategy can be controlled for baseline and ablation runs:

```bash
python -m cpp_release_note_mvp generate-release-notes --config configs/benchmark/third_party_curl_v6_0_to_v6_0_0_1.json --backend mock --aggregation-strategy exact
```

Real backend switch for Stage 3:

- set `generation.backend` to `openai`
- set `generation.model_name` to a real model id
- keep `generation.base_url` pointing to your provider's OpenAI-compatible base URL
- set the API key through `OPENAI_API_KEY` or the env var named by `generation.api_key_env`

Provider-ready configs for the verified sqlite version pair:

- `configs/third_party_sqlite_v6_0_to_v6_0_0_1_openai.json`
- `configs/third_party_sqlite_v6_0_to_v6_0_0_1_deepseek.json`

Recommended real-call smoke tests that keep provider outputs separate:

```bash
python -m cpp_release_note_mvp generate-release-notes --config configs/third_party_sqlite_v6_0_to_v6_0_0_1_openai.json --prompt-bundle-input outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/prompt_bundle_matched_only.json --json-output outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/release_note_openai_smoke.json --markdown-output outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/release_note_openai_smoke.md
```

```bash
python -m cpp_release_note_mvp generate-release-notes --config configs/third_party_sqlite_v6_0_to_v6_0_0_1_deepseek.json --prompt-bundle-input outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/prompt_bundle_matched_only.json --json-output outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/release_note_deepseek_smoke.json --markdown-output outputs/third_party_sqlite/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/release_note_deepseek_smoke.md
```

Notes for the provider configs:

- `third_party_sqlite_v6_0_to_v6_0_0_1_openai.json` defaults to `gpt-4.1-mini`; change `generation.model_name` if your account exposes a different chat-completions model.
- `third_party_sqlite_v6_0_to_v6_0_0_1_deepseek.json` defaults to `deepseek-v4-flash` with `generation.extra_body.thinking.type = disabled`; use `deepseek-v4-pro` only for selected high-value final runs.
- Older DeepSeek aliases such as `deepseek-chat` and `deepseek-reasoner` should be avoided in new configs because DeepSeek lists them as deprecated compatibility aliases.

The expected output of stage 1 is a `changed_functions.json` artifact for a concrete version pair.
The expected output of stage 2 step 3 is an ENRE raw JSON artifact under `outputs/enre_raw/`.
The expected output of stage 2 step 4 is a normalized ENRE graph JSON next to the raw file.
The expected output of stage 2 step 5 is a `cmg.json` artifact under the configured `output_dir`.
The expected output of stage 3 step 1 is a `prompt_input.json` and `prompt_bundle.json` pair under the configured `output_dir`.
The expected output of stage 3 step 2 is a `release_note.json` and `release_note.md` pair under the configured `output_dir`.

## Notes

- The current symbol extractor uses `tree-sitter-cpp` with regex fallback.
- ENRE-cpp is currently integrated at the runner level.
- ENRE raw parsing is now implemented via `pipeline/enre_parser.py`.
- The normalized ENRE graph now separates a compact prompt graph from a richer matching-only graph.
- The compact prompt graph is still hard-filtered to function-like entities and `call` edges only.
- The matching-only graph retains extra symbol-bearing entities such as classes, macros, files, and relation bridges for improved CMG matching coverage.
- Each retained function entity includes an `is_user_defined` heuristic flag for later CMG pruning.
- Changed-function to ENRE-entity matching and 1-hop CMG construction are now implemented.
- Matcher now includes a `symbol+overlap` fallback level after path-based matching.
- `build-cmg --matching-view rich` can use the richer matching-only graph and then project matching-only entities back to function-like prompt graph nodes.
- Current sqlite spot-check result is intentionally partial: `DestroyDbFile` matches, while `fts5SegIterAllocTombstone` and macro-based test entries still fall back to `unmatched_symbols`.
- CMG builder now emits `fallback_context` for unmatched or sparse-CMG entries, including pseudo changed nodes, diff-derived call symbols, compact resolved call evidence, and changed identifiers.
- Adaptive CMG is now available through `cmg.strategy = adaptive`.
- Unmatched entries can now receive synthetic changed nodes inside `cmg.nodes` and diff-derived `call` edges inside `cmg.edges`.
- Sparse matched entries can be supplemented with diff-derived calls instead of staying as single-node graphs.
- Stage 3 now has an initial `pipeline/prompt_builder.py` that formats one CMG entry into system/user prompts.
- Stage 3 prompts now include fallback evidence so unmatched ENRE entities no longer become empty-context model inputs.
- Stage 3 batch prompt artifacts are documented in `src/schemas/prompt_input_schema.md`.
- `build-prompts --matched-only` can be used when you only want prompt-ready entries with CMG matches.
- `build-prompts --prompt-variant text_only|diff_only|no_graph|no_fallback|full` can be used to create comparable baseline prompt bundles from the same case artifacts.
- `run-baselines` is the repeatable P2 entrypoint for generating all baseline prompt bundles and mock/real release-note outputs from existing `changed_functions.json` and `cmg.json`.
- `evaluate-release-notes` prepares manual match templates and computes precision/recall/F1 once a `matches.json` file is supplied.
- `evaluate-baselines` runs the same evaluation preparation/computation across baseline outputs for one or more benchmark cases.
- `summarize-evaluations` builds JSON and Markdown summary tables from generated evaluation files.
- `rewrite-aggregation` rewrites an existing `release_note.json` with a different aggregation strategy without rerunning the LLM backend.
- `summarize-experiments` builds a thesis-oriented core5 experiment matrix from the existing evaluation, output, ablation, and aggregation summaries.
- The final 82-GT all-variant matrix is materialized under `benchmark/final_all_variant_matrix.md/json`.
- The expanded 137-GT robustness matrix is materialized under `benchmark/expanded_137gt_matrix.md/json`.
- `build-visual-report` builds a self-contained HTML visualization from the final matrix when available, otherwise from the core5 matrix, plus optional CMG samples.
- Stage 3 generation is currently verified through a deterministic `mock` backend and also supports a real `openai` HTTP backend.
- Real generation prefers API keys from environment variables, with `OPENAI_API_KEY` as the default fallback.
- Stage 3 now normalizes backend responses into a structured release-note contract with `section`, `title`, and `summary`.
- Grouped Markdown rendering is now available for cleaner report/demo output.
- A deterministic aggregation layer now supports `none`, `exact`, `rule_family`, `similarity_family`, `evidence_similarity_family`, and experimental `salience_similarity_family` strategies for report-facing final entries.
- Experimental and report-facing generation runs can be organized under `outputs/<project>/<version-pair>/runs/release_note_generation/`.
- Release-note output artifacts are documented in `src/schemas/release_note_output_schema.md`.
- On this machine, `python` in `PATH` may still point to the Windows Store stub, so prefer the project-local interpreter or `py -3`.

# C/C++ Release Note MVP

This repository contains a prototype pipeline for generating release-note drafts from C/C++ project version pairs. It is designed around OpenHarmony third-party repositories, but the pipeline is generic enough to run on other Git-based C/C++ projects.

## Pipeline

1. Detect changed C/C++ functions from a Git version pair.
2. Prepare detached source snapshots for the reference and target versions.
3. Run ENRE-CPP and normalize the raw call graph.
4. Match changed functions to graph entities and build CMG context.
5. Build LLM prompts from diff and graph evidence.
6. Generate structured release-note drafts with either a mock backend or an OpenAI-compatible backend.

## Repository Layout

- `cpp_release_note_mvp/src/`: Python package source.
- `cpp_release_note_mvp/configs/`: runnable example configs with relative paths.
- `cpp_release_note_mvp/benchmark/`: benchmark candidate manifest.
- `cpp_release_note_mvp/docs/`: public benchmark notes.
- `cpp_release_note_mvp/prompts/`: prompt templates.
- `cpp_release_note_mvp/outputs/`: generated outputs, ignored except `.gitkeep`.

## Setup

```powershell
python -m venv cpp_release_note_mvp/.venv
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m pip install -e .\cpp_release_note_mvp
```

For Stage 2 graph extraction, download ENRE-CPP separately and place it at `tools/ENRE-CPP.jar`, or update `enre.enre_jar_path` in the config.

## Example Source Checkout

```powershell
git clone https://github.com/openharmony/third_party_sqlite.git cpp_release_note_mvp/workspaces/third_party_sqlite
```

## Basic Usage

Detect changed functions:

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp detect-changes --config cpp_release_note_mvp/configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Prepare version snapshots:

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp prepare-snapshots --config cpp_release_note_mvp/configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Run ENRE-CPP:

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp run-enre --config cpp_release_note_mvp/configs/third_party_sqlite_v6_0_to_v6_0_0_1.json --target both
```

Build CMG context:

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp build-cmg --config cpp_release_note_mvp/configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Build prompts:

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp build-prompts --config cpp_release_note_mvp/configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

Generate release-note drafts with the deterministic mock backend:

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp generate-release-notes --config cpp_release_note_mvp/configs/third_party_sqlite_v6_0_to_v6_0_0_1.json
```

## Real LLM Backends

The generation layer supports OpenAI-compatible chat completion endpoints. Keep API keys in environment variables, not in config files.

```powershell
$env:OPENAI_API_KEY = "your-key"
$env:DEEPSEEK_API_KEY = "your-key"
```

Provider-specific example configs are available under `cpp_release_note_mvp/configs/`.

## Public Data Policy

This public repository intentionally excludes local workspaces, generated outputs, private documents, API keys, and large third-party analysis binaries.

# C/C++ Release Note MVP

This directory contains the implementation package for the automated C/C++ release-note generation prototype.

For public setup and usage instructions, see the repository-level `README.md`.

## Current Capabilities

- Git version-pair configuration.
- Unified diff collection.
- C/C++ function extraction with tree-sitter and regex fallback.
- Diff hunk to function matching.
- Changed-function JSON generation.
- Git worktree based version snapshot preparation.
- ENRE-CPP execution wrapper.
- ENRE raw graph normalization.
- CMG construction with strict and adaptive context modes.
- Prompt bundle construction.
- Mock and OpenAI-compatible release-note generation backends.

## Layout

- `configs/`: runnable example configs with relative paths.
- `benchmark/`: benchmark manifests and candidate version-pair metadata.
- `docs/`: public benchmark notes.
- `outputs/`: generated artifacts, ignored except `.gitkeep`.
- `prompts/`: prompt templates.
- `src/cpp_release_note_mvp/`: Python package source.

## Notes

- Source repositories are expected under `workspaces/`, which is ignored by Git.
- ENRE-CPP is not vendored. Download it separately and configure `enre.enre_jar_path`.
- Real LLM API keys should be provided through environment variables.

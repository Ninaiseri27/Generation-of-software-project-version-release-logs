# Benchmark Expansion Plan

Last updated: 2026-04-30

This document records the first post-midterm benchmark expansion beyond `third_party_sqlite`.

## Goal

Build a reproducible OpenHarmony C/C++ benchmark for release-note generation.

Initial target:

- `5-10` OpenHarmony C/C++ repositories.
- At least `5` adjacent tag version pairs.
- Stage 1 change-detection outputs for all candidates before expensive ENRE runs.
- Full Stage 2/3 runs only for candidates with meaningful changed-function volume.

## Current Candidate Set

The canonical machine-readable manifest is:

- `cpp_release_note_mvp/benchmark/openharmony_cpp_benchmark.json`

Initial repositories:

- `third_party_sqlite`: database, already verified through full pipeline for one pair.
- `third_party_libpng`: image codec, selected as a small/medium C repository.
- `third_party_curl`: network library, selected as a realistic medium C repository.
- `third_party_zlib`: compression library, selected as a small C repository.
- `third_party_mbedtls`: security/crypto library, selected as a compact crypto candidate.
- `third_party_libxml2`: XML parser library, currently patch-only for the tested pair.
- `third_party_openssl`: security/crypto library, selected as a larger secondary candidate.

## Initial Version Pairs

Primary verified or smoke-test pairs:

- `third_party_sqlite`: `OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release`
- `third_party_sqlite`: `OpenHarmony-v5.0.1-Release -> OpenHarmony-v5.0.2-Release`
- `third_party_libpng`: `OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release`
- `third_party_curl`: `OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release`
- `third_party_zlib`: `OpenHarmony-v6.0.0.1-Release -> OpenHarmony-v6.0.0.2-Release`
- `third_party_mbedtls`: `OpenHarmony-v6.0.0.1-Release -> OpenHarmony-v6.0.0.2-Release`

Stage 1 smoke results on 2026-04-30:

| Repository | Version Pair | Changed C/C++ Files | Changed Functions | Decision |
| --- | --- | ---: | ---: | --- |
| `third_party_sqlite` | `v6.0 -> v6.0.0.1` | 4 | 4 | Keep for full-pipeline demo |
| `third_party_sqlite` | `v5.0.1 -> v5.0.2` | 1 | 20 | Keep for benchmark |
| `third_party_curl` | `v6.0 -> v6.0.0.1` | 17 | 47 | Keep; high-value medium sample |
| `third_party_zlib` | `v6.0.0.1 -> v6.0.0.2` | 2 | 2 | Keep; small CVE-style sample |
| `third_party_mbedtls` | `v6.0.0.1 -> v6.0.0.2` | 1 | 2 | Keep; small crypto/security sample |
| `third_party_libpng` | `v6.0 -> v6.0.0.1` | 0 | 0 | Deprioritize; patch-only diff |
| `third_party_libxml2` | `v6.0.0.1 -> v6.0.0.2` | 0 | 0 | Deprioritize; patch-only diff |

## Stage 1 Smoke Commands

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp.cli detect-changes --config cpp_release_note_mvp/configs/benchmark/third_party_libpng_v6_0_to_v6_0_0_1.json
```

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp.cli detect-changes --config cpp_release_note_mvp/configs/benchmark/third_party_curl_v6_0_to_v6_0_0_1.json
```

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp.cli detect-changes --config cpp_release_note_mvp/configs/benchmark/third_party_zlib_v6_0_0_1_to_v6_0_0_2.json
```

```powershell
.\cpp_release_note_mvp\.venv\Scripts\python.exe -m cpp_release_note_mvp.cli detect-changes --config cpp_release_note_mvp/configs/benchmark/third_party_mbedtls_v6_0_0_1_to_v6_0_0_2.json
```

## Selection Policy

Use Stage 1 output to rank version pairs:

- Prefer pairs with `3-50` changed functions for manual inspection and full ENRE runs.
- Deprioritize pairs with `0` changed functions or only repository metadata changes.
- Keep large repositories such as `third_party_openssl` as secondary candidates until smaller repos establish the benchmark workflow.

## Next Steps

1. Promote useful pairs to full Stage 2/3 runs, starting with `third_party_curl`.
2. Keep `third_party_zlib` and `third_party_mbedtls` as compact CVE/security-style samples.
3. Keep patch-only pairs as separate benchmark cases only after adding patch-file extraction support.
4. Start collecting ground truth from release notes, changelogs, tag messages, commit messages, and PR/MR summaries.

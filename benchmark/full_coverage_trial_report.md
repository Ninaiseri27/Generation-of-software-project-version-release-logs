# Full Coverage Trial Report

Generated on: 2026-05-29

This report records a controlled trial for replacing sampled stress scopes with full changed-function coverage. The goal is not to admit the cases automatically, but to measure the engineering cost and decide whether full-scope GT and evaluation are worth adding.

## Trial Scope

| Case | Existing final role | Full changed functions | Sampled changed functions | Full CMG status | Full prompt status |
| --- | --- | ---: | ---: | --- | --- |
| `third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release` | sampled stress | 1123 | 80 | completed | completed for all six prompt variants |
| `upstream_git v2.52.0 -> v2.53.0` | sampled extension | 905 | 80 | completed | completed for `full` and `diff_only` |

## Stage 1 Scale

| Case | Changed functions | Changed C/C++ files | Unique symbols | Change-type profile | Total hunk lines |
| --- | ---: | ---: | ---: | --- | ---: |
| `third_party_pcre2` | 1123 | 62 | 505 | 950 deleted, 113 modified, 60 added | 52560 |
| `upstream_git_2_52_to_2_53` | 905 | 183 | 740 | 400 modified, 285 added, 220 deleted | 8873 |

Interpretation:

- PCRE2 is dominated by deleted SLJIT/JIT backend functions. Full coverage is useful as a scale stress test, but many function-level changes are implementation churn rather than independent release-note facts.
- Git 2.53 has broader source-file coverage and a healthier mix of modified, added, and deleted functions. It is a stronger candidate for full-scope semantic GT expansion because official release notes are rich and source-backed.

## Stage 2 CMG Result

| Case | CMG entries | Prompt-node matches | Unmatched symbols | Matched rate | Runtime observation |
| --- | ---: | ---: | ---: | ---: | --- |
| `third_party_pcre2` | 1123 | 806 | 241 unique symbols | 71.77% by entry | completed in about 7 seconds |
| `upstream_git_2_52_to_2_53` | 905 | 900 | 4 unique symbols | 99.45% by entry | completed in about 32 seconds |

Commands:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli build-cmg `
  --config configs/benchmark/third_party_pcre2_v6_0_0_2_to_v6_1.json `
  --changed-input outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/changed_functions.json `
  --ref-normalized-graph-input outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/ref_normalized_graph.json `
  --tgt-normalized-graph-input outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/tgt_normalized_graph.json `
  --output outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/cmg.json
```

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli build-cmg `
  --config configs/benchmark/upstream_git_2_52_0_to_2_53_0.json `
  --changed-input outputs/benchmark/upstream_git/v2.52.0__v2.53.0/changed_functions.json `
  --ref-normalized-graph-input outputs/benchmark/upstream_git/v2.52.0__v2.53.0/ref_normalized_graph.json `
  --tgt-normalized-graph-input outputs/benchmark/upstream_git/v2.52.0__v2.53.0/tgt_normalized_graph.json `
  --output outputs/benchmark/upstream_git/v2.52.0__v2.53.0/full_coverage/cmg.json
```

## Stage 3 Prompt Cost

| Case | Variant | Prompt entries | Bundle size | Approx input tokens | Avg chars per entry | Max chars per entry |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `third_party_pcre2` | `full` | 1123 | 8.82 MB | 2067932 | 7365.7 | 42311 |
| `third_party_pcre2` | `diff_only` | 1123 | 4.38 MB | 985246 | 3509.3 | 39716 |
| `third_party_pcre2` | `no_graph` | 1123 | 5.54 MB | 1322426 | 4710.3 | 40917 |
| `third_party_pcre2` | `no_fallback` | 1123 | 5.82 MB | 1394108 | 4965.7 | 41328 |
| `third_party_pcre2` | `strict_1hop_full` | 1123 | 7.47 MB | 1823007 | 6493.3 | 42310 |
| `upstream_git_2_52_to_2_53` | `full` | 905 | 7.03 MB | 1671380 | 7387.3 | 24042 |
| `upstream_git_2_52_to_2_53` | `diff_only` | 905 | 2.33 MB | 512418 | 2264.8 | 7453 |

Commands:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli build-prompts `
  --config configs/benchmark/third_party_pcre2_v6_0_0_2_to_v6_1.json `
  --changed-input outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/changed_functions.json `
  --cmg-input outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/cmg.json `
  --prompt-input-output outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/prompt_input_full.json `
  --prompt-bundle-output outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/prompt_bundle_full.json `
  --prompt-variant full
```

Use the same command shape with `--prompt-variant diff_only`, and replace paths with the upstream Git output directory for Git 2.53.

Current PCRE2 real-backend status: DeepSeek full-scope generation is complete for all selected method variants. The earlier `diff_only` quota interruption was recovered by retrying only the failed entries and merging the retry output. OpenAI smoke testing with `gpt-4.1-mini` still failed with `HTTP 429 insufficient_quota`, so the admitted PCRE2 full-scope matrix uses DeepSeek only. See `benchmark/pcre2_full_scope_all_methods_status.md`.

## Admission Implications

Full coverage should change the evaluation boundary, not the definition of a GT item.

GT entries remain semantic release-note facts. They should not become "one GT per changed function." A full-scope case should be admitted only after official or reviewed release-note evidence is audited over the full changed-function set.

## Preliminary GT Impact

### Git 2.53

Official source: `Documentation/RelNotes/2.53.0.adoc` in tag `v2.53.0`.

The release note contains `80` top-level bullets. The existing sampled GT keeps `15` high-evidence entries. A full-scope review can likely add material GT, but not all 80 bullets should be admitted:

| Category | Preliminary count | Treatment |
| --- | ---: | --- |
| Already represented by sampled GT | about 15 | Keep after re-checking source evidence. |
| Likely addable source-backed user/developer facts | about 18-24 | Review as full-scope GT candidates. |
| Documentation, CI, build, test, mailmap, cleanup, or pure refactor items | about 40+ | Exclude from P/R/F1 or keep only as notes. |

High-priority additional Git candidates:

- `git replay --onto` bad-argument diagnostic improvement.
- `git diff --quiet` rename/copy detection shortcut for performance.
- `git diff --find-copies-harder` artificial-filepair memory reduction.
- `git diff-files -R --find-copies-harder` index copy-source handling.
- Promisor object enumeration optimization.
- `git bugreport` and `git version --build-options` gettext diagnostic reporting.
- macOS keychain credential helper idempotent-store fix.
- `git repo structure` display-width fix.
- Windows credential helper under-allocation fix.
- `git config unset -h` option-help correction.
- `git config set` multi-value error-message correction.
- `git replay` omission of `gpgsig-sha256`.
- Additional `git submodule add` crash fix for missing `.gitmodules` path.
- Tag overwrite backfill behavior in `git fetch`.
- Avoiding no-op MIDX rewrite in `git repack`.
- `git diff --name-only` use-after-free with promisor objects.
- `git cat-file` performance regression fix.
- `git fsck` inconsistent-ref warning fix.
- HTTP transport newline fix.
- `git repack --geometric` promisor-pack fix.
- MIDX wrong-checksum reuse fix.

Current expansion result: `benchmark/cases/upstream_git/git_2_52_0_to_2_53_0/ground_truth_full_candidate.md` drafts `39` full-scope candidate semantic GT entries. This expands the sampled `15` entries while still excluding documentation-only, localization-only, build-only, CI-only, test-only, mailmap-only, and cleanup-only items.

Expected effect: Git 2.53 can plausibly move from 15 sampled GT entries to a reviewed full-scope set near 39 entries after strict evaluation. This is large enough to affect thesis-scale conclusions, so it is the best first full-coverage expansion target.

### PCRE2 10.45/10.46

Official sources: `pcre2/NEWS` and `pcre2/ChangeLog` in the OpenHarmony `third_party_pcre2` workspace.

The existing sampled GT keeps `5` broad entries. Full-scope review should split some broad entries, but it should still avoid counting low-level SLJIT churn as independent user-facing changes.

Likely addable or splittable PCRE2 candidates:

- Keep CVE-2025-58050 as one security GT.
- Split scan-substring assertions, UTS#18 extended classes, and Perl-style extended classes into separate pattern-syntax GT entries.
- Split Unicode UCD 16, Perl-compatible Unicode-property caseless behavior, Turkish casing, and stricter `\x` parsing when source evidence is clear.
- Split API/configuration facts such as `pcre2_set_optimize()`, `PCRE2_ERROR_JIT_UNSUPPORTED`, and new extra options when they are separately generated.
- Keep substitution replacement handling as one or more entries depending on generation granularity.
- Consider pcre2grep/pcre2test behavior only if the thesis wants tool-facing release notes, not just library API/runtime behavior.
- Treat SLJIT submodule migration, JIT backend churn, CI/build metadata, and per-architecture backend rewrites as stress evidence unless a stable release-note claim can be stated.

Current expansion result: `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/ground_truth_full_candidate.md` drafts `16` full-scope candidate semantic GT entries. The file keeps security, API, syntax, matching behavior, substitution behavior, Unicode behavior, JIT-visible behavior, and tool-facing behavior as candidates while excluding CI/build/test/static-analysis/OAT cleanup and per-architecture SLJIT churn by default.

Expected effect: PCRE2 may increase from 5 sampled GT entries to roughly 16 reviewed semantic entries if tool-facing entries are kept. It is useful for scale and security/API coverage, but less clean than Git 2.53 because many changed functions come from implementation migration rather than independent release-note facts.

Recommended inclusion gates:

1. Derive a full-scope GT candidate list from official release notes or changelogs.
2. Retain only user/developer-visible behavior, API, security, compatibility, diagnostics, or performance facts.
3. Map every admitted GT item to source evidence in the full changed-function artifact.
4. Run at least `diff_only`, `full_strict_1hop`, and `full_similarity_family` before adding the case to the final matrix.
5. Fill `matches_strict.json` against the full-scope GT and generated entries.
6. Admit the case only if the added GT materially changes coverage or stress conclusions without making the main table dominated by one oversized repository.

## Current Decision

Do not immediately replace the final 82-GT matrix. The trial shows that full CMG and prompt construction are feasible, but the next bottleneck is semantic GT admission and strict matching, not Stage 2 execution.

## First Full-Scope Generation Result

The first full-scope real-backend generation has been completed for Git 2.53 `diff_only`.

Result report:

- `benchmark/git_2_53_full_scope_diff_only_result.md`

Key result:

- `905/905` generated entries, `0` failures.
- Rule-family final notes: `878`.
- Similarity-family reaggregation final notes: `510`.
- Conservative strict result against `39` full-scope GT entries: precision `0.0911`, recall `0.8462`, F1 `0.1645`, unsupported rate `0.9089`.

Interpretation:

- Full-scope diff evidence scales technically and covers many GT facts.
- The output is too redundant for direct final reporting without stronger aggregation.
- Before adding this case to the final matrix, similarity-aggregated strict matching and at least one graph-context variant should be evaluated.

Recommended next step:

- Expand Git 2.53 from sampled GT to full-scope reviewed GT first, because its CMG coverage is high and its official release notes are rich.
- Expand PCRE2 more cautiously by splitting optional JIT/SLJIT and tooling items only when they can be stated as stable release-note facts. Avoid counting low-level per-architecture SLJIT churn as independent GT.
- After full-scope GT is drafted, run real LLM generation in stages: `diff_only` first, then graph/aggregation variants if the generated output is reviewable.

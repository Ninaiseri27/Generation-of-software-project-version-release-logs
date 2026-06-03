# Full-Scope Ground Truth Candidate: third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release

Status: `full_scope_candidate_not_evaluated`

This file expands the sampled PCRE2 stress GT into a full-scope candidate set. The unit is still a semantic release-note fact, not a changed function. Entries are derived from upstream `pcre2/NEWS`, `pcre2/ChangeLog`, local commit messages, and the full Stage 1 function-level diff.

This candidate file does not replace `ground_truth.md` or `ground_truth_strict.md` yet. It should be used only after full-scope generation outputs and `matches_strict.json` are prepared.

## Scope And Evidence

- Official sources: `pcre2/NEWS` and `pcre2/ChangeLog` in the local OpenHarmony `third_party_pcre2` workspace.
- Full Stage 1 output: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/changed_functions.json`.
- Full Stage 2 CMG output: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/cmg.json`.
- Full prompt bundles: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/full_coverage/prompt_bundle_full.json` and `prompt_bundle_diff_only.json`.
- Full scale: `1123` changed functions across `62` changed C/C++ files.
- Full CMG trial: `806` prompt-node matches and `241` unique unmatched symbols.

## Admission Rules

- Keep security, API, pattern syntax, matching behavior, substitution behavior, Unicode behavior, JIT-visible behavior, and user-facing tool behavior.
- Exclude CI-only, build-only, repository metadata, test-only, static-analysis cleanup, OAT warning cleanup, and pure per-architecture SLJIT churn unless a stable user/developer release-note fact can be stated.
- Treat broad SLJIT/JIT backend rewrites as supporting evidence, not as many independent GT entries.

## Full-Scope Candidate Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-P201 | Security | Update PCRE2 through 10.46 and include the CVE-2025-58050 fix for a read-past-the-end memory error involving attacker-controlled patterns that combine `(*ACCEPT)` with `(*scs:)`. | `pcre2/NEWS` and `pcre2/ChangeLog` describe CVE-2025-58050; full changed functions include `parse_regex`, `compile_branch`, and `match` in PCRE2 compile/match paths. | Carried over from sampled GT; keep precise CVE wording. |
| GT-P202 | Feature | Add scan-substring assertions that match captured text against a sub-pattern. | `pcre2/NEWS` and `ChangeLog` list scan substring; changed functions include `parse_regex`, `compile_branch`, `compile_regex`, and related compile-path helpers in `pcre2_compile.c`. | Split from the earlier broad pattern-syntax GT. |
| GT-P203 | Feature | Add UTS#18-compatible extended character classes through `PCRE2_ALT_EXTENDED_CLASS`. | `pcre2/NEWS` lists UTS#18 class operations; changed functions include `parse_class`, `compile_class_operand`, `compile_class_binary_tight`, `compile_class_binary_loose`, and `compile_eclass_nested` in `pcre2_compile_class.c`. | Split from the earlier broad pattern-syntax GT. |
| GT-P204 | Feature | Add Perl-style extended character classes using the `(?[...])` syntax. | `pcre2/NEWS` and `ChangeLog` list Perl-style extended classes; changed class compilation functions include `compile_eclass_nested`, `compile_class_unary`, and `compile_class_binary_loose`. | Split from the earlier broad pattern-syntax GT. |
| GT-P205 | Behavior | Update Unicode support to UCD 16. | `pcre2/NEWS` and `ChangeLog` list UCD 16; changed functions include Unicode/property compile paths such as `get_ucp`, `add_list_to_class_internal`, `get_nocase_range`, and xclass helpers. | User-visible matching behavior. |
| GT-P206 | Behavior | Align case-insensitive matching of Unicode properties `Ll`, `Lt`, and `Lu` with Perl behavior. | `pcre2/NEWS` and `ChangeLog` describe Perl-compatible property matching; changed functions include `get_ucp`, `get_nocase_range`, `utf_caseless_extend`, and class compilation helpers. | Split from the earlier Unicode/case behavior GT. |
| GT-P207 | Behavior | Make case-insensitive backreference matching respect `PCRE2_EXTRA_CASELESS_RESTRICT`. | `pcre2/NEWS` and `ChangeLog` list this match behavior change; changed functions include `match_ref` in `pcre2_match.c` and JIT reference matching functions. | User-visible match behavior. |
| GT-P208 | Behavior | Parse `\x` escapes more strictly instead of treating malformed escapes as NUL. | `pcre2/NEWS` and `ChangeLog` list stricter `\x` parsing; changed functions include `read_number`, `parse_regex`, and compile-path parsing helpers in `pcre2_compile.c`. | User-visible syntax compatibility change. |
| GT-P209 | API | Add `pcre2_set_optimize()` to control which optimizations are enabled. | `pcre2/NEWS` and `ChangeLog` list the new API; changed function `pcre2_set_optimize` appears in `pcre2_context.c`, with related config/test functions. | Developer-facing API. |
| GT-P210 | API | Add extra options including `PCRE2_EXTRA_NO_BS0`, `PCRE2_EXTRA_PYTHON_OCTAL`, `PCRE2_EXTRA_NEVER_CALLOUT`, and `PCRE2_EXTRA_TURKISH_CASING`. | `pcre2/NEWS` lists new extra options; changed functions include `show_compile_extra_options`, `process_pattern`, `parse_regex`, and matching/compile option handling paths. | Group options as one API/configuration GT unless generated output separates them. |
| GT-P211 | Behavior | Add Turkish casing controls via `PCRE2_EXTRA_TURKISH_CASING`, `(*TURKISH_CASING)`, and `(*CASELESS_RESTRICT)`. | `pcre2/NEWS` and `ChangeLog` describe Turkish casing and pattern flags; changed functions include `parse_regex`, `get_nocase_range`, `utf_caseless_extend`, and pcre2test option display paths. | Separate from general option availability because it changes matching behavior. |
| GT-P212 | API | Report unsupported JIT features through the new `PCRE2_ERROR_JIT_UNSUPPORTED` error code. | `pcre2/NEWS` and `ChangeLog` list the new JIT error; changed functions include `pcre2_get_error_message`, JIT compile helpers in `pcre2_jit_compile.c`, and related test/config paths. | Developer-facing JIT error reporting. |
| GT-P213 | Performance | Improve character-class matching by making compiled classes more compact and faster for large or complex character sets. | `pcre2/NEWS` describes class match-engine improvements; changed functions include `compile_optimize_class`, `PRIV` helpers in `pcre2_compile_class.c`, and `PRIV` xclass functions in `pcre2_xclass.c`. | Performance/size GT; keep if generated output mentions class matching. |
| GT-P214 | Feature | Extend `pcre2_substitute()` replacement syntax with octal escapes, Python-style backreferences, numbered and named backreferences, and whole-match variables. | `pcre2/NEWS` and `ChangeLog` list replacement-string extensions; changed functions include `pcre2_substitute`, `read_name_subst`, `find_text_end`, and pcre2test substitution paths. | Split from broad substitution GT. |
| GT-P215 | Feature | Add title-casing and locale-aware substitution case transformation through `pcre2_set_substitute_case_callout()`. | `pcre2/NEWS` and `ChangeLog` list title casing and custom case transformation; changed functions include `pcre2_set_substitute_case_callout`, `default_substitute_case_callout`, `do_case_copy`, and pcre2test `case_transform`. | Split from broad substitution GT. |
| GT-P216 | Tooling | Add or update user-facing PCRE2 tool behavior, including pcre2grep pattern-file handling and pcre2test reporting of new options and optimization flags. | `pcre2/ChangeLog` lists pcre2grep and pcre2test changes; changed functions include `read_pattern_file`, `handle_option`, and `main` in `pcre2grep.c`, plus `show_compile_extra_options`, `show_optimize_flags`, and `process_pattern` in `pcre2test.c`. | Optional in core library evaluation; keep only if tool-facing notes are in scope. |

## Excluded Or Optional Full-Scope Items

| Item | Decision | Reason |
| --- | --- | --- |
| SLJIT split into a Git submodule | Optional build/integration note | It is visible to Git checkout users, but it is mainly repository integration/build workflow rather than PCRE2 runtime/API behavior. |
| Many per-architecture SLJIT backend rewrites | Exclude from P/R/F1 by default | They dominate the changed-function count but do not map cleanly to independent release-note facts. |
| CI, Bazel, Zig, CMake, static-analysis cleanup, OAT cleanup | Exclude | Maintenance or build hygiene, not core user/developer release-note behavior under this benchmark. |
| Test-only and fuzz-support changes | Exclude as standalone GT | They can support behavior evidence but should not be counted as independent release-note entries unless they expose tool behavior. |
| Broad JIT improvements | Optional | Keep only when split into stable claims such as unsupported-feature error reporting or generated-code size reductions. |

## Expected Use

This file provides `16` candidate semantic GT entries. Before replacing the sampled PCRE2 GT in the final matrix:

1. Decide whether tool-facing entries such as GT-P216 are in scope.
2. Run real LLM generation for full-scope `diff_only`, `full_strict_1hop`, and `full_similarity_family`.
3. Create `matches_strict.json` files against this full-scope GT.
4. Report PCRE2 as a stress/full-scope case separately if its deleted-function-heavy SLJIT churn makes aggregate metrics unstable.

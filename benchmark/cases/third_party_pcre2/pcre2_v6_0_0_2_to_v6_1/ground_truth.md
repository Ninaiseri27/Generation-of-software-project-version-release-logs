# Ground Truth: third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release

Status: `reviewed_sampled_with_optional_exclusions`

This case is a large direct-source stress candidate, not an admitted `core_eval` case.

## Screening Summary

- Recent-pair screening report: `outputs/screening/third_party_pcre2_recent8.json`
- Full Stage 1 output: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/changed_functions.json`
- Sampled Stage 1 output: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_changed_functions.json`
- Sample summary: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_changed_functions_summary.md`
- Commit count: `12`
- Changed files: `360`
- Changed C/C++ files: `77`
- Changed functions: `1123`
- Sampled functions: `80`
- Sampled files: `62`
- Patch only: `false`
- Size bucket: `large`

## Admission Decision

Do not admit this case into `core_eval` yet.

The case is useful for scalability or sampled stress experiments, but a full ground-truth review over 1123 changed functions is not currently comparable with the core5 benchmark. Before any real DeepSeek generation or strict evaluation, define a sampling protocol that fixes:

- sampled modules or files;
- maximum changed functions;
- evidence packet format;
- reviewed GT scope;
- strict matching rules;
- whether metrics are reported separately from core5.

## Evidence Checklist

- [x] Stage 1 recent-pair screening completed.
- [x] Large direct-source candidate identified.
- [x] Sampling protocol defined.
- [x] Sampled changed-functions artifact generated.
- [x] Evidence packet generated for sampled scope.
- [x] Ground truth drafted from sampled evidence.
- [ ] Strict matches reviewed.

## Reviewed Sampled Release Note Entries

These entries are reviewed for the sampled stress protocol only. They are not core-eval GT and must not be mixed into the core5 average.

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-S01 | Security | Update PCRE2 through 10.46 and include the CVE-2025-58050 fix for a read-past-the-end memory error involving attacker-controlled patterns that combine `(*ACCEPT)` with `(*scs:)`. | Local commit `feat: update pcre2 to version of 10.46`; `pcre2/NEWS` states 10.46 is a security-only release for CVE-2025-58050; `pcre2/ChangeLog` describes the read-past-end issue; sampled compile/match functions include `parse_regex`, `compile_branch`, and `match`. | Keep. Strong upstream NEWS/ChangeLog evidence. Wording must stay limited to pattern-triggered read-past-end behavior. |
| GT-S02 | Feature | Add PCRE2 10.45 pattern-syntax features, including scan-substring assertions and extended character-class syntax for UTS#18-style and Perl-style set operations. | `pcre2/NEWS` lists scan substring, `PCRE2_ALT_EXTENDED_CLASS`, and Perl-style `(?[...])`; sampled functions include `parse_regex`, `compile_optimize_class`, `PRIV` in `pcre2_compile_class.c`, and `PRIV` in `pcre2_xclass.c`. | Keep. This is a user-visible pattern syntax group. |
| GT-S03 | Behavior | Update Unicode and case-handling behavior, including UCD 16 support, Perl-compatible caseless handling for Unicode letter properties, Turkish casing options, and stricter parsing for `\\x` escapes. | `pcre2/NEWS` lists UCD 16, Ll/Lt/Lu caseless behavior alignment with Perl, `PCRE2_EXTRA_TURKISH_CASING`, `(*TURKISH_CASING)`, `(*CASELESS_RESTRICT)`, and stricter `\\x` parsing; sampled functions include `check_char_prop`, `get_chr_property_list`, `pcre2_pattern_convert`, and class-compilation functions. | Keep. It is broad but directly release-note visible and supported by upstream NEWS. |
| GT-S04 | API | Add new API controls and error reporting, including `pcre2_set_optimize()` for optimization selection and `PCRE2_ERROR_JIT_UNSUPPORTED` for unsupported JIT features. | `pcre2/NEWS` and `ChangeLog` list `pcre2_set_optimize()` and `PCRE2_ERROR_JIT_UNSUPPORTED`; sampled functions include `pcre2_set_optimize`, `pcre2_config`, `pcre2_get_error_message`, and JIT compile-path functions. | Keep. Developer-facing API/configuration GT. |
| GT-S05 | Feature | Extend substitution replacement handling with additional backreference forms, octal/Python-style replacement behavior, title casing, locale-aware case transformation callbacks, and related replacement syntax. | `pcre2/NEWS` lists replacement-string support for octal escapes, Python-style backrefs, `\\g<n>`, `$<name>`, `$&`, `$'`, `$_`, and `pcre2_set_substitute_case_callout()`; sampled functions include `pcre2_substitute`, `case_transform`, and `process_data`. | Keep. User/developer-visible replacement feature group. |

## Optional Or Excluded Sampled Entries

| Draft ID | Decision | Reason | Evidence |
| --- | --- | --- | --- |
| GT-S06 | Optional, exclude from sampled P/R/F1 by default | The JIT/SLJIT topic mixes performance, generated-code size, unsupported-feature reporting, submodule/build integration, and many architecture backend changes. It is too broad for strict release-note matching unless split into narrower GT items. | `pcre2/NEWS`; sampled `pcre2_jit_compile.c`, JIT include files, and many `sljit/*` files. |
| GT-S07 | Optional, exclude from sampled P/R/F1 by default | The tooling topic is partly user-visible but overlaps with test/reporting behavior. It is less central than library behavior/API/security changes and may make strict evaluation inconsistent. | `pcre2/NEWS`; sampled `pcre2grep.c`, `pcre2test.c`, and helper functions. |

## Excluded Or Low-Priority Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| OAT warning cleanup | OpenHarmony maintenance/compliance cleanup with low direct release-note value. | Commit messages `OAT告警清理`, `OAT告警处理20260114`; changed files such as `OAT.xml`. |
| CI and repository metadata updates | Build/CI hygiene is not core user-facing regex behavior unless the stress protocol explicitly evaluates build-system notes. | `.github/*`, Bazel/CMake/build script updates. |
| Test-only updates | Useful as evidence for behavior changes, but not standalone release-note GT unless they expose a user/developer-facing behavior. | `pcre2test`, fuzz support, and test infrastructure changes. |
| Per-architecture SLJIT low-level edits | Evidence for GT-S06 rather than independent release-note entries. | `pcre2/src/sljit/sljitNative*` and allocator files. |

## Reviewer Notes

- Keep this case outside the main matrix unless sampled GT and strict matches are completed.
- Do not compare full pcre2 stress results directly with core5 averages unless the thesis explicitly introduces a separate stress-test protocol.
- Reviewed sampled GT is based primarily on local `pcre2/NEWS`, `pcre2/ChangeLog`, commit messages, and the deterministic 80-function sample.
- Use GT-S01 through GT-S05 as the default sampled strict-evaluation set.
- Keep GT-S06 and GT-S07 as optional stress notes only unless they are split and reviewed separately.

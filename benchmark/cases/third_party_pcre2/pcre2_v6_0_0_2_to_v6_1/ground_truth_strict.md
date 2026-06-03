# Strict Ground Truth: third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release

Status: `reviewed_sampled_strict`

This file contains only the reviewed sampled GT entries used for strict P/R/F1 evaluation.
Optional or excluded stress notes are kept in `ground_truth.md` and intentionally omitted here.

## Reviewed Sampled Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-S01 | Security | Update PCRE2 through 10.46 and include the CVE-2025-58050 fix for a read-past-the-end memory error involving attacker-controlled patterns that combine `(*ACCEPT)` with `(*scs:)`. | Local commit `feat: update pcre2 to version of 10.46`; `pcre2/NEWS` states 10.46 is a security-only release for CVE-2025-58050; `pcre2/ChangeLog` describes the read-past-end issue; sampled compile/match functions include `parse_regex`, `compile_branch`, and `match`. | Keep. Strong upstream NEWS/ChangeLog evidence. Wording must stay limited to pattern-triggered read-past-end behavior. |
| GT-S02 | Feature | Add PCRE2 10.45 pattern-syntax features, including scan-substring assertions and extended character-class syntax for UTS#18-style and Perl-style set operations. | `pcre2/NEWS` lists scan substring, `PCRE2_ALT_EXTENDED_CLASS`, and Perl-style `(?[...])`; sampled functions include `parse_regex`, `compile_optimize_class`, `PRIV` in `pcre2_compile_class.c`, and `PRIV` in `pcre2_xclass.c`. | Keep. This is a user-visible pattern syntax group. |
| GT-S03 | Behavior | Update Unicode and case-handling behavior, including UCD 16 support, Perl-compatible caseless handling for Unicode letter properties, Turkish casing options, and stricter parsing for `\\x` escapes. | `pcre2/NEWS` lists UCD 16, Ll/Lt/Lu caseless behavior alignment with Perl, `PCRE2_EXTRA_TURKISH_CASING`, `(*TURKISH_CASING)`, `(*CASELESS_RESTRICT)`, and stricter `\\x` parsing; sampled functions include `check_char_prop`, `get_chr_property_list`, `pcre2_pattern_convert`, and class-compilation functions. | Keep. It is broad but directly release-note visible and supported by upstream NEWS. |
| GT-S04 | API | Add new API controls and error reporting, including `pcre2_set_optimize()` for optimization selection and `PCRE2_ERROR_JIT_UNSUPPORTED` for unsupported JIT features. | `pcre2/NEWS` and `ChangeLog` list `pcre2_set_optimize()` and `PCRE2_ERROR_JIT_UNSUPPORTED`; sampled functions include `pcre2_set_optimize`, `pcre2_config`, `pcre2_get_error_message`, and JIT compile-path functions. | Keep. Developer-facing API/configuration GT. |
| GT-S05 | Feature | Extend substitution replacement handling with additional backreference forms, octal/Python-style replacement behavior, title casing, locale-aware case transformation callbacks, and related replacement syntax. | `pcre2/NEWS` lists replacement-string support for octal escapes, Python-style backrefs, `\\g<n>`, `$<name>`, `$&`, `$'`, `$_`, and `pcre2_set_substitute_case_callout()`; sampled functions include `pcre2_substitute`, `case_transform`, and `process_data`. | Keep. User/developer-visible replacement feature group. |

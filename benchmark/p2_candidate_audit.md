# P2 Candidate Audit

Last updated: 2026-05-16

This note records the benchmark-extension decision after the core5 result scope was stabilized.

## Current Core Set

The current core evaluation set remains `core5`:

| Case | Role | Reviewed GT | Why It Stays |
| --- | --- | ---: | --- |
| `curl_v6_0_beta1_to_v6_0` | `core_eval` | 4 | Medium network case with OpenHarmony-specific curl behavior. |
| `mbedtls_v6_0_beta1_to_v6_0` | `core_eval` | 6 | Security-heavy TLS case with enough GT diversity. |
| `sqlite_v6_0_0_2_to_v6_1` | `core_eval` | 4 | Medium database case with security, reliability, and rekey/binlog behavior. |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `core_eval` | 1 | Low-GT compression/security-fix coverage; interpret cautiously. |
| `cjson_v6_0_beta1_to_v6_0` | `core_eval` | 2 | Low-GT JSON-parser coverage; interpret cautiously. |

## Candidate Screening

| Candidate | Changed Functions | Patch Only | GT Status | Current Decision |
| --- | ---: | --- | --- | --- |
| `curl_v6_0_to_v6_0_0_1` | 47 | No | `draft_candidate` | Highest-priority P2 candidate. |
| `mbedtls_v6_0_0_1_to_v6_0_0_2` | 2 | No | `draft_required` | Too small to materially improve benchmark scale. |
| `sqlite_v5_0_1_to_v5_0_2` | 20 | No | `draft_required` | Possible secondary candidate, but evidence still needs grouping. |
| `sqlite_v6_0_to_v6_0_0_1` | 4 | No | `draft_required` | Small case; less useful than curl expansion. |
| `libpng_v6_0_to_v6_0_0_1` | 0 | Yes | `not_started` | Keep as patch-only challenge, outside current method scope. |
| `libxml2_v6_0_0_1_to_v6_0_0_2` | 0 | Yes | `not_started` | Keep as patch-only challenge, outside current method scope. |
| `pcre2_v6_0_0_2_to_v6_1` | 1123 | No | `not_started` | Large direct-source stress candidate; requires fixed sampling scope before ENRE/LLM/GT. |
| `jsoncpp_recent8` | 0 | Yes | `not_started` | Recent pairs are patch-only or metadata-only under the current extractor. |
| `libjpeg_turbo_recent8` | 0 | Yes | `not_started` | Recent pairs are patch-only or metadata-only under the current extractor. |

Additional P2 screening note:

- `benchmark/p2_recent_screening_summary.md`

Recent screening decision:

- `third_party_pcre2` is the only newly screened repository with large direct C/C++ function changes. The preferred current-line stress pair is `OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release`, with `1123` changed functions across `77` C/C++ files.
- `third_party_jsoncpp` and `third_party_libjpeg-turbo` remain patch-challenge cases because their recent pairs are patch-only or metadata-only for the current direct-source extractor.
- Do not run full pcre2 real generation before defining a fixed sampling protocol; otherwise the result will be expensive and hard to compare with core5.

## Selected P2 Candidate

`curl_v6_0_to_v6_0_0_1` is selected as the next benchmark-extension candidate because:

- it is not patch-only;
- it has 47 changed functions and 17 changed C/C++ files;
- Stage 2/3 mock pipeline is already smoke-tested;
- adaptive fallback covers all 47 entries;
- it contains a coherent feature/security cluster around OpenHiTLS/GMSSL/TLCP plus CVE-2025-9086 cookie handling.

Current drafted GT entries:

| GT ID | Topic |
| --- | --- |
| `GT-001` | CVE-2025-9086 cookie path hardening. |
| `GT-002` | OpenHiTLS/TLCP 1.1 backend support. |
| `GT-003` | TLCP encrypted certificate/key options through libcurl and CLI. |

The GT is intentionally marked `draft_candidate`, not `reviewed`.

Source-strength audit:

- `GT-001` is strong because it is backed by curl's official CVE advisory, the local `fix CVE-2025-9086` commit, and cookie-function diffs.
- `GT-002` is medium strength because it is backed by OpenHarmony commit messages and broad OpenHiTLS/TLCP code diffs, but no independent upstream release-note entry has been mapped yet.
- `GT-003` is medium strength because the option and CLI evidence is direct; reviewer accepted keeping it separate from `GT-002` because it is an API/CLI exposure layer rather than backend implementation only.

## Admission Checklist

Before adding this case to the final evaluation matrix:

- review the 3 drafted GT entries in `ground_truth.md`;
- decide whether `cacert.pem` should remain excluded because it is data-only and invisible to function-level extraction;
- real DeepSeek baseline variants have been run for `text_only`, `diff_only`, `no_graph`, and `full`;
- `matches_strict.json` files have been created and audited for every real variant;
- strict evaluation has been run and unsupported claims have been inspected;
- only then change `eligible_for_core_eval` to `true`.

## Controlled Real-Backend Snapshot

A controlled real-backend snapshot now exists for all four main variants:

| Variant | Generated Notes | Precision | Recall | F1 | Current Reading |
| --- | ---: | ---: | ---: | ---: | --- |
| `text_only` | 1 | 1.0000 | 0.3333 | 0.5000 | Covers only the exact CVE entry. |
| `diff_only` | 47 | 0.6596 | 0.6667 | 0.6631 | Best current variant for this candidate. |
| `no_graph` | 45 | 0.6222 | 0.6667 | 0.6437 | Similar to diff-only but with more context noise. |
| `full` | 47 | 0.4681 | 0.6667 | 0.5500 | Highest token cost and weakest evidence-rich result. |

Strict matching for evidence-rich variants covers `GT-002` and `GT-003`, but not `GT-001`. The `text_only` output covers `GT-001` only by exact CVE identifier. Evidence-rich outputs include security-related unsupported claims that incorrectly associate CVE-2025-9086 with unrelated OpenHiTLS/OpenSSL changes, so this case should currently remain a P2 candidate rather than an automatic core-eval case.

Detailed audit note:

- `benchmark/core6_candidate_curl_v6_0_to_v6_0_0_1.md`
- `benchmark/core6_candidate_stress_analysis.md`
- `benchmark/curl_stress_aggregation_strict_eval.md`

Aggregated-note strict evaluation has also been completed for this candidate. The best aggregate setting is `diff_only + similarity_family`: it reduces final notes from 47 to 28 while keeping F1 close to the unaggregated `diff_only` result (`0.6545` vs `0.6631`). This supports using the case as an aggregation stress test, but it does not justify promoting it to core evaluation because the CVE GT remains uncovered by evidence-rich outputs.

## Current Decision

Do not expand `core5` yet.

The current recommendation is to report this candidate as a secondary stress case rather than immediately promoting it to a formal `core6` matrix. If it is promoted later, the thesis must explicitly discuss the high redundancy, weak GT-001 coverage in evidence-rich variants, and the manual policy that accepts exact CVE-only text as a minimal GT-001 match.

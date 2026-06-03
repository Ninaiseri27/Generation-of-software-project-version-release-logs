# Ground Truth: third_party_curl OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release

Status: `reviewed_extension`

Evidence packet:

- `benchmark/cases/third_party_curl/curl_v6_0_to_v6_0_0_1/evidence.md`

Pipeline status: full Stage 2/3 smoke test completed with mock backend on 2026-05-04.

## Evidence Checklist

- [x] Inspect `changed_functions.json`.
- [x] Run Stage 2/3 before final admission.
- [x] Inspect commit messages between the two tags.
- [x] Check curl CVE advisory for CVE-2025-9086.
- [x] Group related function-level changes into user/developer-visible release-note entries.
- [x] Human/assistant review before changing status to `reviewed_extension`.

## Pipeline Smoke Summary

- Changed functions: `47`.
- ENRE matched entries: `27`.
- Unmatched entries with adaptive fallback context: `20`.
- Fallback-context coverage: `47/47`.
- Mock generated entries: `47/47`.
- Aggregation smoke strategies tested: `none`, `exact`, `rule_family`.

The mock output validates pipeline wiring only. It should not be used as ground truth or final quality evidence.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Security | Fix CVE-2025-9086 by hardening libcurl cookie path handling so secure cookies cannot be incorrectly overridden through malformed or root-path cookie comparisons. | Commit `fix CVE-2025-9086`; curl advisory `https://curl.se/docs/CVE-2025-9086.html`; changed functions `sanitize_cookie_path`, `Curl_cookie_add`; diff changes the trailing-slash path condition and guards `spath` lookup before `strchr`. | Official curl advisory describes an out-of-bounds read in cookie path comparison. Treat as low-severity libcurl security/robustness GT. |
| GT-002 | Feature | Add OpenHiTLS/TLCP 1.1 backend support for curl TLS connections, including initialization, certificate loading, nonblocking connection setup, send/receive, close, and backend dispatch paths. | Commits `support gmssl`, `gmssl fix`, `!333 support gmssl 6.0 release`; changed functions `hitls_init`, `BuildCertStoreFromList`, `ParseAndSetCACertificate`, `ParseAndSetCertificate`, `ParseAndSetPrivateKey`, `hitls_connect_nonblocking*`, `hitls_recv`, `hitls_send`, `hitls_close`, and OpenSSL dispatch wrappers such as `ossl_init`, `ossl_connect_nonblocking`, `ossl_send`, `ossl_recv`, `ossl_close`. | Code evidence is primarily `USE_OPENHITLS`, `hitls_*`, and `CURL_SSLVERSION_TLCPv1_1`; `gmssl` is retained only as commit-message context, not as the strongest technical label. Many `hitls_*` entries are ENRE-unmatched but covered by fallback diff evidence. |
| GT-003 | Feature | Expose TLCP encrypted certificate and encrypted private-key configuration through libcurl options and the curl command-line interface. | Changed functions `Curl_vsetopt`, `Curl_ssl_easy_config_complete`, `clone_ssl_primary_config`, `Curl_free_primary_ssl_config`, `curl_easy_setopt_ccsid`, `getparameter`, `single_transfer`; diff adds `CURLOPT_SSLENCCERT`, `CURLOPT_SSLENCKEY`, `--enc-cert`, `--enc-key`, and related config storage/freeing paths. | Closely related to GT-002 but distinct enough for release-note evaluation because it exposes user/developer-facing API and CLI options. |

## Excluded Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| Merge commits | Merge-only history entries do not add independent release-note semantics beyond their child changes. | Commit messages beginning with `merge` or `!348 merge`. |
| `cacert.pem` update | Data/certificate bundle refresh is potentially useful as a compatibility/security note, but it is not represented in function-level C/C++ evidence. Exclude from core P/R/F1 unless a separate data-file-aware extraction baseline is added. | Commit `update cacert.pem`; no `changed_functions.json` item. |
| Low-level OpenHiTLS wrapper details | Helper-level functions are evidence for GT-002, not independent release-note entries. | Individual `hitls_*`, certificate-store helper, and dispatch-wrapper changes. |
| Placeholder or unsupported HITLS internals | `ossl_sha256sum`, `ossl_get_internals`, and `ossl_free_multi_ssl_backend_data` contain TODO/NULL-style handling and should not be counted as standalone user-facing behavior. | Function-level diff snippets in `lib/vtls/openssl.c`. |

## GT Source Audit

| GT ID | Evidence Strength | Primary Sources | Admission Decision |
| --- | --- | --- | --- |
| Source for GT-001 | Strong | Official curl CVE advisory, local commit `fix CVE-2025-9086`, and `lib/cookie.c` function-level diff. | Keep as a reviewed candidate after human check. The final wording must stay limited to cookie path comparison, secure-cookie override, and out-of-bounds read behavior. |
| Source for GT-002 | Medium | OpenHarmony commit messages plus broad OpenHiTLS/TLCP backend diff in `lib/vtls/openssl.c`, `lib/vtls/openssl.h`, `lib/vtls/vtls.c`, and dispatch wrappers. | Keep as a draft candidate, but do not mark reviewed until a reviewer accepts the OpenHiTLS/TLCP grouping. Avoid overstating GMSSL beyond commit-message evidence. |
| Source for GT-003 | Medium | API/CLI/config diff adding `CURLOPT_SSLENCCERT`, `CURLOPT_SSLENCKEY`, `--enc-cert`, `--enc-key`, and related storage/free paths. | Reviewer accepted keeping this as a separate candidate because it exposes user/developer-facing API and CLI configuration, while GT-002 captures backend implementation support. |

## Reviewer Notes

- Drafted from local commit messages, function-level diff evidence, and curl's official CVE-2025-9086 advisory.
- This case is a good P2 expansion candidate because it has 47 changed functions and a coherent medium/large network-security feature cluster.
- Do not admit to `core_eval` until the three GT entries above are reviewed and strict matches are prepared for real DeepSeek outputs.

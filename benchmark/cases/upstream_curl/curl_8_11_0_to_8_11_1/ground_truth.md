# Ground Truth: upstream curl curl-8_11_0 -> curl-8_11_1

Status: `reviewed_extension`

This file contains reviewed GT entries for the upstream curl extension case. The entries are derived from the official curl 8.11.1 `RELEASE-NOTES`, local commit messages, and Stage 1 function-level diffs.

## Admission Notes

- Role: `extension_eval` candidate.
- Official release-note source: `git show curl-8_11_1:RELEASE-NOTES`.
- Stage 1 output: `outputs/benchmark/upstream_curl/curl-8_11_0__curl-8_11_1/changed_functions.json`.
- Scope: prioritize release-note entries with direct C source evidence under `lib/`, `src/`, or public headers.
- Exclusion policy: build-only, CI-only, documentation-only, and test-only entries are excluded from strict GT unless they support a runtime/API behavior entry.
- Review policy: keep only entries that have official release-note support, function-level source evidence, and user/developer-visible behavior, diagnostics, API, CLI, or protocol meaning.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-U001 | Fix | Treat cookie names case-sensitively when parsing and replacing Netscape-format cookies. | Official `RELEASE-NOTES`: `cookie: treat cookie name case sensitively`; changed functions `parse_netscape` and `replace_existing` in `lib/cookie.c`. | User-visible cookie behavior fix. |
| GT-U002 | Fix | Harden `.netrc` parsing and support larger `.netrc` files, longer lines, and longer tokens. | Official `RELEASE-NOTES`: `netrc: address several netrc parser flaws` and `netrc: support large file, longer lines, longer tokens`; changed function `parsenetrc` in `lib/netrc.c`. | Grouped because both notes target the same parser behavior. |
| GT-U003 | Reliability | Use curl-managed custom memory callbacks for nghttp2 allocations. | Official `RELEASE-NOTES`: `nghttp2: use custom memory functions`; added functions `Curl_nghttp2_malloc`, `Curl_nghttp2_free`, `Curl_nghttp2_calloc`, and `Curl_nghttp2_realloc` in `lib/http2.c`. | Developer/runtime reliability item for HTTP/2 allocation behavior. |
| GT-U004 | Fix | Avoid resolving fully qualified `localhost` names through the normal resolver path. | Official `RELEASE-NOTES`: `hostip: don't use the resolver for FQDN localhost`; changed function `Curl_resolv` in `lib/hostip.c`. | Network behavior fix. |
| GT-U005 | Fix | Initialize netrc state correctly when duplicating easy handles. | Official `RELEASE-NOTES`: `duphandle: also init netrc`; changed function `curl_easy_duphandle` in `lib/easy.c`. | Developer-facing libcurl handle duplication behavior. |
| GT-U006 | Reliability | Fix integer-overflow checks in curl's formatted-output parser. | Official `RELEASE-NOTES`: `mprintf: fix the integer overflow checks`; changed function `parsefmt` in `lib/mprintf.c`. | Runtime robustness/security-adjacent parser hardening. |
| GT-U007 | Fix | Initialize PSA crypto during mbedTLS global initialization. | Official `RELEASE-NOTES`: `mbedtls: call psa_crypt_init() in global init`; changed function `mbedtls_init` in `lib/vtls/mbedtls.c`. | TLS backend initialization fix. |
| GT-U008 | Diagnostics | Improve OpenSSL error reporting for expired certificates. | Official `RELEASE-NOTES`: `OpenSSL: improve error message on expired certificate`; changed OpenSSL TLS path including `ossl_connect_step2` in `lib/vtls/openssl.c`. | User/developer diagnostic behavior. |
| GT-U009 | Compatibility | Remove Schannel TLS 1.3 ciphersuite-list support. | Official `RELEASE-NOTES`: `schannel: remove TLS 1.3 ciphersuite-list support`; changed `schannel_acquire_credential_handle` and related code in `lib/vtls/schannel.c`. | Platform TLS backend compatibility behavior. |
| GT-U010 | Fix | Correct `CURLOPT_HTTP_CONTENT_DECODING` handling and option availability in builds without HTTP or MQTT. | Official `RELEASE-NOTES`: `setopt: fix CURLOPT_HTTP_CONTENT_DECODING` and `setopt: fix missing options for builds without HTTP & MQTT`; changed functions `setopt_long` and `setopt_cptr` in `lib/setopt.c`. | Grouped as option-handling behavior. |
| GT-U011 | Fix | Detect end-of-stream in RTSP receive handling and return an error code instead of silently continuing. | Official `RELEASE-NOTES`: `rtsp: check EOS in the RTSP receive and return an error code`; changed function `rtsp_done` in `lib/rtsp.c`. | Protocol behavior fix. |
| GT-U012 | Feature | Use libssh asynchronous SFTP upload support and bracket numeric IPv6 addresses in libssh connections. | Official `RELEASE-NOTES`: `libssh: use libssh sftp_aio to upload file` and `libssh: when using IPv6 numerical address, add brackets`; changed functions `myssh_statemach_act`, `myssh_connect`, and `sftp_send` in `lib/vssh/libssh.c`. | Grouped as libssh SFTP/connection behavior. |
| GT-U013 | Fix | Generate shorter Digest authentication client nonce values. | Official `RELEASE-NOTES`: `digest: produce a shorter cnonce in Digest headers`; changed digest-auth functions in `lib/vauth/digest.c`. | Protocol header behavior. |
| GT-U014 | Fix | Correct socket binding behavior for `host!<ip>` local binding syntax. | Official `RELEASE-NOTES`: `socket: handle binding to "host!<ip>"`; changed function `bindlocal` in `lib/cf-socket.c`. | Network binding behavior. |
| GT-U015 | Fix | Prevent MIME reader stalls on small read lengths. | Official `RELEASE-NOTES`: `mime: fix reader stall on small read lengths`; changed functions `cr_mime_init`, `cr_mime_close`, and `cr_mime_read` in `lib/mime.c`. | MIME upload/read behavior. |
| GT-U016 | CLI | Reject incompatible command-line combinations involving `--continue-at` with `--no-clobber`, `--range`, or `--remove-on-error`. | Official `RELEASE-NOTES`: three `curl: --continue-at is mutually exclusive ...` entries; changed command-line parser functions such as `parse_continue_at`, `parse_range`, and `getparameter` in `src/tool_getparam.c`. | CLI behavior; can be kept if CLI release-note entries are in scope. |

## Optional Or Excluded Entries

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| GT-U017 draft: replace several `sscanf()`-based command-line parsers | Excluded from strict GT because the official notes describe implementation cleanup more than a stable user-facing behavior. It can support parser-related generated text only as secondary evidence. | Official `RELEASE-NOTES`: `tool_getparam: parse --localport without using sscanf`, `tool_formparse: remove use of sscanf()`, `tool_urlglob: parse character globbing range without sscanf`; changed `parse_localport`, `get_param_part`, and `glob_range`. |
| GT-U018 draft: move HTTP proxy custom-header assembly into the proxy code path | Excluded from strict GT because it is primarily an internal refactor; release-note-level behavior is too weak for high-quality semantic matching. | Official `RELEASE-NOTES`: `http_proxy: move dynhds_add_custom here from http.c`; changed/deleted `hd_name_eq`, `Curl_dynhds_add_custom`, added `dynhds_add_custom`, and changed `Curl_http_proxy_create_CONNECT`. |
| Build, CI, cmake, configure, packaging entries | Useful to maintainers but not central to release-note generation for user/developer-facing runtime behavior. | Many official `RELEASE-NOTES` build and CI entries. |
| Documentation-only entries | Do not represent source behavior changes under the current function-level extractor. | `docs: bring back ALTSVC.md and HSTS.md`, command documentation edits, known-bugs/doc updates. |
| Test-only entries | Support behavior validation but are not standalone release-note GT. | pytest/test server/test data updates. |
| Pure static-analysis cleanups | Low user-facing value unless tied to behavior. | OpenSSL useless assignments, formatting, redundant condition removals. |

## Reviewer Notes

- This reviewed extension set intentionally keeps `16` strict GT entries and excludes `2` weaker drafts.
- `GT-U016` is retained because rejecting incompatible `--continue-at` CLI combinations is explicit user-facing behavior.
- `GT-U017` and `GT-U018` are excluded to keep the strict GT quality close to manual review standards.
- Do not average this extension case into the existing core5 matrix until comparable real-backend outputs and `matches_strict` files are complete.

# Ground Truth: upstream curl curl-8_14_0 -> curl-8_14_1

Status: `reviewed_extension`

This file contains reviewed GT entries for the upstream curl 8.14.1 extension case. The entries are derived from the official curl 8.14.1 `RELEASE-NOTES`, local commit messages, and Stage 1 function-level diffs.

## Admission Notes

- Role: `extension_eval` candidate.
- Official release-note source: `git show curl-8_14_1:RELEASE-NOTES`.
- Stage 1 output: `outputs/benchmark/upstream_curl/curl-8_14_0__curl-8_14_1/changed_functions.json`.
- Scope: prioritize release-note entries with direct C source evidence under `lib/`, `src/`, or public headers.
- Exclusion policy: build-only, CI-only, documentation-only, spelling-only, and test-only entries are excluded from strict GT unless they support a runtime/API behavior entry.
- Review policy: keep only entries that have official release-note support, function-level source evidence, and user/developer-visible behavior, diagnostics, API, CLI, or protocol meaning.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-C001 | Reliability | Clean up threaded async resolver state correctly when resolving fails due to out-of-memory. | Official `RELEASE-NOTES`: `asyn-thrdd: fix cleanup when RR fails due to OOM`; changed function `Curl_async_is_resolved` in `lib/asyn-thrdd.c`. | Runtime robustness for DNS resolution failure handling. |
| GT-C002 | CLI | Apply `curl -N`/no-buffer handling in the correct option setup order. | Official `RELEASE-NOTES`: `curl: make -N handled correctly`; changed functions `gen_trace_setopts`, `gen_cb_setopts`, and `config2setopts` in `src/config2setopts.c`. | User-visible command-line behavior. |
| GT-C003 | CLI | Correct uploads when the command-line upload source is `.`. | Official `RELEASE-NOTES`: `curl: upload from '.' fix`; changed function `config2setopts` in `src/config2setopts.c` and related upload tests. | User-visible upload path handling. |
| GT-C004 | Fix | Tear down the FTP DATA connection through the proper secondary-socket cleanup path. | Official `RELEASE-NOTES`: `ftp: fix teardown of DATA connection in done`; changed functions `ftp_epsv_disable`, `ftp_done`, and added helper `Curl_conn_is_setup`. | FTP transfer cleanup and connection-state behavior. |
| GT-C005 | Fix | Fail early when request-body rewind fails while following HTTP redirects. | Official `RELEASE-NOTES`: `http: fail early when rewind of input failed when following redirects`; changed functions `Curl_http_follow` and `Curl_http_output_auth` in `lib/http.c`. | Prevents silently continuing after an invalid redirect rewind state. |
| GT-C006 | Reliability | Resize multi-handle transfer storage to the intended capacity when adding transfers. | Official `RELEASE-NOTES`: `multi: fix add_handle resizing`; changed function `multi_xfers_add` in `lib/multi.c`. | Runtime robustness for multi interface bookkeeping. |
| GT-C007 | TLS | Report TLS BIO EOF based on peer-closed state instead of lower filter connectivity. | Official `RELEASE-NOTES`: `tls BIOs: handle BIO_CTRL_EOF correctly`; changed functions `ossl_bio_cf_ctrl` in `lib/vtls/openssl.c` and `wssl_bio_cf_ctrl` in `lib/vtls/wolfssl.c`. | TLS backend behavior fix affecting EOF detection. |
| GT-C008 | CLI | Reject `--no-anyauth` because `--anyauth` is not a boolean option. | Official `RELEASE-NOTES`: `tool_getparam: make --no-anyauth not be accepted`; changed option parser path in `src/tool_getparam.c`. | User-visible command-line validation. |
| GT-C009 | TLS | Configure wolfSSL early data limits before sending TLS early data. | Official `RELEASE-NOTES`: `wolfssl: fix sending of early data`; changed function `wssl_setup_session` in `lib/vtls/wolfssl.c`. | TLS backend compatibility and behavior fix. |
| GT-C010 | WebSocket | Improve WebSocket send/receive robustness for blocked sends, continuation frames, control-frame sizes, and diagnostics. | Official `RELEASE-NOTES`: `ws: handle blocked sends better` and `ws: tests and fixes`; changed WebSocket functions such as `ws_frame_firstbyte2flags`, `ws_dec_read_head`, `ws_enc_write_head`, `ws_send_raw_blocking`, `ws_send_raw`, and `curl_ws_send` in `lib/ws.c`. | Grouped because both release-note entries target the same WebSocket protocol handling surface. |

## Optional Or Excluded Entries

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| `tool_getparam: refactored, simplified` | Excluded from strict GT because it is primarily an internal parser refactor; only behavior-changing parser entries are kept. | Official `RELEASE-NOTES`; broad changes in `src/tool_getparam.c`. |
| `tool_getparam: remove two nextarg NULL checks` | Excluded as defensive cleanup without a distinct release-note-level behavior claim. | Official `RELEASE-NOTES`; changed `GetFileAndPassword` and `parse_url`. |
| Autotools, cmake, dllmain, GHA, scorecard, packaging, and policy entries | Useful to maintainers but not central to the user/developer-facing runtime behavior currently evaluated. | Official `RELEASE-NOTES` build and infrastructure entries. |
| Documentation-only and spelling-only entries | Do not represent source behavior changes under the current function-level release-note evaluation target. | Command docs, examples, typo/spelling changes. |
| Test-only entries | Support behavior validation but are not standalone strict GT entries. | `test1498`, `test1510`, pytest, mtls tests, WebSocket tests. |
| `memanalyze.pl` changes | Excluded because the changed artifact is a maintenance script, not a C/C++ runtime/API behavior in the benchmark scope. | Official `RELEASE-NOTES`: `memanalyze.pl: fix getaddrinfo/freeaddrinfo checks`. |

## Reviewer Notes

- This reviewed extension set keeps `10` strict GT entries.
- The WebSocket item is intentionally grouped to avoid over-counting several closely related protocol-validation and blocked-send fixes from the same module.
- CLI entries are retained when they affect command-line behavior visible to curl users.
- Do not average this extension case into the existing core5 matrix until comparable real-backend outputs and `matches_strict` files are complete.

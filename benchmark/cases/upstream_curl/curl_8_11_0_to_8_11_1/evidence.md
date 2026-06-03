# Evidence Pack: upstream_curl curl-8_11_0 -> curl-8_11_1

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `curl_8_11_0_to_8_11_1`
- Repository: `upstream_curl`
- Category: `network`
- Reference version: `curl-8_11_0`
- Target version: `curl-8_11_1`
- Pipeline status: `verified_stage1`
- Ground-truth status: `draft_required`

## Evidence Sources To Inspect

- [ ] official curl 8.11.1 RELEASE-NOTES
- [ ] commit_messages
- [ ] function_level_diff
- [ ] changed_files
- [ ] curl issue references in RELEASE-NOTES

## Local Artifacts

- Changed functions: `outputs/benchmark/upstream_curl/curl-8_11_0__curl-8_11_1/changed_functions.json`

## Pipeline Summary

- Commit count: `117`
- Changed C/C++ files: `67`
- Changed functions: `103`
- Patch only: `False`
- CMG matched entries: `unknown`
- CMG unmatched entries: `unknown`
- Fallback-context entries: `unknown`
- Diff-derived call edges: `unknown`
- Prompt entries: `unknown`
- Mock generated entries: `unknown`

## Commit Messages

- RELEASE: synced
- THANKS: contributors from 8.11.1
- build: fix tests when documentation/manual is disabled
- GHA: update four depencencies
- docs: bring back ALTSVC.md and HSTS.md
- test2086: disable MSYS2's POSIX path conversion
- mprintf: fix the integer overflow checks
- RELEASE-NOTES: synced
- tool_getparam: remove Redundant Condition
- hostip: don't use the resolver for FQDN localhost
- http_negotiate: allow for a one byte larger channel binding buffer
- cmake: set `CURL_STATICLIB` for static lib when `SHARE_LIB_OBJECT=OFF`
- mime: fix reader stall on small read lengths
- dmaketgz: use --no-cache when building docker image
- tool_getparam: parse --localport without using sscanf
- tool_formparse: remove use of sscanf()
- tool_urlglob: parse character globbing range without sscanf
- digest: produce a shorter cnonce in Digest headers
- curl: do more command line parsing in sub functions
- openssl: remove three "Useless Assignments"
- liub: fixes for wolfSSL OPENSSL_COEXIST
- KNOWN_BUGS: setting a disabled option should return CURLE_NOT_BUILT_IN
- RELEASE-NOTES: synced
- http_proxy: move dynhds_add_custom here from http.c
- openssl: stop using SSL_CTX_ function prefix for our functions
- Dockerfile: Update debian:bookworm-slim Docker digest to b73bf02
- CI: update dependencies
- libssh: use libssh sftp_aio to upload file
- curl: --continue-at is mutually exclusive with --remove-on-error
- curl: --continue-at is mutually exclusive with --no-clobber
- curl: use realtime in trace timestamps
- OpenSSL: improvde error message on expired certificate
- pytest: add test for use of CURLMOPT_MAX_HOST_CONNECTIONS
- curl: --continue-at is mutually exclusive with --range
- docs: suggest --ssl-reqd instead of --ftp-ssl
- RELEASE-NOTES: synced
- setopt: fix missing options for builds without HTTP & MQTT
- GHA/windows: extend PATH instead copying libcurl.dll
- tests: add the ending time stamp in testcurl.pl
- DISTROS: update Alt Linux links
- GHA/windows: avoid libtool wrapper for test and server executables
- cmake: remove legacy unused IMMEDIATE keyword
- build: fix MSVC UWP builds
- build: fix ECH to always enable HTTPS RR
- tests: re-enable 2086, and 472, 1299, 1613 for Windows
- tool_getpass: replace `getch()` call with `_getch()` on Windows
- GHA/windows: enable ECH in vcpkg wolfSSL job
- GHA/windows: merge cmake/autotools steps
- tool_getpass: restore UWP `getpass_r()`, fixup CI builds, fix UWP `-Wnull-dereference`
- tool_getpass: make local `getpass_r()` a dummy for UWP
- multi: fix callback for `CURLMOPT_TIMERFUNCTION` not being called again when...
- rtsp: check EOS in the RTSP receive and return an error code
- GHA: source mbedTLS from official tarball
- GHA: speed up 3 openssl/quictls builds 3x
- GHA: disable building tests, apps, docs in dependencies
- cmake: include `wolfssl/options.h` first
- schannel: remove TLS 1.3 ciphersuite-list support
- cmake: do not echo most inherited `LDFLAGS` to config files
- curl_multi_socket_all.md: soften the deprecation warning
- docs: document default `User-Agent`
- show-headers.md: clarify the headers are saved with the data
- GHA/macos: enable ECH in wolfSSL jobs
- RELEASE-NOTES: synced
- multi: add clarifying comment for wakeup_write()
- netrc: fix pointer to bool conversion
- socket: handle binding to "host!<ip>"
- netrc: address several netrc parser flaws
- GHA/linux: enable ECH in wolfSSL jobs
- curl.h: mark two error codes as obsolete
- CI: update dependencies
- GHA/windows: enable GSS-API in an MSVC job
- krb5: fix socket/sockindex confusion, MSVC compiler warnings
- CURLOPT_PREREQFUNCTION.md: add result code on failure
- Rename struct var to fix AIX build
- tidy-up: indentation [ci skip]
- configure: replace `$#` shell syntax
- cmake: restore cmake args list in `buildinfo.txt`
- configure: add FIXMEs for disabled pkg-config references
- build: omit certain deps from `libcurl.pc` unless found via `pkg-config`
- cmake: sync GSS config code with other deps
- strtok: use namespaced `strtok_r` macro instead of redefining it
- socketpair: fix enabling `USE_EVENTFD`
- configure: do not echo most inherited `LDFLAGS` to config files
- GHA/linux: fix `pip3 install impacket` breakage
- os400: Fix IBMi builds
- os400: Fix IBMi EBCDIC conversion of arguments
- cmake: typo in comment [ci skip]
- GHA/macos: follow Homebrew and switch to `pkgconf`
- cmakelint: fix to check root `CMakeLists.txt`
- cmake: work around `ios.toolchain.cmake` breaking feature-detections
- tests: use the standard format of an IGNORED line
- GHA/non-native: streamline installed packages on FreeBSD
- mk-ca-bundle: remove CKA_NSS_SERVER_DISTRUST_AFTER conditions
- curl-rustls.m4: keep existing `CPPFLAGS`/`LDFLAGS` when detected
- build: use `_fseeki64()` on Windows, drop detections
- GHA: update four dependencies
- libssh: when using IPv6 numerical address, add brackets
- GHA/non-native: enable nghttp2 in OmniOS job
- ci: Update vmactions/omnios-vm digest to 16b5996
- RELEASE-NOTES: synced
- nghttp2: use custom memory functions
- ECH: enable support for the AWS-LC backend
- curl: --test-duphandle in debug builds runs "duphandled"
- macos: disable gcc `availability` workaround as needed
- RELEASE-PROCEDURE.md: adjust release dates
- cmake: drop cmake args list from `buildinfo.txt`
- GHA/macos: let gcc dictate the configured Apple SDK
- GHA: add `apt update` where missing
- TODO: consider OCSP stapling by default
- vtls: fix compile warning when ALPN is not available
- cmdline/ech.md: formatting cleanups
- netrc: support large file, longer lines, longer tokens
- setopt: fix CURLOPT_HTTP_CONTENT_DECODING
- RELEASE-NOTES: synced
- mbedtls: call psa_crypt_init() in global init
- duphandle: also init netrc
- cookie: treat cookie name case sensitively

## Changed C/C++ Files

- `docs/examples/websocket.c`
- `include/curl/curl.h`
- `include/curl/curlver.h`
- `lib/cf-h2-proxy.c`
- `lib/cf-socket.c`
- `lib/config-win32.h`
- `lib/cookie.c`
- `lib/curl_ntlm_core.c`
- `lib/curl_setup.h`
- `lib/curl_trc.c`
- `lib/easy.c`
- `lib/formdata.c`
- `lib/hostip.c`
- `lib/http.c`
- `lib/http.h`
- `lib/http2.c`
- `lib/http2.h`
- `lib/http_negotiate.c`
- `lib/http_proxy.c`
- `lib/http_proxy.h`
- `lib/krb5.c`
- `lib/ldap.c`
- `lib/md4.c`
- `lib/md5.c`
- `lib/mime.c`
- `lib/mprintf.c`
- `lib/multi.c`
- `lib/netrc.c`
- `lib/rtsp.c`
- `lib/setopt.c`
- `lib/smb.c`
- `lib/socketpair.h`
- `lib/strerror.c`
- `lib/strtok.h`
- `lib/url.c`
- `lib/vauth/digest.c`
- `lib/version.c`
- `lib/vssh/libssh.c`
- `lib/vssh/ssh.h`
- `lib/vtls/mbedtls.c`
- `lib/vtls/openssl.c`
- `lib/vtls/schannel.c`
- `lib/vtls/schannel_verify.c`
- `lib/vtls/sectransp.c`
- `lib/vtls/wolfssl.c`
- `packages/OS400/ccsidcurl.c`
- `packages/OS400/curlmain.c`
- `src/tool_cb_dbg.c`
- `src/tool_cfgable.h`
- `src/tool_doswin.c`
- `src/tool_formparse.c`
- `src/tool_getparam.c`
- `src/tool_getparam.h`
- `src/tool_getpass.c`
- `src/tool_operate.c`
- `src/tool_urlglob.c`
- `src/tool_util.c`
- `src/tool_util.h`
- `src/var.c`
- `src/var.h`
- `tests/http/clients/hx-download.c`
- `tests/libtest/lib2309.c`
- `tests/server/rtspd.c`
- `tests/server/sws.c`
- `tests/server/tftpd.c`
- `tests/server/util.c`
- `tests/unit/unit1304.c`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `proxy_h2_client_new` | `modified` | `lib/cf-h2-proxy.c` | `275-297` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 2 | `bindlocal` | `modified` | `lib/cf-socket.c` | `568-820` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 3 | `parse_netscape` | `modified` | `lib/cookie.c` | `797-931` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 4 | `replace_existing` | `modified` | `lib/cookie.c` | `981-1083` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 5 | `trc_opt` | `modified` | `lib/curl_trc.c` | `359-398` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 6 | `curl_easy_duphandle` | `modified` | `lib/easy.c` | `924-1067` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 7 | `fseeko_wrapper` | `modified` | `lib/formdata.c` | `794-805` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 8 | `Curl_resolv` | `modified` | `lib/hostip.c` | `685-1488` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `Curl_http_output_auth` | `modified` | `lib/http.c` | `702-3505` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 10 | `Curl_add_custom_headers` | `modified` | `lib/http.c` | `1232-1384` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 11 | `hd_name_eq` | `deleted` | `lib/http.c` | `1238-1245` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `Curl_dynhds_add_custom` | `deleted` | `lib/http.c` | `1247-1387` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `h2_client_new` | `modified` | `lib/http2.c` | `431-453` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 14 | `Curl_nghttp2_malloc` | `added` | `lib/http2.c` | `2965-2969` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 15 | `Curl_nghttp2_free` | `added` | `lib/http2.c` | `2971-2975` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 16 | `Curl_nghttp2_calloc` | `added` | `lib/http2.c` | `2977-2981` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 17 | `Curl_nghttp2_realloc` | `added` | `lib/http2.c` | `2983-2987` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 18 | `Curl_input_negotiate` | `modified` | `lib/http_negotiate.c` | `40-135` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 19 | `hd_name_eq` | `added` | `lib/http_proxy.c` | `55-59` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 20 | `dynhds_add_custom` | `added` | `lib/http_proxy.c` | `61-196` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 21 | `Curl_http_proxy_create_CONNECT` | `modified` | `lib/http_proxy.c` | `227-302` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `krb5_auth` | `modified` | `lib/krb5.c` | `192-372` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 23 | `krb5_end` | `modified` | `lib/krb5.c` | `374-383` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 24 | `do_sec_send` | `deleted` | `lib/krb5.c` | `617-669` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 25 | `do_sec_send` | `added` | `lib/krb5.c` | `618-670` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 26 | `sec_write` | `deleted` | `lib/krb5.c` | `671-688` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 27 | `sec_write` | `added` | `lib/krb5.c` | `672-689` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 28 | `sec_send` | `modified` | `lib/krb5.c` | `692-700` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 29 | `split_str` | `modified` | `lib/ldap.c` | `810-836` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 30 | `cr_mime_init` | `modified` | `lib/mime.c` | `1934-1943` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 31 | `cr_mime_close` | `added` | `lib/mime.c` | `1945-1951` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 32 | `cr_mime_read` | `modified` | `lib/mime.c` | `1954-2090` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 33 | `parsefmt` | `modified` | `lib/mprintf.c` | `215-648` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 34 | `curl_multi_wakeup` | `modified` | `lib/multi.c` | `1513-1579` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 35 | `multi_socket` | `modified` | `lib/multi.c` | `3524-3628` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 36 | `parsenetrc` | `deleted` | `lib/netrc.c` | `95-317` | `unmatched` | unmatched; level=unmatched; diff_hunks=20; fallback_calls=0 |
| 37 | `parsenetrc` | `added` | `lib/netrc.c` | `98-332` | `unmatched` | unmatched; level=unmatched; diff_hunks=21; fallback_calls=0 |
| 38 | `rtsp_done` | `modified` | `lib/rtsp.c` | `190-224` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 39 | `setopt_long` | `modified` | `lib/setopt.c` | `258-1418` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 40 | `setopt_cptr` | `modified` | `lib/setopt.c` | `1669-2697` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 41 | `smb_format_message` | `modified` | `lib/smb.c` | `528-548` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 42 | `curl_easy_strerror` | `modified` | `lib/strerror.c` | `55-361` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 43 | `str_has_ctrl` | `added` | `lib/url.c` | `2654-2663` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 44 | `override_login` | `modified` | `lib/url.c` | `2669-2787` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 45 | `auth_digest_get_qop_values` | `modified` | `lib/vauth/digest.c` | `220-250` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 46 | `Curl_auth_decode_digest_http_message` | `modified` | `lib/vauth/digest.c` | `503-658` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 47 | `auth_create_digest_http_message` | `modified` | `lib/vauth/digest.c` | `680-953` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 48 | `myssh_statemach_act` | `modified` | `lib/vssh/libssh.c` | `664-2042` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 49 | `myssh_connect` | `modified` | `lib/vssh/libssh.c` | `2170-2285` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 50 | `sftp_send` | `modified` | `lib/vssh/libssh.c` | `2568-2633` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 51 | `mbedtls_init` | `modified` | `lib/vtls/mbedtls.c` | `1557-1579` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 52 | `SSL_CTX_use_certificate_blob` | `deleted` | `lib/vtls/openssl.c` | `1155-1191` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 53 | `use_certificate_blob` | `added` | `lib/vtls/openssl.c` | `1155-1190` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 54 | `use_privatekey_blob` | `added` | `lib/vtls/openssl.c` | `1192-1217` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 55 | `SSL_CTX_use_PrivateKey_blob` | `deleted` | `lib/vtls/openssl.c` | `1193-1221` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 56 | `use_certificate_chain_blob` | `added` | `lib/vtls/openssl.c` | `1219-1284` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 57 | `SSL_CTX_use_certificate_chain_blob` | `deleted` | `lib/vtls/openssl.c` | `1223-1291` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 58 | `cert_stuff` | `modified` | `lib/vtls/openssl.c` | `1286-1673` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 59 | `Curl_ossl_ctx_init` | `modified` | `lib/vtls/openssl.c` | `3467-3997` | `unmatched` | unmatched; level=unmatched; diff_hunks=10; fallback_calls=0 |
| 60 | `ossl_trace_ech_retry_configs` | `modified` | `lib/vtls/openssl.c` | `4060-4118` | `unmatched` | unmatched; level=unmatched; diff_hunks=7; fallback_calls=0 |
| 61 | `ossl_connect_step2` | `modified` | `lib/vtls/openssl.c` | `4122-4274` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 62 | `algo` | `deleted` | `lib/vtls/schannel.c` | `454-457` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 63 | `schannel_acquire_credential_handle` | `modified` | `lib/vtls/schannel.c` | `454-875` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 64 | `Curl_verify_host` | `modified` | `lib/vtls/schannel_verify.c` | `516-669` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 65 | `GetDarwinVersionNumber` | `modified` | `lib/vtls/sectransp.c` | `335-362` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 66 | `curl_easy_setopt_ccsid` | `modified` | `packages/OS400/ccsidcurl.c` | `1066-1297` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 67 | `main` | `modified` | `packages/OS400/curlmain.c` | `53-121` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 68 | `hms_for_sec` | `modified` | `src/tool_cb_dbg.c` | `43-56` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 69 | `tool_debug_cb` | `modified` | `src/tool_cb_dbg.c` | `80-235` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 70 | `GetLoadedModulePaths` | `modified` | `src/tool_doswin.c` | `617-667` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 71 | `get_param_part` | `modified` | `src/tool_formparse.c` | `460-646` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 72 | `parse_url` | `added` | `src/tool_getparam.c` | `1022-1055` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 73 | `parse_localport` | `added` | `src/tool_getparam.c` | `1057-1089` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 74 | `parse_continue_at` | `added` | `src/tool_getparam.c` | `1091-1121` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 75 | `parse_ech` | `added` | `src/tool_getparam.c` | `1123-1174` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 76 | `parse_header` | `added` | `src/tool_getparam.c` | `1176-1222` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 77 | `parse_output` | `added` | `src/tool_getparam.c` | `1224-1258` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 78 | `parse_remote_name` | `added` | `src/tool_getparam.c` | `1260-1299` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 79 | `parse_quote` | `added` | `src/tool_getparam.c` | `1301-1323` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 80 | `parse_range` | `added` | `src/tool_getparam.c` | `1325-1374` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| ... | ... | ... | ... | ... | ... | truncated at 80 of 103 functions |

## Function-Level Diff Snippets

### 1. `proxy_h2_client_new` in `lib/cf-h2-proxy.c`

```diff
+  nghttp2_mem mem = {NULL, Curl_nghttp2_malloc, Curl_nghttp2_free,
+                     Curl_nghttp2_calloc, Curl_nghttp2_realloc};
-  rc = nghttp2_session_client_new2(&ctx->h2, cbs, cf, o);
+  rc = nghttp2_session_client_new3(&ctx->h2, cbs, cf, o, &mem);
```

### 2. `bindlocal` in `lib/cf-socket.c`

```diff
+  else if(iface && (strlen(iface) >= 255) )
+    return CURLE_BAD_FUNCTION_ARGUMENT;
-  if(iface && (strlen(iface) < 255) ) {
+  if(iface || host) {
-    /* interface */
-    /*
-      * This binds the local socket to a particular interface. This will
-      * force even requests to other local interfaces to go out the external
-      * interface. Only bind to the interface when specified as interface,
-      * not just as a hostname or ip address.
-      *
-      * The interface might be a VRF, eg: vrf-blue, which means it cannot be
... truncated 35 additional diff lines ...
```

### 3. `parse_netscape` in `lib/cookie.c`

```diff
-  firstptr = strtok_r((char *)lineptr, "\t", &tok_buf); /* tokenize on TAB */
+  /* tokenize on TAB */
+  firstptr = Curl_strtok_r((char *)lineptr, "\t", &tok_buf);
-  for(ptr = firstptr; ptr; ptr = strtok_r(NULL, "\t", &tok_buf), fields++) {
+  for(ptr = firstptr; ptr;
+      ptr = Curl_strtok_r(NULL, "\t", &tok_buf), fields++) {
```

### 4. `replace_existing` in `lib/cookie.c`

```diff
-    if(strcasecompare(clist->name, co->name)) {
+    if(!strcmp(clist->name, co->name)) {
-    if(!replace_n && strcasecompare(clist->name, co->name)) {
+    if(!replace_n && !strcmp(clist->name, co->name)) {
```

### 5. `trc_opt` in `lib/curl_trc.c`

```diff
-  token = strtok_r(tmp, ", ", &tok_buf);
+  token = Curl_strtok_r(tmp, ", ", &tok_buf);
-    token = strtok_r(NULL, ", ", &tok_buf);
+    token = Curl_strtok_r(NULL, ", ", &tok_buf);
```

### 6. `curl_easy_duphandle` in `lib/easy.c`

```diff
+  Curl_netrc_init(&outcurl->state.netrc);
```

### 7. `fseeko_wrapper` in `lib/formdata.c`

```diff
-#if defined(HAVE__FSEEKI64)
+#if defined(_WIN32) && defined(USE_WIN32_LARGE_FILES)
```

### 8. `Curl_resolv` in `lib/hostip.c`

```diff
-         tailmatch(hostname, ".localhost"))
+         strcasecompare(hostname, "localhost.") ||
+         tailmatch(hostname, ".localhost") ||
+         tailmatch(hostname, ".localhost."))
```

### 9. `Curl_http_output_auth` in `lib/http.c`

```diff
-enum proxy_use {
-  HEADER_SERVER,  /* direct to server */
-  HEADER_PROXY,   /* regular request to proxy */
-  HEADER_CONNECT  /* sending CONNECT to a proxy */
-};
-
-static bool hd_name_eq(const char *n1, size_t n1len,
-                       const char *n2, size_t n2len)
-{
-  if(n1len == n2len) {
-    return strncasecompare(n1, n2, n1len);
-  }
... truncated 147 additional diff lines ...
```

### 10. `Curl_add_custom_headers` in `lib/http.c`

```diff
+  enum Curl_proxy_use proxy;
```

### 11. `hd_name_eq` in `lib/http.c`

```diff
-static bool hd_name_eq(const char *n1, size_t n1len,
-                       const char *n2, size_t n2len)
-{
-  if(n1len == n2len) {
-    return strncasecompare(n1, n2, n1len);
-  }
-  return FALSE;
-}
```

### 12. `Curl_dynhds_add_custom` in `lib/http.c`

```diff
-CURLcode Curl_dynhds_add_custom(struct Curl_easy *data,
-                                bool is_connect,
-                                struct dynhds *hds)
-{
-  struct connectdata *conn = data->conn;
-  char *ptr;
-  struct curl_slist *h[2];
-  struct curl_slist *headers;
-  int numlists = 1; /* by default */
-  int i;
-
-#ifndef CURL_DISABLE_PROXY
... truncated 129 additional diff lines ...
```

### 13. `h2_client_new` in `lib/http2.c`

```diff
+  nghttp2_mem mem = {NULL, Curl_nghttp2_malloc, Curl_nghttp2_free,
+                     Curl_nghttp2_calloc, Curl_nghttp2_realloc};
-  rc = nghttp2_session_client_new2(&ctx->h2, cbs, cf, o);
+  rc = nghttp2_session_client_new3(&ctx->h2, cbs, cf, o, &mem);
```

### 14. `Curl_nghttp2_malloc` in `lib/http2.c`

```diff
+void *Curl_nghttp2_malloc(size_t size, void *user_data)
+{
+  (void)user_data;
+  return Curl_cmalloc(size);
+}
```

### 15. `Curl_nghttp2_free` in `lib/http2.c`

```diff
+void Curl_nghttp2_free(void *ptr, void *user_data)
+{
+  (void)user_data;
+  Curl_cfree(ptr);
+}
```

### 16. `Curl_nghttp2_calloc` in `lib/http2.c`

```diff
+void *Curl_nghttp2_calloc(size_t nmemb, size_t size, void *user_data)
+{
+  (void)user_data;
+  return Curl_ccalloc(nmemb, size);
+}
```

### 17. `Curl_nghttp2_realloc` in `lib/http2.c`

```diff
+void *Curl_nghttp2_realloc(void *ptr, size_t size, void *user_data)
+{
+  (void)user_data;
+  return Curl_crealloc(ptr, size);
+}
```

### 18. `Curl_input_negotiate` in `lib/http_negotiate.c`

```diff
-    Curl_dyn_init(&neg_ctx->channel_binding_data, SSL_CB_MAX_SIZE);
+    Curl_dyn_init(&neg_ctx->channel_binding_data, SSL_CB_MAX_SIZE + 1);
```

### 19. `hd_name_eq` in `lib/http_proxy.c`

```diff
+static bool hd_name_eq(const char *n1, size_t n1len,
+                       const char *n2, size_t n2len)
+{
+  return (n1len == n2len) ? strncasecompare(n1, n2, n1len) : FALSE;
+}
```

### 20. `dynhds_add_custom` in `lib/http_proxy.c`

```diff
+static CURLcode dynhds_add_custom(struct Curl_easy *data,
+                                  bool is_connect,
+                                  struct dynhds *hds)
+{
+  struct connectdata *conn = data->conn;
+  char *ptr;
+  struct curl_slist *h[2];
+  struct curl_slist *headers;
+  int numlists = 1; /* by default */
+  int i;
+
+  enum Curl_proxy_use proxy;
... truncated 124 additional diff lines ...
```

### 21. `Curl_http_proxy_create_CONNECT` in `lib/http_proxy.c`

```diff
+  result = dynhds_add_custom(data, TRUE, &req->headers);
```

### 22. `krb5_auth` in `lib/krb5.c`

```diff
-  gss_buffer_desc input_buffer, output_buffer, _gssresp, *gssresp;
+  gss_buffer_desc input_buffer, output_buffer, *gssresp;
+  gss_buffer_desc _gssresp = GSS_C_EMPTY_BUFFER;
-      return ret;
+      break;
```

### 23. `krb5_end` in `lib/krb5.c`

```diff
-    OM_uint32 min;
-    gss_ctx_id_t *context = app_data;
-    if(*context != GSS_C_NO_CONTEXT) {
-      OM_uint32 maj = gss_delete_sec_context(&min, context, GSS_C_NO_BUFFER);
-      (void)maj;
-      DEBUGASSERT(maj == GSS_S_COMPLETE);
-    }
+  OM_uint32 min;
+  gss_ctx_id_t *context = app_data;
+  if(*context != GSS_C_NO_CONTEXT) {
+    OM_uint32 maj = gss_delete_sec_context(&min, context, GSS_C_NO_BUFFER);
+    (void)maj;
... truncated 2 additional diff lines ...
```

### 24. `do_sec_send` in `lib/krb5.c`

```diff
-                        curl_socket_t fd, const char *from, int length)
-        socket_write(data, fd, enc, 4);
-        socket_write(data, fd, mic, 4);
-      socket_write(data, fd, cmd_buffer, cmd_size);
-      socket_write(data, fd, "\r\n", 2);
-    socket_write(data, fd, &htonl_bytes, sizeof(htonl_bytes));
-    socket_write(data, fd, buffer, curlx_sitouz(bytes));
```

### 25. `do_sec_send` in `lib/krb5.c`

```diff
+                        int sockindex, const char *from, int length)
+        socket_write(data, sockindex, enc, 4);
+        socket_write(data, sockindex, mic, 4);
+      socket_write(data, sockindex, cmd_buffer, cmd_size);
+      socket_write(data, sockindex, "\r\n", 2);
+    socket_write(data, sockindex, &htonl_bytes, sizeof(htonl_bytes));
+    socket_write(data, sockindex, buffer, curlx_sitouz(bytes));
```

### 26. `sec_write` in `lib/krb5.c`

```diff
-                         curl_socket_t fd, const char *buffer, size_t length)
-    do_sec_send(data, conn, fd, buffer, curlx_sztosi(len));
```

### 27. `sec_write` in `lib/krb5.c`

```diff
+                         int sockindex, const char *buffer, size_t length)
+    do_sec_send(data, conn, sockindex, buffer, curlx_sztosi(len));
```

### 28. `sec_send` in `lib/krb5.c`

```diff
-  curl_socket_t fd = conn->sock[sockindex];
-  return sec_write(data, conn, fd, buffer, len);
+  return sec_write(data, conn, sockindex, buffer, len);
```

### 29. `split_str` in `lib/ldap.c`

```diff
-  for(i = 0, s = strtok_r(str, ",", &lasts); s && i < items;
-      s = strtok_r(NULL, ",", &lasts), i++)
+  for(i = 0, s = Curl_strtok_r(str, ",", &lasts); s && i < items;
+      s = Curl_strtok_r(NULL, ",", &lasts), i++)
```

### 30. `cr_mime_init` in `lib/mime.c`

```diff
+  Curl_bufq_init2(&ctx->tmpbuf, 1024, 1, BUFQ_OPT_NO_SPARES);
```

### 31. `cr_mime_close` in `lib/mime.c`

```diff
+static void cr_mime_close(struct Curl_easy *data,
+                          struct Curl_creader *reader)
+{
+  struct cr_mime_ctx *ctx = reader->ctx;
+  (void)data;
+  Curl_bufq_free(&ctx->tmpbuf);
+}
```

### 32. `cr_mime_read` in `lib/mime.c`

```diff
+  char tmp[256];
-  if(blen <= 4) {
-    /* TODO: Curl_mime_read() may go into an infinite loop when reading
-     * such small lengths. Returning 0 bytes read is a fix that only works
-     * as request upload buffers will get flushed eventually and larger
-     * reads will happen again. */
-    CURL_TRC_READ(data, "cr_mime_read(len=%zu), too small, return", blen);
-    *pnread = 0;
-    *peos = FALSE;
-    goto out;
+  if(!Curl_bufq_is_empty(&ctx->tmpbuf)) {
+    CURLcode result = CURLE_OK;
... truncated 38 additional diff lines ...
```

### 33. `parsefmt` in `lib/mprintf.c`

```diff
-              if(precision > INT_MAX/10)
+              int n = *fmt - '0';
+              if(precision > (INT_MAX - n) / 10)
-              precision *= 10;
-              precision += *fmt - '0';
+              precision = precision * 10 + n;
-            if(width > INT_MAX/10)
+            int n = *fmt - '0';
+            if(width > (INT_MAX - n) / 10)
-            width *= 10;
-            width += *fmt - '0';
+            width = width * 10 + n;
```

### 34. `curl_multi_wakeup` in `lib/multi.c`

```diff
+    /* eventfd has a stringent rule of requiring the 8-byte buffer when
+       calling write(2) on it, which makes the sizeof(buf) below fine since
+       this is only used on 64-bit systems and then the pointer is 64-bit */
```

### 35. `multi_socket` in `lib/multi.c`

```diff
+  else {
+    /* Asked to run due to time-out. Clear the 'last_expire_ts' variable to
+       force Curl_update_timer() to trigger a callback to the app again even
+       if the same timeout is still the one to run after this call. That
+       handles the case when the application asks libcurl to run the timeout
+       prematurely. */
+    memset(&multi->last_expire_ts, 0, sizeof(multi->last_expire_ts));
+  }
```

### 36. `parsenetrc` in `lib/netrc.c`

```diff
-                      char **loginp,
-  char *password = *passwordp;
-  bool specific_login = (login && *login != 0);
-  bool login_alloc = FALSE;
-  bool password_alloc = FALSE;
-  enum found_state found = NONE;
-  bool our_login = TRUE;  /* With specific_login, found *our* login name (or
-                             login-less line) */
-    while(tok) {
-      if((login && *login) && (password && *password)) {
-        done = TRUE;
-        break;
... truncated 37 additional diff lines ...
```

### 37. `parsenetrc` in `lib/netrc.c`

```diff
+                      char **loginp, /* might point to a username */
+  char *password = NULL;
+  bool specific_login = !!login; /* points to something */
+  enum found_state keyword = NONE;
+  unsigned char found = 0; /* login + password found bits, as they can come in
+                              any order */
+  bool our_login = FALSE;  /* found our login name */
+  DEBUGASSERT(!*passwordp);
+    while(tok && !done) {
+        else if(strcasecompare("machine", tok)) {
+          keyword = NONE;
+          found = 0;
... truncated 49 additional diff lines ...
```

### 38. `rtsp_done` in `lib/rtsp.c`

```diff
+    if(data->set.rtspreq == RTSPREQ_RECEIVE &&
+       data->req.eos_written) {
+      failf(data, "Server prematurely closed the RTSP connection.");
+      return CURLE_RECV_ERROR;
+    }
```

### 39. `setopt_long` in `lib/setopt.c`

```diff
-    data->set.http_ce_skip = enabled;
+    data->set.http_ce_skip = !enabled; /* reversed */
```

### 40. `setopt_cptr` in `lib/setopt.c`

```diff
+#endif /* ! CURL_DISABLE_HTTP || ! CURL_DISABLE_MQTT */
-#endif
+#endif /* ! CURL_DISABLE_PROXY */
-#endif /* ! CURL_DISABLE_PROXY */
```

### 41. `smb_format_message` in `lib/smb.c`

```diff
+  pid = (unsigned int)Curl_getpid();
```

### 42. `curl_easy_strerror` in `lib/strerror.c`

```diff
-  case CURLE_HTTP_POST_ERROR:
-    return "Internal problem setting up the POST";
-
-  case CURLE_FUNCTION_NOT_FOUND:
-    return "A required function in the library was not found";
-
+  case CURLE_OBSOLETE34:
+  case CURLE_OBSOLETE41:
```

### 43. `str_has_ctrl` in `lib/url.c`

```diff
+static bool str_has_ctrl(const char *input)
+{
+  const unsigned char *str = (const unsigned char *)input;
+  while(*str) {
+    if(*str < 0x20)
+      return TRUE;
+    str++;
+  }
+  return FALSE;
+}
```

### 44. `override_login` in `lib/url.c`

```diff
-      /* there was a username in the URL. Use the URL decoded version */
+      /* there was a username with a length in the URL. Use the URL decoded
+         version */
-    ret = Curl_parsenetrc(&data->state.netrc, conn->host.name,
-                          userp, passwdp,
-                          data->set.str[STRING_NETRC_FILE]);
-    if(ret > 0) {
-      infof(data, "Couldn't find host %s in the %s file; using defaults",
-            conn->host.name,
-            (data->set.str[STRING_NETRC_FILE] ?
-             data->set.str[STRING_NETRC_FILE] : ".netrc"));
-    }
... truncated 37 additional diff lines ...
```

### 45. `auth_digest_get_qop_values` in `lib/vauth/digest.c`

```diff
-     strtok_r() ruins it. */
+     Curl_strtok_r() ruins it. */
-  token = strtok_r(tmp, ",", &tok_buf);
+  token = Curl_strtok_r(tmp, ",", &tok_buf);
-    token = strtok_r(NULL, ",", &tok_buf);
+    token = Curl_strtok_r(NULL, ",", &tok_buf);
```

### 46. `Curl_auth_decode_digest_http_message` in `lib/vauth/digest.c`

```diff
-           clone of the buffer since strtok_r() ruins it */
+           clone of the buffer since Curl_strtok_r() ruins it */
-        token = strtok_r(tmp, ",", &tok_buf);
+        token = Curl_strtok_r(tmp, ",", &tok_buf);
-          token = strtok_r(NULL, ",", &tok_buf);
+          token = Curl_strtok_r(NULL, ",", &tok_buf);
```

### 47. `auth_create_digest_http_message` in `lib/vauth/digest.c`

```diff
-    char cnoncebuf[33];
-    result = Curl_rand_hex(data, (unsigned char *)cnoncebuf,
-                           sizeof(cnoncebuf));
+    char cnoncebuf[12];
+    result = Curl_rand_bytes(data,
+#ifdef DEBUGBUILD
+                             TRUE,
+#endif
+                             (unsigned char *)cnoncebuf,
+                             sizeof(cnoncebuf));
-    result = Curl_base64_encode(cnoncebuf, strlen(cnoncebuf),
+    result = Curl_base64_encode(cnoncebuf, sizeof(cnoncebuf),
```

### 48. `myssh_statemach_act` in `lib/vssh/libssh.c`

```diff
-
+#if LIBSSH_VERSION_INT > SSH_VERSION_INT(0, 11, 0)
+      sshc->sftp_send_state = 0;
+#endif
+      ssh_set_blocking(sshc->ssh_session, 0);
+#if LIBSSH_VERSION_INT > SSH_VERSION_INT(0, 11, 0)
+      if(sshc->sftp_aio) {
+        sftp_aio_free(sshc->sftp_aio);
+        sshc->sftp_aio = NULL;
+      }
+#endif
```

### 49. `myssh_connect` in `lib/vssh/libssh.c`

```diff
-  rc = ssh_options_set(ssh->ssh_session, SSH_OPTIONS_HOST, conn->host.name);
+  if(conn->bits.ipv6_ip) {
+    char ipv6[MAX_IPADR_LEN];
+    msnprintf(ipv6, sizeof(ipv6), "[%s]", conn->host.name);
+    rc = ssh_options_set(ssh->ssh_session, SSH_OPTIONS_HOST, ipv6);
+  }
+  else
+    rc = ssh_options_set(ssh->ssh_session, SSH_OPTIONS_HOST, conn->host.name);
+
```

### 50. `sftp_send` in `lib/vssh/libssh.c`

```diff
+#if LIBSSH_VERSION_INT > SSH_VERSION_INT(0, 11, 0)
+  switch(conn->proto.sshc.sftp_send_state) {
+    case 0:
+      sftp_file_set_nonblocking(conn->proto.sshc.sftp_file);
+      if(sftp_aio_begin_write(conn->proto.sshc.sftp_file, mem, len,
+                              &conn->proto.sshc.sftp_aio) == SSH_ERROR) {
+        *err = CURLE_SEND_ERROR;
+        return -1;
+      }
+      conn->proto.sshc.sftp_send_state = 1;
+      FALLTHROUGH();
+    case 1:
... truncated 22 additional diff lines ...
```

### 51. `mbedtls_init` in `lib/vtls/mbedtls.c`

```diff
+#ifdef TLS13_SUPPORT
+  {
+    int ret;
+#ifdef THREADING_SUPPORT
+    Curl_mbedtlsthreadlock_lock_function(0);
+#endif
+    ret = psa_crypto_init();
+#ifdef THREADING_SUPPORT
+    Curl_mbedtlsthreadlock_unlock_function(0);
+#endif
+    if(ret != PSA_SUCCESS)
+      return 0;
... truncated 2 additional diff lines ...
```

### 52. `SSL_CTX_use_certificate_blob` in `lib/vtls/openssl.c`

```diff
-static int
-SSL_CTX_use_certificate_blob(SSL_CTX *ctx, const struct curl_blob *blob,
-                             int type, const char *key_passwd)
```

### 53. `use_certificate_blob` in `lib/vtls/openssl.c`

```diff
+static int use_certificate_blob(SSL_CTX *ctx, const struct curl_blob *blob,
+                                int type, const char *key_passwd)
```

### 54. `use_privatekey_blob` in `lib/vtls/openssl.c`

```diff
+static int use_privatekey_blob(SSL_CTX *ctx, const struct curl_blob *blob,
+                               int type, const char *key_passwd)
+  else
+
+  if(!pkey)
+
```

### 55. `SSL_CTX_use_PrivateKey_blob` in `lib/vtls/openssl.c`

```diff
-static int
-SSL_CTX_use_PrivateKey_blob(SSL_CTX *ctx, const struct curl_blob *blob,
-                            int type, const char *key_passwd)
-  else {
-    ret = 0;
-  }
-  if(!pkey) {
-    ret = 0;
-  }
```

### 56. `use_certificate_chain_blob` in `lib/vtls/openssl.c`

```diff
+use_certificate_chain_blob(SSL_CTX *ctx, const struct curl_blob *blob,
+                           const char *key_passwd)
+  if(!x)
```

### 57. `SSL_CTX_use_certificate_chain_blob` in `lib/vtls/openssl.c`

```diff
-SSL_CTX_use_certificate_chain_blob(SSL_CTX *ctx, const struct curl_blob *blob,
-                                   const char *key_passwd)
-
-  if(!x) {
-    ret = 0;
-  }
```

### 58. `cert_stuff` in `lib/vtls/openssl.c`

```diff
-        SSL_CTX_use_certificate_chain_blob(ctx, cert_blob, key_passwd) :
+        use_certificate_chain_blob(ctx, cert_blob, key_passwd) :
-        SSL_CTX_use_certificate_blob(ctx, cert_blob,
-                                     file_type, key_passwd) :
+        use_certificate_blob(ctx, cert_blob, file_type, key_passwd) :
-        SSL_CTX_use_PrivateKey_blob(ctx, key_blob, file_type, key_passwd) :
+        use_privatekey_blob(ctx, key_blob, file_type, key_passwd) :
```

### 59. `Curl_ossl_ctx_init` in `lib/vtls/openssl.c`

```diff
-#ifdef HAS_ALPN
+#ifdef HAS_ALPN
-  }
+  }
-# ifdef OPENSSL_IS_BORINGSSL
+# if defined(OPENSSL_IS_BORINGSSL) || defined(OPENSSL_IS_AWSLC)
-# ifdef OPENSSL_IS_BORINGSSL
-      /* have to do base64 decode here for boring */
+# if defined(OPENSSL_IS_BORINGSSL) || defined(OPENSSL_IS_AWSLC)
+      /* have to do base64 decode here for BoringSSL */
-# ifndef OPENSSL_IS_BORINGSSL
+# if !defined(OPENSSL_IS_BORINGSSL) && !defined(OPENSSL_IS_AWSLC)
... truncated 6 additional diff lines ...
```

### 60. `ossl_trace_ech_retry_configs` in `lib/vtls/openssl.c`

```diff
-# ifndef OPENSSL_IS_BORINGSSL
+# if !defined(OPENSSL_IS_BORINGSSL) && !defined(OPENSSL_IS_AWSLC)
-# ifndef OPENSSL_IS_BORINGSSL
+# if !defined(OPENSSL_IS_BORINGSSL) && !defined(OPENSSL_IS_AWSLC)
-# ifndef OPENSSL_IS_BORINGSSL
+# if !defined(OPENSSL_IS_BORINGSSL) && !defined(OPENSSL_IS_AWSLC)
-#else
+# else
-    /* TODO: get the inner from boring */
+    /* TODO: get the inner from BoringSSL */
-#endif
+# endif
... truncated 1 additional diff lines ...
```

### 61. `ossl_connect_step2` in `lib/vtls/openssl.c`

```diff
-          msnprintf(error_buffer, sizeof(error_buffer),
-                    "SSL certificate problem: %s",
-                    X509_verify_cert_error_string(lerr));
+          failf(data, "SSL certificate problem: %s",
+                X509_verify_cert_error_string(lerr));
-        else {
+        else
-          return result;
-        }
-# ifndef OPENSSL_IS_BORINGSSL
+# if !defined(OPENSSL_IS_BORINGSSL) && !defined(OPENSSL_IS_AWSLC)
```

### 62. `algo` in `lib/vtls/schannel.c`

```diff
-static bool algo(const char *check, char *namep, size_t nlen)
-{
-  return (strlen(check) == nlen) && !strncmp(check, namep, nlen);
-}
```

### 63. `schannel_acquire_credential_handle` in `lib/vtls/schannel.c`

```diff
-    char *ciphers13 = 0;
-
-    bool disable_aes_gcm_sha384 = FALSE;
-    bool disable_aes_gcm_sha256 = FALSE;
-    bool disable_chacha_poly = FALSE;
-    bool disable_aes_ccm_8_sha256 = FALSE;
-    bool disable_aes_ccm_sha256 = FALSE;
-
-    CRYPTO_SETTINGS crypto_settings[4] = { { 0 } };
-    UNICODE_STRING blocked_ccm_modes[1] = { { 0 } };
-    UNICODE_STRING blocked_gcm_modes[1] = { { 0 } };
-
... truncated 84 additional diff lines ...
```

### 64. `Curl_verify_host` in `lib/vtls/schannel_verify.c`

```diff
-  if(p->size) {
+  if(p->size && alt_name_info) {
-
```

### 65. `GetDarwinVersionNumber` in `lib/vtls/sectransp.c`

```diff
-  os_version_major = strtok_r(os_version, ".", &tok_buf);
-  os_version_minor = strtok_r(NULL, ".", &tok_buf);
+  os_version_major = Curl_strtok_r(os_version, ".", &tok_buf);
+  os_version_minor = Curl_strtok_r(NULL, ".", &tok_buf);
```

### 66. `curl_easy_setopt_ccsid` in `packages/OS400/ccsidcurl.c`

```diff
+  struct Curl_easy *data = easy;
-    pfsize = easy->set.postfieldsize;
+    pfsize = data->set.postfieldsize;
-      easy->set.postfieldsize = pfsize;         /* Replace data size. */
+      data->set.postfieldsize = pfsize;         /* Replace data size. */
-    easy->set.str[STRING_COPYPOSTFIELDS] = s;   /* Give to library. */
+    data->set.str[STRING_COPYPOSTFIELDS] = s;   /* Give to library. */
```

### 67. `main` in `packages/OS400/curlmain.c`

```diff
-  const char *tocode = "IBMCCSID01208"; /* Use UTF-8. */
-  const char *fromcode = "IBMCCSID000000000010";
+  /* To/From codes are 32 byte long strings with
+     reserved fields initialized to ZEROs */
+  const char tocode[32]   = {"IBMCCSID01208"}; /* Use UTF-8. */
+  const char fromcode[32] = {"IBMCCSID000000000010"};
```

### 68. `hms_for_sec` in `src/tool_cb_dbg.c`

```diff
-  static time_t epoch_offset;
-  static int known_epoch;
-    struct tm *now;
-    time_t secs;
-    /* recalculate */
-    if(!known_epoch) {
-      epoch_offset = time(NULL) - tv_sec;
-      known_epoch = 1;
+    struct tm *now = localtime(&tv_sec);  /* not thread safe either */
```

### 69. `tool_debug_cb` in `src/tool_cb_dbg.c`

```diff
-    tv = tvnow();
+    tv = tvrealnow();
```

### 70. `GetLoadedModulePaths` in `src/tool_doswin.c`

```diff
+  struct curl_slist *slist = NULL;
+#if !defined(CURL_WINDOWS_UWP)
-  struct curl_slist *slist = NULL;
+#endif
```

### 71. `get_param_part` in `src/tool_formparse.c`

```diff
-  char type_major[128] = "";
-  char type_minor[128] = "";
-      /* verify that this is a fine type specifier */
-      if(2 != sscanf(type, "%127[^/ ]/%127[^;, \n]", type_major, type_minor)) {
-        warnf(config->global, "Illegally formatted content-type field");
-        curl_slist_free_all(headers);
-        return -1; /* illegal content-type syntax! */
-      }
-
-      /* now point beyond the content-type specifier */
-      p = type + strlen(type_major) + strlen(type_minor) + 1;
-      for(endct = p; *p && *p != ';' && *p != endchar; p++)
... truncated 6 additional diff lines ...
```

### 72. `parse_url` in `src/tool_getparam.c`

```diff
+static ParameterError parse_url(struct OperationConfig *config,
+                                const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+  struct getout *url;
+
+  if(!config->url_get)
+    config->url_get = config->url_list;
+
+  if(config->url_get) {
+    /* there is a node here, if it already is filled-in continue to find
+       an "empty" node */
... truncated 22 additional diff lines ...
```

### 73. `parse_localport` in `src/tool_getparam.c`

```diff
+static ParameterError parse_localport(struct OperationConfig *config,
+                                      char *nextarg)
+{
+  char *pp = NULL;
+  char *p = nextarg;
+  while(ISDIGIT(*p))
+    p++;
+  if(*p) {
+    pp = p;
+    /* check for ' - [end]' */
+    if(ISSPACE(*pp))
+      pp++;
... truncated 21 additional diff lines ...
```

### 74. `parse_continue_at` in `src/tool_getparam.c`

```diff
+static ParameterError parse_continue_at(struct GlobalConfig *global,
+                                        struct OperationConfig *config,
+                                        const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+  if(config->range) {
+    errorf(global, "--continue-at is mutually exclusive with --range");
+    return PARAM_BAD_USE;
+  }
+  if(config->rm_partial) {
+    errorf(config->global,
+           "--continue-at is mutually exclusive with --remove-on-error");
... truncated 19 additional diff lines ...
```

### 75. `parse_ech` in `src/tool_getparam.c`

```diff
+static ParameterError parse_ech(struct GlobalConfig *global,
+                                struct OperationConfig *config,
+                                const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+  if(!feature_ech)
+    err = PARAM_LIBCURL_DOESNT_SUPPORT;
+  else if(strlen(nextarg) > 4 && strncasecompare("pn:", nextarg, 3)) {
+    /* a public_name */
+    err = getstr(&config->ech_public, nextarg, DENY_BLANK);
+  }
+  else if(strlen(nextarg) > 5 && strncasecompare("ecl:", nextarg, 4)) {
... truncated 40 additional diff lines ...
```

### 76. `parse_header` in `src/tool_getparam.c`

```diff
+static ParameterError parse_header(struct GlobalConfig *global,
+                                   struct OperationConfig *config,
+                                   cmdline_t cmd,
+                                   const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+
+  /* A custom header to append to a list */
+  if(nextarg[0] == '@') {
+    /* read many headers from a file or stdin */
+    char *string;
+    size_t len;
... truncated 35 additional diff lines ...
```

### 77. `parse_output` in `src/tool_getparam.c`

```diff
+static ParameterError parse_output(struct OperationConfig *config,
+                                   const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+  struct getout *url;
+
+  /* output file */
+  if(!config->url_out)
+    config->url_out = config->url_list;
+  if(config->url_out) {
+    /* there is a node here, if it already is filled-in continue to find
+       an "empty" node */
... truncated 23 additional diff lines ...
```

### 78. `parse_remote_name` in `src/tool_getparam.c`

```diff
+static ParameterError parse_remote_name(struct OperationConfig *config,
+                                        bool toggle)
+{
+  ParameterError err = PARAM_OK;
+  struct getout *url;
+
+  if(!toggle && !config->default_node_flags)
+    return err; /* nothing to do */
+
+  /* output file */
+  if(!config->url_out)
+    config->url_out = config->url_list;
... truncated 28 additional diff lines ...
```

### 79. `parse_quote` in `src/tool_getparam.c`

```diff
+static ParameterError parse_quote(struct OperationConfig *config,
+                                  const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+
+  /* QUOTE command to send to FTP server */
+  switch(nextarg[0]) {
+  case '-':
+    /* prefixed with a dash makes it a POST TRANSFER one */
+    nextarg++;
+    err = add2list(&config->postquote, nextarg);
+    break;
... truncated 11 additional diff lines ...
```

### 80. `parse_range` in `src/tool_getparam.c`

```diff
+static ParameterError parse_range(struct GlobalConfig *global,
+                                  struct OperationConfig *config,
+                                  const char *nextarg)
+{
+  ParameterError err = PARAM_OK;
+
+  if(config->use_resume) {
+    errorf(global, "--continue-at is mutually exclusive with --range");
+    return PARAM_BAD_USE;
+  }
+  /* Specifying a range WITHOUT A DASH will create an illegal HTTP range
+     (and will not actually be range by definition). The manpage
... truncated 38 additional diff lines ...
```

## Mock Release-Note Drafts

- No mock release-note output available.

## Ground-Truth Drafting Workspace

| GT ID | Section | Semantic Release-Note Entry | Supporting Evidence | Decision |
| --- | --- | --- | --- | --- |
| GT-001 |  |  |  | pending |

## Excluded Or Low-Level Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
|  |  |  |

## Reviewer Notes

- Record uncertainty, alternative interpretations, and final consensus here.

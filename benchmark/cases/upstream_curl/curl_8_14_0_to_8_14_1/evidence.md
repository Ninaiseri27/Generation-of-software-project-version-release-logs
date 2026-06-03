# Evidence Pack: upstream_curl curl-8_14_0 -> curl-8_14_1

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `curl_8_14_0_to_8_14_1`
- Repository: `upstream_curl`
- Category: `network`
- Reference version: `curl-8_14_0`
- Target version: `curl-8_14_1`
- Pipeline status: `verified_stage1`
- Ground-truth status: `reviewed`

## Evidence Sources To Inspect

- [ ] official curl 8.14.1 RELEASE-NOTES
- [ ] commit_messages
- [ ] function_level_diff
- [ ] changed_files
- [ ] curl issue references in RELEASE-NOTES

## Local Artifacts

- Changed functions: `outputs/benchmark/upstream_curl/curl-8_14_0__curl-8_14_1/changed_functions.json`

## Pipeline Summary

- Commit count: `48`
- Changed C/C++ files: `109`
- Changed functions: `121`
- Patch only: `False`
- CMG matched entries: `unknown`
- CMG unmatched entries: `unknown`
- Fallback-context entries: `unknown`
- Diff-derived call edges: `unknown`
- Prompt entries: `unknown`
- Mock generated entries: `unknown`

## Commit Messages

- RELEASE-NOTES: synced
- THANKS: add names from 8.14.1 release
- cmake: enable `-std=gnu99` for Windows CE CeGCC
- dllmain: exclude from Cygwin builds
- tls BIOs: handle BIO_CTRL_EOF correctly
- curl: make -N handled correctly
- autotools: recognize more Linux targets when setting `-D_GNU_SOURCE`
- cmdline-docs: mention HTTP resumed uploads to be shaky
- pytest: do not use reserved chars in url queries
- scorecard: rework format and add json print
- test1498: verify "-T ."
- RELEASE-NOTES: synced
- curl: upload from '.' fix
- tool_getparam: make --no-anyauth not be accepted
- ws: tests and fixes
- tests: improve server start reliability
- test1510: fix expectation
- asyn-thrdd: fix cleanup when RR fails due to OOM
- GHA/non-native: un-ignore tests on OpenBSD, bump to `-j8` for NetBSD/FreeBSD
- tests: re-enable 1510, unignore 2027 2051 in GHA/macos, document heimdal memleak
- docs/tests: remove mention of hyper
- license: update some copyright links to curl.se
- memanalyze.pl: fix getaddrinfo/freeaddrinfo checks
- VULN-DISCLOSURE-POLICY.md: the distros list wants <= 7 days embargo
- ws: handle blocked sends better
- tests: test mtls also w/ clientAuth EKU only
- tests: test mtls with --insecure
- tests: fix checks for https-mtls proto
- ftp: fix teardown of DATA connection in done
- RELEASE-NOTES: synced
- tests: await portfile to be complete
- spelling: call it null-terminate consistently
- wolfssl: fix sending of early data
- spelling: 'a' vs 'an'
- GHA/non-native: drop AmigaOS jobs, toolchain no longer available
- libssh: adjust indentation
- misc: we write *an* IPv6 address
- tool_getparam: remove two nextarg NULL checks
- docs: fix typos
- misc: fix spelling
- cmake: fix missed version number for multi-pkg-config detections
- misc: fix spelling
- tests: move test docs into /docs
- RELEASE-NOTES: synced
- http: fail early when rewind of input failed when following redirects
- multi: fix add_handle resizing
- tool_getparam: refactored, simplified
- BUG-BOUNTY.md. mention the medium bounty amount in 2025

## Changed C/C++ Files

- `docs/examples/imap-ssl.c`
- `docs/examples/multithread.c`
- `docs/examples/pop3-ssl.c`
- `docs/examples/smtp-ssl.c`
- `include/curl/curl.h`
- `include/curl/curlver.h`
- `include/curl/typecheck-gcc.h`
- `lib/altsvc.c`
- `lib/asyn-thrdd.c`
- `lib/cf-https-connect.c`
- `lib/cfilters.c`
- `lib/cfilters.h`
- `lib/config-win32.h`
- `lib/curl_addrinfo.c`
- `lib/curl_sspi.c`
- `lib/curl_sspi.h`
- `lib/curlx/base64.c`
- `lib/dllmain.c`
- `lib/doh.c`
- `lib/dynhds.h`
- `lib/ftp.c`
- `lib/headers.c`
- `lib/hsts.c`
- `lib/http.c`
- `lib/http1.c`
- `lib/http_aws_sigv4.c`
- `lib/http_aws_sigv4.h`
- `lib/http_chunks.h`
- `lib/imap.c`
- `lib/inet_ntop.c`
- `lib/multi.c`
- `lib/multi_ev.c`
- `lib/noproxy.c`
- `lib/pop3.c`
- `lib/setopt.c`
- `lib/smb.c`
- `lib/smtp.c`
- `lib/socks.c`
- `lib/strcase.c`
- `lib/strdup.c`
- `lib/system_win32.c`
- `lib/transfer.h`
- `lib/uint-table.h`
- `lib/url.c`
- `lib/vauth/digest.c`
- `lib/vauth/digest_sspi.c`
- `lib/vauth/vauth.c`
- `lib/vauth/vauth.h`
- `lib/vquic/curl_osslq.c`
- `lib/vssh/libssh.c`
- `lib/vssh/libssh2.c`
- `lib/vtls/gtls.c`
- `lib/vtls/keylog.c`
- `lib/vtls/keylog.h`
- `lib/vtls/openssl.c`
- `lib/vtls/schannel_verify.c`
- `lib/vtls/vtls.c`
- `lib/vtls/vtls_scache.c`
- `lib/vtls/vtls_scache.h`
- `lib/vtls/wolfssl.c`
- `lib/vtls/x509asn1.c`
- `lib/ws.c`
- `packages/vms/curl_crtl_init.c`
- `src/config2setopts.c`
- `src/tool_cb_hdr.c`
- `src/tool_cfgable.h`
- `src/tool_getparam.c`
- `src/tool_getparam.h`
- `src/tool_helpers.c`
- `src/tool_parsecfg.c`
- `tests/http/clients/hx-upload.c`
- `tests/libtest/lib1933.c`
- `tests/libtest/lib1934.c`
- `tests/libtest/lib1935.c`
- `tests/libtest/lib1936.c`
- `tests/libtest/lib1937.c`
- `tests/libtest/lib1938.c`
- `tests/libtest/lib1939.c`
- `tests/libtest/lib1940.c`
- `tests/libtest/lib1945.c`
- `tests/libtest/lib1947.c`
- `tests/libtest/lib1948.c`
- `tests/libtest/lib1955.c`
- `tests/libtest/lib1956.c`
- `tests/libtest/lib1957.c`
- `tests/libtest/lib1958.c`
- `tests/libtest/lib1959.c`
- `tests/libtest/lib1960.c`
- `tests/libtest/lib1964.c`
- `tests/libtest/lib1970.c`
- `tests/libtest/lib1971.c`
- `tests/libtest/lib1972.c`
- `tests/libtest/lib1973.c`
- `tests/libtest/lib1974.c`
- `tests/libtest/lib1975.c`
- `tests/libtest/lib1978.c`
- `tests/libtest/lib2305.c`
- `tests/libtest/lib2310.c`
- `tests/libtest/lib2311.c`
- `tests/libtest/lib2312.c`
- `tests/libtest/lib2405.c`
- `tests/libtest/lib2700.c`
- `tests/libtest/lib518.c`
- `tests/libtest/lib537.c`
- `tests/libtest/lib751.c`
- `tests/libtest/stub_gssapi.c`
- `tests/server/getpart.c`
- `tests/unit/unit1658.c`
- `tests/unit/unit1660.c`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `main` | `modified` | `docs/examples/imap-ssl.c` | `40-94` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 2 | `main` | `modified` | `docs/examples/pop3-ssl.c` | `40-93` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 3 | `main` | `modified` | `docs/examples/smtp-ssl.c` | `89-170` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 4 | `altsvc_add` | `modified` | `lib/altsvc.c` | `154-209` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 5 | `Curl_async_is_resolved` | `modified` | `lib/asyn-thrdd.c` | `547-641` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 6 | `Curl_cf_https_setup` | `modified` | `lib/cf-https-connect.c` | `644-741` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 7 | `Curl_conn_is_setup` | `added` | `lib/cfilters.c` | `500-503` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 8 | `Curl_unix2addr` | `modified` | `lib/curl_addrinfo.c` | `454-491` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `ftp_state_use_port` | `modified` | `lib/ftp.c` | `873-1255` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 10 | `ftp_state_use_pasv` | `modified` | `lib/ftp.c` | `1257-1295` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 11 | `ftp_epsv_disable` | `modified` | `lib/ftp.c` | `1736-1765` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `ftp_pp_statemachine` | `modified` | `lib/ftp.c` | `2661-3123` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `ftp_done` | `modified` | `lib/ftp.c` | `3219-3434` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 14 | `namevalue` | `modified` | `lib/headers.c` | `189-222` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 15 | `Curl_headers_push` | `modified` | `lib/headers.c` | `278-344` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 16 | `Curl_hsts` | `modified` | `lib/hsts.c` | `245-288` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 17 | `hsts_add` | `modified` | `lib/hsts.c` | `411-460` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 18 | `Curl_http_output_auth` | `modified` | `lib/http.c` | `749-3858` | `unmatched` | unmatched; level=unmatched; diff_hunks=10; fallback_calls=0 |
| 19 | `Curl_http_follow` | `modified` | `lib/http.c` | `1172-1458` | `unmatched` | unmatched; level=unmatched; diff_hunks=9; fallback_calls=0 |
| 20 | `http_on_response` | `modified` | `lib/http.c` | `3577-3676` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 21 | `start_req` | `modified` | `lib/http1.c` | `137-258` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `trim_headers` | `modified` | `lib/http_aws_sigv4.c` | `103-138` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 23 | `imap_state_capability_resp` | `modified` | `lib/imap.c` | `1024-1104` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 24 | `multi_xfers_add` | `modified` | `lib/multi.c` | `335-369` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 25 | `multi_timeout` | `modified` | `lib/multi.c` | `3168-3210` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 26 | `mev_pollset_diff` | `modified` | `lib/multi_ev.c` | `294-439` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 27 | `Curl_check_noproxy` | `modified` | `lib/noproxy.c` | `123-261` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 28 | `pop3_state_capa_resp` | `modified` | `lib/pop3.c` | `861-948` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 29 | `setopt_cptr` | `modified` | `lib/setopt.c` | `1665-2711` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 30 | `setopt_func` | `modified` | `lib/setopt.c` | `2713-2885` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 31 | `smb_send_setup` | `modified` | `lib/smb.c` | `679-732` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 32 | `smb_send_tree_connect` | `modified` | `lib/smb.c` | `734-763` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 33 | `smtp_perform_upgrade_tls` | `modified` | `lib/smtp.c` | `462-496` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 34 | `smtp_state_ehlo_resp` | `modified` | `lib/smtp.c` | `960-1061` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 35 | `do_SOCKS4` | `modified` | `lib/socks.c` | `283-542` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 36 | `Curl_load_library` | `modified` | `lib/system_win32.c` | `179-242` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 37 | `url_match_destination` | `modified` | `lib/url.c` | `1118-1157` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 38 | `auth_digest_string_quoted` | `modified` | `lib/vauth/digest.c` | `164-193` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 39 | `cf_osslq_query` | `modified` | `lib/vquic/curl_osslq.c` | `2351-2405` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 40 | `myssh_state_sftp_dowload_stat` | `deleted` | `lib/vssh/libssh.c` | `925-1071` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 41 | `myssh_state_sftp_download_stat` | `added` | `lib/vssh/libssh.c` | `925-1071` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 42 | `myssh_statemach_act` | `modified` | `lib/vssh/libssh.c` | `1079-2019` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 43 | `ssh_state_sftp_realpath` | `modified` | `lib/vssh/libssh2.c` | `1995-2046` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 44 | `Curl_tls_keylog_write_line` | `modified` | `lib/vtls/keylog.c` | `84-111` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 45 | `ossl_bio_cf_ctrl` | `modified` | `lib/vtls/openssl.c` | `678-712` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 46 | `add_certs_file_to_store` | `modified` | `lib/vtls/schannel_verify.c` | `241-350` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 47 | `Curl_pin_peer_pubkey` | `modified` | `lib/vtls/vtls.c` | `715-869` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 48 | `cf_ssl_scache_session_ldestroy` | `added` | `lib/vtls/vtls_scache.c` | `111-119` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 49 | `cf_ssl_scache_sesssion_ldestroy` | `deleted` | `lib/vtls/vtls_scache.c` | `111-119` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 50 | `Curl_ssl_session_create2` | `modified` | `lib/vtls/vtls_scache.c` | `132-170` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 51 | `Curl_ssl_session_destroy` | `modified` | `lib/vtls/vtls_scache.c` | `172-182` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 52 | `Curl_ssl_scache_create` | `modified` | `lib/vtls/vtls_scache.c` | `317-349` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 53 | `Curl_ssl_peer_key_make` | `modified` | `lib/vtls/vtls_scache.c` | `448-607` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 54 | `wssl_bio_cf_ctrl` | `modified` | `lib/vtls/wolfssl.c` | `272-313` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 55 | `wssl_on_session_reuse` | `modified` | `lib/vtls/wolfssl.c` | `501-538` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 56 | `wssl_setup_session` | `modified` | `lib/vtls/wolfssl.c` | `540-603` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 57 | `keylog_callback` | `deleted` | `lib/vtls/wolfssl.c` | `935-939` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 58 | `ws_frame_firstbyte2flags` | `modified` | `lib/ws.c` | `144-221` | `unmatched` | unmatched; level=unmatched; diff_hunks=17; fallback_calls=0 |
| 59 | `ws_frame_flags2firstbyte` | `modified` | `lib/ws.c` | `223-280` | `unmatched` | unmatched; level=unmatched; diff_hunks=8; fallback_calls=0 |
| 60 | `ws_dec_info` | `modified` | `lib/ws.c` | `282-309` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 61 | `ws_dec_read_head` | `modified` | `lib/ws.c` | `348-467` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 62 | `ws_dec_pass_payload` | `modified` | `lib/ws.c` | `469-498` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 63 | `ws_dec_pass` | `modified` | `lib/ws.c` | `500-554` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 64 | `ws_cw_dec_next` | `modified` | `lib/ws.c` | `600-636` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 65 | `ws_cw_write` | `modified` | `lib/ws.c` | `638-692` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 66 | `ws_enc_info` | `modified` | `lib/ws.c` | `705-713` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 67 | `ws_enc_write_head` | `modified` | `lib/ws.c` | `750-850` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 68 | `Curl_ws_accept` | `modified` | `lib/ws.c` | `967-1076` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 69 | `ws_client_collect` | `modified` | `lib/ws.c` | `1090-1138` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 70 | `curl_ws_recv` | `modified` | `lib/ws.c` | `1153-1237` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 71 | `ws_flush` | `modified` | `lib/ws.c` | `1239-1295` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 72 | `ws_send_raw_blocking` | `modified` | `lib/ws.c` | `1297-1337` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 73 | `ws_send_raw` | `modified` | `lib/ws.c` | `1339-1374` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 74 | `curl_ws_send` | `modified` | `lib/ws.c` | `1376-1516` | `unmatched` | unmatched; level=unmatched; diff_hunks=7; fallback_calls=0 |
| 75 | `sys_trnlnm` | `modified` | `packages/vms/curl_crtl_init.c` | `106-140` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 76 | `gen_trace_setopts` | `added` | `src/config2setopts.c` | `643-652` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 77 | `gen_cb_setopts` | `modified` | `src/config2setopts.c` | `654-694` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 78 | `config2setopts` | `modified` | `src/config2setopts.c` | `781-1145` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 79 | `tool_header_cb` | `modified` | `src/tool_cb_hdr.c` | `87-316` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 80 | `write_linked_location` | `modified` | `src/tool_cb_hdr.c` | `407-490` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| ... | ... | ... | ... | ... | ... | truncated at 80 of 121 functions |

## Function-Level Diff Snippets

### 1. `main` in `docs/examples/imap-ssl.c`

```diff
-    * imaps:// rather than imap:// to request a SSL based connection. */
+    * imaps:// rather than imap:// to request an SSL based connection. */
```

### 2. `main` in `docs/examples/pop3-ssl.c`

```diff
-    /* This retrieves message 1 from the user's mailbox. Note the use of
-     * pop3s:// rather than pop3:// to request a SSL based connection. */
+    /* This retrieves message 1 from the user's mailbox. Note the use of *
+       pop3s:// rather than pop3:// to request an SSL based connection. */
```

### 3. `main` in `docs/examples/smtp-ssl.c`

```diff
-     * than smtp:// to request a SSL based connection. */
+     * than smtp:// to request an SSL based connection. */
```

### 4. `altsvc_add` in `lib/altsvc.c`

```diff
-    /* The date parser works on a null terminated string. The maximum length
+    /* The date parser works on a null-terminated string. The maximum length
```

### 5. `Curl_async_is_resolved` in `lib/asyn-thrdd.c`

```diff
-          if(!lhrr) {
-            async_thrdd_destroy(data);
-            return CURLE_OUT_OF_MEMORY;
-          }
-          data->state.async.dns->hinfo = lhrr;
+          if(!lhrr)
+            result = CURLE_OUT_OF_MEMORY;
+          else
+            data->state.async.dns->hinfo = lhrr;
-     if(!result && data->state.async.dns)
-       result = Curl_dnscache_add(data, data->state.async.dns);
+      if(!result && data->state.async.dns)
... truncated 1 additional diff lines ...
```

### 6. `Curl_cf_https_setup` in `lib/cf-https-connect.c`

```diff
-    /* Is there a HTTPSRR use its ALPNs here.
+    /* Is there an HTTPSRR use its ALPNs here.
```

### 7. `Curl_conn_is_setup` in `lib/cfilters.c`

```diff
+bool Curl_conn_is_setup(struct connectdata *conn, int sockindex)
+{
+  return (conn->cfilter[sockindex] != NULL);
+}
```

### 8. `Curl_unix2addr` in `lib/curl_addrinfo.c`

```diff
-  /* sun_path must be able to store the NUL-terminated path */
+  /* sun_path must be able to store the null-terminated path */
```

### 9. `ftp_state_use_port` in `lib/ftp.c`

```diff
-    /* EPRT is disabled but we are connected to a IPv6 host, so we ignore the
+    /* EPRT is disabled but we are connected to an IPv6 host, so we ignore the
```

### 10. `ftp_state_use_pasv` in `lib/ftp.c`

```diff
-    /* EPSV is disabled but we are connected to a IPv6 host, so we ignore the
+    /* EPSV is disabled but we are connected to an IPv6 host, so we ignore the
```

### 11. `ftp_epsv_disable` in `lib/ftp.c`

```diff
-  Curl_conn_close(data, SECONDARYSOCKET);
-  Curl_conn_cf_discard_all(data, conn, SECONDARYSOCKET);
+  close_secondarysocket(data, ftpc);
```

### 12. `ftp_pp_statemachine` in `lib/ftp.c`

```diff
-        /* We do not have a SSL/TLS control connection yet, but FTPS is
-           requested. Try a FTPS connection now */
+        /* We do not have an SSL/TLS control connection yet, but FTPS is
+           requested. Try an FTPS connection now */
```

### 13. `ftp_done` in `lib/ftp.c`

```diff
-  if(conn->sock[SECONDARYSOCKET] != CURL_SOCKET_BAD) {
+  if(Curl_conn_is_setup(conn, SECONDARYSOCKET)) {
```

### 14. `namevalue` in `lib/headers.c`

```diff
-    *end-- = 0; /* nul terminate */
+    *end-- = 0; /* null-terminate */
```

### 15. `Curl_headers_push` in `lib/headers.c`

```diff
-  hs->buffer[hlen] = 0; /* nul terminate */
+  hs->buffer[hlen] = 0; /* null-terminate */
```

### 16. `Curl_hsts` in `lib/hsts.c`

```diff
-      /* avoid strcasecompare because the host name is not null terminated */
+      /* avoid strcasecompare because the host name is not null-terminated */
```

### 17. `hsts_add` in `lib/hsts.c`

```diff
-    /* The date parser works on a null terminated string. The maximum length
+    /* The date parser works on a null-terminated string. The maximum length
```

### 18. `Curl_http_output_auth` in `lib/http.c`

```diff
+  CURLcode rewind_result;
+  bool switch_to_get = FALSE;
-  Curl_req_soft_reset(&data->req, data);
+  rewind_result = Curl_req_soft_reset(&data->req, data);
-       && !(data->set.keep_post & CURL_REDIR_POST_301))
+       && !(data->set.keep_post & CURL_REDIR_POST_301)) {
+      switch_to_get = TRUE;
+    }
-       && !(data->set.keep_post & CURL_REDIR_POST_302))
+       && !(data->set.keep_post & CURL_REDIR_POST_302)) {
+      switch_to_get = TRUE;
+    }
... truncated 12 additional diff lines ...
```

### 19. `Curl_http_follow` in `lib/http.c`

```diff
+  CURLcode rewind_result;
+  bool switch_to_get = FALSE;
-  Curl_req_soft_reset(&data->req, data);
+  rewind_result = Curl_req_soft_reset(&data->req, data);
-       && !(data->set.keep_post & CURL_REDIR_POST_301))
+       && !(data->set.keep_post & CURL_REDIR_POST_301)) {
+      switch_to_get = TRUE;
+    }
-       && !(data->set.keep_post & CURL_REDIR_POST_302))
+       && !(data->set.keep_post & CURL_REDIR_POST_302)) {
+      switch_to_get = TRUE;
+    }
... truncated 10 additional diff lines ...
```

### 20. `http_on_response` in `lib/http.c`

```diff
-        k->httpversion_sent = 20; /* It's a HTTP/2 request now */
+        k->httpversion_sent = 20; /* It's an HTTP/2 request now */
```

### 21. `start_req` in `lib/http1.c`

```diff
-    /* URL parser wants 0-termination */
+    /* URL parser wants null-termination */
```

### 22. `trim_headers` in `lib/http_aws_sigv4.c`

```diff
-    *store = 0; /* null terminate */
+    *store = 0; /* null-terminate */
```

### 23. `imap_state_capability_resp` in `lib/imap.c`

```diff
-  /* Do we have a untagged response? */
+  /* Do we have an untagged response? */
```

### 24. `multi_xfers_add` in `lib/multi.c`

```diff
-    unsigned int newsize = ((capacity + min_unused) + 63) / 64;
+    unsigned int newsize = (((capacity + min_unused) + 63) / 64) * 64;
+    DEBUGASSERT(newsize > capacity);
```

### 25. `multi_timeout` in `lib/multi.c`

```diff
-    /* this will not return NULL from a non-emtpy tree, but some compilers
+    /* this will not return NULL from a non-empty tree, but some compilers
```

### 26. `mev_pollset_diff` in `lib/multi_ev.c`

```diff
-   * in and which combinatino of CURL_POLL_IN/CURL_POLL_OUT it wants
+   * in and which combination of CURL_POLL_IN/CURL_POLL_OUT it wants
```

### 27. `Curl_check_noproxy` in `lib/noproxy.c`

```diff
-            *slash = 0; /* null terminate there */
+            *slash = 0; /* null-terminate there */
```

### 28. `pop3_state_capa_resp` in `lib/pop3.c`

```diff
-  /* Do we have a untagged continuation response? */
+  /* Do we have an untagged continuation response? */
```

### 29. `setopt_cptr` in `lib/setopt.c`

```diff
-     * Set a SSL_CTX callback parameter pointer
+     * Set an SSL_CTX callback parameter pointer
```

### 30. `setopt_func` in `lib/setopt.c`

```diff
-     * Set a SSL_CTX callback
+     * Set an SSL_CTX callback
```

### 31. `smb_send_setup` in `lib/smb.c`

```diff
-  p++; /* count the final null termination */
+  p++; /* count the final null-termination */
```

### 32. `smb_send_tree_connect` in `lib/smb.c`

```diff
-  p++; /* count the final null termination */
+  p++; /* count the final null-termination */
```

### 33. `smtp_perform_upgrade_tls` in `lib/smtp.c`

```diff
-    /* perform EHLO now, changes smpt->state out of SMTP_UPGRADETLS */
+    /* perform EHLO now, changes smtp->state out of SMTP_UPGRADETLS */
```

### 34. `smtp_state_ehlo_resp` in `lib/smtp.c`

```diff
-        /* We do not have a SSL/TLS connection yet, but SSL is requested */
+        /* We do not have an SSL/TLS connection yet, but SSL is requested */
```

### 35. `do_SOCKS4` in `lib/socks.c`

```diff
-    socksreq[8] = 0; /* ensure empty userid is NUL-terminated */
+    socksreq[8] = 0; /* ensure empty userid is null-terminated */
```

### 36. `Curl_load_library` in `lib/system_win32.c`

```diff
-      /* Allocate space for the full DLL path (Room for the null terminator
+      /* Allocate space for the full DLL path (Room for the null-terminator
```

### 37. `url_match_destination` in `lib/url.c`

```diff
-          "Connection #%" FMT_OFF_T " has compatible protocol famiy, "
+          "Connection #%" FMT_OFF_T " has compatible protocol family, "
```

### 38. `auth_digest_string_quoted` in `lib/vauth/digest.c`

```diff
-  size_t n = 1; /* null terminator */
+  size_t n = 1; /* null-terminator */
```

### 39. `cf_osslq_query` in `lib/vquic/curl_osslq.c`

```diff
-    CURL_TRC_CF(data, cf, "query max_conncurrent -> %d", *pres1);
+    CURL_TRC_CF(data, cf, "query max_concurrent -> %d", *pres1);
```

### 40. `myssh_state_sftp_dowload_stat` in `lib/vssh/libssh.c`

```diff
-static int myssh_state_sftp_dowload_stat(struct Curl_easy *data,
-                                         struct ssh_conn *sshc)
```

### 41. `myssh_state_sftp_download_stat` in `lib/vssh/libssh.c`

```diff
+static int myssh_state_sftp_download_stat(struct Curl_easy *data,
+                                          struct ssh_conn *sshc)
```

### 42. `myssh_statemach_act` in `lib/vssh/libssh.c`

```diff
-      rc = myssh_state_sftp_dowload_stat(data, sshc);
+      rc = myssh_state_sftp_download_stat(data, sshc);
```

### 43. `ssh_state_sftp_realpath` in `lib/vssh/libssh2.c`

```diff
-    /* It seems that this string is not always NULL terminated */
+    /* It seems that this string is not always null-terminated */
```

### 44. `Curl_tls_keylog_write_line` in `lib/vtls/keylog.c`

```diff
-    /* Empty line or too big to fit in a LF and NUL. */
+    /* Empty line or too big to fit in an LF and NUL. */
```

### 45. `ossl_bio_cf_ctrl` in `lib/vtls/openssl.c`

```diff
-  case BIO_CTRL_EOF:
+  case BIO_CTRL_EOF: {
-    return !cf->next || !cf->next->connected;
+    struct ssl_connect_data *connssl = cf->ctx;
+    return connssl->peer_closed;
+  }
```

### 46. `add_certs_file_to_store` in `lib/vtls/schannel_verify.c`

```diff
-  /* Null terminate the buffer */
+  /* null-terminate the buffer */
```

### 47. `Curl_pin_peer_pubkey` in `lib/vtls/vtls.c`

```diff
-       * if there is an end_pos, null terminate,
-       * otherwise it will go to the end of the original string
+       * if there is an end_pos, null-terminate, otherwise it will go to the
+       * end of the original string
-     * Otherwise we will assume it is PEM and try to decode it
-     * after placing null terminator
+     * Otherwise we will assume it is PEM and try to decode it after placing
+     * null-terminator
```

### 48. `cf_ssl_scache_session_ldestroy` in `lib/vtls/vtls_scache.c`

```diff
+static void cf_ssl_scache_session_ldestroy(void *udata, void *obj)
```

### 49. `cf_ssl_scache_sesssion_ldestroy` in `lib/vtls/vtls_scache.c`

```diff
-static void cf_ssl_scache_sesssion_ldestroy(void *udata, void *obj)
```

### 50. `Curl_ssl_session_create2` in `lib/vtls/vtls_scache.c`

```diff
-      cf_ssl_scache_sesssion_ldestroy(NULL, s);
+      cf_ssl_scache_session_ldestroy(NULL, s);
```

### 51. `Curl_ssl_session_destroy` in `lib/vtls/vtls_scache.c`

```diff
-      cf_ssl_scache_sesssion_ldestroy(NULL, s);
+      cf_ssl_scache_session_ldestroy(NULL, s);
```

### 52. `Curl_ssl_scache_create` in `lib/vtls/vtls_scache.c`

```diff
-                    cf_ssl_scache_sesssion_ldestroy);
+                    cf_ssl_scache_session_ldestroy);
```

### 53. `Curl_ssl_peer_key_make` in `lib/vtls/vtls_scache.c`

```diff
-  /* we just added printable char, and dynbuf always 0 terminates,
-   * no need to track length */
-
+  /* we just added printable char, and dynbuf always null-terminates, no need
+   * to track length */
```

### 54. `wssl_bio_cf_ctrl` in `lib/vtls/wolfssl.c`

```diff
-  case WOLFSSL_BIO_CTRL_EOF:
+  case WOLFSSL_BIO_CTRL_EOF: {
-    return !cf->next || !cf->next->connected;
+    struct ssl_connect_data *connssl = cf->ctx;
+    return connssl->peer_closed;
+  }
```

### 55. `wssl_on_session_reuse` in `lib/vtls/wolfssl.c`

```diff
-                            wolfSSL_get_session(wssl->ssl));
+    wolfSSL_get_session(wssl->ssl));
```

### 56. `wssl_setup_session` in `lib/vtls/wolfssl.c`

```diff
+#ifdef WOLFSSL_EARLY_DATA
+            unsigned int edmax = (scs->earlydata_max < UINT_MAX) ?
+              (unsigned int)scs->earlydata_max : UINT_MAX;
+            wolfSSL_set_max_early_data(wss->ssl, edmax);
+#else
+          /* Should never enable when not supported */
+          DEBUGASSERT(!do_early_data);
+#endif
```

### 57. `keylog_callback` in `lib/vtls/wolfssl.c`

```diff
-static void keylog_callback(const WOLFSSL *ssl, const char *line)
-{
-  (void)ssl;
-  Curl_tls_keylog_write_line(line);
-}
```

### 58. `ws_frame_firstbyte2flags` in `lib/ws.c`

```diff
+    /* 0x00 - intermediate TEXT/BINARY fragment */
-      /* continuation of a previous fragment: restore stored flags */
+      if(!(cont_flags & CURLWS_CONT)) {
+        failf(data, "[WS] no ongoing fragmented message to resume");
+        return 0;
+      }
+    /* 0x80 - final TEXT/BIN fragment */
-      /* continuation of a previous fragment: restore stored flags */
+      if(!(cont_flags & CURLWS_CONT)) {
+        failf(data, "[WS] no ongoing fragmented message to resume");
+        return 0;
+      }
... truncated 50 additional diff lines ...
```

### 59. `ws_frame_flags2firstbyte` in `lib/ws.c`

```diff
+        infof(data, "[WS] no flags given; interpreting as continuation "
+      failf(data, "[WS] no flags given");
+        infof(data, "[WS] setting CURLWS_CONT flag without message type is "
+      failf(data, "[WS] No ongoing fragmented message to continue");
+      failf(data, "[WS] CLOSE frame must not be fragmented");
-      failf(data, "WS: PING frame must not be fragmented");
+      failf(data, "[WS] PING frame must not be fragmented");
-      failf(data, "WS: PONG frame must not be fragmented");
+      failf(data, "[WS] PONG frame must not be fragmented");
-      failf(data, "WS: unknown flags: %x", flags);
-      *err = CURLE_SEND_ERROR;
+      failf(data, "[WS] unknown flags: %x", flags);
... truncated 1 additional diff lines ...
```

### 60. `ws_dec_info` in `lib/ws.c`

```diff
+    CURL_TRC_WS(data, "decoded %s [%s%s]", msg,
+                ws_frame_name_of_op(dec->head[0]),
+                (dec->head[0] & WSBIT_FIN) ? "" : " NON-FINAL");
+      CURL_TRC_WS(data, "decoded %s [%s%s](%d/%d)", msg,
+                  ws_frame_name_of_op(dec->head[0]),
+                  (dec->head[0] & WSBIT_FIN) ? "" : " NON-FINAL",
+                  dec->head_len, dec->head_total);
+      CURL_TRC_WS(data, "decoded %s [%s%s payload=%"
+                  FMT_OFF_T "/%" FMT_OFF_T "]",
+                  msg, ws_frame_name_of_op(dec->head[0]),
+                  (dec->head[0] & WSBIT_FIN) ? "" : " NON-FINAL",
+                  dec->payload_offset, dec->payload_len);
```

### 61. `ws_dec_read_head` in `lib/ws.c`

```diff
+      /* fragmentation only applies to data frames (text/binary);
+       * control frames (close/ping/pong) do not affect the CONT status */
+      if(dec->frame_flags & (CURLWS_TEXT | CURLWS_BINARY)) {
+        failf(data, "[WS] masked input frame");
+      if(dec->frame_flags & CURLWS_PING && dec->head[1] > 125) {
+        /* The maximum valid size of PING frames is 125 bytes.
+           Accepting overlong pings would mean sending equivalent pongs! */
+        failf(data, "[WS] received PING frame is too big");
+        ws_dec_reset(dec);
+        return CURLE_RECV_ERROR;
+      }
+      if(dec->frame_flags & CURLWS_PONG && dec->head[1] > 125) {
... truncated 16 additional diff lines ...
```

### 62. `ws_dec_pass_payload` in `lib/ws.c`

```diff
+    CURL_TRC_WS(data, "passed %zd bytes payload, %"
+                FMT_OFF_T " remain", nwritten, remain);
```

### 63. `ws_dec_pass` in `lib/ws.c`

```diff
+        infof(data, "[WS] decode error %d", (int)result);
```

### 64. `ws_cw_dec_next` in `lib/ws.c`

```diff
+    infof(data, "[WS] auto-respond to PING with a PONG");
```

### 65. `ws_cw_write` in `lib/ws.c`

```diff
+    failf(data, "[WS] not a websocket transfer");
+      infof(data, "[WS] error adding data to buffer %d", result);
+      CURL_TRC_WS(data, "buffered incomplete frame head");
+      infof(data, "[WS] decode error %d", (int)result);
+    failf(data, "[WS] decode ending with %zd frame bytes remaining",
```

### 66. `ws_enc_info` in `lib/ws.c`

```diff
+  CURL_TRC_WS(data, "WS-ENC: %s [%s%s payload=%"
+              FMT_OFF_T "/%" FMT_OFF_T "]",
+              msg, ws_frame_name_of_op(enc->firstbyte),
+              (enc->firstbyte & WSBIT_FIN) ? "" : " NON-FIN",
+              enc->payload_len - enc->payload_remain, enc->payload_len);
```

### 67. `ws_enc_write_head` in `lib/ws.c`

```diff
+    failf(data, "[WS] starting new frame with negative payload length %"
+    failf(data, "[WS] starting new frame with %zd bytes from last one "
+  if(flags & CURLWS_PING && payload_len > 125) {
+    /* The maximum valid size of PING frames is 125 bytes. */
+    failf(data, "[WS] given PING frame is too big");
+    *err = CURLE_TOO_LARGE;
+    return -1;
+  }
+  if(flags & CURLWS_PONG && payload_len > 125) {
+    /* The maximum valid size of PONG frames is 125 bytes. */
+    failf(data, "[WS] given PONG frame is too big");
+    *err = CURLE_TOO_LARGE;
... truncated 9 additional diff lines ...
```

### 68. `Curl_ws_accept` in `lib/ws.c`

```diff
+
+#ifdef DEBUGBUILD
+  if(getenv("CURL_WS_FORCE_ZERO_MASK"))
+    /* force the bit mask to 0x00000000, effectively disabling masking */
+    memset(ws->enc.mask, 0, sizeof(ws->enc.mask));
+#endif
+
+  infof(data, "[WS] Received 101, switch to WebSocket; mask %02x%02x%02x%02x",
-    infof(data, "%zu bytes websocket payload", nread);
+    CURL_TRC_WS(data, "%zu bytes payload", nread);
```

### 69. `ws_client_collect` in `lib/ws.c`

```diff
+    infof(ctx->data, "[WS] auto-respond to PING with a PONG");
```

### 70. `curl_ws_recv` in `lib/ws.c`

```diff
+      failf(data, "[WS] CONNECT_ONLY is required");
+      failf(data, "[WS] connection not found");
+    failf(data, "[WS] connection is not setup for websocket");
+        infof(data, "[WS] connection expectedly closed?");
```

### 71. `ws_flush` in `lib/ws.c`

```diff
+        failf(data, "[WS] flush, write error %d", result);
+        CURL_TRC_WS(data, "flushed %zu bytes", n);
```

### 72. `ws_send_raw_blocking` in `lib/ws.c`

```diff
+        failf(data, "[WS] Timeout waiting for socket becoming writable");
+        failf(data, "[WS] Error while waiting for socket becoming writable");
```

### 73. `ws_send_raw` in `lib/ws.c`

```diff
+    failf(data, "[WS] Not a websocket transfer");
```

### 74. `curl_ws_send` in `lib/ws.c`

```diff
+    failf(data, "[WS] No associated connection");
+    failf(data, "[WS] Not a websocket transfer");
+      failf(data, "[WS] fragsize and flags must be zero in raw mode");
+      failf(data, "[WS] curl_ws_send() called with smaller 'buflen' than "
+      failf(data, "[WS] unaligned frame size (sending %zu instead of %"
+      if(!ws->sendbuf_payload) {
+        result = CURLE_AGAIN;
+        goto out;
+      }
-    if(!result) {
+    if(!result && ws->sendbuf_payload > 0) {
```

### 75. `sys_trnlnm` in `packages/vms/curl_crtl_init.c`

```diff
-    /* Null terminate and return the string */
+    /* Null-terminate and return the string */
```

### 76. `gen_trace_setopts` in `src/config2setopts.c`

```diff
+static void gen_trace_setopts(struct GlobalConfig *global,
+                              struct OperationConfig *config,
+                              CURL *curl)
+{
+  if(global->tracetype != TRACE_NONE) {
+    my_setopt(curl, CURLOPT_DEBUGFUNCTION, tool_debug_cb);
+    my_setopt(curl, CURLOPT_DEBUGDATA, config);
+    my_setopt_long(curl, CURLOPT_VERBOSE, 1L);
+  }
+}
```

### 77. `gen_cb_setopts` in `src/config2setopts.c`

```diff
+  (void) config;
-  if(global->tracetype != TRACE_NONE) {
-    my_setopt(curl, CURLOPT_DEBUGFUNCTION, tool_debug_cb);
-    my_setopt(curl, CURLOPT_DEBUGDATA, config);
-    my_setopt_long(curl, CURLOPT_VERBOSE, 1L);
-  }
-
```

### 78. `config2setopts` in `src/config2setopts.c`

```diff
-  gen_cb_setopts(global, config, per, curl);
+  gen_trace_setopts(global, config, curl);
+  /* call after the line above. It may override CURLOPT_NOPROGRESS */
+  gen_cb_setopts(global, config, per, curl);
+
```

### 79. `tool_header_cb` in `src/tool_cb_hdr.c`

```diff
-           memory. Since it is not zero terminated, we need an extra dance. */
+           memory. Since it is not null-terminated, we need an extra dance. */
```

### 80. `write_linked_location` in `src/tool_cb_hdr.c`

```diff
-  /* Create a NUL-terminated and whitespace-stripped copy of Location: */
+  /* Create a null-terminated and whitespace-stripped copy of Location: */
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

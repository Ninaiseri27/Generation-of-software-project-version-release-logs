# Evidence Pack: third_party_curl OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `curl_v6_0_beta1_to_v6_0`
- Repository: `third_party_curl`
- Category: `network`
- Reference version: `OpenHarmony-v6.0-Beta1`
- Target version: `OpenHarmony-v6.0-Release`
- Pipeline status: `verified_full_pipeline_mock`
- Ground-truth status: `draft_required`

## Evidence Sources To Inspect

- [ ] OpenHarmony v6.0 Beta1 and v6.0 platform release notes
- [ ] commit_messages
- [ ] function_level_diff
- [ ] curl CHANGES or RELEASE-NOTES if relevant entries can be mapped

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/changed_functions.json`
- cmg_output: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/cmg.json`
- prompt_input: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/prompt_input.json`
- prompt_bundle: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/prompt_bundle.json`
- release_note_mock_rule_family: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/release_note_mock_rule_family.json`

## Pipeline Summary

- Commit count: `20`
- Changed C/C++ files: `11`
- Changed functions: `12`
- Patch only: `False`
- CMG matched entries: `10`
- CMG unmatched entries: `2`
- Fallback-context entries: `12`
- Diff-derived call edges: `11`
- Prompt entries: `12`
- Mock generated entries: `12`

## Commit Messages

- !330 update BUILD.gn. Merge pull request !330 from heqianmo/master
- update BUILD.gn.
- update bundle.json.
- !328 update bundle.json. Merge pull request !328 from heqianmo/master
- update bundle.json.
- !325 update Merge pull request !325 from liujiaqing/master
- !327 DTS2025052220894 Merge pull request !327 from liujiaqing/master
- DTS2025052220894
- update
- !322 update lib/ftplistparser.c. Merge pull request !322 from HuangHaitao/master
- update lib/ftplistparser.c. 回合https://github.com/curl/curl/commit/196afaf75c4f04ebe33c60cc2ea07301a9b9321a
- !321 add mms reserved default port option Merge pull request !321 from 张文杰/0624
- mms opt
- !319 【轻量级 PR】：update copyright Merge pull request !319 from zhaohui91/N/A
- update copyright update copyright https://gitee.com/openharmony/third_party_curl/issues/ICE4CM
- !317 add options for handover feature Merge pull request !317 from YangWeimin/dev
- !318 clean cache but not destroy Merge pull request !318 from maosiping/master
- clean cache but not destroy
- add options for handover feature
- add handover

## Changed C/C++ Files

- `include/curl/curl.h`
- `lib/asyn-ares.c`
- `lib/cf-socket.c`
- `lib/easyoptions.c`
- `lib/ftplistparser.c`
- `lib/headers.c`
- `lib/http.c`
- `lib/http.h`
- `lib/setopt.c`
- `lib/url.c`
- `lib/urldata.h`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `bindohosnetid` | `added` | `lib/asyn-ares.c` | `169-186` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 2 | `Curl_resolver_init` | `modified` | `lib/asyn-ares.c` | `196-234` | `matched` | matched; level=symbol+overlap; diff_hunks=1; fallback_calls=0 |
| 3 | `bindohosnetid` | `added` | `lib/cf-socket.c` | `403-417` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 4 | `bindlocal` | `modified` | `lib/cf-socket.c` | `420-673` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 5 | `Curl_ftp_parselist` | `modified` | `lib/ftplistparser.c` | `364-1039` | `matched` | matched; level=path+symbol; diff_hunks=3; fallback_calls=0 |
| 6 | `Curl_headers_push` | `modified` | `lib/headers.c` | `277-340` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 7 | `Curl_http_output_auth` | `modified` | `lib/http.c` | `711-3632` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 8 | `Curl_http_target` | `modified` | `lib/http.c` | `1790-1901` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 9 | `Curl_vsetopt` | `modified` | `lib/setopt.c` | `187-3202` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 10 | `Curl_init_userdefined` | `modified` | `lib/url.c` | `350-499` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 11 | `ConnectionExists` | `modified` | `lib/url.c` | `947-1363` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 12 | `allocate_conn` | `modified` | `lib/url.c` | `1385-1479` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `bindohosnetid` in `lib/asyn-ares.c`

```diff
+static int bindohosnetid(ares_socket_t socket_fd, int type, void *data)
+{
+  struct Curl_easy *easy = (struct Curl_easy *)data;
+  if (!easy || socket_fd <= 0) {
+    return -1;
+  }
+  unsigned int netid = easy->set.socket_bind_netid;
+  if (netid > 0) {
+    int ret = BindSocket(socket_fd, netid);
+    if (ret == 0) {
+      return 0;
+    } else {
... truncated 6 additional diff lines ...
```

### 2. `Curl_resolver_init` in `lib/asyn-ares.c`

```diff
+#ifdef HTTP_HANDOVER_FEATURE
+  if (easy->set.socket_bind_netid > 0) {
+    ares_set_socket_configure_callback(resolver, bindohosnetid, easy);
+  }
+#endif
```

### 3. `bindohosnetid` in `lib/cf-socket.c`

```diff
+static CURLcode bindohosnetid(struct Curl_easy *data, struct connectdata *conn, curl_socket_t sockfd)
+{
+  unsigned int netid = data->set.socket_bind_netid;
+  if (netid > 0) {
+    int ret = BindSocket(sockfd, netid);
+    if (ret == 0) {
+      conn->socket_bind_netid = netid;
+      return CURLE_OK;
+    } else {
+      // try bind but failed
+      return CURLE_INTERFACE_FAILED;
+    }
... truncated 3 additional diff lines ...
```

### 4. `bindlocal` in `lib/cf-socket.c`

```diff
+#ifdef HTTP_HANDOVER_FEATURE
+  if (!dev && !port) {
+    /*no local kind of binding was requested */
+    return data->set.socket_bind_netid > 0 ? bindohosnetid(data, conn, sockfd) : CURLE_OK;
+  }
+#else
-
+#endif
```

### 5. `Curl_ftp_parselist` in `lib/ftplistparser.c`

```diff
-            if(ISALNUM(c)) {
+            if(ISALNUM(c) && len) {
-          if(c != ' ') {
+          if(c != ' ' && len) {
-          if(c != ' ') {
+          if(c != ' ' && len) {
```

### 6. `Curl_headers_push` in `lib/headers.c`

```diff
-
+  if(Curl_llist_count(&data->state.httphdrs) >= MAX_HTTP_RESP_HEADER_COUNT) {
+    failf(data, "Too many response headers, %d is max",
+          MAX_HTTP_RESP_HEADER_COUNT);
+    return CURLE_TOO_LARGE;
+  }
```

### 7. `Curl_http_output_auth` in `lib/http.c`

```diff
-    uc = curl_url_get(h, CURLUPART_URL, &url, CURLU_NO_DEFAULT_PORT);
+    if(data->set.mms_reserved_default_port != 1L)
+      uc = curl_url_get(h, CURLUPART_URL, &url, CURLU_NO_DEFAULT_PORT);
+    else
+      uc = curl_url_get(h, CURLUPART_URL, &url, 0);
+
```

### 8. `Curl_http_target` in `lib/http.c`

```diff
-    uc = curl_url_get(h, CURLUPART_URL, &url, CURLU_NO_DEFAULT_PORT);
+    if(data->set.mms_reserved_default_port != 1L)
+      uc = curl_url_get(h, CURLUPART_URL, &url, CURLU_NO_DEFAULT_PORT);
+    else
+      uc = curl_url_get(h, CURLUPART_URL, &url, 0);
+
```

### 9. `Curl_vsetopt` in `lib/setopt.c`

```diff
+#ifdef HTTP_HANDOVER_FEATURE
+  case CURLOPT_OHOS_SOCKET_BIND_NET_ID:
+    uarg = va_arg(param, unsigned long);
+#define MAX_NET_ID (0xFFFF - 0x400)
+    if (uarg > MAX_NET_ID)
+      return CURLE_BAD_FUNCTION_ARGUMENT;
+    data->set.socket_bind_netid = uarg;
+    break;
+  case CURLOPT_CONNREUSEFUNCTION:
+    data->set.fconnreuse = va_arg(param, curl_connreuse_callback);
+    break;
+  case CURLOPT_CONNREUSEDATA:
... truncated 6 additional diff lines ...
```

### 10. `Curl_init_userdefined` in `lib/url.c`

```diff
+#ifdef HTTP_HANDOVER_FEATURE
+  set->socket_bind_netid = 0; /* OHOS default network */
+  set->fconnreuse = ZERO_NULL;
+  set->connreuse_userp = ZERO_NULL;
+#endif
```

### 11. `ConnectionExists` in `lib/url.c`

```diff
-
+#ifdef HTTP_HANDOVER_FEATURE
+    if (check->socket_bind_netid != data->set.socket_bind_netid) {
+      continue;
+    }
+    if (data->set.fconnreuse && !data->set.fconnreuse(data->set.connreuse_userp, check->sockfd)) {
+      // no reuse
+      continue;
+    }
+#endif
```

### 12. `allocate_conn` in `lib/url.c`

```diff
-
+#ifdef HTTP_HANDOVER_FEATURE
+  conn->socket_bind_netid = 0; /* OHOS default net id*/
+#endif
```

## Mock Release-Note Drafts

1. [Features] Add the bindohosnetid routine: Added the bindohosnetid routine.
2. [Internal] Update ConnectionExists: Updated ConnectionExists.
3. [Internal] Update the Curl_ftp_parselist routine: Updated the Curl_ftp_parselist routine.
4. [Internal] Update the Curl_headers_push routine: Updated the Curl_headers_push routine.
5. [Internal] Update the Curl_http_output_auth routine: Updated the Curl_http_output_auth routine.
6. [Internal] Update the Curl_http_target routine: Updated the Curl_http_target routine.
7. [Internal] Update the Curl_init_userdefined routine: Updated the Curl_init_userdefined routine.
8. [Internal] Update the Curl_resolver_init routine: Updated the Curl_resolver_init routine.
9. [Internal] Update the Curl_vsetopt routine: Updated the Curl_vsetopt routine.
10. [Internal] Update the allocate_conn routine: Updated the allocate_conn routine.
11. [Internal] Update the bindlocal routine: Updated the bindlocal routine.

These drafts are generated evidence only. Do not copy them as ground truth without review.

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

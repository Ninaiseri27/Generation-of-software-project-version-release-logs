# Evidence Pack: third_party_mbedtls OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `mbedtls_v6_0_beta1_to_v6_0`
- Repository: `third_party_mbedtls`
- Category: `security_crypto`
- Reference version: `OpenHarmony-v6.0-Beta1`
- Target version: `OpenHarmony-v6.0-Release`
- Pipeline status: `verified_full_pipeline_mock`
- Ground-truth status: `draft_required`

## Evidence Sources To Inspect

- [ ] OpenHarmony v6.0 Beta1 and v6.0 platform release notes
- [ ] commit_messages
- [ ] function_level_diff
- [ ] mbedtls ChangeLog or ChangeLog.d entries if they can be mapped

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/changed_functions.json`
- cmg_output: `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/cmg.json`
- prompt_input: `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/prompt_input.json`
- prompt_bundle: `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/prompt_bundle.json`
- release_note_mock_rule_family: `outputs/benchmark/third_party_mbedtls/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/release_note_mock_rule_family.json`

## Pipeline Summary

- Commit count: `10`
- Changed C/C++ files: `17`
- Changed functions: `23`
- Patch only: `False`
- CMG matched entries: `6`
- CMG unmatched entries: `17`
- Fallback-context entries: `23`
- Diff-derived call edges: `41`
- Prompt entries: `23`
- Mock generated entries: `23`

## Commit Messages

- !157 fix bug CVE-2025-47917 CVE-2025-48965 Merge pull request !157 from 李江海/master
- fix bug CVE-2025-47917 CVE-2025-48965
- !155 Fix CVE-2025-27809 Merge pull request !155 from HuangHaitao/master
- Fix CVE-2025-27809
- !154 【轻量级 PR】：add chipsetsdk Merge pull request !154 from Yiming Lv/N/A
- add chipsetsdk
- !151 [PATCH] Fix bug in mbedtls_asn1_store_named_data() Merge pull request !151 from HuangHaitao/master
- [PATCH] Fix bug in mbedtls_asn1_store_named_data()
- !150 fix CVE-2025-52496,CVE-2025-52497,CVE-2025-49600,CVE-2025-49601 Merge pull request !150 from HuangHaitao/master
- fix CVE-2025-52496,CVE-2025-52497,CVE-2025-49600,CVE-2025-49601

## Changed C/C++ Files

- `include/mbedtls/error.h`
- `include/mbedtls/mbedtls_config.h`
- `include/mbedtls/ssl.h`
- `include/mbedtls/x509.h`
- `library/aesni.c`
- `library/asn1write.c`
- `library/lmots.c`
- `library/lms.c`
- `library/pem.c`
- `library/ssl_client.c`
- `library/ssl_misc.h`
- `library/ssl_tls.c`
- `library/x509_create.c`
- `library/x509write_crt.c`
- `library/x509write_csr.c`
- `programs/x509/cert_req.c`
- `programs/x509/cert_write.c`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `mbedtls_aesni_has_support` | `modified` | `library/aesni.c` | `49-85` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 2 | `mbedtls_asn1_write_raw_buffer` | `modified` | `library/asn1write.c` | `82-98` | `matched` | matched; level=symbol+overlap; diff_hunks=1; fallback_calls=0 |
| 3 | `mbedtls_asn1_store_named_data` | `modified` | `library/asn1write.c` | `376-439` | `matched` | matched; level=symbol+overlap; diff_hunks=1; fallback_calls=0 |
| 4 | `mbedtls_lmots_import_public_key` | `modified` | `library/lmots.c` | `393-425` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 5 | `create_merkle_leaf_value` | `modified` | `library/lms.c` | `94-146` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 6 | `mbedtls_lms_import_public_key` | `modified` | `library/lms.c` | `238-270` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 7 | `mbedtls_lms_verify` | `modified` | `library/lms.c` | `300-418` | `matched` | matched; level=symbol+overlap; diff_hunks=3; fallback_calls=0 |
| 8 | `pem_check_pkcs_padding` | `modified` | `library/pem.c` | `244-266` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `ssl_write_hostname_ext` | `modified` | `library/ssl_client.c` | `25-97` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 10 | `ssl_prepare_client_hello` | `modified` | `library/ssl_client.c` | `736-910` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 11 | `mbedtls_ssl_has_set_hostname_been_called` | `added` | `library/ssl_tls.c` | `2766-2770` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `mbedtls_ssl_get_hostname_pointer` | `added` | `library/ssl_tls.c` | `2778-2784` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `mbedtls_ssl_free_hostname` | `added` | `library/ssl_tls.c` | `2786-2793` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 14 | `mbedtls_ssl_set_hostname` | `modified` | `library/ssl_tls.c` | `2795-2836` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 15 | `mbedtls_ssl_free` | `modified` | `library/ssl_tls.c` | `5540-5610` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 16 | `get_hostname_for_verification` | `added` | `library/ssl_tls.c` | `9780-9799` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 17 | `mbedtls_ssl_verify_certificate` | `modified` | `library/ssl_tls.c` | `9801-9986` | `unmatched` | unmatched; level=unmatched; diff_hunks=3; fallback_calls=0 |
| 18 | `mbedtls_x509_string_to_names` | `modified` | `library/x509_create.c` | `281-379` | `matched` | matched; level=symbol+overlap; diff_hunks=1; fallback_calls=0 |
| 19 | `mbedtls_x509write_crt_set_subject_name` | `modified` | `library/x509write_crt.c` | `80-85` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 20 | `mbedtls_x509write_crt_set_issuer_name` | `modified` | `library/x509write_crt.c` | `87-92` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 21 | `mbedtls_x509write_csr_set_subject_name` | `modified` | `library/x509write_csr.c` | `62-67` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `main` | `modified` | `programs/x509/cert_req.c` | `140-530` | `matched` | matched; level=path+symbol; diff_hunks=5; fallback_calls=0 |
| 23 | `main` | `modified` | `programs/x509/cert_write.c` | `290-1038` | `matched` | matched; level=path+symbol; diff_hunks=5; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `mbedtls_aesni_has_support` in `library/aesni.c`

```diff
-    static int done = 0;
-    static unsigned int c = 0;
+    /* To avoid a race condition, tell the compiler that the assignment
+     * `done = 1` and the assignment to `c` may not be reordered.
+     * https://github.com/Mbed-TLS/mbedtls/issues/9840
+     *
+     * Note that we may also be worried about memory access reordering,
+     * but fortunately the x86 memory model is not too wild: stores
+     * from the same thread are observed consistently by other threads.
+     * (See example 8-1 in Sewell et al., "x86-TSO: A Rigorous and Usable
+     * Programmer’s Model for x86 Multiprocessors", CACM, 2010,
+     * https://www.cl.cam.ac.uk/~pes20/weakmemory/cacm.pdf)
... truncated 3 additional diff lines ...
```

### 2. `mbedtls_asn1_write_raw_buffer` in `library/asn1write.c`

```diff
-    memcpy(*p, buf, len);
+    if (len != 0) {
+        memcpy(*p, buf, len);
+    }
```

### 3. `mbedtls_asn1_store_named_data` in `library/asn1write.c`

```diff
+        cur->val.len = 0;
```

### 4. `mbedtls_lmots_import_public_key` in `library/lmots.c`

```diff
-    ctx->params.type = (mbedtls_lmots_algorithm_type_t)
-                       MBEDTLS_GET_UINT32_BE(key, MBEDTLS_LMOTS_SIG_TYPE_OFFSET);
+    uint32_t type = MBEDTLS_GET_UINT32_BE(key, MBEDTLS_LMOTS_SIG_TYPE_OFFSET);
+    if (type != (uint32_t) MBEDTLS_LMOTS_SHA256_N32_W8) {
+        return MBEDTLS_ERR_LMS_BAD_INPUT_DATA;
+    }
+    ctx->params.type = (mbedtls_lmots_algorithm_type_t) type;
```

### 5. `create_merkle_leaf_value` in `library/lms.c`

```diff
+    /* Always zeroize the output buffer because it may contain data from the previous invocation */
+    memset(out, 0, MBEDTLS_LMS_M_NODE_BYTES(params->type));
+
```

### 6. `mbedtls_lms_import_public_key` in `library/lms.c`

```diff
-    mbedtls_lms_algorithm_type_t type;
-    mbedtls_lmots_algorithm_type_t otstype;
+    if (key_size < 4) {
+        return MBEDTLS_ERR_LMS_BAD_INPUT_DATA;
+    }
-    type = (mbedtls_lms_algorithm_type_t) MBEDTLS_GET_UINT32_BE(key, PUBLIC_KEY_TYPE_OFFSET);
-    if (type != MBEDTLS_LMS_SHA256_M32_H10) {
+    uint32_t type = MBEDTLS_GET_UINT32_BE(key, PUBLIC_KEY_TYPE_OFFSET);
+    if (type != (uint32_t) MBEDTLS_LMS_SHA256_M32_H10) {
-    ctx->params.type = type;
+    ctx->params.type = (mbedtls_lms_algorithm_type_t) type;
-    otstype = (mbedtls_lmots_algorithm_type_t)
... truncated 6 additional diff lines ...
```

### 7. `mbedtls_lms_verify` in `library/lms.c`

```diff
-    create_merkle_leaf_value(
+    ret = create_merkle_leaf_value(
+    if (ret != 0) {
+        return MBEDTLS_ERR_LMS_VERIFY_FAILED;
+    }
+
-        create_merkle_internal_value(&ctx->params, left_node, right_node,
-                                     parent_node_id, Tc_candidate_root_node);
-
+        ret = create_merkle_internal_value(&ctx->params, left_node, right_node,
+                                           parent_node_id, Tc_candidate_root_node);
+        if (ret != 0) {
... truncated 2 additional diff lines ...
```

### 8. `pem_check_pkcs_padding` in `library/pem.c`

```diff
-    /* input_len > 0 is guaranteed by mbedtls_pem_read_buffer(). */
+    /* input_len > 0 is not guaranteed by mbedtls_pem_read_buffer(). */
+    if (input_len < 1) {
+        return MBEDTLS_ERR_PEM_INVALID_DATA;
+    }
```

### 9. `ssl_write_hostname_ext` in `library/ssl_client.c`

```diff
+    const char *hostname = mbedtls_ssl_get_hostname_pointer(ssl);
-    if (ssl->hostname == NULL) {
+    if (hostname == NULL) {
-                           ssl->hostname));
+                           hostname));
-    hostname_len = strlen(ssl->hostname);
+    hostname_len = strlen(hostname);
-    memcpy(p, ssl->hostname, hostname_len);
+    memcpy(p, hostname, hostname_len);
```

### 10. `ssl_prepare_client_hello` in `library/ssl_client.c`

```diff
+    const char *context_hostname = mbedtls_ssl_get_hostname_pointer(ssl);
-        int hostname_mismatch = ssl->hostname != NULL ||
+        int hostname_mismatch = context_hostname != NULL ||
-        if (ssl->hostname != NULL && session_negotiate->hostname != NULL) {
+        if (context_hostname != NULL && session_negotiate->hostname != NULL) {
-                ssl->hostname, session_negotiate->hostname) != 0;
+                context_hostname, session_negotiate->hostname) != 0;
-                                                ssl->hostname);
+                                                context_hostname);
```

### 11. `mbedtls_ssl_has_set_hostname_been_called` in `library/ssl_tls.c`

```diff
+static int mbedtls_ssl_has_set_hostname_been_called(
+    const mbedtls_ssl_context *ssl)
+{
+    return ssl->hostname != NULL;
+}
```

### 12. `mbedtls_ssl_get_hostname_pointer` in `library/ssl_tls.c`

```diff
+const char *mbedtls_ssl_get_hostname_pointer(const mbedtls_ssl_context *ssl)
+{
+    if (ssl->hostname == ssl_hostname_skip_cn_verification) {
+        return NULL;
+    }
+    return ssl->hostname;
+}
```

### 13. `mbedtls_ssl_free_hostname` in `library/ssl_tls.c`

```diff
+static void mbedtls_ssl_free_hostname(mbedtls_ssl_context *ssl)
+{
+    if (ssl->hostname != NULL &&
+        ssl->hostname != ssl_hostname_skip_cn_verification) {
+        mbedtls_zeroize_and_free(ssl->hostname, strlen(ssl->hostname));
+    }
+    ssl->hostname = NULL;
+}
```

### 14. `mbedtls_ssl_set_hostname` in `library/ssl_tls.c`

```diff
+    mbedtls_ssl_free_hostname(ssl);
+        /* Passing NULL as hostname clears the old one, but leaves a
+         * special marker to indicate that mbedtls_ssl_set_hostname()
+         * has been called. */
+        /* ssl->hostname should be const, but isn't. We won't actually
+         * write to the buffer, so it's ok to cast away the const. */
+        ssl->hostname = (char *) ssl_hostname_skip_cn_verification;
+            /* mbedtls_ssl_set_hostname() has been called, but unsuccessfully.
+             * Leave ssl->hostname in the same state as if the function had
+             * not been called, i.e. a null pointer. */
```

### 15. `mbedtls_ssl_free` in `library/ssl_tls.c`

```diff
-    if (ssl->hostname != NULL) {
-        mbedtls_zeroize_and_free(ssl->hostname, strlen(ssl->hostname));
-    }
+    mbedtls_ssl_free_hostname(ssl);
```

### 16. `get_hostname_for_verification` in `library/ssl_tls.c`

```diff
+static int get_hostname_for_verification(mbedtls_ssl_context *ssl,
+                                         const char **hostname)
+{
+    if (!mbedtls_ssl_has_set_hostname_been_called(ssl)) {
+        MBEDTLS_SSL_DEBUG_MSG(1, ("Certificate verification without having set hostname"));
+#if !defined(MBEDTLS_SSL_CLI_ALLOW_WEAK_CERTIFICATE_VERIFICATION_WITHOUT_HOSTNAME)
+        if (mbedtls_ssl_conf_get_endpoint(ssl->conf) == MBEDTLS_SSL_IS_CLIENT &&
+            ssl->conf->authmode == MBEDTLS_SSL_VERIFY_REQUIRED) {
+            return MBEDTLS_ERR_SSL_CERTIFICATE_VERIFICATION_WITHOUT_HOSTNAME;
+        }
+#endif
+    }
... truncated 8 additional diff lines ...
```

### 17. `mbedtls_ssl_verify_certificate` in `library/ssl_tls.c`

```diff
+    const char *hostname = "";
+    int ret = get_hostname_for_verification(ssl, &hostname);
+    if (ret != 0) {
+        MBEDTLS_SSL_DEBUG_RET(1, "get_hostname_for_verification", ret);
+        return ret;
+    }
+
+            hostname,
+            hostname,
```

### 18. `mbedtls_x509_string_to_names` in `library/x509_create.c`

```diff
-    /* Clear existing chain if present */
-    mbedtls_asn1_free_named_data_list(head);
+    /* Ensure the output parameter is not already populated.
+     * (If it were, overwriting it would likely cause a memory leak.)
+     */
+    if (*head != NULL) {
+        return MBEDTLS_ERR_X509_BAD_INPUT_DATA;
+    }
```

### 19. `mbedtls_x509write_crt_set_subject_name` in `library/x509write_crt.c`

```diff
+    mbedtls_asn1_free_named_data_list(&ctx->subject);
```

### 20. `mbedtls_x509write_crt_set_issuer_name` in `library/x509write_crt.c`

```diff
+    mbedtls_asn1_free_named_data_list(&ctx->issuer);
```

### 21. `mbedtls_x509write_csr_set_subject_name` in `library/x509write_csr.c`

```diff
+    mbedtls_asn1_free_named_data_list(&ctx->subject);
```

### 22. `main` in `programs/x509/cert_req.c`

```diff
-    mbedtls_asn1_named_data *ext_san_dirname = NULL;
-                    if ((ret = mbedtls_x509_string_to_names(&ext_san_dirname,
+                    /* Work around an API mismatch between string_to names() and
+                     * mbedtls_x509_subject_alternative_name, which holds an
+                     * actual mbedtls_x509_name while a pointer to one would be
+                     * more convenient here. (Note mbedtls_x509_name and
+                     * mbedtls_ans1_named_data are synonymous, again
+                     * string_to_names () uses one while
+                     * cur->node.san.directory_name is nominally the other.) */
+                    mbedtls_asn1_named_data *tmp_san_dirname = NULL;
+                    if ((ret = mbedtls_x509_string_to_names(&tmp_san_dirname,
-                    cur->node.san.directory_name = *ext_san_dirname;
... truncated 20 additional diff lines ...
```

### 23. `main` in `programs/x509/cert_write.c`

```diff
-    mbedtls_asn1_named_data *ext_san_dirname = NULL;
-                    if ((ret = mbedtls_x509_string_to_names(&ext_san_dirname,
+                    cur->node.type = MBEDTLS_X509_SAN_DIRECTORY_NAME;
+                    /* Work around an API mismatch between string_to names() and
+                     * mbedtls_x509_subject_alternative_name, which holds an
+                     * actual mbedtls_x509_name while a pointer to one would be
+                     * more convenient here. (Note mbedtls_x509_name and
+                     * mbedtls_ans1_named_data are synonymous, again
+                     * string_to_names () uses one while
+                     * cur->node.san.directory_name is nominally the other.) */
+                    mbedtls_asn1_named_data *tmp_san_dirname = NULL;
+                    if ((ret = mbedtls_x509_string_to_names(&tmp_san_dirname,
... truncated 21 additional diff lines ...
```

## Mock Release-Note Drafts

1. [Features] Add the get_hostname_for_verification routine: Added the get_hostname_for_verification routine.
2. [Features] Add the mbedtls_ssl_free_hostname routine: Added the mbedtls_ssl_free_hostname routine.
3. [Features] Add the mbedtls_ssl_get_hostname_pointer routine: Added the mbedtls_ssl_get_hostname_pointer routine.
4. [Features] Add the mbedtls_ssl_has_set_hostname_been_called routine: Added the mbedtls_ssl_has_set_hostname_been_called routine.
5. [Internal] Update the create_merkle_leaf_value routine: Updated the create_merkle_leaf_value routine.
6. [Internal] Update the main routine: Updated the main routine.
7. [Internal] Update the mbedtls_aesni_has_support routine: Updated the mbedtls_aesni_has_support routine.
8. [Internal] Update the mbedtls_asn1_store_named_data routine: Updated the mbedtls_asn1_store_named_data routine.
9. [Internal] Update the mbedtls_asn1_write_raw_buffer routine: Updated the mbedtls_asn1_write_raw_buffer routine.
10. [Internal] Update the mbedtls_lmots_import_public_key routine: Updated the mbedtls_lmots_import_public_key routine.
11. [Internal] Update the mbedtls_lms_import_public_key routine: Updated the mbedtls_lms_import_public_key routine.
12. [Internal] Update the mbedtls_lms_verify routine: Updated the mbedtls_lms_verify routine.
13. [Internal] Update the mbedtls_ssl_free routine: Updated the mbedtls_ssl_free routine.
14. [Internal] Update the mbedtls_ssl_set_hostname routine: Updated the mbedtls_ssl_set_hostname routine.
15. [Internal] Update the mbedtls_ssl_verify_certificate routine: Updated the mbedtls_ssl_verify_certificate routine.
16. [Internal] Update the mbedtls_x509_string_to_names routine: Updated the mbedtls_x509_string_to_names routine.
17. [Internal] Update the mbedtls_x509write_crt_set_issuer_name routine: Updated the mbedtls_x509write_crt_set_issuer_name routine.
18. [Internal] Update the mbedtls_x509write_crt_set_subject_name routine: Updated the mbedtls_x509write_crt_set_subject_name routine.
19. [Internal] Update the mbedtls_x509write_csr_set_subject_name routine: Updated the mbedtls_x509write_csr_set_subject_name routine.
20. [Internal] Update the pem_check_pkcs_padding routine: Updated the pem_check_pkcs_padding routine.
21. [Internal] Update the ssl_prepare_client_hello routine: Updated the ssl_prepare_client_hello routine.
22. [Internal] Update the ssl_write_hostname_ext routine: Updated the ssl_write_hostname_ext routine.

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

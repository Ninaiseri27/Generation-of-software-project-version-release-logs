# Evidence Pack: third_party_curl OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `curl_v6_0_to_v6_0_0_1`
- Repository: `third_party_curl`
- Category: `network`
- Reference version: `OpenHarmony-v6.0-Release`
- Target version: `OpenHarmony-v6.0.0.1-Release`
- Pipeline status: `verified_full_pipeline_mock`
- Ground-truth status: `draft_required`

## Evidence Sources To Inspect

- [ ] commit_messages
- [ ] function_level_diff
- [ ] curl upstream changelog if matching changes are identifiable
- [ ] OpenHarmony release notes if available

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/changed_functions.json`
- cmg: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/cmg.json`
- prompt_input: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/prompt_input.json`
- prompt_bundle: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/prompt_bundle.json`
- mock_release_note: `outputs/benchmark/third_party_curl/OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release/release_note.json`

## Pipeline Summary

- Commit count: `7`
- Changed C/C++ files: `17`
- Changed functions: `47`
- Patch only: `False`
- CMG matched entries: `27`
- CMG unmatched entries: `20`
- Fallback-context entries: `47`
- Diff-derived call edges: `103`
- Prompt entries: `47`
- Mock generated entries: `47`

## Commit Messages

- !348 merge OpenHarmony-6.0-Release into OpenHarmony-6.0-Release
- update cacert.pem
- merge OpenHarmony-6.0-Release into OpenHarmony-6.0-Release
- fix CVE-2025-9086
- !333 support gmssl 6.0 release Merge pull request !333 from pjie131/OpenHarmony-6.0-Release
- gmssl fix
- support gmssl

## Changed C/C++ Files

- `include/curl/curl.h`
- `include/curl/typecheck-gcc.h`
- `lib/cookie.c`
- `lib/curl_setup.h`
- `lib/easy.c`
- `lib/easyoptions.c`
- `lib/setopt.c`
- `lib/urldata.h`
- `lib/vtls/openssl.c`
- `lib/vtls/openssl.h`
- `lib/vtls/vtls.c`
- `lib/vtls/vtls.h`
- `packages/OS400/ccsidcurl.c`
- `src/tool_cfgable.h`
- `src/tool_getparam.c`
- `src/tool_listhelp.c`
- `src/tool_operate.c`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `sanitize_cookie_path` | `modified` | `lib/cookie.c` | `294-324` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 2 | `Curl_cookie_add` | `modified` | `lib/cookie.c` | `482-1189` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 3 | `easy_perform` | `modified` | `lib/easy.c` | `717-782` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 4 | `Curl_vsetopt` | `modified` | `lib/setopt.c` | `187-3216` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 5 | `hitls_init` | `added` | `lib/vtls/openssl.c` | `57-77` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 6 | `BuildCertStoreFromList` | `added` | `lib/vtls/openssl.c` | `79-106` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 7 | `SetCertListToChainStore` | `added` | `lib/vtls/openssl.c` | `108-125` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 8 | `SetCertListToCertStore` | `added` | `lib/vtls/openssl.c` | `127-144` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `ParseAndSetCACertificate` | `added` | `lib/vtls/openssl.c` | `146-185` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 10 | `LoadCertListAndCert` | `added` | `lib/vtls/openssl.c` | `187-222` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 11 | `ParseFilePriKey` | `added` | `lib/vtls/openssl.c` | `224-243` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 12 | `ParseAndSetCertificate` | `added` | `lib/vtls/openssl.c` | `245-285` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `ParseAndSetPrivateKey` | `added` | `lib/vtls/openssl.c` | `287-320` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 14 | `hitls_connect_nonblocking_step1` | `added` | `lib/vtls/openssl.c` | `322-352` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 15 | `hitls_connect_nonblocking_step2` | `added` | `lib/vtls/openssl.c` | `354-396` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 16 | `hitls_connect_nonblocking_step3` | `added` | `lib/vtls/openssl.c` | `398-436` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 17 | `hitls_connect_nonblocking` | `added` | `lib/vtls/openssl.c` | `438-474` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 18 | `hitls_recv` | `added` | `lib/vtls/openssl.c` | `476-496` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 19 | `hitls_send` | `added` | `lib/vtls/openssl.c` | `498-516` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 20 | `hitls_connect` | `added` | `lib/vtls/openssl.c` | `518-521` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 21 | `hitls_version` | `added` | `lib/vtls/openssl.c` | `523-526` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `hitls_get_internals` | `added` | `lib/vtls/openssl.c` | `528-531` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 23 | `hitls_close` | `added` | `lib/vtls/openssl.c` | `533-545` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 24 | `ossl_init` | `modified` | `lib/vtls/openssl.c` | `2248-2299` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 25 | `ossl_cleanup` | `modified` | `lib/vtls/openssl.c` | `2302-2339` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 26 | `ossl_set_engine` | `modified` | `lib/vtls/openssl.c` | `2343-2390` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 27 | `ossl_set_engine_default` | `modified` | `lib/vtls/openssl.c` | `2394-2417` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 28 | `ossl_engines_list` | `modified` | `lib/vtls/openssl.c` | `2421-2444` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 29 | `ossl_close` | `modified` | `lib/vtls/openssl.c` | `2446-2540` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 30 | `ossl_shutdown` | `modified` | `lib/vtls/openssl.c` | `2546-2653` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 31 | `ossl_close_all` | `modified` | `lib/vtls/openssl.c` | `2666-2690` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 32 | `ossl_connect_common` | `modified` | `lib/vtls/openssl.c` | `5358-5464` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 33 | `ossl_connect_nonblocking` | `modified` | `lib/vtls/openssl.c` | `5466-5488` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 34 | `ossl_connect` | `modified` | `lib/vtls/openssl.c` | `5490-5508` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 35 | `ossl_data_pending` | `modified` | `lib/vtls/openssl.c` | `5510-5526` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 36 | `ossl_send` | `modified` | `lib/vtls/openssl.c` | `5528-5624` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 37 | `ossl_recv` | `modified` | `lib/vtls/openssl.c` | `5626-5734` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 38 | `ossl_random` | `modified` | `lib/vtls/openssl.c` | `5817-5837` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 39 | `ossl_sha256sum` | `modified` | `lib/vtls/openssl.c` | `5840-5861` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 40 | `ossl_get_internals` | `modified` | `lib/vtls/openssl.c` | `5874-5883` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 41 | `ossl_free_multi_ssl_backend_data` | `modified` | `lib/vtls/openssl.c` | `5885-5898` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 42 | `clone_ssl_primary_config` | `modified` | `lib/vtls/vtls.c` | `223-253` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 43 | `Curl_free_primary_ssl_config` | `modified` | `lib/vtls/vtls.c` | `255-274` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 44 | `Curl_ssl_easy_config_complete` | `modified` | `lib/vtls/vtls.c` | `276-338` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 45 | `curl_easy_setopt_ccsid` | `modified` | `packages/OS400/ccsidcurl.c` | `1066-1298` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 46 | `getparameter` | `modified` | `src/tool_getparam.c` | `1221-2830` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 47 | `single_transfer` | `modified` | `src/tool_operate.c` | `736-2251` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `sanitize_cookie_path` in `lib/cookie.c`

```diff
-  if(len && new_path[len - 1] == '/') {
+  if(len > 1 && new_path[len - 1] == '/') {
```

### 2. `Curl_cookie_add` in `lib/cookie.c`

```diff
-        const char *sep;
+        const char *sep = NULL;
-        sep = strchr(clist->spath + 1, '/');
-
+        DEBUGASSERT(clist->spath[0]);
+        if(clist->spath[0])
+          sep = strchr(clist->spath + 1, '/');
```

### 3. `easy_perform` in `lib/easy.c`

```diff
+#if defined(USE_OPENHITLS)
+    multi->conn_cache.closure_handle->set.ssl.primary.version = data->set.ssl.primary.version;
+#endif
```

### 4. `Curl_vsetopt` in `lib/setopt.c`

```diff
+    case CURLOPT_SSLENCCERT:
+    /*
+     * String that holds file name of the SSL certificate to use
+     */
+    result = Curl_setstropt(&data->set.str[STRING_ENCCERT],
+                            va_arg(param, char *));
+    break;
+    case CURLOPT_SSLENCKEY:
+    /*
+     * String that holds file name of the SSL key to use
+     */
+    result = Curl_setstropt(&data->set.str[STRING_ENCKEY],
+                            va_arg(param, char *));
+    break;
```

### 5. `hitls_init` in `lib/vtls/openssl.c`

```diff
+static int hitls_init(void)
+{
+    int32_t ret = BSL_GLOBAL_Init();
+    if (ret != BSL_SUCCESS) {
+        return FALSE;
+    }
+    ret = CRYPT_EAL_Init(CRYPT_EAL_INIT_CPU | CRYPT_EAL_INIT_PROVIDER);
+    if (ret != CRYPT_SUCCESS) {
+        return FALSE;
+    }
+    ret = CRYPT_EAL_RandInit(CRYPT_RAND_SHA256, NULL, NULL, NULL, 0);
+    if (ret != CRYPT_SUCCESS && ret != CRYPT_EAL_ERR_DRBG_REPEAT_INIT) {
+        return FALSE;
+    }
+    ret = HITLS_CertMethodInit();
+    if (ret != HITLS_SUCCESS) {
... truncated 5 additional diff lines ...
```

### 6. `BuildCertStoreFromList` in `lib/vtls/openssl.c`

```diff
+static HITLS_CERT_Store *BuildCertStoreFromList(BslList *certList, struct Curl_easy *data)
+{
+    int32_t ret = 0;
+    HITLS_CERT_Store *x509Store = NULL;
+    HITLS_X509_Cert *cert = NULL;
+
+    x509Store = HITLS_X509_StoreCtxNew();
+    if (x509Store == NULL) {
+        failf(data, "HITLS_X509_StoreCtxNew failed.");
+        goto exit;
+    }
+
+    cert = BSL_LIST_GET_FIRST(certList);
+    while (cert != NULL) {
+        ret = HITLS_X509_StoreCtxCtrl(x509Store, HITLS_X509_STORECTX_DEEP_COPY_SET_CA, cert, 0);
+        if (ret != HITLS_SUCCESS) {
... truncated 12 additional diff lines ...
```

### 7. `SetCertListToChainStore` in `lib/vtls/openssl.c`

```diff
+static int SetCertListToChainStore(HITLS_Config *config, BslList *certList, struct Curl_easy *data)
+{
+    HITLS_CERT_Store *chainStore = BuildCertStoreFromList(certList, data);
+    if (chainStore == NULL) {
+        failf(data, "Failed to build chain store from list.");
+        goto exit;
+    }
+
+    if (HITLS_CFG_SetChainStore(config, chainStore, false) != HITLS_SUCCESS) {
+        failf(data, "Failed to set chain store.");
+        goto exit;
+    }
+
+    return CURLE_OK;
+exit:
+    HITLS_X509_StoreCtxFree(chainStore);
... truncated 2 additional diff lines ...
```

### 8. `SetCertListToCertStore` in `lib/vtls/openssl.c`

```diff
+static int SetCertListToCertStore(HITLS_Config *config, BslList *certList, struct Curl_easy *data)
+{
+    HITLS_CERT_Store *certStore = BuildCertStoreFromList(certList, data);
+    if (certStore == NULL) {
+        failf(data, "Failed to build cert store from list.");
+        goto exit;
+    }
+
+    if (HITLS_CFG_SetCertStore(config, certStore, false) != HITLS_SUCCESS) {
+        failf(data, "Failed to set cert store.");
+        goto exit;
+    }
+
+    return CURLE_OK;
+exit:
+    HITLS_X509_StoreCtxFree(certStore);
... truncated 2 additional diff lines ...
```

### 9. `ParseAndSetCACertificate` in `lib/vtls/openssl.c`

```diff
+static int32_t ParseAndSetCACertificate(HITLS_Config *config, const char *caFile, uint32_t depth,
+                                        struct Curl_easy *data)
+{
+    BslList *certList = NULL;
+    if (caFile == NULL) {
+        failf(data, "caFile is NULL.");
+        return CURLE_OK;
+    }
+
+    int32_t ret = HITLS_CFG_SetVerifyDepth(config, depth);
+    if (ret != HITLS_SUCCESS) {
+        failf(data, "HITLS_CFG_SetVerifyDepth failed.");
+        goto exit;
+    }
+
+    ret = HITLS_X509_CertParseBundleFile(BSL_FORMAT_PEM, caFile, &certList);
... truncated 24 additional diff lines ...
```

### 10. `LoadCertListAndCert` in `lib/vtls/openssl.c`

```diff
+static HITLS_X509_Cert *LoadCertListAndCert(const char *certFile, BslList **certList, const char *certName,
+                                            struct Curl_easy *data)
+{
+    HITLS_X509_Cert *cert = NULL;
+    BslListNode *detachNode = NULL;
+    if (certFile == NULL) {
+        failf(data, "certFile is NULL.");
+        return NULL;
+    }
+
+    if (HITLS_X509_CertParseBundleFile(BSL_FORMAT_PEM, certFile, certList) != HITLS_PKI_SUCCESS) {
+        failf(data, "Error parsing certificate: %s.", certName);
+        goto exit;
+    }
+
+    if (*certList == NULL || BSL_LIST_COUNT(*certList) == 0) {
... truncated 20 additional diff lines ...
```

### 11. `ParseFilePriKey` in `lib/vtls/openssl.c`

```diff
+static CRYPT_EAL_PkeyCtx *ParseFilePriKey(const char *path, uint8_t *pwd, uint32_t pwdlen, struct Curl_easy *data)
+{
+    static int32_t tryTypes[] = {CRYPT_PRIKEY_PKCS8_UNENCRYPT, CRYPT_PRIKEY_PKCS8_ENCRYPT, CRYPT_PRIKEY_RSA,
+                                 CRYPT_PRIKEY_ECC};
+    CRYPT_EAL_PkeyCtx *ealPriKey = NULL;
+    uint32_t i = 0;
+    if (path == NULL) {
+        failf(data, "path is NULL.");
+        return NULL;
+    }
+    for (; i < sizeof(tryTypes) / sizeof(tryTypes[0]); i++) {
+        if (CRYPT_EAL_DecodeFileKey(BSL_FORMAT_PEM, tryTypes[i], path, pwd, pwdlen, &ealPriKey) == HITLS_SUCCESS) {
+            return ealPriKey;
+        }
+    }
+
... truncated 4 additional diff lines ...
```

### 12. `ParseAndSetCertificate` in `lib/vtls/openssl.c`

```diff
+static int32_t ParseAndSetCertificate(const char *certFile, HITLS_Config *config, bool isEncryption,
+                                      const char *certName, const long int sslVersion, struct Curl_easy *data)
+{
+    int32_t ret = 0;
+    BslList *certList = NULL;
+    HITLS_X509_Cert *cert = NULL;
+    if (certFile == NULL) {
+        failf(data, "certFile is NULL.");
+        return CURLE_OK;
+    }
+
+    cert = LoadCertListAndCert(certFile, &certList, certName, data);
+    if (cert == NULL) {
+        failf(data, "LoadCertListAndCert failed: %s.", certName);
+        goto exit;
+    }
... truncated 25 additional diff lines ...
```

### 13. `ParseAndSetPrivateKey` in `lib/vtls/openssl.c`

```diff
+static int32_t ParseAndSetPrivateKey(const char *keyFile, HITLS_Config *config, bool isEncryption, const char *keyName,
+                                     const long int sslVersion, struct Curl_easy *data)
+{
+    int32_t ret = 0;
+    CRYPT_EAL_PkeyCtx *certKey = NULL;
+    if (keyFile == NULL) {
+        failf(data, "keyFile is NULL.");
+        return CURLE_OK;
+    }
+    certKey = ParseFilePriKey(keyFile, NULL, 0, data);
+    if (certKey == NULL) {
+        failf(data, "Error parsing private key: %s.", keyName);
+        goto exit;
+    }
+    if (sslVersion == CURL_SSLVERSION_TLCPv1_1) { /* TLCP */
+        ret = HITLS_CFG_SetTlcpPrivateKey(config, (HITLS_CERT_Key *)certKey, false, isEncryption);
... truncated 18 additional diff lines ...
```

### 14. `hitls_connect_nonblocking_step1` in `lib/vtls/openssl.c`

```diff
+static CURLcode hitls_connect_nonblocking_step1(struct hitls_ssl_backend_data *backend, struct Curl_cfilter *cf,
+    struct Curl_easy *data)
+{
+    int32_t ret = 0;
+    struct ssl_config_data *sslConfig = Curl_ssl_cf_get_config(cf, data);
+    const long int sslVersion = sslConfig->primary.version;
+    if (sslVersion != CURL_SSLVERSION_TLCPv1_1) {
+        failf(data, "Unrecognized parameter passed via CURLOPT_SSLVERSION in hitls.");
+        return CURLE_NOT_BUILT_IN;
+    }
+    if (backend && backend->ctx == NULL) {
+        backend->config = HITLS_CFG_NewTLCPConfig();
+        if (backend->config == NULL) {
+            failf(data, "HITLS_CFG_NewTLCPConfig failed.");
+            return CURLE_SSL_CONNECT_ERROR;
+        }
... truncated 15 additional diff lines ...
```

### 15. `hitls_connect_nonblocking_step2` in `lib/vtls/openssl.c`

```diff
+static CURLcode hitls_connect_nonblocking_step2(struct hitls_ssl_backend_data *backend, struct Curl_cfilter *cf,
+    struct Curl_easy *data)
+{
+    int32_t ret = 0;
+    struct ssl_config_data *sslConfig = Curl_ssl_cf_get_config(cf, data);
+    char *const sslCafile = sslConfig->primary.CAfile;
+    char *const sslSignCert = sslConfig->primary.clientcert;
+    char *const sslEncCert = sslConfig->primary.clientcertEnc;
+    char *const sslSignKey = sslConfig->key;
+    char *const sslEncKey = sslConfig->encKey;
+    const long int sslVersion = sslConfig->primary.version;
+    uint32_t depth = 20;
+    if (backend && backend->config != NULL) {
+        ret = ParseAndSetCACertificate(backend->config, sslCafile, depth, data);
+        if (ret != CURLE_OK) {
+            failf(data, "Some problems were encountered when processing CA Certificate.");
... truncated 27 additional diff lines ...
```

### 16. `hitls_connect_nonblocking_step3` in `lib/vtls/openssl.c`

```diff
+static CURLcode hitls_connect_nonblocking_step3(struct hitls_ssl_backend_data *backend, struct Curl_cfilter *cf,
+    struct Curl_easy *data)
+{
+    int32_t ret = 0;
+    BSL_UIO *uio = NULL;
+    curl_socket_t sockfd;
+    if (backend && backend->config != NULL) {
+        backend->ctx = HITLS_New(backend->config);
+        if (backend->ctx == NULL) {
+            failf(data, "HITLS_New failed.");
+            return CURLE_SSL_CONNECT_ERROR;
+        }
+        sockfd = Curl_conn_cf_get_socket(cf, data);
+        if (sockfd < 0) {
+            failf(data, "TCP_Connect failed.");
+            return CURLE_SSL_CONNECT_ERROR;
... truncated 23 additional diff lines ...
```

### 17. `hitls_connect_nonblocking` in `lib/vtls/openssl.c`

```diff
+static CURLcode hitls_connect_nonblocking(struct Curl_cfilter *cf, struct Curl_easy *data, bool *done)
+{
+    int32_t ret = 0;
+    struct ssl_connect_data *connssl = cf->ctx;
+    struct hitls_ssl_backend_data *backend = (struct hitls_ssl_backend_data *)connssl->backend;
+    if (hitls_connect_nonblocking_step1(backend, cf, data) != CURLE_OK) {
+        goto exit;
+    }
+    if (hitls_connect_nonblocking_step2(backend, cf, data) != CURLE_OK) {
+        goto exit;
+    }
+    if (hitls_connect_nonblocking_step3(backend, cf, data) != CURLE_OK) {
+        goto exit;
+    }
+    do {
+        ret = HITLS_Connect(backend->ctx);
... truncated 21 additional diff lines ...
```

### 18. `hitls_recv` in `lib/vtls/openssl.c`

```diff
+static ssize_t hitls_recv(struct Curl_cfilter *cf, struct Curl_easy *data, char *buf, size_t bufferSize,
+                          CURLcode *curlCode)
+{
+    int ret = 0;
+    unsigned int readLen = 0;
+
+    struct ssl_connect_data *connssl = cf->ctx;
+    struct hitls_ssl_backend_data *backend = (struct hitls_ssl_backend_data *)connssl->backend;
+
+    ret = HITLS_Read(backend->ctx, buf, bufferSize, &readLen);
+    if (ret == HITLS_SUCCESS) {
+        buf[readLen] = '\0'; // Ensure null-termination
+        return readLen;
+    } else if (ret == HITLS_REC_NORMAL_RECV_BUF_EMPTY || ret == HITLS_REC_NORMAL_IO_BUSY) {
+        *curlCode = CURLE_AGAIN;
+    } else {
... truncated 5 additional diff lines ...
```

### 19. `hitls_send` in `lib/vtls/openssl.c`

```diff
+static ssize_t hitls_send(struct Curl_cfilter *cf, struct Curl_easy *data, const void *mem, size_t len,
+                          CURLcode *curlCode)
+{
+    int ret = 0;
+    uint32_t writeLen = 0;
+    struct ssl_connect_data *connssl = cf->ctx;
+    struct hitls_ssl_backend_data *backend = (struct hitls_ssl_backend_data *)connssl->backend;
+
+    ret = HITLS_Write(backend->ctx, mem, len, &writeLen);
+    if (ret == HITLS_SUCCESS) {
+        return writeLen;
+    } else if (ret == HITLS_REC_NORMAL_RECV_BUF_EMPTY || ret == HITLS_REC_NORMAL_IO_BUSY) {
+        *curlCode = CURLE_AGAIN;
+    } else {
+        *curlCode = CURLE_RECV_ERROR;
+    }
... truncated 3 additional diff lines ...
```

### 20. `hitls_connect` in `lib/vtls/openssl.c`

```diff
+static CURLcode hitls_connect(struct Curl_cfilter *cf, struct Curl_easy *data)
+{
+    return CURLE_NOT_BUILT_IN;
+}
```

### 21. `hitls_version` in `lib/vtls/openssl.c`

```diff
+static size_t hitls_version(char *buffer, size_t size)
+{
+    return msnprintf(buffer, size, "TLCP1.1");
+}
```

### 22. `hitls_get_internals` in `lib/vtls/openssl.c`

```diff
+static void *hitls_get_internals(struct ssl_connect_data *connssl, CURLINFO info)
+{
+    return NULL;
+}
```

### 23. `hitls_close` in `lib/vtls/openssl.c`

```diff
+static void hitls_close(struct Curl_cfilter *cf, struct Curl_easy *data)
+{
+    struct ssl_connect_data *connssl = cf->ctx;
+    struct hitls_ssl_backend_data *backend = (struct hitls_ssl_backend_data *)connssl->backend;
+
+    if (backend != NULL) {
+        HITLS_Close(backend->ctx);
+        HITLS_Free(backend->ctx);
+        backend->ctx = NULL;
+        HITLS_CFG_FreeConfig(backend->config);
+        backend->config = NULL;
+    }
+}
```

### 24. `ossl_init` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    Curl_ssl_hitls.init();
+#endif
```

### 25. `ossl_cleanup` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    Curl_ssl_hitls.cleanup();
+#endif
```

### 26. `ossl_set_engine` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return CURLE_NOT_BUILT_IN;
+    }
+#endif
+
```

### 27. `ossl_set_engine_default` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return CURLE_NOT_BUILT_IN;
+    }
+#endif
```

### 28. `ossl_engines_list` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return NULL;
+    }
+#endif
```

### 29. `ossl_close` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return Curl_ssl_hitls.close(cf, data);
+    }
+#endif
```

### 30. `ossl_shutdown` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return 0;
+    }
+#endif
```

### 31. `ossl_close_all` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return;
+    }
+#endif
```

### 32. `ossl_connect_common` in `lib/vtls/openssl.c`

```diff
+
```

### 33. `ossl_connect_nonblocking` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        CURLcode result = Curl_ssl_hitls.connect_nonblocking(cf, data, done);
+        if (result == CURLE_OK) {
+            struct ssl_connect_data *connssl = cf->ctx;
+            connssl->state = ssl_connection_complete;
+            if (done) {
+                *done = TRUE;
+            }
+        } else {
+            if (done) {
+                *done = FALSE;
+            }
+        }
+        return result;
+    }
... truncated 1 additional diff lines ...
```

### 34. `ossl_connect` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return CURLE_NOT_BUILT_IN;
+    }
+#endif
```

### 35. `ossl_data_pending` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return 0;
+    }
+#endif
```

### 36. `ossl_send` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return Curl_ssl_hitls.send_plain(cf, data, mem, len, curlcode);
+    }
+#endif
```

### 37. `ossl_recv` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return Curl_ssl_hitls.recv_plain(cf, data, buf, buffersize, curlcode);
+    }
+#endif
```

### 38. `ossl_random` in `lib/vtls/openssl.c`

```diff
+#if defined(USE_OPENHITLS)
+    if (data->set.ssl.primary.version == CURL_SSLVERSION_TLCPv1_1) {
+        return CURLE_NOT_BUILT_IN;
+    }
+#endif
```

### 39. `ossl_sha256sum` in `lib/vtls/openssl.c`

```diff
+  //todo for hitls
```

### 40. `ossl_get_internals` in `lib/vtls/openssl.c`

```diff
+  //todo openhitls return NULL
```

### 41. `ossl_free_multi_ssl_backend_data` in `lib/vtls/openssl.c`

```diff
+  // todo for hitls
```

### 42. `clone_ssl_primary_config` in `lib/vtls/vtls.c`

```diff
+  CLONE_STRING(clientcertEnc);
```

### 43. `Curl_free_primary_ssl_config` in `lib/vtls/vtls.c`

```diff
+  Curl_safefree(sslc->clientcertEnc);
```

### 44. `Curl_ssl_easy_config_complete` in `lib/vtls/vtls.c`

```diff
+  data->set.ssl.encKey = data->set.str[STRING_ENCKEY];
+  data->set.ssl.primary.clientcertEnc = data->set.str[STRING_ENCCERT];
```

### 45. `curl_easy_setopt_ccsid` in `packages/OS400/ccsidcurl.c`

```diff
+  case CURLOPT_SSLENCCERT:
+  case CURLOPT_SSLENCKEY:
```

### 46. `getparameter` in `src/tool_getparam.c`

```diff
+    case C_TLCPV1_1:
+      config->ssl_version = CURL_SSLVERSION_TLCPv1_1;
+      break;
+    case C_ENC_CERT: /* --enc-cert */
+      cleanarg(clearthis);
+      GetFileAndPassword(nextarg, &config->encCert, &config->key_passwd);
+      break;
+    case C_ENC_KEY: /* --enc-key */
+      err = getstr(&config->encKey, nextarg, DENY_BLANK);
+      break;
```

### 47. `single_transfer` in `src/tool_operate.c`

```diff
+          my_setopt_str(curl, CURLOPT_SSLENCCERT, config->encCert);
+          my_setopt_str(curl, CURLOPT_SSLENCKEY, config->encKey);
```

## Mock Release-Note Drafts

1. [Features] Add BuildCertStoreFromList: Added BuildCertStoreFromList.
2. [Features] Add LoadCertListAndCert: Added LoadCertListAndCert.
3. [Features] Add ParseAndSetCACertificate: Added ParseAndSetCACertificate.
4. [Features] Add ParseAndSetCertificate: Added ParseAndSetCertificate.
5. [Features] Add ParseAndSetPrivateKey: Added ParseAndSetPrivateKey.
6. [Features] Add ParseFilePriKey: Added ParseFilePriKey.
7. [Features] Add SetCertListToCertStore: Added SetCertListToCertStore.
8. [Features] Add SetCertListToChainStore: Added SetCertListToChainStore.
9. [Features] Add the hitls_close routine: Added the hitls_close routine.
10. [Features] Add the hitls_connect routine: Added the hitls_connect routine.
11. [Features] Add the hitls_connect_nonblocking routine: Added the hitls_connect_nonblocking routine.
12. [Features] Add the hitls_connect_nonblocking_step1 routine: Added the hitls_connect_nonblocking_step1 routine.
13. [Features] Add the hitls_connect_nonblocking_step2 routine: Added the hitls_connect_nonblocking_step2 routine.
14. [Features] Add the hitls_connect_nonblocking_step3 routine: Added the hitls_connect_nonblocking_step3 routine.
15. [Features] Add the hitls_get_internals routine: Added the hitls_get_internals routine.
16. [Features] Add the hitls_init routine: Added the hitls_init routine.
17. [Features] Add the hitls_recv routine: Added the hitls_recv routine.
18. [Features] Add the hitls_send routine: Added the hitls_send routine.
19. [Features] Add the hitls_version routine: Added the hitls_version routine.
20. [Internal] Update the Curl_cookie_add routine: Updated the Curl_cookie_add routine.
21. [Internal] Update the Curl_free_primary_ssl_config routine: Updated the Curl_free_primary_ssl_config routine.
22. [Internal] Update the Curl_ssl_easy_config_complete routine: Updated the Curl_ssl_easy_config_complete routine.
23. [Internal] Update the Curl_vsetopt routine: Updated the Curl_vsetopt routine.
24. [Internal] Update the clone_ssl_primary_config routine: Updated the clone_ssl_primary_config routine.
25. [Internal] Update the curl_easy_setopt_ccsid routine: Updated the curl_easy_setopt_ccsid routine.
26. [Internal] Update the easy_perform routine: Updated the easy_perform routine.
27. [Internal] Update the getparameter routine: Updated the getparameter routine.
28. [Internal] Update the ossl_cleanup routine: Updated the ossl_cleanup routine.
29. [Internal] Update the ossl_close routine: Updated the ossl_close routine.
30. [Internal] Update the ossl_close_all routine: Updated the ossl_close_all routine.
31. [Internal] Update the ossl_connect routine: Updated the ossl_connect routine.
32. [Internal] Update the ossl_connect_common routine: Updated the ossl_connect_common routine.
33. [Internal] Update the ossl_connect_nonblocking routine: Updated the ossl_connect_nonblocking routine.
34. [Internal] Update the ossl_data_pending routine: Updated the ossl_data_pending routine.
35. [Internal] Update the ossl_engines_list routine: Updated the ossl_engines_list routine.
36. [Internal] Update the ossl_free_multi_ssl_backend_data routine: Updated the ossl_free_multi_ssl_backend_data routine.
37. [Internal] Update the ossl_get_internals routine: Updated the ossl_get_internals routine.
38. [Internal] Update the ossl_init routine: Updated the ossl_init routine.
39. [Internal] Update the ossl_random routine: Updated the ossl_random routine.
40. [Internal] Update the ossl_recv routine: Updated the ossl_recv routine.
41. [Internal] Update the ossl_send routine: Updated the ossl_send routine.
42. [Internal] Update the ossl_set_engine routine: Updated the ossl_set_engine routine.
43. [Internal] Update the ossl_set_engine_default routine: Updated the ossl_set_engine_default routine.
44. [Internal] Update the ossl_sha256sum routine: Updated the ossl_sha256sum routine.
45. [Internal] Update the ossl_shutdown routine: Updated the ossl_shutdown routine.
46. [Internal] Update the sanitize_cookie_path routine: Updated the sanitize_cookie_path routine.
47. [Internal] Update the single_transfer routine: Updated the single_transfer routine.

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

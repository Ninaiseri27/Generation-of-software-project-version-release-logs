# Ground Truth: third_party_mbedtls OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release

Status: `reviewed`

Evidence packet:

- `benchmark/cases/third_party_mbedtls/mbedtls_v6_0_beta1_to_v6_0/evidence.md`

## Evidence Checklist

- [ ] Inspect OpenHarmony v6.0 Beta1 platform release notes.
- [ ] Inspect OpenHarmony v6.0 platform release notes.
- [x] Inspect `changed_functions.json` for changed-function inventory.
- [x] Run Stage 2/3 artifacts before final admission.
- [x] Inspect commit messages between the two tags.
- [x] Inspect mbedtls `ChangeLog.d` entries that map to the OpenHarmony component diff.

## Evidence Summary

- Pipeline status: `verified_full_pipeline_mock`.
- Changed functions: `23`.
- CMG matched entries: `6`.
- CMG unmatched entries: `17`.
- Fallback-context coverage: `23/23`.
- Current use: medium security/crypto case admitted for `core_eval`.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Security | Make TLS client certificate verification fail when certificate authentication is attempted without calling `mbedtls_ssl_set_hostname`, unless the weak-compatibility option is explicitly enabled. | Commit `Fix CVE-2025-27809`; `ChangeLog.d/mbedtls_ssl_set_hostname.txt`; changed functions `ssl_write_hostname_ext`, `ssl_prepare_client_hello`, `mbedtls_ssl_set_hostname`, `mbedtls_ssl_verify_certificate`, `get_hostname_for_verification`; diff adds `MBEDTLS_ERR_SSL_CERTIFICATE_VERIFICATION_WITHOUT_HOSTNAME`. | Security and behavior-change entry; may affect compatibility for clients that previously omitted hostname configuration. |
| GT-002 | Security | Fix X.509/ASN.1 name-list memory management bugs that could cause use-after-free, double-free, or NULL dereference when creating certificates, CSRs, or CRLs. | Commit `fix bug CVE-2025-47917 CVE-2025-48965`; `ChangeLog.d/fix-string-to-names-memory-management.txt`; `ChangeLog.d/fix-string-to-names-store-named-data.txt`; changed functions `mbedtls_asn1_store_named_data`, `mbedtls_x509_string_to_names`, `mbedtls_x509write_crt_set_subject_name`, `mbedtls_x509write_crt_set_issuer_name`, `mbedtls_x509write_csr_set_subject_name`, and x509 sample `main` functions. | High-value security entry with direct component changelog evidence. |
| GT-003 | Security | Fix LMS/LM-OTS public-key import and verification weaknesses, including short-input overread, unsafe enum-type validation, and accepting invalid signatures after Merkle/hash helper failures. | Commit `fix CVE-2025-52496,CVE-2025-52497,CVE-2025-49600,CVE-2025-49601`; `ChangeLog.d/1351_lms_overread.txt`, `1352_lms_enum_casting.txt`, `1353_lms_check_return_of_merkle_leaf.txt`; changed functions `mbedtls_lmots_import_public_key`, `mbedtls_lms_import_public_key`, `create_merkle_leaf_value`, `mbedtls_lms_verify`. | CVE group from the same security commit; keep grouped to avoid over-fragmented release notes. |
| GT-004 | Security | Fix an AESNI support-detection race on x86/amd64 that could temporarily force software AES/GCM paths in multithreaded programs and expose timing or forgery risks. | Commit `fix CVE-2025-52496,CVE-2025-52497,CVE-2025-49600,CVE-2025-49601`; `ChangeLog.d/aesni_has_support.txt`; changed function `mbedtls_aesni_has_support`. | Security impact is architecture-specific. |
| GT-005 | Security | Fix an integer underflow when parsing malformed encrypted PEM keys, preventing potential crashes or information disclosure. | Commit `fix CVE-2025-52496,CVE-2025-52497,CVE-2025-49600,CVE-2025-49601`; `ChangeLog.d/pem-integer-underflow.txt`; changed function `pem_check_pkcs_padding`. | Security parser hardening. |
| GT-006 | Fix | Avoid undefined behavior in `mbedtls_asn1_write_raw_buffer` by skipping `memcpy` when the input buffer is NULL and length is zero. | Commit `fix bug CVE-2025-47917 CVE-2025-48965`; `ChangeLog.d/fix-asnn1write-raw-buffer.txt`; changed function `mbedtls_asn1_write_raw_buffer`. | Changelog labels this as bugfix rather than security. |

## Excluded Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| `add chipsetsdk` | Build/integration addition with no inspected C/C++ function-level release-note evidence in this case. | Commit `add chipsetsdk`; no corresponding changed function evidence in `changed_functions.json`. |
| Sample-program internal restructuring | Evidence supporting GT-002, not a separate end-user release-note entry. | Changed `main` in `programs/x509/cert_req.c` and `programs/x509/cert_write.c`. |

## Reviewer Notes

- Drafted from component `ChangeLog.d` files, commit messages, and function-level diff evidence.
- This is the strongest current ground-truth case because upstream/component changelog entries directly map to changed functions.
- Second-pass review accepted the six current entries for core evaluation.

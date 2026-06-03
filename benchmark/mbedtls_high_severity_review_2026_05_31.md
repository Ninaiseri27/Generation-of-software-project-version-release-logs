# mbedTLS High-Severity Strict-Match Review 2026-05-31

This record documents the targeted review of the remaining high-severity rows in `final_strict_match_audit.md`.

## Summary

- date: `2026-05-31`
- scope: `mbedtls high-severity strict-match review`
- reviewed_rows: `7`
- kept_matches: `7`
- removed_matches: `0`
- metric_refresh_required: `false`

## Decision

All seven high-severity mbedTLS rows are retained. The audit flags are useful as thesis-review warnings, but the generated notes state the same release-note-level facts as the reviewed GT entries.

## Rationale

- `GT-001` is about failing TLS client certificate verification when hostname configuration is missing. The reviewed generated note explicitly states the no-hostname verification failure behavior and security-bypass prevention.
- `GT-002` is about X.509/ASN.1 name-list memory-management bugs that can cause use-after-free, double-free, or NULL dereference when creating certificates, CSRs, or CRLs.
- The `cert_req` and `cert_write` generated notes mention memory leak/use-after-free fixes in certificate request or certificate writing SAN directory-name handling. These are not standalone test/helper-only claims; the ground truth explicitly lists the x509 sample `main` functions as supporting evidence for `GT-002`.
- Therefore, removing these rows would undercount valid semantic coverage.

## Reviewed Rows

| Method | Generated | GT | Decision | Reason |
| --- | --- | --- | --- | --- |
| `diff_only` | `GEN-010` | `GT-002` | keep | Describes cert_req SAN memory leak/use-after-free, within GT-002 certificate/CSR memory-management scope. |
| `full_adaptive_rule_family` | `GEN-004` | `GT-001` | keep | Explicitly describes no-hostname certificate verification failure and security-bypass prevention. |
| `full_adaptive_rule_family` | `GEN-014` | `GT-002` | keep | Describes cert_write directory-name SAN memory leak/use-after-free, within GT-002 scope. |
| `full_adaptive_rule_family` | `GEN-015` | `GT-002` | keep | Describes cert_req directory-name SAN memory leak/use-after-free, within GT-002 scope. |
| `full_no_fallback` | `GEN-016` | `GT-002` | keep | Describes certificate-request directory-name memory leak/use-after-free, within GT-002 scope. |
| `full_strict_1hop` | `GEN-011` | `GT-002` | keep | Describes cert_write SAN memory leak/use-after-free, within GT-002 scope. |
| `no_graph` | `GEN-017` | `GT-002` | keep | Describes certificate request SAN memory leak/use-after-free, within GT-002 scope. |

## Thesis Note

When writing the thesis, describe these rows as security-sensitive but semantically valid. The important boundary is that sample-program changes are not separate GT entries; they are accepted only because they express the same memory-safety release-note fact as `GT-002`.

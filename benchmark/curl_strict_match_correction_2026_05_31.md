# Curl Strict Match Correction 2026-05-31

This record documents the second targeted strict-match audit for curl cases. It removes helper/test/refactor-only matches that did not state the reviewed release-note-level behavior and moves backend-only TLCP/OpenHiTLS evidence from the user-option GT to the backend-support GT where appropriate.

## Summary

- date: `2026-05-31`
- scope: `curl strict-match correction`
- changed_match_files: `14`
- record_count: `35`
- removed_count: `30`
- moved_count: `5`

## Corrections

| Action | Case | Method Path | Generated | GT | Title | Reason |
| --- | --- | --- | --- | --- | --- | --- |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\cmg_strict_1hop\baselines\full` | `GEN-035` | `GT-U014` | Fix buffer overflow check and interface binding logic in bindlocal | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\cmg_strict_1hop\baselines\full` | `GEN-051` | `GT-U015` | Fix memory leak in MIME reader cleanup | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\cmg_strict_1hop\baselines\full` | `GEN-074` | `GT-U015` | Initialize temporary buffer in mime reader initialization | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\cmg_strict_1hop\baselines\full` | `GEN-093` | `GT-U016` | Refactor option parsing into dedicated functions | Generated note is parser refactoring only and does not state the --continue-at incompatibility behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\no_fallback\baselines\no_fallback` | `GEN-027` | `GT-U014` | Fix interface length validation and binding logic in bindlocal | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\no_fallback\baselines\no_fallback` | `GEN-059` | `GT-U015` | Fixed memory leak in MIME reader cleanup | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\no_fallback\baselines\no_fallback` | `GEN-061` | `GT-U015` | Fixed mime reader buffer initialization | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `ablations\no_fallback\baselines\no_fallback` | `GEN-076` | `GT-U016` | Refactor option parsing into dedicated functions | Generated note is parser refactoring only and does not state the --continue-at incompatibility behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\diff_only` | `GEN-039` | `GT-U014` | Fix interface binding logic and add length validation | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\diff_only` | `GEN-046` | `GT-U015` | Fix memory leak in MIME reader close | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\diff_only` | `GEN-072` | `GT-U015` | Initialize temporary buffer in MIME reader | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\full` | `GEN-041` | `GT-U014` | Fix interface length validation and binding logic in bindlocal | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\full` | `GEN-047` | `GT-U015` | Fix memory leak in MIME reader cleanup | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\full` | `GEN-072` | `GT-U015` | Initialize temporary buffer for MIME reader | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\no_graph` | `GEN-041` | `GT-U014` | Fix interface binding logic and add length check | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\no_graph` | `GEN-042` | `GT-U015` | Fix mime reader buffer initialization | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines\no_graph` | `GEN-069` | `GT-U015` | Fixed memory leak in MIME reader cleanup | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_evidence_similarity\full` | `GEN-039` | `GT-U014` | Fix interface length validation and binding logic in bindlocal | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_evidence_similarity\full` | `GEN-044` | `GT-U015` | Fix memory leak in MIME reader cleanup | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_evidence_similarity\full` | `GEN-069` | `GT-U015` | Initialize temporary buffer for MIME reader | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_evidence_similarity\full` | `GEN-090` | `GT-U016` | Refactor option parsing into dedicated functions | Generated note is parser refactoring only and does not state the --continue-at incompatibility behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_similarity\full` | `GEN-036` | `GT-U014` | Fix interface length validation and binding logic in bindlocal | Generated note describes generic interface/SO_BINDTODEVICE handling, not the reviewed host!<ip> local-binding behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_similarity\full` | `GEN-041` | `GT-U015` | Fix memory leak in MIME reader cleanup | Generated note is MIME buffer cleanup/initialization support, not the small-read stall behavior. |
| `remove` | `curl_8_11_0_to_8_11_1` | `baselines_similarity\full` | `GEN-078` | `GT-U016` | Refactor option parsing into dedicated functions | Generated note is parser refactoring only and does not state the --continue-at incompatibility behavior. |
| `remove` | `curl_8_14_0_to_8_14_1` | `ablations\cmg_strict_1hop\baselines\full` | `GEN-097` | `GT-C010` | Add send_chunk helper for WebSocket test reliability | Generated note is WebSocket test helper coverage, not runtime WebSocket behavior or diagnostics. |
| `remove` | `curl_8_14_0_to_8_14_1` | `baselines_evidence_similarity\full` | `GEN-015` | `GT-C005` | Enable automatic redirect following in hx-upload test client | Generated note is test-client redirect setup, not the runtime HTTP redirect rewind failure behavior. |
| `remove` | `curl_8_14_0_to_8_14_1` | `baselines_evidence_similarity\full` | `GEN-090` | `GT-C010` | Add recv_chunk helper for WebSocket test coverage | Generated note is WebSocket test helper coverage, not runtime WebSocket behavior or diagnostics. |
| `remove` | `curl_8_14_0_to_8_14_1` | `baselines_similarity\full` | `GEN-012` | `GT-C005` | Enable automatic redirect following in hx-upload test client | Generated note is test-client redirect setup, not the runtime HTTP redirect rewind failure behavior. |
| `remove` | `curl_8_14_0_to_8_14_1` | `baselines_similarity\full` | `GEN-065` | `GT-C010` | Add recv_chunk helper for WebSocket test coverage | Generated note is WebSocket test helper coverage, not runtime WebSocket behavior or diagnostics. |
| `remove` | `curl_v6_0_to_v6_0_0_1` | `ablations\no_fallback\baselines_deepseek_chat\no_fallback` | `GEN-025` | `GT-002` | Fix CA certificate parsing and verification for HITLS | Generated note attaches CVE wording to non-cookie OpenHiTLS/TLCP behavior. |
| `move` | `curl_v6_0_to_v6_0_0_1` | `baselines_deepseek_v4_flash\full` | `GEN-007` | `GT-003 -> GT-002` | Add OpenHiTLS cleanup support in OpenSSL backend | Generated note is backend TLCP/OpenHiTLS support evidence, not user-facing encrypted certificate/key option exposure. |
| `move` | `curl_v6_0_to_v6_0_0_1` | `baselines_deepseek_v4_flash\full` | `GEN-010` | `GT-003 -> GT-002` | Add TLCP private key parsing and configuration support | Generated note is backend TLCP/OpenHiTLS support evidence, not user-facing encrypted certificate/key option exposure. |
| `move` | `curl_v6_0_to_v6_0_0_1` | `baselines_deepseek_v4_flash\full` | `GEN-022` | `GT-003 -> GT-002` | Add support for parsing private keys with multiple formats | Generated note is backend TLCP/OpenHiTLS support evidence, not user-facing encrypted certificate/key option exposure. |
| `move` | `curl_v6_0_to_v6_0_0_1` | `baselines_deepseek_v4_flash_evidence_similarity\full` | `GEN-007` | `GT-003 -> GT-002` | Add TLCP private key parsing and configuration support | Generated note is backend TLCP/OpenHiTLS support evidence, not user-facing encrypted certificate/key option exposure. |
| `move` | `curl_v6_0_to_v6_0_0_1` | `baselines_deepseek_v4_flash_similarity\full` | `GEN-013` | `GT-003 -> GT-002` | Support TLCPv1.1 SSL version in OpenHiTLS | Generated note is backend TLCP/OpenHiTLS support evidence, not user-facing encrypted certificate/key option exposure. |

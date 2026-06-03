# Ground Truth: third_party_curl OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release

Status: `reviewed`

Evidence packet:

- `benchmark/cases/third_party_curl/curl_v6_0_beta1_to_v6_0/evidence.md`

## Evidence Checklist

- [ ] Inspect OpenHarmony v6.0 Beta1 platform release notes.
- [ ] Inspect OpenHarmony v6.0 platform release notes.
- [x] Inspect `changed_functions.json` for changed-function inventory.
- [x] Run Stage 2/3 artifacts before final admission.
- [x] Inspect commit messages between the two tags.
- [ ] Inspect curl `CHANGES` or `RELEASE-NOTES` if entries can be mapped to the OpenHarmony component diff.

## Evidence Summary

- Pipeline status: `verified_full_pipeline_mock`.
- Changed functions: `12`.
- CMG matched entries: `10`.
- CMG unmatched entries: `2`.
- Fallback-context coverage: `12/12`.
- Current use: medium network case admitted for `core_eval`.

## Reviewed Release Note Entries

| GT ID | Section | Release-Note Entry | Supporting Evidence | Notes |
| --- | --- | --- | --- | --- |
| GT-001 | Feature | Add OpenHarmony network handover support so curl can bind resolver and transfer sockets to a specified OHOS network ID and avoid reusing cached connections across incompatible network contexts. | Commits `add handover`, `add options for handover feature`; changed functions `bindohosnetid`, `Curl_resolver_init`, `bindlocal`, `Curl_vsetopt`, `Curl_init_userdefined`, `ConnectionExists`, `allocate_conn`; diff adds `CURLOPT_OHOS_SOCKET_BIND_NET_ID`, connection-reuse callback fields, and `BindSocket` calls. | OpenHarmony-specific behavior; two `bindohosnetid` functions remain ENRE-unmatched but are covered by fallback diff evidence. |
| GT-002 | Feature | Add an MMS reserved-default-port option so HTTP URL construction can preserve the scheme default port when MMS scenarios require it. | Commit `mms opt`; changed functions `Curl_http_output_auth`, `Curl_http_target`, `Curl_vsetopt`; diff adds `CURLOPT_MMS_RESERVED_DEFAULT_PORT` and bypasses `CURLU_NO_DEFAULT_PORT` when enabled. | Component-level option change; no official platform release-note mapping found yet. |
| GT-003 | Fix | Limit stored HTTP response headers and return `CURLE_TOO_LARGE` when the response header list exceeds the configured maximum. | Commit message `DTS2025052220894`; changed function `Curl_headers_push`; diff adds `MAX_HTTP_RESP_HEADER_COUNT` and checks `Curl_llist_count(&data->state.httphdrs)`. | Interpreted as robustness/resource-protection fix. |
| GT-004 | Fix | Harden FTP directory-list parsing by guarding offset updates when the parsed line length is zero, matching an upstream curl parser fix. | Commit `update lib/ftplistparser.c` references upstream curl commit `196afaf75c4f04ebe33c60cc2ea07301a9b9321a`; changed function `Curl_ftp_parselist`; diff adds `&& len` checks. | Upstream-mapped parser robustness fix. |

## Excluded Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
| BUILD.gn and bundle metadata updates | Build/package metadata only; no direct release-note semantics for runtime behavior. | Commit messages `update BUILD.gn`, `update bundle.json`; changed C/C++ evidence unaffected. |
| Copyright update | Maintenance-only copyright refresh. | Commit message `update copyright`; no changed runtime function evidence. |
| DNS cache patch wording change | Patch-file maintenance is not represented in the current C/C++ function-level evidence for this case. | Commit `clean cache but not destroy` changes `0004-ProvieClearDnsCacheAPI.patch` only. |

## Reviewer Notes

- Drafted from local commit messages, function-level diff evidence, and the generated evidence packet.
- Second-pass review accepted the four current entries for core evaluation.
- Current entries are semantic ground-truth candidates; generated mock release notes were not copied as authoritative evidence.

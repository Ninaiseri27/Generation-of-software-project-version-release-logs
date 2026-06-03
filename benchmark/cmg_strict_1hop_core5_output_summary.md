# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `summarized` | `rule_family` | 12 | 12 | 12 | 1.0000 | 0.0000 | 14665 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `summarized` | `rule_family` | 23 | 23 | 22 | 0.9565 | 0.0435 | 29766 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `summarized` | `rule_family` | 42 | 42 | 35 | 0.8333 | 0.1667 | 70737 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `summarized` | `rule_family` | 2 | 2 | 2 | 1.0000 | 0.0000 | 1510 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `summarized` | `rule_family` | 11 | 11 | 11 | 1.0000 | 0.0000 | 11398 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 18.0000 | 16.4000 | 0.9580 | 0.0420 | 25615.2000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

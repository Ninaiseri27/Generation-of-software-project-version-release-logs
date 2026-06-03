# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `no_fallback` | `summarized` | `rule_family` | 12 | 12 | 12 | 1.0000 | 0.0000 | 10761 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_fallback` | `summarized` | `rule_family` | 23 | 23 | 22 | 0.9565 | 0.0435 | 26161 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_fallback` | `summarized` | `rule_family` | 42 | 42 | 38 | 0.9048 | 0.0952 | 47113 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `no_fallback` | `summarized` | `rule_family` | 2 | 2 | 2 | 1.0000 | 0.0000 | 1400 |
| `cjson_v6_0_beta1_to_v6_0` | `no_fallback` | `summarized` | `rule_family` | 11 | 11 | 11 | 1.0000 | 0.0000 | 9726 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `no_fallback` | 5 | 18.0000 | 17.0000 | 0.9723 | 0.0277 | 19032.2000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

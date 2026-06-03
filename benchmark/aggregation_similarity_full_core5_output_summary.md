# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `full` | `summarized` | `similarity_family` | 12 | 12 | 5 | 0.4167 | 0.5833 | 15146 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `summarized` | `similarity_family` | 23 | 23 | 14 | 0.6087 | 0.3913 | 31862 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `summarized` | `similarity_family` | 42 | 42 | 25 | 0.5952 | 0.4048 | 83975 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `summarized` | `similarity_family` | 2 | 2 | 1 | 0.5000 | 0.5000 | 1527 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `summarized` | `similarity_family` | 11 | 11 | 7 | 0.6364 | 0.3636 | 11463 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 18.0000 | 10.4000 | 0.5514 | 0.4486 | 28794.6000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

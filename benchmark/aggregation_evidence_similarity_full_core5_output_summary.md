# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `summarized` | `evidence_similarity_family` | 11 | 11 | 10 | 0.9091 | 0.0909 | 11463 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `summarized` | `evidence_similarity_family` | 12 | 12 | 11 | 0.9167 | 0.0833 | 15146 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `summarized` | `evidence_similarity_family` | 23 | 23 | 19 | 0.8261 | 0.1739 | 31862 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `summarized` | `evidence_similarity_family` | 42 | 42 | 30 | 0.7143 | 0.2857 | 83975 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `summarized` | `evidence_similarity_family` | 2 | 2 | 1 | 0.5000 | 0.5000 | 1527 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | 5 | 18.0000 | 14.2000 | 0.7732 | 0.2268 | 28794.6000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

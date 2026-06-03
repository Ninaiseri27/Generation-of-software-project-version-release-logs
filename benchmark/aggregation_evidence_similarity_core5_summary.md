# Aggregation Strategy Summary

| Case | Variant | Strategy | Status | Generated | Exact Notes | Final Notes | Compression | Reduction | Merged Groups | Max Group Size |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `rule_family` | `summarized` | 11 | 11 | 11 | 1.0000 | 0.0000 | 0 | 1 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `similarity_family` | `summarized` | 11 | 11 | 7 | 0.6364 | 0.3636 | 2 | 4 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `evidence_similarity_family` | `summarized` | 11 | 11 | 10 | 0.9091 | 0.0909 | 1 | 2 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `rule_family` | `summarized` | 12 | 12 | 12 | 1.0000 | 0.0000 | 0 | 1 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `similarity_family` | `summarized` | 12 | 12 | 5 | 0.4167 | 0.5833 | 3 | 4 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `evidence_similarity_family` | `summarized` | 12 | 12 | 11 | 0.9167 | 0.0833 | 1 | 2 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `rule_family` | `summarized` | 23 | 23 | 22 | 0.9565 | 0.0435 | 1 | 2 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `similarity_family` | `summarized` | 23 | 23 | 14 | 0.6087 | 0.3913 | 5 | 4 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `evidence_similarity_family` | `summarized` | 23 | 23 | 19 | 0.8261 | 0.1739 | 3 | 3 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `rule_family` | `summarized` | 42 | 42 | 34 | 0.8095 | 0.1905 | 4 | 6 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `similarity_family` | `summarized` | 42 | 42 | 25 | 0.5952 | 0.4048 | 9 | 4 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `evidence_similarity_family` | `summarized` | 42 | 42 | 30 | 0.7143 | 0.2857 | 6 | 4 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `rule_family` | `summarized` | 2 | 2 | 2 | 1.0000 | 0.0000 | 0 | 1 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `similarity_family` | `summarized` | 2 | 2 | 1 | 0.5000 | 0.5000 | 1 | 2 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `evidence_similarity_family` | `summarized` | 2 | 2 | 1 | 0.5000 | 0.5000 | 1 | 2 |

## Macro Averages

| Variant | Strategy | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Merged Groups | Avg Max Group Size |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `full` | `rule_family` | 5 | 18.0000 | 16.2000 | 0.9532 | 0.0468 | 1.0000 | 2.2000 |
| `full` | `similarity_family` | 5 | 18.0000 | 10.4000 | 0.5514 | 0.4486 | 4.0000 | 3.6000 |
| `full` | `evidence_similarity_family` | 5 | 18.0000 | 14.2000 | 0.7732 | 0.2268 | 2.4000 | 2.6000 |

Notes:

- `none` keeps one final note per generated entry.
- `exact` merges only exactly identical structured notes.
- `rule_family` applies the current heuristic family grouping.
- `similarity_family` groups notes with conservative token and symbol overlap.
- `evidence_similarity_family` additionally requires source-symbol, entity, or file evidence.
- Compression is `final release-note count / generated entry count`; lower means stronger aggregation.

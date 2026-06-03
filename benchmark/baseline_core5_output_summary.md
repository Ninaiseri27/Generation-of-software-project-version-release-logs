# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_beta1_to_v6_0` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 518 |
| `curl_v6_0_beta1_to_v6_0` | `diff_only` | `summarized` | `rule_family` | 12 | 12 | 12 | 1.0000 | 0.0000 | 7212 |
| `curl_v6_0_beta1_to_v6_0` | `no_graph` | `summarized` | `rule_family` | 12 | 12 | 12 | 1.0000 | 0.0000 | 9795 |
| `curl_v6_0_beta1_to_v6_0` | `full` | `summarized` | `rule_family` | 12 | 12 | 12 | 1.0000 | 0.0000 | 15146 |
| `mbedtls_v6_0_beta1_to_v6_0` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 779 |
| `mbedtls_v6_0_beta1_to_v6_0` | `diff_only` | `summarized` | `rule_family` | 23 | 23 | 23 | 1.0000 | 0.0000 | 15466 |
| `mbedtls_v6_0_beta1_to_v6_0` | `no_graph` | `summarized` | `rule_family` | 23 | 23 | 22 | 0.9565 | 0.0435 | 25234 |
| `mbedtls_v6_0_beta1_to_v6_0` | `full` | `summarized` | `rule_family` | 23 | 23 | 22 | 0.9565 | 0.0435 | 31862 |
| `sqlite_v6_0_0_2_to_v6_1` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 482 |
| `sqlite_v6_0_0_2_to_v6_1` | `diff_only` | `summarized` | `rule_family` | 42 | 42 | 37 | 0.8810 | 0.1190 | 35086 |
| `sqlite_v6_0_0_2_to_v6_1` | `no_graph` | `summarized` | `rule_family` | 42 | 42 | 36 | 0.8571 | 0.1429 | 42637 |
| `sqlite_v6_0_0_2_to_v6_1` | `full` | `summarized` | `rule_family` | 42 | 42 | 34 | 0.8095 | 0.1905 | 83975 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 367 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `diff_only` | `summarized` | `rule_family` | 2 | 2 | 2 | 1.0000 | 0.0000 | 1015 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `no_graph` | `summarized` | `rule_family` | 2 | 2 | 2 | 1.0000 | 0.0000 | 1131 |
| `zlib_v6_0_0_1_to_v6_0_0_2` | `full` | `summarized` | `rule_family` | 2 | 2 | 2 | 1.0000 | 0.0000 | 1527 |
| `cjson_v6_0_beta1_to_v6_0` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 505 |
| `cjson_v6_0_beta1_to_v6_0` | `diff_only` | `summarized` | `rule_family` | 11 | 11 | 11 | 1.0000 | 0.0000 | 5927 |
| `cjson_v6_0_beta1_to_v6_0` | `no_graph` | `summarized` | `rule_family` | 11 | 11 | 10 | 0.9091 | 0.0909 | 8147 |
| `cjson_v6_0_beta1_to_v6_0` | `full` | `summarized` | `rule_family` | 11 | 11 | 11 | 1.0000 | 0.0000 | 11463 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 5 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 530.2000 |
| `diff_only` | 5 | 18.0000 | 17.0000 | 0.9762 | 0.0238 | 12941.2000 |
| `no_graph` | 5 | 18.0000 | 16.4000 | 0.9445 | 0.0555 | 17388.8000 |
| `full` | 5 | 18.0000 | 16.2000 | 0.9532 | 0.0468 | 28794.6000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_8_11_0_to_8_11_1` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 633 |
| `curl_8_11_0_to_8_11_1` | `diff_only` | `summarized` | `rule_family` | 103 | 103 | 99 | 0.9612 | 0.0388 | 78164 |
| `curl_8_11_0_to_8_11_1` | `no_graph` | `summarized` | `rule_family` | 103 | 103 | 102 | 0.9903 | 0.0097 | 113490 |
| `curl_8_11_0_to_8_11_1` | `full` | `summarized` | `rule_family` | 103 | 103 | 101 | 0.9806 | 0.0194 | 170746 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 633.0000 |
| `diff_only` | 1 | 103.0000 | 99.0000 | 0.9612 | 0.0388 | 78164.0000 |
| `no_graph` | 1 | 103.0000 | 102.0000 | 0.9903 | 0.0097 | 113490.0000 |
| `full` | 1 | 103.0000 | 101.0000 | 0.9806 | 0.0194 | 170746.0000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

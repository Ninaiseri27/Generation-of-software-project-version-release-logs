# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_8_14_0_to_8_14_1` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 707 |
| `curl_8_14_0_to_8_14_1` | `diff_only` | `summarized` | `rule_family` | 121 | 121 | 121 | 1.0000 | 0.0000 | 103397 |
| `curl_8_14_0_to_8_14_1` | `no_graph` | `summarized` | `rule_family` | 121 | 121 | 118 | 0.9752 | 0.0248 | 151993 |
| `curl_8_14_0_to_8_14_1` | `full` | `summarized` | `rule_family` | 121 | 121 | 119 | 0.9835 | 0.0165 | 222383 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 707.0000 |
| `diff_only` | 1 | 121.0000 | 121.0000 | 1.0000 | 0.0000 | 103397.0000 |
| `no_graph` | 1 | 121.0000 | 118.0000 | 0.9752 | 0.0248 | 151993.0000 |
| `full` | 1 | 121.0000 | 119.0000 | 0.9835 | 0.0165 | 222383.0000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

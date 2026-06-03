# Baseline Output Summary

| Case | Variant | Status | Strategy | Prompt Entries | Generated | Final Notes | Compression | Reduction | Total Tokens |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `summarized` | `rule_family` | 1 | 1 | 1 | 1.0000 | 0.0000 | 796 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `summarized` | `rule_family` | 80 | 80 | 78 | 0.9750 | 0.0250 | 244504 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `summarized` | `rule_family` | 80 | 80 | 79 | 0.9875 | 0.0125 | 283732 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `summarized` | `rule_family` | 80 | 80 | 79 | 0.9875 | 0.0125 | 289843 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `summarized` | `rule_family` | 80 | 80 | 79 | 0.9875 | 0.0125 | 346520 |

## Macro Averages

| Variant | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Total Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 796.0000 |
| `diff_only` | 1 | 80.0000 | 78.0000 | 0.9750 | 0.0250 | 244504.0000 |
| `no_graph` | 1 | 80.0000 | 79.0000 | 0.9875 | 0.0125 | 283732.0000 |
| `no_fallback` | 1 | 80.0000 | 79.0000 | 0.9875 | 0.0125 | 289843.0000 |
| `full` | 1 | 80.0000 | 79.0000 | 0.9875 | 0.0125 | 346520.0000 |

Notes:

- Compression is `final release-note count / generated entry count`; lower means more aggregation.
- Reduction is `1 - compression`; higher means more generated entries were merged or removed.

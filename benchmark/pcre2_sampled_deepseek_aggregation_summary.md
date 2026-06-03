# Aggregation Strategy Summary

| Case | Variant | Strategy | Status | Generated | Exact Notes | Final Notes | Compression | Reduction | Merged Groups | Max Group Size |
| --- | --- | --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `none` | `summarized` | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `exact` | `summarized` | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `rule_family` | `summarized` | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `similarity_family` | `summarized` | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `text_only` | `evidence_similarity_family` | `summarized` | 1 | 1 | 1 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `none` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `exact` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `rule_family` | `summarized` | 80 | 80 | 78 | 0.9750 | 0.0250 | 2 | 2 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `similarity_family` | `summarized` | 80 | 80 | 49 | 0.6125 | 0.3875 | 14 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `diff_only` | `evidence_similarity_family` | `summarized` | 80 | 80 | 55 | 0.6875 | 0.3125 | 16 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `none` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `exact` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `rule_family` | `summarized` | 80 | 80 | 79 | 0.9875 | 0.0125 | 1 | 2 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `similarity_family` | `summarized` | 80 | 80 | 45 | 0.5625 | 0.4375 | 15 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_graph` | `evidence_similarity_family` | `summarized` | 80 | 80 | 53 | 0.6625 | 0.3375 | 15 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `none` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `exact` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `rule_family` | `summarized` | 80 | 80 | 79 | 0.9875 | 0.0125 | 1 | 2 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `similarity_family` | `summarized` | 80 | 80 | 46 | 0.5750 | 0.4250 | 12 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `no_fallback` | `evidence_similarity_family` | `summarized` | 80 | 80 | 52 | 0.6500 | 0.3500 | 15 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `none` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `exact` | `summarized` | 80 | 80 | 80 | 1.0000 | 0.0000 | 0 | 1 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `rule_family` | `summarized` | 80 | 80 | 79 | 0.9875 | 0.0125 | 1 | 2 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `similarity_family` | `summarized` | 80 | 80 | 46 | 0.5750 | 0.4250 | 12 | 4 |
| `pcre2_v6_0_0_2_to_v6_1` | `full` | `evidence_similarity_family` | `summarized` | 80 | 80 | 54 | 0.6750 | 0.3250 | 14 | 4 |

## Macro Averages

| Variant | Strategy | Summarized Cases | Avg Generated | Avg Final Notes | Avg Compression | Avg Reduction | Avg Merged Groups | Avg Max Group Size |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | `none` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `text_only` | `exact` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `text_only` | `rule_family` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `text_only` | `similarity_family` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `text_only` | `evidence_similarity_family` | 1 | 1.0000 | 1.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `diff_only` | `none` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `diff_only` | `exact` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `diff_only` | `rule_family` | 1 | 80.0000 | 78.0000 | 0.9750 | 0.0250 | 2.0000 | 2.0000 |
| `diff_only` | `similarity_family` | 1 | 80.0000 | 49.0000 | 0.6125 | 0.3875 | 14.0000 | 4.0000 |
| `diff_only` | `evidence_similarity_family` | 1 | 80.0000 | 55.0000 | 0.6875 | 0.3125 | 16.0000 | 4.0000 |
| `no_graph` | `none` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `no_graph` | `exact` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `no_graph` | `rule_family` | 1 | 80.0000 | 79.0000 | 0.9875 | 0.0125 | 1.0000 | 2.0000 |
| `no_graph` | `similarity_family` | 1 | 80.0000 | 45.0000 | 0.5625 | 0.4375 | 15.0000 | 4.0000 |
| `no_graph` | `evidence_similarity_family` | 1 | 80.0000 | 53.0000 | 0.6625 | 0.3375 | 15.0000 | 4.0000 |
| `no_fallback` | `none` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `no_fallback` | `exact` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `no_fallback` | `rule_family` | 1 | 80.0000 | 79.0000 | 0.9875 | 0.0125 | 1.0000 | 2.0000 |
| `no_fallback` | `similarity_family` | 1 | 80.0000 | 46.0000 | 0.5750 | 0.4250 | 12.0000 | 4.0000 |
| `no_fallback` | `evidence_similarity_family` | 1 | 80.0000 | 52.0000 | 0.6500 | 0.3500 | 15.0000 | 4.0000 |
| `full` | `none` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `full` | `exact` | 1 | 80.0000 | 80.0000 | 1.0000 | 0.0000 | 0.0000 | 1.0000 |
| `full` | `rule_family` | 1 | 80.0000 | 79.0000 | 0.9875 | 0.0125 | 1.0000 | 2.0000 |
| `full` | `similarity_family` | 1 | 80.0000 | 46.0000 | 0.5750 | 0.4250 | 12.0000 | 4.0000 |
| `full` | `evidence_similarity_family` | 1 | 80.0000 | 54.0000 | 0.6750 | 0.3250 | 14.0000 | 4.0000 |

Notes:

- `none` keeps one final note per generated entry.
- `exact` merges only exactly identical structured notes.
- `rule_family` applies the current heuristic family grouping.
- `similarity_family` groups notes with conservative token and symbol overlap.
- `evidence_similarity_family` additionally requires source-symbol, entity, or file evidence.
- Compression is `final release-note count / generated entry count`; lower means stronger aggregation.

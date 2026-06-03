# Core6 Candidate Stress Analysis

Last updated: 2026-05-16

This document summarizes the completed real-backend stress analysis for
`third_party_curl OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release`.

The case is intentionally treated as an extended stress case rather than an admitted
`core_eval` case. It is useful because it has larger changed-function volume than the
current core5 cases, but its GT status and output behavior make it less stable as a
main-matrix case.

## Case Position

| Item | Value |
| --- | --- |
| Case ID | `curl_v6_0_to_v6_0_0_1` |
| Repository | `third_party_curl` |
| Version Pair | `OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release` |
| Changed Functions | 47 |
| Changed C/C++ Files | 17 |
| GT Entries | 3 draft candidate entries |
| Current Role | `core6_candidate` / secondary stress case |
| Main Recommendation | Do not replace core5. Report as a stress-case extension if needed. |

## Strict Evaluation Result

Strict matching uses release-note-level semantic judgments in `matches_strict.json`.

| Variant | Generated | Final Notes | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT | Tokens |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `text_only` | 1 | 1 | 1.0000 | 0.3333 | 0.5000 | 0.0000 | 0.3333 | 0.0000 | 561 |
| `diff_only` | 47 | 47 | 0.6596 | 0.6667 | 0.6631 | 0.3404 | 10.3333 | 9.6667 | 30450 |
| `no_graph` | 47 | 45 | 0.6222 | 0.6667 | 0.6437 | 0.3778 | 9.3333 | 8.6667 | 42926 |
| `full` | 47 | 47 | 0.4681 | 0.6667 | 0.5500 | 0.5319 | 7.3333 | 6.6667 | 73440 |

Coverage:

- `text_only` covers only `GT-001` by exact CVE identifier.
- `diff_only`, `no_graph`, and `full` cover `GT-002` and `GT-003`.
- Evidence-rich variants do not strictly cover `GT-001` because their cookie-related notes do not state the full CVE/security behavior.

Interpretation:

- `diff_only` is strongest on this large curl candidate.
- `full` has the highest token cost and weakest evidence-rich F1, reinforcing the context-noise risk already observed in core5.
- All evidence-rich variants remain highly redundant, with `Extra/GT` above `6.0`.
- The case is therefore valuable as a stress test for redundancy, context noise, and security-claim precision, not as a clean replacement for the core5 main matrix.

## Aggregation Stress Result

Aggregation is computed from existing generated notes and does not consume additional API budget.

| Variant | Strategy | Generated | Final Notes | Reduction | Merged Groups | Max Group Size |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `diff_only` | `rule_family` | 47 | 47 | 0.0000 | 0 | 1 |
| `diff_only` | `similarity_family` | 47 | 28 | 0.4043 | 10 | 4 |
| `diff_only` | `evidence_similarity_family` | 47 | 38 | 0.1915 | 6 | 4 |
| `no_graph` | `rule_family` | 47 | 45 | 0.0426 | 1 | 3 |
| `no_graph` | `similarity_family` | 47 | 28 | 0.4043 | 13 | 4 |
| `no_graph` | `evidence_similarity_family` | 47 | 39 | 0.1702 | 7 | 3 |
| `full` | `rule_family` | 47 | 47 | 0.0000 | 0 | 1 |
| `full` | `similarity_family` | 47 | 25 | 0.4681 | 13 | 4 |
| `full` | `evidence_similarity_family` | 47 | 37 | 0.2128 | 7 | 4 |

Interpretation:

- `rule_family` is too weak for this larger network/TLS cluster.
- `similarity_family` gives the strongest compression, especially on `full`, reducing 47 generated notes to 25.
- `evidence_similarity_family` is more conservative and keeps stronger traceability, but still reduces around 17-21%.
- Aggregated-note strict matching has now been performed separately; see `benchmark/curl_stress_aggregation_strict_eval.md`.

## Aggregated Strict Evaluation

| Variant | Strategy | Generated | Precision | Recall | F1 | Unsupported Rate | Extra/GT |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: |
| `diff_only` | `similarity_family` | 28 | 0.6429 | 0.6667 | 0.6545 | 0.3571 | 5.3333 |
| `diff_only` | `evidence_similarity_family` | 38 | 0.6316 | 0.6667 | 0.6486 | 0.3684 | 7.3333 |
| `no_graph` | `similarity_family` | 28 | 0.5714 | 0.6667 | 0.6154 | 0.4286 | 4.6667 |
| `no_graph` | `evidence_similarity_family` | 39 | 0.5897 | 0.6667 | 0.6259 | 0.4103 | 7.0000 |
| `full` | `similarity_family` | 25 | 0.4800 | 0.6667 | 0.5581 | 0.5200 | 4.3333 |
| `full` | `evidence_similarity_family` | 37 | 0.4324 | 0.6667 | 0.5246 | 0.5676 | 4.6667 |

Strict aggregation evaluation confirms that aggregation reduces redundancy but does not solve GT-001 coverage or unsupported security claims. The best aggregate result is `diff_only + similarity_family`, which keeps F1 close to unaggregated `diff_only` while reducing final notes from 47 to 28.

## Thesis Usage

Use this case as a secondary experiment paragraph rather than the headline table:

- It supports the claim that larger real-world version pairs make redundancy more severe.
- It supports the claim that `diff_only` can remain a strong baseline when extra context is noisy.
- It provides a concrete security-claim failure case: evidence-rich outputs can misattribute CVE-2025-9086 to unrelated OpenHiTLS/OpenSSL changes.
- It motivates future aggregation work because rule-based family grouping is too weak on large coherent feature clusters.

Do not use it to claim that CMG is ineffective in general. The case has only three draft GT entries, and the GT granularity makes recall sensitive to whether CVE-only notes are accepted.

## Reproduction Commands

Real baseline generation:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli run-baselines `
  --config configs\third_party_curl_v6_0_to_v6_0_0_1_deepseek.json `
  --variants text_only diff_only no_graph `
  --backend openai `
  --model deepseek-v4-flash `
  --aggregation-strategy rule_family `
  --output-root outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash `
  --summary-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash\baseline_summary_missing_variants.json
```

Strict evaluation:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli evaluate-baselines `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_to_v6_0_0_1\metadata.json `
  --variants text_only diff_only no_graph full `
  --baseline-root-name baselines_deepseek_v4_flash `
  --matches-filename matches_strict.json `
  --evaluation-filename evaluation_strict.json `
  --match-template-filename match_template_strict.json `
  --summary-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\evaluation_deepseek_v4_flash_summary.json
```

Aggregation summary:

```powershell
$env:PYTHONPATH='cpp_release_note_mvp/src'
python -m cpp_release_note_mvp.cli summarize-aggregation `
  --metadata benchmark\cases\third_party_curl\curl_v6_0_to_v6_0_0_1\metadata.json `
  --variants text_only diff_only no_graph full `
  --strategies none exact rule_family similarity_family evidence_similarity_family `
  --baseline-root-name baselines_deepseek_v4_flash `
  --json-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\aggregation_deepseek_v4_flash_table.json `
  --markdown-output outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\aggregation_deepseek_v4_flash_table.md
```

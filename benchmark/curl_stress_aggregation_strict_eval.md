# Curl Stress Aggregation Strict Evaluation

Last updated: 2026-05-16

This note records strict semantic evaluation for aggregation variants on the
`curl_v6_0_to_v6_0_0_1` stress case. Unlike the earlier aggregation summary,
this evaluation does not only count final-note compression; it evaluates the
materialized aggregated `release_note.json` files against the same GT entries.

## Scope

Case:

- `third_party_curl OpenHarmony-v6.0-Release -> OpenHarmony-v6.0.0.1-Release`

Evaluated variants:

- `diff_only`
- `no_graph`
- `full`

Evaluated aggregation strategies:

- `similarity_family`
- `evidence_similarity_family`

The `text_only` variant is omitted here because it has one generated note and no
meaningful aggregation behavior.

## Match Policy

Aggregated matches are derived from source entries that were already accepted in
the unaggregated `matches_strict.json`, then manually audited.

High-risk security rule:

- If aggregation introduces an unsupported CVE attribution, the aggregate note is
  left unmatched even when part of the same note contains otherwise valid backend
  evidence.

This rule specifically affects no-graph aggregate notes that incorrectly connect
CVE-2025-9086 to HITLS/OpenSSL certificate-store or blank-line changes.

## Results

| Variant | Strategy | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `diff_only` | `similarity_family` | 28 | 0.6429 | 0.6667 | 0.6545 | 0.3571 | 6.0000 | 5.3333 |
| `diff_only` | `evidence_similarity_family` | 38 | 0.6316 | 0.6667 | 0.6486 | 0.3684 | 8.0000 | 7.3333 |
| `no_graph` | `similarity_family` | 28 | 0.5714 | 0.6667 | 0.6154 | 0.4286 | 5.3333 | 4.6667 |
| `no_graph` | `evidence_similarity_family` | 39 | 0.5897 | 0.6667 | 0.6259 | 0.4103 | 7.6667 | 7.0000 |
| `full` | `similarity_family` | 25 | 0.4800 | 0.6667 | 0.5581 | 0.5200 | 5.0000 | 4.3333 |
| `full` | `evidence_similarity_family` | 37 | 0.4324 | 0.6667 | 0.5246 | 0.5676 | 5.3333 | 4.6667 |

For comparison, the unaggregated strict results were:

| Variant | Generated | Precision | Recall | F1 | Unsupported Rate | Matches/GT | Extra/GT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `diff_only` | 47 | 0.6596 | 0.6667 | 0.6631 | 0.3404 | 10.3333 | 9.6667 |
| `no_graph` | 45 | 0.6222 | 0.6667 | 0.6437 | 0.3778 | 9.3333 | 8.6667 |
| `full` | 47 | 0.4681 | 0.6667 | 0.5500 | 0.5319 | 7.3333 | 6.6667 |

## Interpretation

- Aggregation reduces redundancy substantially on this larger curl case.
- `diff_only + similarity_family` is the best aggregate result: it reduces
  final notes from 47 to 28 while keeping F1 close to unaggregated `diff_only`
  (`0.6545` vs `0.6631`).
- `full + similarity_family` has the strongest compression but only slightly
  improves F1 over unaggregated `full` (`0.5581` vs `0.5500`), and unsupported
  rate remains high.
- `evidence_similarity_family` is not always better than `similarity_family` in
  this case. Its evidence gate preserves more notes, so it reduces less
  redundancy and does not improve strict F1.
- No aggregation strategy recovers GT-001 for evidence-rich variants. The CVE
  entry remains covered only by `text_only` through exact CVE wording.

## Thesis Use

This result can be cited as a secondary stress-case finding:

> On a larger curl version pair, aggregation reduces redundant generated notes,
> but the best result remains a tradeoff. Similarity-based aggregation compresses
> aggressively and keeps F1 close to the unaggregated diff-only output, while
> graph-rich outputs still suffer from unsupported security claims and high token
> cost.

Do not mix these numbers into the core5 main matrix unless the thesis explicitly
introduces a separate extended/stress evaluation table.

## Reproduction

Materialize aggregation outputs:

```powershell
$base='outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash'
$env:PYTHONPATH='cpp_release_note_mvp/src'
foreach ($variant in @('diff_only','no_graph','full')) {
  foreach ($strategy in @('similarity_family','evidence_similarity_family')) {
    python -m cpp_release_note_mvp.cli rewrite-aggregation `
      --input "$base\$variant\release_note.json" `
      --aggregation-strategy $strategy `
      --json-output "$base\$variant\release_note_$strategy.json" `
      --markdown-output "$base\$variant\release_note_$strategy.md"
  }
}
```

Evaluate after preparing `matches_<strategy>.json`:

```powershell
$gt='benchmark\cases\third_party_curl\curl_v6_0_to_v6_0_0_1\ground_truth.md'
$env:PYTHONPATH='cpp_release_note_mvp/src'
foreach ($variant in @('diff_only','no_graph','full')) {
  foreach ($strategy in @('similarity_family','evidence_similarity_family')) {
    python -m cpp_release_note_mvp.cli evaluate-release-notes `
      --ground-truth $gt `
      --release-note "$base\$variant\release_note_$strategy.json" `
      --matches "$base\$variant\matches_$strategy.json" `
      --output "$base\$variant\evaluation_$strategy.json" `
      --match-template-output "$base\$variant\match_template_$strategy.json"
  }
}
```

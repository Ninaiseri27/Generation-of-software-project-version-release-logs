# Final Match Completion Report

Last updated: 2026-05-28

This report records the assistant-completed strict match files for the selected final benchmark matrix. Version 2 uses a conservative semantic filter: a generated item must overlap GT source-symbol evidence and state visible behavior, while helper/refactor-only summaries are rejected unless they also express the release-note-level behavior.

| Case | Output Dir | GT | Generated | Matches | Precision | Recall | F1 | Unsupported |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| `curl_v6_0_to_v6_0_0_1` | `outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\ablations\no_fallback\baselines_deepseek_chat\no_fallback` | 3 | 46 | 24 | 0.5217 | 1.0 | 0.6857 | 0.4783 |
| `curl_v6_0_to_v6_0_0_1` | `outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\ablations\cmg_strict_1hop\baselines_deepseek_chat\full` | 3 | 45 | 24 | 0.5333 | 1.0 | 0.6957 | 0.4667 |
| `curl_v6_0_to_v6_0_0_1` | `outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash_similarity\full` | 3 | 25 | 18 | 0.68 | 1.0 | 0.8095 | 0.32 |
| `curl_v6_0_to_v6_0_0_1` | `outputs\benchmark\third_party_curl\OpenHarmony-v6.0-Release__OpenHarmony-v6.0.0.1-Release\baselines_deepseek_v4_flash_evidence_similarity\full` | 3 | 37 | 21 | 0.5405 | 1.0 | 0.7018 | 0.4595 |
| `pcre2_v6_0_0_2_to_v6_1` | `outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\ablations\cmg_strict_1hop\sampled_baselines_deepseek_chat\full` | 5 | 80 | 18 | 0.1875 | 1.0 | 0.3158 | 0.8125 |
| `pcre2_v6_0_0_2_to_v6_1` | `outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_baselines_deepseek_chat_similarity\full` | 5 | 46 | 15 | 0.2609 | 1.0 | 0.4138 | 0.7391 |
| `pcre2_v6_0_0_2_to_v6_1` | `outputs\benchmark\third_party_pcre2\OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release\sampled_baselines_deepseek_chat_evidence_similarity\full` | 5 | 54 | 14 | 0.2037 | 1.0 | 0.3385 | 0.7963 |
| `curl_8_11_0_to_8_11_1` | `outputs\benchmark\upstream_curl\curl-8_11_0__curl-8_11_1\ablations\no_fallback\baselines\no_fallback` | 16 | 103 | 29 | 0.2816 | 0.9375 | 0.4331 | 0.7184 |
| `curl_8_11_0_to_8_11_1` | `outputs\benchmark\upstream_curl\curl-8_11_0__curl-8_11_1\ablations\cmg_strict_1hop\baselines\full` | 16 | 101 | 30 | 0.297 | 1.0 | 0.458 | 0.703 |
| `curl_8_11_0_to_8_11_1` | `outputs\benchmark\upstream_curl\curl-8_11_0__curl-8_11_1\baselines_similarity\full` | 16 | 82 | 26 | 0.3171 | 0.9375 | 0.4739 | 0.6829 |
| `curl_8_11_0_to_8_11_1` | `outputs\benchmark\upstream_curl\curl-8_11_0__curl-8_11_1\baselines_evidence_similarity\full` | 16 | 96 | 28 | 0.2917 | 0.9375 | 0.4449 | 0.7083 |
| `curl_8_14_0_to_8_14_1` | `outputs\benchmark\upstream_curl\curl-8_14_0__curl-8_14_1\ablations\no_fallback\baselines\no_fallback` | 10 | 120 | 16 | 0.1333 | 0.8 | 0.2286 | 0.8667 |
| `curl_8_14_0_to_8_14_1` | `outputs\benchmark\upstream_curl\curl-8_14_0__curl-8_14_1\ablations\cmg_strict_1hop\baselines\full` | 10 | 119 | 18 | 0.1429 | 0.9 | 0.2466 | 0.8571 |
| `curl_8_14_0_to_8_14_1` | `outputs\benchmark\upstream_curl\curl-8_14_0__curl-8_14_1\baselines_similarity\full` | 10 | 77 | 16 | 0.1948 | 0.9 | 0.3203 | 0.8052 |
| `curl_8_14_0_to_8_14_1` | `outputs\benchmark\upstream_curl\curl-8_14_0__curl-8_14_1\baselines_evidence_similarity\full` | 10 | 106 | 19 | 0.1698 | 0.9 | 0.2857 | 0.8302 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines\text_only` | 16 | 1 | 0 | 0.0 | 0.0 | 0.0 | 1.0 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines\diff_only` | 16 | 102 | 46 | 0.451 | 1.0 | 0.6216 | 0.549 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines\no_graph` | 16 | 100 | 47 | 0.47 | 1.0 | 0.6395 | 0.53 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines\full` | 16 | 102 | 47 | 0.4608 | 1.0 | 0.6309 | 0.5392 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines\no_fallback` | 16 | 102 | 47 | 0.4608 | 0.9375 | 0.6179 | 0.5392 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\ablations\cmg_strict_1hop\baselines\full` | 16 | 100 | 49 | 0.48 | 0.9375 | 0.6349 | 0.52 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines_similarity\full` | 16 | 75 | 46 | 0.5867 | 1.0 | 0.7395 | 0.4133 |
| `git_2_51_0_to_2_51_1` | `outputs\benchmark\upstream_git\v2.51.0__v2.51.1\baselines_evidence_similarity\full` | 16 | 94 | 47 | 0.4894 | 1.0 | 0.6571 | 0.5106 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat\text_only` | 15 | 1 | 0 | 0.0 | 0.0 | 0.0 | 1.0 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat\diff_only` | 15 | 80 | 58 | 0.725 | 1.0 | 0.8406 | 0.275 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat\no_graph` | 15 | 79 | 54 | 0.6835 | 1.0 | 0.812 | 0.3165 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat\full` | 15 | 80 | 55 | 0.6875 | 1.0 | 0.8148 | 0.3125 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat\no_fallback` | 15 | 80 | 55 | 0.6875 | 1.0 | 0.8148 | 0.3125 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\ablations\cmg_strict_1hop\sampled_baselines_deepseek_chat\full` | 15 | 80 | 55 | 0.6875 | 1.0 | 0.8148 | 0.3125 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat_similarity\full` | 15 | 58 | 44 | 0.7586 | 1.0 | 0.8627 | 0.2414 |
| `git_2_52_0_to_2_53_0` | `outputs\benchmark\upstream_git\v2.52.0__v2.53.0\sampled_baselines_deepseek_chat_evidence_similarity\full` | 15 | 74 | 50 | 0.6757 | 1.0 | 0.8065 | 0.3243 |

# Evidence Pack: third_party_pcre2 OpenHarmony-v6.0.0.2-Release -> OpenHarmony-v6.1-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `pcre2_v6_0_0_2_to_v6_1`
- Repository: `third_party_pcre2`
- Category: `regex_engine`
- Reference version: `OpenHarmony-v6.0.0.2-Release`
- Target version: `OpenHarmony-v6.1-Release`
- Pipeline status: `sampled_stage3_mock_verified`
- Ground-truth status: `draft_sampled`

## Evidence Sources To Inspect

- [ ] sampled changed_functions.json
- [ ] commit messages
- [ ] function-level diffs
- [ ] PCRE2 upstream changelog or release notes if matching version evidence is identifiable
- [ ] OpenHarmony tag and component metadata

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_changed_functions.json`
- sampled_evidence: `benchmark/cases/third_party_pcre2/pcre2_v6_0_0_2_to_v6_1/evidence.md`
- sampled_cmg: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_cmg.json`
- sampled_prompt_bundle: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_prompt_bundle.json`
- sampled_mock_release_note: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_release_note_mock.json`
- sampled_mock_baseline_summary: `outputs/benchmark/third_party_pcre2/OpenHarmony-v6.0.0.2-Release__OpenHarmony-v6.1-Release/sampled_baselines_mock/baseline_summary.json`

## Pipeline Summary

- Commit count: `12`
- Changed C/C++ files: `77`
- Changed functions: `1123`
- Patch only: `False`
- CMG matched entries: `49`
- CMG unmatched entries: `31`
- Fallback-context entries: `80`
- Diff-derived call edges: `764`
- Prompt entries: `80`
- Mock generated entries: `80`

## Commit Messages

- !92 merge fixRegexp into master
- fix static regexp
- !93 merge wls260114 into master
- OAT告警处理20260114
- !91 merge master into master
- feat: update pcre2 to version of 10.46
- !87 merge master into master
- oat告警清理
- !83 merge master into master
- 头文件问题修复
- !82 OAT告警清理 Merge pull request !82 from zhenghui/master
- OAT告警清理

## Changed C/C++ Files

- `pcre2/maint/utf8.c`
- `pcre2/src/pcre2_auto_possess.c`
- `pcre2/src/pcre2_chkdint.c`
- `pcre2/src/pcre2_compile.c`
- `pcre2/src/pcre2_compile_class.c`
- `pcre2/src/pcre2_config.c`
- `pcre2/src/pcre2_context.c`
- `pcre2/src/pcre2_convert.c`
- `pcre2/src/pcre2_dfa_match.c`
- `pcre2/src/pcre2_error.c`
- `pcre2/src/pcre2_find_bracket.c`
- `pcre2/src/pcre2_fuzzsupport.c`
- `pcre2/src/pcre2_jit_char_inc.h`
- `pcre2/src/pcre2_jit_compile.c`
- `pcre2/src/pcre2_jit_neon_inc.h`
- `pcre2/src/pcre2_jit_simd_inc.h`
- `pcre2/src/pcre2_maketables.c`
- `pcre2/src/pcre2_match.c`
- `pcre2/src/pcre2_match_data.c`
- `pcre2/src/pcre2_pattern_info.c`
- `pcre2/src/pcre2_printint.c`
- `pcre2/src/pcre2_serialize.c`
- `pcre2/src/pcre2_study.c`
- `pcre2/src/pcre2_substitute.c`
- `pcre2/src/pcre2_substring.c`
- `pcre2/src/pcre2_xclass.c`
- `pcre2/src/pcre2grep.c`
- `pcre2/src/pcre2posix.c`
- `pcre2/src/pcre2test.c`
- `pcre2/src/sljit/allocator_src/sljitExecAllocatorApple.c`
- `pcre2/src/sljit/allocator_src/sljitExecAllocatorCore.c`
- `pcre2/src/sljit/allocator_src/sljitExecAllocatorFreeBSD.c`
- `pcre2/src/sljit/allocator_src/sljitExecAllocatorPosix.c`
- `pcre2/src/sljit/allocator_src/sljitExecAllocatorWindows.c`
- `pcre2/src/sljit/allocator_src/sljitProtExecAllocatorNetBSD.c`
- `pcre2/src/sljit/allocator_src/sljitProtExecAllocatorPosix.c`
- `pcre2/src/sljit/allocator_src/sljitWXExecAllocatorPosix.c`
- `pcre2/src/sljit/allocator_src/sljitWXExecAllocatorWindows.c`
- `pcre2/src/sljit/sljitExecAllocator.c`
- `pcre2/src/sljit/sljitLir.c`
- `pcre2/src/sljit/sljitLir.h`
- `pcre2/src/sljit/sljitNativeARM_32.c`
- `pcre2/src/sljit/sljitNativeARM_64.c`
- `pcre2/src/sljit/sljitNativeARM_T2_32.c`
- `pcre2/src/sljit/sljitNativeLOONGARCH_64.c`
- `pcre2/src/sljit/sljitNativeMIPS_32.c`
- `pcre2/src/sljit/sljitNativeMIPS_64.c`
- `pcre2/src/sljit/sljitNativeMIPS_common.c`
- `pcre2/src/sljit/sljitNativePPC_32.c`
- `pcre2/src/sljit/sljitNativePPC_64.c`
- `pcre2/src/sljit/sljitNativePPC_common.c`
- `pcre2/src/sljit/sljitNativeRISCV_32.c`
- `pcre2/src/sljit/sljitNativeRISCV_64.c`
- `pcre2/src/sljit/sljitNativeRISCV_common.c`
- `pcre2/src/sljit/sljitNativeS390X.c`
- `pcre2/src/sljit/sljitNativeX86_32.c`
- `pcre2/src/sljit/sljitNativeX86_64.c`
- `pcre2/src/sljit/sljitNativeX86_common.c`
- `pcre2/src/sljit/sljitProtExecAllocator.c`
- `pcre2/src/sljit/sljitSerialize.c`
- `pcre2/src/sljit/sljitUtils.c`
- `pcre2/src/sljit/sljitWXExecAllocator.c`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `main` | `modified` | `pcre2/maint/utf8.c` | `210-345` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 2 | `compare_opcodes` | `modified` | `pcre2/src/pcre2_auto_possess.c` | `547-1146` | `unmatched` | unmatched; level=unmatched; diff_hunks=17; fallback_calls=0 |
| 3 | `PRIV` | `modified` | `pcre2/src/pcre2_chkdint.c` | `65-92` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 4 | `parse_regex` | `added` | `pcre2/src/pcre2_compile.c` | `2923-5756` | `unmatched` | unmatched; level=unmatched; diff_hunks=73; fallback_calls=0 |
| 5 | `compile_branch` | `modified` | `pcre2/src/pcre2_compile.c` | `5946-8285` | `unmatched` | unmatched; level=unmatched; diff_hunks=66; fallback_calls=0 |
| 6 | `compile_optimize_class` | `added` | `pcre2/src/pcre2_compile_class.c` | `500-736` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 7 | `PRIV` | `added` | `pcre2/src/pcre2_compile_class.c` | `1058-1839` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 8 | `pcre2_config` | `modified` | `pcre2/src/pcre2_config.c` | `77-250` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 9 | `pcre2_set_optimize` | `added` | `pcre2/src/pcre2_context.c` | `415-446` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 10 | `pcre2_pattern_convert` | `modified` | `pcre2/src/pcre2_convert.c` | `1062-1167` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 11 | `internal_dfa_match` | `modified` | `pcre2/src/pcre2_dfa_match.c` | `531-3310` | `unmatched` | unmatched; level=unmatched; diff_hunks=16; fallback_calls=0 |
| 12 | `pcre2_get_error_message` | `modified` | `pcre2/src/pcre2_error.c` | `322-365` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 13 | `PRIV` | `modified` | `pcre2/src/pcre2_find_bracket.c` | `69-218` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 14 | `LLVMFuzzerTestOneInput` | `modified` | `pcre2/src/pcre2_fuzzsupport.c` | `279-720` | `unmatched` | unmatched; level=unmatched; diff_hunks=8; fallback_calls=0 |
| 15 | `compile_xclass_matchingpath` | `added` | `pcre2/src/pcre2_jit_char_inc.h` | `501-1229` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 16 | `compile_char1_matchingpath` | `added` | `pcre2/src/pcre2_jit_char_inc.h` | `1816-2212` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 17 | `compile_simple_assertion_matchingpath` | `modified` | `pcre2/src/pcre2_jit_compile.c` | `7709-7950` | `unmatched` | unmatched; level=unmatched; diff_hunks=46; fallback_calls=0 |
| 18 | `compile_char1_matchingpath` | `deleted` | `pcre2/src/pcre2_jit_compile.c` | `8950-9332` | `unmatched` | unmatched; level=unmatched; diff_hunks=36; fallback_calls=0 |
| 19 | `FF_FUN` | `modified` | `pcre2/src/pcre2_jit_neon_inc.h` | `88-354` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 20 | `fast_forward_char_pair_simd` | `modified` | `pcre2/src/pcre2_jit_simd_inc.h` | `476-737` | `unmatched` | unmatched; level=unmatched; diff_hunks=14; fallback_calls=0 |
| 21 | `pcre2_maketables_free` | `modified` | `pcre2/src/pcre2_maketables.c` | `155-162` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 22 | `match` | `modified` | `pcre2/src/pcre2_match.c` | `614-6809` | `unmatched` | unmatched; level=unmatched; diff_hunks=94; fallback_calls=0 |
| 23 | `pcre2_match_data_create_from_pattern` | `modified` | `pcre2/src/pcre2_match_data.c` | `85-91` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 24 | `pcre2_callout_enumerate` | `modified` | `pcre2/src/pcre2_pattern_info.c` | `268-432` | `unmatched` | unmatched; level=unmatched; diff_hunks=4; fallback_calls=0 |
| 25 | `pcre2_printint` | `modified` | `pcre2/src/pcre2_printint.c` | `634-1109` | `unmatched` | unmatched; level=unmatched; diff_hunks=19; fallback_calls=0 |
| 26 | `pcre2_serialize_encode` | `modified` | `pcre2/src/pcre2_serialize.c` | `71-155` | `unmatched` | unmatched; level=unmatched; diff_hunks=5; fallback_calls=0 |
| 27 | `study_char_list` | `added` | `pcre2/src/pcre2_study.c` | `939-1051` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 28 | `pcre2_substitute` | `deleted` | `pcre2/src/pcre2_substitute.c` | `219-1007` | `unmatched` | unmatched; level=unmatched; diff_hunks=46; fallback_calls=0 |
| 29 | `pcre2_substring_nametable_scan` | `modified` | `pcre2/src/pcre2_substring.c` | `482-523` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 30 | `PRIV` | `added` | `pcre2/src/pcre2_xclass.c` | `68-441` | `unmatched` | unmatched; level=unmatched; diff_hunks=31; fallback_calls=0 |
| 31 | `end_of_line` | `modified` | `pcre2/src/pcre2grep.c` | `1504-1647` | `unmatched` | unmatched; level=unmatched; diff_hunks=16; fallback_calls=0 |
| 32 | `pcre2_regerror` | `modified` | `pcre2/src/pcre2posix.c` | `182-246` | `unmatched` | unmatched; level=unmatched; diff_hunks=2; fallback_calls=0 |
| 33 | `case_transform` | `added` | `pcre2/src/pcre2test.c` | `6507-6622` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 34 | `process_data` | `modified` | `pcre2/src/pcre2test.c` | `7201-8810` | `unmatched` | unmatched; level=unmatched; diff_hunks=45; fallback_calls=0 |
| 35 | `get_map_jit_flag` | `deleted` | `pcre2/src/sljit/allocator_src/sljitExecAllocatorApple.c` | `48-73` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 36 | `sljit_malloc_exec` | `deleted` | `pcre2/src/sljit/allocator_src/sljitExecAllocatorCore.c` | `147-245` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 37 | `alloc_chunk` | `deleted` | `pcre2/src/sljit/allocator_src/sljitExecAllocatorFreeBSD.c` | `46-82` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 38 | `alloc_chunk` | `deleted` | `pcre2/src/sljit/allocator_src/sljitExecAllocatorPosix.c` | `30-55` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 39 | `free_chunk` | `deleted` | `pcre2/src/sljit/allocator_src/sljitExecAllocatorWindows.c` | `34-38` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 40 | `alloc_chunk` | `deleted` | `pcre2/src/sljit/allocator_src/sljitProtExecAllocatorNetBSD.c` | `38-62` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 41 | `create_tempfile` | `deleted` | `pcre2/src/sljit/allocator_src/sljitProtExecAllocatorPosix.c` | `53-129` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 42 | `sljit_malloc_exec` | `deleted` | `pcre2/src/sljit/allocator_src/sljitWXExecAllocatorPosix.c` | `78-112` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 43 | `sljit_malloc_exec` | `deleted` | `pcre2/src/sljit/allocator_src/sljitWXExecAllocatorWindows.c` | `56-70` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 44 | `sljit_malloc_exec` | `deleted` | `pcre2/src/sljit/sljitExecAllocator.c` | `269-339` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 45 | `sljit_create_compiler` | `deleted` | `pcre2/src/sljit/sljitLir.c` | `457-542` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 46 | `check_sljit_emit_mem` | `deleted` | `pcre2/src/sljit/sljitLir.c` | `2493-2577` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 47 | `sljit_compiler_get_allocator_data` | `deleted` | `pcre2/src/sljit/sljitLir.h` | `629-629` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 48 | `sljit_compiler_get_user_data` | `deleted` | `pcre2/src/sljit/sljitLir.h` | `632-632` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 49 | `sljit_generate_code` | `deleted` | `pcre2/src/sljit/sljitNativeARM_32.c` | `816-1100` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 50 | `emit_op` | `deleted` | `pcre2/src/sljit/sljitNativeARM_32.c` | `2062-2282` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 51 | `emit_op_imm` | `deleted` | `pcre2/src/sljit/sljitNativeARM_64.c` | `816-1120` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 52 | `sljit_emit_enter` | `deleted` | `pcre2/src/sljit/sljitNativeARM_64.c` | `1210-1383` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 53 | `emit_op_imm` | `deleted` | `pcre2/src/sljit/sljitNativeARM_T2_32.c` | `791-1161` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 54 | `sljit_emit_enter` | `deleted` | `pcre2/src/sljit/sljitNativeARM_T2_32.c` | `1369-1577` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 55 | `emit_single_op` | `deleted` | `pcre2/src/sljit/sljitNativeLOONGARCH_64.c` | `1313-1729` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 56 | `sljit_emit_simd_lane_mov` | `deleted` | `pcre2/src/sljit/sljitNativeLOONGARCH_64.c` | `3270-3409` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 57 | `call_with_args` | `deleted` | `pcre2/src/sljit/sljitNativeMIPS_32.c` | `211-351` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 58 | `load_immediate` | `deleted` | `pcre2/src/sljit/sljitNativeMIPS_64.c` | `46-136` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 59 | `sljit_emit_enter` | `deleted` | `pcre2/src/sljit/sljitNativeMIPS_common.c` | `930-1138` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 60 | `emit_single_op` | `deleted` | `pcre2/src/sljit/sljitNativeMIPS_common.c` | `1695-2253` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 61 | `emit_single_op` | `deleted` | `pcre2/src/sljit/sljitNativePPC_32.c` | `45-320` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 62 | `emit_single_op` | `deleted` | `pcre2/src/sljit/sljitNativePPC_64.c` | `152-505` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 63 | `sljit_emit_op2` | `deleted` | `pcre2/src/sljit/sljitNativePPC_common.c` | `1709-1949` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 64 | `sljit_emit_op_flags` | `deleted` | `pcre2/src/sljit/sljitNativePPC_common.c` | `2639-2791` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 65 | `sljit_emit_fcopy` | `deleted` | `pcre2/src/sljit/sljitNativeRISCV_32.c` | `70-113` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 66 | `load_immediate` | `deleted` | `pcre2/src/sljit/sljitNativeRISCV_64.c` | `27-127` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 67 | `sljit_generate_code` | `deleted` | `pcre2/src/sljit/sljitNativeRISCV_common.c` | `499-635` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 68 | `emit_single_op` | `deleted` | `pcre2/src/sljit/sljitNativeRISCV_common.c` | `1286-1718` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 69 | `sljit_generate_code` | `deleted` | `pcre2/src/sljit/sljitNativeS390X.c` | `1395-1620` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 70 | `sljit_emit_op1` | `deleted` | `pcre2/src/sljit/sljitNativeS390X.c` | `2083-2341` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 71 | `sljit_emit_enter` | `deleted` | `pcre2/src/sljit/sljitNativeX86_32.c` | `313-536` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 72 | `tail_call_with_args` | `deleted` | `pcre2/src/sljit/sljitNativeX86_32.c` | `780-992` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 73 | `emit_x86_instruction` | `deleted` | `pcre2/src/sljit/sljitNativeX86_64.c` | `61-284` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 74 | `sljit_emit_enter` | `deleted` | `pcre2/src/sljit/sljitNativeX86_64.c` | `456-630` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 75 | `sljit_emit_simd_replicate` | `deleted` | `pcre2/src/sljit/sljitNativeX86_common.c` | `3678-3927` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 76 | `sljit_emit_simd_lane_mov` | `deleted` | `pcre2/src/sljit/sljitNativeX86_common.c` | `3929-4262` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 77 | `create_tempfile` | `deleted` | `pcre2/src/sljit/sljitProtExecAllocator.c` | `105-186` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 78 | `sljit_deserialize_compiler` | `deleted` | `pcre2/src/sljit/sljitSerialize.c` | `288-516` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 79 | `sljit_allocate_stack` | `deleted` | `pcre2/src/sljit/sljitUtils.c` | `175-200` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |
| 80 | `sljit_malloc_exec` | `deleted` | `pcre2/src/sljit/sljitWXExecAllocator.c` | `92-127` | `unmatched` | unmatched; level=unmatched; diff_hunks=1; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `main` in `pcre2/maint/utf8.c`

```diff
-      y = y * 16 + tolower(*x) - ((isdigit(*x))? '0' : 'W');
+      y = y * 16 + (tolower(*x) - ((isdigit(*x))? '0' : 'W'));
```

### 2. `compare_opcodes` in `pcre2/src/pcre2_auto_possess.c`

```diff
+uint32_t list[MAX_LIST];
-  /* At the end of a branch, skip to the end of the group. */
+  /* At the end of a branch, skip to the end of the group and process it. */
-      /* Atomic sub-patterns and assertions can always auto-possessify their
-      last iterator except for variable length lookbehinds. However, if the
-      group was entered as a result of checking a previous iterator, this is
-      not possible. */
+      /* Atomic sub-patterns and forward assertions can always auto-possessify
... truncated 51 additional diff lines ...
```

### 3. `PRIV` in `pcre2/src/pcre2_chkdint.c`

```diff
-#ifdef PCRE2_DEBUG
-if (a < 0 || b < 0) abort();
-#endif
+PCRE2_ASSERT(a >= 0 && b >= 0);
```

### 4. `parse_regex` in `pcre2/src/pcre2_compile.c`

```diff
+static int parse_regex(PCRE2_SPTR ptr, uint32_t options, uint32_t xoptions,
+  BOOL *has_lookbehind, compile_block *cb)
+uint32_t class_op_state;
+uint32_t class_mode_state;
+uint32_t *class_start;
+int16_t class_depth_m1 = -1; /* The m1 means minus 1. */
+int16_t class_maxdepth_m1 = -1;
+PCRE2_SPTR class_range_forbid_ptr = NULL;
... truncated 713 additional diff lines ...
```

### 5. `compile_branch` in `pcre2/src/pcre2_compile.c`

```diff
+/* Some opcodes, such as META_SCS_NUMBER or META_SCS_NAME,
+depends on the previous value of offset. */
+      if (code >= cb->start_workspace + cb->workspace_size)
+        {
+        PCRE2_DEBUG_UNREACHABLE();
+        *errorcodeptr = ERR52;  /* Over-ran workspace - internal error */
+        }
+      else
... truncated 816 additional diff lines ...
```

### 6. `compile_optimize_class` in `pcre2/src/pcre2_compile_class.c`

```diff
+static class_ranges *
+compile_optimize_class(uint32_t *start_ptr, uint32_t options,
+  uint32_t xoptions, compile_block *cb)
+{
+class_ranges* cranges;
+uint32_t *ptr;
+uint32_t *buffer;
+uint32_t *dst;
... truncated 229 additional diff lines ...
```

### 7. `PRIV` in `pcre2/src/pcre2_compile_class.c`

```diff
+uint32_t *
+PRIV(compile_class_not_nested)(uint32_t options, uint32_t xoptions,
+  uint32_t *start_ptr, PCRE2_UCHAR **pcode, BOOL negate_class, BOOL* has_bitmap,
+  int *errorcodeptr, compile_block *cb, PCRE2_SIZE *lengthptr)
+{
+uint32_t *pptr = start_ptr;
+PCRE2_UCHAR *code = *pcode;
+BOOL should_flip_negation;
... truncated 774 additional diff lines ...
```

### 8. `pcre2_config` in `pcre2/src/pcre2_config.c`

```diff
-     XSTRING(PCRE2_MAJOR) "." XSTRING(PCRE_MINOR)
-     XSTRING(PCRE2_PRERELEASE) " " XSTRING(PCRE_DATE)
+     XSTRING(PCRE2_MAJOR) "." XSTRING(PCRE2_MINOR)
+     XSTRING(PCRE2_PRERELEASE) " " XSTRING(PCRE2_DATE)
```

### 9. `pcre2_set_optimize` in `pcre2/src/pcre2_context.c`

```diff
+PCRE2_EXP_DEFN int PCRE2_CALL_CONVENTION
+pcre2_set_optimize(pcre2_compile_context *ccontext, uint32_t directive)
+{
+if (ccontext == NULL)
+  return PCRE2_ERROR_NULL;
+
+switch (directive)
+  {
... truncated 24 additional diff lines ...
```

### 10. `pcre2_pattern_convert` in `pcre2/src/pcre2_convert.c`

```diff
-int i, rc;
+int rc;
-for (i = 0; i < 2; i++)
+for (int i = 0; i < 2; i++)
-    *bufflenptr = 0;  /* Error offset */
-    return PCRE2_ERROR_INTERNAL;
+    goto EXIT;
-/* Control should never get here. */
... truncated 5 additional diff lines ...
```

### 11. `internal_dfa_match` in `pcre2/src/pcre2_dfa_match.c`

```diff
-  int forced_fail = 0;
-/* ========================================================================== */
-      /* These cases are never obeyed. This is a fudge that causes a compile-
-      time error if the vectors coptable or poptable, which are indexed by
-      opcode, are not the correct length. It seems to be the only way to do
-      such a check at compile time, as the sizeof() operator does not work
-      in the C preprocessor. */
-
... truncated 74 additional diff lines ...
```

### 12. `pcre2_get_error_message` in `pcre2/src/pcre2_error.c`

```diff
+  message = (const unsigned char *)"\0";  /* Empty message list */
```

### 13. `PRIV` in `pcre2/src/pcre2_find_bracket.c`

```diff
-  This includes negated single high-valued characters. CALLOUT_STR is used for
-  callouts with string arguments. In both cases the length in the table is
+  This includes negated single high-valued characters. ECLASS is used for
+  classes that use set operations internally. CALLOUT_STR is used for
+  callouts with string arguments. In each case the length in the table is
-  if (c == OP_XCLASS) code += GET(code, 1);
-    else if (c == OP_CALLOUT_STR) code += GET(code, 1 + 2*LINK_SIZE);
+  if (c == OP_XCLASS || c == OP_ECLASS) code += GET(code, 1);
... truncated 5 additional diff lines ...
```

### 14. `LLVMFuzzerTestOneInput` in `pcre2/src/pcre2_fuzzsupport.c`

```diff
-    /* Loop for two values a quantifier. Offset i points to brace or comma at the
-    start of the loop.*/
+    /* Loop for two values in a quantifier. Offset i points to brace or comma
+    at the start of the loop. */
-      /* Ignore leading spaces */
+      /* Ignore leading spaces. */
-      /* Scan for a number ending in brace or comma in the first iteration,
+      /* Ignore non-significant leading zeros. */
... truncated 18 additional diff lines ...
```

### 15. `compile_xclass_matchingpath` in `pcre2/src/pcre2_jit_char_inc.h`

```diff
+static void compile_xclass_matchingpath(compiler_common *common, PCRE2_SPTR cc, jump_list **backtracks, sljit_u32 status)
+{
+DEFINE_COMPILER;
+jump_list *found = NULL;
+jump_list *check_result = NULL;
+jump_list **list = (cc[0] & XCL_NOT) == 0 ? &found : backtracks;
+sljit_uw c, charoffset;
+sljit_u32 max = READ_CHAR_MAX, min = 0;
... truncated 721 additional diff lines ...
```

### 16. `compile_char1_matchingpath` in `pcre2/src/pcre2_jit_char_inc.h`

```diff
+static PCRE2_SPTR compile_char1_matchingpath(compiler_common *common, PCRE2_UCHAR type, PCRE2_SPTR cc, jump_list **backtracks, BOOL check_str_ptr)
+{
+DEFINE_COMPILER;
+int length;
+unsigned int c, oc, bit;
+compare_context context;
+struct sljit_jump *jump[3];
+jump_list *end_list;
... truncated 389 additional diff lines ...
```

### 17. `compile_simple_assertion_matchingpath` in `pcre2/src/pcre2_jit_compile.c`

```diff
+static PCRE2_SPTR compile_simple_assertion_matchingpath(compiler_common *common, PCRE2_UCHAR type, PCRE2_SPTR cc, jump_list **backtracks)
+struct sljit_jump *jump[4];
+switch(type)
+  case OP_SOD:
+  if (HAS_VIRTUAL_REGISTERS)
+    {
+    OP1(SLJIT_MOV, TMP1, 0, ARGUMENTS, 0);
+    OP1(SLJIT_MOV, TMP1, 0, SLJIT_MEM1(TMP1), SLJIT_OFFSETOF(jit_arguments, begin));
... truncated 414 additional diff lines ...
```

### 18. `compile_char1_matchingpath` in `pcre2/src/pcre2_jit_compile.c`

```diff
-static PCRE2_SPTR compile_char1_matchingpath(compiler_common *common, PCRE2_UCHAR type, PCRE2_SPTR cc, jump_list **backtracks, BOOL check_str_ptr)
-{
-DEFINE_COMPILER;
-int length;
-unsigned int c, oc, bit;
-compare_context context;
-struct sljit_jump *jump[3];
-jump_list *end_list;
... truncated 328 additional diff lines ...
```

### 19. `FF_FUN` in `pcre2/src/pcre2_jit_neon_inc.h`

```diff
-
+
-vect_t eq = VORRQ(eq1, eq2);
+vect_t eq = VORRQ(eq1, eq2);
-
+
-  eq = VORRQ(eq1, eq2);
+  eq = VORRQ(eq1, eq2);
```

### 20. `fast_forward_char_pair_simd` in `pcre2/src/pcre2_jit_simd_inc.h`

```diff
-sljit_s32 data1_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR0);
-sljit_s32 data2_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR1);
-sljit_s32 cmp1a_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR2);
-sljit_s32 cmp2a_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR3);
-sljit_s32 cmp1b_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR4);
-sljit_s32 cmp2b_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR5);
-sljit_s32 tmp1_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_FR6);
-sljit_s32 tmp2_ind = sljit_get_register_index(SLJIT_FLOAT_REGISTER, SLJIT_TMP_FR0);
... truncated 40 additional diff lines ...
```

### 21. `pcre2_maketables_free` in `pcre2/src/pcre2_maketables.c`

```diff
-  if (gcontext)
-    gcontext->memctl.free((void *)tables, gcontext->memctl.memory_data);
-  else
-    free((void *)tables);
+if (gcontext != NULL)
+  gcontext->memctl.free((void *)tables, gcontext->memctl.memory_data);
+else
+  free((void *)tables);
```

### 22. `match` in `pcre2/src/pcre2_match.c`

```diff
+        /* Corrupted heapframes?. Trigger an assert and return an error */
+        PCRE2_ASSERT(offset != PCRE2_UNSET);
+
+        /* Corrupted heapframes?. Trigger an assert and return an error */
+        PCRE2_ASSERT(offset != PCRE2_UNSET);
+
-          /* Control never gets here */
+          PCRE2_UNREACHABLE(); /* Control never reaches here */
... truncated 510 additional diff lines ...
```

### 23. `pcre2_match_data_create_from_pattern` in `pcre2/src/pcre2_match_data.c`

```diff
-return pcre2_match_data_create(((pcre2_real_code *)code)->top_bracket + 1,
+return pcre2_match_data_create(((const pcre2_real_code *)code)->top_bracket + 1,
```

### 24. `pcre2_callout_enumerate` in `pcre2/src/pcre2_pattern_info.c`

```diff
-pcre2_real_code *re = (pcre2_real_code *)code;
+const pcre2_real_code *re = (const pcre2_real_code *)code;
-cc = (PCRE2_SPTR)((uint8_t *)re + sizeof(pcre2_real_code))
+cc = (PCRE2_SPTR)((const uint8_t *)re + sizeof(pcre2_real_code))
-#if defined SUPPORT_UNICODE || PCRE2_CODE_UNIT_WIDTH != 8
+#ifdef SUPPORT_WIDE_CHARS
+    case OP_ECLASS:
```

### 25. `pcre2_printint` in `pcre2/src/pcre2_printint.c`

```diff
+code = codestart = (PCRE2_SPTR)((uint8_t *)re + re->code_start);
+    case OP_ASSERT_SCS:
+      fprintf(f, " %s Capture ref <", flag);
+    fprintf(f, "] (not)");
+    fprintf(f, "]%s (not)", OP_names[*code]);
+    fprintf(f, " (not)");
+    extra = code[1 + IMM2_SIZE];
+    if (extra != 0) fprintf(f, " 0x%02x", extra);
... truncated 190 additional diff lines ...
```

### 26. `pcre2_serialize_encode` in `pcre2/src/pcre2_serialize.c`

```diff
-  (void)memcpy(dst_bytes, (char *)re, re->blocksize);
-
-  /* Certain fields in the compiled code block are re-set during
-  deserialization. In order to ensure that the serialized data stream is always
-  the same for the same pattern, set them to zero here. We can't assume the
-  copy of the pattern is correctly aligned for accessing the fields as part of
+  (void)memcpy(dst_bytes, (const char *)re, re->blocksize);
+
... truncated 20 additional diff lines ...
```

### 27. `study_char_list` in `pcre2/src/pcre2_study.c`

```diff
+static void
+study_char_list(PCRE2_SPTR code, uint8_t *start_bitmap,
+  const uint8_t *char_lists_end)
+{
+uint32_t type, list_ind;
+uint32_t char_list_add = XCL_CHAR_LIST_LOW_16_ADD;
+uint32_t range_start = ~(uint32_t)0, range_end = 0;
+const uint8_t *next_char;
... truncated 105 additional diff lines ...
```

### 28. `pcre2_substitute` in `pcre2/src/pcre2_substitute.c`

```diff
-int forcecase = 0;
-int forcecasereset = 0;
-#ifdef SUPPORT_UNICODE
-BOOL ucp = (code->overall_options & PCRE2_UCP) != 0;
-#endif
-PCRE2_SPTR repend;
-  pcre2_general_context *gcontext;
-  gcontext = (mcontext == NULL)?
... truncated 134 additional diff lines ...
```

### 29. `pcre2_substring_nametable_scan` in `pcre2/src/pcre2_substring.c`

```diff
-PCRE2_SPTR nametable = (PCRE2_SPTR)((char *)code + sizeof(pcre2_real_code));
+PCRE2_SPTR nametable = (PCRE2_SPTR)((const char *)code + sizeof(pcre2_real_code));
```

### 30. `PRIV` in `pcre2/src/pcre2_xclass.c`

```diff
+PRIV(xclass)(uint32_t c, PCRE2_SPTR data, const uint8_t *char_lists_end, BOOL utf)
+/* Update PRIV(update_classbits) when this function is changed. */
+BOOL not_negated = (*data & XCL_NOT) == 0;
+uint32_t type, max_index, min_index, value;
+const uint8_t *next_char;
+/* Code points < 256 are matched against a bitmap, if one is present. */
+if ((*data++ & XCL_MAP) != 0)
+  if (c < 256)
... truncated 203 additional diff lines ...
```

### 31. `end_of_line` in `pcre2/src/pcre2grep.c`

```diff
-    if (++p >= endptr)
+    if (p == endptr)
-    if (*p == '\n')
+    p++;
+    if (p < endptr && *p == '\n')
-    int extra = 0;
-    int c = *((unsigned char *)p);
-
... truncated 49 additional diff lines ...
```

### 32. `pcre2_regerror` in `pcre2/src/pcre2posix.c`

```diff
-  /* there are 11 charactes between message and offset,
+  /* there are 11 characters between message and offset;
+PCRE2_ASSERT(len > 0 || preg != NULL);
+
```

### 33. `case_transform` in `pcre2/src/pcre2test.c`

```diff
+static BOOL
+case_transform(int to_case, int num_in, int *num_read, int *num_write,
+  uint32_t *c1, uint32_t *c2)
+{
+/* Let's have one character which aborts the substitution. */
+if (*c1 == '!') return FALSE;
+
+/* Default behaviour is to read one character, and write back that same one
... truncated 108 additional diff lines ...
```

### 34. `process_data` in `pcre2/src/pcre2test.c`

```diff
+while (isspace(*p))
+  {
+  p++;
+  len--;
+  }
+  int i = 0;
+  enum force_encoding encoding = FORCE_NONE;
+    i = (int)li;
... truncated 175 additional diff lines ...
```

### 35. `get_map_jit_flag` in `pcre2/src/sljit/allocator_src/sljitExecAllocatorApple.c`

```diff
-static SLJIT_INLINE int get_map_jit_flag(void)
-{
-	size_t page_size;
-	void *ptr;
-	struct utsname name;
-	static int map_jit_flag = -1;
-
-	if (map_jit_flag < 0) {
... truncated 18 additional diff lines ...
```

### 36. `sljit_malloc_exec` in `pcre2/src/sljit/allocator_src/sljitExecAllocatorCore.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_malloc_exec(sljit_uw size)
-{
-	struct block_header *header;
-	struct block_header *next_header;
-	struct free_block *free_block;
-	sljit_uw chunk_size;
-
-#ifdef SLJIT_HAS_CHUNK_HEADER
... truncated 91 additional diff lines ...
```

### 37. `alloc_chunk` in `pcre2/src/sljit/allocator_src/sljitExecAllocatorFreeBSD.c`

```diff
-static SLJIT_INLINE void* alloc_chunk(sljit_uw size)
-{
-	void *retval;
-	int prot = PROT_READ | PROT_WRITE | PROT_EXEC;
-	int flags = MAP_PRIVATE;
-	int fd = -1;
-
-#ifdef PROT_MAX
... truncated 29 additional diff lines ...
```

### 38. `alloc_chunk` in `pcre2/src/sljit/allocator_src/sljitExecAllocatorPosix.c`

```diff
-static SLJIT_INLINE void* alloc_chunk(sljit_uw size)
-{
-	void *retval;
-	int prot = PROT_READ | PROT_WRITE | PROT_EXEC;
-	int flags = MAP_PRIVATE;
-	int fd = -1;
-
-#ifdef PROT_MAX
... truncated 18 additional diff lines ...
```

### 39. `free_chunk` in `pcre2/src/sljit/allocator_src/sljitExecAllocatorWindows.c`

```diff
-static SLJIT_INLINE void free_chunk(void *chunk, sljit_uw size)
-{
-	SLJIT_UNUSED_ARG(size);
-	VirtualFree(chunk, 0, MEM_RELEASE);
-}
```

### 40. `alloc_chunk` in `pcre2/src/sljit/allocator_src/sljitProtExecAllocatorNetBSD.c`

```diff
-static SLJIT_INLINE struct sljit_chunk_header* alloc_chunk(sljit_uw size)
-{
-	struct sljit_chunk_header *retval;
-
-	retval = (struct sljit_chunk_header *)mmap(NULL, size,
-			PROT_READ | PROT_WRITE | PROT_MPROTECT(PROT_EXEC),
-			MAP_ANON | MAP_SHARED, -1, 0);
-
... truncated 17 additional diff lines ...
```

### 41. `create_tempfile` in `pcre2/src/sljit/allocator_src/sljitProtExecAllocatorPosix.c`

```diff
-static SLJIT_INLINE int create_tempfile(void)
-{
-	int fd;
-	char tmp_name[256];
-	size_t tmp_name_len = 0;
-	char *dir;
-	struct stat st;
-#if defined(SLJIT_SINGLE_THREADED) && SLJIT_SINGLE_THREADED
... truncated 69 additional diff lines ...
```

### 42. `sljit_malloc_exec` in `pcre2/src/sljit/allocator_src/sljitWXExecAllocatorPosix.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_malloc_exec(sljit_uw size)
-{
-#if !(defined SLJIT_SINGLE_THREADED && SLJIT_SINGLE_THREADED)
-	static pthread_mutex_t se_lock = PTHREAD_MUTEX_INITIALIZER;
-#endif
-	static int wx_block = -1;
-	int prot = PROT_READ | PROT_WRITE;
-	sljit_uw* ptr;
... truncated 27 additional diff lines ...
```

### 43. `sljit_malloc_exec` in `pcre2/src/sljit/allocator_src/sljitWXExecAllocatorWindows.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_malloc_exec(sljit_uw size)
-{
-	sljit_uw *ptr;
-
-	size += sizeof(sljit_uw);
-	ptr = (sljit_uw*)VirtualAlloc(NULL, size,
-				MEM_COMMIT | MEM_RESERVE, PAGE_READWRITE);
-
... truncated 7 additional diff lines ...
```

### 44. `sljit_malloc_exec` in `pcre2/src/sljit/sljitExecAllocator.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_malloc_exec(sljit_uw size)
-{
-	struct block_header *header;
-	struct block_header *next_header;
-	struct free_block *free_block;
-	sljit_uw chunk_size;
-
-	SLJIT_ALLOCATOR_LOCK();
... truncated 63 additional diff lines ...
```

### 45. `sljit_create_compiler` in `pcre2/src/sljit/sljitLir.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE struct sljit_compiler* sljit_create_compiler(void *allocator_data)
-{
-	struct sljit_compiler *compiler = (struct sljit_compiler*)SLJIT_MALLOC(sizeof(struct sljit_compiler), allocator_data);
-	if (!compiler)
-		return NULL;
-	SLJIT_ZEROMEM(compiler, sizeof(struct sljit_compiler));
-
-	SLJIT_COMPILE_ASSERT(
... truncated 78 additional diff lines ...
```

### 46. `check_sljit_emit_mem` in `pcre2/src/sljit/sljitLir.c`

```diff
-static SLJIT_INLINE CHECK_RETURN_TYPE check_sljit_emit_mem(struct sljit_compiler *compiler, sljit_s32 type,
-	sljit_s32 reg,
-	sljit_s32 mem, sljit_sw memw)
-{
-#if (defined SLJIT_ARGUMENT_CHECKS && SLJIT_ARGUMENT_CHECKS)
-	sljit_s32 allowed_flags;
-#endif /* SLJIT_ARGUMENT_CHECKS */
-
... truncated 77 additional diff lines ...
```

### 47. `sljit_compiler_get_allocator_data` in `pcre2/src/sljit/sljitLir.h`

```diff
-static SLJIT_INLINE void* sljit_compiler_get_allocator_data(struct sljit_compiler *compiler) { return compiler->allocator_data; }
```

### 48. `sljit_compiler_get_user_data` in `pcre2/src/sljit/sljitLir.h`

```diff
-static SLJIT_INLINE void* sljit_compiler_get_user_data(struct sljit_compiler *compiler) { return compiler->user_data; }
```

### 49. `sljit_generate_code` in `pcre2/src/sljit/sljitNativeARM_32.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_generate_code(struct sljit_compiler *compiler, sljit_s32 options, void *exec_allocator_data)
-{
-	struct sljit_memory_fragment *buf;
-	sljit_ins *code;
-	sljit_ins *code_ptr;
-	sljit_ins *buf_ptr;
-	sljit_ins *buf_end;
-	sljit_uw word_count;
... truncated 277 additional diff lines ...
```

### 50. `emit_op` in `pcre2/src/sljit/sljitNativeARM_32.c`

```diff
-static sljit_s32 emit_op(struct sljit_compiler *compiler, sljit_s32 op, sljit_s32 inp_flags,
-	sljit_s32 dst, sljit_sw dstw,
-	sljit_s32 src1, sljit_sw src1w,
-	sljit_s32 src2, sljit_sw src2w)
-{
-	/* src1 is reg or TMP_REG1
-	   src2 is reg, TMP_REG2, or imm
-	   result goes to TMP_REG2, so put result can use TMP_REG1. */
... truncated 213 additional diff lines ...
```

### 51. `emit_op_imm` in `pcre2/src/sljit/sljitNativeARM_64.c`

```diff
-static sljit_s32 emit_op_imm(struct sljit_compiler *compiler, sljit_s32 flags, sljit_s32 dst, sljit_sw arg1, sljit_sw arg2)
-{
-	/* dst must be register, TMP_REG1
-	   arg1 must be register, TMP_REG1, imm
-	   arg2 must be register, TMP_REG2, imm */
-	sljit_ins inv_bits = (flags & INT_OP) ? W_OP : 0;
-	sljit_ins inst_bits;
-	sljit_s32 op = (flags & 0xffff);
... truncated 297 additional diff lines ...
```

### 52. `sljit_emit_enter` in `pcre2/src/sljit/sljitNativeARM_64.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_enter(struct sljit_compiler *compiler,
-	sljit_s32 options, sljit_s32 arg_types, sljit_s32 scratches, sljit_s32 saveds,
-	sljit_s32 fscratches, sljit_s32 fsaveds, sljit_s32 local_size)
-{
-	sljit_s32 prev, fprev, saved_regs_size, i, tmp;
-	sljit_s32 saved_arg_count = SLJIT_KEPT_SAVEDS_COUNT(options);
-	sljit_ins offs;
-
... truncated 166 additional diff lines ...
```

### 53. `emit_op_imm` in `pcre2/src/sljit/sljitNativeARM_T2_32.c`

```diff
-static sljit_s32 emit_op_imm(struct sljit_compiler *compiler, sljit_s32 flags, sljit_s32 dst, sljit_uw arg1, sljit_uw arg2)
-{
-	/* dst must be register
-	   arg1 must be register, imm
-	   arg2 must be register, imm */
-	sljit_s32 reg;
-	sljit_uw imm, imm2;
-
... truncated 363 additional diff lines ...
```

### 54. `sljit_emit_enter` in `pcre2/src/sljit/sljitNativeARM_T2_32.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_enter(struct sljit_compiler *compiler,
-	sljit_s32 options, sljit_s32 arg_types, sljit_s32 scratches, sljit_s32 saveds,
-	sljit_s32 fscratches, sljit_s32 fsaveds, sljit_s32 local_size)
-{
-	sljit_s32 size, i, tmp, word_arg_count;
-	sljit_s32 saved_arg_count = SLJIT_KEPT_SAVEDS_COUNT(options);
-	sljit_uw offset;
-	sljit_uw imm = 0;
... truncated 201 additional diff lines ...
```

### 55. `emit_single_op` in `pcre2/src/sljit/sljitNativeLOONGARCH_64.c`

```diff
-static SLJIT_INLINE sljit_s32 emit_single_op(struct sljit_compiler *compiler, sljit_s32 op, sljit_s32 flags,
-	sljit_s32 dst, sljit_s32 src1, sljit_sw src2)
-{
-	sljit_s32 is_overflow, is_carry, carry_src_r, is_handled, reg;
-	sljit_ins op_imm, op_reg;
-	sljit_ins word_size = ((op & SLJIT_32) ? 32 : 64);
-
-	switch (GET_OPCODE(op)) {
... truncated 409 additional diff lines ...
```

### 56. `sljit_emit_simd_lane_mov` in `pcre2/src/sljit/sljitNativeLOONGARCH_64.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_simd_lane_mov(struct sljit_compiler *compiler, sljit_s32 type,
-	sljit_s32 freg, sljit_s32 lane_index,
-	sljit_s32 srcdst, sljit_sw srcdstw)
-{
-	sljit_s32 reg_size = SLJIT_SIMD_GET_REG_SIZE(type);
-	sljit_s32 elem_size = SLJIT_SIMD_GET_ELEM_SIZE(type);
-	sljit_ins ins = 0;
-
... truncated 132 additional diff lines ...
```

### 57. `call_with_args` in `pcre2/src/sljit/sljitNativeMIPS_32.c`

```diff
-static sljit_s32 call_with_args(struct sljit_compiler *compiler, sljit_s32 arg_types, sljit_ins *ins_ptr, sljit_u32 *extra_space)
-{
-	sljit_u32 is_tail_call = *extra_space & SLJIT_CALL_RETURN;
-	sljit_u32 offset = 0;
-	sljit_s32 float_arg_count = 0;
-	sljit_s32 word_arg_count = 0;
-	sljit_s32 types = 0;
-	sljit_ins prev_ins = NOP;
... truncated 133 additional diff lines ...
```

### 58. `load_immediate` in `pcre2/src/sljit/sljitNativeMIPS_64.c`

```diff
-static sljit_s32 load_immediate(struct sljit_compiler *compiler, sljit_s32 dst_ar, sljit_sw imm)
-{
-	sljit_s32 shift = 32;
-	sljit_s32 shift2;
-	sljit_s32 inv = 0;
-	sljit_ins ins;
-	sljit_uw uimm;
-
... truncated 83 additional diff lines ...
```

### 59. `sljit_emit_enter` in `pcre2/src/sljit/sljitNativeMIPS_common.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_enter(struct sljit_compiler *compiler,
-	sljit_s32 options, sljit_s32 arg_types, sljit_s32 scratches, sljit_s32 saveds,
-	sljit_s32 fscratches, sljit_s32 fsaveds, sljit_s32 local_size)
-{
-	sljit_ins base;
-	sljit_s32 i, tmp, offset;
-	sljit_s32 arg_count, word_arg_count, float_arg_count;
-	sljit_s32 saved_arg_count = SLJIT_KEPT_SAVEDS_COUNT(options);
... truncated 201 additional diff lines ...
```

### 60. `emit_single_op` in `pcre2/src/sljit/sljitNativeMIPS_common.c`

```diff
-static SLJIT_INLINE sljit_s32 emit_single_op(struct sljit_compiler *compiler, sljit_s32 op, sljit_s32 flags,
-	sljit_s32 dst, sljit_s32 src1, sljit_sw src2)
-{
-	sljit_s32 is_overflow, is_carry, carry_src_ar, is_handled, reg;
-	sljit_ins op_imm, op_v;
-#if (defined SLJIT_CONFIG_MIPS_64 && SLJIT_CONFIG_MIPS_64)
-	sljit_ins ins, op_dimm, op_dimm32, op_dv;
-#endif
... truncated 551 additional diff lines ...
```

### 61. `emit_single_op` in `pcre2/src/sljit/sljitNativePPC_32.c`

```diff
-static SLJIT_INLINE sljit_s32 emit_single_op(struct sljit_compiler *compiler, sljit_s32 op, sljit_s32 flags,
-	sljit_s32 dst, sljit_s32 src1, sljit_s32 src2)
-{
-	sljit_u32 imm;
-
-	switch (op) {
-	case SLJIT_MOV:
-	case SLJIT_MOV_U32:
... truncated 268 additional diff lines ...
```

### 62. `emit_single_op` in `pcre2/src/sljit/sljitNativePPC_64.c`

```diff
-static SLJIT_INLINE sljit_s32 emit_single_op(struct sljit_compiler *compiler, sljit_s32 op, sljit_s32 flags,
-	sljit_s32 dst, sljit_s32 src1, sljit_s32 src2)
-{
-	sljit_u32 imm;
-
-	switch (op) {
-	case SLJIT_MOV:
-	case SLJIT_MOV_P:
... truncated 346 additional diff lines ...
```

### 63. `sljit_emit_op2` in `pcre2/src/sljit/sljitNativePPC_common.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_op2(struct sljit_compiler *compiler, sljit_s32 op,
-	sljit_s32 dst, sljit_sw dstw,
-	sljit_s32 src1, sljit_sw src1w,
-	sljit_s32 src2, sljit_sw src2w)
-{
-	sljit_s32 flags = HAS_FLAGS(op) ? ALT_SET_FLAGS : 0;
-
-	CHECK_ERROR();
... truncated 233 additional diff lines ...
```

### 64. `sljit_emit_op_flags` in `pcre2/src/sljit/sljitNativePPC_common.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_op_flags(struct sljit_compiler *compiler, sljit_s32 op,
-	sljit_s32 dst, sljit_sw dstw,
-	sljit_s32 type)
-{
-	sljit_s32 reg, invert;
-	sljit_u32 bit, from_xer;
-	sljit_s32 saved_op = op;
-	sljit_sw saved_dstw = dstw;
... truncated 145 additional diff lines ...
```

### 65. `sljit_emit_fcopy` in `pcre2/src/sljit/sljitNativeRISCV_32.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_fcopy(struct sljit_compiler *compiler, sljit_s32 op,
-	sljit_s32 freg, sljit_s32 reg)
-{
-	sljit_ins inst;
-	sljit_s32 reg2 = 0;
-
-	CHECK_ERROR();
-	CHECK(check_sljit_emit_fcopy(compiler, op, freg, reg));
... truncated 36 additional diff lines ...
```

### 66. `load_immediate` in `pcre2/src/sljit/sljitNativeRISCV_64.c`

```diff
-static sljit_s32 load_immediate(struct sljit_compiler *compiler, sljit_s32 dst_r, sljit_sw imm, sljit_s32 tmp_r)
-{
-	sljit_sw high;
-
-	if (imm <= SIMM_MAX && imm >= SIMM_MIN)
-		return push_inst(compiler, ADDI | RD(dst_r) | RS1(TMP_ZERO) | IMM_I(imm));
-
-	if (imm <= 0x7fffffffl && imm >= S32_MIN) {
... truncated 93 additional diff lines ...
```

### 67. `sljit_generate_code` in `pcre2/src/sljit/sljitNativeRISCV_common.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_generate_code(struct sljit_compiler *compiler, sljit_s32 options, void *exec_allocator_data)
-{
-	struct sljit_memory_fragment *buf;
-	sljit_ins *code;
-	sljit_ins *code_ptr;
-	sljit_ins *buf_ptr;
-	sljit_ins *buf_end;
-	sljit_uw word_count;
... truncated 129 additional diff lines ...
```

### 68. `emit_single_op` in `pcre2/src/sljit/sljitNativeRISCV_common.c`

```diff
-static SLJIT_INLINE sljit_s32 emit_single_op(struct sljit_compiler *compiler, sljit_s32 op, sljit_s32 flags,
-	sljit_s32 dst, sljit_s32 src1, sljit_sw src2)
-{
-	sljit_s32 is_overflow, is_carry, carry_src_r, is_handled, reg;
-	sljit_ins op_imm, op_reg;
-#if (defined SLJIT_CONFIG_RISCV_64 && SLJIT_CONFIG_RISCV_64)
-	sljit_ins word = (sljit_ins)(op & SLJIT_32) >> 5;
-#endif /* SLJIT_CONFIG_RISCV_64 */
... truncated 425 additional diff lines ...
```

### 69. `sljit_generate_code` in `pcre2/src/sljit/sljitNativeS390X.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_generate_code(struct sljit_compiler *compiler, sljit_s32 options, void *exec_allocator_data)
-{
-	struct sljit_label *label;
-	struct sljit_jump *jump;
-	struct sljit_const *const_;
-	sljit_sw executable_offset;
-	sljit_uw ins_size = compiler->size << 1;
-	sljit_uw pool_size = 0; /* literal pool */
... truncated 218 additional diff lines ...
```

### 70. `sljit_emit_op1` in `pcre2/src/sljit/sljitNativeS390X.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_op1(struct sljit_compiler *compiler, sljit_s32 op,
-	sljit_s32 dst, sljit_sw dstw,
-	sljit_s32 src, sljit_sw srcw)
-{
-	sljit_ins ins;
-	struct addr mem;
-	sljit_gpr dst_r;
-	sljit_gpr src_r;
... truncated 251 additional diff lines ...
```

### 71. `sljit_emit_enter` in `pcre2/src/sljit/sljitNativeX86_32.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_enter(struct sljit_compiler *compiler,
-	sljit_s32 options, sljit_s32 arg_types, sljit_s32 scratches, sljit_s32 saveds,
-	sljit_s32 fscratches, sljit_s32 fsaveds, sljit_s32 local_size)
-{
-	sljit_s32 word_arg_count, saved_arg_count, float_arg_count;
-	sljit_s32 size, args_size, types, status;
-	sljit_s32 kept_saveds_count = SLJIT_KEPT_SAVEDS_COUNT(options);
-	sljit_u8 *inst;
... truncated 216 additional diff lines ...
```

### 72. `tail_call_with_args` in `pcre2/src/sljit/sljitNativeX86_32.c`

```diff
-static sljit_s32 tail_call_with_args(struct sljit_compiler *compiler,
-	sljit_s32 *extra_space, sljit_s32 arg_types,
-	sljit_s32 src, sljit_sw srcw)
-{
-	sljit_sw args_size, saved_regs_size;
-	sljit_sw types, word_arg_count, float_arg_count;
-	sljit_sw stack_size, prev_stack_size, min_size, offset;
-	sljit_sw word_arg4_offset;
... truncated 205 additional diff lines ...
```

### 73. `emit_x86_instruction` in `pcre2/src/sljit/sljitNativeX86_64.c`

```diff
-static sljit_u8* emit_x86_instruction(struct sljit_compiler *compiler, sljit_uw size,
-	/* The register or immediate operand. */
-	sljit_s32 a, sljit_sw imma,
-	/* The general operand (not immediate). */
-	sljit_s32 b, sljit_sw immb)
-{
-	sljit_u8 *inst;
-	sljit_u8 *buf_ptr;
... truncated 216 additional diff lines ...
```

### 74. `sljit_emit_enter` in `pcre2/src/sljit/sljitNativeX86_64.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_enter(struct sljit_compiler *compiler,
-	sljit_s32 options, sljit_s32 arg_types, sljit_s32 scratches, sljit_s32 saveds,
-	sljit_s32 fscratches, sljit_s32 fsaveds, sljit_s32 local_size)
-{
-	sljit_uw size;
-	sljit_s32 word_arg_count = 0;
-	sljit_s32 saved_arg_count = SLJIT_KEPT_SAVEDS_COUNT(options);
-	sljit_s32 saved_regs_size, tmp, i;
... truncated 167 additional diff lines ...
```

### 75. `sljit_emit_simd_replicate` in `pcre2/src/sljit/sljitNativeX86_common.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_simd_replicate(struct sljit_compiler *compiler, sljit_s32 type,
-	sljit_s32 freg,
-	sljit_s32 src, sljit_sw srcw)
-{
-	sljit_s32 reg_size = SLJIT_SIMD_GET_REG_SIZE(type);
-	sljit_s32 elem_size = SLJIT_SIMD_GET_ELEM_SIZE(type);
-	sljit_s32 use_vex = (cpu_feature_list & CPU_FEATURE_AVX) && (compiler->options & SLJIT_ENTER_USE_VEX);
-	sljit_u8 *inst;
... truncated 242 additional diff lines ...
```

### 76. `sljit_emit_simd_lane_mov` in `pcre2/src/sljit/sljitNativeX86_common.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE sljit_s32 sljit_emit_simd_lane_mov(struct sljit_compiler *compiler, sljit_s32 type,
-	sljit_s32 freg, sljit_s32 lane_index,
-	sljit_s32 srcdst, sljit_sw srcdstw)
-{
-	sljit_s32 reg_size = SLJIT_SIMD_GET_REG_SIZE(type);
-	sljit_s32 elem_size = SLJIT_SIMD_GET_ELEM_SIZE(type);
-	sljit_s32 use_vex = (cpu_feature_list & CPU_FEATURE_AVX) && (compiler->options & SLJIT_ENTER_USE_VEX);
-	sljit_u8 *inst;
... truncated 326 additional diff lines ...
```

### 77. `create_tempfile` in `pcre2/src/sljit/sljitProtExecAllocator.c`

```diff
-static SLJIT_INLINE int create_tempfile(void)
-{
-	int fd;
-	char tmp_name[256];
-	size_t tmp_name_len = 0;
-	char *dir;
-	struct stat st;
-#if defined(SLJIT_SINGLE_THREADED) && SLJIT_SINGLE_THREADED
... truncated 74 additional diff lines ...
```

### 78. `sljit_deserialize_compiler` in `pcre2/src/sljit/sljitSerialize.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE struct sljit_compiler *sljit_deserialize_compiler(sljit_uw* buffer, sljit_uw size,
-	sljit_s32 options, void *allocator_data)
-{
-	struct sljit_compiler *compiler;
-	struct sljit_serialized_compiler *serialized_compiler;
-	struct sljit_serialized_label *serialized_label;
-	struct sljit_serialized_jump *serialized_jump;
-	struct sljit_serialized_const *serialized_const;
... truncated 221 additional diff lines ...
```

### 79. `sljit_allocate_stack` in `pcre2/src/sljit/sljitUtils.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE struct sljit_stack* SLJIT_FUNC sljit_allocate_stack(sljit_uw start_size, sljit_uw max_size, void *allocator_data)
-{
-	struct sljit_stack *stack;
-	void *ptr;
-
-	SLJIT_UNUSED_ARG(allocator_data);
-
-	if (start_size > max_size || start_size < 1)
... truncated 18 additional diff lines ...
```

### 80. `sljit_malloc_exec` in `pcre2/src/sljit/sljitWXExecAllocator.c`

```diff
-SLJIT_API_FUNC_ATTRIBUTE void* sljit_malloc_exec(sljit_uw size)
-{
-#if !(defined SLJIT_SINGLE_THREADED && SLJIT_SINGLE_THREADED) \
-	&& !defined(__NetBSD__)
-	static pthread_mutex_t se_lock = PTHREAD_MUTEX_INITIALIZER;
-#endif
-	static int se_protected = !SLJIT_PROT_WX;
-	int prot = PROT_READ | PROT_WRITE | SLJIT_PROT_WX;
... truncated 28 additional diff lines ...
```

## Mock Release-Note Drafts

- No mock release-note output available.

## Ground-Truth Drafting Workspace

| GT ID | Section | Semantic Release-Note Entry | Supporting Evidence | Decision |
| --- | --- | --- | --- | --- |
| GT-001 |  |  |  | pending |

## Excluded Or Low-Level Changes

| Item | Reason For Exclusion | Evidence |
| --- | --- | --- |
|  |  |  |

## Reviewer Notes

- Record uncertainty, alternative interpretations, and final consensus here.

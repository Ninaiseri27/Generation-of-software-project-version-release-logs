# Evidence Pack: third_party_cJSON OpenHarmony-v6.0-Beta1 -> OpenHarmony-v6.0-Release

This file is an evidence packet for ground-truth drafting. It is not the reviewed ground truth.

## Case Overview

- Case ID: `cjson_v6_0_beta1_to_v6_0`
- Repository: `third_party_cJSON`
- Category: `json_parser`
- Reference version: `OpenHarmony-v6.0-Beta1`
- Target version: `OpenHarmony-v6.0-Release`
- Pipeline status: `verified_full_pipeline_mock`
- Ground-truth status: `draft_required`

## Evidence Sources To Inspect

- [ ] commit_messages
- [ ] function_level_diff
- [ ] test changes
- [ ] component changelog or upstream issue references if available

## Local Artifacts

- Changed functions: `outputs/benchmark/third_party_cJSON/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/changed_functions.json`
- cmg_output: `outputs/benchmark/third_party_cJSON/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/cmg.json`
- mock_baselines: `outputs/benchmark/third_party_cJSON/OpenHarmony-v6.0-Beta1__OpenHarmony-v6.0-Release/baselines`

## Pipeline Summary

- Commit count: `14`
- Changed C/C++ files: `5`
- Changed functions: `11`
- Patch only: `False`
- CMG matched entries: `11`
- CMG unmatched entries: `0`
- Fallback-context entries: `11`
- Diff-derived call edges: `17`
- Prompt entries: `11`
- Mock generated entries: `11`

## Commit Messages

- !104 Added max recusrion depth for cJSONDuplicate to prevent stack exhausti… Merge pull request !104 from liukaii/gitee0619
- Added max recusrion depth for cJSONDuplicate to prevent stack exhaustion in case of circular reference
- !103 cjson gn文件整改 Merge pull request !103 from liukaii/gitee0617
- cJSON GN文件整改
- !100 tdd add Merge pull request !100 from liuyuxiu/master
- tdd add
- !99 add tdd Merge pull request !99 from liuyuxiu/master
- add tdd
- !98 bug fix  53154 Merge pull request !98 from liuyuxiu/master
- update tests/parse_examples.c.
- bugfix
- bug fix
- !97 revert bugfix Merge pull request !97 from liuyuxiu/master
- revert bugfix

## Changed C/C++ Files

- `cJSON.c`
- `cJSON.h`
- `tests/misc_tests.c`
- `tests/parse_examples.c`
- `tests/parse_number.c`

## Changed Function Evidence

| # | Symbol | Type | File | Lines | Match | Evidence Notes |
| ---: | --- | --- | --- | --- | --- | --- |
| 1 | `parse_number` | `modified` | `cJSON.c` | `311-412` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 2 | `cJSON_Duplicate` | `modified` | `cJSON.c` | `2756-2759` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 3 | `cJSON_Duplicate_rec` | `added` | `cJSON.c` | `2761-2845` | `matched` | matched; level=path+symbol; diff_hunks=2; fallback_calls=0 |
| 4 | `cjson_should_not_follow_too_deep_circular_references` | `added` | `tests/misc_tests.c` | `222-237` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 5 | `cjson_set_bool_value_must_not_break_objects` | `modified` | `tests/misc_tests.c` | `693-749` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 6 | `cjson_parse_big_numbers_should_not_report_error` | `added` | `tests/misc_tests.c` | `751-765` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 7 | `main` | `modified` | `tests/misc_tests.c` | `767-801` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 8 | `test15_should_not_heap_buffer_overflow` | `added` | `tests/parse_examples.c` | `254-278` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 9 | `main` | `modified` | `tests/parse_examples.c` | `280-299` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 10 | `a` | `deleted` | `tests/parse_number.c` | `111-116` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |
| 11 | `parse_number_should_parse_big_numbers` | `added` | `tests/parse_number.c` | `111-116` | `matched` | matched; level=path+symbol; diff_hunks=1; fallback_calls=0 |

## Function-Level Diff Snippets

### 1. `parse_number` in `cJSON.c`

```diff
-    number_c_string[i] = '\0';
```

### 2. `cJSON_Duplicate` in `cJSON.c`

```diff
+{
+    return cJSON_Duplicate_rec(item, 0, recurse );
+}
```

### 3. `cJSON_Duplicate_rec` in `cJSON.c`

```diff
+cJSON * cJSON_Duplicate_rec(const cJSON *item, size_t depth, cJSON_bool recurse)
+        if(depth >= CJSON_CIRCULAR_LIMIT) {
+            goto fail;
+        }
+        newchild = cJSON_Duplicate_rec(child, depth + 1, true); /* Duplicate (with recurse) each item in the ->next chain */
```

### 4. `cjson_should_not_follow_too_deep_circular_references` in `tests/misc_tests.c`

```diff
+static void cjson_should_not_follow_too_deep_circular_references(void)
+{
+    cJSON *o = cJSON_CreateArray();
+    cJSON *a = cJSON_CreateArray();
+    cJSON *b = cJSON_CreateArray();
+    cJSON *x;
+
+    cJSON_AddItemToArray(o, a);
+    cJSON_AddItemToArray(a, b);
+    cJSON_AddItemToArray(b, o);
+
+    x = cJSON_Duplicate(o, 1);
... truncated 4 additional diff lines ...
```

### 5. `cjson_set_bool_value_must_not_break_objects` in `tests/misc_tests.c`

```diff
+}
```

### 6. `cjson_parse_big_numbers_should_not_report_error` in `tests/misc_tests.c`

```diff
+static void cjson_parse_big_numbers_should_not_report_error(void)
+{
+    cJSON *valid_big_number_json_object1 = cJSON_Parse("{\"a\": true, \"b\": [ null,9999999999999999999999999999999999999999999999912345678901234567]}");
+    cJSON *valid_big_number_json_object2 = cJSON_Parse("{\"a\": true, \"b\": [ null,999999999999999999999999999999999999999999999991234567890.1234567E3]}");
+    const char *invalid_big_number_json1 = "{\"a\": true, \"b\": [ null,99999999999999999999999999999999999999999999999.1234567890.1234567]}";
+    const char *invalid_big_number_json2 = "{\"a\": true, \"b\": [ null,99999999999999999999999999999999999999999999999E1234567890e1234567]}";
+
+    TEST_ASSERT_NOT_NULL(valid_big_number_json_object1);
+    TEST_ASSERT_NOT_NULL(valid_big_number_json_object2);
+    TEST_ASSERT_NULL_MESSAGE(cJSON_Parse(invalid_big_number_json1), "Invalid big number JSONs should not be parsed.");
+    TEST_ASSERT_NULL_MESSAGE(cJSON_Parse(invalid_big_number_json2), "Invalid big number JSONs should not be parsed.");
+
```

### 7. `main` in `tests/misc_tests.c`

```diff
+    RUN_TEST(cjson_should_not_follow_too_deep_circular_references);
```

### 8. `test15_should_not_heap_buffer_overflow` in `tests/parse_examples.c`

```diff
+static void test15_should_not_heap_buffer_overflow(void)
+{
+    const char *strings[] = {
+        "{\"1\":1,",
+        "{\"1\":1, ",
+    };
+
+    size_t i;
+
+    for (i = 0; i < sizeof(strings) / sizeof(strings[0]); i+=1)
+    {
+        const char *json_string = strings[i];
... truncated 13 additional diff lines ...
```

### 9. `main` in `tests/parse_examples.c`

```diff
+    RUN_TEST(test15_should_not_heap_buffer_overflow);
```

### 10. `a` in `tests/parse_number.c`

```diff
-static void a(void)
```

### 11. `parse_number_should_parse_big_numbers` in `tests/parse_number.c`

```diff
+static void parse_number_should_parse_big_numbers(void)
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

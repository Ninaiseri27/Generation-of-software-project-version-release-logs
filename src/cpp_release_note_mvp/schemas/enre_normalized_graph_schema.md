# ENRE Normalized Graph Schema

This schema defines the stable internal graph contract produced by `pipeline/enre_parser.py`.

## Purpose

The raw ENRE-CPP JSON is suitable for tool output capture, but it is not ideal as a downstream contract for:

- changed-function to entity matching
- CMG construction
- prompt building
- statistics and debugging

This normalized schema provides one consistent representation regardless of later changes to the ENRE runner or raw-output format.

The schema intentionally separates two graph views:

- `entities` and `relations` are the compact prompt graph. They keep only function-like entities and `call` edges.
- `matching_entities` and `matching_relations` are the richer matching graph. They are used only to improve changed-symbol matching and debugging, not injected directly into prompts.

## Input Assumption

The parser accepts either:

1. the official ENRE single-item list payload
2. a direct object with `variables` and `relations`

## Normalization Rules

1. Only function-like entities are retained in the compact prompt graph.
   - retained kinds currently include:
     - `function`
     - `method`
     - `constructor`
     - `destructor`

2. Entity `entityType` values are converted to lowercase snake case.
   - Example: `Parameter Variable` -> `parameter_variable`

3. Only `call` relations are retained in the compact prompt graph.

4. Relation `type` values are converted to lowercase snake case.
   - Example: `Call` and `call` both become `call`

5. Paths are normalized to forward slashes.

6. `-1` values in line, column, scale, and parent fields become `null`.

7. One normalized entity is produced for each retained raw ENRE function-like entity.

8. An `is_user_defined` flag is attached to each retained entity.
   - current heuristic:
     - implementation files such as `.c/.cc/.cpp/.cxx` -> `true`
     - header files and unknown paths -> `false`
   - this is a pragmatic engineering heuristic for CMG construction, not a semantic ground truth label
   - function-like entities with `is_user_defined == false` are still retained so later CMG logic can choose whether to keep them as external leaf context or prune them

9. Relations are deduplicated by:
   - `(normalized_type, source_id, target_id)`

10. Deduplicated relations retain:
   - `occurrence_count`
   - `raw_types`

11. Relations whose `source_id` or `target_id` do not resolve to a retained function-like entity are dropped and counted in `summary.dropped_relation_count`.

12. A richer matching graph is emitted separately.
   - retained matching entity kinds currently include function-like kinds plus class/struct/template/namespace/macro/file/enum-like kinds
   - matching relations keep every normalized relation type whose endpoints resolve to retained matching entities
   - downstream CMG construction may use this richer graph to map a changed symbol back to a prompt-graph function node, but prompt construction should continue to use the compact graph

## Top-Level JSON Shape

```json
{
  "source": {
    "parser": "enre-normalizer-v2",
    "input_path": "string or null"
  },
  "summary": {
    "raw_entity_count": 0,
    "normalized_entity_count": 0,
    "dropped_entity_count": 0,
    "raw_relation_count": 0,
    "normalized_relation_count": 0,
    "dropped_relation_count": 0,
    "deduplicated_relation_count": 0,
    "function_like_entity_count": 0,
    "call_relation_count": 0,
    "user_defined_function_count": 0,
    "matching_entity_count": 0,
    "matching_relation_count": 0,
    "matching_entity_kind_counts": {
      "function": 0,
      "macro": 0
    },
    "matching_relation_type_counts": {
      "call": 0,
      "define": 0
    },
    "raw_entity_kind_counts": {
      "function": 0
    },
    "raw_relation_type_counts": {
      "call": 0
    },
    "entity_kind_counts": {
      "function": 0
    },
    "relation_type_counts": {
      "call": 0
    }
  },
  "entities": [
    {
      "id": 0,
      "name": "sqlite3_libversion",
      "qualified_name": "sqlite3_libversion",
      "kind": "function",
      "raw_kind": "Function",
      "is_user_defined": true,
      "file_path": "src/sqlite3.c",
      "start_line": 499,
      "end_line": 499,
      "start_column": 19984,
      "end_column": 19984,
      "parent_id": 7472,
      "parent_qualified_name": "sqlite3",
      "raw_scale": null
    }
  ],
  "relations": [
    {
      "type": "call",
      "source_id": 7097,
      "target_id": 491,
      "occurrence_count": 1,
      "raw_types": ["Call"]
    }
  ],
  "matching_entities": [
    {
      "id": 0,
      "name": "TEST_CASE",
      "qualified_name": "TEST_CASE",
      "kind": "macro",
      "raw_kind": "Macro",
      "is_user_defined": true,
      "file_path": "test/demo.cpp",
      "start_line": 100,
      "end_line": 100,
      "start_column": null,
      "end_column": null,
      "parent_id": 42,
      "parent_qualified_name": "DemoTest::TestBody",
      "raw_scale": null
    }
  ],
  "matching_relations": [
    {
      "type": "define",
      "source_id": 42,
      "target_id": 0,
      "occurrence_count": 1,
      "raw_types": ["Define"]
    }
  ]
}
```

## Entity Fields

- `id`
  - raw ENRE entity id

- `name`
  - simple display name derived from `qualified_name`
  - for file entities, uses the basename

- `qualified_name`
  - raw ENRE qualified name

- `kind`
  - normalized entity kind

- `raw_kind`
  - original ENRE entity type

- `is_user_defined`
  - heuristic flag for later CMG pruning

- `file_path`
  - source-relative path when available

- `start_line`, `end_line`, `start_column`, `end_column`
  - normalized source location metadata

- `parent_id`
  - normalized parent entity id

- `parent_qualified_name`
  - convenience field for later matching and debugging

- `raw_scale`
  - currently passed through from ENRE when available

## Relation Fields

- `type`
  - normalized relation type

- `source_id`
  - source entity id

- `target_id`
  - target entity id

- `occurrence_count`
  - how many raw relations collapsed into this normalized edge

- `raw_types`
  - original ENRE relation labels that contributed to this edge

## Intended Downstream Usage

Stage 2 downstream modules should use:

- `entities` for id-to-symbol lookup
- `relations` filtered by `type == "call"` for call graph traversal
- `summary` for quick sanity checks and debug output
- `is_user_defined` for later CMG pruning decisions

Downstream logic should not depend directly on the raw ENRE JSON shape once this schema is available.

When `cmg.matching_view = rich`, `CmgBuilder` may consult `matching_entities` and `matching_relations` first and then project any matching-only entity back to a function-like prompt node through same id, parent id, relation bridge, or nearby file/line evidence. This is designed to improve matching coverage without expanding the prompt graph.

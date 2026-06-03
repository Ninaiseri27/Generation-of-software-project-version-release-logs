# Unified Ground-Truth Protocol

Last updated: 2026-05-28

This document defines the single ground-truth protocol used by all benchmark
cases in the thesis. It replaces wording that implied separate GT protocols for
core, extension, and stress cases.

## Core Decision

All GT entries use one protocol:

- one semantic release-note entry definition;
- one evidence admission standard;
- one exclusion standard;
- one strict generated-entry matching rule;
- one metric definition.

The project may still use separate interim tables while generation coverage
differs. For final quantitative comparison, however, an added case should be
treated the same way as the original 17-entry core set: it needs the required
method outputs, strict matches, and evaluation files before it is averaged into
an all-method result table. This is a method-coverage gate, not a separate GT
protocol.

## GT Entry Definition

A GT entry is a human-reviewed semantic release-note fact for one version pair.
It is not a single commit, not a single function, and not a generated sentence.

One GT entry may be supported by multiple commits, changed functions,
release-note bullets, or diff hunks when they implement the same
release-note-level behavior.

## Evidence Admission Standard

An entry can be admitted only when it satisfies all conditions below:

- It is user-visible or developer-visible.
- It is supported by at least one reliable high-level evidence source, such as official release notes, upstream changelog, advisory, or reviewed component notes; if high-level notes are incomplete, reviewed commits and source diffs may be used together.
- It has source-level evidence, such as changed functions, commits, patch files, or inspected diff snippets.
- It can be written as a concise release-note fact rather than a low-level implementation trace.

## Exclusion Standard

Exclude changes from strict GT when they are only:

- test scaffolding;
- spelling or comment updates;
- pure refactoring without behavior, API, compatibility, reliability, security, performance, or diagnostics impact;
- build, CI, formatting, or dependency metadata changes with no release-note-level meaning;
- generated output unsupported by evidence.

Some excluded changes may be mentioned qualitatively as implementation or
diagnostic notes, but they do not enter P/R/F1 computation.

## Strict Matching Rule

Generated entries are matched to GT entries by semantic correspondence.

Accept a match only when the generated entry states the same release-note-level
fact as the GT entry. It does not need identical wording.

Reject a match when the generated entry only mentions:

- a helper function;
- a test case;
- a file-local implementation detail;
- an unsupported security or CVE claim;
- a broad statement that does not identify the GT behavior.

## Reporting Scope

Use one GT protocol, but report results according to experiment coverage:

| Scope | Meaning | Reporting Rule |
| --- | --- | --- |
| Core matrix | Cases with full comparable generation and strict matches for the main variants and ablations. | Can be averaged as the main controlled table. |
| Extension matrix | Cases with the same GT protocol and, during development, partial selected variants. | Interim reporting only. For the final matrix, complete all required variants before averaging. |
| Sampled scope | Cases where the changed-function set is sampled before GT construction due to scale. | GT entries still use the same protocol; the sampling scope must be stated, and all required variants must be run for final quantitative comparison. |
| Inventory | All reviewed GT entries across the project. | Use for dataset-size reporting only until all required outputs and strict matches exist. |

## Thesis Wording

Recommended wording:

> 本文所有 GT 条目均采用统一的语义级发布日志事实定义、证据准入标准和严格匹配规则。core、extension 和 sampled scope 仅表示用例来源、规模和采样范围不同，不表示采用了不同的 GT 判定协议。最终进入定量主实验的用例均需完成相同方法变体下的生成、严格匹配和指标计算。

Avoid saying:

- "core and extension use different GT protocols";
- "sampled cases use a different matching protocol";
- "82 entries are averaged directly across all methods" unless all corresponding generated outputs and strict matches exist;
- "extension cases are only supplementary" after they have been selected into the final matrix and their full method coverage is complete.

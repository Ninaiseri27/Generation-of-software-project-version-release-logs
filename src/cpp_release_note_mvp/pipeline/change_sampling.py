from __future__ import annotations

from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class SampledItem:
    item: dict[str, Any]
    file_path: str
    change_type: str
    diff_line_count: int
    hunk_count: int
    score: int


class ChangedFunctionSampler:
    """Build deterministic samples from large changed_functions.json payloads.

    The sampler is designed for stress experiments where the full changed-function
    set is too large for fair manual GT and strict matching. It preserves the
    original payload shape so sampled outputs can be passed to downstream stages.
    """

    def __init__(
        self,
        payload: dict[str, Any],
        *,
        max_functions: int = 80,
        max_per_file: int = 5,
        strategy: str = "stratified_file_round_robin",
    ) -> None:
        if max_functions <= 0:
            raise ValueError("max_functions must be positive.")
        if max_per_file <= 0:
            raise ValueError("max_per_file must be positive.")
        if strategy != "stratified_file_round_robin":
            raise ValueError(f"Unsupported sampling strategy: {strategy}")

        self.payload = payload
        self.max_functions = max_functions
        self.max_per_file = max_per_file
        self.strategy = strategy

    def build_payload(self, *, source_path: str | None = None) -> dict[str, Any]:
        items = self._list_of_dicts(self.payload.get("items"))
        sampled = self._sample(items)
        sampled_items = [entry.item for entry in sampled]
        sampled_files = sorted({entry.file_path for entry in sampled})

        output = dict(self.payload)
        output["items"] = sampled_items
        output["changed_files"] = sampled_files
        output["sampling"] = {
            "tool": "changed-function-sampler-v1",
            "strategy": self.strategy,
            "source_path": source_path,
            "source_item_count": len(items),
            "sampled_item_count": len(sampled_items),
            "source_file_count": len({self._string_value(item.get("file_path")) for item in items if item.get("file_path")}),
            "sampled_file_count": len(sampled_files),
            "max_functions": self.max_functions,
            "max_per_file": self.max_per_file,
            "selection_rules": [
                "Group changed functions by file_path.",
                "Rank files by changed-function count, total diff size, then path.",
                "Rank functions within each file by diff size, hunk count, symbol, and line number.",
                "Select functions with round-robin traversal across ranked files.",
                "Cap selected functions per file to preserve cross-file coverage.",
            ],
            "sampled_files": self._sampled_file_summary(sampled),
            "change_type_counts": self._count_by(sampled, key="change_type"),
        }
        return output

    def build_markdown_summary(self, sampled_payload: dict[str, Any]) -> str:
        sampling = sampled_payload.get("sampling")
        if not isinstance(sampling, dict):
            raise ValueError("sampled_payload does not contain sampling metadata.")

        lines = [
            "# Changed Function Sampling Summary",
            "",
            f"- Strategy: `{sampling.get('strategy')}`",
            f"- Source items: `{sampling.get('source_item_count')}`",
            f"- Sampled items: `{sampling.get('sampled_item_count')}`",
            f"- Source files: `{sampling.get('source_file_count')}`",
            f"- Sampled files: `{sampling.get('sampled_file_count')}`",
            f"- Max functions: `{sampling.get('max_functions')}`",
            f"- Max per file: `{sampling.get('max_per_file')}`",
            "",
            "## Change Type Counts",
            "",
            "| Change Type | Count |",
            "| --- | ---: |",
        ]
        change_counts = sampling.get("change_type_counts")
        if isinstance(change_counts, dict):
            for key in sorted(change_counts):
                lines.append(f"| `{key}` | {change_counts[key]} |")

        lines.extend(
            [
                "",
                "## Sampled Files",
                "",
                "| File | Sampled Functions |",
                "| --- | ---: |",
            ]
        )
        sampled_files = sampling.get("sampled_files")
        if isinstance(sampled_files, list):
            for entry in sampled_files:
                if not isinstance(entry, dict):
                    continue
                lines.append(f"| `{entry.get('file_path')}` | {entry.get('sampled_count')} |")

        lines.extend(
            [
                "",
                "## Notes",
                "",
                "- This sample is deterministic and intended for stress-case evidence construction.",
                "- Do not mix sampled stress metrics into the core benchmark average unless the thesis explicitly defines a sampled-stress protocol.",
            ]
        )
        return "\n".join(lines) + "\n"

    def _sample(self, items: list[dict[str, Any]]) -> list[SampledItem]:
        scored_items = [self._score_item(item) for item in items]
        by_file: dict[str, list[SampledItem]] = defaultdict(list)
        for item in scored_items:
            by_file[item.file_path].append(item)

        for file_items in by_file.values():
            file_items.sort(key=lambda item: (-item.score, item.item.get("symbol", ""), item.item.get("start_line", 0)))

        ranked_files = sorted(
            by_file,
            key=lambda file_path: (
                -len(by_file[file_path]),
                -sum(item.diff_line_count for item in by_file[file_path]),
                file_path,
            ),
        )

        selected: list[SampledItem] = []
        selected_keys: set[tuple[str, str, int, str]] = set()
        per_file_count: dict[str, int] = defaultdict(int)

        cursor = 0
        while len(selected) < self.max_functions and ranked_files:
            progressed = False
            for file_path in ranked_files:
                if per_file_count[file_path] >= self.max_per_file:
                    continue
                file_items = by_file[file_path]
                if cursor >= len(file_items):
                    continue
                candidate = file_items[cursor]
                key = self._item_key(candidate.item)
                if key in selected_keys:
                    continue
                selected.append(candidate)
                selected_keys.add(key)
                per_file_count[file_path] += 1
                progressed = True
                if len(selected) >= self.max_functions:
                    break
            if not progressed:
                break
            cursor += 1

        selected.sort(key=lambda item: (item.file_path, int(item.item.get("start_line", 0)), item.item.get("symbol", "")))
        return selected

    def _score_item(self, item: dict[str, Any]) -> SampledItem:
        file_path = self._string_value(item.get("file_path"))
        change_type = self._string_value(item.get("change_type")) or "unknown"
        hunk_count = 0
        diff_line_count = 0
        hunks = item.get("diff_hunks")
        if isinstance(hunks, list):
            hunk_count = len(hunks)
            for hunk in hunks:
                if not isinstance(hunk, dict):
                    continue
                lines = hunk.get("lines")
                if not isinstance(lines, list):
                    continue
                diff_line_count += sum(
                    1
                    for line in lines
                    if isinstance(line, str)
                    and (line.startswith("+") or line.startswith("-"))
                    and not line.startswith("+++")
                    and not line.startswith("---")
                )

        change_type_weight = {"added": 4, "deleted": 4, "modified": 2}.get(change_type, 1)
        score = diff_line_count + hunk_count * 3 + change_type_weight
        return SampledItem(
            item=item,
            file_path=file_path,
            change_type=change_type,
            diff_line_count=diff_line_count,
            hunk_count=hunk_count,
            score=score,
        )

    @staticmethod
    def _sampled_file_summary(sampled: list[SampledItem]) -> list[dict[str, Any]]:
        counts: dict[str, int] = defaultdict(int)
        for item in sampled:
            counts[item.file_path] += 1
        return [{"file_path": path, "sampled_count": counts[path]} for path in sorted(counts)]

    @staticmethod
    def _count_by(sampled: list[SampledItem], *, key: str) -> dict[str, int]:
        counts: dict[str, int] = defaultdict(int)
        for item in sampled:
            counts[getattr(item, key)] += 1
        return dict(sorted(counts.items()))

    @staticmethod
    def _list_of_dicts(value: object) -> list[dict[str, Any]]:
        if not isinstance(value, list):
            return []
        return [item for item in value if isinstance(item, dict)]

    @staticmethod
    def _string_value(value: object) -> str:
        return value if isinstance(value, str) else ""

    @staticmethod
    def _item_key(item: dict[str, Any]) -> tuple[str, str, int, str]:
        return (
            ChangedFunctionSampler._string_value(item.get("file_path")),
            ChangedFunctionSampler._string_value(item.get("symbol")),
            int(item.get("start_line", 0) or 0),
            ChangedFunctionSampler._string_value(item.get("change_type")),
        )


def load_changed_functions(path: str | Path) -> dict[str, Any]:
    import json

    source = Path(path)
    return json.loads(source.read_text(encoding="utf-8"))

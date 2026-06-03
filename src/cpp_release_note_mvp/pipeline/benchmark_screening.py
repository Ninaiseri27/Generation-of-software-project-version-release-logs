from __future__ import annotations

from dataclasses import replace
from pathlib import Path
from typing import Any

from ..config import AppConfig
from ..models import VersionPair
from .change_detection import ChangeDetector
from .git_utils import run_git


class VersionPairScreener:
    """Screen adjacent release tags before expensive ENRE/LLM runs."""

    def __init__(
        self,
        config: AppConfig,
        *,
        tag_pattern: str = "OpenHarmony-v*",
        recent_pairs: int | None = None,
        max_symbols_per_pair: int = 25,
    ) -> None:
        self.config = config
        self.tag_pattern = tag_pattern
        self.recent_pairs = recent_pairs
        self.max_symbols_per_pair = max_symbols_per_pair

    def screen(self) -> dict[str, Any]:
        tags = self._list_tags()
        pairs = self._adjacent_pairs(tags)

        results: list[dict[str, Any]] = []
        for ref, tgt in pairs:
            results.append(self._screen_pair(ref, tgt))

        return {
            "source": {
                "tool": "version-pair-screener-v1",
                "repository": str(self.config.version_pair.repo_path),
                "tag_pattern": self.tag_pattern,
                "recent_pairs": self.recent_pairs,
            },
            "summary": self._summarize(results),
            "items": results,
        }

    def _list_tags(self) -> list[str]:
        output = run_git(
            self.config.version_pair.repo_path,
            self.config.git_executable,
            ["tag", "--list", self.tag_pattern, "--sort=version:refname"],
        )
        return [line.strip() for line in output.splitlines() if line.strip()]

    def _adjacent_pairs(self, tags: list[str]) -> list[tuple[str, str]]:
        if len(tags) < 2:
            return []

        pairs = list(zip(tags, tags[1:]))
        if self.recent_pairs is not None and self.recent_pairs > 0:
            return pairs[-self.recent_pairs :]
        return pairs

    def _screen_pair(self, ref: str, tgt: str) -> dict[str, Any]:
        pair_config = replace(
            self.config,
            version_pair=VersionPair(
                repo_path=self.config.version_pair.repo_path,
                ref_version=ref,
                tgt_version=tgt,
            ),
            output_dir=None,
        )

        try:
            all_changed_files = self._list_all_changed_files(ref, tgt)
            detector = ChangeDetector(pair_config)
            changed_payload = detector.detect_as_payload()
            changed_files = list(changed_payload.get("changed_files", []))
            changed_functions = list(changed_payload.get("items", []))
            commit_messages = list(changed_payload.get("commit_messages", []))
            result = {
                "ref": ref,
                "tgt": tgt,
                "status": "passed",
                "commit_count": self._commit_count(ref, tgt),
                "changed_file_count": len(all_changed_files),
                "changed_cpp_file_count": len(changed_files),
                "changed_function_count": len(changed_functions),
                "patch_only": bool(all_changed_files and not changed_files),
                "size_bucket": self._size_bucket(len(changed_functions), bool(all_changed_files and not changed_files)),
                "changed_cpp_files": changed_files,
                "changed_symbol_sample_limit": self.max_symbols_per_pair,
                "changed_symbols": [
                    {
                        "symbol": item.get("symbol"),
                        "file_path": item.get("file_path"),
                        "change_type": item.get("change_type"),
                    }
                    for item in changed_functions[: self.max_symbols_per_pair]
                ],
                "commit_messages": commit_messages[:10],
            }
            return result
        except Exception as exc:  # pragma: no cover - protects batch screening.
            return {
                "ref": ref,
                "tgt": tgt,
                "status": "failed",
                "error": f"{type(exc).__name__}: {exc}",
            }

    def _list_all_changed_files(self, ref: str, tgt: str) -> list[str]:
        output = run_git(
            self.config.version_pair.repo_path,
            self.config.git_executable,
            ["diff", "--name-only", "--diff-filter=ADM", ref, tgt, "--"],
        )
        return [line.strip() for line in output.splitlines() if line.strip()]

    def _commit_count(self, ref: str, tgt: str) -> int:
        output = run_git(
            self.config.version_pair.repo_path,
            self.config.git_executable,
            ["rev-list", "--count", f"{ref}..{tgt}"],
        )
        return int(output.strip() or "0")

    @staticmethod
    def _size_bucket(changed_function_count: int, patch_only: bool) -> str:
        if patch_only:
            return "patch_only"
        if changed_function_count == 0:
            return "empty_or_metadata"
        if changed_function_count <= 2:
            return "tiny"
        if changed_function_count <= 10:
            return "small"
        if changed_function_count <= 50:
            return "medium"
        return "large"

    @staticmethod
    def _summarize(results: list[dict[str, Any]]) -> dict[str, Any]:
        bucket_counts: dict[str, int] = {}
        passed = 0
        failed = 0
        for item in results:
            if item.get("status") == "passed":
                passed += 1
                bucket = str(item.get("size_bucket", "unknown"))
                bucket_counts[bucket] = bucket_counts.get(bucket, 0) + 1
            else:
                failed += 1

        return {
            "screened_pair_count": len(results),
            "passed_pair_count": passed,
            "failed_pair_count": failed,
            "size_bucket_counts": bucket_counts,
        }

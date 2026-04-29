from __future__ import annotations

from collections import defaultdict

from ..config import AppConfig
from ..models import ChangedFunction, CodeSymbol, DiffHunk
from .cpp_symbol_extractor import CppSymbolExtractor
from .git_utils import get_commit_messages, get_file_content, get_unified_diff, list_changed_files, parse_unified_diff


class ChangeDetector:
    def __init__(self, config: AppConfig) -> None:
        self.config = config
        self.symbol_extractor = CppSymbolExtractor()

    def detect(self) -> list[ChangedFunction]:
        changed_files = list_changed_files(self.config)
        diff_text = get_unified_diff(self.config, changed_files)
        hunks_by_file = parse_unified_diff(diff_text)

        detected: list[ChangedFunction] = []
        for relative_path in changed_files:
            detected.extend(self.detect_for_file(relative_path, hunks_by_file.get(relative_path, [])))

        detected.sort(key=lambda item: (item.file_path, item.start_line, item.symbol, item.change_type))
        return detected

    def detect_for_file(self, relative_path: str, hunks: list[DiffHunk]) -> list[ChangedFunction]:
        ref_content = get_file_content(
            self.config.version_pair.repo_path,
            self.config.git_executable,
            self.config.version_pair.ref_version,
            relative_path,
        )
        tgt_content = get_file_content(
            self.config.version_pair.repo_path,
            self.config.git_executable,
            self.config.version_pair.tgt_version,
            relative_path,
        )

        ref_symbols = self.symbol_extractor.extract(ref_content, relative_path) if ref_content else []
        tgt_symbols = self.symbol_extractor.extract(tgt_content, relative_path) if tgt_content else []

        ref_by_key = self._index_symbols(ref_symbols)
        tgt_by_key = self._index_symbols(tgt_symbols)
        all_keys = set(ref_by_key) | set(tgt_by_key)

        changed_functions: list[ChangedFunction] = []
        for key in sorted(all_keys):
            ref_symbol = ref_by_key.get(key)
            tgt_symbol = tgt_by_key.get(key)

            if ref_symbol is None and tgt_symbol is not None:
                matched_hunks = self._slice_hunks(
                    tgt_symbol,
                    [hunk for hunk in hunks if self._overlaps_new_range(tgt_symbol, hunk)],
                    mode="new",
                )
                changed_functions.append(
                    ChangedFunction(
                        symbol=tgt_symbol.name,
                        signature=tgt_symbol.signature,
                        file_path=relative_path,
                        change_type="added",
                        start_line=tgt_symbol.start_line,
                        end_line=tgt_symbol.end_line,
                        diff_hunks=matched_hunks,
                        notes=["Detected by target-only symbol presence."],
                    )
                )
                continue

            if ref_symbol is not None and tgt_symbol is None:
                matched_hunks = self._slice_hunks(
                    ref_symbol,
                    [hunk for hunk in hunks if self._overlaps_old_range(ref_symbol, hunk)],
                    mode="old",
                )
                changed_functions.append(
                    ChangedFunction(
                        symbol=ref_symbol.name,
                        signature=ref_symbol.signature,
                        file_path=relative_path,
                        change_type="deleted",
                        start_line=ref_symbol.start_line,
                        end_line=ref_symbol.end_line,
                        diff_hunks=matched_hunks,
                        notes=["Detected by reference-only symbol presence."],
                    )
                )
                continue

            if ref_symbol is None or tgt_symbol is None:
                continue

            matched_hunks = [
                hunk
                for hunk in hunks
                if self._overlaps_old_range(ref_symbol, hunk) or self._overlaps_new_range(tgt_symbol, hunk)
            ]
            matched_hunks = self._slice_hunks(tgt_symbol, matched_hunks, mode="both")
            if not matched_hunks:
                continue

            changed_functions.append(
                ChangedFunction(
                    symbol=tgt_symbol.name,
                    signature=tgt_symbol.signature,
                    file_path=relative_path,
                    change_type="modified",
                    start_line=tgt_symbol.start_line,
                    end_line=tgt_symbol.end_line,
                    diff_hunks=matched_hunks,
                    notes=["Detected by diff-hunk overlap across matched symbols."],
                )
            )

        return changed_functions

    def detect_as_payload(self) -> dict[str, object]:
        changed_files = list_changed_files(self.config)
        items = [item.to_dict() for item in self.detect()]
        return {
            "version_pair": {
                "repo_path": str(self.config.version_pair.repo_path),
                "ref_version": self.config.version_pair.ref_version,
                "tgt_version": self.config.version_pair.tgt_version,
            },
            "detector": "tree-sitter-cpp+regex-fallback-v1",
            "changed_files": changed_files,
            "commit_messages": get_commit_messages(self.config),
            "items": items,
        }

    @staticmethod
    def _index_symbols(symbols: list[CodeSymbol]) -> dict[str, CodeSymbol]:
        grouped: dict[str, list[CodeSymbol]] = defaultdict(list)
        for symbol in symbols:
            grouped[ChangeDetector._symbol_key(symbol)].append(symbol)

        indexed: dict[str, CodeSymbol] = {}
        for key, items in grouped.items():
            indexed[key] = items[0]
        return indexed

    @staticmethod
    def _symbol_key(symbol: CodeSymbol) -> str:
        return f"{symbol.file_path}::{symbol.signature}"

    @staticmethod
    def _overlaps_old_range(symbol: CodeSymbol, hunk: DiffHunk) -> bool:
        if hunk.old_count == 0:
            return False
        hunk_start = hunk.old_start
        hunk_end = hunk.old_start + max(hunk.old_count - 1, 0)
        return not (symbol.end_line < hunk_start or symbol.start_line > hunk_end)

    @staticmethod
    def _overlaps_new_range(symbol: CodeSymbol, hunk: DiffHunk) -> bool:
        if hunk.new_count == 0:
            return False
        hunk_start = hunk.new_start
        hunk_end = hunk.new_start + max(hunk.new_count - 1, 0)
        return not (symbol.end_line < hunk_start or symbol.start_line > hunk_end)

    def _slice_hunks(self, symbol: CodeSymbol, hunks: list[DiffHunk], mode: str) -> list[DiffHunk]:
        sliced: list[DiffHunk] = []
        for hunk in hunks:
            sliced_hunk = self._slice_hunk(symbol, hunk, mode)
            if sliced_hunk is not None and sliced_hunk.lines:
                sliced.append(sliced_hunk)
        return sliced

    @staticmethod
    def _slice_hunk(symbol: CodeSymbol, hunk: DiffHunk, mode: str) -> DiffHunk | None:
        old_line = hunk.old_start
        new_line = hunk.new_start
        selected_lines: list[str] = []
        selected_old_lines: list[int] = []
        selected_new_lines: list[int] = []

        for line in hunk.lines:
            prefix = line[:1] if line else " "
            include = False

            if prefix == "+":
                current_new = new_line
                include = mode in {"new", "both"} and symbol.start_line <= current_new <= symbol.end_line
                if include:
                    selected_new_lines.append(current_new)
                new_line += 1
            elif prefix == "-":
                current_old = old_line
                include = mode in {"old", "both"} and symbol.start_line <= current_old <= symbol.end_line
                if include:
                    selected_old_lines.append(current_old)
                old_line += 1
            else:
                current_old = old_line
                current_new = new_line
                if mode == "old":
                    include = symbol.start_line <= current_old <= symbol.end_line
                elif mode == "new":
                    include = symbol.start_line <= current_new <= symbol.end_line
                else:
                    include = (
                        symbol.start_line <= current_old <= symbol.end_line
                        or symbol.start_line <= current_new <= symbol.end_line
                    )
                if include:
                    selected_old_lines.append(current_old)
                    selected_new_lines.append(current_new)
                old_line += 1
                new_line += 1

            if include:
                selected_lines.append(line)

        if not selected_lines:
            return None

        return DiffHunk(
            file_path=hunk.file_path,
            old_start=min(selected_old_lines) if selected_old_lines else hunk.old_start,
            old_count=len(selected_old_lines),
            new_start=min(selected_new_lines) if selected_new_lines else hunk.new_start,
            new_count=len(selected_new_lines),
            lines=selected_lines,
        )

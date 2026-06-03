from __future__ import annotations

import re
from dataclasses import dataclass

from tree_sitter import Language, Parser
import tree_sitter_cpp

from ..models import CodeSymbol


CONTROL_KEYWORDS = ("if", "for", "while", "switch", "catch")
TEST_MACROS = ("HWTEST_F", "HWTEST", "TEST_F", "TEST", "TEST_P", "TYPED_TEST")


@dataclass(slots=True)
class _CandidateBlock:
    header: str
    start_line: int
    brace_balance: int


class CppSymbolExtractor:
    """
    Extract C/C++ function-like symbols.

    Primary mode uses tree-sitter-cpp for accurate function-definition parsing.
    A lightweight regex fallback is kept for resilience.
    """

    def __init__(self) -> None:
        self.parser = Parser(Language(tree_sitter_cpp.language()))

    def extract(self, content: str, file_path: str) -> list[CodeSymbol]:
        if not content.strip():
            return []

        symbols = self._extract_with_tree_sitter(content, file_path)
        if symbols:
            return symbols
        return self._extract_with_regex(content, file_path)

    def _extract_with_tree_sitter(self, content: str, file_path: str) -> list[CodeSymbol]:
        source = content.encode("utf-8")
        tree = self.parser.parse(source)
        symbols: list[CodeSymbol] = []

        self._collect_function_definitions(tree.root_node, source, file_path, symbols)
        self._collect_macro_test_functions(tree.root_node, source, file_path, symbols)

        deduped: dict[tuple[str, int, int], CodeSymbol] = {}
        for symbol in symbols:
            deduped[(symbol.signature, symbol.start_line, symbol.end_line)] = symbol

        return sorted(deduped.values(), key=lambda item: (item.start_line, item.end_line, item.signature))

    def _collect_function_definitions(
        self,
        node,
        source: bytes,
        file_path: str,
        symbols: list[CodeSymbol],
    ) -> None:
        if node.type == "function_definition":
            declarator = node.child_by_field_name("declarator")
            body = node.child_by_field_name("body")
            if declarator is not None and body is not None:
                signature = self._decode_slice(source, node.start_byte, body.start_byte).strip()
                declarator_text = self._decode_slice(source, declarator.start_byte, declarator.end_byte)
                name = self._extract_name_from_declarator(declarator_text)
                if name:
                    symbols.append(
                        CodeSymbol(
                            name=name,
                            signature=self._normalize_signature(signature),
                            file_path=file_path,
                            start_line=node.start_point.row + 1,
                            end_line=node.end_point.row + 1,
                            raw_header=signature,
                        )
                    )

        for child in node.children:
            self._collect_function_definitions(child, source, file_path, symbols)

    def _collect_macro_test_functions(
        self,
        node,
        source: bytes,
        file_path: str,
        symbols: list[CodeSymbol],
    ) -> None:
        named_children = list(node.named_children)
        for index, child in enumerate(named_children[:-1]):
            next_child = named_children[index + 1]
            if child.type != "expression_statement" or next_child.type != "compound_statement":
                continue

            statement_text = self._decode_slice(source, child.start_byte, child.end_byte).strip().rstrip(";")
            macro_match = re.match(
                r"(?P<macro>" + "|".join(TEST_MACROS) + r")\s*\(\s*[^,]+,\s*(?P<name>[A-Za-z_]\w*)",
                statement_text,
            )
            if macro_match is None:
                continue

            symbols.append(
                CodeSymbol(
                    name=macro_match.group("name"),
                    signature=self._normalize_signature(statement_text),
                    file_path=file_path,
                    start_line=child.start_point.row + 1,
                    end_line=next_child.end_point.row + 1,
                    raw_header=statement_text,
                )
            )

        for child in node.children:
            self._collect_macro_test_functions(child, source, file_path, symbols)

    def _extract_with_regex(self, content: str, file_path: str) -> list[CodeSymbol]:
        lines = content.splitlines()
        symbols: list[CodeSymbol] = []
        pending: _CandidateBlock | None = None
        header_buffer: list[tuple[int, str]] = []

        for line_no, line in enumerate(lines, start=1):
            stripped = line.strip()
            if not stripped:
                continue

            header_buffer.append((line_no, stripped))
            if len(header_buffer) > 8:
                header_buffer.pop(0)

            if pending is None:
                maybe_candidate = self._build_candidate(header_buffer)
                if maybe_candidate and "{" in stripped:
                    pending = maybe_candidate
                    pending.brace_balance += stripped.count("{") - stripped.count("}")
                    if pending.brace_balance <= 0:
                        symbol = self._candidate_to_symbol(pending, file_path, line_no)
                        if symbol is not None:
                            symbols.append(symbol)
                        pending = None
                continue

            pending.brace_balance += stripped.count("{") - stripped.count("}")
            if pending.brace_balance <= 0:
                symbol = self._candidate_to_symbol(pending, file_path, line_no)
                if symbol is not None:
                    symbols.append(symbol)
                pending = None

        return symbols

    def _build_candidate(self, header_buffer: list[tuple[int, str]]) -> _CandidateBlock | None:
        candidate_lines: list[tuple[int, str]] = []
        paren_balance = 0

        for line_no, stripped in reversed(header_buffer):
            candidate_lines.append((line_no, stripped))
            paren_balance += stripped.count(")") - stripped.count("(")

            if "{" in stripped and "(" not in stripped:
                return None

            if paren_balance > 0:
                break

            if stripped.endswith(";") or stripped.startswith("#"):
                return None

        candidate_lines.reverse()
        header = " ".join(part for _, part in candidate_lines)
        if not self._looks_like_function_definition(header):
            return None

        return _CandidateBlock(
            header=header,
            start_line=candidate_lines[0][0],
            brace_balance=0,
        )

    def _looks_like_function_definition(self, header: str) -> bool:
        normalized = " ".join(header.split())
        if "(" not in normalized or ")" not in normalized or "{" not in normalized:
            return False

        lowered = normalized.lstrip()
        if lowered.startswith(CONTROL_KEYWORDS):
            return False

        if normalized.endswith(";"):
            return False

        if "=" in normalized and "==" not in normalized and "{" not in normalized.split("=")[0]:
            return False

        if re.search(r"\b(class|struct|enum|namespace)\b", normalized):
            return False

        return bool(self._extract_name_from_declarator(normalized))

    def _candidate_to_symbol(self, candidate: _CandidateBlock, file_path: str, end_line: int) -> CodeSymbol | None:
        signature = candidate.header.split("{", maxsplit=1)[0].strip()
        name = self._extract_name_from_declarator(signature)
        if not name:
            return None

        return CodeSymbol(
            name=name,
            signature=self._normalize_signature(signature),
            file_path=file_path,
            start_line=candidate.start_line,
            end_line=end_line,
            raw_header=candidate.header,
        )

    @staticmethod
    def _decode_slice(source: bytes, start_byte: int, end_byte: int) -> str:
        return source[start_byte:end_byte].decode("utf-8", "replace")

    @staticmethod
    def _extract_name_from_declarator(declarator_text: str) -> str | None:
        before_params = declarator_text.split("(", maxsplit=1)[0].strip()
        match = re.search(r"([~A-Za-z_]\w*(?:::[~A-Za-z_]\w*)*)\s*$", before_params)
        if not match:
            return None
        return match.group(1)

    @staticmethod
    def _normalize_signature(signature: str) -> str:
        return " ".join(signature.split())


RegexCppSymbolExtractor = CppSymbolExtractor

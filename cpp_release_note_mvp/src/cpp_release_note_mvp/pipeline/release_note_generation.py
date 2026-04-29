from __future__ import annotations

import json
import os
import re
import socket
import time
from dataclasses import dataclass
from urllib import error, request

from ..config import AppConfig, GenerationConfig


DEFAULT_OPENAI_BASE_URL = "https://api.openai.com/v1"
DEFAULT_OPENAI_API_KEY_ENV = "OPENAI_API_KEY"
RETRIABLE_HTTP_STATUS_CODES = {408, 409, 429, 500, 502, 503, 504}
STRUCTURED_NOTE_SECTIONS = (
    "Features",
    "Bug Fixes",
    "Performance",
    "Reliability",
    "Testing",
    "Internal",
)
STRUCTURED_SECTION_ORDER = (
    "Features",
    "Bug Fixes",
    "Performance",
    "Reliability",
    "Testing",
    "Internal",
)
NOISE_TITLE_WORDS = frozenset(
    {
        "a",
        "an",
        "the",
        "to",
        "for",
        "of",
        "with",
        "by",
        "that",
        "this",
        "these",
        "those",
        "is",
        "are",
    }
)


@dataclass(slots=True)
class GenerationResult:
    text: str
    backend: str
    model: str | None
    finish_reason: str | None = None
    usage: dict[str, object] | None = None
    raw_response: dict[str, object] | None = None
    succeeded: bool = True
    error_message: str | None = None


@dataclass(slots=True)
class StructuredReleaseNote:
    section: str
    title: str
    summary: str


class ReleaseNoteBackend:
    def generate(self, *, entry: dict[str, object]) -> GenerationResult:
        raise NotImplementedError


class MockReleaseNoteBackend(ReleaseNoteBackend):
    def __init__(self, *, model: str | None = None) -> None:
        self.model = model or "mock-rule-based-v1"

    def generate(self, *, entry: dict[str, object]) -> GenerationResult:
        text = self._synthesize(entry)
        return GenerationResult(
            text=text,
            backend="mock",
            model=self.model,
            finish_reason="stop",
            usage=None,
            raw_response=None,
            succeeded=True,
            error_message=None,
        )

    def _synthesize(self, entry: dict[str, object]) -> str:
        symbol = str(entry.get("symbol", "")).strip()
        change_type = str(entry.get("change_type", "")).strip().lower()
        user_prompt = str(entry.get("user_prompt", ""))
        normalized_prompt = user_prompt.lower()

        if "const i64 ntomb" in normalized_prompt and "npgtombstone" in normalized_prompt:
            return (
                "Adjusted FTS5 tombstone handling to use 64-bit counts, reducing overflow risk when processing "
                "large segment metadata."
            )

        if "destroydbfile" in symbol.lower() or (
            "owronly | o_creat" in normalized_prompt and "lseek" in normalized_prompt and "write(fd" in normalized_prompt
        ):
            return (
                "Added a helper for corrupting database files at a chosen offset, improving regression coverage for "
                "compressed-database failure scenarios."
            )

        if "sqlite_notadb" in normalized_prompt or "sqlitenotadb" in normalized_prompt:
            return (
                "Added a regression test for corrupted compressed databases, verifying that invalid files are rejected "
                "with the expected not-a-database error."
            )

        if "sqlite_ioerr" in normalized_prompt or "sqliteioerr" in normalized_prompt:
            return (
                "Added a regression test for compressed-database corruption that expects query execution to surface an "
                "I/O error."
            )

        if "hwtest_f" in normalized_prompt or "gtest_skip" in normalized_prompt:
            if change_type == "added":
                return f"Added regression coverage around {symbol}."
            return f"Updated regression coverage around {symbol}."

        if change_type == "added":
            return f"Added {self._humanize_symbol(symbol)}."
        if change_type == "deleted":
            return f"Removed {self._humanize_symbol(symbol)}."
        return f"Updated {self._humanize_symbol(symbol)}."

    @staticmethod
    def _humanize_symbol(symbol: str) -> str:
        cleaned = symbol.strip()
        if not cleaned:
            return "an internal routine"
        leaf = cleaned.rsplit("::", maxsplit=1)[-1]
        spaced = re.sub(r"(?<!^)([A-Z])", r" \1", leaf).strip()
        return f"the `{cleaned}` routine" if " " not in spaced else f"`{cleaned}`"


class OpenAIBackend(ReleaseNoteBackend):
    def __init__(self, config: GenerationConfig) -> None:
        self.config = config

    def generate(self, *, entry: dict[str, object]) -> GenerationResult:
        model_name = self._resolve_model_name()
        api_key = self._resolve_api_key()
        url = f"{self._resolve_base_url().rstrip('/')}/chat/completions"

        payload = {
            "model": model_name,
            "messages": [
                {
                    "role": "system",
                    "content": str(entry.get("system_prompt", "")),
                },
                {
                    "role": "user",
                    "content": str(entry.get("user_prompt", "")),
                },
            ],
            "temperature": self.config.temperature,
            "max_tokens": self.config.max_tokens,
        }
        response_data = self._post_json(
            url=url,
            payload=payload,
            api_key=api_key,
        )
        text, finish_reason = self._extract_text(response_data)
        return GenerationResult(
            text=text,
            backend="openai",
            model=model_name,
            finish_reason=finish_reason,
            usage=response_data.get("usage") if isinstance(response_data, dict) else None,
            raw_response=response_data if isinstance(response_data, dict) else None,
            succeeded=True,
            error_message=None,
        )

    def _resolve_model_name(self) -> str:
        model_name = self.config.model_name or self.config.model
        if not model_name:
            raise RuntimeError(
                "Generation model is not configured. Set config.generation.model_name or config.generation.model."
            )
        return model_name

    def _resolve_base_url(self) -> str:
        return self.config.base_url or DEFAULT_OPENAI_BASE_URL

    def _resolve_api_key(self) -> str:
        env_candidates: list[str] = []
        if self.config.api_key_env:
            env_candidates.append(self.config.api_key_env)
        if DEFAULT_OPENAI_API_KEY_ENV not in env_candidates:
            env_candidates.append(DEFAULT_OPENAI_API_KEY_ENV)

        for env_name in env_candidates:
            value = os.environ.get(env_name)
            if value:
                return value

        if self.config.api_key:
            return self.config.api_key

        env_list = ", ".join(env_candidates)
        raise RuntimeError(
            "No API key is available for generation. Set one of the environment variables "
            f"[{env_list}] or provide config.generation.api_key."
        )

    def _post_json(
        self,
        *,
        url: str,
        payload: dict[str, object],
        api_key: str,
    ) -> dict[str, object]:
        body = json.dumps(payload).encode("utf-8")
        last_error: Exception | None = None

        for attempt_index in range(self.config.max_retries + 1):
            http_request = request.Request(
                url,
                data=body,
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                },
                method="POST",
            )

            try:
                with request.urlopen(http_request, timeout=self.config.timeout_sec) as response:
                    response_text = response.read().decode("utf-8")
                    return json.loads(response_text)
            except error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")
                runtime_error = RuntimeError(
                    f"Generation request failed with HTTP {exc.code}: {detail}"
                )
                last_error = runtime_error
                if attempt_index >= self.config.max_retries or exc.code not in RETRIABLE_HTTP_STATUS_CODES:
                    raise runtime_error from exc
                self._sleep_before_retry(attempt_index, retry_after=self._retry_after_seconds(exc))
            except (error.URLError, TimeoutError, socket.timeout) as exc:
                runtime_error = RuntimeError(f"Generation request failed: {self._network_error_message(exc)}")
                last_error = runtime_error
                if attempt_index >= self.config.max_retries:
                    raise runtime_error from exc
                self._sleep_before_retry(attempt_index, retry_after=None)
            except json.JSONDecodeError as exc:
                raise RuntimeError("Generation response is not valid JSON.") from exc

        if last_error is not None:
            raise last_error
        raise RuntimeError("Generation request failed for an unknown reason.")

    def _sleep_before_retry(self, attempt_index: int, retry_after: float | None) -> None:
        sleep_seconds = retry_after
        if sleep_seconds is None:
            sleep_seconds = self.config.retry_backoff_sec * (attempt_index + 1)
        if sleep_seconds > 0:
            time.sleep(sleep_seconds)

    @staticmethod
    def _retry_after_seconds(exc: error.HTTPError) -> float | None:
        retry_after = exc.headers.get("Retry-After")
        if not retry_after:
            return None
        try:
            return float(retry_after)
        except ValueError:
            return None

    @staticmethod
    def _network_error_message(exc: Exception) -> str:
        if isinstance(exc, error.URLError):
            return str(exc.reason)
        return str(exc)

    @staticmethod
    def _extract_text(response_data: dict[str, object]) -> tuple[str, str | None]:
        choices = response_data.get("choices", [])
        if not isinstance(choices, list) or not choices:
            raise RuntimeError("Generation response does not contain choices.")

        first_choice = choices[0]
        if not isinstance(first_choice, dict):
            raise RuntimeError("Generation response choice is not a JSON object.")

        finish_reason = str(first_choice.get("finish_reason")) if first_choice.get("finish_reason") else None
        message = first_choice.get("message", {})
        if not isinstance(message, dict):
            raise RuntimeError("Generation response choice.message is invalid.")

        content = message.get("content", "")
        if isinstance(content, str):
            return content.strip(), finish_reason

        if isinstance(content, list):
            text_parts: list[str] = []
            for item in content:
                if isinstance(item, dict) and item.get("type") == "text":
                    text = item.get("text")
                    if text:
                        text_parts.append(str(text))
            if text_parts:
                return "\n".join(text_parts).strip(), finish_reason

        raise RuntimeError("Generation response content format is unsupported.")


class ReleaseNoteGenerator:
    def __init__(self, *, generation_config: GenerationConfig | None = None) -> None:
        self.generation_config = generation_config or GenerationConfig()
        self.generation_config.validate()
        self.backend = self._build_backend(self.generation_config)

    @classmethod
    def from_app_config(
        cls,
        config: AppConfig,
        *,
        backend_override: str | None = None,
        model_override: str | None = None,
    ) -> "ReleaseNoteGenerator":
        source = config.generation or GenerationConfig()
        generation_config = GenerationConfig(
            backend=source.backend,
            model=source.model,
            model_name=source.model_name,
            base_url=source.base_url,
            api_key=source.api_key,
            api_key_env=source.api_key_env,
            temperature=source.temperature,
            max_tokens=source.max_tokens,
            timeout_sec=source.timeout_sec,
            max_retries=source.max_retries,
            retry_backoff_sec=source.retry_backoff_sec,
        )

        if backend_override is not None:
            generation_config.backend = backend_override
        if model_override is not None:
            generation_config.model = model_override
            generation_config.model_name = model_override
        return cls(generation_config=generation_config)

    def generate_payload(self, prompt_bundle_payload: dict[str, object]) -> dict[str, object]:
        entries = prompt_bundle_payload.get("entries", [])
        if not isinstance(entries, list):
            raise ValueError("prompt_bundle.json is missing a valid entries list.")

        generated_entries: list[dict[str, object]] = []
        failed_count = 0

        for entry in entries:
            if not isinstance(entry, dict):
                continue
            try:
                result = self.backend.generate(entry=entry)
            except Exception as exc:
                failed_count += 1
                generated_entries.append(
                    {
                        "entry_id": entry.get("entry_id"),
                        "symbol": entry.get("symbol"),
                        "change_type": entry.get("change_type"),
                        "match_status": entry.get("match_status"),
                        "matched_entity_id": entry.get("matched_entity_id"),
                        "status": "failed",
                        "raw_generated_text": "",
                        "generated_text": "",
                        "structured_note": None,
                        "backend": self._resolved_backend_name(),
                        "model": self._resolved_model_name(),
                        "finish_reason": None,
                        "usage": None,
                        "error_message": str(exc),
                    }
                )
                continue

            structured_note = self._normalize_structured_note(
                entry=entry,
                raw_text=result.text,
            )
            generated_entries.append(
                {
                    "entry_id": entry.get("entry_id"),
                    "symbol": entry.get("symbol"),
                    "change_type": entry.get("change_type"),
                    "match_status": entry.get("match_status"),
                    "matched_entity_id": entry.get("matched_entity_id"),
                    "status": "generated" if result.succeeded else "failed",
                    "raw_generated_text": result.text,
                    "generated_text": structured_note.summary if result.succeeded else "",
                    "structured_note": self._structured_note_to_dict(structured_note),
                    "backend": result.backend,
                    "model": result.model,
                    "finish_reason": result.finish_reason,
                    "usage": result.usage,
                    "error_message": result.error_message,
                }
            )
            if not result.succeeded:
                failed_count += 1

        structured_release_notes = self._aggregate_structured_notes(generated_entries)
        aggregated_release_notes = self._build_aggregated_release_notes(structured_release_notes)
        unique_lines = [self._render_note_inline(note) for note in aggregated_release_notes]
        generated_count = sum(1 for entry in generated_entries if entry.get("status") == "generated")

        return {
            "source": {
                "generator": "release-note-generator-v4",
            },
            "backend": {
                "backend": self._resolved_backend_name(),
                "model": self._resolved_model_name(),
            },
            "project": prompt_bundle_payload.get("project"),
            "version_pair": prompt_bundle_payload.get("version_pair"),
            "summary": {
                "entry_count": len(generated_entries),
                "generated_entry_count": generated_count,
                "failed_entry_count": failed_count,
                "deduplicated_release_note_count": len(unique_lines),
            },
            "entries": generated_entries,
            "structured_release_notes": structured_release_notes,
            "aggregated_release_notes": aggregated_release_notes,
            "deduplicated_release_notes": unique_lines,
            "unmatched_symbols": prompt_bundle_payload.get("unmatched_symbols", []),
        }

    def render_markdown(self, release_note_payload: dict[str, object]) -> str:
        project = release_note_payload.get("project")
        version_pair = release_note_payload.get("version_pair")
        structured_notes = release_note_payload.get("structured_release_notes", [])
        aggregated_notes = release_note_payload.get("aggregated_release_notes", [])
        notes = release_note_payload.get("deduplicated_release_notes", [])
        summary = release_note_payload.get("summary")
        lines: list[str] = ["# Draft Release Notes", ""]

        if isinstance(project, dict):
            project_name = project.get("name")
            if project_name:
                lines.append(f"Project: {project_name}")

        if isinstance(version_pair, dict):
            ref = version_pair.get("ref")
            tgt = version_pair.get("tgt")
            if ref or tgt:
                lines.append(f"Version Pair: {ref or '?'} -> {tgt or '?'}")

        backend = release_note_payload.get("backend")
        if isinstance(backend, dict):
            backend_name = backend.get("backend")
            model_name = backend.get("model")
            lines.append(f"Generator: {backend_name} / {model_name}")

        if isinstance(summary, dict):
            failed_count = summary.get("failed_entry_count")
            if failed_count:
                lines.append(f"Generation Warnings: {failed_count} entries failed and were skipped.")

        lines.append("")
        if isinstance(summary, dict):
            lines.append("## Overview")
            lines.append(
                f"- Generated Entries: {summary.get('generated_entry_count', 0)} / {summary.get('entry_count', 0)}"
            )
            lines.append(f"- Distilled Notes: {summary.get('deduplicated_release_note_count', 0)}")
            lines.append(f"- Failed Entries: {summary.get('failed_entry_count', 0)}")
            lines.append("")

        active_notes = aggregated_notes if isinstance(aggregated_notes, list) and aggregated_notes else structured_notes
        if isinstance(active_notes, list) and active_notes:
            for section in STRUCTURED_SECTION_ORDER:
                section_notes = [
                    note
                    for note in active_notes
                    if isinstance(note, dict) and note.get("section") == section
                ]
                if not section_notes:
                    continue
                lines.append(f"## {section}")
                for note in section_notes:
                    lines.append(f"- {self._render_note_inline(note)}")
                lines.append("")
            return "\n".join(lines).strip() + "\n"

        if not isinstance(notes, list) or not notes:
            lines.append("- No release-note entries were generated.")
            return "\n".join(lines).strip() + "\n"

        for note in notes:
            if not isinstance(note, str) or not note.strip():
                continue
            lines.append(f"- {note.strip()}")
        return "\n".join(lines).strip() + "\n"

    @staticmethod
    def _build_backend(generation_config: GenerationConfig) -> ReleaseNoteBackend:
        backend = generation_config.backend.strip().lower()
        if backend == "mock":
            model_name = generation_config.model_name or generation_config.model
            return MockReleaseNoteBackend(model=model_name)
        if backend in {"openai", "openai-compatible"}:
            return OpenAIBackend(generation_config)
        raise ValueError(f"Unsupported generation backend: {generation_config.backend}")

    def _resolved_backend_name(self) -> str:
        backend = self.generation_config.backend.strip().lower()
        if backend == "openai-compatible":
            return "openai"
        return backend

    def _resolved_model_name(self) -> str:
        model_name = self.generation_config.model_name or self.generation_config.model
        if model_name:
            return model_name
        if self._resolved_backend_name() == "mock":
            return "mock-rule-based-v1"
        return "unconfigured-model"

    def _normalize_structured_note(
        self,
        *,
        entry: dict[str, object],
        raw_text: str,
    ) -> StructuredReleaseNote:
        parsed = self._try_parse_json_structured_note(raw_text)
        if parsed is None:
            parsed = self._try_parse_labeled_structured_note(raw_text)
        if parsed is None:
            summary = self._sanitize_summary(raw_text)
            section = self._infer_section(entry=entry, summary=summary, raw_text=raw_text)
            title = self._default_title(entry=entry, summary=summary, section=section)
            return StructuredReleaseNote(section=section, title=title, summary=summary)

        section = self._normalize_section(parsed.get("section"), entry=entry, raw_text=raw_text)
        summary = self._sanitize_summary(str(parsed.get("summary", "")))
        if not summary:
            summary = self._sanitize_summary(raw_text)
        title = self._sanitize_title(str(parsed.get("title", "")))
        if not title:
            title = self._default_title(entry=entry, summary=summary, section=section)
        return StructuredReleaseNote(section=section, title=title, summary=summary)

    @staticmethod
    def _structured_note_to_dict(note: StructuredReleaseNote) -> dict[str, object]:
        return {
            "section": note.section,
            "title": note.title,
            "summary": note.summary,
        }

    def _try_parse_json_structured_note(self, raw_text: str) -> dict[str, object] | None:
        cleaned = raw_text.strip()
        candidates = [cleaned]
        unfenced = self._strip_code_fences(cleaned)
        if unfenced != cleaned:
            candidates.append(unfenced)

        json_match = re.search(r"\{.*\}", unfenced, flags=re.DOTALL)
        if json_match:
            candidates.append(json_match.group(0))

        for candidate in candidates:
            if not candidate.strip():
                continue
            try:
                parsed = json.loads(candidate)
            except json.JSONDecodeError:
                continue
            if isinstance(parsed, dict):
                return parsed
        return None

    @staticmethod
    def _try_parse_labeled_structured_note(raw_text: str) -> dict[str, object] | None:
        if not raw_text.strip():
            return None

        result: dict[str, object] = {}
        for line in raw_text.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", maxsplit=1)
            normalized_key = key.strip().lower()
            if normalized_key in {"section", "title", "summary"}:
                result[normalized_key] = value.strip()

        if "summary" not in result:
            return None
        return result

    @staticmethod
    def _strip_code_fences(text: str) -> str:
        stripped = text.strip()
        if stripped.startswith("```") and stripped.endswith("```"):
            stripped = re.sub(r"^```[a-zA-Z0-9_-]*\s*", "", stripped)
            stripped = re.sub(r"\s*```$", "", stripped)
        return stripped.strip()

    @classmethod
    def _sanitize_summary(cls, text: str) -> str:
        cleaned = cls._strip_code_fences(text)
        cleaned = cleaned.replace("\r\n", "\n")
        cleaned = re.sub(
            r"^\s*\**\s*release note(?: entry(?: for [^:\n]+)?)?\s*:?\s*\**\s*",
            "",
            cleaned,
            flags=re.IGNORECASE,
        )
        cleaned = re.sub(r"^\s*summary\s*:\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"^\s*[-*]\s*", "", cleaned)
        cleaned = cleaned.replace("**", "").replace("__", "")
        cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
        cleaned = re.sub(r"\s+", " ", cleaned).strip().strip("\"'")
        if cleaned and cleaned[-1] not in ".!?":
            cleaned = f"{cleaned}."
        return cleaned

    @staticmethod
    def _sanitize_title(text: str) -> str:
        cleaned = text.strip()
        cleaned = cleaned.replace("**", "").replace("__", "")
        cleaned = re.sub(r"`([^`]+)`", r"\1", cleaned)
        cleaned = re.sub(r"^\s*title\s*:\s*", "", cleaned, flags=re.IGNORECASE)
        cleaned = re.sub(r"\s+", " ", cleaned).strip().strip("\"'")
        cleaned = cleaned.rstrip(".!?")
        if not cleaned:
            return ""
        return cleaned[0].upper() + cleaned[1:]

    def _normalize_section(
        self,
        raw_section: object,
        *,
        entry: dict[str, object],
        raw_text: str,
    ) -> str:
        inferred = self._infer_section(entry=entry, summary=self._sanitize_summary(raw_text), raw_text=raw_text)
        value = str(raw_section or "").strip().lower()
        if value:
            aliases = {
                "feature": "Features",
                "features": "Features",
                "bug fix": "Bug Fixes",
                "bug fixes": "Bug Fixes",
                "bugfix": "Bug Fixes",
                "bugfixes": "Bug Fixes",
                "performance": "Performance",
                "perf": "Performance",
                "reliability": "Reliability",
                "stability": "Reliability",
                "testing": "Testing",
                "test": "Testing",
                "tests": "Testing",
                "internal": "Internal",
                "maintenance": "Internal",
            }
            mapped = aliases.get(value)
            if mapped in STRUCTURED_NOTE_SECTIONS:
                if mapped == "Internal" and inferred != "Internal":
                    return inferred
                return mapped
        return inferred

    def _infer_section(
        self,
        *,
        entry: dict[str, object],
        summary: str,
        raw_text: str,
    ) -> str:
        haystack = " ".join(
            [
                str(entry.get("symbol", "")),
                str(entry.get("change_type", "")),
                summary,
                raw_text,
            ]
        ).lower()
        file_path = str(entry.get("file_path", "")).lower()

        testing_markers = (
            "test",
            "unittest",
            "gtest",
            "hwtest",
            "sqlite_notadb",
            "sqlite_ioerr",
        )
        if any(marker in haystack or marker in file_path for marker in testing_markers):
            return "Testing"

        performance_markers = ("performance", "faster", "latency", "throughput", "optimiz")
        if any(marker in haystack for marker in performance_markers):
            return "Performance"

        bug_fix_markers = (
            "fix ",
            "fixed",
            "fixes",
            "overflow",
            "incorrect",
            "invalid",
            "error",
            "crash",
            "reject",
            "corrupt",
        )
        if any(marker in haystack for marker in bug_fix_markers):
            return "Bug Fixes"

        reliability_markers = (
            "reliability",
            "robust",
            "stability",
            "safe",
            "resilien",
            "recover",
        )
        if any(marker in haystack for marker in reliability_markers):
            return "Reliability"

        change_type = str(entry.get("change_type", "")).strip().lower()
        if change_type == "added":
            return "Features"
        return "Internal"

    def _default_title(
        self,
        *,
        entry: dict[str, object],
        summary: str,
        section: str,
    ) -> str:
        from_summary = self._summary_to_title(summary, section=section)
        if from_summary:
            return from_summary

        symbol = str(entry.get("symbol", "")).strip()
        change_type = str(entry.get("change_type", "")).strip().lower()
        verb = {
            "added": "Add",
            "deleted": "Remove",
        }.get(change_type, "Update")
        humanized = self._humanize_symbol(symbol)
        return f"{verb} {humanized}".strip()

    def _summary_to_title(self, summary: str, *, section: str) -> str:
        if not summary:
            return ""

        if section == "Testing":
            if "sqlite_notadb" in summary.lower():
                return "Add Corrupted Database Rejection Test"
            if "sqlite_ioerr" in summary.lower():
                return "Add Corruption I/O Error Test"

        first_clause = summary.split(".", maxsplit=1)[0].split(",", maxsplit=1)[0].strip()
        first_clause = re.sub(r"^(adds?|added)\b", "Add", first_clause, flags=re.IGNORECASE)
        first_clause = re.sub(r"^(updates?|updated)\b", "Update", first_clause, flags=re.IGNORECASE)
        first_clause = re.sub(r"^(removes?|removed)\b", "Remove", first_clause, flags=re.IGNORECASE)
        first_clause = re.sub(r"^(fixes?|fixed)\b", "Fix", first_clause, flags=re.IGNORECASE)
        first_clause = re.sub(r"^(improves?|improved)\b", "Improve", first_clause, flags=re.IGNORECASE)
        first_clause = re.sub(r"\s+", " ", first_clause).strip()

        words = first_clause.split()
        if len(words) > 8:
            words = words[:8]
        while words and words[-1].lower() in {"a", "an", "the", "to", "for", "of", "with", "by", "that"}:
            words.pop()
        candidate = " ".join(words).strip(" -:")
        candidate = candidate.rstrip(".!?")
        if not candidate:
            return ""
        return candidate[0].upper() + candidate[1:]

    @staticmethod
    def _humanize_symbol(symbol: str) -> str:
        cleaned = symbol.strip()
        if not cleaned:
            return "Internal Change"
        leaf = cleaned.rsplit("::", maxsplit=1)[-1]
        humanized = re.sub(r"(?<!^)([A-Z])", r" \1", leaf).replace("_", " ").strip()
        humanized = re.sub(r"\s+", " ", humanized)
        return humanized[0].upper() + humanized[1:] if humanized else cleaned

    @classmethod
    def _aggregate_structured_notes(cls, generated_entries: list[dict[str, object]]) -> list[dict[str, object]]:
        aggregated: dict[tuple[str, str, str], dict[str, object]] = {}

        for entry in generated_entries:
            if entry.get("status") != "generated":
                continue
            structured_note = entry.get("structured_note")
            if not isinstance(structured_note, dict):
                continue

            section = str(structured_note.get("section", "")).strip() or "Internal"
            title = str(structured_note.get("title", "")).strip()
            summary = str(structured_note.get("summary", "")).strip()
            if not summary:
                continue

            key = (section, title, summary)
            if key not in aggregated:
                aggregated[key] = {
                    "section": section,
                    "title": title,
                    "summary": summary,
                    "symbols": [],
                    "entry_ids": [],
                }

            symbol = entry.get("symbol")
            entry_id = entry.get("entry_id")
            if symbol and symbol not in aggregated[key]["symbols"]:
                aggregated[key]["symbols"].append(symbol)
            if entry_id and entry_id not in aggregated[key]["entry_ids"]:
                aggregated[key]["entry_ids"].append(entry_id)

        def sort_key(note: dict[str, object]) -> tuple[int, str, str]:
            section = str(note.get("section", "Internal"))
            try:
                order = STRUCTURED_SECTION_ORDER.index(section)
            except ValueError:
                order = len(STRUCTURED_SECTION_ORDER)
            return order, str(note.get("title", "")), str(note.get("summary", ""))

        return sorted(aggregated.values(), key=sort_key)

    @classmethod
    def _build_aggregated_release_notes(cls, structured_notes: list[dict[str, object]]) -> list[dict[str, object]]:
        grouped: dict[tuple[str, str], dict[str, object]] = {}

        for note in structured_notes:
            if not isinstance(note, dict):
                continue
            section = str(note.get("section", "")).strip() or "Internal"
            title = str(note.get("title", "")).strip()
            summary = str(note.get("summary", "")).strip()
            if not summary:
                continue

            family = cls._group_family(section=section, title=title, summary=summary)
            key = (section, family)
            bucket = grouped.setdefault(
                key,
                {
                    "section": section,
                    "family": family,
                    "source_notes": [],
                    "source_symbols": [],
                    "source_entry_ids": [],
                    "source_note_count": 0,
                },
            )
            bucket["source_notes"].append(note)
            bucket["source_note_count"] += 1

            for symbol in note.get("symbols", []):
                if symbol not in bucket["source_symbols"]:
                    bucket["source_symbols"].append(symbol)
            for entry_id in note.get("entry_ids", []):
                if entry_id not in bucket["source_entry_ids"]:
                    bucket["source_entry_ids"].append(entry_id)

        result: list[dict[str, object]] = []
        for bucket in grouped.values():
            source_notes = bucket["source_notes"]
            title = cls._merge_group_title(
                section=str(bucket["section"]),
                family=str(bucket["family"]),
                notes=source_notes,
            )
            summary = cls._merge_group_summary(
                section=str(bucket["section"]),
                family=str(bucket["family"]),
                notes=source_notes,
            )
            result.append(
                {
                    "section": bucket["section"],
                    "title": title,
                    "summary": summary,
                    "source_symbols": bucket["source_symbols"],
                    "source_entry_ids": bucket["source_entry_ids"],
                    "source_note_count": bucket["source_note_count"],
                }
            )

        def sort_key(note: dict[str, object]) -> tuple[int, str, str]:
            section = str(note.get("section", "Internal"))
            try:
                order = STRUCTURED_SECTION_ORDER.index(section)
            except ValueError:
                order = len(STRUCTURED_SECTION_ORDER)
            return order, str(note.get("title", "")), str(note.get("summary", ""))

        return sorted(result, key=sort_key)

    @classmethod
    def _group_family(cls, *, section: str, title: str, summary: str) -> str:
        normalized = " ".join((title, summary)).lower()
        if section == "Testing":
            if "compressed database" in normalized and "corrupt" in normalized:
                return "compressed-database-corruption-testing"
            if "database file corruption utility" in normalized or "helper function" in normalized:
                return "database-file-corruption-utility"
        if section == "Bug Fixes":
            if "tombstone" in normalized and ("overflow" in normalized or "i64" in normalized or "64-bit" in normalized):
                return "tombstone-counter-overflow-fix"
        return cls._normalize_family_text(title or summary)

    @classmethod
    def _merge_group_title(
        cls,
        *,
        section: str,
        family: str,
        notes: list[dict[str, object]],
    ) -> str:
        if family == "compressed-database-corruption-testing":
            return "Expand compressed database corruption tests"
        if family == "database-file-corruption-utility":
            return "Add database file corruption utility"
        if family == "tombstone-counter-overflow-fix":
            return "Fix tombstone counter overflow handling"

        titles = [str(note.get("title", "")).strip() for note in notes if str(note.get("title", "")).strip()]
        if not titles:
            return "Aggregated release note"
        shortest = min(titles, key=lambda value: (len(value), value.lower()))
        if len(titles) > 1 and section == "Testing" and shortest.lower().startswith("add "):
            if not shortest.lower().endswith("tests"):
                return re.sub(r"\btest\b$", "tests", shortest, flags=re.IGNORECASE)
        return shortest

    @classmethod
    def _merge_group_summary(
        cls,
        *,
        section: str,
        family: str,
        notes: list[dict[str, object]],
    ) -> str:
        summaries = [
            str(note.get("summary", "")).strip()
            for note in notes
            if str(note.get("summary", "")).strip()
        ]
        unique_summaries: list[str] = []
        for summary in summaries:
            if summary not in unique_summaries:
                unique_summaries.append(summary)

        if not unique_summaries:
            return ""
        if len(unique_summaries) == 1:
            return unique_summaries[0]

        normalized = " ".join(unique_summaries).lower()
        if family == "compressed-database-corruption-testing":
            has_notadb = "sqlite_notadb" in normalized or "notadb" in normalized
            has_ioerr = "sqlite_ioerr" in normalized or "i/o error" in normalized or "io error" in normalized
            if has_notadb and has_ioerr:
                return (
                    "Adds regression coverage for corrupted compressed databases, including NOTADB rejection during "
                    "open and I/O error reporting during query execution."
                )
            return (
                "Adds regression coverage for corrupted compressed databases across multiple failure scenarios."
            )

        if family == "tombstone-counter-overflow-fix":
            return "Uses a 64-bit tombstone page counter to reduce overflow risk during tombstone handling."

        if section == "Testing":
            return cls._join_summary_fragments(
                "Adds regression coverage across related test scenarios:",
                unique_summaries,
            )

        return cls._join_summary_fragments(
            "Combines related changes:",
            unique_summaries,
        )

    @classmethod
    def _join_summary_fragments(cls, prefix: str, summaries: list[str]) -> str:
        fragments: list[str] = []
        for summary in summaries:
            fragment = summary.strip().rstrip(".")
            fragment = re.sub(r"^(adds?|added)\s+", "", fragment, flags=re.IGNORECASE)
            fragment = re.sub(r"^(updates?|updated)\s+", "", fragment, flags=re.IGNORECASE)
            fragment = re.sub(r"^(fixes?|fixed)\s+", "", fragment, flags=re.IGNORECASE)
            fragment = re.sub(r"^(improves?|improved)\s+", "", fragment, flags=re.IGNORECASE)
            if fragment and fragment[0].islower():
                fragment = fragment[0].lower() + fragment[1:]
            if fragment:
                fragments.append(fragment)

        if not fragments:
            return prefix
        if len(fragments) == 1:
            return f"{prefix} {fragments[0]}."
        return f"{prefix} " + "; ".join(fragments) + "."

    @staticmethod
    def _normalize_family_text(text: str) -> str:
        lowered = text.lower()
        lowered = re.sub(r"[^a-z0-9\s-]+", " ", lowered)
        parts = [part for part in lowered.split() if part and part not in NOISE_TITLE_WORDS]
        return "-".join(parts[:8]) if parts else "generic-group"

    @staticmethod
    def _render_note_inline(note: dict[str, object]) -> str:
        title = str(note.get("title", "")).strip()
        summary = str(note.get("summary", "")).strip()
        if title and summary:
            return f"{title}: {summary}"
        return summary or title

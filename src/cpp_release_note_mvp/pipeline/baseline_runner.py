from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from ..config import AppConfig
from .prompt_builder import SUPPORTED_PROMPT_VARIANTS, PromptBundleBuilder
from .release_note_generation import ReleaseNoteGenerator


class BaselineRunner:
    def __init__(
        self,
        *,
        config: AppConfig,
        variants: list[str] | None = None,
        changed_input_path: str | Path | None = None,
        cmg_input_path: str | Path | None = None,
        output_root: str | Path | None = None,
        backend_override: str | None = None,
        model_override: str | None = None,
        aggregation_strategy_override: str | None = None,
    ) -> None:
        if config.output_dir is None and (changed_input_path is None or cmg_input_path is None):
            raise ValueError(
                "config.output_dir is required unless --changed-input and --cmg-input are both provided."
            )

        self.config = config
        self.variants = self._normalize_variants(variants)
        self.changed_input_path = Path(changed_input_path) if changed_input_path else config.output_dir / "changed_functions.json"  # type: ignore[operator]
        self.cmg_input_path = Path(cmg_input_path) if cmg_input_path else config.output_dir / "cmg.json"  # type: ignore[operator]
        if output_root is not None:
            self.output_root = Path(output_root)
        elif config.output_dir is not None:
            self.output_root = config.output_dir / "baselines"
        else:
            self.output_root = Path("baselines")

        self.backend_override = backend_override
        self.model_override = model_override
        self.aggregation_strategy_override = aggregation_strategy_override

    def run(self) -> dict[str, object]:
        changed_payload = self._read_json(self.changed_input_path)
        cmg_payload = self._read_json(self.cmg_input_path)
        results: list[dict[str, object]] = []

        for variant in self.variants:
            variant_dir = self.output_root / variant
            variant_dir.mkdir(parents=True, exist_ok=True)

            prompt_input_path = variant_dir / "prompt_input.json"
            prompt_bundle_path = variant_dir / "prompt_bundle.json"
            release_note_json_path = variant_dir / "release_note.json"
            release_note_markdown_path = variant_dir / "release_note.md"

            bundle_builder = PromptBundleBuilder.from_app_config(self.config)
            bundle_builder.prompt_variant = variant
            prompt_input_payload = bundle_builder.build_prompt_input_payload(
                changed_payload=changed_payload,
                cmg_payload=cmg_payload,
            )
            prompt_bundle_payload = bundle_builder.build_prompt_bundle_payload(
                prompt_input_payload=prompt_input_payload,
            )
            self._write_json(prompt_input_path, prompt_input_payload)
            self._write_json(prompt_bundle_path, prompt_bundle_payload)

            generator = ReleaseNoteGenerator.from_app_config(
                self.config,
                backend_override=self.backend_override,
                model_override=self.model_override,
                aggregation_strategy_override=self.aggregation_strategy_override,
            )
            release_note_payload = generator.generate_payload(prompt_bundle_payload)
            release_note_markdown = generator.render_markdown(release_note_payload)
            self._write_json(release_note_json_path, release_note_payload)
            release_note_markdown_path.write_text(release_note_markdown, encoding="utf-8")

            prompt_summary = prompt_input_payload.get("summary", {})
            generation_summary = release_note_payload.get("summary", {})
            results.append(
                {
                    "variant": variant,
                    "prompt_entry_count": self._summary_int(prompt_summary, "entry_count"),
                    "matched_entry_count": self._summary_int(prompt_summary, "matched_entry_count"),
                    "unmatched_entry_count": self._summary_int(prompt_summary, "unmatched_entry_count"),
                    "not_applicable_entry_count": self._summary_int(
                        prompt_summary,
                        "not_applicable_entry_count",
                    ),
                    "generated_entry_count": self._summary_int(generation_summary, "generated_entry_count"),
                    "failed_entry_count": self._summary_int(generation_summary, "failed_entry_count"),
                    "release_note_count": self._summary_int(
                        generation_summary,
                        "deduplicated_release_note_count",
                    ),
                    "aggregation_strategy": self._summary_value(generation_summary, "aggregation_strategy"),
                    "prompt_input_path": str(prompt_input_path),
                    "prompt_bundle_path": str(prompt_bundle_path),
                    "release_note_json_path": str(release_note_json_path),
                    "release_note_markdown_path": str(release_note_markdown_path),
                }
            )

        return {
            "source": {
                "runner": "baseline-runner-v1",
                "variants": self.variants,
            },
            "project": self._project_payload(),
            "version_pair": {
                "repo_path": str(self.config.version_pair.repo_path),
                "ref": self.config.version_pair.ref_version,
                "tgt": self.config.version_pair.tgt_version,
            },
            "inputs": {
                "changed_functions": str(self.changed_input_path),
                "cmg": str(self.cmg_input_path),
            },
            "output_root": str(self.output_root),
            "results": results,
        }

    def _project_payload(self) -> dict[str, object]:
        if self.config.project is None:
            return {
                "name": self.config.version_pair.repo_path.name,
                "description": None,
            }
        return {
            "name": self.config.project.name,
            "description": self.config.project.description,
        }

    @staticmethod
    def _normalize_variants(variants: list[str] | None) -> list[str]:
        if not variants:
            return list(SUPPORTED_PROMPT_VARIANTS)
        normalized: list[str] = []
        for variant in variants:
            value = variant.strip().lower().replace("-", "_")
            if value not in SUPPORTED_PROMPT_VARIANTS:
                allowed = ", ".join(SUPPORTED_PROMPT_VARIANTS)
                raise ValueError(f"Unsupported baseline variant: {variant}. Expected one of: {allowed}.")
            if value not in normalized:
                normalized.append(value)
        return normalized

    @staticmethod
    def _read_json(path: Path) -> dict[str, object]:
        if not path.exists():
            raise FileNotFoundError(f"Required baseline input not found: {path}")
        payload = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(payload, dict):
            raise ValueError(f"JSON payload must be an object: {path}")
        return payload

    @staticmethod
    def _write_json(path: Path, payload: dict[str, object]) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")

    @staticmethod
    def _summary_int(summary: object, key: str) -> int:
        value = BaselineRunner._summary_value(summary, key)
        if isinstance(value, int):
            return value
        if isinstance(value, float):
            return int(value)
        return 0

    @staticmethod
    def _summary_value(summary: object, key: str) -> Any:
        if not isinstance(summary, dict):
            return None
        return summary.get(key)

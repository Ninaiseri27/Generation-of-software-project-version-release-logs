from __future__ import annotations

import argparse
import json
from pathlib import Path

from .config import AppConfig
from .pipeline.change_detection import ChangeDetector
from .pipeline.cmg_builder import CmgBuilder
from .pipeline.enre_parser import EnreParser
from .pipeline.enre_runner import EnreRunner
from .pipeline.prompt_builder import PromptBundleBuilder
from .pipeline.release_note_generation import ReleaseNoteGenerator
from .pipeline.version_snapshot import VersionSnapshotManager


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="C/C++ release note MVP CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    detect_parser = subparsers.add_parser("detect-changes", help="Detect changed functions for one version pair")
    detect_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    detect_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for changed_functions.json; defaults to <output_dir>/changed_functions.json",
    )

    snapshot_parser = subparsers.add_parser(
        "prepare-snapshots",
        help="Create or reuse git worktree snapshots for the configured ref/tgt versions",
    )
    snapshot_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    snapshot_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for snapshot metadata JSON; prints to stdout if omitted",
    )

    enre_parser = subparsers.add_parser(
        "run-enre",
        help="Run ENRE-CPP on prepared snapshots for ref, tgt, or both versions",
    )
    enre_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    enre_parser.add_argument(
        "--target",
        choices=("ref", "tgt", "both"),
        default="both",
        help="Which snapshot(s) to analyze",
    )
    enre_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for ENRE run metadata JSON; prints to stdout if omitted",
    )

    normalize_enre_parser = subparsers.add_parser(
        "parse-enre",
        help="Normalize one ENRE raw JSON file into the internal graph schema",
    )
    normalize_enre_parser.add_argument("--input", required=True, help="Path to the ENRE raw JSON file")
    normalize_enre_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for normalized ENRE JSON; defaults next to the input file",
    )

    cmg_parser = subparsers.add_parser(
        "build-cmg",
        help="Build 1-hop CMG entries by chaining change detection, ENRE execution, normalization, and matching",
    )
    cmg_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    cmg_parser.add_argument(
        "--output",
        default=None,
        help="Optional output path for cmg.json; defaults to <output_dir>/cmg.json",
    )

    prompt_parser = subparsers.add_parser(
        "build-prompts",
        help="Build prompt_input.json and prompt_bundle.json from existing changed_functions.json and cmg.json",
    )
    prompt_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    prompt_parser.add_argument(
        "--changed-input",
        default=None,
        help="Optional input path for changed_functions.json; defaults to <output_dir>/changed_functions.json",
    )
    prompt_parser.add_argument(
        "--cmg-input",
        default=None,
        help="Optional input path for cmg.json; defaults to <output_dir>/cmg.json",
    )
    prompt_parser.add_argument(
        "--prompt-input-output",
        default=None,
        help="Optional output path for prompt_input.json; defaults to <output_dir>/prompt_input.json",
    )
    prompt_parser.add_argument(
        "--prompt-bundle-output",
        default=None,
        help="Optional output path for prompt_bundle.json; defaults to <output_dir>/prompt_bundle.json",
    )
    prompt_parser.add_argument(
        "--matched-only",
        action="store_true",
        help="Only generate prompts for matched CMG entries.",
    )

    generation_parser = subparsers.add_parser(
        "generate-release-notes",
        help="Generate release_note.json and release_note.md from prompt_bundle.json",
    )
    generation_parser.add_argument("--config", required=True, help="Path to the JSON config file")
    generation_parser.add_argument(
        "--prompt-bundle-input",
        default=None,
        help="Optional input path for prompt_bundle.json; defaults to <output_dir>/prompt_bundle.json",
    )
    generation_parser.add_argument(
        "--json-output",
        default=None,
        help="Optional output path for release_note.json; defaults to <output_dir>/release_note.json",
    )
    generation_parser.add_argument(
        "--markdown-output",
        default=None,
        help="Optional output path for release_note.md; defaults to <output_dir>/release_note.md",
    )
    generation_parser.add_argument(
        "--backend",
        choices=("mock", "openai", "openai-compatible"),
        default=None,
        help="Optional generation backend override.",
    )
    generation_parser.add_argument(
        "--model",
        default=None,
        help="Optional generation model override.",
    )

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "detect-changes":
        config = AppConfig.from_json_file(args.config)
        detector = ChangeDetector(config)
        payload = detector.detect_as_payload()

        output_path = args.output
        if output_path is None:
            if config.output_dir is None:
                raise ValueError("Either --output or config.output_dir must be provided.")
            output_path = str(Path(config.output_dir) / "changed_functions.json")

        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        return

    if args.command == "prepare-snapshots":
        config = AppConfig.from_json_file(args.config)
        manager = VersionSnapshotManager.from_app_config(config)
        payload = manager.ensure_version_pair_payload(config.version_pair)

        if args.output:
            target = Path(args.output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "run-enre":
        config = AppConfig.from_json_file(args.config)
        snapshot_manager = VersionSnapshotManager.from_app_config(config)
        snapshot_pair = snapshot_manager.ensure_version_pair(config.version_pair)
        runner = EnreRunner.from_app_config(config)
        payload = runner.run_for_pair(snapshot_pair, target=args.target)

        if args.output:
            target = Path(args.output)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
            return

        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return

    if args.command == "parse-enre":
        parser = EnreParser()
        graph = parser.parse_json_file(args.input)
        payload = graph.to_dict()

        output_path = args.output
        if output_path is None:
            source_path = Path(args.input)
            output_path = str(source_path.with_name(f"{source_path.stem}_normalized.json"))

        target = Path(output_path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(payload["summary"], ensure_ascii=False, indent=2))
        return

    if args.command == "build-cmg":
        config = AppConfig.from_json_file(args.config)
        config.cmg.validate()
        if config.output_dir is None and args.output is None:
            raise ValueError("Either --output or config.output_dir must be provided for build-cmg.")

        changed_payload = ChangeDetector(config).detect_as_payload()
        changed_output_path = _resolve_output_path(
            args_output=None,
            config_output_dir=config.output_dir,
            default_filename="changed_functions.json",
        )
        _write_json(changed_output_path, changed_payload)

        snapshot_manager = VersionSnapshotManager.from_app_config(config)
        snapshot_pair = snapshot_manager.ensure_version_pair(config.version_pair)
        runner = EnreRunner.from_app_config(config)
        run_payload = runner.run_for_pair(snapshot_pair, target="both")

        normalized_paths: dict[str, Path] = {}
        parser_impl = EnreParser()
        normalized_graphs: dict[str, dict[str, object]] = {}
        for side in ("ref", "tgt"):
            side_run = run_payload["runs"][side]
            raw_output_path = Path(str(side_run["output_json_path"]))
            graph = parser_impl.parse_json_file(raw_output_path)
            normalized_payload = graph.to_dict()
            normalized_path = raw_output_path.with_name(f"{raw_output_path.stem}_normalized.json")
            _write_json(normalized_path, normalized_payload)
            normalized_paths[side] = normalized_path
            normalized_graphs[side] = normalized_payload

        builder = CmgBuilder(
            changed_functions=list(changed_payload.get("items", [])),
            ref_normalized_graph=normalized_graphs["ref"],
            tgt_normalized_graph=normalized_graphs["tgt"],
            version_pair=changed_payload.get("version_pair") if isinstance(changed_payload, dict) else None,
            strategy=config.cmg.strategy,
            matching_view=config.cmg.matching_view,
            context_hops=config.cmg.context_hops,
            matched_hops=config.cmg.matched_hops,
            sparse_matched_hops=config.cmg.sparse_matched_hops,
            unmatched_expand_hops=config.cmg.unmatched_expand_hops,
            unmatched_expand_from_diff_calls=config.cmg.unmatched_expand_from_diff_calls,
            min_edges_for_sparse=config.cmg.min_edges_for_sparse,
            include_parent_context=config.cmg.include_parent_context,
            include_diff_calls=config.cmg.include_diff_calls,
            max_nodes=config.cmg.max_nodes,
            max_edges=config.cmg.max_edges,
        )
        cmg_payload = builder.build_payload()
        output_path = _resolve_output_path(
            args_output=args.output,
            config_output_dir=config.output_dir,
            default_filename="cmg.json",
        )
        _write_json(output_path, cmg_payload)

        matched_count = sum(1 for entry in cmg_payload["entries"] if entry["matched_entity_id"] is not None)
        unmatched_count = len(cmg_payload["unmatched_symbols"])
        print(f"成功匹配 {matched_count} 个，失败 {unmatched_count} 个。")
        print(
            json.dumps(
                {
                    "matched_count": matched_count,
                    "unmatched_count": unmatched_count,
                    "fallback_context_entry_count": cmg_payload.get("summary", {}).get(
                        "fallback_context_entry_count"
                    ),
                    "changed_functions_path": str(changed_output_path),
                    "ref_normalized_graph_path": str(normalized_paths["ref"]),
                    "tgt_normalized_graph_path": str(normalized_paths["tgt"]),
                    "cmg_output_path": str(output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "build-prompts":
        config = AppConfig.from_json_file(args.config)
        if config.output_dir is None and (
            args.changed_input is None
            or args.cmg_input is None
            or args.prompt_input_output is None
            or args.prompt_bundle_output is None
        ):
            raise ValueError(
                "config.output_dir is required unless all build-prompts input and output paths are provided."
            )

        changed_input_path = _resolve_output_path(
            args_output=args.changed_input,
            config_output_dir=config.output_dir,
            default_filename="changed_functions.json",
        )
        cmg_input_path = _resolve_output_path(
            args_output=args.cmg_input,
            config_output_dir=config.output_dir,
            default_filename="cmg.json",
        )
        prompt_input_output_path = _resolve_output_path(
            args_output=args.prompt_input_output,
            config_output_dir=config.output_dir,
            default_filename="prompt_input.json",
        )
        prompt_bundle_output_path = _resolve_output_path(
            args_output=args.prompt_bundle_output,
            config_output_dir=config.output_dir,
            default_filename="prompt_bundle.json",
        )

        if not changed_input_path.exists():
            raise FileNotFoundError(
                f"changed_functions.json not found: {changed_input_path}. Run detect-changes or build-cmg first."
            )
        if not cmg_input_path.exists():
            raise FileNotFoundError(f"cmg.json not found: {cmg_input_path}. Run build-cmg first.")

        changed_payload = json.loads(changed_input_path.read_text(encoding="utf-8"))
        cmg_payload = json.loads(cmg_input_path.read_text(encoding="utf-8"))

        bundle_builder = PromptBundleBuilder.from_app_config(config)
        if args.matched_only:
            bundle_builder.include_unmatched_entries = False

        prompt_input_payload = bundle_builder.build_prompt_input_payload(
            changed_payload=changed_payload,
            cmg_payload=cmg_payload,
        )
        prompt_bundle_payload = bundle_builder.build_prompt_bundle_payload(
            prompt_input_payload=prompt_input_payload,
        )

        _write_json(prompt_input_output_path, prompt_input_payload)
        _write_json(prompt_bundle_output_path, prompt_bundle_payload)

        print(
            json.dumps(
                {
                    "entry_count": prompt_input_payload["summary"]["entry_count"],
                    "matched_entry_count": prompt_input_payload["summary"]["matched_entry_count"],
                    "unmatched_entry_count": prompt_input_payload["summary"]["unmatched_entry_count"],
                    "changed_input_path": str(changed_input_path),
                    "cmg_input_path": str(cmg_input_path),
                    "prompt_input_output_path": str(prompt_input_output_path),
                    "prompt_bundle_output_path": str(prompt_bundle_output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return

    if args.command == "generate-release-notes":
        config = AppConfig.from_json_file(args.config)
        if config.output_dir is None and (
            args.prompt_bundle_input is None
            or args.json_output is None
            or args.markdown_output is None
        ):
            raise ValueError(
                "config.output_dir is required unless all generate-release-notes input and output paths are provided."
            )

        prompt_bundle_input_path = _resolve_output_path(
            args_output=args.prompt_bundle_input,
            config_output_dir=config.output_dir,
            default_filename="prompt_bundle.json",
        )
        json_output_path = _resolve_output_path(
            args_output=args.json_output,
            config_output_dir=config.output_dir,
            default_filename="release_note.json",
        )
        markdown_output_path = _resolve_output_path(
            args_output=args.markdown_output,
            config_output_dir=config.output_dir,
            default_filename="release_note.md",
        )

        if not prompt_bundle_input_path.exists():
            raise FileNotFoundError(
                f"prompt_bundle.json not found: {prompt_bundle_input_path}. Run build-prompts first."
            )

        prompt_bundle_payload = json.loads(prompt_bundle_input_path.read_text(encoding="utf-8"))
        generator = ReleaseNoteGenerator.from_app_config(
            config,
            backend_override=args.backend,
            model_override=args.model,
        )
        release_note_payload = generator.generate_payload(prompt_bundle_payload)
        release_note_markdown = generator.render_markdown(release_note_payload)

        _write_json(json_output_path, release_note_payload)
        markdown_output_path.parent.mkdir(parents=True, exist_ok=True)
        markdown_output_path.write_text(release_note_markdown, encoding="utf-8")

        print(
            json.dumps(
                {
                    "generated_entry_count": release_note_payload["summary"]["generated_entry_count"],
                    "failed_entry_count": release_note_payload["summary"]["failed_entry_count"],
                    "deduplicated_release_note_count": release_note_payload["summary"][
                        "deduplicated_release_note_count"
                    ],
                    "backend": release_note_payload["backend"]["backend"],
                    "model": release_note_payload["backend"]["model"],
                    "prompt_bundle_input_path": str(prompt_bundle_input_path),
                    "json_output_path": str(json_output_path),
                    "markdown_output_path": str(markdown_output_path),
                },
                ensure_ascii=False,
                indent=2,
            )
        )
        return


def _resolve_output_path(
    *,
    args_output: str | None,
    config_output_dir: Path | None,
    default_filename: str,
) -> Path:
    if args_output is not None:
        return Path(args_output)
    if config_output_dir is None:
        raise ValueError("config.output_dir is required when no explicit --output path is provided.")
    return config_output_dir / default_filename


def _write_json(path: str | Path, payload: dict[str, object]) -> None:
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .models import VersionPair


DEFAULT_EXTENSIONS = (
    ".c",
    ".cc",
    ".cpp",
    ".cxx",
    ".h",
    ".hh",
    ".hpp",
    ".hxx",
)


@dataclass(slots=True)
class ProjectMetadata:
    name: str
    description: str | None = None

    @classmethod
    def from_dict(
        cls,
        raw: dict[str, object],
        *,
        default_name: str,
    ) -> "ProjectMetadata":
        description = raw.get("description")
        return cls(
            name=str(raw.get("name", default_name)),
            description=str(description) if description else None,
        )


@dataclass(slots=True)
class EnreConfig:
    java_executable: str = "java"
    enre_jar_path: Path | None = None
    max_heap: str = "8g"
    snapshot_root: Path | None = None
    project_name: str | None = None
    extra_dirs: tuple[str, ...] = ()
    program_environments: tuple[str, ...] = ()
    raw_output_root: Path | None = None

    @classmethod
    def from_dict(
        cls,
        raw: dict[str, object],
        *,
        default_project_name: str,
        default_snapshot_root: Path,
        default_raw_output_root: Path,
    ) -> "EnreConfig":
        enre_jar_path = raw.get("enre_jar_path")
        snapshot_root = raw.get("snapshot_root")
        raw_output_root = raw.get("raw_output_root")

        return cls(
            java_executable=str(raw.get("java_executable", "java")),
            enre_jar_path=Path(enre_jar_path) if enre_jar_path else None,
            max_heap=str(raw.get("max_heap", "8g")),
            snapshot_root=Path(snapshot_root) if snapshot_root else default_snapshot_root,
            project_name=str(raw.get("project_name", default_project_name)),
            extra_dirs=tuple(str(item) for item in raw.get("extra_dirs", [])),
            program_environments=tuple(str(item) for item in raw.get("program_environments", [])),
            raw_output_root=Path(raw_output_root) if raw_output_root else default_raw_output_root,
        )

    def validate(self) -> None:
        if self.enre_jar_path is None:
            raise ValueError("config.enre.enre_jar_path must be set before running ENRE.")
        if self.snapshot_root is None:
            raise ValueError("config.enre.snapshot_root must be set before running ENRE.")
        if self.raw_output_root is None:
            raise ValueError("config.enre.raw_output_root must be set before running ENRE.")
        if not self.project_name:
            raise ValueError("config.enre.project_name must be set before running ENRE.")


@dataclass(slots=True)
class GenerationConfig:
    backend: str = "mock"
    model: str | None = None
    model_name: str | None = None
    base_url: str | None = None
    api_key: str | None = None
    api_key_env: str | None = None
    temperature: float = 0.2
    max_tokens: int = 256
    timeout_sec: int = 60
    max_retries: int = 2
    retry_backoff_sec: float = 1.5

    @classmethod
    def from_dict(cls, raw: dict[str, object]) -> "GenerationConfig":
        base_url = raw.get("base_url")
        api_key = raw.get("api_key")
        api_key_env = raw.get("api_key_env")
        model = raw.get("model")
        model_name = raw.get("model_name")
        return cls(
            backend=str(raw.get("backend", "mock")),
            model=str(model) if model else None,
            model_name=str(model_name) if model_name else None,
            base_url=str(base_url) if base_url else None,
            api_key=str(api_key) if api_key else None,
            api_key_env=str(api_key_env) if api_key_env else None,
            temperature=float(raw.get("temperature", 0.2)),
            max_tokens=int(raw.get("max_tokens", 256)),
            timeout_sec=int(raw.get("timeout_sec", 60)),
            max_retries=int(raw.get("max_retries", 2)),
            retry_backoff_sec=float(raw.get("retry_backoff_sec", 1.5)),
        )

    def validate(self) -> None:
        normalized_backend = self.backend.strip().lower()
        if normalized_backend not in {"mock", "openai", "openai-compatible"}:
            raise ValueError(
                "config.generation.backend must be one of: mock, openai, openai-compatible."
            )
        if self.max_tokens <= 0:
            raise ValueError("config.generation.max_tokens must be greater than 0.")
        if self.timeout_sec <= 0:
            raise ValueError("config.generation.timeout_sec must be greater than 0.")
        if self.max_retries < 0:
            raise ValueError("config.generation.max_retries must be 0 or greater.")
        if self.retry_backoff_sec < 0:
            raise ValueError("config.generation.retry_backoff_sec must be 0 or greater.")


@dataclass(slots=True)
class CmgConfig:
    strategy: str = "adaptive"
    matching_view: str = "strict"
    context_hops: int = 1
    matched_hops: int = 1
    sparse_matched_hops: int = 2
    unmatched_expand_hops: int = 1
    unmatched_source_window_lines: int = 80
    unmatched_expand_from_diff_calls: bool = True
    min_edges_for_sparse: int = 1
    include_parent_context: bool = True
    include_diff_calls: bool = True
    max_nodes: int = 30
    max_edges: int = 60

    @classmethod
    def from_dict(cls, raw: dict[str, object]) -> "CmgConfig":
        context_hops = int(raw.get("context_hops", 1))
        return cls(
            strategy=str(raw.get("strategy", "adaptive")),
            matching_view=str(raw.get("matching_view", "strict")),
            context_hops=context_hops,
            matched_hops=int(raw.get("matched_hops", context_hops)),
            sparse_matched_hops=int(raw.get("sparse_matched_hops", 2)),
            unmatched_expand_hops=int(raw.get("unmatched_expand_hops", 1)),
            unmatched_source_window_lines=int(raw.get("unmatched_source_window_lines", 80)),
            unmatched_expand_from_diff_calls=bool(raw.get("unmatched_expand_from_diff_calls", True)),
            min_edges_for_sparse=int(raw.get("min_edges_for_sparse", 1)),
            include_parent_context=bool(raw.get("include_parent_context", True)),
            include_diff_calls=bool(raw.get("include_diff_calls", True)),
            max_nodes=int(raw.get("max_nodes", 30)),
            max_edges=int(raw.get("max_edges", 60)),
        )

    def validate(self) -> None:
        normalized_strategy = self.strategy.strip().lower()
        if normalized_strategy not in {"strict_1hop", "adaptive"}:
            raise ValueError("config.cmg.strategy must be either 'strict_1hop' or 'adaptive'.")
        normalized_view = self.matching_view.strip().lower()
        if normalized_view not in {"strict", "rich"}:
            raise ValueError("config.cmg.matching_view must be either 'strict' or 'rich'.")
        for field_name, value in (
            ("context_hops", self.context_hops),
            ("matched_hops", self.matched_hops),
            ("sparse_matched_hops", self.sparse_matched_hops),
            ("unmatched_expand_hops", self.unmatched_expand_hops),
        ):
            if value < 0 or value > 2:
                raise ValueError(f"config.cmg.{field_name} must be between 0 and 2.")
        if self.matched_hops < 1:
            raise ValueError("config.cmg.matched_hops must be at least 1.")
        if self.sparse_matched_hops < self.matched_hops:
            raise ValueError("config.cmg.sparse_matched_hops must be >= config.cmg.matched_hops.")
        if self.unmatched_source_window_lines < 0:
            raise ValueError("config.cmg.unmatched_source_window_lines must be 0 or greater.")
        if self.min_edges_for_sparse < 0:
            raise ValueError("config.cmg.min_edges_for_sparse must be 0 or greater.")
        if self.max_nodes <= 0:
            raise ValueError("config.cmg.max_nodes must be greater than 0.")
        if self.max_edges <= 0:
            raise ValueError("config.cmg.max_edges must be greater than 0.")


@dataclass(slots=True)
class AppConfig:
    git_executable: str
    version_pair: VersionPair
    include_extensions: tuple[str, ...] = DEFAULT_EXTENSIONS
    diff_context_lines: int = 0
    output_dir: Path | None = None
    project: ProjectMetadata | None = None
    enre: EnreConfig | None = None
    cmg: CmgConfig = field(default_factory=CmgConfig)
    generation: GenerationConfig | None = None

    @classmethod
    def from_json_file(cls, path: str | Path) -> "AppConfig":
        raw = json.loads(Path(path).read_text(encoding="utf-8"))

        version_pair = VersionPair(
            repo_path=Path(raw["version_pair"]["repo_path"]),
            ref_version=raw["version_pair"]["ref_version"],
            tgt_version=raw["version_pair"]["tgt_version"],
        )

        output_dir = raw.get("output_dir")
        repo_workspace_root = version_pair.repo_path.parent
        project_raw = raw.get("project")
        project = None
        if isinstance(project_raw, dict):
            project = ProjectMetadata.from_dict(
                project_raw,
                default_name=version_pair.repo_path.name,
            )

        enre_raw = raw.get("enre")
        enre = None
        if isinstance(enre_raw, dict):
            enre = EnreConfig.from_dict(
                enre_raw,
                default_project_name=version_pair.repo_path.name,
                default_snapshot_root=repo_workspace_root / "version_snapshots",
                default_raw_output_root=Path(raw.get("output_dir")) / "enre_raw"
                if output_dir
                else repo_workspace_root / "enre_raw",
            )

        cmg_raw = raw.get("cmg")
        cmg = CmgConfig.from_dict(cmg_raw) if isinstance(cmg_raw, dict) else CmgConfig()

        generation_raw = raw.get("generation")
        generation = None
        if isinstance(generation_raw, dict):
            generation = GenerationConfig.from_dict(generation_raw)

        return cls(
            git_executable=raw.get("git_executable", "git"),
            version_pair=version_pair,
            include_extensions=tuple(raw.get("include_extensions", DEFAULT_EXTENSIONS)),
            diff_context_lines=int(raw.get("diff_context_lines", 0)),
            output_dir=Path(output_dir) if output_dir else None,
            project=project,
            enre=enre,
            cmg=cmg,
            generation=generation,
        )

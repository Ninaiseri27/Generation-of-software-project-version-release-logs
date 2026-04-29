from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import subprocess
import shutil
import time

from ..config import AppConfig
from .version_snapshot import VersionSnapshot, VersionSnapshotPair


def sanitize_component(value: str) -> str:
    invalid = '<>:"/\\|?*'
    result = "".join("_" if char in invalid else char for char in value.strip())
    if not result:
        raise ValueError("Path component resolved to an empty string.")
    return result


@dataclass(slots=True)
class EnreRunResult:
    version: str
    snapshot_path: Path
    working_dir: Path
    project_alias: str
    output_json_path: Path
    stdout_log_path: Path
    stderr_log_path: Path
    command: list[str]
    duration_seconds: float
    reused_existing_output: bool

    def to_dict(self) -> dict[str, object]:
        return {
            "version": self.version,
            "snapshot_path": str(self.snapshot_path),
            "working_dir": str(self.working_dir),
            "project_alias": self.project_alias,
            "output_json_path": str(self.output_json_path),
            "stdout_log_path": str(self.stdout_log_path),
            "stderr_log_path": str(self.stderr_log_path),
            "command": self.command,
            "duration_seconds": self.duration_seconds,
            "reused_existing_output": self.reused_existing_output,
        }


class EnreRunner:
    def __init__(
        self,
        *,
        java_executable: Path,
        enre_jar_path: Path,
        max_heap: str,
        raw_output_root: Path,
        project_name: str,
        extra_dirs: tuple[str, ...] = (),
        program_environments: tuple[str, ...] = (),
    ) -> None:
        self.java_executable = java_executable
        self.enre_jar_path = enre_jar_path
        self.max_heap = max_heap
        self.raw_output_root = raw_output_root
        self.project_name = project_name
        self.extra_dirs = extra_dirs
        self.program_environments = program_environments

    @classmethod
    def from_app_config(cls, config: AppConfig) -> "EnreRunner":
        if config.enre is None:
            raise ValueError("The config must contain an 'enre' section to run ENRE.")
        config.enre.validate()
        return cls(
            java_executable=Path(config.enre.java_executable),
            enre_jar_path=config.enre.enre_jar_path,
            max_heap=config.enre.max_heap,
            raw_output_root=config.enre.raw_output_root,
            project_name=config.enre.project_name or config.version_pair.repo_path.name,
            extra_dirs=config.enre.extra_dirs,
            program_environments=config.enre.program_environments,
        )

    def run_for_pair(self, pair: VersionSnapshotPair, *, target: str = "both") -> dict[str, object]:
        results: dict[str, object] = {
            "repo_path": str(pair.repo_path),
            "target": target,
            "runs": {},
        }

        if target in {"ref", "both"}:
            results["runs"]["ref"] = self.run_on_snapshot(pair.ref).to_dict()
        if target in {"tgt", "both"}:
            results["runs"]["tgt"] = self.run_on_snapshot(pair.tgt).to_dict()

        return results

    def run_on_snapshot(self, snapshot: VersionSnapshot) -> EnreRunResult:
        self._validate_runtime()

        version_name = sanitize_component(snapshot.version)
        project_name = sanitize_component(self.project_name)
        project_alias = f"{project_name}__{version_name}"
        working_dir = self.raw_output_root / project_name / version_name
        working_dir.mkdir(parents=True, exist_ok=True)

        output_json_path = working_dir / f"{project_alias}_out.json"
        stdout_log_path = working_dir / "enre.stdout.log"
        stderr_log_path = working_dir / "enre.stderr.log"

        command = [
            str(self.java_executable),
            f"-Xmx{self.max_heap}",
            "-jar",
            str(self.enre_jar_path),
        ]

        for extra_dir in self._resolve_paths(snapshot, self.extra_dirs):
            command.append(f"-d={extra_dir}")
        for program_environment in self._resolve_paths(snapshot, self.program_environments):
            command.append(f"-p={program_environment}")

        command.extend([str(snapshot.path), project_alias])

        if output_json_path.exists():
            return EnreRunResult(
                version=snapshot.version,
                snapshot_path=snapshot.path,
                working_dir=working_dir,
                project_alias=project_alias,
                output_json_path=output_json_path,
                stdout_log_path=stdout_log_path,
                stderr_log_path=stderr_log_path,
                command=command,
                duration_seconds=0.0,
                reused_existing_output=True,
            )

        started_at = time.perf_counter()
        completed = subprocess.run(
            command,
            cwd=working_dir,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=False,
        )
        duration_seconds = time.perf_counter() - started_at

        stdout_log_path.write_text(completed.stdout, encoding="utf-8")
        stderr_log_path.write_text(completed.stderr, encoding="utf-8")

        if completed.returncode != 0:
            raise RuntimeError(
                "ENRE-CPP execution failed. "
                f"version={snapshot.version} working_dir={working_dir} stderr_log={stderr_log_path}"
            )
        if not output_json_path.exists():
            raise RuntimeError(
                "ENRE-CPP finished but the expected output JSON was not created. "
                f"expected={output_json_path}"
            )

        return EnreRunResult(
            version=snapshot.version,
            snapshot_path=snapshot.path,
            working_dir=working_dir,
            project_alias=project_alias,
            output_json_path=output_json_path,
            stdout_log_path=stdout_log_path,
            stderr_log_path=stderr_log_path,
            command=command,
            duration_seconds=duration_seconds,
            reused_existing_output=False,
        )

    def _validate_runtime(self) -> None:
        java_text = str(self.java_executable)
        if not self.java_executable.exists() and not shutil.which(java_text):
            raise ValueError(
                f"Configured Java executable does not exist or is not on PATH: {self.java_executable}"
            )
        if not self.enre_jar_path.exists():
            raise ValueError(f"Configured ENRE jar does not exist: {self.enre_jar_path}")

    @staticmethod
    def _resolve_paths(snapshot: VersionSnapshot, entries: tuple[str, ...]) -> list[str]:
        resolved: list[str] = []
        for entry in entries:
            raw = Path(entry)
            if raw.is_absolute():
                resolved.append(str(raw))
            else:
                resolved.append(str(snapshot.path / raw))
        return resolved

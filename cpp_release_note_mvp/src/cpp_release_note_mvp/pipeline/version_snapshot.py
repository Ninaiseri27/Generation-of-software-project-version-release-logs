from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path
import shutil
import subprocess

from ..config import AppConfig
from ..models import VersionPair
from .git_utils import run_git


INVALID_PATH_CHARS_RE = re.compile(r'[<>:"/\\|?*]')


@dataclass(slots=True)
class VersionSnapshot:
    version: str
    path: Path
    commit: str

    def to_dict(self) -> dict[str, str]:
        return {
            "version": self.version,
            "path": str(self.path),
            "commit": self.commit,
        }


@dataclass(slots=True)
class VersionSnapshotPair:
    repo_path: Path
    ref: VersionSnapshot
    tgt: VersionSnapshot

    def to_dict(self) -> dict[str, object]:
        return {
            "repo_path": str(self.repo_path),
            "ref": self.ref.to_dict(),
            "tgt": self.tgt.to_dict(),
        }


class VersionSnapshotManager:
    def __init__(
        self,
        *,
        repo_path: Path,
        git_executable: str,
        snapshot_root: Path,
        project_name: str,
    ) -> None:
        self.repo_path = repo_path
        self.git_executable = git_executable
        self.snapshot_root = snapshot_root
        self.project_name = project_name

    @classmethod
    def from_app_config(cls, config: AppConfig) -> "VersionSnapshotManager":
        if config.enre is None:
            raise ValueError("The config must contain an 'enre' section for snapshot management.")
        if config.enre.snapshot_root is None:
            raise ValueError("The config.enre.snapshot_root must be set.")
        if not config.enre.project_name:
            raise ValueError("The config.enre.project_name must be set.")

        return cls(
            repo_path=config.version_pair.repo_path,
            git_executable=config.git_executable,
            snapshot_root=config.enre.snapshot_root,
            project_name=config.enre.project_name,
        )

    @property
    def project_snapshot_root(self) -> Path:
        return self.snapshot_root / self._sanitize_path_component(self.project_name)

    def snapshot_path_for_version(self, version: str) -> Path:
        return self.project_snapshot_root / self._sanitize_path_component(version)

    def ensure_version_pair(self, version_pair: VersionPair) -> VersionSnapshotPair:
        self._ensure_git_repo()
        self._prune_worktrees()
        self.project_snapshot_root.mkdir(parents=True, exist_ok=True)

        ref_snapshot = self.ensure_snapshot(version_pair.ref_version)
        tgt_snapshot = self.ensure_snapshot(version_pair.tgt_version)

        return VersionSnapshotPair(
            repo_path=self.repo_path,
            ref=ref_snapshot,
            tgt=tgt_snapshot,
        )

    def ensure_version_pair_payload(self, version_pair: VersionPair) -> dict[str, object]:
        pair = self.ensure_version_pair(version_pair)
        return pair.to_dict()

    def ensure_snapshot(self, version: str) -> VersionSnapshot:
        snapshot_path = self.snapshot_path_for_version(version)
        expected_commit = self._resolve_commit(version)

        if snapshot_path.exists():
            self._validate_existing_snapshot(snapshot_path, expected_commit)
            return VersionSnapshot(version=version, path=snapshot_path, commit=expected_commit)

        try:
            run_git(
                self.repo_path,
                self.git_executable,
                [
                    "worktree",
                    "add",
                    "--detach",
                    str(snapshot_path),
                    version,
                ],
            )
        except subprocess.CalledProcessError as exc:
            self._cleanup_failed_snapshot(snapshot_path)
            raise ValueError(
                "Failed to create git worktree snapshot. "
                "If the repository is a partial clone, Git may need to fetch missing objects for this version. "
                f"repo={self.repo_path} version={version} snapshot_path={snapshot_path}"
            ) from exc

        return VersionSnapshot(version=version, path=snapshot_path, commit=expected_commit)

    def _ensure_git_repo(self) -> None:
        git_dir = self.repo_path / ".git"
        if not git_dir.exists():
            raise ValueError(f"Not a git repository: {self.repo_path}")

    def _prune_worktrees(self) -> None:
        run_git(self.repo_path, self.git_executable, ["worktree", "prune"])

    def _validate_existing_snapshot(self, snapshot_path: Path, expected_commit: str) -> None:
        if not snapshot_path.is_dir():
            raise ValueError(f"Snapshot path exists but is not a directory: {snapshot_path}")

        git_marker = snapshot_path / ".git"
        if not git_marker.exists():
            if any(snapshot_path.iterdir()):
                raise ValueError(
                    f"Snapshot path already exists and is not a git worktree directory: {snapshot_path}"
                )
            raise ValueError(
                f"Snapshot path exists as an empty directory. Remove it and rerun: {snapshot_path}"
            )

        current_commit = self._get_head_commit(snapshot_path)
        if current_commit != expected_commit:
            raise ValueError(
                "Snapshot path already exists but points to a different commit: "
                f"{snapshot_path} ({current_commit} != {expected_commit})"
            )

    def _cleanup_failed_snapshot(self, snapshot_path: Path) -> None:
        if snapshot_path.exists():
            shutil.rmtree(snapshot_path, ignore_errors=True)
        worktree_ref = self.repo_path / ".git" / "worktrees" / snapshot_path.name
        if worktree_ref.exists():
            shutil.rmtree(worktree_ref, ignore_errors=True)
        self._prune_worktrees()

    def _resolve_commit(self, version: str) -> str:
        return run_git(
            self.repo_path,
            self.git_executable,
            ["rev-parse", f"{version}^{{commit}}"],
        ).strip()

    def _get_head_commit(self, repo_path: Path) -> str:
        try:
            return run_git(repo_path, self.git_executable, ["rev-parse", "HEAD"]).strip()
        except subprocess.CalledProcessError as exc:
            raise ValueError(f"Failed to read HEAD for snapshot path: {repo_path}") from exc

    @staticmethod
    def _sanitize_path_component(value: str) -> str:
        sanitized = INVALID_PATH_CHARS_RE.sub("_", value.strip())
        if not sanitized:
            raise ValueError("Snapshot path component resolved to an empty string.")
        return sanitized

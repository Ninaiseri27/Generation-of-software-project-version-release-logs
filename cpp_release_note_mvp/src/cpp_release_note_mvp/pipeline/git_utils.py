from __future__ import annotations

import re
import subprocess
from pathlib import Path

from ..config import AppConfig
from ..models import DiffHunk


HUNK_HEADER_RE = re.compile(r"^@@ -(?P<old_start>\d+)(?:,(?P<old_count>\d+))? \+(?P<new_start>\d+)(?:,(?P<new_count>\d+))? @@")


def run_git(repo_path: Path, git_executable: str, args: list[str]) -> str:
    command = [
        git_executable,
        "-c",
        "core.quotepath=false",
        "-c",
        "i18n.logOutputEncoding=utf-8",
        "-c",
        "i18n.commitEncoding=utf-8",
        "-C",
        str(repo_path),
        *args,
    ]
    completed = subprocess.run(
        command,
        check=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
    )
    return completed.stdout


def list_changed_files(config: AppConfig) -> list[str]:
    output = run_git(
        config.version_pair.repo_path,
        config.git_executable,
        [
            "diff",
            "--name-only",
            "--diff-filter=ADM",
            config.version_pair.ref_version,
            config.version_pair.tgt_version,
            "--",
        ],
    )

    files = [line.strip() for line in output.splitlines() if line.strip()]
    return [path for path in files if Path(path).suffix.lower() in set(config.include_extensions)]


def get_unified_diff(config: AppConfig, relative_paths: list[str] | None = None) -> str:
    args = [
        "diff",
        f"--unified={config.diff_context_lines}",
        "--diff-filter=ADM",
        config.version_pair.ref_version,
        config.version_pair.tgt_version,
        "--",
    ]
    if relative_paths:
        args.extend(relative_paths)
    return run_git(config.version_pair.repo_path, config.git_executable, args)


def get_commit_messages(config: AppConfig) -> list[str]:
    output = run_git(
        config.version_pair.repo_path,
        config.git_executable,
        [
            "log",
            "--pretty=format:%s",
            f"{config.version_pair.ref_version}..{config.version_pair.tgt_version}",
        ],
    )
    return [line.strip() for line in output.splitlines() if line.strip()]


def get_file_content(repo_path: Path, git_executable: str, version: str, relative_path: str) -> str:
    try:
        return run_git(repo_path, git_executable, ["show", f"{version}:{relative_path}"])
    except subprocess.CalledProcessError:
        return ""


def parse_unified_diff(diff_text: str) -> dict[str, list[DiffHunk]]:
    hunks_by_file: dict[str, list[DiffHunk]] = {}
    current_file: str | None = None
    current_hunk: DiffHunk | None = None
    current_old_file: str | None = None
    current_new_file: str | None = None

    for raw_line in diff_text.splitlines():
        if raw_line.startswith("diff --git "):
            if current_hunk and current_file:
                hunks_by_file.setdefault(current_file, []).append(current_hunk)
            current_hunk = None
            parts = raw_line.split()
            current_old_file = parts[2][2:] if len(parts) > 2 and parts[2].startswith("a/") else None
            current_new_file = parts[3][2:] if len(parts) > 3 and parts[3].startswith("b/") else None
            current_file = current_new_file or current_old_file
            continue

        if raw_line == "--- /dev/null":
            current_old_file = None
            continue

        if raw_line.startswith("--- a/"):
            current_old_file = raw_line[6:]
            if current_file is None:
                current_file = current_old_file
            continue

        if raw_line == "+++ /dev/null":
            current_new_file = None
            current_file = current_old_file
            continue

        if raw_line.startswith("+++ b/"):
            current_new_file = raw_line[6:]
            current_file = current_new_file
            hunks_by_file.setdefault(current_file, [])
            continue

        header_match = HUNK_HEADER_RE.match(raw_line)
        if header_match:
            if current_hunk and current_file:
                hunks_by_file.setdefault(current_file, []).append(current_hunk)

            current_hunk = DiffHunk(
                file_path=current_file or "",
                old_start=int(header_match.group("old_start")),
                old_count=int(header_match.group("old_count") or "1"),
                new_start=int(header_match.group("new_start")),
                new_count=int(header_match.group("new_count") or "1"),
                lines=[],
            )
            continue

        if current_hunk is not None:
            current_hunk.lines.append(raw_line)

    if current_hunk and current_file:
        hunks_by_file.setdefault(current_file, []).append(current_hunk)

    return hunks_by_file

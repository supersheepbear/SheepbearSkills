#!/usr/bin/env python3
"""Summarize git working-tree changes as JSON."""

from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path


def run_git(root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    """Run a git command in root."""

    return subprocess.run(
        ["git", *args],
        cwd=root,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def parse_porcelain(output: str) -> list[dict[str, str]]:
    """Parse `git status --short` output."""

    changes: list[dict[str, str]] = []
    for line in output.splitlines():
        if not line:
            continue
        status = line[:2]
        path = line[3:] if len(line) > 3 else ""
        changes.append({"status": status, "path": path})
    return changes


def summarize(root: Path) -> dict[str, object]:
    """Return branch and working-tree change summary."""

    status = run_git(root, ["status", "--short"])
    branch = run_git(root, ["branch", "--show-current"])
    staged = run_git(root, ["diff", "--name-only", "--cached"])
    unstaged = run_git(root, ["diff", "--name-only"])

    if status.returncode != 0:
        return {
            "ok": False,
            "error": status.stderr.strip() or "git status failed",
        }

    return {
        "ok": True,
        "branch": branch.stdout.strip(),
        "changes": parse_porcelain(status.stdout),
        "staged": [line for line in staged.stdout.splitlines() if line],
        "unstaged": [line for line in unstaged.stdout.splitlines() if line],
    }


def main() -> int:
    """CLI entry point."""

    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    print(json.dumps(summarize(Path(args.root).resolve()), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

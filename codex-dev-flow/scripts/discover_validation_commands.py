#!/usr/bin/env python3
"""Discover likely validation commands for a repository.

The script is intentionally conservative. It reads common metadata files and
prints JSON suggestions with evidence paths. Humans or agents should still
choose the command that matches the touched files.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


COMMAND_PATTERNS: tuple[tuple[str, str], ...] = (
    (r"\bmake\s+test\b", "test"),
    (r"\bmake\s+docs-test\b", "docs"),
    (r"\bmake\s+lint\b", "lint"),
    (r"\bmake\s+typecheck\b", "typecheck"),
    (r"\buv\s+run\s+pytest\b", "test"),
    (r"\bpytest\b", "test"),
    (r"\bnpm\s+test\b", "test"),
    (r"\bnpm\s+run\s+lint\b", "lint"),
    (r"\bnpm\s+run\s+typecheck\b", "typecheck"),
    (r"\bcargo\s+test\b", "test"),
    (r"\bgo\s+test\s+\./\.\.\.\b", "test"),
    (r"\bdotnet\s+test\b", "test"),
)

DOC_FILES = (
    "AGENTS.md",
    "README.md",
    "README.rst",
    "CONTRIBUTING.md",
    "Makefile",
    "justfile",
    "Taskfile.yml",
    "pyproject.toml",
    "package.json",
)


def read_text(path: Path) -> str:
    """Return file text with tolerant decoding."""

    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def add_command(
    commands: dict[str, dict[str, Any]],
    command: str,
    kind: str,
    source: str,
) -> None:
    """Add a command suggestion keyed by command string."""

    entry = commands.setdefault(
        command,
        {"command": command, "kind": kind, "sources": []},
    )
    if source not in entry["sources"]:
        entry["sources"].append(source)


def discover_from_text(path: Path, commands: dict[str, dict[str, Any]]) -> None:
    """Find command-looking snippets in documentation text."""

    text = read_text(path)
    for pattern, kind in COMMAND_PATTERNS:
        for match in re.finditer(pattern, text):
            add_command(commands, match.group(0), kind, str(path))


def discover_from_makefile(path: Path, commands: dict[str, dict[str, Any]]) -> None:
    """Discover simple Makefile targets."""

    text = read_text(path)
    for line in text.splitlines():
        if line.startswith("\t") or ":" not in line:
            continue
        target = line.split(":", 1)[0].strip()
        if not target or target.startswith(".") or " " in target:
            continue
        lower = target.lower()
        if lower in {"test", "docs-test", "lint", "typecheck", "format"}:
            kind = "docs" if "docs" in lower else lower
            add_command(commands, f"make {target}", kind, str(path))


def discover_from_package_json(
    path: Path,
    commands: dict[str, dict[str, Any]],
) -> None:
    """Discover npm scripts from package.json."""

    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError:
        return
    scripts = data.get("scripts")
    if not isinstance(scripts, dict):
        return
    for name in scripts:
        lower = name.lower()
        if lower in {"test", "lint", "typecheck", "build", "format"}:
            add_command(commands, f"npm run {name}", lower, str(path))


def discover(root: Path) -> list[dict[str, Any]]:
    """Discover validation command candidates under root."""

    commands: dict[str, dict[str, Any]] = {}

    for name in DOC_FILES:
        path = root / name
        if not path.exists() or not path.is_file():
            continue
        if name == "Makefile":
            discover_from_makefile(path, commands)
        elif name == "package.json":
            discover_from_package_json(path, commands)
        discover_from_text(path, commands)

    workflow_dir = root / ".github" / "workflows"
    if workflow_dir.exists():
        for path in sorted(workflow_dir.glob("*.y*ml")):
            discover_from_text(path, commands)

    return sorted(commands.values(), key=lambda item: (item["kind"], item["command"]))


def main() -> int:
    """CLI entry point."""

    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    print(json.dumps(discover(root), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

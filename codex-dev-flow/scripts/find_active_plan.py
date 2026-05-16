#!/usr/bin/env python3
"""Find the most likely active Codex dev-flow plan."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


PLAN_DIRS = (".codex/plans", ".github")
PLAN_PATTERNS = ("*.md", "scratchpad_*.md")


def find_plans(root: Path) -> list[Path]:
    """Return candidate plan files sorted newest first."""

    candidates: list[Path] = []
    for directory in PLAN_DIRS:
        base = root / directory
        if not base.exists():
            continue
        for pattern in PLAN_PATTERNS:
            candidates.extend(path for path in base.glob(pattern) if path.is_file())

    return sorted(candidates, key=lambda path: path.stat().st_mtime, reverse=True)


def main() -> int:
    """CLI entry point."""

    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    plans = find_plans(root)

    if args.json:
        print(json.dumps([str(path) for path in plans], indent=2))
    elif plans:
        print(plans[0])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

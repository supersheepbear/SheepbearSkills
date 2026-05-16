#!/usr/bin/env python3
"""Validate that a Codex dev-flow plan has the required sections."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


REQUIRED_SECTIONS = (
    "## 0. Control",
    "## 1. Request History",
    "## 2. Repository Context",
    "## 2.1 Preflight",
    "## 2.2 Automation Authorization",
    "## 3. Plan History",
    "## 4. Requirements And Assumptions",
    "## 4.1 Root Cause And Code Audit",
    "## 4.2 Policy Exceptions",
    "## 6.1 Approach Tradeoffs",
    "## 7. Tasks",
    "## 9. Validation Log",
    "## 9.1 Docs Impact",
    "## 10. Review Findings",
    "## 13. Handoff Notes",
)


def read_text(path: Path) -> str:
    """Return file text with tolerant decoding."""

    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(errors="replace")


def validate(path: Path) -> dict[str, object]:
    """Validate a plan file and return a JSON-serializable report."""

    text = read_text(path)
    missing = [section for section in REQUIRED_SECTIONS if section not in text]
    task_ids = sorted(set(re.findall(r"\bT-\d{3}\b", text)))
    request_ids = sorted(set(re.findall(r"\bREQ-\d{3}\b", text)))
    finding_ids = sorted(set(re.findall(r"\bFIND-\d{3}\b", text)))
    validation_ids = sorted(set(re.findall(r"\bVAL-\d{3}\b", text)))

    has_next_action = "**Next Action**:" in text
    has_done_when = "**Done When**:" in text

    errors: list[str] = []
    if missing:
        errors.append("missing required sections")
    if not has_next_action:
        errors.append("missing next action")
    if not has_done_when:
        errors.append("missing done-when criteria")

    return {
        "path": str(path),
        "ok": not errors,
        "errors": errors,
        "missing_sections": missing,
        "counts": {
            "requests": len(request_ids),
            "tasks": len(task_ids),
            "findings": len(finding_ids),
            "validations": len(validation_ids),
        },
    }


def main() -> int:
    """CLI entry point."""

    parser = argparse.ArgumentParser()
    parser.add_argument("plan")
    args = parser.parse_args()

    report = validate(Path(args.plan).resolve())
    print(json.dumps(report, indent=2))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())

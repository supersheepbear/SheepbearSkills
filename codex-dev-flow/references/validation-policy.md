# Validation Policy

Validation is evidence, not ceremony. Discover the repo's real commands before inventing generic ones.

## Command Discovery Order

1. `AGENTS.md` and nested agent instructions.
2. README, docs, contributing guide, architecture docs.
3. Makefile, justfile, taskfile, npm scripts, pyproject scripts, tox/nox, cargo, go, gradle, maven, dotnet.
4. CI workflow files.
5. Existing plan or context pack.

Use `scripts/discover_validation_commands.py` to collect candidates quickly, then apply judgment.

## Execution Order

1. Smallest relevant check for the touched area.
2. Related unit tests.
3. Lint/type/docs checks when touched files require them.
4. Full required check before final handoff or check-in.

## Evidence Rules

- Record exact command, purpose, result, and timestamp in the active plan.
- Never say "passes" unless the command ran and exited successfully.
- If a command is unavailable, record `not run` with the reason.
- Summarize long logs. Keep full logs out of the active plan unless the user asks.
- Failed validation creates a `FIND-*` entry and usually a remediation task.

## Suggested Result Values

- `pass`: command ran and succeeded.
- `fail`: command ran and failed.
- `not-run`: intentionally skipped or unavailable.
- `blocked`: could not run because of missing environment, credentials, service, or dependency.

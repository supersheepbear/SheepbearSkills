# Migration From Developer Modes

This skill is a Codex-native successor to `developer-modes`, not a literal port.

## Keep

- explicit workflow modes,
- plan-driven development,
- one-task-at-a-time and all-tasks-together execution scopes,
- strict validation evidence,
- issue and PR drafting,
- Python and pytest discipline when relevant.

## Change

- `planner` becomes `plan`.
- `executor` becomes `execute`.
- repo-context behavior becomes `context` mode.
- detailed human-readable repo summaries become `repo-overview` mode.
- read-only question answering and external/docs investigation become `research` mode.
- `help` mode is added for mode-selection guidance.
- `review` becomes a first-class mode.
- `handoff` is added for continuation summaries.
- task-level handoff becomes an automatic active-plan update; full session handoff remains user-triggered.
- automation modes `ship`, `auto-ship`, `merge`, `sync`, and `super-ship` are added for gated multi-phase workflows.
- `.github/scratchpad_*` becomes optional; default state is `.codex/plans/`.
- Python and pytest rules become conditional references.
- `CONFIDENCE_GATE` becomes a risk-based clarification gate.
- `/repo-context` and `.github/.context` are no longer hard dependencies.
- Durable repo facts move to `AGENTS.md` or docs instead of the task plan.

## Remove

- unsupported SKILL.md frontmatter keys such as `argument-hint`, `user-invocable`, and `disable-model-invocation`,
- hardcoded `make test` and `make docs-test` as universal commands,
- reviewer behavior hidden inside an executor scratchpad section.

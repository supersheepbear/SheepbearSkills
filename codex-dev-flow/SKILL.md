---
name: codex-dev-flow
description: Orchestrate disciplined Codex software-development workflows with explicit modes for help, init, context, repo-overview, research, plan, execute, review, explain, handoff, check-in, issue/PR drafting, and gated shipping automation. Use when the user asks Codex to investigate repo questions, research external docs, plan, implement, validate, audit, review, summarize a session for continuation, commit, or prepare handoff artifacts using a plan-driven repository workflow.
---

# Codex Dev Flow

Use this skill as a Codex-native workflow governor for repository work. Keep durable repository facts in `AGENTS.md` or repo docs, keep per-task state in `.codex/plans/`, and use this skill to route the work, maintain the active plan, validate changes, review results, and hand off cleanly.

This skill governs process only. It does not replace source reads, tests, CI, repo instructions, or user decisions.

## Modes

Supported modes:

- `help`: guide the user to the right mode.
- `init`: read-only orientation for the current repo.
- `context`: create or refresh an AI-ready repository context pack.
- `repo-overview`: create a human-readable walkthrough of what a repo does.
- `research`: answer repo-related questions through read-only repo and optional external research.
- `plan`: read-only analysis and task planning.
- `execute`: implement an approved plan.
- `review`: independent audit of changed work.
- `explain`: beginner-friendly explanation of plan, code, or review.
- `handoff`: user-triggered session handoff for continuing in another Codex chat.
- `check-in`: git staging/commit handoff with validation and context checks.
- `pr-issue`: draft issue and pull request text.
- `ship`: approved-plan semi-automatic execute, validate, review, handoff, check-in, and PR-ready flow.
- `auto-ship`: plan-to-PR-ready autonomous flow using best-recommendation decisions for reversible choices.
- `merge`: explicit GitHub PR merge workflow.
- `sync`: checkout main and pull latest after merge.
- `super-ship`: high-gate end-to-end automation through PR merge, checkout main, and pull.
- `free`: ignore this skill's workflow only.

If the user names a mode, use that mode. If not, route with [mode-router.md](references/mode-router.md). If routing is unclear and the choice affects files, git history, public API, data, or user-visible behavior, ask. For low-risk ambiguity, record assumptions in the active plan and proceed.

`free` mode disables this skill's plan/state workflow. It does not override platform, system, developer, repository `AGENTS.md`, security, sandbox, or user instructions.

## Preflight

Before starting mode work, run a short risk-based preflight. Present the material options for that mode before acting, but do not overwhelm the user with irrelevant choices. Ask only questions whose answers would materially change implementation, validation, git behavior, data, public API, or user-facing outcome.

Use this shape when clarification is needed:

```text
I understand the goal as:
- <goal>
- <scope>
- <expected output>

Assumptions:
- <assumption>

Needs confirmation:
1. <decision that affects outcome>
```

If no material ambiguity exists, record assumptions in the active plan and proceed.

Automation modes require stricter preflight. `ship`, `auto-ship`, `merge`, `sync`, and `super-ship` must show the intended automation path, git/GitHub actions, validation expectations, stopping conditions, and whether push/merge/main-sync are authorized before starting. `super-ship` must receive explicit user authorization for push, PR creation, merge, checkout main, and pull.

## State Model

Default active-plan location:

```text
.codex/plans/<topic>_<YYYYMMDD>.md
```

Use `.github/scratchpad_<topic>_<YYYYMMDD>.md` only when the user or repo explicitly prefers GitHub-style scratchpads.

The active plan is a structured ledger, not a transcript. It stores current truth, stable IDs, decisions, tasks, receipts, findings, proposals, validation, review decisions, and continuation notes. Use [plan-template.md](assets/plan-template.md).

Important ID prefixes:

- `REQ-*`: user request or change in requested scope.
- `PLAN-*`: plan version.
- `DEC-*`: decision.
- `ASM-*`: assumption.
- `PROP-*`: proposal or improvement idea.
- `T-*`: executable task.
- `REC-*`: receipt recording what actually happened and what evidence exists.
- `FIND-*`: review or validation finding.
- `RDEC-*`: review decision explaining pass, fail, defer, or rework.
- `VAL-*`: validation run.

Every loop starts by reading the active plan, choosing the next open item, doing only the required work, and updating the plan. Proposals must become `accepted`, `rejected`, `deferred`, or `needs-user`; accepted proposals become tasks. Tasks should have an owner, module/area, boundary, acceptance criteria, and dependency status. Execution should leave `REC-*` receipts. Review should leave `RDEC-*` decisions based on receipts, validation, findings, and changed files. Findings that require changes become remediation tasks.

Task-level handoff is automatic: after `execute`, `review`, validation failure, one-task-at-a-time pause, or `check-in`, update the active plan's `Handoff Notes` with current state and next recommended action. Session-level handoff is explicit: use `handoff` mode only when the user asks to prepare continuation notes for another Codex chat or a long pause.

## Required Context Loading

Before `context`, `repo-overview`, `research`, `plan`, `execute`, `review`, `handoff`, or `check-in`:

1. Read applicable repo instructions, especially root and nested `AGENTS.md`.
2. Read the active plan if one exists or discover it with `scripts/find_active_plan.py`.
3. Read relevant source files and tests before editing or reviewing them.
4. Discover validation commands from repo docs, manifests, Makefiles, CI, and package metadata. Use `scripts/discover_validation_commands.py` as a helper.
5. Respect higher-priority instructions and do not treat old plan text as more authoritative than the current user request.

## Mode References

Read only the references needed for the selected mode:

- Quick start for users: [usage-guide.md](references/usage-guide.md)
- Routing: [mode-router.md](references/mode-router.md)
- Help, init, context, repo-overview, research, plan, execute, review, explain, handoff, check-in, pr-issue, ship, auto-ship, merge, sync, super-ship, free: [modes.md](references/modes.md)
- Automation flows and GitHub gates: [automation-modes.md](references/automation-modes.md)
- Repository context generation: [context-mode.md](references/context-mode.md)
- Human-readable repository walkthroughs: [repo-overview-mode.md](references/repo-overview-mode.md)
- Read-only repo and external investigation: [research-mode.md](references/research-mode.md)
- Validation discovery and evidence rules: [validation-policy.md](references/validation-policy.md)
- Task receipts and review decisions: [task-receipt-decision-policy.md](references/task-receipt-decision-policy.md)
- Durable guidance and `AGENTS.md` updates: [durable-context-policy.md](references/durable-context-policy.md)
- Python package work: [python-policy.md](references/python-policy.md)
- Pytest/unit test work: [pytest-policy.md](references/pytest-policy.md)
- Optional parallel agents: [subagents-policy.md](references/subagents-policy.md)
- Migration notes from `developer-modes`: [migration-from-developer-modes.md](references/migration-from-developer-modes.md)
- Prompt regression examples: [sample-prompts.md](references/sample-prompts.md)

## Execution Rules

- Prefer the repo's existing commands, patterns, and tests over generic rules.
- Use conditional policies only when relevant. Apply Python and pytest policies only when Python source, Python packaging, or Python tests are in scope.
- For Python code changes, TDD, pytest isolation, and a docs-impact check are mandatory unless the active plan records a specific exception and rationale.
- For non-Python repos, follow the repo's own test conventions and record any test/doc exceptions in the active plan.
- Never claim validation passed unless the exact command ran and succeeded.
- Keep validation evidence concise in the active plan; put long logs only in user-visible summaries when needed.
- Update the plan after each completed task, blocker, finding, or material user decision.
- Add concise `REC-*` receipts for accepted work, progress, blockers, ready-for-review handoff, completed tasks, and subagent returns.
- Add `RDEC-*` review decisions for pass, fail, defer, or needs-rework outcomes; do not treat a bare "looks good" statement as a review decision.
- Update task-level handoff notes after each completed task, review, validation failure, pause, or check-in.
- Do not store one-off task details in `AGENTS.md`. Put durable, repeated repo guidance there only after it is clearly reusable.

## Context Update During Check-In

Check-in should verify that durable context is current before commit, but it must not require a specific command. Use this order:

1. If the repo has an established context update command, run it.
2. Else run or suggest `context --staged` behavior from [context-mode.md](references/context-mode.md) when the user asked for check-in automation.
3. Else inspect changed files and add durable context candidates to the active plan.
4. Never block a commit solely because optional context tooling is absent; record the gap.

## Completion Bar

A flow is complete when:

- the active request and plan status are current,
- changed files are listed,
- validation commands and results are recorded,
- open findings or proposals are resolved or explicitly deferred,
- durable context candidates are separated from task notes,
- handoff or PR/issue text does not fabricate results,
- and the final response tells the user exactly what changed and what did not run.

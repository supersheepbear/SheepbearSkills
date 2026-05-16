# Codex Dev Flow Usage Guide

Use this skill when you want Codex to work from a clear plan, track decisions, validate changes, review results, and leave a clean handoff.

## Quick Start

Start with one of these prompts:

```text
Use $codex-dev-flow help to choose the right mode for my task.
```

```text
Use $codex-dev-flow init to orient yourself in this repo.
```

```text
Use $codex-dev-flow context to create an AI-ready repo context pack.
```

```text
Use $codex-dev-flow repo-overview to write a detailed human-readable walkthrough of what this repo can do.
```

```text
Use $codex-dev-flow research to answer this repo question without editing files: <question>
```

```text
Use $codex-dev-flow plan to design the change before implementation: <goal>
```

```text
Use $codex-dev-flow execute one-task-at-a-time for the approved plan.
```

```text
Use $codex-dev-flow review the current diff against the active plan.
```

```text
Use $codex-dev-flow handoff to summarize this session for a future Codex chat.
```

## Common Flow

1. `init`: load repo context and commands.
2. `context`: create or refresh `.codex/context/` when repo-level context is missing or stale.
3. `repo-overview`: write a human-readable repo walkthrough when the user wants understanding rather than coding context.
4. `research`: answer repo questions or investigate risks without editing files.
5. `plan`: create `.codex/plans/<topic>_<date>.md`.
6. `execute`: implement approved tasks.
7. `review`: audit the diff and produce tracked findings.
8. `execute`: remediate findings if needed.
9. Automatic task handoff: update the active plan's `Handoff Notes`.
10. `check-in`: validate, stage, commit, and optionally push.
11. `pr-issue`: draft issue or PR text.

For larger work, use an automation mode:

- `ship`: approved plan to PR-ready result.
- `auto-ship`: plan through PR-ready result with Codex choosing best reversible recommendations.
- `super-ship`: full high-gate path through merge, checkout main, and pull.

## Preflight Questions

Before work starts, the skill should confirm only the things that materially change the outcome. It should not ask you to choose from every possible option every time.

The usual preflight shape is:

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

If the ambiguity is low-risk and reversible, Codex should record the assumption in the plan and continue. If the ambiguity affects implementation, validation, git behavior, data, public API, or user-visible behavior, Codex should ask before acting.

## Modes

| Mode | Use when | File edits |
|---|---|---|
| `help` | You want guidance choosing a mode. | No |
| `init` | You need repo orientation. | No |
| `context` | You want an AI-ready repo context pack. | Context files only |
| `repo-overview` | You want a human-readable walkthrough. | Report file |
| `research` | You want an evidence-backed answer or read-only audit. | No by default |
| `plan` | You want analysis and an implementation plan. | Plan file only |
| `execute` | You approved the plan and want code changes. | Yes |
| `review` | You want an independent audit. | No by default |
| `explain` | You want a plain-language explanation. | No |
| `handoff` | You want another chat to continue smoothly. | Plan/handoff files |
| `check-in` | You want git staging/commit/push help. | Git/index only as requested |
| `pr-issue` | You want issue or PR text. | Usually no |
| `ship` | You approved a plan and want implementation through PR-ready handoff. | Yes |
| `auto-ship` | You want Codex to plan and ship with recorded recommendations. | Yes |
| `merge` | You want a PR merged after checks. | GitHub remote |
| `sync` | You want local main updated after merge. | Git checkout/pull |
| `super-ship` | You want end-to-end automation through merge and main sync. | Yes, high impact |
| `free` | You want to bypass this workflow. | Depends on request |

## Automation Modes

Automation modes must show options and get required authorization before starting.

| Mode | Best for | Stops before |
|---|---|---|
| `ship` | Approved plan -> implementation -> validation -> review -> check-in -> PR-ready. | Merge unless explicitly requested. |
| `auto-ship` | Goal -> plan -> implementation -> PR-ready with Codex choosing reversible recommendations. | Irreversible/public/user-visible choices unless approved. |
| `merge` | Merging an existing PR with GitHub CLI. | Failing checks or unclear merge target. |
| `sync` | Checkout main/master and pull after merge. | Local changes that could be lost. |
| `super-ship` | Full end-to-end flow through merge, checkout main, and pull. | Any missing authorization or failed gate. |

`super-ship` should present these options before starting:

1. **Safe super-ship**: complete through PR creation, then ask before merge/main sync.
2. **Full super-ship**: complete through merge, checkout main, and pull if all gates pass.
3. **Local-only ship**: execute, validate, review, and commit locally without remote actions.

Before remote actions, Codex should verify GitHub CLI with `gh --version` and `gh auth status`. If GitHub CLI is unavailable, it should fall back to manual PR text.

In `plan` mode, Codex should preserve the strongest part of the old flow: root-cause analysis, proactive code audit, decision points, performance/tradeoff reasoning, and an implementation-ready task list.

## Help Mode

Use help when you are unsure what to run:

```text
Use $codex-dev-flow help. I want to <goal>.
```

Codex should recommend the best mode and, when useful, give 2-3 options with tradeoffs.

## Context Mode

Use context mode when the repo needs an AI-readable map:

```text
Use $codex-dev-flow context.
```

This creates or refreshes `.codex/context/` by default. It is useful before large planning work, before check-in when context may be stale, or when starting a future session that should understand the repo quickly.

## Repo Overview Mode

Use repo-overview when you want a detailed explanation document for a person:

```text
Use $codex-dev-flow repo-overview. Read the docs and code, then write a detailed beginner-friendly summary to ReadingSteiner.md. Do not fabricate anything.
```

This mode should read docs first, verify features against code where needed, separate supported capabilities from inferred or not-built-in workflows, and write a polished document. It is the right mode for "what can this repo do?" questions.

## Research Mode

Use research mode when you have a repo question but do not necessarily want a plan or code changes:

```text
Use $codex-dev-flow research. Does this repo support multi-instrument backtesting? Cite the evidence.
```

```text
Use $codex-dev-flow research. Look up the current FastAPI docs and compare them with how this repo handles dependency injection.
```

Research mode is read-only by default. It should use repo evidence first, use external sources only when useful or required, and clearly separate verified facts from inferences.

## Execution Scope

Use `one-task-at-a-time` for risky or evolving work:

```text
Use $codex-dev-flow execute one-task-at-a-time.
```

Use `all-tasks-together` when the plan is stable:

```text
Use $codex-dev-flow execute all-tasks-together.
```

## Python Work

For Python code changes, the flow expects:

- a pytest unit test first,
- isolated/mocked test dependencies,
- minimal passing code,
- focused pytest validation,
- a docs-impact check.

Any exception should be recorded in the active plan before relying on it.

## Optional Subagents

Subagents are still supported, but they are optional. Use them when a task benefits from context isolation or parallelism:

```text
Use $codex-dev-flow plan and propose whether explorer/reviewer/verifier subagents would help.
```

Good uses are read-only exploration, independent review, test failure analysis, docs-only work, or disjoint implementation slices. Avoid multiple agents editing the same files.

## Continuation

Task-level handoff is automatic. After execution, review, validation failure, one-task-at-a-time pause, or check-in, Codex should update the active plan's `Handoff Notes` with the current state and next action.

Before ending a long chat session, run:

```text
Use $codex-dev-flow handoff.
```

The full handoff should record the active request, plan, decisions, assumptions, completed tasks, open findings, validation results, changed files, and next action. A new Codex chat should read the handoff and active plan before continuing.

If the context is getting long or work is paused, Codex should suggest running `handoff`, but should not create a full session handoff automatically unless the user agrees.

## Free Mode

`free` mode disables this skill's plan/state workflow only. It does not override Codex, system, developer, user, security, sandbox, or repository `AGENTS.md` instructions.

```text
Use $codex-dev-flow free to brainstorm alternatives without creating a plan.
```

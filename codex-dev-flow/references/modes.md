# Mode Procedures

Run a short preflight before each mode. Present material options and clarify material uncertainties. Do not ask ceremonial questions when the repo, active plan, and user request already make the next step clear.

For automation modes (`ship`, `auto-ship`, `merge`, `sync`, `super-ship`), read [automation-modes.md](automation-modes.md) before acting.

## `help`

Read-only mode-selection guidance.

1. Inspect the user's request and current repo/work state only as much as needed.
2. List the available modes with one-line purposes.
3. Recommend the best next mode and explain why.
4. If multiple modes are plausible, present 2-3 choices with tradeoffs.
5. Do not create or edit task files unless the user asks to start a mode.

Preflight focus: none unless the user's goal is too vague to recommend a mode.

## `init`

Read-only orientation.

1. Read root and relevant nested `AGENTS.md`.
2. Read existing `.codex/context/`, `.github/.context/`, or other repo context packs if present.
3. Inspect repo metadata: README, package manifests, Makefile/task files, CI, and git status.
4. Summarize purpose, stack, key commands, important source areas, active branch, and context freshness.
5. Do not create a plan unless the user also provided a development goal.

Preflight focus: confirm repo/path only if unclear.

## `context`

Create or refresh an AI-ready repository context pack.

1. Follow [context-mode.md](context-mode.md).
2. Keep the context pack separate from the active plan.
3. Update the active plan only with a concise note that context was generated or refreshed.

Preflight focus: target path, focus area, output location, and whether this is full, update, or staged context.

## `repo-overview`

Create a human-readable walkthrough of the repository.

1. Follow [repo-overview-mode.md](repo-overview-mode.md).
2. Read docs first, then code enough to verify features and boundaries.
3. Write the requested summary artifact, or default to `.codex/reports/repo-overview.md`.
4. Do not invent capabilities. Mark uncertain or inferred items clearly.

Preflight focus: target audience, desired language, output file path, depth, and whether to include beginner explanations.

## `research`

Read-only investigation for repo questions, feasibility, risks, external docs, or future planning inputs.

1. Follow [research-mode.md](research-mode.md).
2. Use repo evidence first.
3. Use web or external docs only when the question depends on current external facts, APIs, packages, standards, or best practices.
4. Answer directly in chat unless the user asks for a research note.
5. If findings imply future implementation, record proposals or plan candidates only when there is an active plan; do not start coding.

Preflight focus: exact question, scope, whether web/external research is allowed or required, and desired output format.

## `plan`

Read-only planning.

1. Capture the user request as `REQ-*` in a new or active plan.
2. Read repo instructions and relevant code/docs/tests.
3. Identify root cause, requirements, assumptions, decision points, nearby code risks, and validation strategy.
4. Perform a proactive code audit in the relevant area: duplication, overly complex design, inconsistent naming, missing tests, brittle boundaries, and performance-sensitive paths.
5. Compare viable approaches and record tradeoffs for performance, maintainability, readability, extensibility, testability, and documentation.
6. Create or update `.codex/plans/<topic>_<YYYYMMDD>.md` from `assets/plan-template.md`.
7. Add tasks with stable IDs and clear acceptance criteria.
8. Add docs impact only when behavior, API, CLI, config, or user workflow changes.
9. Ask for user decisions only when the clarification gate requires it.

Preflight focus: business goal, acceptance criteria, constraints, user-visible behavior, and decision points.

## `execute`

Implementation against an approved plan.

1. Read the active plan and identify the next eligible task.
2. Confirm execution scope: `one-task-at-a-time` or `all-tasks-together`.
3. Read exact files and nearby tests before editing.
4. Implement the smallest defensible change.
5. Add or update tests according to repo policy.
6. For Python code changes, follow TDD: write or update the failing pytest unit test first, implement the minimal passing code, then refactor.
7. For Python code changes, verify pytest isolation and record docs impact or the reason docs are not affected.
8. Run relevant validation, then full required validation before final handoff.
9. Update task status, changed files, validation entries, findings, and proposals.

For `one-task-at-a-time`, stop after one task, update `Handoff Notes`, and report status. For `all-tasks-together`, continue until the approved plan is complete or blocked.

Preflight focus: active plan, execution scope, unresolved decisions, and whether file edits are intended.

## `review`

Independent audit. Default is read-only.

1. Read the active plan, changed files, and relevant tests/docs.
2. Compare implementation to requirements and acceptance criteria.
3. Check correctness, missing tests, docs impact, security/safety, maintainability, and workflow hygiene.
4. Write findings as `FIND-*` entries with severity, evidence, and required remediation.
5. Update `Handoff Notes` with the next remediation or completion action.
6. Do not edit code unless the user explicitly asks for remediation.

Preflight focus: review target, diff base, and strictness level when unclear.

## `explain`

Human-readable explanation.

1. Read the active plan or requested files.
2. Explain what is changing, why, how it works, and how it was or will be validated.
3. Keep beginner explanations concrete and avoid unnecessary implementation detail.
4. Do not modify files.

Preflight focus: audience and depth only if unclear.

## `handoff`

User-triggered continuation summary for another Codex session or long pause.

1. Read the current conversation context available to you, active plan, git status, changed files, and validation entries.
2. Update or create a handoff section in the active plan.
3. Optionally create `.codex/plans/<topic>_handoff.md` from `assets/handoff-template.md` for long tasks.
4. Include current goal, original request IDs, decisions, assumptions, completed tasks, open tasks, open findings, changed files, commands run, and next recommended action.
5. Make the handoff sufficient for a new chat to continue without reinvestigating settled decisions or re-asking answered questions.

Do not run full session handoff automatically after every task. Automatic task handoff means updating the active plan's `Handoff Notes`; full `handoff` mode is for explicit user requests or when the agent suggests it because context is getting long.

Preflight focus: whether to update only the active plan or create a separate handoff file.

## `check-in`

Git handoff.

1. Inspect working tree and active plan.
2. Identify intended vs unrelated changes.
3. Ensure required validation has run or record why it did not.
4. Check durable context candidates and update AGENTS/docs only when appropriate.
5. Update `Handoff Notes` before staging or committing.
6. Stage only intended files.
7. Commit with a clear message if the user asked to commit.
8. Push only when explicitly requested and permitted.

Preflight focus: intended files, commit vs push, validation expectations, and unrelated changes.

## `pr-issue`

Draft issue and pull request text.

1. Read active plan, validation, review findings, changed files, and handoff notes.
2. Use `assets/issue-template.md` and `assets/pr-template.md`.
3. Do not fabricate issue numbers, validation, reviewers, or deployment status.
4. Clearly label anything that is pending or not run.

Preflight focus: target audience, known issue number, and whether output is manual text or remote creation.

## `ship`

Semi-automatic approved-plan flow. Follow [automation-modes.md](automation-modes.md).

Preflight focus: approved plan, execution scope, validation commands, check-in behavior, PR creation method, and stopping conditions.

## `auto-ship`

Autonomous plan-to-PR-ready flow. Follow [automation-modes.md](automation-modes.md).

Preflight focus: autonomy boundaries, recommendation policy, validation requirements, and which external git/GitHub actions are allowed.

## `merge`

Explicit PR merge workflow. Follow [automation-modes.md](automation-modes.md).

Preflight focus: PR target, merge method, required checks, post-merge branch behavior, and whether main sync should follow.

## `sync`

Checkout main and pull latest after merge. Follow [automation-modes.md](automation-modes.md).

Preflight focus: intended main branch name, whether local changes exist, and whether branch cleanup is desired.

## `super-ship`

High-gate end-to-end automation: plan, execute, validate, review, remediate, handoff, check-in, PR, merge, checkout main, and pull. Follow [automation-modes.md](automation-modes.md).

Preflight focus: explicit authorization for push, PR creation, merge, checkout main, pull, validation gates, and failure stopping rules.

## `free`

Disable only this skill's workflow state requirements. Continue to obey higher-priority instructions, repo instructions, safety rules, and direct user constraints.

Preflight focus: state that this skill's workflow is bypassed; ask only if the task itself is unclear or risky.

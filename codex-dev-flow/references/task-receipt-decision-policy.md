# Task Receipt Decision Policy

Use this policy when work spans more than a quick answer, uses subagents, runs through review, or needs reliable continuation across sessions.

## Purpose

The active plan should answer three questions without relying on chat memory:

1. What task is being done, by whom, and within what boundary?
2. What actually happened, and what evidence proves it?
3. Why did review pass, fail, defer, or request rework?

Keep this lightweight. Do not create extra files unless the task is large enough to need them.

## Tasks

Each `T-*` task should include:

- owner: main agent, named subagent, user, or external owner,
- module or area,
- boundary: what may change and what must not change,
- purpose,
- files or expected files,
- acceptance criteria,
- dependencies.

For cross-module work, assign one primary owner and split subtasks only when ownership or validation differs.

## Receipts

Receipts use `REC-*` IDs and record facts, not intentions.

Create a receipt when:

- a task is accepted or delegated,
- meaningful progress is made,
- a blocker is found,
- work is ready for review,
- a task completes,
- a subagent returns output.

Each receipt should state:

- related task,
- phase: accepted, progress, blocked, ready-for-review, completed, or returned,
- owner,
- what happened,
- files changed or inspected,
- validation or evidence,
- remaining risks,
- next recommended action.

If a receipt claims validation, it must reference a `VAL-*` entry or state why validation was not run.

## Review Decisions

Review decisions use `RDEC-*` IDs. They are separate from `FIND-*` entries:

- `FIND-*` records a specific issue or risk.
- `RDEC-*` records the review verdict and why that verdict is justified.

Valid verdicts:

- `pass`: acceptance criteria are met and no blocking findings remain.
- `fail`: work does not meet acceptance criteria.
- `defer`: known issue is accepted for later work.
- `needs-rework`: remediation is required before completion.

Each review decision should reference the receipts, validation entries, findings, and changed files it relies on. Do not approve work only from a final status statement.

## Subagents

Every subagent must return a receipt-shaped summary. The main agent remains responsible for integrating the result, resolving conflicts, and writing the final `REC-*` or `RDEC-*` entry in the active plan.

## Compatibility

Older plans may not have receipt or review-decision sections. When continuing old work, do not block only because the old plan lacks these sections. Add them when the plan is next updated.

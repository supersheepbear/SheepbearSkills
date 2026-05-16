# Durable Context Policy

Durable context belongs in `AGENTS.md` or repo docs only when it is reusable, short, repo-specific, and likely to prevent repeated mistakes.

## Promote To AGENTS.md

Good candidates:

- build, test, lint, typecheck, docs, and release commands,
- package manager and version constraints,
- repo architecture map and ownership boundaries,
- generated-file warnings,
- security and secret-handling rules,
- common pitfalls that affect future tasks,
- path-specific conventions that apply repeatedly.

## Keep In The Active Plan

Do not promote:

- one-off task plans,
- temporary debugging notes,
- raw command logs,
- unapproved proposals,
- speculative design ideas,
- details that apply only to the current branch.

## Update Protocol

1. Record candidates in the active plan first.
2. Promote only if repeated relevance is clear or the user asks.
3. Keep additions concise and command-focused.
4. Check nested `AGENTS.md` scope before editing.
5. Avoid conflicting root and nested guidance.

## Check-In Behavior

During `check-in`, inspect durable context candidates. If no update is warranted, record that no durable context update was needed. If tooling such as a repo context generator exists, use it when it is part of the repo workflow or the user asks for it.

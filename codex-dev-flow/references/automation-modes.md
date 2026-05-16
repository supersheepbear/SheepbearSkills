# Automation Modes

Automation modes run multiple workflow phases in sequence. They are useful, but they must be gated because they can affect git history, remotes, pull requests, and the main branch.

## Shared Preflight

Before starting any automation mode, present the user with:

- selected mode,
- intended steps,
- expected git/GitHub actions,
- validation commands or discovery plan,
- stop conditions,
- assumptions,
- options that materially change the outcome.

Use a concise shape:

```text
Automation preflight:
- Mode: <ship | auto-ship | merge | sync | super-ship>
- Planned path: <steps>
- Git/GitHub actions: <commit/push/PR/merge/checkout/pull>
- Stop if: <conditions>
- Options:
  1. <recommended option>
  2. <alternative>
```

Proceed only when required confirmations are satisfied. If the user already gave explicit authorization in the prompt, record that authorization in the active plan.

## GitHub CLI Gate

Before creating, merging, or inspecting remote PRs with GitHub CLI, verify:

```text
gh --version
gh auth status
git remote -v
git branch --show-current
git status --short
```

If `gh` is unavailable or unauthenticated, fall back to manual PR/issue text and stop before remote actions. Never fabricate remote URLs, PR numbers, or merge status.

## Stop Conditions

All automation modes must stop when:

- validation fails and no approved remediation remains,
- review has open high or medium findings,
- unrelated working-tree changes would be staged or overwritten,
- required GitHub CLI checks fail,
- branch/remote state is unclear,
- merge target is unclear,
- user authorization for push, PR creation, merge, checkout, or pull is missing,
- action would rewrite history, deploy, release, or touch production without explicit authorization.

## `ship`

Semi-automatic flow for an approved plan.

Path:

```text
approved plan
-> write accepted/progress receipts for active tasks
-> execute approved tasks
-> validate
-> review
-> write review decision
-> remediate approved findings
-> update task handoff notes
-> check-in
-> draft or create PR if authorized and gh works
-> stop before merge unless user explicitly asked for merge
```

Required confirmation before start:

- active plan is approved,
- execution scope,
- whether commit is allowed,
- whether push is allowed,
- whether PR creation is allowed.

## `auto-ship`

Autonomous flow from goal to PR-ready result.

Path:

```text
preflight
-> plan with best recommendations
-> record decisions and assumptions
-> write accepted/progress receipts for active tasks
-> execute
-> validate
-> review
-> write review decision
-> remediate
-> update task handoff notes
-> check-in if authorized
-> draft or create PR if authorized and gh works
-> stop before merge unless user explicitly asked for merge
```

Decision policy:

- Codex may choose best recommendations for reversible engineering choices.
- Record chosen options as `DEC-*` entries.
- Ask before public API, data migration, user-visible behavior, production, release, destructive, or irreversible choices.

## `merge`

Explicit PR merge workflow.

Path:

```text
identify PR
-> check gh availability and auth
-> inspect PR status/checks
-> confirm merge method
-> merge if authorized and checks are acceptable
-> write merge receipt and review/merge decision
-> update active plan/handoff notes
```

Supported merge methods:

- merge commit,
- squash,
- rebase.

Ask if the method is unclear. Do not merge with failing checks unless the user explicitly confirms and the repo policy permits it.

## `sync`

Post-merge local branch sync.

Path:

```text
confirm local working tree is clean or safe
-> checkout main/master target
-> pull latest
-> write sync receipt
-> optionally delete local feature branch if authorized
-> update active plan/handoff notes
```

Ask before discarding, stashing, or moving local changes.

## `super-ship`

End-to-end high-gate automation. This mode includes merge to main, checkout main, and pull.

Path:

```text
preflight with explicit authorization
-> plan or load active plan
-> write accepted/progress receipts for active tasks
-> execute
-> validate
-> review
-> write review decision
-> remediate until clean or blocked
-> update task handoff notes
-> check-in
-> create or update PR
-> verify PR checks/status
-> merge PR
-> write merge receipt
-> checkout main
-> pull latest
-> update final handoff notes
```

Required explicit authorization:

- commit,
- push,
- PR creation/update,
- merge,
- checkout main,
- pull latest.

Recommended preflight options:

1. **Safe super-ship**: complete through PR creation, then ask before merge/main sync.
2. **Full super-ship**: complete through merge, checkout main, and pull if all gates pass.
3. **Local-only ship**: execute, validate, review, and commit locally without remote actions.

Default recommendation is Safe super-ship unless the user explicitly asked for full end-to-end automation.

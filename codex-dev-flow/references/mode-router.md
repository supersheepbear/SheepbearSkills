# Mode Router

Use the user's explicit mode when present. If no mode is named, choose the least surprising mode from the request.

## Routing Table

| User intent | Mode |
|---|---|
| "help", "what mode", "which mode should I use" | `help` |
| "load context", "orient", "what is this repo" | `init` |
| "generate repo context", "update context pack", "make AI repo summary" | `context` |
| "walk me through the repo", "what can this repo do", "write a detailed repo summary" | `repo-overview` |
| "plan", "design", "audit before implementation", "what should we do" | `plan` |
| "implement", "fix", "build", "continue approved plan" | `execute` |
| "review", "audit the diff", "find issues", "check this work" | `review` |
| "explain", "teach me", "summarize simply" | `explain` |
| "summarize this session", "make continuation notes", "handoff to next chat" | `handoff` |
| "commit", "stage", "push", "check in" | `check-in` |
| "PR", "issue", "release notes" | `pr-issue` |
| "ship this", "finish the approved plan", "implement and prepare PR" | `ship` |
| "do everything", "plan and ship", "fully automate to PR" | `auto-ship` |
| "merge the PR", "merge to main" | `merge` |
| "checkout main and pull", "sync main" | `sync` |
| "do the whole flow including merge and pull main" | `super-ship` |
| "ignore the workflow", "quick answer", "free mode" | `free` |

## Clarification Gate

Ask before acting when:

- acceptance criteria materially change what should be built,
- choices affect public APIs, data migration, storage, deployment, or user-visible behavior,
- the action could expose secrets, destroy data, rewrite git history, deploy, release, or affect production,
- required credentials or services are missing,
- the user asks for mutually incompatible outcomes.

Proceed with documented assumptions when:

- the work is read-only,
- ambiguity affects only internal implementation,
- a minimal reversible change is available,
- the repo has clear precedent.

## Mode Switching

Mode switching is allowed when the user's latest request implies it. Record the switch in the active plan:

```markdown
- 2026-05-16: Mode changed from `plan` to `execute` after user approval.
```

Do not silently switch from read-only modes to file-editing modes unless the user clearly asked for implementation.

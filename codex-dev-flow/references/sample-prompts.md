# Sample Prompts And Expected Routing

Use these as regression examples when forward-testing the skill.

| Prompt | Expected mode | Expected behavior |
|---|---|---|
| "Use codex-dev-flow help. I am not sure what mode to use." | `help` | Recommend a mode and show 2-3 options when useful. |
| "Use codex-dev-flow init. What is this repo?" | `init` | Read-only orientation, no plan unless a goal is provided. |
| "Generate an AI-readable context pack for this repo." | `context` | Create or refresh `.codex/context/` and record coverage gaps. |
| "Read the docs and write a detailed beginner-friendly repo summary to ReadingSteiner.md. Do not fabricate." | `repo-overview` | Produce a human-readable repo walkthrough with evidence and uncertainty markers. |
| "Does this repo support multi-instrument backtesting? Cite evidence." | `research` | Inspect repo evidence and answer without editing files. |
| "Research the latest FastAPI docs and compare them with this repo's dependency injection." | `research` | Use repo evidence plus official external docs when needed. |
| "Plan a refactor for the data loader." | `plan` | Create `.codex/plans/...`, capture requirements and tasks, no edits. |
| "Execute the approved plan one task at a time." | `execute` | Read active plan, implement next task, validate, update status, stop. |
| "Review the current diff against the plan." | `review` | Read-only audit, produce `FIND-*` entries, no code edits. |
| "Summarize this session so I can continue in a new Codex chat." | `handoff` | Create user-triggered session handoff notes with next action. |
| "Commit the completed work." | `check-in` | Inspect diff, verify validation/context status, stage intended files, commit only if requested. |
| "Draft the PR body." | `pr-issue` | Use stored plan and validation; do not invent issue numbers. |
| "Ship the approved plan and prepare a PR." | `ship` | Present automation options, execute approved work, validate, review, check in, and stop before merge unless authorized. |
| "Plan and ship this using your best recommendation." | `auto-ship` | Plan, record decisions, execute, validate, review, and prepare PR-ready output with safety gates. |
| "Merge this PR after checks pass." | `merge` | Verify gh auth/status, inspect checks, confirm method, merge only if authorized. |
| "Checkout main and pull latest." | `sync` | Confirm working tree safety, checkout main/master, pull, and update handoff notes. |
| "Super-ship this all the way through merge and pull main." | `super-ship` | Present Safe/Full/Local-only options and require explicit authorization for remote/main actions. |
| "Free mode, just brainstorm." | `free` | Ignore this skill's workflow only; still obey higher-priority rules. |

Forward tests should check that mode routing is correct, state files are concise, and validation claims are evidence-backed.

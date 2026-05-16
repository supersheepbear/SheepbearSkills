# my_skills

Personal Codex skill library.

This repo stores reusable skills that can be copied or synced into a Codex skills folder when needed. Each skill lives in its own folder and has a `SKILL.md` file plus optional `references/`, `assets/`, `scripts/`, and `agents/openai.yaml`.

## Skills

| Skill | What It Does | Use When | Typical Output |
|---|---|---|---|
| [`codex-dev-flow`](./codex-dev-flow/SKILL.md) | Governs disciplined repository development workflows with modes for help, init, context, repo overview, planning, execution, review, handoff, check-in, PR/issue drafting, and automation. | You want Codex to plan, implement, validate, review, summarize, commit, create/merge PRs, or keep a task ledger. | `.codex/plans/` task plans, `.codex/context/` repo context, review findings, handoff notes, PR/issue text, git workflow guidance. |
| [`explain-content-deeply`](./explain-content-deeply/SKILL.md) | Turns source material or a topic into a complete beginner-friendly textbook-style lesson and writes it to files. | You want content explained deeply, rewritten as a lesson, split into chapters, translated, or saved as teaching material. | A lesson-specific folder, `_lesson-manifest.md`, optional writing guide/table of contents, and one or more Markdown lesson files. |

## Quick Usage

| Goal | Suggested Skill | Example Prompt |
|---|---|---|
| Choose the right development workflow mode. | `codex-dev-flow` | `Use $codex-dev-flow help. I want to fix a bug and open a PR.` |
| Load repo orientation before work. | `codex-dev-flow` | `Use $codex-dev-flow init to orient yourself in this repo.` |
| Create AI-readable repo context. | `codex-dev-flow` | `Use $codex-dev-flow context to create a repo context pack.` |
| Write a human-readable repo walkthrough. | `codex-dev-flow` | `Use $codex-dev-flow repo-overview and write a detailed beginner-friendly summary to RepoOverview.md.` |
| Plan and implement a code change carefully. | `codex-dev-flow` | `Use $codex-dev-flow plan for this change, then execute one-task-at-a-time after I approve.` |
| Run the full automation path. | `codex-dev-flow` | `Use $codex-dev-flow super-ship, present the options, and wait for my authorization before remote actions.` |
| Create a detailed lesson from notes or a topic. | `explain-content-deeply` | `Use $explain-content-deeply to explain this material in Chinese, split into chapters, and save it under D:\teaching.` |

## Skill Notes

### `codex-dev-flow`

Main modes:

| Mode | Purpose |
|---|---|
| `help` | Suggests which mode to use. |
| `init` | Reads repo instructions/context and gives a read-only orientation. |
| `context` | Creates or refreshes an AI-readable repo context pack. |
| `repo-overview` | Writes a human-readable walkthrough of what the repo does. |
| `plan` | Creates a structured implementation plan. |
| `execute` | Implements approved plan tasks. |
| `review` | Audits the diff and records findings. |
| `handoff` | Writes continuation notes for another Codex session. |
| `check-in` | Handles validation, staging, commit, and optional push. |
| `pr-issue` | Drafts issue and PR text. |
| `ship` | Runs an approved-plan flow through PR-ready handoff. |
| `auto-ship` | Plans and ships with recorded best-recommendation decisions. |
| `merge` | Merges a PR after explicit gates. |
| `sync` | Checks out main/master and pulls latest after merge. |
| `super-ship` | High-gate end-to-end flow through merge and main sync. |
| `free` | Bypasses this skill's workflow only. |

See [`codex-dev-flow/references/usage-guide.md`](./codex-dev-flow/references/usage-guide.md) for the fuller user guide.

### `explain-content-deeply`

Before writing, the skill asks for:

| Choice | Options |
|---|---|
| Output folder | A parent folder; defaults to `D:\teaching` when omitted. |
| Answer format | One file, multiple chapter files, or let Codex choose. |
| Answer language | English, Chinese with English key terms, or another requested language. |
| Complexity | Simple, default, or complex mode. |

It always writes the teaching output to a lesson-specific folder and maintains `_lesson-manifest.md` for progress and recovery.

## Adding More Skills

When adding a new skill:

1. Create a new folder with a valid `SKILL.md`.
2. Keep `SKILL.md` concise and move detailed guidance into `references/`.
3. Add reusable templates to `assets/` and deterministic helpers to `scripts/` when useful.
4. Add or update `agents/openai.yaml` for display metadata.
5. Add a row to the tables in this README.

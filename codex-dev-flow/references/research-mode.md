# Research Mode

Use `research` mode for read-only investigation. It answers repo-related questions, audits code areas without editing, checks feasibility, compares implementation against external docs, or gathers evidence for later planning.

This differs from nearby modes:

- `init`: quick repo orientation.
- `context`: writes AI-readable repo context files.
- `repo-overview`: writes a full human-readable repo walkthrough.
- `plan`: turns a goal into implementation tasks.
- `review`: audits an existing diff or completed work.
- `research`: investigates a question and answers it without modifying code.

## Preflight

Clarify only material items:

- exact question,
- repo scope or files to inspect,
- whether web/external research is allowed or required,
- whether sources must be official/primary,
- desired output: chat answer, research note, risk list, recommendation, or future plan candidates.

## Evidence Rules

- Use repo evidence first.
- Cite local paths for repo claims.
- Use external sources only when needed for current APIs, package behavior, standards, laws, prices, security guidance, or best practices.
- For technical external research, prefer official documentation, standards, changelogs, source repos, or primary papers.
- Clearly separate `[VERIFIED]`, `[INFERRED]`, and `[NOT VERIFIED]` claims.
- Do not modify files unless the user explicitly switches modes.

## Research Types

| Type | Use For |
|---|---|
| question | Answering a specific repo question. |
| repo-audit | Finding risks in an area without changing code. |
| external-docs | Checking current package/API/framework behavior. |
| feasibility | Determining whether a requested feature is realistic. |
| risk-scan | Looking for likely security, correctness, test, or maintenance risks. |

## Optional Output File

Default to chat. If the user wants a file, write:

```text
.codex/research/<topic>_<YYYYMMDD>.md
```

Suggested structure:

```markdown
# Research: <question>

## Answer

## Evidence

## Risks Or Gaps

## Recommendations

## Future Plan Candidates
```

## Completion

Research mode is complete when the answer is evidence-backed, uncertainties are explicit, and any future implementation ideas are recorded as recommendations rather than silently becoming tasks.

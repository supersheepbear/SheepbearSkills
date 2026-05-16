# Repo Overview Mode

Use `repo-overview` mode when the user wants a human-readable explanation of what a repository does, what features it supports, how it is structured, and how a target reader should understand it.

This differs from `context` mode:

- `context` produces compact AI reference files for future coding work.
- `repo-overview` produces a polished human document for understanding.

## Preflight

Clarify only material items:

- output file path, if the user cares,
- target audience: beginner, technical, stakeholder, domain expert,
- desired language,
- depth: concise, detailed, exhaustive,
- focus areas or exclusions,
- whether examples, diagrams, or downstream-use guidance are needed.

If the user says not to fabricate, preserve epistemic status throughout.

## Reading Order

1. User-provided requirements or prompt.
2. Root and nested `AGENTS.md`.
3. README and docs index.
4. Usage guides, research/design docs, architecture docs.
5. Examples, notebooks, CLI help, API docs.
6. Entry points and public interfaces.
7. Core source modules needed to verify docs.
8. Tests and fixtures that reveal supported behavior.
9. Recent context packs or plans only as secondary aids.

For domain repos, read enough domain-specific docs/code to explain capabilities accurately in that domain's language.

## Output Guidance

Default output path:

```text
.codex/reports/repo-overview.md
```

Use the user's requested path when provided, such as `ReadingSteiner.md`.

The document should usually include:

- project identity and purpose,
- who should use it,
- complete feature/capability summary,
- what each major module or workflow does,
- input/output data and important formats,
- setup and usage commands if relevant,
- examples of supported workflows,
- explicit "can do" vs "not built-in / requires user code",
- important limitations and gotchas,
- beginner-friendly glossary or plain-language explanation,
- source evidence pointers,
- uncertainty and not-verified sections.

## Style

- Be professional and evidence-backed.
- Explain domain terms simply when the user is a beginner.
- Do not fabricate features from names alone.
- Separate documented features from inferred capabilities.
- Prefer tables for feature inventories.
- Cite repo paths for important claims.

## Validation

Before finishing:

1. Cross-check feature claims against docs or code.
2. Verify the output file exists and is readable.
3. If writing non-English content on Windows, validate UTF-8 readback if mojibake is possible.
4. Record any skipped areas or uncertainty.

## Suggested Document Skeleton

```markdown
# <Repo Name> Overview

## Executive Summary

## What This Repo Is For

## Main Capabilities

| Capability | What it does | Evidence | Notes |
|---|---|---|---|

## How The Repo Is Organized

## Core Workflows

## Data, Inputs, And Outputs

## What It Can And Cannot Do

## Beginner-Friendly Explanation

## Setup And Usage

## Limitations, Gotchas, And Unverified Areas

## Source Map
```

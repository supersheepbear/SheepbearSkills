# Context Mode

Use `context` mode to create or refresh an AI-ready repository context pack. The pack is a map for future development, not a replacement for reading source files before editing.

Default output:

```text
.codex/context/
```

Use `.github/.context/` only when the user or repo explicitly prefers that location.

## Commands By Intent

| Intent | Behavior |
|---|---|
| full context | Read the repo and create/refresh core context files. |
| focused context | Read root metadata plus a requested subdirectory/domain. |
| update context | Refresh changed areas based on hashes or changed files. |
| staged context | Refresh context affected by staged git changes before check-in. |

## Output Files

Core files:

```text
.codex/context/
  _index.md
  overview.md
  architecture.md
  development.md
  conventions.md
  gotchas.md
  _meta.json
```

Optional detail files:

```text
module-map.md
api-surface.md
data-models.md
data-flow.md
dependencies.md
testing.md
domains/<domain>.md
```

## Workflow

1. Identify repo root, focus path, output path, and mode: full, focused, update, or staged.
2. Respect `.gitignore`, `.git/info/exclude`, generated-file conventions, and dependency folders.
3. Prefer `git ls-files`, `rg --files`, and package manifests for inventory.
4. Read in dependency order:
   - repo instructions and README,
   - manifests, build files, CI, dev commands,
   - architecture/docs/design material,
   - entry points and top-level wiring,
   - public API/routes/CLI/exports,
   - data models and validation,
   - core services and state transitions,
   - storage, integrations, queues, schedulers, auth, side effects,
   - test fixtures and representative tests.
5. Write compact core files that can be loaded together.
6. Split detail files by domain when a single file becomes dense or incomplete.
7. Mark direct facts with source paths and guesses as `[INFERRED]`.
8. Record coverage gaps in `_index.md`.
9. Write `_meta.json` with generated timestamp, repo root, scope, output files, counts, and source hashes when feasible.

## Context Budget

- Core files target 80 to 160 lines each.
- Detail files target 80 to 220 lines each.
- Do not omit public contracts, setup commands, ownership boundaries, or high-risk gotchas just to hit a line count.
- Prefer dense tables and source pointers over prose.
- Do not paste large source blocks.

## Staged Context During Check-In

For check-in mode:

1. Run `git diff --name-only --cached`.
2. If no files are staged, record that no staged context update was needed.
3. Map staged files to affected context files.
4. Refresh only affected context entries when possible.
5. If context tooling is unavailable or the context pack does not exist, record the gap and continue unless the user requires it.

## Completion

Context mode is complete when `_index.md` points to generated files, core context is compact, coverage gaps are explicit, and the user knows where the context pack was written.

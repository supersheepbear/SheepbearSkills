# Subagents Policy

Default to the main agent. Use subagents only when context isolation or parallelism clearly helps.

## Good Uses

- Read-heavy codebase exploration.
- Independent review of changed files.
- Test failure and log analysis.
- Documentation-only updates.
- Large implementation work split into disjoint file ownership.

## Avoid

- Small tasks.
- Unclear requirements.
- Multiple agents editing the same files.
- Parallel implementation without explicit ownership.
- Delegating the next immediate blocker when the main agent can handle it faster.

## Delegation Contract

Every subagent prompt should include:

- active request ID and task ID,
- exact scope and file ownership,
- owner label to use in the active plan,
- whether the agent may edit files,
- required output format,
- validation expectation,
- reminder not to revert or overwrite unrelated changes.

Every subagent final response should be receipt-shaped:

- task ID and owner label,
- phase: returned, blocked, ready-for-review, or completed,
- files read or changed,
- actions taken,
- validation or evidence,
- remaining risks,
- recommended next action.

## Integration

The main agent must review subagent outputs, integrate changes, convert the final response into a `REC-*` entry, update review decisions when applicable, and close completed subagent threads when no longer needed.

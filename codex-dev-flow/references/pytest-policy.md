# Pytest Policy

Apply this policy only when pytest tests are in scope.

## Unit Test Bias

- Prefer small, isolated unit tests.
- Mock network, database, filesystem, and external service dependencies.
- Use `tmp_path` only for isolated file-path behavior.
- Avoid integration and end-to-end tests unless the user or repo explicitly requires them.
- For Python code changes, pytest isolation is mandatory unless the active plan records a specific exception and rationale.

## Fixture Rules

- Prefer function-scoped fixtures.
- Avoid session-scoped mutable state.
- Use `yield` fixtures when teardown is needed.
- Ensure tests are safe under parallel execution.

## Test Shape

- Arrange mocked dependencies clearly.
- Assert both returned behavior and important interactions.
- Name tests by expected behavior.
- Keep test data minimal but realistic.

## Validation

- Run focused pytest commands for touched behavior first.
- Run the repo's required test command before handoff when feasible.
- Record exact commands and results in the active plan.
- Failed pytest validation creates a `FIND-*` entry and a remediation task unless the user stops the work.

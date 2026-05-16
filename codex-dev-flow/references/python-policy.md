# Python Policy

Apply this policy only when Python source, Python packaging, or Python tests are in scope.

## Package First

- Prefer a `src/` layout when the repo already uses or requests package-style development.
- Keep code importable. Avoid one-off scripts unless the repo has an established scripts pattern.
- Follow existing package boundaries before adding new abstractions.

## TDD Requirement

- For Python code changes, write or update a failing pytest unit test before application code.
- Implement the smallest code change that makes the test pass.
- Refactor only after the focused test passes.
- If TDD is not appropriate for a specific Python change, record the exception and rationale in the active plan before continuing.

## Tooling

- Use `uv run` for Python execution when the repo uses `uv` or the active plan requires it.
- Use `uv add` for project dependencies when dependency changes are approved.
- Do not use direct `pip install` to mutate project dependencies.

## Code Standards

- Add type hints for new or changed public functions.
- Use NumPy-style docstrings when adding public modules/classes/functions in repos that require API-grade docs.
- Keep functions focused and testable.
- Avoid broad `except Exception` unless the repo pattern justifies it and the behavior is documented.
- Respect existing formatter/linter configuration.

## Performance

- Prefer algorithmically efficient and vectorized approaches when performance matters.
- Profile or reason from measured bottlenecks before complex optimization.
- Record performance assumptions in the active plan when they affect design.

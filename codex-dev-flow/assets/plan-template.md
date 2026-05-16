# [TASK] <goal>

## 0. Control

- **Active Request**: REQ-001
- **Active Plan**: PLAN-001
- **Mode**: help | init | context | repo-overview | research | plan | execute | review | explain | handoff | check-in | pr-issue | ship | auto-ship | merge | sync | super-ship | free
- **Execution Scope**: one-task-at-a-time | all-tasks-together | review-only | read-only
- **Date**: <YYYY-MM-DD>
- **Branch**: <branch>
- **Done When**: <acceptance criteria>
- **Next Action**: <T-* | FIND-* | PROP-* | user decision>

## 1. Request History

### REQ-001

- **Original user request**: <quote or concise exact summary>
- **Interpreted goal**: <agent interpretation>
- **Status**: active | superseded | completed | rejected
- **Links**: PLAN-001

## 2. Repository Context

- **Relevant instructions**: <AGENTS.md paths>
- **Relevant source areas**: <paths>
- **Validation commands discovered**: <commands or "pending">
- **Constraints**: <repo/user/platform constraints>

## 2.1 Preflight

- **Goal understood as**: <goal/scope/expected output>
- **Material ambiguities**: none | <list>
- **Options presented**: <recommended option and alternatives>
- **Questions asked**: none | <list>
- **Assumptions accepted for now**: <ASM-* links>
- **Proceeding because**: clear requirements | low-risk reversible assumption | user confirmed

## 2.2 Automation Authorization

Complete this section for `ship`, `auto-ship`, `merge`, `sync`, or `super-ship`.

| Action | Authorized | Evidence |
|---|---|---|
| Commit | yes/no/not applicable | <user prompt or plan decision> |
| Push | yes/no/not applicable | <user prompt or plan decision> |
| Create/update PR | yes/no/not applicable | <user prompt or plan decision> |
| Merge PR | yes/no/not applicable | <user prompt or plan decision> |
| Checkout main | yes/no/not applicable | <user prompt or plan decision> |
| Pull latest | yes/no/not applicable | <user prompt or plan decision> |

## 3. Plan History

### PLAN-001

- **Status**: proposed | approved | active | superseded | completed
- **Reason**: <why this plan exists or changed>
- **Supersedes**: none

## 4. Requirements And Assumptions

- **Requirement REQ-001.1**: <requirement>
- **Assumption ASM-001**: <assumption> - risk: low | medium | high - needs user: yes | no

## 4.1 Root Cause And Code Audit

- **Root cause / underlying need**: <why this change is needed>
- **Relevant code risks**: <duplication, complexity, naming, boundaries, missing tests>
- **Performance-sensitive areas**: <paths or "none found">
- **Existing patterns to preserve**: <repo patterns>

## 4.2 Policy Exceptions

Record exceptions before relying on them.

| ID | Policy | Exception | Rationale | Approved By |
|---|---|---|---|---|
| EXC-001 | Python TDD | none | N/A | N/A |

## 5. Decisions

| ID | Decision | Rationale | Status |
|---|---|---|---|
| DEC-001 | <decision> | <why> | proposed | accepted | rejected |

## 6. Proposals

| ID | Proposal | Status | Promotion |
|---|---|---|---|
| PROP-001 | <idea> | proposed | T-001 if accepted |

## 6.1 Approach Tradeoffs

| Option | Pros | Cons | Recommendation |
|---|---|---|---|
| <option> | <benefits> | <costs/risks> | <yes/no and why> |

## 7. Tasks

- [ ] T-001: <task>
  - **Owner**: main-agent | subagent:<name> | user | external
  - **Module/Area**: <primary repo area>
  - **Boundary**: <what this task may change, and what it must not change>
  - **Purpose**: <why>
  - **Files**: <paths>
  - **Acceptance**: <observable completion>
  - **Depends**: none

## 8. Receipt Log

Receipts record what actually happened. Add one when work is accepted, progress is made, a blocker appears, work is ready for review, or work completes.

| ID | Task | Phase | Owner | Summary | Evidence | Risks | Next |
|---|---|---|---|---|---|---|---|
| REC-001 | T-001 | accepted | <owner> | <what started or changed> | <files, commands, artifacts, or notes> | <known risks or none> | <next action> |

## 8.1 Execution Log

- **NOW**: <current work>
- **DONE**: <completed work>
- **BLOCKED**: <blockers>

## 9. Validation Log

| ID | Command | Purpose | Result | Evidence |
|---|---|---|---|---|
| VAL-001 | `<command>` | <why> | pass | fail | not-run | blocked | <summary> |

## 9.1 Docs Impact

- **Docs update needed**: yes | no
- **Reason**: <user-facing behavior/API/CLI/config/workflow changed, or no docs impact>
- **Docs validation**: <command and result, or not-run reason>

## 10. Review Findings

| ID | Severity | Finding | Required Fix | Status |
|---|---|---|---|---|
| FIND-001 | high | <issue> | T-002 | open | fixed | deferred |

## 10.1 Review Decisions

Review decisions explain why work passed, failed, was deferred, or needs rework. Base each decision on receipts, findings, validation, and changed files.

| ID | Based On | Verdict | Evidence | Rationale | Next |
|---|---|---|---|---|---|
| RDEC-001 | REC-001, VAL-001, FIND-001 | pass/fail/defer/needs-rework | <evidence summary> | <why this verdict is justified> | <next action> |

## 11. Changed Files

| Path | Reason | Task |
|---|---|---|
| `path/to/file` | <why changed> | T-001 |

## 12. Durable Context Candidates

- <Guidance to consider for AGENTS.md or repo docs, if reusable.>

## 13. Handoff Notes

- **Task handoff updated**: <timestamp or "not yet">
- **Handoff type**: automatic task update | user-triggered session handoff
- **Current state**: <where things stand>
- **Next recommended action**: <specific next step>
- **Latest receipt**: <REC-* or none>
- **Latest review decision**: <RDEC-* or none>
- **Do not re-ask**: <answered questions and settled decisions>

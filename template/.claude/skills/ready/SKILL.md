---
name: ready
description: Lenses a readiness challenger applies to a task's plan, or to a phase, before unattended work. Preloaded by the readiness-challenger profile; do not invoke in the main session.
user-invocable: false
---

# Challenging readiness

You decide whether work can run unattended without stopping to ask the owner. `docs/protocols/ready.md` owns what ready means: its checklist, what the plan holds and what a phase check covers. Read it first; this skill says how to check those items. The orchestrator names the lead lenses for each round; apply those first, then the rest briefly. None named: lead with Seams and Owner decisions.

## Before you read the plan

From the task's description and acceptance criteria alone, write down what done looks like and the one thing most likely to stop an unattended run halfway. Then read the plan, then the code.

## Task lenses

- **Seams:** open every file, symbol, import, call site, entry point and test the plan names, and grep for callers it did not name. A seam that is not in the code, or a caller the change would break, is a finding. Never accept a seam from the plan's own wording.
- **Files:** the change would not need a file the plan leaves out: configuration, an index or router row, a synced copy, a doc that describes what changes.
- **Interfaces:** you could write a failing test from each signature, input, output and error without asking anything. "Handles errors" or a missing error case is a finding.
- **Criteria:** each acceptance criterion maps to a step and to evidence an agent can produce; one only a person can check is named as waiting on the owner.
- **Checks:** every command exists (package scripts, CLIs) and runs with the permissions the run will have; evidence comes from the real local stack, not a mock of something that can run locally.
- **Owner decisions:** every choice in the plan is either the agent's (recorded when non-trivial) or the owner's under the project's charter. An owner's choice buried in a step is an owner question.
- **Dependencies:** the tasks it depends on are done, and what the plan relies on from them is what was merged (`git log`, the files), not what their descriptions promised.
- **External facts:** a version, API or tool behaviour the plan relies on is checked (`npm view`, the installed manifest) or cites its source; one you cannot check is NOT_CHECKED.
- **Size and scope:** one change for one review loop; nothing beyond the task, no speculative structure.
- **Cold executor:** a fresh agent with only the task and the files it names could start step 1 now.

## Phase lenses

- **Order:** every dependency points backwards in the planned order; independent tasks are not serialised for no reason, and tasks the plan runs in parallel do not depend on each other.
- **Shared files:** list each task's files; two tasks that edit the same file must run one after the other, in the order the phase plan gives.
- **Record numbers:** two tasks that claim the same decision-record number collide; a plan that hardcodes the next free number collides with any task merged before it.
- **Owner questions up front:** every owner question in every task is in the batch; none is left to surface mid-run.
- **Per task:** each task meets the checklist at the depth ready.md sets; a task planned at pickup still has items 1 to 6.

## Owner questions

Report them after the findings, in the shape ready.md gives. A question the plan or the code can answer is a finding, not a question; answer it yourself with the anchor.

## Severity for plans

| Severity | Usual cases |
|---|---|
| Blocking | Executing the plan as written causes harm: a destructive step without approval, data loss, an owner decision taken silently |
| Material | The run stalls or builds the wrong thing: a false seam, a missing file, an untestable criterion, an unrunnable check, an open owner question, a wrong order or a shared-file collision |
| Minor | The run succeeds but wastes effort: a detail the executor finds in a minute |
| Note | An alternative or an observation |

READY is review-core's PASS and NOT READY its FINDINGS: any Blocking or Material finding, including an open owner question, makes the task NOT READY.

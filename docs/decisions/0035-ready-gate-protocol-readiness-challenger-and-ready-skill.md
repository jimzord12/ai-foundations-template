---
status: accepted
date: 2026-10-02
decision-makers: agent
kind: technical
supersedes: []
---

# Ready gate protocol, readiness-challenger and ready skill

## Context and Problem Statement

[0019](0019-definition-of-ready-gate-before-unattended-work.md) chose a Definition of Ready gate before unattended work, and [0020](0020-specific-thin-agent-profiles-plus-shared-skills.md) a thin `readiness-challenger` profile preloading a `ready` skill. Left open: where each rule lives, the challenger's tools, how small tasks get "a light version", and how the task and phase levels fit together when a later task's code depends on an earlier one. TASK-26.

## Considered Options

- Checklist and plan contents in the `ready` skill, with `ready.md` pointing to it.
- Checklist and plan contents in `docs/protocols/ready.md`; the skill holds only how to challenge them.

## Decision Outcome

Chosen option: "Checklist and plan contents in `docs/protocols/ready.md`", because the agent writing the plan, and agents without Claude Code subagents, must reach them from the AGENTS.md router; a skill is loaded only into the challenger.

- `ready.md` owns: when the gate applies and the owner's waiver, the depth table, the checklist, what the plan holds (seams, files, interfaces precise enough to write tests first, steps, checks and evidence), the challenge loop (INCOMPLETE and round caps as in `review.md`), batched owner questions with a recommended answer each, the `ready` label (never on a Backlog draft; removed when the task changes) and the phase level.
- The `ready` skill owns: the task and phase lenses, the "before you read the plan" step, the severity mapping for plans, and the verdict mapping (READY = PASS, NOT READY = FINDINGS; an open owner question is Material, so NOT READY). It is hidden (`user-invocable: false`) and never sets `disable-model-invocation`.
- `readiness-challenger`: Read, Grep, Glob, Bash; Opus, high effort, 80 turns (a phase check reads every task); preloads `review-core` and `ready`. Bash, as for `code-reviewer` and `docs-reviewer`, is read-only by instruction: it reads tasks with the Backlog CLI (already on the template's allowlist), sees what was merged with git, and checks versions. No web tools: they are not on the template allowlist, so a plan cites its sources and an unverifiable fact is NOT_CHECKED.
- Depth: a trivial task (as `review.md` defines it) needs only the checklist answered in its notes by the agent itself, which then adds the label, no challenger; non-trivial tasks get challenger rounds until READY.
- Phase level: a task whose plan depends on code an earlier task in the same phase changes is labelled on the checklist's first six items and gets its plan and a task-level challenge at pickup. This is how the challenges of TASK-29 and TASK-30 ran in this repo.
- Unattended runs: at pickup, every dependency must be Done and the task notes must record a task-level READY (or the trivial self-check), so a `ready` label alone never starts work. When the owner is away, a task blocked on an owner question stays unready together with every task that depends on it; the agent does not adopt its own recommended answer. When the only open findings are owner questions, the rounds stop.
- Decision-record numbers: a plan names a new record by title and takes the next free number when it writes it, so tasks in one phase do not collide.
- Fallback: without the profile, `code-reviewer` applies the `ready` skill, as `review.md` does for the lens skills.

### Consequences

- Good, because the gate is the same in this repo and in generated projects (`ready.md`, the profile and the skill are dogfooded).
- Bad, because a plan written early for a dependent task goes stale; the pickup re-check costs one more challenger run per such task.

## More Information

- Refines [0019](0019-definition-of-ready-gate-before-unattended-work.md); follows [0020](0020-specific-thin-agent-profiles-plus-shared-skills.md) and [0032](0032-review-loop-protocol-code-reviewer-and-review-skills.md).
- Extracted from the owner's existing plan reviewer in another workspace, with everything project-specific removed.
- Proof: TASK-26 notes (headless run of the shipped challenger on one real task).

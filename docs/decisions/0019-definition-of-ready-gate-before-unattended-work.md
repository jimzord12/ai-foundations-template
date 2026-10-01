---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: product
supersedes: []
---

# Definition of Ready gate before unattended work

## Context and Problem Statement

Tasks went straight from "created" to "worked on", so gaps surfaced mid-run when the owner was away. The owner wants every task planned and challenged before unattended work, here and in generated projects.

## Considered Options

Backlog.md drafts as the "not ready" state — tested 2026-10-01: `backlog task demote` did nothing on a scratch copy, and promotion may renumber tasks and break references, so a label is used instead. Planning only at pickup — leaves gaps to be found mid-run.

## Decision Outcome

A Definition of Ready gate (the standard counterpart of a Definition of Done): (1) ready checklist (why, testable acceptance criteria, dependencies, one-change size, open decisions answered, verification named); (2) the plan is written into the task with the real seams traced; (3) a fresh-context reviewer with a readiness lens returns READY or NOT READY; (4) owner-only questions are batched with a recommended answer each. Unattended work starts only on READY; the owner may waive it when present; depth scales with task size. Two levels: per task, and per phase (phase plan doc plus a ready check of every task in it). Ready tasks carry the `ready` label. Ships in the template and is used in this repo. Tracked in TASK-26.

### Consequences

Every task costs a planning and challenge step; small tasks get a light version.

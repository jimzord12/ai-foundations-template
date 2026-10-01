---
id: TASK-20
title: >-
  Agent eval harness: predefined tasks, deterministic checks and independent
  judge
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
updated_date: '2026-10-01 16:40'
labels:
  - testing
  - evals
milestone: m-2
dependencies:
  - TASK-18
  - TASK-19
priority: high
type: feature
ordinal: 20000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Check that the instructions are loaded and followed and do more good than harm. Run an agent headlessly in a container on a fixture with a predefined task, capture transcript and diff, then grade with deterministic checks plus an independent judge agent with no session context. Candidate tasks: add an endpoint or page with validation; add a date helper (should reuse date-fns or existing code); add a new library (should log a decision); hit a hard-to-reverse choice such as auth or database (should ask the owner); a third duplication (should extract); a subagent report (must contain a findings block); a destructive git request (should ask). Agent runs are non-deterministic, so each cell runs several times and reports pass rates, not single results. Also measure that the router works: did the agent open the linked protocol file when the situation matched, and a canary rule in a test build proving AGENTS.md was loaded via CLAUDE.md.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 6-10 predefined tasks, each with a written expectation and a deterministic check where possible
- [ ] #2 Harness runs a task on a fixture in Docker and stores transcript, diff, token cost and grades
- [ ] #3 Independent judge agent grades instruction loading and adherence; router hit rate measured
- [ ] #4 Each eval verified to fail on a baseline without the instructions (an eval that passes without the rule tests nothing)
<!-- AC:END -->

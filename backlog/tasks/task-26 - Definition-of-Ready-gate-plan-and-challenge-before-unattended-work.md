---
id: TASK-26
title: 'Definition of Ready gate: plan and challenge before unattended work'
status: To Do
assignee: []
created_date: '2026-10-01 19:50'
updated_date: '2026-10-01 19:51'
labels:
  - process
  - ready
milestone: m-0
dependencies:
  - TASK-11
priority: high
type: feature
ordinal: 500
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner-approved 2026-10-01 (docs/decisions.md). Before unattended work a task must pass: ready checklist, a written plan with real seams traced, an independent fresh-context challenge (READY / NOT READY), and batched owner questions with recommended answers. Two levels: per task and per phase. Ready tasks carry the ready label (Backlog drafts were tested and rejected). Ships in the template and is used in this repo. The readiness lens lives in the reviewer agent from TASK-11, not a new agent.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 docs/protocols/ready.md ships in the template and in this repo, with the checklist, plan contents, challenge step, question batching and phase-level rule; linked from the AGENTS.md router
- [ ] #2 Reviewer agent from TASK-11 has a readiness lens returning READY / NOT READY with findings
- [ ] #3 Rule in AGENTS.md: unattended work starts only on tasks labelled ready; owner may waive when present; depth scales with size
- [ ] #4 Used once end to end on a real task in this repo with the evidence recorded; smoke test and review loop pass
<!-- AC:END -->

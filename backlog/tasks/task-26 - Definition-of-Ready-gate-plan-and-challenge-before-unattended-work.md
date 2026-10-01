---
id: TASK-26
title: 'Definition of Ready gate: plan and challenge before unattended work'
status: To Do
assignee: []
created_date: '2026-10-01 19:50'
updated_date: '2026-10-01 20:14'
labels:
  - process
  - ready
milestone: m-0
dependencies:
  - TASK-11
priority: high
type: feature
ordinal: 700
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner-approved 2026-10-01. Gate before unattended work: ready checklist, plan written into the task with real seams traced, independent challenge (READY / NOT READY), batched owner questions with recommended answers; per task and per phase; ready tasks carry the ready label (drafts tested and rejected). Built as a ready skill plus a readiness-challenger profile (read-only tools, Opus, preloads review-core and ready), per the agents+skills decision.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 ready skill and readiness-challenger profile ship in template/ and in this repo (dogfood manifest); docs/protocols/ready.md linked from the router in both the root and the template AGENTS.md
- [ ] #2 Rule in both AGENTS.md files: unattended work starts only on tasks labelled ready; owner may waive when attended; depth scales with size
- [ ] #3 Proof: the shipped challenger is run on one real task in this repo and its verdict recorded
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

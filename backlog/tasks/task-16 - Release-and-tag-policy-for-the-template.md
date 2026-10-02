---
id: TASK-16
title: Release and tag policy for the template
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-02 16:17'
labels:
  - release
milestone: m-0
dependencies:
  - TASK-2
  - TASK-7
  - TASK-11
  - TASK-13
  - TASK-14
  - TASK-15
  - TASK-17
  - TASK-23
  - TASK-24
  - TASK-25
  - TASK-26
  - TASK-27
  - TASK-28
  - TASK-29
  - TASK-30
  - TASK-31
  - TASK-32
  - TASK-33
priority: medium
type: chore
ordinal: 1900
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Copier update only delivers template changes to projects when a git tag exists, and there is no tag yet. Decide when and how to tag so that projects get stable updates.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Versioning rule documented in a Releases section of the README (patch, minor, major; migrations for renamed questions)
- [ ] #2 README fixed: gh:jimzord12/ai-foundations-template, per-stack scaffold-then-copy steps including the Express skeleton
- [ ] #3 Agent prepares tag v0.1.0 locally and asks; the owner approves the push in session (never pushed unattended)
- [ ] #4 copier update proven from v0.1.0 to a scratch tag v0.1.1-test in a scratch clone, never pushed
- [ ] #5 Phase exit criterion, in the same attended session after the push: a project generated per stack from gh:jimzord12/ai-foundations-template@v0.1.0 passes npm run check and its CI workflow in the scratch repository
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner answer Q1: CI proofs use the private repo jimzord12/ai-foundations-scratch (decision of that date). Push one branch per stack and proof; delete only branches you created; never create or delete repositories or force push.

2026-10-02: record 0040 (stack-agnostic core with packs picked by detection): "per stack" in this task now means per Phase 1 pack (Next.js, bare React Native, Express); more frameworks are TASK-2.6. The README scaffold-then-copy steps describe how the stack is detected (the stack question default) and how to override it, not a closed stack list. The ready label was removed because this changes what the task must do; plan and challenge again before unattended work, or the owner waives it.
<!-- SECTION:NOTES:END -->

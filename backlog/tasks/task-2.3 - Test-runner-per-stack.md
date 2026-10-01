---
id: TASK-2.3
title: Test runner per stack
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
labels:
  - stack
  - tests
milestone: m-0
dependencies: []
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1100
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Each stack needs a test runner agents can call in seconds, matching the owner's rule that tests exercise the real implementation (mocks only at true external boundaries). Evaluate current standards (for example Vitest for Express and Next.js, Jest for React Native, which is the RN default) and verify versions.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Runner chosen and configured per stack, recorded in docs/decisions.md
- [ ] #2 One example test per stack that exercises real code and fails when that code is broken
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

---
id: TASK-2.3
title: Test runner per stack
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-02 03:01'
labels:
  - stack
  - tests
  - ready
milestone: m-0
dependencies:
  - TASK-2.5
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Each stack needs a test runner agents can call in seconds, matching the owner's rule that tests exercise the real implementation (mocks only at true external boundaries). Evaluate current standards (for example Vitest for Express and Next.js, Jest for React Native, which is the RN default) and verify versions.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Runner chosen and configured per stack (verify current standards, for example Vitest for Express and Next.js, Jest for RN), recorded in docs/decisions/
- [ ] #2 Example test per stack exercises named real code: Express GET /health via the app, a Next.js utility function (async Server Components are out of scope for unit tests and stated as such), the RN App component render
- [ ] #3 Each example test is shown red after deliberately breaking the code under test, then green again (evidence recorded)
- [ ] #4 2.3 adds the test script through the post-copy task
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
2026-10-02: record 0036 applies: never overwrite the project's own config; ship a new file that extends or imports it, and verify that per tool before relying on it.
<!-- SECTION:NOTES:END -->

---
id: TASK-2.3
title: Test runner per stack
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-02 21:29'
labels:
  - stack
  - tests
milestone: m-0
dependencies:
  - TASK-2.5
  - TASK-2.7
  - TASK-2.8
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Each supported framework (its pack) needs a test runner agents can call in seconds behind one contract: the test script, matching the owner's rule that tests exercise the real implementation (mocks only at true external boundaries). Evaluate current standards (for example Vitest for Express and Next.js, Jest for React Native, which is the RN default) and verify versions.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Runner chosen and configured for each Phase 1 pack (verify current standards, for example Vitest for Express and Next.js, Jest for RN), written in the pack and recorded in docs/decisions/
- [ ] #2 Example test per Phase 1 pack exercises named real code: Express GET /health via the app (a skeleton file, under the skeleton condition, so an existing Express app does not receive it), a Next.js utility function (async Server Components are out of scope for unit tests and stated as such), the RN App component render
- [ ] #3 Each example test is shown red after deliberately breaking the code under test, then green again (evidence recorded)
- [ ] #4 2.3 adds the test script through the post-copy task for each pack that defines one, unless the project already has a test script (TASK-2.7 criterion 2), and any per-pack config file in the home TASK-2.7 criterion 1 decides (rendered by Copier, not written by a task); the generic pack defines none
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

2026-10-02: ready label removed: its dependency 2.5 changed what the plan relies on (record 0036, ready.md); plan and challenge again, or the owner waives it.

2026-10-02: record 0041: the contract (test) is the same for every framework and each pack says how it is met; frameworks beyond Phase 1 are TASK-2.6.

2026-10-03: TASK-2.5 was split into 2.5 (detection and packs), 2.7 (post-copy tasks) and 2.8 (Express skeleton); dependencies and criterion references updated (old 2.5 criterion 1 is 2.7 criterion 1, old 2.5 criterion 6 is 2.7 criterion 2).
<!-- SECTION:NOTES:END -->

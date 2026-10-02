---
id: TASK-2.1
title: 'Strict TypeScript per stack: tsconfig and ts-reset'
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-02 03:01'
labels:
  - stack
  - typescript
  - ready
milestone: m-0
dependencies:
  - TASK-2.5
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1100
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents write more consistent code under a strict compiler. Ship a strict tsconfig per stack (standard base packages such as @tsconfig/strictest combined with the framework's own base where one exists) and @total-typescript/ts-reset. Verify current versions and framework compatibility first.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The template ships one tsconfig.foundations.json that extends the project's own tsconfig.json with the strict flags and never overwrites it (record 0036); the Express skeleton, which has no scaffolder, ships its own tsconfig.json from a standard strict base for the foundations file to extend
- [ ] #2 ts-reset installed (via the post-copy task) and wired per stack
- [ ] #3 npx tsc -p tsconfig.foundations.json --noEmit passes on a freshly scaffolded Next.js and RN project and on the Express skeleton, and each framework's own build is unaffected; the open checks listed in record 0036 (editor-only plugins through extends) are verified
- [ ] #4 Choices and versions recorded in docs/decisions/
- [ ] #5 2.1 adds the typecheck script (tsc -p tsconfig.foundations.json --noEmit) through the post-copy task
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
2026-10-02: acceptance criteria 1, 3 and 5 amended by record 0036 (config files are extended, not overwritten).
<!-- SECTION:NOTES:END -->

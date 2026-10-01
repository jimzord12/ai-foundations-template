---
id: TASK-2.1
title: 'Strict TypeScript per stack: tsconfig and ts-reset'
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-01 20:14'
labels:
  - stack
  - typescript
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
- [ ] #1 Each stack ships a strict tsconfig that extends the framework base (Next.js, RN) or a standard strict base (Express), overwriting the scaffolded file on purpose as documented
- [ ] #2 ts-reset installed (via the post-copy task) and wired per stack
- [ ] #3 npx tsc --noEmit passes on a freshly scaffolded Next.js and RN project and on the Express skeleton
- [ ] #4 Choices and versions recorded in docs/decisions.md
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

---
id: TASK-2.2
title: Lint and format per stack
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-01 21:26'
labels:
  - stack
  - lint
  - ready
milestone: m-0
dependencies:
  - TASK-2.5
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1200
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
One standard linter and formatter per stack so agents get fast, consistent feedback. Evaluate the current standards (for example ESLint + Prettier vs Biome) against each framework's defaults (Next.js ships its own ESLint config). Prefer the framework default where one exists.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Linter and formatter chosen per stack, extending the framework shipped config where one exists (Next.js ESLint, RN ESLint and Prettier); reason recorded in docs/decisions/
- [ ] #2 lint and format:check scripts exit 0 on a freshly scaffolded project for each stack, and lint exits non-zero on a planted violation
- [ ] #3 2.2 adds the lint and format:check scripts through the post-copy task
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

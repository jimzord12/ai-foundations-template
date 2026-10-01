---
id: TASK-2.2
title: Lint and format per stack
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
labels:
  - stack
  - lint
milestone: m-0
dependencies: []
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
One standard linter and formatter per stack so agents get fast, consistent feedback. Evaluate the current standards (for example ESLint + Prettier vs Biome) against each framework's defaults (Next.js ships its own ESLint config). Prefer the framework default where one exists.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Linter and formatter chosen per stack with the reason recorded in docs/decisions.md
- [ ] #2 Config ships in the template and passes on a freshly scaffolded project for each stack
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

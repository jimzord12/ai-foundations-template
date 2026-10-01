---
id: TASK-13
title: 'CI for the template: smoke-test all three stacks on every push'
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 20:14'
labels:
  - ci
  - quality
milestone: m-0
dependencies:
  - TASK-17
priority: high
type: chore
ordinal: 1700
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The smoke test (copier copy for express, next, rn) is manual today and easy to forget; one broken template breaks every new project. Run it automatically on push and pull request.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 GitHub Actions workflow on push and pull request runs the TASK-17 test suite
- [ ] #2 Workflow runs npm run check on a freshly scaffolded project per stack
- [ ] #3 Identical-check: every file in the dogfood manifest (TASK-24) matches its template/ source, and the job fails on drift
- [ ] #4 Action and uv versions verified; workflow green on main
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of the CI workflow. TASK-23 adds its secret-scanning step to this workflow; TASK-2 subtasks provide the check commands it runs.
<!-- SECTION:NOTES:END -->

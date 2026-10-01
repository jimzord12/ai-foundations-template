---
id: TASK-16
title: Release and tag policy for the template
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 19:51'
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
priority: medium
type: chore
ordinal: 1600
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Copier update only delivers template changes to projects when a git tag exists, and there is no tag yet. Decide when and how to tag so that projects get stable updates.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Tag v0.1.0 created once the template has real content, and pushed
- [ ] #2 Versioning rule documented (what counts as a patch, minor or major; migrations for renamed questions)
- [ ] #3 Verified with a real copier update from one tag to the next on a scratch project
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

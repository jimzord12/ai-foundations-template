---
id: TASK-16
title: Release and tag policy for the template
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 16:40'
labels:
  - release
milestone: m-0
dependencies: []
priority: medium
type: chore
ordinal: 16000
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

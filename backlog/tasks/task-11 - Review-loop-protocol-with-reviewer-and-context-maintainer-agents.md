---
id: TASK-11
title: Review-loop protocol with reviewer and context-maintainer agents
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
labels:
  - review
  - agents
dependencies: []
priority: medium
type: feature
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner experience: independent fresh-context review loops are very valuable, so the round cap goes up: 8 rounds attended, 15 unattended (interpreted as caps, stop on PASS). Cap exists only for rare stuck-agent edge cases.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Reviewer and context-maintainer agent definitions in the template (fresh context each round, PASS/FINDINGS/INCOMPLETE, Blocking/Material/Minor/Note)
- [ ] #2 Protocol states caps 8 attended and 15 unattended; unresolved after cap goes to the owner
<!-- AC:END -->

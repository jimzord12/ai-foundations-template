---
id: TASK-21
title: A/B comparison and regression gate for template versions
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
updated_date: '2026-10-01 16:40'
labels:
  - testing
  - evals
milestone: m-2
dependencies:
  - TASK-20
priority: medium
type: feature
ordinal: 21000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Answer 'does this template do more good than harm': run the same eval tasks with no instructions, the previous template version and the new one, and compare pass rates, tokens and time. Use the result to gate tags (TASK-16) so a template release cannot make agents worse. Also track the token cost of the AGENTS.md itself, since it is loaded every session.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Comparison report across no-instructions, previous version and new version, stored per template version
- [ ] #2 Rule for what counts as a regression, and the tag process (TASK-16) checks it
- [ ] #3 Instruction size and per-session token cost recorded for each version
<!-- AC:END -->

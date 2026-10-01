---
id: TASK-5
title: 'Decide single decision log: docs/decisions.md vs Backlog.md decisions'
status: To Do
assignee: []
created_date: '2026-09-29 10:28'
updated_date: '2026-10-01 19:29'
labels:
  - decision
milestone: m-1
dependencies: []
priority: low
ordinal: 5000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Backlog.md has its own backlog/decisions/ records (one file per decision). We currently use a single docs/decisions.md, which the agent instructions reference. Decide whether to keep docs/decisions.md or move to Backlog.md decisions, for this repo and for generated projects.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Choice recorded; agent instructions and template updated to match
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: decided as part of the project knowledge system (docs/decisions.md entry of that date): neither the single file nor Backlog.md decisions; generated projects use one MADR file per decision in docs/decisions/. Implementation and the question for this repo moved to TASK-25. Archived to avoid duplicate tracking.
<!-- SECTION:NOTES:END -->

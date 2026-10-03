---
id: TASK-8
title: 'Owner-inbox JSON schemas, .foundations folder and validator'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-03 20:11'
labels:
  - schemas
  - inbox
milestone: m-1
dependencies: []
priority: high
type: feature
ordinal: 8000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Everything the owner must know, approve or decide has to be structured data so a viewer can render it. Viewer-agnostic schemas are needed now because the generic viewer (TASK-6) is blocked; Night Shift's ask/feedback commands cover the gap meanwhile. Approvals and questions are JSON; the history log stays markdown.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 JSON Schemas for question (2-6 options plus recommendation), decision, finding and proposal, with a versioned schema field
- [ ] #2 Template ships them under a .foundations folder plus a validate command agents can run
- [ ] #3 Interim use with Night Shift ask/feedback documented
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
2026-10-01: the owner is designing the feedback loop (self-improvement system) with another agent and will bring back a markdown with the design and decisions. Re-check this task against that design before starting.

2026-10-03 owner: the feedback-loop design will come at some point, not now. Keep this task waiting for it; do not plan it without that design.
<!-- SECTION:NOTES:END -->

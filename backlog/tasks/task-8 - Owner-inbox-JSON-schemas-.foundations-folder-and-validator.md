---
id: TASK-8
title: 'Owner-inbox JSON schemas, .foundations folder and validator'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-01 16:40'
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

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: the owner is designing the feedback loop (self-improvement system) with another agent and will bring back a markdown with the design and decisions. Re-check this task against that design before starting.
<!-- SECTION:NOTES:END -->

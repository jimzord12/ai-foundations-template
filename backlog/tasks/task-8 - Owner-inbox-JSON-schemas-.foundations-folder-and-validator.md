---
id: TASK-8
title: 'Owner-inbox JSON schemas, .foundations folder and validator'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
labels:
  - schemas
  - inbox
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

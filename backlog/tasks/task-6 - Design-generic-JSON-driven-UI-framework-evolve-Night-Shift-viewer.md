---
id: TASK-6
title: Design generic JSON-driven UI framework (evolve Night Shift viewer)
status: To Do
assignee: []
created_date: '2026-09-29 11:17'
labels:
  - night-shift
  - viewer
  - blocked-external
dependencies: []
references:
  - 'C:\Users\jimzord12\Documents\GitHub\night-shift'
priority: medium
type: feature
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner decision (2026-09-29): the shared owner-facing viewer is Night Shift, evolved into a generic mini-framework where agents describe UIs in JSON and a validator checks the schema, instead of building a viewer inside this template. Night Shift's views are hard-wired to 'nights' today. BLOCKED EXTERNALLY: start only once the Night Shift UI Viewer (repo C:\Users\jimzord12\Documents\GitHub\night-shift) has stabilized. Needs a dedicated deep design discussion with the owner before any code; details matter.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Design discussion held with owner; decisions recorded in docs/decisions.md
- [ ] #2 JSON UI schema and validation tooling specified (owner-decision, finding, proposal, report as first item kinds)
- [ ] #3 Migration path from Night Shift's night-specific types to the generic model agreed
- [ ] #4 Template ships schemas plus a register-this-project step (no viewer copy per project)
<!-- AC:END -->

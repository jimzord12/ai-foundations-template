---
id: TASK-6
title: >-
  Create a separate repo for the generic JSON-driven viewer framework (evolved
  from Night Shift)
status: To Do
assignee: []
created_date: '2026-09-29 11:17'
updated_date: '2026-10-01 21:26'
labels:
  - night-shift
  - viewer
  - blocked-external
  - separate-repo
milestone: m-3
dependencies: []
references:
  - 'C:\Users\jimzord12\Documents\GitHub\night-shift'
priority: medium
type: feature
ordinal: 6000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner decision (2026-09-29): the shared owner-facing viewer is Night Shift evolved into a generic mini-framework where agents describe UIs in JSON and a validator checks the schema. That is far beyond the scope of this template, so it is built in its OWN repository, not here. This task tracks creating that repo and keeping this template's part small. First open point for the design session: is the new repo Night Shift itself (evolved in place) or a new repo that Night Shift becomes a consumer of. BLOCKED EXTERNALLY: start only once Night Shift's UI viewer (C:\Users\jimzord12\Documents\GitHub\night-shift) has stabilized. Needs a dedicated deep design discussion with the owner before any code; details matter. Start with fixed item kinds (question, finding, proposal, report) and generalize on the third real need. What stays in THIS template: viewer-agnostic JSON schemas (TASK-8) and a register-this-project step, nothing else.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Design discussion held with owner; decisions recorded in docs/decisions/
- [ ] #2 Repo home decided (Night Shift evolved in place vs new repo) and the repo created on GitHub, with its own backlog and instructions
- [ ] #3 Generic JSON UI schema and validation tooling specified in that repo (question, finding, proposal, report as first item kinds)
- [ ] #4 Migration path from Night Shift's night-specific types to the generic model agreed
- [ ] #5 This template only links to it: schemas from TASK-8 plus a register-this-project step, no viewer code copied here
<!-- AC:END -->

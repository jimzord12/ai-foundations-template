---
id: TASK-27
title: 'CI workflow for generated projects: check and secret scanning'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-01 20:20'
labels:
  - ci
  - stack
milestone: m-0
dependencies:
  - TASK-2.4
priority: high
type: feature
ordinal: 1500
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner decision 2026-10-01: generated projects get one minimal CI workflow in v0.1.0 so agent changes are checked on every push. It runs the project's check script (from TASK-2.4); TASK-23 adds the secret-scanning step to it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Template ships .github/workflows/check.yml for every stack that runs npm ci and npm run check
- [ ] #2 Workflow is green on a freshly generated project per stack pushed as a branch to the owner-approved scratch repository (open owner question Q1), and red when a check fails; the agent deletes only branches it created, never repositories
- [ ] #3 Action versions verified against current docs and recorded
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

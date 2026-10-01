---
id: TASK-2.4
title: 'Check commands: package scripts and AGENTS.md'
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-01 19:51'
labels:
  - stack
  - instructions
milestone: m-0
dependencies:
  - TASK-2.1
  - TASK-2.2
  - TASK-2.3
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1200
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents must know the exact fast commands to run (typecheck, lint, test, one combined check). Ship them as package.json scripts per stack and name them in the AGENTS.md stack blocks.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Scripts typecheck, lint, test and check exist per stack and pass on a freshly scaffolded project
- [ ] #2 AGENTS.md stack blocks name the exact commands
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

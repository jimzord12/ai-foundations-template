---
id: TASK-2.4
title: 'Check commands: package scripts and AGENTS.md'
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-02 16:45'
labels:
  - stack
  - instructions
milestone: m-0
dependencies:
  - TASK-2.1
  - TASK-2.2
  - TASK-2.3
  - TASK-2.5
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1400
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents must know the exact fast commands to run (typecheck, lint, test, one combined check). The contract is the same for every pack; the scripts come from 2.1 to 2.3 (where they live: TASK-2.5 criterion 1) and each pack names them.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Post-copy task adds only the combined check script (runs typecheck, lint, format:check and test, which 2.1-2.3 add)
- [ ] #2 npm run check passes on a freshly scaffolded project for each Phase 1 pack, and fails when any one of the four fails
- [ ] #3 The packs and AGENTS.md name the exact commands, within the line budget of the phase plan
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
2026-10-02 (TASK-15): template done.md and its Backlog definition_of_done line name the combined script npm run check; keep that name.

2026-10-02: ready label removed: criteria changed after the challenge (record 0040, ready.md); plan and challenge again before unattended work, or the owner waives it.
<!-- SECTION:NOTES:END -->

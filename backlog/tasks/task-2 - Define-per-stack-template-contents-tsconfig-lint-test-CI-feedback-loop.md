---
id: TASK-2
title: >-
  Per-stack baseline: strict TypeScript, lint/format, tests, check commands
  (parent)
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
updated_date: '2026-10-01 20:26'
labels:
  - template
  - tooling
  - ready
milestone: m-0
dependencies:
  - TASK-2.1
  - TASK-2.2
  - TASK-2.3
  - TASK-2.4
  - TASK-2.5
priority: high
ordinal: 1450
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Parent for the technical baseline every generated project gets, split into one-change subtasks. Stacks: Express 5 + Zod, Next.js 16.3, bare React Native at the current stable of @react-native-community/template (owner answer 2026-10-01; verify the version when 2.5 starts). Start with TASK-2.5 (integration mechanism and Express skeleton); 2.1-2.3 build on it; 2.4 wires the check commands. CI is owned by TASK-13 (template repo) and TASK-27 (generated projects); the done rule by TASK-15.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 All subtasks Done
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

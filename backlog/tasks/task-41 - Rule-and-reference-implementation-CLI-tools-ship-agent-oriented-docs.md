---
id: TASK-41
title: 'Rule and reference implementation: CLI tools ship agent-oriented docs'
status: To Do
assignee: []
created_date: '2026-10-03 20:11'
updated_date: '2026-10-03 20:13'
labels:
  - instructions
  - cli
milestone: m-1
dependencies:
  - TASK-4
priority: medium
type: feature
ordinal: 26000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents build and use many CLI tools and should learn why, how and what a command does without reading its code. The owner used this pattern in an earlier tool and it was very useful to agents. The design comes from the TASK-4 spike; this task turns it into a rule and something agents can copy.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Rule text added to the template's agent instructions (AGENTS.md at most 2 lines, detail in a protocol) following the design recorded by TASK-4
- [ ] #2 A shared helper or reference implementation ships with a test that fails when a command has no docs (and, if TASK-4 adopted size budgets, when its docs exceed one)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

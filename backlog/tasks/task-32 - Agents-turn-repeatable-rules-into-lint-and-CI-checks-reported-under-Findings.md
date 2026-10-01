---
id: TASK-32
title: 'Agents turn repeatable rules into lint and CI checks, reported under Findings'
status: To Do
assignee: []
created_date: '2026-10-01 23:02'
labels:
  - agents
  - lint
  - ci
  - reporting
milestone: m-0
dependencies:
  - TASK-15
priority: medium
ordinal: 24000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner request 2026-10-02. Instructions alone drift: a rule an agent must remember gets forgotten, while a lint rule or CI check enforces it on every change for every agent. Agents in generated projects (and in this repo) are therefore recommended to add, update or create lint and CI rules whenever a convention, a recurring review finding or a past mistake can be caught mechanically. The owner wants to see them: every end-of-task report lists them in a 'Lint and CI rules' subsection of its Findings section. The report shape comes from TASK-15 (docs/protocols/done.md); the subagent findings block in TASK-9 should reuse the same subsection once it is built. Lint tooling per stack is TASK-2.2, generated-project CI is TASK-27.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Template rule (AGENTS.md at most 2 lines, detail in a linked protocol): when a convention, recurring review finding or past mistake can be checked mechanically, add, update or create a lint rule or CI check in the same change; prefer an existing rule or plugin over a custom one, and do not add speculative rules
- [ ] #2 The end-of-task report defined by TASK-15 has a Findings section with a 'Lint and CI rules' subsection listing rules added, changed or created (file and one-line reason) and rules proposed but not added (with why); the subsection says 'none' when empty
- [ ] #3 This repo's root AGENTS.md carries the same recommendation and report subsection for agents working on the template
- [ ] #4 Smoke test passes for all three stacks; rendered AGENTS.md stays within the line budget; decision recorded in docs/decisions/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

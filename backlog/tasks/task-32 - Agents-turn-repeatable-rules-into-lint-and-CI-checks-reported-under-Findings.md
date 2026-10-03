---
id: TASK-32
title: 'Agents turn repeatable rules into lint and CI checks, reported under Findings'
status: To Do
assignee: []
created_date: '2026-10-01 23:02'
updated_date: '2026-10-03 20:11'
labels:
  - agents
  - lint
  - ci
  - reporting
milestone: m-1
dependencies:
  - TASK-15
  - TASK-2.2
  - TASK-27
priority: medium
type: feature
ordinal: 11000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner request 2026-10-02. Instructions alone drift: a rule an agent must remember gets forgotten, while a lint rule or CI check enforces it on every change for every agent. Agents in generated projects (and in this repo) are therefore recommended to add, update or create lint and CI rules whenever a convention, a recurring review finding or a past mistake can be caught mechanically. The owner wants to see them: every end-of-task report lists them in a 'Lint and CI rules' subsection of its Findings section. The report shape comes from TASK-15 (docs/protocols/done.md); the subagent findings block in TASK-9 should reuse the same subsection once it is built. Lint tooling per stack is TASK-2.2, generated-project CI is TASK-27.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Template rule (AGENTS.md at most 2 lines, detail in docs/protocols/checks.md): when a convention, recurring review finding or past mistake can be checked mechanically, add or update a lint rule or CI check in the same change when it is cheap, otherwise propose it in the report; prefer an existing rule or plugin over a custom one; no speculative rules
- [ ] #2 done.md's Findings section (defined by TASK-15) gains a 'Lint and CI rules' subsection listing rules added or changed (file and one-line reason) and rules proposed but not added (with why); when empty it folds into one line such as 'Lint/CI: none'; one line says an accepted proposal becomes a Backlog task (or a GitHub issue once the findings pipeline exists)
- [ ] #3 This repo's root AGENTS.md gets at most 3 lines carrying the same recommendation and naming where this repo's end-of-task report lists the subsection
- [ ] #4 TASK-9 carries a note that the subagent findings block reuses this subsection
- [ ] #5 Smoke test passes for all three stacks; rendered AGENTS.md stays within the line budget; decision recorded in docs/decisions/
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
Moved to phase 2 on 2026-10-02 by the owner: not needed for a usable v0.1.0, and it builds on the lint and TypeScript baseline (TASK-2.x) that phase 1 delivers.
<!-- SECTION:NOTES:END -->

---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-01 21:25'
labels:
  - instructions
  - charter
  - ready
milestone: m-0
dependencies:
  - TASK-25
priority: high
type: feature
ordinal: 200
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The main agent acts as tech lead and senior engineer and owns the codebase; the owner is a technical product owner who does not want to babysit. Agents need explicit rules for what they decide alone (bounded by the repo's instruction files) versus what goes to the owner (hard-to-reverse list), and concrete signals for when to move from simple code to patterns to restructured folders.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Authority tiers moved from the AGENTS.md section Who decides what into docs/protocols/charter.md with the mapping per decision kind (product: owner; architecture: agent proposes, owner approves big ones; technical: agent decides and logs); AGENTS.md keeps a short pointer
- [ ] #2 Design evolution protocol in docs/protocols/evolution.md: measurable signals, procedure (architecture decision record, owner approval for big changes, pure-move commit then reference commit, update architecture.md and glossary in the same change, tests and review pass), step-down rule
- [ ] #3 Decision named Design evolution protocol and authority tiers recorded; smoke test passes
- [ ] #4 Interim rules stated where Phase 2 is not built yet: friction signals come from the end-of-task summary until a findings pipeline exists; the full safe-move protocol arrives in a later template version. Shipped text never names this repo's task IDs
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
2026-10-01 owner of authority tiers (who decides what). TASK-25 references these tiers for who decides each decision kind instead of restating them.
<!-- SECTION:NOTES:END -->

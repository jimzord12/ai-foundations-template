---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: In Progress
assignee:
  - '@claude'
created_date: '2026-09-29 11:39'
updated_date: '2026-10-02 00:06'
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

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Stop condition: start only after TASK-31 is merged into main (record 0027 exists on main); branch feature/task-7-charter from main. New record is 0028.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of authority tiers (who decides what). TASK-25 references these tiers for who decides each decision kind instead of restating them.

Moved-rule table (old template AGENTS.md line -> new home): 23 'You decide' -> stays in AGENTS.md; 24 kind mapping -> stays (one line) plus pointer to charter.md for 'big'; 25 hard-to-reverse list -> stays in AGENTS.md only (charter.md references it); 26 supersede wording -> removed from AGENTS.md, owned by docs/decisions/README.md line 8; 27 end-of-task decision summary -> stays (done.md will own detail, TASK-15 note); 30 Evolve paragraph -> one ladder line plus rule of three in AGENTS.md, signals/bands/move/step-down in evolution.md, interim proposal-pipeline wording dropped (roadmap moved to record 0028). Verification: smoke express/next/rn exit 0, AGENTS.md 57/58/57 lines (was 55/56/55), no Jinja leftovers, all router paths exist except the docs/adr/ brownfield example; reference grep shows only valid 'Who decides what' / 'Evolve the codebase' references; leak grep (TASK-, task-, Phase N, findings pipeline, 0008, 0018) finds nothing in template/.
<!-- SECTION:NOTES:END -->

---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-01 23:12'
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
1. Branch feature/task-7-charter from main after TASK-31 merges.
2. template/docs/protocols/charter.md: roles (agent = tech lead and senior engineer who owns the codebase; owner = technical product owner); authority tiers per decision kind (product: owner decides; architecture: agent proposes, owner approves big changes, with a concrete test for 'big': crosses a boundary named in architecture.md, adds a project-wide pattern or layer, moves or renames many files, or changes a public API or data model; technical: agent decides and records); the hard-to-reverse list always goes to the owner (database, auth provider, hosting and infrastructure, paid services, core framework changes, anything contradicting the instructions) with options, tradeoffs and a recommendation; do not re-argue a recorded decision without new facts; end-of-task one-line-per-decision summary.
3. template/docs/protocols/evolution.md: ladder (inline code, function, module, pattern or interface, folder restructure, ports and adapters at a boundary); measurable signals (second copy note it, third extract it; file over about 300 lines or function over about 50; one change needing edits in more than 3 folders; the same bug fixed twice; test setup pain; a second business area means glossary level 2); procedure (architecture record status proposed, owner approval for big changes, one commit that only moves or renames and updates references with checks green, then separate commits for behaviour, update architecture.md and the glossary in the same change, tests and review pass); step-down rule (an abstraction with one implementation and no second in sight, or indirection nobody uses, is removed through a new record that supersedes the old); interim rules (friction signals come from the end-of-task summary until a findings pipeline exists; the full safe-move protocol arrives in a later template version). No task IDs of this repo in shipped text.
4. template/AGENTS.md.jinja: 'Who decides what' shrinks to a pointer that still names the owner-only hard-to-reverse list in one line (always loaded, safety-critical); 'Evolve the codebase' shrinks to a pointer plus the ladder in one line; router rows for charter.md and evolution.md. Net line change negative or at most +4; rendered <= 100 lines. template/docs/decisions/README.md Kinds bullet points to charter.md instead of AGENTS.md 'Who decides what'.
5. Decision record 'Design evolution protocol and authority tiers' (kind product, owner-approved design 2026-10-01) plus index row.
6. Verify: smoke test 3 stacks (files present, no Jinja leftovers, line count, router paths exist); grep that every pointer target exists; grep shipped files for TASK- IDs (none).
7. Independent review loop to PASS; merge, push, delete branch.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of authority tiers (who decides what). TASK-25 references these tiers for who decides each decision kind instead of restating them.
<!-- SECTION:NOTES:END -->

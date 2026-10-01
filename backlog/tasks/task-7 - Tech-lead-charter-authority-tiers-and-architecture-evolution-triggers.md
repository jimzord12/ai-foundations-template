---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-01 19:29'
labels:
  - instructions
  - charter
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 7000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The main agent acts as tech lead and senior engineer and owns the codebase; the owner is a technical product owner who does not want to babysit. Agents need explicit rules for what they decide alone (bounded by the repo's instruction files) versus what goes to the owner (hard-to-reverse list), and concrete signals for when to move from simple code to patterns to restructured folders.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Charter text (in AGENTS.md or a linked protocol) defines decide-alone vs ask tiers, bounded by repo instructions
- [ ] #2 Evolution triggers defined: rule of three plus friction counts from findings; restructuring is a lead decision surfaced as a proposal
- [ ] #3 Decision recorded in docs/decisions.md
- [ ] #4 Design evolution protocol written as a linked file: measurable signals (third duplication, second business area, second external service of one kind, folder past about 25 files or circular imports, repeated findings), the procedure (architecture decision record, owner approval for big changes, safe-move protocol from TASK-22, update architecture.md and glossary in the same change, tests and review pass), and the step-down rule (propose removing patterns that never paid off)
<!-- AC:END -->

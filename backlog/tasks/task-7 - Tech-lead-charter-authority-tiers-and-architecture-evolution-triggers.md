---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
labels:
  - instructions
  - charter
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
<!-- AC:END -->

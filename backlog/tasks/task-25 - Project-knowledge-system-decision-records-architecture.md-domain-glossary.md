---
id: TASK-25
title: 'Project knowledge system: decision records, architecture.md, domain glossary'
status: To Do
assignee: []
created_date: '2026-10-01 19:29'
updated_date: '2026-10-01 20:14'
labels:
  - knowledge
  - decisions
  - ddd
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 100
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner-approved design (2026-10-01, see docs/decisions.md). Generated projects get one knowledge system, separate from the feedback loop and linked to it only through decision records. (1) Decisions: one file per decision in docs/decisions/ using the MADR standard, front matter with kind (product | architecture | technical), status, date, deciders, supersedes; an index README. Who decides: product = owner; architecture = agent proposes, owner approves big ones; technical = agent decides and logs. (2) docs/architecture.md = the current shape (folder map, layers, key flows, links to decisions); starts nearly empty and must be updated in the same change as every accepted architecture decision. (3) DDD, mandatory but levelled: level 1 always on = docs/domain/glossary.md (term, meaning, not-this, context; agents use terms in code and UI, add terms, flag synonyms); level 2 when a second business area appears = docs/domain/contexts.md; level 3 tactical patterns only via architecture decisions. Replaces the single-file docs/decisions.md for generated projects and absorbs TASK-5. Verify the current MADR version before adopting its template.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 template/docs/decisions/ ships a MADR-based record template with kind, status, date, deciders, supersedes, plus an index; template/docs/decisions.md removed
- [ ] #2 template/docs/architecture.md and template/docs/domain/glossary.md ship as short starters; contexts.md documented as level 2, created only when needed
- [ ] #3 Template AGENTS.md: check decisions before deciding, update architecture.md with every architecture decision, use and maintain the glossary, and if the project already has an ADR folder use it instead (brownfield rule kept); who decides each kind references the tiers owned by TASK-7
- [ ] #4 This repo migrates its own docs/decisions.md to one file per decision (owner answer 2026-10-01) and updates in the same change every reference: root AGENTS.md, README, backlog config definition_of_done, task descriptions and acceptance criteria that name docs/decisions.md
- [ ] #5 Smoke test passes for all stacks; rendered AGENTS.md stays within the line budget
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

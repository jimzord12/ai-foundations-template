---
id: TASK-25
title: 'Project knowledge system: decision records, architecture.md, domain glossary'
status: To Do
assignee: []
created_date: '2026-10-01 19:29'
labels:
  - knowledge
  - decisions
  - ddd
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 25000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner-approved design (2026-10-01, see docs/decisions.md). Generated projects get one knowledge system, separate from the feedback loop and linked to it only through decision records. (1) Decisions: one file per decision in docs/decisions/ using the MADR standard, front matter with kind (product | architecture | technical), status, date, deciders, supersedes; an index README. Who decides: product = owner; architecture = agent proposes, owner approves big ones; technical = agent decides and logs. (2) docs/architecture.md = the current shape (folder map, layers, key flows, links to decisions); starts nearly empty and must be updated in the same change as every accepted architecture decision. (3) DDD, mandatory but levelled: level 1 always on = docs/domain/glossary.md (term, meaning, not-this, context; agents use terms in code and UI, add terms, flag synonyms); level 2 when a second business area appears = docs/domain/contexts.md; level 3 tactical patterns only via architecture decisions. Replaces the single-file docs/decisions.md for generated projects and absorbs TASK-5. Verify the current MADR version before adopting its template.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 template/docs/decisions/ ships a MADR-based template with the kind field and an index; old single-file template/docs/decisions.md replaced
- [ ] #2 template/docs/architecture.md and template/docs/domain/glossary.md ship as short starters; contexts.md documented as level 2 (created when needed)
- [ ] #3 AGENTS.md router and rules updated: check decisions before deciding, who decides per kind, update architecture.md with architecture decisions, use and maintain the glossary
- [ ] #4 Decide and record whether this template repo migrates its own docs/decisions.md to the same format
- [ ] #5 Smoke test passes for all stacks; independent review rounds pass
<!-- AC:END -->

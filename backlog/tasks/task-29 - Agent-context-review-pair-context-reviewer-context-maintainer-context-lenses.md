---
id: TASK-29
title: >-
  Agent-context review pair: context-reviewer, context-maintainer,
  context-lenses
status: To Do
assignee: []
created_date: '2026-10-01 20:52'
labels:
  - review
  - agents
  - docs
milestone: m-0
dependencies:
  - TASK-11
priority: high
type: feature
ordinal: 650
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Most of this template is agent context (AGENTS.md, protocols, agent profiles, skills), and changes to it were going unreviewed. The owner already runs mature context reviewer and maintainer pairs in the ICS workspace (.claude/agents/agent-context-reviewer.md, agent-context-maintainer.md) and in night-shift and cvgen (context-reviewer, context-maintainer). Extract their generic core, drop everything repo-specific (product names, paths, glossary locations, line-ending rules, the sensitive-data paragraph), and add the gaps found on 2026-10-01: literal-reader safety, frontmatter checks (trigger description, least-privilege tools, model fit), router reachability (a file no pointer names is as absent as one never written), line budgets, Claude/Codex parity, rotating lead lenses per round. Decision: 'Two documentation reviewer families with shared skills'.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 context-lenses skill ships with: principle written before reading the diff, placement and owning file, integrate not append, principle vs example (overfit and over-general), terminology against glossary and code, timeless files carry no dates, literal-reader safety, frontmatter checks, router reachability, line budgets, Claude/Codex parity, anti-overcorrection guards, and a lead-lens rotation table
- [ ] #2 context-reviewer profile (Read, Grep, Glob only; no Agent; Opus, high) preloads review-core and context-lenses; context-maintainer profile (adds Edit and Write, documentation files only, never deletes or renames, never edits dated records) preloads context-lenses
- [ ] #3 Both ship in template/ and in this repo (pairs in dogfood.json); a grep over the shipped files finds none of the source repos' names, paths or product terms
- [ ] #4 Proof: the shipped context-reviewer reviews one real instruction change in this repo, quotes a marker line from context-lenses, and its report is saved in the task notes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

---
id: TASK-28
title: 'Codex: expose shared skills natively'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-01 20:26'
labels:
  - codex
  - skills
  - ready
milestone: m-0
dependencies:
  - TASK-11
  - TASK-24
priority: medium
type: feature
ordinal: 800
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner decision 2026-10-01: in v0.1.0 Codex gets only what it supports natively: AGENTS.md (already shared) and skills. Skills are the shared knowledge layer (agents+skills decision), so Codex should read the same skill files as Claude Code, with one source of truth. Verify Codex's current skill location and format before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Codex's current skill discovery location and format verified from its docs and recorded
- [ ] #2 Shared skills are available to Codex from one source of truth; any copy is recorded as a source-to-copy pair in the dogfood manifest (checked later by TASK-13)
- [ ] #3 Verified in a live Codex session that lists or uses one shared skill
- [ ] #4 Rule recorded in docs/protocols/agents.md: every new shared skill gets its Codex pair in the dogfood manifest
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

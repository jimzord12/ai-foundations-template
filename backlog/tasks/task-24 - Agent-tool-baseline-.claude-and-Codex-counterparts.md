---
id: TASK-24
title: 'Agent tool baseline: .claude/ and Codex counterparts'
status: To Do
assignee: []
created_date: '2026-10-01 16:40'
updated_date: '2026-10-01 19:51'
labels:
  - agents
  - claude
  - codex
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Claude Code is the owner's main coding agent, but Codex is also used at times. Permissions, hooks, subagent definitions and skills are currently scattered across TASK-9, TASK-11, TASK-12 and TASK-22 with no owner. This task owns the baseline layout for both tools: Claude Code (.claude/settings.json, agents, skills) and the Codex equivalents. AGENTS.md is already shared by both. Verify current Claude Code and Codex docs for config, skills and agent file locations before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Baseline .claude/ layout shipped (settings with a sensible permission allowlist, folders for agents and skills) and documented in the AGENTS.md router
- [ ] #2 Codex counterparts shipped where Codex supports them (config, skills or agents), with one source of truth so the two do not drift
- [ ] #3 Other tasks that add agents, skills or hooks reference this layout; decision recorded
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of the .claude/ and Codex layout. TASK-11 (reviewer agents) and TASK-22 (maintenance skill) put their files into this layout.
<!-- SECTION:NOTES:END -->

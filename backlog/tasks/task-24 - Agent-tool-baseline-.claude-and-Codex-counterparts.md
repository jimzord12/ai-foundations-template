---
id: TASK-24
title: 'Agent tool baseline: .claude/ layout, permission allowlist, dogfood manifest'
status: To Do
assignee: []
created_date: '2026-10-01 16:40'
updated_date: '2026-10-01 20:20'
labels:
  - agents
  - claude
  - codex
milestone: m-0
dependencies:
  - TASK-15
priority: high
type: feature
ordinal: 500
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner of the agent-tool layout for this repo and generated projects. Layout rule (decision 2026-10-01, specific thin agent profiles plus shared skills): .claude/agents/ holds one-job profiles that preload skills; .claude/skills/ holds the shared knowledge. Codex native support is TASK-28. Permission allowlist per owner answer 2026-10-01. Verify current Claude Code settings and agent docs before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 .claude/settings.json ships with an allowlist of: read-only tools, package scripts, backlog, git add/commit/push; nothing broader
- [ ] #2 .claude/agents/ and .claude/skills/ layout documented in the AGENTS.md router (at most 4 lines) and in docs/protocols/agents.md (thin profiles, skills preloaded with the skills field, read-only reviewers get no Edit or Write)
- [ ] #3 Dogfood manifest (one JSON file in this repo) lists source-to-copy pairs. Initial scope: .claude/agents/*, .claude/skills/*, docs/protocols/review.md, ready.md, agents.md. Template-only files (charter.md, evolution.md, git.md, done.md, stack files) are not copied. Later tasks add their pairs to it
- [ ] #4 Proof via headless claude -p in a generated project: an allowlisted command runs without a permission prompt and a non-listed command does not
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

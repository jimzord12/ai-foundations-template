---
id: TASK-24
title: 'Agent tool baseline: .claude/ layout, permission allowlist, dogfood manifest'
status: To Do
assignee: []
created_date: '2026-10-01 16:40'
updated_date: '2026-10-01 21:26'
labels:
  - agents
  - claude
  - codex
  - ready
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
- [ ] #1 template/.claude/settings.json ships with an allowlist of: read-only tools, package scripts, backlog, git add/commit/push, and the branch commands git switch, git branch, git merge and git push --delete (amended owner answer 5); nothing broader. This repo gets its own root .claude/settings.json with the same allowlist minus package scripts
- [ ] #2 .claude/agents/ and .claude/skills/ layout documented in the router of both the root and the template AGENTS.md (at most 4 lines each) and in docs/protocols/agents.md (thin profiles, skills preloaded with the skills field, read-only reviewers get no Edit or Write, dogfooded files must not be .jinja or link to template-only files)
- [ ] #3 Dogfood manifest at dogfood.json in this repo's root lists source-to-copy pairs. TASK-24 adds only docs/protocols/agents.md and the .claude/agents/* and .claude/skills/* globs; TASK-11 adds review.md and TASK-26 adds ready.md when they create them. Template-only files (charter.md, evolution.md, git.md, done.md, stack files) are never copied
- [ ] #4 Proof via headless claude -p --output-format json in a generated project, run with --setting-sources project (or a clean CLAUDE_CONFIG_DIR) and without --allowedTools, --permission-mode or any permission-skipping flag: an allowlisted command runs without a permission prompt, and a non-listed command appears in permission_denials
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of the .claude/ and Codex layout. TASK-11 (reviewer agents) and TASK-22 (maintenance skill) put their files into this layout.

2026-10-01: allowlist amended with branch commands (decision 'Branch model refinements after the first instruction review').
<!-- SECTION:NOTES:END -->

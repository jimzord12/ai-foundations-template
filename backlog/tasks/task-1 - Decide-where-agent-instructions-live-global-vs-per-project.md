---
id: TASK-1
title: Decide where agent instructions live (global vs per-project)
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
labels:
  - decision
  - instructions
dependencies: []
priority: high
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The agreed baseline in docs/agent-instructions.md was written for a global CLAUDE.md. Proposal (not yet confirmed): move nearly all of it into each project via template/AGENTS.md.jinja so cloud sessions, CI agents, other tools and collaborators see it; keep only personal working style in the global ~/.claude/CLAUDE.md. Also proposed: AGENTS.md is canonical (cross-tool standard), CLAUDE.md just contains @AGENTS.md; stack-specific rules in .claude/rules/ with paths: frontmatter (Claude-only; other agents see only AGENTS.md).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Placement decided and recorded in docs/decisions.md
- [ ] #2 template/AGENTS.md.jinja contains the chosen content
- [ ] #3 Global CLAUDE.md scope written down
<!-- AC:END -->

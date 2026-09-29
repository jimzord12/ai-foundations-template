---
id: TASK-13
title: 'CI for the template: smoke-test all three stacks on every push'
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-09-29 22:47'
labels:
  - ci
  - quality
dependencies: []
priority: high
type: chore
ordinal: 13000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The smoke test (copier copy for express, next, rn) is manual today and easy to forget; one broken template breaks every new project. Run it automatically on push and pull request.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 GitHub Actions workflow renders all three stacks with the AGENTS.md smoke-test command and fails on error
- [ ] #2 Workflow also fails on leftover Jinja syntax in rendered files and on a missing stack block in AGENTS.md
- [ ] #3 Action and uv versions verified against current docs; workflow green on main
- [ ] #4 CI fails if this repo's own .claude/skills/repo-maintenance copy differs from template/.claude/skills/repo-maintenance (single source of truth, see TASK-22 decision)
<!-- AC:END -->

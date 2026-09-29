---
id: TASK-14
title: Git and safety rules in the template AGENTS.md
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
labels:
  - instructions
  - git
dependencies: []
priority: high
type: feature
ordinal: 14000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The generated AGENTS.md has no git or safety rules. Earlier projects (agentic-wave, cvgen, night-shift) had an impact-based rule: routine commits and pushes are allowed, high-impact actions (rewriting shared history, deleting unique work, touching production or security) require asking with the exact action and consequence. Needs a neutral default that per-project or personal rules can tighten.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Neutral git and safety section added to template/AGENTS.md.jinja (or a linked protocol) and kept short
- [ ] #2 Rule is impact-based, not a command blocklist, and states what to show when asking (exact action, targets, consequence)
- [ ] #3 Decision recorded in docs/decisions.md; smoke test passes for all stacks
<!-- AC:END -->

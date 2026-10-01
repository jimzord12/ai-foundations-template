---
id: TASK-14
title: Git and safety rules in the template AGENTS.md
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 20:14'
labels:
  - instructions
  - git
milestone: m-0
dependencies:
  - TASK-7
priority: high
type: feature
ordinal: 300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The generated AGENTS.md has no git or safety rules. Earlier projects (agentic-wave, cvgen, night-shift) had an impact-based rule: routine commits and pushes are allowed, high-impact actions (rewriting shared history, deleting unique work, touching production or security) require asking with the exact action and consequence. Needs a neutral default that per-project or personal rules can tighten.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Git and safety rules in docs/protocols/git.md, with at most 4 lines in AGENTS.md pointing to it
- [ ] #2 Rule is impact-based, not a command blocklist, consistent with the permission allowlist of TASK-24, and states what to show when asking (exact action, targets, consequence)
- [ ] #3 Decision recorded; smoke test passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

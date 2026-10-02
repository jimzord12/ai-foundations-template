---
id: TASK-39
title: Ship the protocol check to generated projects
status: To Do
assignee: []
created_date: '2026-10-02 16:45'
labels:
  - feature
dependencies: []
priority: medium
ordinal: 28000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
scripts/protocol_check.py runs only in this repo, on template/ (decision 0040). A generated project that adds or renames a protocol, profile or skill keeps the card format but has nothing that catches a missing card, router row or orphaned skill. Experiment TASK-36 showed agents rely on the check to get the structure right.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A generated project can run a protocol check against its own docs/protocols/, .claude/agents/, .claude/skills/ and AGENTS.md
- [ ] #2 The check is part of the project's documented checks, so agents run it after changing a protocol
- [ ] #3 The smoke render of all three stacks passes and the check passes on a fresh render
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

---
id: TASK-17
title: 'Automated template tests: render, copier update, collision cases'
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
updated_date: '2026-10-01 19:51'
labels:
  - testing
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 1300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Cheap, deterministic layer of the testing strategy, no agents involved. Today only a manual render smoke test exists. CI (TASK-13) will run these.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Render test for every stack: right files, exactly one stack block, no leftover Jinja, links resolve
- [ ] #2 copier update test: tag v(n) to v(n+1) on a scratch project keeps local edits under Project specifics and applies template changes
- [ ] #3 Collision tests: copy onto a project with its own AGENTS.md, CLAUDE.md and .gitignore (create-next-app case) behaves as documented
- [ ] #4 Each test verified to FAIL when the behavior it covers is broken (no tests that pass with the implementation deleted)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

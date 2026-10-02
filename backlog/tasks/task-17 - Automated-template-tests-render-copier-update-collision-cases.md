---
id: TASK-17
title: 'Automated template tests: render, copier update, collision cases'
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
updated_date: '2026-10-02 21:30'
labels:
  - testing
milestone: m-0
dependencies:
  - TASK-2.4
priority: high
type: feature
ordinal: 1600
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Cheap, deterministic layer of the testing strategy, no agents involved. Today only a manual render smoke test exists. CI (TASK-13) will run these.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Render test per Phase 1 pack: right files, the right pack in docs/stack.md, no leftover Jinja, links resolve, rendered AGENTS.md at most 100 lines
- [ ] #2 copier update test using local tags in a scratch clone: local edits under Project specifics kept, template change applied, a changed pack refreshed, the stored stack and skeleton answers kept
- [ ] #3 Collision tests on freshly scaffolded Next.js and RN projects, an existing Express project and the Express skeleton: AGENTS.md, CLAUDE.md, tsconfig, lint config and package.json land as documented, non-interactively; an existing Express project keeps its own package.json and src even with --overwrite
- [ ] #4 Each test shown red when the behaviour it covers is broken; harness language choice recorded
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
2026-10-02: record 0041 (stack-agnostic core with packs picked by detection): "per stack" in this task now means per Phase 1 pack (Next.js, bare React Native, Express); more frameworks are TASK-2.6. The render test checks that detection picks the right pack for sample package.json files; the check that pack files and the precedence list agree is TASK-2.5 criterion 9, so reuse it instead of restating it. The ready label was removed because this changes what the task must do; plan and challenge again before unattended work, or the owner waives it.

2026-10-03: TASK-2.5 was split; the pack-list check named above as TASK-2.5 criterion 9 is now TASK-2.5 criterion 3.
<!-- SECTION:NOTES:END -->

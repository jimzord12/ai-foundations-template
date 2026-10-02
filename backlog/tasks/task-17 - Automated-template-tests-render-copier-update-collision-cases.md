---
id: TASK-17
title: 'Automated template tests: render, copier update, collision cases'
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
updated_date: '2026-10-02 16:08'
labels:
  - testing
  - ready
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
- [ ] #1 Render test per stack: right files, one stack block, no leftover Jinja, links resolve, rendered AGENTS.md at most 100 lines
- [ ] #2 copier update test using local tags in a scratch clone: local edits under Project specifics kept, template change applied
- [ ] #3 Collision tests on freshly scaffolded Next.js and RN projects and the Express skeleton: AGENTS.md, CLAUDE.md, tsconfig, lint config and package.json land as documented, non-interactively
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
2026-10-02: record 0040 (stack-agnostic core with packs picked by detection): "per stack" in this task now means per pack, Phase 1 packs being Next.js, bare React Native and Express (more in TASK-2.6). The render test no longer looks for one stack block in AGENTS.md; it checks that the detector picks the right pack and that every pack it can return exists. Re-plan this at pickup.
<!-- SECTION:NOTES:END -->

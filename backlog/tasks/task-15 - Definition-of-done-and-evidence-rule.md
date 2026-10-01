---
id: TASK-15
title: Definition of done and evidence rule
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 21:26'
labels:
  - instructions
  - verification
  - ready
milestone: m-0
dependencies:
  - TASK-14
priority: high
type: feature
ordinal: 400
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner practice from agentic-wave and Night Shift: a green test does not prove behavior; agents run the real thing and show evidence; committed, pushed, tested and integrated are reported as separate facts; a test that passes with the implementation deleted must not be written. Needs to be part of what every generated project tells its agents. May overlap with TASK-2 (tests and CI per stack).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Definition of done written for generated projects (docs/protocols/done.md plus at most 4 lines in AGENTS.md), referencing npm run check by name
- [ ] #2 Covers: real-run evidence over claims, separate git and test facts, tests must exercise real code, mocks only at true external boundaries
- [ ] #3 Generated projects get Backlog Definition of Done defaults derived from done.md (not this repo's template-only items such as the smoke test), applied with backlog config set definitionOfDone after backlog init, as documented in AGENTS.md
- [ ] #4 Decision recorded; smoke test passes
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
2026-10-01: owns the done rule text; TASK-2 subtasks own the tooling it refers to.
<!-- SECTION:NOTES:END -->

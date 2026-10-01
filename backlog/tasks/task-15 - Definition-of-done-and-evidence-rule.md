---
id: TASK-15
title: Definition of done and evidence rule
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 16:40'
labels:
  - instructions
  - verification
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 15000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner practice from agentic-wave and Night Shift: a green test does not prove behavior; agents run the real thing and show evidence; committed, pushed, tested and integrated are reported as separate facts; a test that passes with the implementation deleted must not be written. Needs to be part of what every generated project tells its agents. May overlap with TASK-2 (tests and CI per stack).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Definition of done written for generated projects (linked protocol plus a short rule in AGENTS.md)
- [ ] #2 Covers: real-run evidence over claims, separate git and test facts, tests must exercise real code, mocks only at true external boundaries
- [ ] #3 Overlap with TASK-2 resolved (merged or clearly split) and decision recorded
<!-- AC:END -->

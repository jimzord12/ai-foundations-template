---
id: TASK-2
title: >-
  Per-stack baseline: strict TypeScript, lint/format, tests, check commands
  (parent)
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
updated_date: '2026-10-03 20:11'
labels:
  - template
  - tooling
milestone: m-0
dependencies:
  - TASK-2.1
  - TASK-2.2
  - TASK-2.3
  - TASK-2.4
  - TASK-2.5
  - TASK-2.7
  - TASK-2.8
priority: high
type: feature
ordinal: 1450
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Parent for the technical baseline every generated project gets, split into one-change subtasks. Stack-agnostic by design (record 0041): a generic core plus a small pack per framework; the stack question's default detects the framework from package.json and Copier renders the pack. The intended reach is any modern TypeScript project: web (Next.js, Astro, SvelteKit, Solid), mobile (bare React Native, Expo) and backend (Elysia, Hono, Fastify, Express, Nest.js). Phase 1 (v0.1.0) verifies the mechanism on Next.js 16.3, bare React Native at the current stable of @react-native-community/template (owner answer 2026-10-01; verify the version when 2.5 starts) and Express 5 + Zod; more frameworks arrive as packs (TASK-2.6). Start with TASK-2.5 (detection and packs), then TASK-2.7 (post-copy tasks) and TASK-2.8 (Express skeleton); 2.1-2.3 build on them; 2.4 wires the check commands. CI is owned by TASK-13 (template repo) and TASK-27 (generated projects); the done rule by TASK-15.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 All Phase 1 subtasks (2.1 to 2.5, 2.7 and 2.8) Done; TASK-2.6 is later work and does not block v0.1.0
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
2026-10-02: ready label removed: description and criterion changed after the challenge (record 0041, ready.md); plan and challenge again before unattended work, or the owner waives it.

2026-10-03: TASK-2.5 split into 2.5 (detection and packs), 2.7 (post-copy tasks) and 2.8 (Express skeleton).
<!-- SECTION:NOTES:END -->

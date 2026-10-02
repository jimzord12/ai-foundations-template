---
id: TASK-2.6
title: >-
  Stack packs beyond v0.1.0: Astro, SvelteKit, SolidStart, Expo, Hono, Fastify,
  Nest.js, Elysia
status: To Do
assignee: []
created_date: '2026-10-02 16:07'
updated_date: '2026-10-02 17:05'
labels:
  - stack
  - packs
dependencies:
  - TASK-2.4
parent_task_id: TASK-2
priority: medium
type: feature
ordinal: 24000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner 2026-10-02: the template targets any modern TypeScript project in an app ecosystem, not three stacks. Record 0041 makes that a generic core plus a pack per framework, with the framework detected in the stack question's default. Spikes showed the foundations tsconfig works on real Next.js, Astro and SvelteKit scaffolds; detection was checked on hand-written package.json files only. Phase 1 (v0.1.0) ships packs for Next.js, bare React Native and Express only; this task adds the rest once the mechanism and the check contract are proven there. It is not part of Phase 1 and does not block the v0.1.0 tag; when it is scheduled is the owner's call.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A pack exists and is detected for each of Astro, SvelteKit, SolidStart, Expo, Hono, Fastify, Nest.js and Elysia (or the owner names a subset; the owner wrote "Solid", so confirm whether plain Solid with Vite is meant too); the precedence list in copier.yml is updated and the check from TASK-2.5 passes
- [ ] #2 Each pack is verified on a project freshly scaffolded with that framework's own tool: copy picks the pack, and npm run check passes (typecheck through the foundations config, lint, format:check, test)
- [ ] #3 Expo is its own pack; the "No Expo packages" rule stays in the bare React Native pack, and any change to the Expo-before-React-Native precedence of record 0041 is recorded in docs/decisions/
- [ ] #4 Where tsc does not cover the framework's files (Astro, SvelteKit), the pack names the framework's own checker and check runs it, or a decision records why not
- [ ] #5 Each pack's tool choices and verified versions are recorded in docs/decisions/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

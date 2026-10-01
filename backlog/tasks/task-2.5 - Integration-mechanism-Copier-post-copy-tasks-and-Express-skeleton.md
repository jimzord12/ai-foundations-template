---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
labels:
  - stack
  - copier
milestone: m-0
dependencies: []
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Next.js and React Native projects are scaffolded first, and their scaffolders already write package.json, tsconfig.json and lint configs, so the template cannot just copy files over them. Owner decision 2026-10-01 (Phase 1 readiness answers): Copier post-copy tasks add scripts and dev dependencies with npm pkg set / npm i -D; shipped config files extend the framework's own configs and overwrite them on purpose, documented in the README; Express has no scaffolder, so the template ships a minimal skeleton. Every other TASK-2 subtask builds on this mechanism.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Copier _tasks run per stack after copy and add scripts and dev dependencies without a merge prompt; README documents the overwrite-on-purpose files
- [ ] #2 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) and runs with npm install then the start script
- [ ] #3 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template) and the Express skeleton: copy finishes non-interactively with --defaults
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

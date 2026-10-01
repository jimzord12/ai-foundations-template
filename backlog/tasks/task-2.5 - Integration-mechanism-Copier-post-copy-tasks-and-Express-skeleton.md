---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-01 20:20'
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
- [ ] #4 Post-copy tasks run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; decision recorded
- [ ] #5 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

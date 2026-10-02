---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 03:01'
labels:
  - stack
  - copier
  - ready
milestone: m-0
dependencies: []
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Next.js and React Native projects are scaffolded first, and their scaffolders already write package.json, tsconfig.json and lint configs, so the template cannot just copy files over them. Owner decision 2026-10-01 (Phase 1 readiness answers), refined 2026-10-02 by record 0036: Copier post-copy tasks add scripts and dev dependencies with npm pkg set / npm i -D; config files are never overwritten, the template ships a new file that extends the project's own (for TypeScript, tsconfig.foundations.json); only instruction and documentation files may overwrite scaffolded ones; Express has no scaffolder, so the template ships a minimal skeleton. Every other TASK-2 subtask builds on this mechanism.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Copier _tasks run per stack after copy and add scripts and dev dependencies without a merge prompt; README documents which files are overwritten (instruction and documentation files only) and which config files are extended instead of overwritten (record 0036)
- [ ] #2 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) and runs with npm install then the start script
- [ ] #3 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template) and the Express skeleton: copy finishes non-interactively with --defaults
- [ ] #4 Post-copy tasks run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; decision recorded
- [ ] #5 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project
- [ ] #6 Scripts and dependencies 2.5 itself adds are named: Express skeleton start and dev scripts plus a TypeScript runner; Next.js and RN get none from 2.5 (their scripts come from 2.1-2.4). The decision for the copy-only guard states the consequence: later script or dependency changes reach existing projects only through a documented manual step
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

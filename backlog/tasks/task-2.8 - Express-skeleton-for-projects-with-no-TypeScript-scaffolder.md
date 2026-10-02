---
id: TASK-2.8
title: Express skeleton for projects with no TypeScript scaffolder
status: To Do
assignee: []
created_date: '2026-10-02 21:29'
updated_date: '2026-10-02 21:33'
labels:
  - stack
  - copier
milestone: m-0
dependencies:
  - TASK-2.5
  - TASK-2.7
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1020
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Express has no TypeScript scaffolder, so for an empty folder the template ships a minimal skeleton (owner answer 2026-10-01; record 0004's conditional-file mechanism, kept for this case only). The skeleton must never land on an existing Express project, which is why it hangs on its own stored question instead of on stack. Split from TASK-2.5 on 2026-10-03; review rounds 2 to 5 and 7 in TASK-2.5's notes cover the skeleton.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) under conditional file and folder names on a stored skeleton question that is true only for a framework with no TypeScript scaffolder and no package.json at the first copy; copying over an existing Express project, even with --overwrite, does not overwrite its own package.json, src or .gitignore with the skeleton's files (post-copy tasks may still add scripts and ignore lines), and no empty src folder appears for other packs
- [ ] #2 The skeleton question's default tests stack before it reads package.json, so for a package.json that is not valid YAML (for example tab-indented) -d stack=<name> alone avoids the abort for a framework with a scaffolder, and an existing Express project needs -d skeleton=false as well; the README documents both and a test reproduces both cases
- [ ] #3 Skeleton start and dev scripts plus a TypeScript runner live in the skeleton's own package.json template or in a task conditioned on skeleton, never on stack alone (that would overwrite the scripts of an existing Express app)
- [ ] #4 Verified on an empty folder copied with --defaults -d stack=express (the skeleton renders, and npm install then the start script serves GET /health) and on an existing Express project copied with --defaults --overwrite (its package.json, src and .gitignore keep their content); the stored skeleton answer holds across copier update
- [ ] #5 The conditional-file-name sentence in root AGENTS.md 'Where things go' is kept for the Express skeleton but rewritten so its example uses the skeleton question ({% if skeleton %}), not stack
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Independent review loop reached PASS for non-trivial changes
- [ ] #3 Non-trivial decisions recorded in docs/decisions/
- [ ] #4 Committed and pushed
- [ ] #5 Smoke test passes for every smoke run in root AGENTS.md (the three stacks plus the generic run TASK-2.5 adds) when template/ or copier.yml changed
<!-- DOD:END -->

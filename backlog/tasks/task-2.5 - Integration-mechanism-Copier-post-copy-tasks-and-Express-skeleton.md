---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 16:07'
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
Next.js, React Native and other framework projects are scaffolded first with the framework's own tool, and their scaffolders already write package.json, tsconfig.json and lint configs, so the template cannot just copy files over them. Owner decisions: 2026-10-01 (Phase 1 readiness answers), refined 2026-10-02 by record 0036 (config files are extended, never overwritten) and record 0040 (the template is stack-agnostic: a generic core plus a pack per framework, the pack picked by a post-copy task that reads package.json). Copier post-copy tasks detect the framework, copy its pack to docs/stack.md and add scripts and dev dependencies with npm pkg set / npm i -D; only instruction and documentation files may overwrite scaffolded ones; Express has no TypeScript scaffolder, so the template ships a minimal skeleton. Every other TASK-2 subtask builds on this mechanism.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Copier _tasks run after copy and add scripts and dev dependencies without a merge prompt; README documents which files are overwritten (instruction and documentation files only) and which config files are extended instead of overwritten (record 0036)
- [ ] #2 Detection and packs per record 0040: a post-copy task reads package.json and picks the pack by a fixed precedence list (Expo before React Native, and so on); the stack answer defaults to auto and any other value names a pack and skips detection; no match, no package.json or an unknown value gives the generic pack without failing; several matches take the first and print a warning
- [ ] #3 Packs ship for Next.js, bare React Native, Express and the generic fallback (the stack blocks of template/AGENTS.md.jinja move into them); each pack names its prepare step before typecheck, how it meets lint, format:check and test, and the framework's own checker where tsc does not cover its files; AGENTS.md links the project's pack and stays within the line budget of the phase plan
- [ ] #4 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) and runs with npm install then the start script
- [ ] #5 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template) and the Express skeleton: copy finishes non-interactively with --defaults and picks the right pack
- [ ] #6 Post-copy tasks run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; decision recorded, including how a changed pack reaches an existing project (record 0040 notes the pack file is not tracked by Copier)
- [ ] #7 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project; root AGENTS.md "Where things go" describes packs instead of inline stack blocks
- [ ] #8 Scripts and dependencies 2.5 itself adds are named: Express skeleton start and dev scripts plus a TypeScript runner; Next.js and RN get none from 2.5 (their scripts come from 2.1-2.4). The decision for the copy-only guard states the consequence: later script or dependency changes reach existing projects only through a documented manual step
- [ ] #9 Adding a framework is documented (a pack file and one detection line) and a check fails when the detector can return a pack that does not exist
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
2026-10-02: ready label removed: criterion 1 changed after the challenge (record 0036, ready.md); plan and challenge again before unattended work, or the owner waives it.

2026-10-02: scope widened by record 0040 (stack-agnostic core with packs picked by detection; spike evidence there). Criteria 2, 3, 5 and 9 are new or reworded; the old criteria 2 to 6 are now 4 to 8. Phase 1 packs: Next.js, bare React Native, Express; further frameworks are TASK-2.6. The spike found that a pack must declare a prepare step before typecheck and that typescript can be missing from a scaffold; both are inputs to 2.1.
<!-- SECTION:NOTES:END -->

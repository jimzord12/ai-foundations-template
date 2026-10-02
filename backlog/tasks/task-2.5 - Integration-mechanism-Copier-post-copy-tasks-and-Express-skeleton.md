---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 16:18'
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
Next.js, React Native and other framework projects are scaffolded first with the framework's own tool, and their scaffolders already write package.json, tsconfig.json and lint configs, so the template cannot just copy files over them. Owner decisions: 2026-10-01 (Phase 1 readiness answers), refined 2026-10-02 by record 0036 (config files are extended, never overwritten) and record 0040 (the template is stack-agnostic: a generic core plus a pack per framework; the stack question's default detects the framework from package.json and Copier renders the pack into docs/stack.md). Copier post-copy tasks add scripts and dev dependencies with npm pkg set / npm i -D; only instruction and documentation files may overwrite scaffolded ones; Express has no TypeScript scaffolder, so the template ships a minimal skeleton. Every other TASK-2 subtask builds on this mechanism.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Copier _tasks run after copy and add scripts and dev dependencies without a merge prompt; README documents which files are overwritten (instruction and documentation files only) and which config files are extended instead of overwritten (record 0036)
- [ ] #2 Detection per record 0040: the stack question loses its choices and its default is computed in copier.yml from package.json through _external_data, with a fixed precedence list (Expo before React Native, Next.js before Express, and so on); no match or no package.json gives generic; the answer is stored; -d stack=<name> overrides it; a name with no pack file renders the generic pack; the pack names express, next and rn stay valid
- [ ] #3 Packs live in packs/ at the template root, outside template/: one file per framework plus generic, rendered into docs/stack.md by template/docs/stack.md.jinja so Copier tracks it; Phase 1 ships next, rn, express and generic (the stack blocks of template/AGENTS.md.jinja move into them); each pack names its prepare step before typecheck, how it meets lint, format:check and test, and the framework's own checker where tsc does not cover its files; AGENTS.md names the stack, points at docs/stack.md and stays within the line budget of the phase plan; the Next.js rule about the nextjs-agent-rules block says AGENTS.md
- [ ] #4 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) and runs with npm install then the start script
- [ ] #5 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template) and the Express skeleton: copy finishes non-interactively with --defaults and picks the right pack
- [ ] #6 Post-copy tasks (scripts and dev dependencies only) run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; decision recorded; a changed pack reaches existing projects through copier update (checked)
- [ ] #7 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project; root AGENTS.md "Where things go" and the README intro and layout row describe packs instead of inline stack blocks
- [ ] #8 Scripts and dependencies 2.5 itself adds are named: Express skeleton start and dev scripts plus a TypeScript runner; Next.js and RN get none from 2.5 (their scripts come from 2.1-2.4). The decision for the copy-only guard states the consequence: later script or dependency changes reach existing projects only through a documented manual step
- [ ] #9 Adding a framework is documented (a pack file and one precedence line) and a check fails when the precedence list names a pack that has no file
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

2026-10-02: scope widened by record 0040 (stack-agnostic core with packs picked by detection; spike evidence there). Criteria 2, 3 and 9 are new; 1, 5, 6 and 7 are reworded; the old criteria 2 to 6 are now 4 to 8. Detection runs in the stack question default and Copier renders the pack, so copier update refreshes it and no detection script is needed. Phase 1 packs: Next.js, bare React Native, Express; further frameworks are TASK-2.6. The spikes found that a pack must declare a prepare step before typecheck and that typescript can be missing from a scaffold; both are inputs to 2.1.
<!-- SECTION:NOTES:END -->

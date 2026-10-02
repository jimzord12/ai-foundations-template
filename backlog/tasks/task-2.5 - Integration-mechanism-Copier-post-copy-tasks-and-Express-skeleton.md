---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 16:37'
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
- [ ] #1 Copier _tasks run after copy and add scripts and dev dependencies without a merge prompt; README documents which files are overwritten (instruction and documentation files only) and which config files are extended instead of overwritten (record 0036); where per-pack scripts and dev dependencies live (tasks in copier.yml conditioned on stack, or data in the pack) is decided and recorded
- [ ] #2 Detection per record 0040: the stack question loses its choices and its default is computed in copier.yml from package.json through _external_data, with a fixed precedence list (Expo before React Native, Next.js before Express, and so on); no match or no package.json gives generic; the answer is stored; -d stack=<name> overrides it; a name with no pack file renders the generic pack, so Expo is listed in Phase 1 without an Expo pack and an Expo project does not get the bare React Native pack; the pack names express, next and rn stay valid; a package.json that is not valid YAML (for example tab-indented) aborts the first copy, so the README documents the workaround (-d stack=<name>, plus -d skeleton=false for an existing Express project, because the skeleton default reads package.json too) and a test reproduces both cases
- [ ] #3 Packs live in packs/ at the template root, outside template/: one file per framework plus generic, rendered into docs/stack.md by template/docs/stack.md.jinja so Copier tracks it; Phase 1 ships next, rn, express and generic (the stack blocks of template/AGENTS.md.jinja move into them); each pack names its prepare step before typecheck, how it meets lint, format:check and test, and the framework's own checker where tsc does not cover its files; AGENTS.md names the stack, points at docs/stack.md and stays within the line budget of the phase plan; the Next.js rule about the nextjs-agent-rules block says AGENTS.md
- [ ] #4 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) under conditional file and folder names on a stored skeleton question (0004's mechanism, kept for this case only) that is true only for a framework with no scaffolder and no package.json at the first copy; it runs with npm install then the start script; copying over an existing Express project, even with --overwrite, leaves its own package.json, src and .gitignore untouched, and no empty src folder appears for other packs
- [ ] #5 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template), an existing Express project and the Express skeleton (an empty folder copied with -d stack=express): copy finishes non-interactively with --defaults and picks the right pack; detection is also run on the package.json of each real scaffold
- [ ] #6 Post-copy tasks (scripts and dev dependencies only) run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; decision recorded; a changed pack reaches existing projects through copier update, and the stored stack and skeleton answers hold (checked)
- [ ] #7 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project; root AGENTS.md "Where things go" and the README intro and layout row describe packs instead of inline stack blocks, and the conditional-file-name sentence is kept for the Express skeleton but rewritten so its example uses the skeleton question ({% if skeleton %}), not stack
- [ ] #8 Scripts and dependencies 2.5 itself adds are named: Express skeleton start and dev scripts plus a TypeScript runner, which live in the skeleton's own package.json template or in a task conditioned on skeleton, never on stack alone (that would overwrite the scripts of an existing Express app); Next.js and RN get none from 2.5 (their scripts come from 2.1-2.4). The decision for the copy-only guard states the consequence: later script or dependency changes reach existing projects only through a documented manual step
- [ ] #9 Adding a framework is documented (a pack file, a precedence line, and the framework's scripts and dev dependencies; packs are Jinja templates, so code samples are wrapped in raw tags) and a check fails when a pack file other than generic.md is not named by the precedence list (a typo); a list name with no pack file is allowed and renders the generic pack
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

2026-10-02 review round 2: the Express skeleton starts from an empty folder, so it is chosen with -d stack=express and its files keep conditional names on stack (criteria 4, 5, 7); a tab-indented package.json aborts the first copy (criterion 2); packs are Jinja templates (criterion 9).

2026-10-02 review round 3: the skeleton is conditioned on a stored skeleton question so an existing Express project is never overwritten (criteria 4, 5, 6); a name without a pack renders generic, so the check in criterion 9 only requires every pack file to be named by the list (criterion 2); per-pack scripts and dependencies need a home that 0040 leaves to this task (criterion 1).

2026-10-02 review round 4: the tab-indent workaround for an existing Express project needs -d skeleton=false as well (criterion 2); the skeleton question is the condition for the skeleton files, their scripts and the AGENTS.md example (criteria 7 and 8); generic.md is exempt from the named-in-the-list check (criterion 9).
<!-- SECTION:NOTES:END -->

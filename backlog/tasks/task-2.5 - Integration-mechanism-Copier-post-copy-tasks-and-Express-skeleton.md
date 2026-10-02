---
id: TASK-2.5
title: 'Integration mechanism: Copier post-copy tasks and Express skeleton'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 18:27'
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
Next.js, React Native and other framework projects are scaffolded first with the framework's own tool, and their scaffolders already write package.json, tsconfig.json and lint configs, so the template cannot just copy files over them. Owner decisions: 2026-10-01 (Phase 1 readiness answers), refined 2026-10-02 by record 0036 (config files are extended, never overwritten) and record 0041 (the template is stack-agnostic: a generic core plus a pack per framework; the stack question's default detects the framework from package.json and Copier renders the pack into docs/stack.md). Copier post-copy tasks add scripts and dev dependencies with npm pkg set / npm i -D; only instruction and documentation files may overwrite scaffolded ones; Express has no TypeScript scaffolder, so the template ships a minimal skeleton. Every other TASK-2 subtask builds on this mechanism.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Copier _tasks run after copy and add scripts, dev dependencies and appended ignore-file lines (TASK-23 adds .env) without a merge prompt, and nothing else in the project's own files; the generic pack defines no scripts, so a project on it (no package.json, or a framework with no pack yet such as Expo in Phase 1) gets none and the check fallback of done.md applies; README documents which files are overwritten (instruction and documentation files only) and which config files are extended instead of overwritten (record 0036); where per-pack scripts and dev dependencies live (tasks in copier.yml conditioned on stack, or data in the pack) and where per-pack config files live (rendered by Copier, never written by a task: conditional file names on stack that never match a scaffold's own files, or files from a pack folder) are decided and recorded
- [ ] #2 Detection per record 0041: the stack question loses its choices and its default is computed in copier.yml from package.json through _external_data, with a fixed precedence list (Expo before React Native, Next.js before Express, and so on) searched in dependencies and devDependencies; no match or no package.json gives generic; the answer is stored; -d stack=<name> overrides it; a name with no pack file renders the generic pack, so Expo is listed in Phase 1 without an Expo pack and an Expo project does not get the bare React Native pack; the pack names express, next and rn stay valid; a package.json that is not valid YAML (for example tab-indented) aborts the first copy: the skeleton default tests stack before it reads package.json, so -d stack=<name> (any name, generic included) alone avoids the abort for a framework with a scaffolder, and an existing Express project needs -d skeleton=false as well; the README documents both and a test reproduces both cases
- [ ] #3 Packs live in packs/ at the template root, outside template/: one file per framework plus generic, rendered into docs/stack.md by template/docs/stack.md.jinja so Copier tracks it; every pack has a slot for each part of the contract (prepare step before typecheck, lint, format:check, test, and the framework's own checker where tsc does not cover its files); 2.5 fills the prepare step (Next.js next typegen; none for rn and express) and the generic pack's text (no tools chosen, no scripts, points at docs/protocols/done.md), and 2.1 to 2.3 fill the rest; Phase 1 ships next, rn, express and generic (the stack blocks of template/AGENTS.md.jinja move into them); AGENTS.md names the stack, points at docs/stack.md, has a row in the When to read what table and stays within the line budget of the phase plan; the Next.js rule about the nextjs-agent-rules block says AGENTS.md
- [ ] #4 Express skeleton ships (package.json, src/app.ts with a GET /health route, .gitignore including .env) under conditional file and folder names on a stored skeleton question (0004's mechanism, kept for this case only) that is true only for a framework with no TypeScript scaffolder and no package.json at the first copy; it runs with npm install then the start script; copying over an existing Express project, even with --overwrite, does not overwrite its own package.json, src or .gitignore with the skeleton's files (post-copy tasks may still add scripts and ignore lines), and no empty src folder appears for other packs
- [ ] #5 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template), an existing Express project (once without contract scripts and once already carrying its own test and lint scripts and a typescript version, which must survive) and the Express skeleton (an empty folder copied with -d stack=express): copy finishes non-interactively with --defaults --overwrite over the scaffolds and the existing Express project (a scaffold's own AGENTS.md would otherwise stop the copy at a conflict) and with --defaults for the skeleton, and picks the right pack; detection is also run on the package.json of each real scaffold
- [ ] #6 Post-copy tasks (scripts, dev dependencies and appended ignore-file lines only) run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; a task sets a contract script (typecheck, lint, format:check, test, check) only when the project has no script of that name, and installs a dev dependency only when the project does not list it, and keeps and reports an existing one unless the decision records a reason to overwrite it (Next.js ships lint, RN ships lint and test); the decision lists every write a task makes (file, key, behaviour when it already exists); a changed pack reaches existing projects through copier update, and the stored stack and skeleton answers hold (checked)
- [ ] #7 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project; root AGENTS.md "Where things go" and the README intro, "Use it" comment and layout row describe packs instead of inline stack blocks (the README also says the MissingFileWarning for a folder without package.json is expected), and the conditional-file-name sentence is kept for the Express skeleton but rewritten so its example uses the skeleton question ({% if skeleton %}), not stack
- [ ] #8 Scripts and dependencies 2.5 itself adds are named: Express skeleton start and dev scripts plus a TypeScript runner, which live in the skeleton's own package.json template or in a task conditioned on skeleton, never on stack alone (that would overwrite the scripts of an existing Express app); Next.js and RN get none from 2.5 (their scripts come from 2.1-2.4). The decision for the copy-only guard states the consequence: later script or dependency changes reach existing projects only through a documented manual step
- [ ] #9 Adding a framework is documented (a pack file, a precedence line, the framework's scripts and dev dependencies, and any config files it needs, rendered by Copier and never written by a task; packs are Jinja templates, so code samples are wrapped in raw tags) and a check fails when a pack file other than generic.md is not named by the precedence list (a typo); a list name with no pack file is allowed and renders the generic pack
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

2026-10-02: scope widened by record 0041 (stack-agnostic core with packs picked by detection; spike evidence there). Criteria 2, 3 and 9 are new; 1, 5, 6 and 7 are reworded; the old criteria 2 to 6 are now 4 to 8. Detection runs in the stack question default and Copier renders the pack, so copier update refreshes it and no detection script is needed. Phase 1 packs: Next.js, bare React Native, Express; further frameworks are TASK-2.6. The spikes found that a pack must declare a prepare step before typecheck and that typescript can be missing from a scaffold; both are inputs to 2.1.

2026-10-02 review round 2: the Express skeleton starts from an empty folder, so it is chosen with -d stack=express and its files keep conditional names on stack (criteria 4, 5, 7); a tab-indented package.json aborts the first copy (criterion 2); packs are Jinja templates (criterion 9).

2026-10-02 review round 3: the skeleton is conditioned on a stored skeleton question so an existing Express project is never overwritten (criteria 4, 5, 6); a name without a pack renders generic, so the check in criterion 9 only requires every pack file to be named by the list (criterion 2); per-pack scripts and dependencies need a home that 0041 leaves to this task (criterion 1).

2026-10-02 review round 4: the tab-indent workaround for an existing Express project needs -d skeleton=false as well (criterion 2); the skeleton question is the condition for the skeleton files, their scripts and the AGENTS.md example (criteria 7 and 8); generic.md is exempt from the named-in-the-list check (criterion 9).

2026-10-02 review round 5: the skeleton default must test stack before it reads package.json (criterion 2); packs have a slot per contract part that 2.5 fills only for the prepare step and the generic text, 2.1 to 2.3 fill the rest (criterion 3); the When to read what row and the README Use it comment are named (criteria 3 and 7).

2026-10-02 review round 6: post-copy tasks may also append ignore-file lines, which TASK-23 needs (criteria 1 and 6); scaffolded projects are copied with --defaults --overwrite (criterion 5); a generic project gets no scripts (criterion 1).

2026-10-02 review round 7: the generic pack defines no scripts, so pack-less projects get none (criteria 1 and 3); per-pack config files are part of the open point in criterion 1 and of criterion 9; detection searches devDependencies (criterion 2); the skeleton does not overwrite existing files but post-copy tasks may still edit them (criterion 4).

2026-10-02 review round 9: a task sets a contract script only when the project has no script of that name, because npm pkg set replaces an existing key (criterion 6); the verification adds an existing Express project that already has test and lint scripts (criterion 5).
<!-- SECTION:NOTES:END -->

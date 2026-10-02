---
id: TASK-2.5
title: 'Stack detection and packs: generic core plus a pack per framework'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 21:29'
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
Record 0041 makes the template stack-agnostic: a generic core plus a pack per framework. The stack question's default detects the framework from package.json and Copier renders the pack into docs/stack.md, so copier update refreshes it and no detection script is needed. Owner decisions: 2026-10-01 (Phase 1 readiness answers), refined 2026-10-02 by record 0036 (config files are extended, never overwritten) and record 0041. On 2026-10-03 this task was split in three because it carried nine criteria after eleven review rounds: this one keeps detection and packs, TASK-2.7 has the post-copy tasks and TASK-2.8 the Express skeleton. Every other TASK-2 subtask builds on it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Detection per record 0041: the stack question loses its choices and its default is computed in copier.yml from package.json through _external_data, with a fixed precedence list (Expo before React Native, Next.js before Express, and so on) searched in dependencies and devDependencies; no match or no package.json gives generic; the answer is stored; -d stack=<name> overrides it; a name with no pack file renders the generic pack, so Expo is listed in Phase 1 without an Expo pack and an Expo project does not get the bare React Native pack; the pack names express, next and rn stay valid; a package.json that is not valid YAML (for example tab-indented) aborts the first copy unless -d stack=<name> is given (the skeleton side of this case is TASK-2.8); the README documents it and a test reproduces it
- [ ] #2 Packs live in packs/ at the template root, outside template/: one file per framework plus generic, rendered into docs/stack.md by template/docs/stack.md.jinja so Copier tracks it; every pack has a slot for each part of the contract (prepare step before typecheck, lint, format:check, test, and the framework's own checker where tsc does not cover its files); 2.5 fills the prepare step (Next.js next typegen; none for rn and express) and the generic pack's text (no tools chosen, no scripts, points at docs/protocols/done.md), and 2.1 to 2.3 fill the rest; Phase 1 ships next, rn, express and generic (the stack blocks of template/AGENTS.md.jinja move into them); AGENTS.md names the stack, points at docs/stack.md, has a row in the When to read what table and stays within the line budget of the phase plan; the Next.js rule about the nextjs-agent-rules block says AGENTS.md
- [ ] #3 Adding a framework is documented (a pack file, a precedence line, the framework's scripts and dev dependencies, and any config files it needs, rendered by Copier and never written by a task; packs are Jinja templates, so code samples are wrapped in raw tags) and a check fails when a pack file other than generic.md is not named by the precedence list (a typo); a list name with no pack file is allowed and renders the generic pack
- [ ] #4 Detection is run on the package.json of each real Phase 1 scaffold (create-next-app, the current stable RN community template, an existing Express project) and on a folder with no package.json, and picks next, rn, express and generic; the smoke test in root AGENTS.md and the backlog Definition of Done gain a fourth run into an empty folder without -d stack, which renders the generic pack
- [ ] #5 Root AGENTS.md 'Where things go' and the README intro, 'Use it' comment and layout row describe packs instead of inline stack blocks (the conditional-file-name sentence stays until TASK-2.8 rewrites it); the README says the MissingFileWarning for a folder without package.json is expected
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

2026-10-02 review round 11: the generic pack also defines no dev dependencies (criterion 1; record 0041). When a task needs to know whether a script already exists (criterion 6), read it from the shell (npm pkg get scripts.<name>), not through _external_data: that reads package.json as YAML and aborts on a tab-indented file at task time, even with -d stack=<name>, and a test run with --skip-tasks would not show it, so run the criterion 2 test with tasks enabled.

2026-10-03 split (owner review of the backlog): old criteria 2, 3 and 9 are now 1, 2 and 3; the detection part of old 5 is 4, with the generic smoke run added; the packs part of old 7 is 5. Old 1, 6 and 8 and the post-copy parts of 5 and 7 moved to TASK-2.7 (old 1 is 2.7 criterion 1, old 6 is 2.7 criterion 2). Old 4 and the skeleton parts of 2, 5, 7 and 8 moved to TASK-2.8. The review-round notes above use the old numbers.
<!-- SECTION:NOTES:END -->

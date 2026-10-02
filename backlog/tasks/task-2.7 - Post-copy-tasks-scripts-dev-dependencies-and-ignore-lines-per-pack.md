---
id: TASK-2.7
title: 'Post-copy tasks: scripts, dev dependencies and ignore lines per pack'
status: To Do
assignee: []
created_date: '2026-10-02 21:29'
updated_date: '2026-10-02 21:34'
labels:
  - stack
  - copier
milestone: m-0
dependencies:
  - TASK-2.5
  - TASK-40
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1010
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Next.js, React Native and other framework scaffolders already write package.json, tsconfig.json and lint configs, so the template cannot copy files over them (records 0036 and 0041). Copier post-copy tasks add scripts and dev dependencies (npm pkg set, npm i -D) and append ignore-file lines, and touch nothing else in the project's own files. TASK-2.1 to 2.4 add their scripts through this mechanism. Split from TASK-2.5 on 2026-10-03 (that task carried nine criteria after eleven review rounds); records 0036 and 0041 name TASK-2.5 for the open points that now live here.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Copier _tasks run after copy and add scripts, dev dependencies and appended ignore-file lines (TASK-23 adds .env) without a merge prompt, and nothing else in the project's own files; the generic pack defines no scripts and no dev dependencies, so a project on it (no package.json, or a framework with no pack yet such as Expo in Phase 1) gets none and the check fallback of done.md applies; README documents which files are overwritten (instruction and documentation files only), which config files are extended instead of overwritten (record 0036) and which ship only when missing (_skip_if_exists, rule recorded by TASK-40); where per-pack scripts and dev dependencies live (tasks in copier.yml conditioned on stack, or data in the pack) and where per-pack config files live (rendered by Copier, never written by a task: conditional file names on stack that never match a scaffold's own files, or files from a pack folder) are decided and recorded
- [ ] #2 Post-copy tasks (scripts, dev dependencies and appended ignore-file lines only) run only on copy (guarded with _copier_operation or equivalent, verified in the installed Copier version) or are idempotent, so copier update never overwrites the user's scripts; a task sets a contract script (typecheck, lint, format:check, test, check) only when the project has no script of that name, and installs a dev dependency only when the project does not list it, and keeps and reports an existing one unless the decision records a reason to overwrite it (Next.js ships lint, RN ships lint and test); the tasks assume npm, so a project with another package manager's lock file (pnpm-lock.yaml, yarn.lock, bun.lock, bun.lockb) gets no task writes and a report; the decision lists every write a task makes (file, key, behaviour when it already exists); a changed pack reaches existing projects through copier update, and the stored stack answer holds (checked)
- [ ] #3 2.7 itself adds no scripts or dependencies for Next.js, RN or an existing Express project (their scripts come from 2.1-2.4; the skeleton's own are TASK-2.8). The decision for the copy-only guard states the consequence: later script or dependency changes reach existing projects only through a documented manual step
- [ ] #4 Verified on a freshly scaffolded Next.js project, a freshly scaffolded RN project (current stable template) and an existing Express project (once without contract scripts and once already carrying its own test and lint scripts and a typescript version, which must survive): copy finishes non-interactively with --defaults --overwrite (a scaffold's own AGENTS.md would otherwise stop the copy at a conflict), the tasks write only what the decision lists, and a project with a pnpm, Yarn or Bun lock file gets no writes and a report; a tab-indented package.json copied with -d stack=<name> completes with tasks enabled (tasks read scripts through npm pkg get, not _external_data)
- [ ] #5 Root AGENTS.md smoke-test command and the backlog Definition of Done updated so the smoke test still renders into an empty folder (for example with --skip-tasks), plus a separate documented check that runs the tasks on a scaffolded project
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Independent review loop reached PASS for non-trivial changes
- [ ] #3 Non-trivial decisions recorded in docs/decisions/
- [ ] #4 Committed and pushed
- [ ] #5 Smoke test passes for every smoke run in root AGENTS.md (the three stacks plus the generic run TASK-2.5 adds) when template/ or copier.yml changed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-03: review-round notes from before the split stay in TASK-2.5; rounds 6, 9 and 11 are about post-copy tasks and apply here. In particular (round 11): when a task needs to know whether a script already exists, read it from the shell (npm pkg get scripts.<name>), not through _external_data, which reads package.json as YAML and aborts on a tab-indented file at task time even with -d stack=<name>; a test run with --skip-tasks would not show it, so run that test with tasks enabled.
<!-- SECTION:NOTES:END -->

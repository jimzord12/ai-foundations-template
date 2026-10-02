---
id: TASK-2.1
title: 'Strict TypeScript per stack: tsconfig and ts-reset'
status: To Do
assignee: []
created_date: '2026-10-01 19:51'
updated_date: '2026-10-02 16:52'
labels:
  - stack
  - typescript
milestone: m-0
dependencies:
  - TASK-2.5
parent_task_id: TASK-2
priority: high
type: feature
ordinal: 1100
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents write more consistent code under a strict compiler. Ship one tsconfig.foundations.json that extends the project's own tsconfig.json (a standard strict base such as @tsconfig/strictest can supply the flags; record 0036) and @total-typescript/ts-reset. Verify current versions and framework compatibility first.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The template ships one tsconfig.foundations.json that extends the project's own tsconfig.json with the strict flags and never overwrites it (record 0036); 2.1 also adds a tsconfig.json and the typescript dev dependency to the Express skeleton (which has no TypeScript scaffolder; its package.json is a template file shipped by 2.5), under the same skeleton condition as the other skeleton files, from a standard strict base, for the foundations file to extend
- [ ] #2 ts-reset installed (via the post-copy task) and wired per pack
- [ ] #3 npm run typecheck (tsc -p tsconfig.foundations.json --noEmit) passes on a freshly scaffolded project for each Phase 1 pack (Next.js, RN, Express skeleton) and each framework's own build is unaffected; the script runs the pack's prepare step first (for example next typegen) and the post-copy task ensures typescript is a dev dependency (record 0040); the open checks listed in record 0036 (editor-only plugins through extends) are verified
- [ ] #4 Choices and versions recorded in docs/decisions/
- [ ] #5 2.1 adds the typecheck script (the pack's prepare step, then tsc -p tsconfig.foundations.json --noEmit) through the post-copy task
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
2026-10-02: acceptance criteria 1, 3 and 5 amended by record 0036 (config files are extended, not overwritten).

2026-10-02: option to weigh and verify: Next.js has a typescript.tsconfigPath setting in next.config; pointing it at tsconfig.foundations.json would make next build enforce the strict flags too.

2026-10-02: ready label removed: criteria changed after the challenge (ready.md); plan and challenge again before unattended work, or the owner waives it. When trying tsconfigPath, check whether next build writes include or plugins into tsconfig.foundations.json.

2026-10-02: record 0040: the foundations file worked on real Next.js, Astro and SvelteKit scaffolds in a spike (Expo and the other frameworks are not checked; see 0036 and 0040). What differs per framework is the prepare step before tsc and whether typescript is installed; both belong in the pack. Frameworks beyond Phase 1 are TASK-2.6.
<!-- SECTION:NOTES:END -->

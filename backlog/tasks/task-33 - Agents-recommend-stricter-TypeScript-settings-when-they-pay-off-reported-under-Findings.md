---
id: TASK-33
title: >-
  Agents recommend stricter TypeScript settings when they pay off, reported
  under Findings
status: To Do
assignee: []
created_date: '2026-10-01 23:05'
updated_date: '2026-10-02 03:05'
labels:
  - agents
  - typescript
  - reporting
milestone: m-0
dependencies:
  - TASK-15
  - TASK-2.1
  - TASK-32
priority: medium
ordinal: 1560
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner request 2026-10-02. Every generated project is TypeScript. TASK-2.1 ships a strict baseline in tsconfig.foundations.json (record 0036), which is also where a stricter flag goes, but projects evolve: a codebase that has grown may be ready for a stricter flag it could not afford on day one, or a flag may cause more noise than value. Agents are therefore recommended to look for tsconfig settings that catch real bugs for this codebase and propose or apply them, without overdoing it: a flag earns its place only if the errors it raises are mostly real problems and fixing them is cheap. The owner wants to see these: the end-of-task report lists them in a 'TypeScript settings' subsection of its Findings section, next to the 'Lint and CI rules' subsection from TASK-32. The report shape comes from TASK-15 (docs/protocols/done.md).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Guidance extends the existing docs/protocols/typescript.md (and its row in the AGENTS.md router; AGENTS.md grows at most 1 line): look for stricter settings only when triggered (a bug or review finding in a class a flag catches, a tsconfig or TypeScript version change, or the owner asks), never on every task
- [ ] #2 Before applying a flag, run the type check with it and count new errors; apply it in its own commit only when the count is small (about 10 or fewer) and the fixes are mechanical; otherwise propose it with the count. Relaxing a baseline flag that is mostly noise is also proposed, and needs a decision record. Shipped text says 'the shipped baseline', never a task ID
- [ ] #3 The candidate list is measured against the baseline TASK-2.1 actually ships and may be short; type-aware lint rules (for example no-floating-promises, switch-exhaustiveness-check) are routed to the 'Lint and CI rules' subsection instead
- [ ] #4 done.md's Findings section gains a 'TypeScript settings' subsection listing flags applied (with error count fixed) and proposed (with count and why), folding into one line when empty
- [ ] #5 Smoke test passes for all three stacks; rendered AGENTS.md stays within the line budget; decision recorded in docs/decisions/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

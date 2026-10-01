---
id: TASK-33
title: >-
  Agents recommend stricter TypeScript settings when they pay off, reported
  under Findings
status: To Do
assignee: []
created_date: '2026-10-01 23:05'
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
ordinal: 25000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner request 2026-10-02. Every generated project is TypeScript. TASK-2.1 ships a strict baseline tsconfig per stack, but projects evolve: a codebase that has grown may be ready for a stricter flag it could not afford on day one, or a flag may cause more noise than value. Agents are therefore recommended to look for tsconfig settings that catch real bugs for this codebase and propose or apply them, without overdoing it: a flag earns its place only if the errors it raises are mostly real problems and fixing them is cheap. The owner wants to see these: the end-of-task report lists them in a 'TypeScript settings' subsection of its Findings section, next to the 'Lint and CI rules' subsection from TASK-32. The report shape comes from TASK-15 (docs/protocols/done.md).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Template guidance (AGENTS.md at most 2 lines, detail in docs/protocols/typescript.md): before proposing a stricter flag, run the type check with it and count the new errors; apply it in the same change only when the errors are few and mostly real; otherwise propose it with the error count; never loosen the TASK-2.1 baseline without a decision record
- [ ] #2 The guidance names a short list of candidate flags beyond the baseline, verified against the current TypeScript release notes, each with the bug class it catches and its typical friction
- [ ] #3 The end-of-task report defined by TASK-15 has a 'TypeScript settings' subsection under Findings listing flags applied (with error count fixed) and flags proposed (with error count and why not applied); it says 'none' when empty
- [ ] #4 Smoke test passes for all three stacks; rendered AGENTS.md stays within the line budget; decision recorded in docs/decisions/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

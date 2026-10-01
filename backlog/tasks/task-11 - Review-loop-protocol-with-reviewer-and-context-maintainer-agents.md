---
id: TASK-11
title: Review-loop protocol with reviewer and context-maintainer agents
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-01 19:51'
labels:
  - review
  - agents
milestone: m-0
dependencies:
  - TASK-24
priority: high
type: feature
ordinal: 400
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner experience: independent fresh-context review loops are very valuable, so the round cap goes up: 8 rounds attended, 15 unattended (interpreted as caps, stop on PASS). Cap exists only for rare stuck-agent edge cases.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Reviewer and context-maintainer agent definitions in the template (fresh context each round, PASS/FINDINGS/INCOMPLETE, Blocking/Material/Minor/Note)
- [ ] #2 Protocol states caps 8 attended and 15 unattended; unresolved after cap goes to the owner
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: moved to Phase 1 because the Ready gate (TASK-26) and every Phase 1 task rely on the reviewer agent. Agent files go in the layout owned by TASK-24.
<!-- SECTION:NOTES:END -->

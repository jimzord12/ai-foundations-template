---
id: TASK-10
title: Session briefing and handoff (Goal / Now / Next / You)
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-03 20:11'
labels:
  - protocol
  - handoff
milestone: m-1
dependencies:
  - TASK-8
priority: medium
type: feature
ordinal: 10000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The owner works on many projects at once and has poor memory; each fresh session must open with a four-line orientation and each session must end by rewriting a single handoff.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Briefing schema (Goal, Now, Next, You) added; rewritten in place at session end by the lead only
- [ ] #2 AGENTS.md tells agents to read it first and to check loose ends (open proposals, blocked tasks, unreviewed commits)
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
2026-10-01: the owner is designing the feedback loop (self-improvement system) with another agent and will bring back a markdown with the design and decisions. Re-check this task against that design before starting.

2026-10-03 owner: the feedback-loop design will come at some point, not now. Keep this task waiting for it; do not plan it without that design.
<!-- SECTION:NOTES:END -->

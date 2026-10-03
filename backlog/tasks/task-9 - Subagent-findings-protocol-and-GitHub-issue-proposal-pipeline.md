---
id: TASK-9
title: Subagent findings protocol and GitHub-issue proposal pipeline
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-03 20:11'
labels:
  - protocol
  - findings
milestone: m-1
dependencies:
  - TASK-8
priority: high
type: feature
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Subagents must report pains, frictions, ideas and risks. Findings are ephemeral and several agents may report the same problem. Flow: subagent finding, lead triages and dedupes, lead creates or updates a GitHub issue (proposal) that counts how many times the problem was reported, owner approves in the viewer, lead then creates the Backlog task.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Every subagent definition in the template requires a findings block in its final report; lead rejects reports without it
- [ ] #2 Lead procedure documented: dedupe against open proposal issues, update occurrence count, or create a new issue
- [ ] #3 Issue format defined (labels, occurrence count, no secrets since repos may be public)
- [ ] #4 Optional SubagentStop hook enforcement verified against current Claude Code docs
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

2026-10-02: the subagent findings block should reuse the 'Lint and CI rules' and 'TypeScript settings' subsections that TASK-32 and TASK-33 add to done.md's Findings section.

2026-10-03 owner: the feedback-loop design will come at some point, not now. Keep this task waiting for it; do not plan it without that design.
<!-- SECTION:NOTES:END -->

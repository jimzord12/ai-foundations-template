---
id: TASK-36
title: >-
  Experiment: can agents add a protocol from a vague prompt with only a
  checklist
status: In Progress
assignee:
  - '@claude'
created_date: '2026-10-02 16:30'
updated_date: '2026-10-02 16:30'
labels:
  - experiment
dependencies: []
priority: medium
ordinal: 25000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The owner asked whether a protocol-authoring skill is needed. Recommendation (2026-10-02): first add an "Adding a protocol" checklist to template/docs/protocols/agents.md, then see whether agents follow it before building a skill. The owner asked for the experiment now: five Sonnet subagents (two at medium effort, three at high), each given a vague request to create a different protocol in its own worktree, graded against a hidden scorecard. Their protocols are throwaway; only the findings and the checklist are kept.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The checklist exists in template/docs/protocols/agents.md and is reviewed to PASS
- [ ] #2 Five agents ran with vague prompts in isolated worktrees, and each result is scored against the same hidden scorecard
- [ ] #3 A findings report says whether a skill is needed, with the evidence, and the owner decides
- [ ] #4 Experiment worktrees, branches and temporary agent profiles are removed afterwards
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
Attended run; owner asked for it now (ready gate waived by the owner).
<!-- SECTION:NOTES:END -->

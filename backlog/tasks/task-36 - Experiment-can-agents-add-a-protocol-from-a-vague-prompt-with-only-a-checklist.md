---
id: TASK-36
title: >-
  Experiment: can agents add a protocol from a vague prompt with only a
  checklist
status: Done
assignee:
  - '@claude'
created_date: '2026-10-02 16:30'
updated_date: '2026-10-02 16:48'
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
- [x] #1 The checklist exists in template/docs/protocols/agents.md and is reviewed to PASS
- [x] #2 Five agents ran with vague prompts in isolated worktrees, and each result is scored against the same hidden scorecard
- [x] #3 A findings report says whether a skill is needed, with the evidence, and the owner decides
- [x] #4 Experiment worktrees, branches and temporary agent profiles are removed afterwards
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [x] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [x] #3 Independent review loop reached PASS for non-trivial changes
- [x] #4 Non-trivial decisions recorded in docs/decisions/
- [x] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Attended run; owner asked for it now (ready gate waived by the owner).

Results. Agent A (handoff, medium) was blocked by the auto-mode classifier when launched headless; the owner did not rerun it. The -w worktrees started from main, so B-E ran WITHOUT the checklist (a control arm). Scorecard (card / router row / decision record / checks / review loop): B bugs, medium: yes/yes/yes/yes/skipped (said so). C experiments, high: yes/yes/yes/yes/PASS r2. D self-improvement, high: yes/yes/yes/yes/PASS r2. E dependencies, high: yes/yes/yes/yes/PASS r3. No agent needed a new profile or skill, so checklist step 4 is untested. Gaps found: B, D and E all numbered their record 0041 (TASK-37); C gave lab-examples.md a fake rule card and router row to pass the check (TASK-38). Owner decision 2026-10-02: no protocol-authoring skill; keep the checklist. D and E text kept as doc-5 and doc-6; shipping the check to projects is TASK-39. Checklist review: context-reviewer round 1 FINDINGS (Material: step 6 named one reviewer though a decision record needs docs-reviewer; fixed by deferring to review.md), round 2 PASS, its Minor applied. Smoke 3 stacks pass; protocol and dogfood checks pass. Cleanup: 4 worktrees, 4 branches, 2 temporary profiles and scratch files removed; the stack-packs worktree belongs to another session and was left alone.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Added an "Adding a protocol" checklist to docs/protocols/agents.md. Experiment: four Sonnet agents given vague requests (without the checklist) all wrote a valid card, router row and decision record and ran the check; three of four ran the review loop. Owner decided no skill is needed. Follow-ups TASK-37 (decision-number collisions), TASK-38 (supporting files), TASK-39 (ship the check to projects); D and E protocol text kept as doc-5 and doc-6. Review loop PASS in round 2.
<!-- SECTION:FINAL_SUMMARY:END -->

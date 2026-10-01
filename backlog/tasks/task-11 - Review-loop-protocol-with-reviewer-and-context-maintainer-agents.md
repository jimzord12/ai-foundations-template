---
id: TASK-11
title: 'Review loop: code-reviewer profile and review-core / review-lenses skills'
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
updated_date: '2026-10-01 21:26'
labels:
  - review
  - agents
  - ready
milestone: m-0
dependencies:
  - TASK-24
priority: high
type: feature
ordinal: 600
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Fresh-context review loop for this repo and generated projects. Specific thin profiles plus shared skills (decision 2026-10-01): a code-reviewer agent (read-only tools, Opus) that preloads a review-core skill (fresh-context rules, evidence, PASS / FINDINGS / INCOMPLETE, Blocking / Material / Minor / Note) and a review-lenses skill. The name code-review is avoided because Claude Code ships a built-in /code-review skill. Caps: 8 rounds attended, 15 unattended; unresolved after the cap goes to the owner. Documentation reviewers (context-reviewer, context-maintainer, docs-reviewer) are built in TASK-29 and TASK-30 on the same review-core skill.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 review-core and review-lenses skills plus the code-reviewer profile ship in template/ and in this repo (pairs added to the dogfood manifest)
- [ ] #2 docs/protocols/review.md states the loop, caps, and the attended rule: a run is attended only while the owner is replying in the session, otherwise unattended; router line in AGENTS.md (at most 4 lines)
- [ ] #3 Proof in a new session or headless claude -p: the code-reviewer profile is found, quotes a marker line from review-core (proving its own skills were preloaded, not the built-in /code-review), and runs one real review round on a diff in this repo, report saved in the task notes
- [ ] #4 docs/protocols/review.md states that changes to instruction files (AGENTS.md, protocols, agent profiles, skills) and decision records are non-trivial and always reviewed, and names which reviewer profile handles which kind of change (code, agent context, project docs)
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
2026-10-01: moved to Phase 1 because the Ready gate (TASK-26) and every Phase 1 task rely on the reviewer agent. Agent files go in the layout owned by TASK-24.

2026-10-01 (decision 'Two documentation reviewer families with shared skills'): review-core is the shared base for every reviewer, including context-reviewer and docs-reviewer (TASK-29, TASK-30); it holds one severity scale repos may remap. review.md must state that changes to instruction files and decision logs count as non-trivial.
<!-- SECTION:NOTES:END -->

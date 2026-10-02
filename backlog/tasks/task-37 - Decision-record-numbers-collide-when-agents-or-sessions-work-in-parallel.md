---
id: TASK-37
title: Decision record numbers collide when agents or sessions work in parallel
status: To Do
assignee: []
created_date: '2026-10-02 16:45'
updated_date: '2026-10-02 21:36'
labels:
  - feature
milestone: m-0
dependencies: []
priority: high
ordinal: 950
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Decision records take the next free number. On 2026-10-02 a parallel session landed 0039 while TASK-34 also used 0039 (renumbered to 0040 at merge), and in experiment TASK-36 three independent agents all chose 0041. Any parallel work (sessions, worktrees, unattended runs) will keep colliding, and the merge only shows a conflict in the README index, not in the record files.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Two branches that each add a decision record from the same base can both merge without renaming a record by hand
- [ ] #2 The rule is documented in template/docs/decisions/README.md and this repo's docs/decisions/README.md
- [ ] #3 Existing records and links keep working
- [ ] #4 New records are named by UTC timestamp and slug (for example 2026-10-03-1415-stack-packs.md) instead of the next free number; every record numbered before this task lands (0001 to 0042 at the time of writing) keeps its name
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
Sequenced 2026-10-02 (owner asked to fix priorities): first in phase 1 before the stack work, because parallel sessions and agents hit the collision four times on 2026-10-02 (0039/0040, 0041 x3 in TASK-36, and the stack-packs record). Not part of the phase check; needs its own ready challenge at pickup.

2026-10-03 owner decision: timestamp names, chosen over numbers assigned at merge because two branches cannot pick the same name and there is no merge-time step for an agent to forget.
<!-- SECTION:NOTES:END -->

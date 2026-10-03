---
id: TASK-3
title: Dependencies protocol and preferred-library freshness check
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
updated_date: '2026-10-03 20:13'
labels:
  - libraries
  - tooling
milestone: m-1
dependencies:
  - TASK-37
priority: medium
type: feature
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents add libraries too easily, and the preferred-library list in template/docs/protocols/typescript.md goes stale (for example date-fns once Temporal is native). Experiment TASK-36 produced a reviewed protocol for adding a dependency (need check, vetting table, who approves, install, proof, record), kept as doc-6 and not adopted. This task adopts it and adds the other half: keeping the preferred list current. Renovate or Dependabot for version bumps is a separate concern. Ideas from the original task, not decided: a machine-readable manifest of the preferred list (for example ai/preferred-libraries.json with purpose, package, runtime notes such as React Native caveats, last reviewed and alternatives), a script that queries the npm registry (weekly downloads among its metrics), and a quarterly review.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 template/docs/protocols/dependencies.md is adopted from doc-6, adapted to the current template (card, router row in AGENTS.md.jinja within the line budget, protocol_check.py passes), with its decision record named under the decision-record naming rule in force (TASK-37); the library bullets in typescript.md that duplicate its need and vetting steps are reduced to a pointer to dependencies.md
- [ ] #2 Where the preferred list lives is decided and recorded (stays in typescript.md, or moves to a machine-readable file that typescript.md and dependencies.md reference); each entry carries a last-reviewed date
- [ ] #3 A check script reports, for each preferred package, the latest version, last publish date, weekly downloads, deprecation and license from the npm registry, and flags any with no release in about 12 months, deprecated, or not permissively licensed; shown flagging a known deprecated package
- [ ] #4 When the list is reviewed is documented (a trigger such as a periodic review or a TASK-22 audit run), and each review outcome goes to the decision log
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
Overlap found 2026-10-02: doc-6 (dependencies protocol text from experiment TASK-36) covers vetting a new library. Reconcile the two before planning this task.

2026-10-03: reconciled with doc-6: doc-6 covers adding a library and this task covered keeping the list fresh, so both halves are now this task (criteria rewritten). TASK-22's template adapter also names a stale-preferred-libraries check; reuse this task's script there instead of building a second one.
<!-- SECTION:NOTES:END -->

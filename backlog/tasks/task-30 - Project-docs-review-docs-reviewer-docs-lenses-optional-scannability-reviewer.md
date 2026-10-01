---
id: TASK-30
title: >-
  Project-docs review: docs-reviewer, docs-lenses, optional
  scannability-reviewer
status: To Do
assignee: []
created_date: '2026-10-01 20:52'
updated_date: '2026-10-01 21:26'
labels:
  - review
  - docs
  - knowledge
  - ready
milestone: m-0
dependencies:
  - TASK-11
  - TASK-25
priority: high
type: feature
ordinal: 660
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
No project-docs reviewer exists in any of the owner's repos; doc correctness was improvised from code-reviewer lenses each time. The knowledge system (TASK-25) adds architecture.md, decision records and a glossary that must stay true to the code. Ideas to reuse: greek-essence doc-reviewer's truth lens (every claim traces to a file, recompute numbers), ICS feature-maps rules (code outranks docs, anchor on symbol names not line numbers, stale claims dropped), ICS plan-reviewer (unverifiable claims reported as unverified), ICS scannability-reviewer (one shape per entry, zero filler, salience spent not sprayed). Decision: 'Two documentation reviewer families with shared skills'.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 docs-lenses skill ships with: code outranks docs, symbol anchors, decision-record completeness and supersede chain, accepted architecture decisions reflected in architecture.md, folder map matches the real tree, glossary terms used in code and UI, README quickstart actually runs, numbers recomputed, unverified claims reported as unverified, cold-reader completeness; items for architecture.md and the glossary apply only when the file exists
- [ ] #2 docs-reviewer profile (Read, Grep, Glob, plus Bash used only for checks in a scratch copy outside the working tree, such as running the quickstart; no Edit, Write or Agent; Opus, high) preloads review-core and docs-lenses; the profile notes that a quickstart run may be denied by the permission allowlist and is then reported NOT_CHECKED
- [ ] #3 scannability-reviewer (Read, Grep, Glob; Sonnet, high effort) preloads review-core and scan-lenses; it ships like any profile, with no Copier question, and is opt-in: its description says to run it only when review.md or the owner asks, and review.md lists it as an add-on for human-facing docs
- [ ] #4 docs-lenses, scan-lenses, docs-reviewer and scannability-reviewer ship in template/ and in this repo (pairs in dogfood.json)
- [ ] #5 Proof: docs-reviewer catches a planted stale claim (a path in architecture.md that no longer exists) in a generated project, report saved in the task notes; shipped files carry no source-repo names (same grep as TASK-29)
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
2026-10-02 readiness round 1 owner-type questions decided by the agent (ordinary choices): scannability-reviewer is opt-in through its description, no Copier question; docs-reviewer is dogfooded in this repo.
<!-- SECTION:NOTES:END -->

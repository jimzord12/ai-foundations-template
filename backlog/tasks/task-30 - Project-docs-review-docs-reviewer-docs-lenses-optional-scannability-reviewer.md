---
id: TASK-30
title: >-
  Project-docs review: docs-reviewer, docs-lenses, optional
  scannability-reviewer
status: To Do
assignee: []
created_date: '2026-10-01 20:52'
labels:
  - review
  - docs
  - knowledge
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
- [ ] #1 docs-lenses skill ships with: code outranks docs, symbol anchors, decision-record completeness and supersede chain, accepted architecture decisions reflected in architecture.md, folder map matches the real tree, glossary terms used in code and UI, README quickstart actually runs, numbers recomputed, unverified claims reported as unverified, cold-reader completeness
- [ ] #2 docs-reviewer profile (Read, Grep, Glob, plus Bash limited to read-only checks such as running the quickstart in a scratch copy; Opus, high) preloads review-core and docs-lenses
- [ ] #3 Optional scannability-reviewer (Read, Grep, Glob; Sonnet, high effort) with a scan-lenses skill ships disabled by default and is documented in review.md as an add-on for human-facing docs
- [ ] #4 Proof: docs-reviewer catches a planted stale claim (a path in architecture.md that no longer exists) in a generated project, report saved in the task notes; shipped files carry no source-repo names
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

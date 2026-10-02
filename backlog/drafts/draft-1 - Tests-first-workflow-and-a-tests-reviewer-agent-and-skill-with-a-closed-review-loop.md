---
id: DRAFT-1
title: >-
  Tests-first workflow and a tests-reviewer (agent and skill) with a closed
  review loop
status: Draft
assignee: []
created_date: '2026-10-02 01:10'
labels:
  - agents
  - testing
  - review
dependencies: []
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner request 2026-10-02, parked as a draft (not for implementation yet; needs research first).

## Problem

Agents rarely write good tests on the first try: tests that pass with the implementation deleted, tests that mirror the code instead of the behaviour, and whole dimensions (boundaries, error paths, state transitions) left out. Test writing needs its own closed review loop.

## Idea

1. Code tasks predefine the signatures, methods and behaviours to implement (inputs, outputs, errors), so the Ready gate can check them and an agent can write tests before the code, black-box.
2. Workflow per code task: tests first -> implementation -> reviews (code-reviewer, tests-reviewer, others as routed).
3. A `tests-reviewer` profile plus a `tests-lenses` skill (on top of `review-core`), run per task and per phase. Its only job: judge whether the tests exercise real behaviour and find the dimensions the author missed, using well-known techniques:
   - mutation testing (for example Stryker for TypeScript);
   - black-box techniques: equivalence partitioning, boundary values, decision tables, state transitions;
   - property-based testing (for example fast-check);
   - the rule that a test which passes with the implementation deleted is worthless; mocks only at true external boundaries.

## Acceptance criteria (draft; refine when promoted)

- [ ] A research note on tools and techniques per stack (Express, Next.js, React Native): mutation testing, property-based testing, black-box design techniques, and their cost.
- [ ] Code tasks carry predefined signatures and behaviours; the Ready gate (TASK-26) checks for them.
- [ ] The tests-first workflow is documented in the template protocols.
- [ ] The tests-reviewer profile and tests-lenses skill ship in template/ and are dogfooded into this repo; review.md routes test changes to it.
- [ ] Proof: on a planted change, the tests-reviewer catches a weak test (passes with the implementation deleted) and a missed boundary case.

## Related

TASK-11 (review loop), TASK-15 (agent layout), TASK-26 (Ready gate), TASK-2.3, TASK-20.
<!-- SECTION:DESCRIPTION:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

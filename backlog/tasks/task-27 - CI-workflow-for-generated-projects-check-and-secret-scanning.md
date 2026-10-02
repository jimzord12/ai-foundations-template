---
id: TASK-27
title: 'CI workflow for generated projects: check'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 18:39'
labels:
  - ci
  - stack
milestone: m-0
dependencies:
  - TASK-2.4
priority: high
type: feature
ordinal: 1500
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner decision 2026-10-01: generated projects get one minimal CI workflow in v0.1.0 so agent changes are checked on every push. It runs the project's check script (from TASK-2.4); TASK-23 adds the secret-scanning step to it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Template ships .github/workflows/check.yml for every Phase 1 pack that runs npm ci and npm run check where the project has a package-lock.json and a check script (a project on the generic pack has no check script and still gets the workflow for secret scanning, unless this task decides otherwise at pickup), triggered on push to any branch and on pull requests
- [ ] #2 Workflow is green on a freshly generated project per stack pushed as a branch to jimzord12/ai-foundations-scratch, and red when a check fails; the agent deletes only branches it created, never repositories
- [ ] #3 Action versions verified against current docs and recorded
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
2026-10-01 owner answer Q1: CI proofs use the private repo jimzord12/ai-foundations-scratch (decision of that date). Push one branch per stack and proof; delete only branches you created; never create or delete repositories or force push.

2026-10-02: record 0041 (stack-agnostic core with packs picked by detection): "per stack" in this task now means per Phase 1 pack (Next.js, bare React Native, Express); more frameworks are TASK-2.6. The generated workflow runs npm ci and npm run check only where the project has a check script (a project on the generic pack, including a framework with no pack yet, gets no scripts under record 0041); it must not hard-code a stack list. Projects without a check script still get the workflow for secret scanning (TASK-23) unless this task decides otherwise at pickup. The ready label was removed because this changes what the task must do; plan and challenge again before unattended work, or the owner waives it.

2026-10-02 (records 0036 and 0041): .github/workflows/check.yml is rendered by Copier, so a copy with --overwrite over an existing project would replace a workflow of the same name. Decide at pickup how it ships so an existing workflow is never overwritten (for example only when missing).
<!-- SECTION:NOTES:END -->

---
id: TASK-23
title: 'Security baseline: secret scanning in CI and safe env handling'
status: To Do
assignee: []
created_date: '2026-10-01 16:40'
updated_date: '2026-10-01 20:20'
labels:
  - security
  - ci
milestone: m-0
dependencies:
  - TASK-13
  - TASK-27
priority: high
type: feature
ordinal: 1800
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Repos are public and agents commit often, so a leaked secret is a real risk. The owner suggests gitleaks for secret scanning in CI. Generated projects and this repo need a small, standard baseline. Verify current gitleaks version and the licence terms of its GitHub Action (free for personal accounts vs organisations) before relying on it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Secret scanning (gitleaks with version and Action licence verified, or the verified standard alternative) runs in this repo CI (TASK-13) and in the generated-project workflow (TASK-27)
- [ ] #2 Generated projects ship .env.example; real .env files are ignored per stack (Next.js and the Express skeleton via their .gitignore, RN verified); the secrets rule itself lives in docs/protocols/git.md (TASK-14)
- [ ] #3 Proof in this repo and in one generated project: a planted fake secret fails CI. Generated-project proof uses the owner-approved scratch repository (open owner question Q1); only branches the agent created are deleted
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions.md
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: adds a step to the CI workflow owned by TASK-13.
<!-- SECTION:NOTES:END -->

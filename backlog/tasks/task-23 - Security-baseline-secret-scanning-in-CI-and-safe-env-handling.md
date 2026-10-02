---
id: TASK-23
title: 'Security baseline: secret scanning in CI and safe env handling'
status: To Do
assignee: []
created_date: '2026-10-01 16:40'
updated_date: '2026-10-02 17:05'
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
- [ ] #2 Generated projects ship .env.example and git check-ignore shows it NOT ignored on every scaffolded stack (Next.js needs a !.env.example exception added by the post-copy task); real .env files are ignored on every stack (RN .gitignore gets .env added if missing); the secrets rule itself lives in docs/protocols/git.md (TASK-14)
- [ ] #3 Proof for both workflows runs on branches of jimzord12/ai-foundations-scratch, never in this public repo: a fake secret that gitleaks detects but GitHub push protection does not block (for example the generic API key rule) fails CI; push protection is never bypassed; only branches the agent created are deleted
- [ ] #4 This repo's root .gitignore gets a !template/.env.example* exception so the template file is tracked (git check-ignore shows it not ignored)
- [ ] #5 Proof details: the fake is first confirmed locally with gitleaks detect (gitleaks skips low-entropy values and words like example); CI output shows the failure comes from the secret-scanning step; the same branch without the fake goes green
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
2026-10-01: adds a step to the CI workflow owned by TASK-13.

2026-10-01 owner answer Q1: CI proofs use the private repo jimzord12/ai-foundations-scratch (decision of that date). Push one branch per stack and proof; delete only branches you created; never create or delete repositories or force push.

2026-10-02: record 0041 (stack-agnostic core with packs picked by detection): "every stack" in this task now means every Phase 1 pack (Next.js, bare React Native, Express) plus the generic fallback; more frameworks are TASK-2.6. The post-copy task appends .env to an ignore file when it is missing (record 0041 allows appended ignore-file lines and nothing else in the project's own files); decide at pickup whether an existing Express project's .gitignore gets the line like an RN one does. The ready label was removed because its dependencies (TASK-13, TASK-27) changed what the plan relies on; plan and challenge again before unattended work, or the owner waives it.
<!-- SECTION:NOTES:END -->

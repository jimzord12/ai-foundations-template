---
id: TASK-23
title: 'Security baseline: secret scanning in CI and safe env handling'
status: To Do
assignee: []
created_date: '2026-10-01 16:40'
labels:
  - security
  - ci
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 23000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Repos are public and agents commit often, so a leaked secret is a real risk. The owner suggests gitleaks for secret scanning in CI. Generated projects and this repo need a small, standard baseline. Verify current gitleaks version and the licence terms of its GitHub Action (free for personal accounts vs organisations) before relying on it.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 gitleaks (or the verified standard alternative) runs in CI for this repo and in generated projects, failing on a finding
- [ ] #2 Generated projects ship .env.example and ignore real .env files; AGENTS.md says secrets never go in code, logs or commits
- [ ] #3 Verified by a planted fake secret failing CI on a scratch branch; decision recorded
<!-- AC:END -->

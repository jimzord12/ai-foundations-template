---
id: TASK-2
title: 'Define per-stack template contents (tsconfig, lint, test, CI, feedback loop)'
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
updated_date: '2026-10-01 16:40'
labels:
  - template
  - tooling
milestone: m-0
dependencies: []
priority: high
ordinal: 2000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Decide and add the baseline each generated project gets: strict tsconfig (e.g. @tsconfig/strictest + stack base), ts-reset setup, linting/formatting, test runner, CI, and the fast typecheck/lint/test commands agents are told to run. Stacks: Express 5 + Zod, Next.js 16.3, bare React Native 0.81 (Hermes). Verify current versions before choosing.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Each choice recorded in docs/decisions.md
- [ ] #2 copier copy renders a working project for express, next and rn
- [ ] #3 Agent instructions name the exact check commands
<!-- AC:END -->

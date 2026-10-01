---
id: TASK-2
title: >-
  Per-stack baseline: strict TypeScript, lint/format, tests, check commands
  (parent)
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
updated_date: '2026-10-01 19:51'
labels:
  - template
  - tooling
milestone: m-0
dependencies: []
priority: high
ordinal: 800
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Parent for the technical baseline every generated project gets, split into subtasks so each is one reviewable change. Stacks: Express 5 + Zod, Next.js 16.3, bare React Native (owner's brief says 0.81 on Hermes, no Expo; a 2026-09-29 review saw @react-native-community/template 0.87.2 as latest, so the RN version is an open question for the owner before 2.1 starts). Verify current versions of every tool before choosing. Owner of CI is TASK-13 (not this task). Owner of the done rule is TASK-15; this task owns the tooling the rule refers to.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 All subtasks done
- [ ] #2 copier copy renders a project for express, next and rn whose check commands pass on a fresh install
<!-- AC:END -->

---
id: TASK-19
title: 'Docker environment for reproducible, isolated test runs'
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
labels:
  - testing
  - docker
dependencies:
  - TASK-17
priority: high
type: feature
ordinal: 19000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Test and eval runs must be reproducible and isolated: pinned Node, uv/Copier, Backlog.md and agent CLI versions, throwaway containers, unattended agent runs that cannot touch the host or the owner's real repos. Known limits to design around: React Native device and Android builds are impractical in a container (limit RN to lint, typecheck, unit tests and instruction-adherence checks); agent authentication inside a container needs an owner decision (API key vs mounting a login).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Pinned image and one command that runs the automated template tests in a clean container
- [ ] #2 Container runs an agent unattended on a fixture with no access to host repos or global config
- [ ] #3 Agent authentication approach decided by the owner and recorded; RN limits documented
<!-- AC:END -->

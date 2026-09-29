---
id: TASK-12
title: Optional personalization skill for new installations (.local preferences)
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
labels:
  - skill
  - onboarding
dependencies: []
priority: medium
type: feature
ordinal: 12000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The template default is a neutral technical-product-owner profile. On a new installation an optional skill runs a 10-15 minute interview (communication style, tone, behaviors, engineering rigor, delivery speed, conventions, standards, stack) and writes the answers to the git-ignored .local preferences folder.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Skill shipped in the template and offered after copier copy
- [ ] #2 Interview covers communication, tone, rigor, speed, conventions, standards, stack
- [ ] #3 Answers written under .local/preferences (git-ignored) and referenced from AGENTS.md with precedence rules
<!-- AC:END -->

---
id: TASK-18
title: 'Fixture projects: 3-5 greenfield and 3-5 brownfield variations'
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
labels:
  - testing
  - fixtures
dependencies: []
priority: high
type: feature
ordinal: 18000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The template must be tried on realistic projects. Greenfield: freshly scaffolded projects per stack and variation (for example Express API with and without a database, Next.js App Router with and without Tailwind, bare React Native). Brownfield: existing repos with their own AGENTS.md or CLAUDE.md, none at all, conflicting rules, a monorepo, a different package manager. Brownfield fixtures are small hand-made repos capturing each collision class; greenfield ones come from pinned scaffolder versions. First decision: where the fixtures and the agent evals live (this repo under tests/ vs a separate evals repo, since fixtures, Docker and transcripts add bulk).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Decision on repo home for fixtures and evals recorded in docs/decisions.md
- [ ] #2 3-5 greenfield and 3-5 brownfield fixtures defined, each documenting the situation it represents
- [ ] #3 Each fixture can be rebuilt from scratch with one command and pinned tool versions
<!-- AC:END -->

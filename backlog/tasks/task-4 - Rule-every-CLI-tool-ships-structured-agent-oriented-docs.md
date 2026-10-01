---
id: TASK-4
title: 'Rule: every CLI tool ships structured, agent-oriented docs'
status: To Do
assignee: []
created_date: '2026-09-29 10:28'
updated_date: '2026-10-01 16:40'
labels:
  - instructions
  - cli
milestone: m-1
dependencies: []
priority: medium
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents build and use many CLI tools; they should learn why/how/what a command does without reading its code. docs differs from --help (--help = usage/args; docs = condensed explanation: purpose, how it works, when to use, behavior, gotchas). Tree-structured, mirroring the command tree: 'sandbox docs' = full docs (~500-1000 lines); 'sandbox docs --index' = sections + subsections with a brief description and a size each. Same at every level: 'sandbox create docs' / 'sandbox create docs --index', scoped to create. Open design points: docs subcommand vs --docs flag (collision with positional args, e.g. a sandbox named 'docs'); fetching one section by id; whether a parent's full docs include children; source format (co-located markdown, headings = sections, generated index); CI enforcement (every command has docs, size budgets); token estimate vs char/word counts; check for an existing standard/library or CLI-framework support before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Design points resolved and recorded in docs/decisions.md
- [ ] #2 Rule text added to agent instructions
- [ ] #3 Shared helper or reference implementation + test available
<!-- AC:END -->

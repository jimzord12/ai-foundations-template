---
id: TASK-4
title: 'Spike: design for agent-oriented docs in CLI tools'
status: To Do
assignee: []
created_date: '2026-09-29 10:28'
updated_date: '2026-10-03 20:13'
labels:
  - instructions
  - cli
milestone: m-1
dependencies: []
priority: medium
type: spike
ordinal: 4000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Agents build and use many CLI tools; they should learn why/how/what a command does without reading its code. docs differs from --help (--help = usage/args; docs = condensed explanation: purpose, how it works, when to use, behavior, gotchas). Tree-structured, mirroring the command tree: 'sandbox docs' = full docs (~500-1000 lines); 'sandbox docs --index' = sections + subsections with a brief description and a size each. Same at every level: 'sandbox create docs' / 'sandbox create docs --index', scoped to create. Open design points: docs subcommand vs --docs flag (collision with positional args, e.g. a sandbox named 'docs'); fetching one section by id; whether a parent's full docs include children; source format (co-located markdown, headings = sections, generated index); CI enforcement (every command has docs, size budgets); token estimate vs char/word counts; check for an existing standard/library or CLI-framework support before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Every open design point in the description is answered and recorded in docs/decisions/ (docs subcommand vs --docs flag, fetching one section by id, whether a parent's docs include its children, source format, CI enforcement and size budgets, token estimate vs character or word counts)
- [ ] #2 Existing standards, libraries and CLI-framework support are checked and either adopted or rejected with a reason in the record
- [ ] #3 The owner's earlier tool that used this pattern is the starting point: the owner names where it is, and the record says what it kept and what it changed
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
2026-10-03 owner: the pattern is already proven: the owner used it in an earlier tool and it was very useful to agents. So this spike decides how, not whether. The rule text and the shared helper or reference implementation (old criteria 2 and 3) moved to a follow-up task that depends on this one.

2026-10-03: the follow-up task named above is TASK-41.
<!-- SECTION:NOTES:END -->

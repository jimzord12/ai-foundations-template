---
id: TASK-38
title: Protocols need a home for supporting files such as worked examples
status: To Do
assignee: []
created_date: '2026-10-02 16:45'
labels:
  - feature
dependencies: []
priority: medium
ordinal: 27000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
scripts/protocol_check.py (decision 0040) requires a card and a router row for every .md file in template/docs/protocols/. In experiment TASK-36 an agent split its lab protocol into lab.md and lab-examples.md and, to pass the check, gave the examples file a fake rule card and its own router row. DRAFT-2 (lab protocol) plans the same split. The format has no place for files that support a protocol without being one.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 A protocol can ship supporting files (for example worked examples) without a card or router row of their own
- [ ] #2 The check still fails when a real protocol lacks a card, and when a supporting file has no owning protocol
- [ ] #3 The Protocol cards section in template/docs/protocols/agents.md says where supporting files go
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

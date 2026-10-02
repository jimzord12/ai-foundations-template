---
id: TASK-40
title: Ship a .gitattributes in generated projects (LF line endings)
status: To Do
assignee: []
created_date: '2026-10-02 03:22'
updated_date: '2026-10-02 18:27'
labels:
  - template
milestone: m-0
dependencies: []
priority: medium
ordinal: 960
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Found in TASK-28 review round 1 (pre-existing, Minor): the root .gitattributes comment says 'LF in the repo and in rendered projects', but template/ ships no .gitattributes, so generated projects get no line-ending rule. Fix: add template/.gitattributes (text=auto eol=lf) or reword the root comment. Check that Copier renders a dotfile from template/ and that the smoke test still passes.
<!-- SECTION:DESCRIPTION:END -->

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
Promoted from DRAFT-3 and sequenced into phase 1 on 2026-10-02 (owner asked to fix priorities): small, and CRLF warnings showed up in this repo the same day. Needs its own ready challenge at pickup.
<!-- SECTION:NOTES:END -->

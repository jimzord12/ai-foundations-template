---
id: TASK-40
title: Ship a .gitattributes in generated projects (LF line endings)
status: To Do
assignee: []
created_date: '2026-10-02 03:22'
updated_date: '2026-10-03 20:11'
labels:
  - template
milestone: m-0
dependencies: []
priority: medium
type: chore
ordinal: 960
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Found in TASK-28 review round 1 (pre-existing, Minor): the root .gitattributes comment says 'LF in the repo and in rendered projects', but template/ ships no .gitattributes, so generated projects get no line-ending rule. Fix: add template/.gitattributes (text=auto eol=lf) or reword the root comment. Check that Copier renders a dotfile from template/ and that the smoke test still passes.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 template/.gitattributes ships with '* text=auto eol=lf' and is listed in _skip_if_exists in copier.yml; a fresh render into an empty folder gets it
- [ ] #2 Copying over a project that already has its own .gitattributes keeps the project's file, also with --overwrite (shown with a scratch copy)
- [ ] #3 A decision record states the general rule: config files the template ships for a project only when missing (.gitattributes here; .env.example in TASK-23 and .github/workflows/check.yml in TASK-27 follow it) are listed in _skip_if_exists; it also states the tradeoff that copier update then never changes such a file in an existing project
- [ ] #4 The root .gitattributes comment about rendered projects is accurate, and the smoke test passes
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
Promoted from DRAFT-3 and sequenced into phase 1 on 2026-10-02 (owner asked to fix priorities): small, and CRLF warnings showed up in this repo the same day. Needs its own ready challenge at pickup.

2026-10-02 (records 0036 and 0041): .gitattributes is a config file of the project, so a copy with --overwrite over a scaffold or an existing project must not replace the project's own. Decide at pickup how it ships: only when the project has none, or as appended lines (post-copy tasks may append lines to an ignore file under record 0041; the same would need a decision for this file).

2026-10-03 (owner review of the backlog): how it ships is decided: _skip_if_exists. A scratch test on Copier 9.18.2 showed a file listed there keeps the project's own copy under copy --overwrite while an unlisted file is replaced. This task comes first in phase 1 order (before TASK-2.5), so it records the general rule that TASK-2.5, TASK-23 and TASK-27 reuse.

2026-10-03 correction: after the TASK-2.5 split, the README part of this rule is TASK-2.7 criterion 1, so the rule is reused by TASK-2.7, TASK-23 and TASK-27 (not TASK-2.5).
<!-- SECTION:NOTES:END -->

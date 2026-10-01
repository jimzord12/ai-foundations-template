---
id: TASK-31
title: >-
  Permissive Claude Code permissions for this repo: allow everything, block
  deleting main
status: To Do
assignee: []
created_date: '2026-10-01 23:01'
labels:
  - agents
  - claude
  - permissions
milestone: m-0
dependencies: []
priority: high
ordinal: 23000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
On 2026-10-02 an unattended run stopped because the Claude Code auto-mode classifier refused `git switch -c`: the command was on neither the allow nor the deny list, so auto mode sent it to the server-side classifier, which refused it with no reason. Branches are mandatory in this repo (AGENTS.md Git), so the refusal blocked all work. Owner instruction 2026-10-02: everything is allowed in this repo except deleting the main branch; only the extremely dangerous commands go to deny or ask. This replaces, for this repo only, TASK-24 AC #1's 'same allowlist minus package scripts, nothing broader'. Whether generated projects get the same permissive policy stays with TASK-24 and is an owner question.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Root .claude/settings.json allows every tool and command an agent needs in this repo without a prompt, including branch creation, commits, merges, pushes and deleting merged branches
- [ ] #2 Deleting main, locally or on the remote, is denied; the destructive git that the owner's rules still gate (force push, reset --hard, git clean, deleting an unmerged branch) is in ask; nothing else is in deny or ask
- [ ] #3 Proof in a throwaway clone under .tmp with headless claude -p, project settings only and no permission flags: creating a branch and committing run without a prompt, and deleting main is refused
- [ ] #4 TASK-24 AC #1 no longer asks for a narrow allowlist in this repo; it points here and keeps the generated-project allowlist as its own open owner question
- [ ] #5 Owner decision recorded as a product record in docs/decisions/
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

---
id: TASK-22
title: Repo maintenance skill and agent profile (from owner's research)
status: To Do
assignee: []
created_date: '2026-09-29 22:09'
updated_date: '2026-09-29 22:39'
labels:
  - maintenance
  - skill
  - agents
dependencies: []
priority: medium
type: feature
ordinal: 22000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Source (outside the repo, owner's research for another repo): C:\Users\jimzord12\Downloads\cvgen-repo-maintenance-bundle. Extract the generic core so this template can evolve and stay in top shape, without importing anything specific to that repo. KEEP (generic): SKILL.md procedure (modes quick/audit/deep/apply, two-layer design, precedence, safety floor, tiers A/B/C, report format, apply protocol with pure-move commit then reference commit), checklist.md (35 checks), scripts/audit.py (stdlib Python + git, 27 read-only checks), repo-auditor-lite (Read/Glob/Grep only), severity words Blocking/Material/Minor/Note as default (matches our review protocol). ADAPT: neutral owner wording (technical product owner, neutral pronouns), report_home (chat by default; saved reports under .local/ or as JSON for the viewer), precedence text (repo's own rules, no 'constitution'), remove .typ from audit.py text extensions, drop the CVgen mention in the optional hook example. DROP (repo-specific, must not enter): .claude/repo-maintenance.md adapter (protected paths, glossary terms, Typst, outputs.py, Trello, Frozen Reference, .night-shift, builds/), docs/04 facts-and-fit, the README adoption playbook and agent cooperation table, third-party-review, newcomer_questions, all CVgen roles (Codex/Claude Code split). Caveats stated by the bundle: skill invocation, subagent spawn, agent-frontmatter hook and the apply protocol were never tested in a live Claude Code session; audit script tested on Linux only; first run on a real repo is noisy. Verify frontmatter fields against current Claude Code docs before shipping. Ties to other tasks: apply protocol is the safe way to do the 'restructure' step of TASK-7; quick mode fits the Definition of Done (TASK-15); brownfield fixtures (TASK-18) with seeded drift are the test bed; audit checks I3 (tracked secrets) and P2 (dependency updates) cover part of the security and dependency gaps.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Extraction filter (keep / adapt / drop) recorded in docs/decisions.md; a grep of everything imported finds no trace of the source repo's names, paths, terms or roles
- [ ] #2 Generic skill, checklist, audit script and lite auditor adapted and working on this repo, with a template-specific adapter (smoke test as declared check, decision-log and backlog hygiene, stale preferred libraries)
- [ ] #3 Decisions made and recorded: where it ships (this repo only vs generated projects, full or lighter), Python dependency for TypeScript projects, how the dogfooded copy in this repo stays in sync with template/
- [ ] #4 Verified in a live Claude Code session on a throwaway branch (skill discovery, auditor spawn, apply protocol), plus the script self-test on this machine; noise from the first run triaged
- [ ] #5 Independent review rounds pass; overlap with TASK-11 (context-maintainer) and TASK-3 (library review) resolved
<!-- AC:END -->

---
id: TASK-1
title: Decide where agent instructions live (global vs per-project)
status: Done
assignee:
  - '@claude'
created_date: '2026-09-29 10:27'
updated_date: '2026-09-29 11:54'
labels:
  - decision
  - instructions
dependencies: []
priority: high
ordinal: 1000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The agreed baseline in docs/agent-instructions.md was written for a global CLAUDE.md. Proposal (not yet confirmed): move nearly all of it into each project via template/AGENTS.md.jinja so cloud sessions, CI agents, other tools and collaborators see it; keep only personal working style in the global ~/.claude/CLAUDE.md. Also proposed: AGENTS.md is canonical (cross-tool standard), CLAUDE.md just contains @AGENTS.md; stack-specific rules in .claude/rules/ with paths: frontmatter (Claude-only; other agents see only AGENTS.md).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Placement decided and recorded in docs/decisions.md
- [x] #2 template/AGENTS.md.jinja contains the chosen content
- [x] #3 Global CLAUDE.md scope written down
<!-- AC:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Write thin template/AGENTS.md.jinja (~100 lines): role, owner profile, philosophy, authority tiers, decision logging, stack blocks, router table, project-specifics section. 2. Move TS reuse-before-building checklist to template/docs/protocols/typescript.md. 3. Update template/CLAUDE.md check, record decisions in docs/decisions.md, mark docs/agent-instructions.md as superseded. 4. Smoke-test all 3 stacks, independent review loop.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Outcome differs from the original proposal: stack rules are inline Jinja blocks in AGENTS.md instead of .claude/rules/ (Claude-only). Global CLAUDE.md scope (personal style only) is recorded in the 2026-09-29 placement decision. AGENTS.md is short (about 60 lines). Round-1 review fixes: .gitignore with .local/, Backlog init instruction, wording fixes.

Review rounds 2-3 outcome: template ships .local/.gitignore (not a root .gitignore, which collides with scaffolded projects); backlog init runs non-interactively with --defaults --agent-instructions none; README documents accepting the AGENTS.md overwrite for create-next-app projects; Next block keeps the managed nextjs-agent-rules block.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Agent instructions now live per project: thin template/AGENTS.md.jinja (about 60 lines, stack blocks inline), TS checklist in template/docs/protocols/typescript.md, CLAUDE.md is @AGENTS.md, global scope recorded in the 2026-09-29 placement decision. Verified by rendering all three stacks (clean, one stack block each, no Jinja leftovers), a real create-next-app + copier copy --overwrite run, non-interactive backlog init from a clean dir, and 4 independent review rounds ending in PASS.
<!-- SECTION:FINAL_SUMMARY:END -->

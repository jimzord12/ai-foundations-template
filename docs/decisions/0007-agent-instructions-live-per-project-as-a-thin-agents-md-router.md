---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: architecture
supersedes: []
---

# Agent instructions live per project, as a thin AGENTS.md router

## Context and Problem Statement

TASK-1. The baseline was written for a global CLAUDE.md, but cloud sessions, CI agents, other tools and collaborators only see files in the repo. Prior projects showed a 17K AGENTS.md becomes a text wall.

## Considered Options

Everything global — invisible to anything but the owner's local Claude Code. Stack rules in `.claude/rules/` with `paths:` — Claude-only, so CI and cloud agents would miss them; reserve that mechanism for long path-scoped rules later.

## Decision Outcome

`template/AGENTS.md.jinja` (short; target under about 100 lines) carries roles, owner profile, philosophy, authority tiers, decision rules and stack blocks, plus a "when to read what" router to files under `docs/`. `CLAUDE.md` contains only `@AGENTS.md`. Stack rules are inline `{% if stack %}` blocks so every agent sees them. The global `~/.claude/CLAUDE.md` keeps only the owner's personal style. Supersedes the "placement open" note in the agent-instruction baseline entry, and narrows "One template, shared files + conditional per-stack files": stack rules are inline blocks, no longer separate `.claude/rules/stack-*.md` files. Global scope: personal style only (tone, language, push-back preference); nothing about libraries, decisions or conventions.

### Consequences

Baseline changes reach projects via a template tag plus `copier update` (not instantly). Keep AGENTS.md under about 100 lines; new detail goes in linked files.

## More Information

- Resolves the open placement note in [0002](0002-agent-instruction-baseline.md); the rest of 0002 stands.
- Narrows [0004](0004-one-template-shared-files-conditional-per-stack-files.md).

---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: technical
supersedes: []
---

# Track open work with Backlog.md

## Context and Problem Statement

Needed a place for open work/backlog that agents and humans can both read and update.

## Considered Options

A single `docs/open-work.md` — no structure/status; GitHub Issues — lives outside the repo, less visible to agents working locally.

## Decision Outcome

[Backlog.md](https://github.com/MrLesk/Backlog.md) (verified v1.53.0, MIT): markdown task files in `backlog/`, git-native, with a CLI (`npx backlog.md ...`) and agent instructions.

### Consequences

Backlog.md also has its own `backlog/decisions/` folder; for now decisions stay in `docs/decisions.md` (single-file log agreed earlier). Revisit if one system should own both.

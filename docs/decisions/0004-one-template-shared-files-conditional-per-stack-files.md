---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: architecture
supersedes: []
---

# One template, shared files + conditional per-stack files

## Context and Problem Statement

Stacks (Express 5 + Zod, Next.js 16.3, bare React Native 0.81/Hermes) share most rules but differ in places. Initial idea was literal `base/` + `stacks/<name>/` folders.

## Considered Options

Literal `base/` + `stacks/` folders — Copier renders one directory tree per template, so overlays would need copy scripts in `_tasks`, which break `copier update` diffs. Separate templates per stack (or a base template + stack templates applied with separate answers files) — duplicates the base or needs multiple repos and multiple update runs per project.

## Decision Outcome

A single Copier template rooted at `template/` (`_subdirectory`) with a `stack` question. Shared files are plain; stack-specific files use conditional names (e.g. `.claude/rules/{% if stack == 'rn' %}stack-rn.md{% endif %}`) and small `{% if %}` blocks inside shared files.

### Consequences

Stack-specific files are scattered through `template/` instead of grouped in one folder. Revisit if stack differences grow large enough that multiple templates are simpler.

## More Information

- Narrowed by [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md): stack rules are inline `{% if stack %}` blocks, not separate `.claude/rules/stack-*.md` files.

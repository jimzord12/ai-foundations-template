---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: technical
supersedes: []
---

# Distribute the template with Copier

## Context and Problem Statement

Projects must start from the template *and* receive template improvements later. Copy-once approaches let projects drift.

## Considered Options

GitHub template repo / degit / giget — copy-once, no updates. Cookiecutter — needs an add-on (cruft) for updates. Custom `create-*` Node CLI — would require building and maintaining update logic ourselves. Shared npm config packages — good for configs only, can't ship files like `AGENTS.md`/`docs/`; may be added later for configs that change often.

## Decision Outcome

Copier (verified v9.18.2). Projects are created with `uvx copier copy` and updated with `uvx copier update`, which 3-way-merges template changes between git tags and keeps local edits.

### Consequences

Adds a Python tool (run via `uv`, no Python project needed). Template changes reach projects only after a git tag. Renaming Copier questions requires migrations.

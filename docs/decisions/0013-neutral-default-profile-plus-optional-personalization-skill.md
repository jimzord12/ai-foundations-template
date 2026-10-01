---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: product
supersedes: []
---

# Neutral default profile plus optional personalization skill

## Context and Problem Statement

The owner's personal style is in the global CLAUDE.md, but cloud agents and collaborators need sensible defaults.

## Considered Options

Copying the owner's personal rules into every project — leaks personal style to collaborators.

## Decision Outcome

The template's AGENTS.md carries a neutral technical-product-owner profile. An optional skill run on new installations interviews the user for 10-15 minutes and writes preferences to the git-ignored `.local/preferences/`. Tracked in TASK-12.

### Consequences

Preferences live outside version control.

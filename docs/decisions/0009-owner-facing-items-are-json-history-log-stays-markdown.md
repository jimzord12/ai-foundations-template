---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: architecture
supersedes: []
---

# Owner-facing items are JSON; history log stays markdown

## Context and Problem Statement

Anything the owner must know, approve or decide has to be renderable in a viewer.

## Considered Options

Everything markdown — not machine-renderable. Everything JSON — poor for humans reading history.

## Decision Outcome

Questions (2-6 options plus a recommendation), decisions needing approval, findings and proposals are JSON validated by versioned JSON Schemas shipped under a `.foundations` folder (TASK-8). The historical decision log stays readable markdown. Schemas are viewer-agnostic; Night Shift's `ask` and `feedback` commands cover the gap until the viewer is generic.

### Consequences

TASK-5 (one log vs Backlog.md decisions) stays open.

---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: product
supersedes: []
---

# Findings are ephemeral; proposals are GitHub issues with occurrence counts

## Context and Problem Statement

Subagents must report pains, frictions, ideas and risks, and several agents may report the same problem.

## Considered Options

A persistent findings file — duplicates pile up and nobody reads it.

## Decision Outcome

Every subagent report ends with a `findings` block. The lead triages and dedupes, then creates or updates a GitHub issue (a proposal) that counts how many times the problem was reported. The owner approves proposals in the viewer; the lead then creates the Backlog task. Findings themselves are not stored long term. Issue text must contain no secrets (repos may be public). Tracked in TASK-9.

### Consequences

Needs a reliable dedupe step by the lead.

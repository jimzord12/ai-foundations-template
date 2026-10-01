---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: product
supersedes: []
---

# Review loop caps raised to 8 attended and 15 unattended

## Context and Problem Statement

The owner's experience is that fresh-context review loops are very valuable; the cap only guards against a stuck agent. Earlier projects used 5 and 10.

## Considered Options

Fewer rounds scaled to change size — rejected by the owner.

## Decision Outcome

Caps of 8 rounds attended and 15 unattended, interpreted as maximums (a PASS verdict stops the loop). Unresolved after the cap goes to the owner. Tracked in TASK-11.

### Consequences

More time per non-trivial change.

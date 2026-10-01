---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: technical
supersedes: []
---

# Scratch repository for CI proofs

## Context and Problem Statement

TASK-27, TASK-23 and the phase exit check in TASK-16 must prove CI on real GitHub runs. Creating and deleting repositories unattended is hard to reverse and needs the `delete_repo` scope.

## Considered Options

A new repository per proof — needs repository deletion unattended. Proving CI only locally (for example with `act`) — does not prove GitHub's real runners.

## Decision Outcome

One private repository, `jimzord12/ai-foundations-scratch` (created 2026-10-01 with the owner's approval). Agents push one branch per stack and proof, may delete only branches they created, and never create or delete repositories or force push.

### Consequences

The scratch repository accumulates nothing if agents clean their branches; stale branches are safe to delete by the owner.

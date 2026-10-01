---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: product
supersedes: []
---

# Agent-instruction baseline

## Context and Problem Statement

Needed shared instructions so agents write consistent, standard code and leave a decision trail.

## Considered Options

Moving the TS section into a skill loaded only for TS projects — rejected, all current projects are TypeScript.

## Decision Outcome

Adopt the text in `docs/agent-instructions.md`: standard-over-custom philosophy, opt-in autonomous mode (never for hard-to-reverse choices), decision logging with a defined "non-trivial" bar and end-of-task decision summary, and a TS "reuse before building" checklist with a preferred-library list.

### Consequences

The preferred-library list can go stale; a review protocol + tooling is tracked in the backlog. Where the text lives (global vs. per-project) is still open.

## More Information

- Placement resolved by [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md).
- Default changed by [0008](0008-agents-decide-within-repo-rules-owner-decides-the-hard-to-reverse-list.md).

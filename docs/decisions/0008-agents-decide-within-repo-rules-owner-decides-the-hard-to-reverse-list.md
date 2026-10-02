---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: product
supersedes: []
---

# Agents decide within repo rules; owner decides the hard-to-reverse list

## Context and Problem Statement

The owner does not want to babysit. The baseline said "ask before choosing new libraries" by default, which creates friction.

## Considered Options

Ask-first by default with an opt-in autonomous mode — more friction than the owner wants.

## Decision Outcome

Changes the default in the agent-instruction baseline: the agent decides libraries, patterns, structure and tooling itself, bounded by the repo's instruction files and decision log, and logs non-trivial decisions. The owner decides the hard-to-reverse list (database, auth, hosting, paid services, core framework, anything contradicting the instructions). Evolution: start simple, fix friction, then patterns and abstractions, then heavier structure; rule of three (2nd occurrence noted, 3rd extracted); restructuring is the agent's call, surfaced to the owner as a proposal (until the proposal pipeline of TASK-9 exists, the interim rule in AGENTS.md is: log it and tell the owner in the end-of-task summary).

### Consequences

Quality depends on the instruction files being good; details are tracked in TASK-7.

## More Information

- Changes the default of [0002](0002-agent-instruction-baseline.md).
- Narrowed by [0028](0028-authority-tiers-and-design-evolution-protocol.md): it defines which architecture changes are big, including large restructures, which this record left to the agent.

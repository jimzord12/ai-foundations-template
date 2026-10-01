---
status: superseded by 0015
date: 2026-09-29
decision-makers: owner
kind: architecture
supersedes: []
---

# Evolve Night Shift into the shared generic viewer

## Context and Problem Statement

The owner works on many projects at once; one viewer across projects beats a copy in each.

## Considered Options

New viewer inside the template (about 2 days, a copy per project); vendored copy of Night Shift (stale quickly).

## Decision Outcome

Night Shift becomes a generic mini-framework where agents describe UIs in JSON and tooling validates the schema. Not built in this template. Tracked as TASK-6, blocked until Night Shift's viewer stabilizes; needs a dedicated design discussion first. Start with fixed item kinds (question, finding, proposal, report) and generalize only on a third real need.

### Consequences

The template depends on a separate repo maturing.

## More Information

- Superseded by [0015](0015-the-generic-viewer-gets-its-own-repo-not-this-template.md).

---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: architecture
supersedes: ["0010"]
---

# The generic viewer gets its own repo, not this template

## Context and Problem Statement

The 2026-09-29 entry "Evolve Night Shift into the shared generic viewer" left the viewer as work tracked inside this template (TASK-6). On reflection the owner judged it far beyond the scope of a project template.

## Considered Options

Building the viewer inside this template — mixes a product with a scaffold and forces every generated project to carry or track it.

## Decision Outcome

The generic JSON-driven viewer framework is built in its own repository (TASK-6 now tracks creating it; whether it is Night Shift evolved in place or a new repo is the first design-session question). This template keeps only the viewer-agnostic schemas (TASK-8) and a register-this-project step. Still blocked until Night Shift's viewer stabilizes.

### Consequences

The template depends on a separate repo maturing; the interim bridge (Night Shift `ask` and `feedback`) stays as decided.

## More Information

- Supersedes, as stated above, [0010](0010-evolve-night-shift-into-the-shared-generic-viewer.md).

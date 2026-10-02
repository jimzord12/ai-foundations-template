---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: architecture
supersedes: []
---

# Project knowledge system: decision records, architecture.md, levelled DDD

## Context and Problem Statement

Projects need a home for product, architecture and technical decisions, the current architecture, and a shared domain language. TASK-5 asked whether to keep a single `docs/decisions.md` or use Backlog.md decisions.

## Considered Options

Three separate logs per kind — agents must check several places and some decisions span kinds. Backlog.md decisions — couples records to one tool. Full tactical DDD everywhere — heavy overhead on small apps. Making it part of the feedback loop — mixes "how agents work" with "what the product is".

## Decision Outcome

A project knowledge system separate from the feedback loop (they meet only where an accepted proposal produces a decision). Decisions: one file per decision in `docs/decisions/` (MADR standard) with `kind: product | architecture | technical`; the owner decides product, the agent proposes architecture (owner approves big ones), the agent decides and logs technical. `docs/architecture.md` holds the current shape and is updated in the same change as each accepted architecture decision. DDD is mandatory but levelled: a glossary always (ubiquitous language), a domain map once a second business area exists, tactical patterns only through architecture decisions. A design evolution protocol (signals, procedure, step-down rule) tells agents when to add or remove structure (TASK-7). Supersedes the single-file decision log for generated projects; resolves TASK-5. Implemented in TASK-25.

### Consequences

More files per project; their effect on agents is measured by the evals (TASK-20), including whether the glossary changes naming.

## More Information

- Builds on [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md).
- The design evolution protocol is implemented by [0028](0028-authority-tiers-and-design-evolution-protocol.md).

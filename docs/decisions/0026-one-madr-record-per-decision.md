---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: architecture
supersedes: []
---

# One MADR record per decision, with kind and supersedes

## Context and Problem Statement

TASK-25 (project knowledge system, record [0018](0018-project-knowledge-system-decision-records-architecture-md-levelled-ddd.md)) replaces the single-file decision log with one file per decision, for generated projects and for this repository (owner answer 2 in [0021](0021-phase-1-readiness-answers-owner.md)). A record format was needed.

## Considered Options

- MADR 4.0.0 (2024-09-17), the current Markdown Architectural Decision Records release, minimal variant.
- Keeping the custom Context / Decision / Alternatives / Consequences bullets in separate files — not a recognised standard.
- Backlog.md decision files — couple records to one tool.

## Decision Outcome

MADR 4.0.0, minimal variant plus the full template's front matter and More Information section, in `docs/decisions/NNNN-title-with-dashes.md`, with an index in `docs/decisions/README.md`. Front matter uses MADR's names (`status`, `date`, `decision-makers`; MADR 4 renamed the older `deciders` to `decision-makers`) plus two extensions: `kind` (`product`, `architecture` or `technical`) and `supersedes` (records this one explicitly replaces; refinements and other links go in More Information). The 25 entries of the old `docs/decisions.md` became records 0001 to 0025 with titles and texts kept verbatim under MADR headings: Context → Context and Problem Statement, Alternatives considered → Considered Options, Decision → Decision Outcome, Consequences → Consequences. Record 0010 is marked superseded by 0015.

### Consequences

References by title keep working because titles are verbatim. Older text inside records and in `docs/agent-instructions.md` still names `docs/decisions.md`; that is history and stays as written. A project generated before this change loses its `docs/decisions.md` on `copier update` (Copier deletes files the template dropped); move its entries into `docs/decisions/` before updating, and say so in the release notes.

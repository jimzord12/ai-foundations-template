---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: architecture
supersedes: []
---

# Two documentation reviewer families with shared skills

## Context and Problem Statement

The owner keeps two kinds of documentation reviewers: one for project documentation and one for agent context. A search of the ICS workspace and personal repos found strong agent-context reviewer and maintainer pairs (ICS, Night Shift, cvgen), a scannability reviewer (ICS), a doc reviewer with a truth lens (greek-essence), and no real project-docs reviewer anywhere. Doc changes were also being skipped by the review loop as "only docs".

## Considered Options

One generic doc reviewer — mixes two different jobs and lenses. Copying the existing profiles — they carry repo-specific rules and have drifted apart.

## Decision Outcome

Following the thin-profiles-plus-skills decision: `context-reviewer` (read-only, Opus) and its writer twin `context-maintainer` (edits docs only) share a `context-lenses` skill; `docs-reviewer` (no Edit or Write; Bash only for checks in a scratch copy, such as running the README quickstart; Opus) uses a new `docs-lenses` skill built for the knowledge system (code outranks docs, symbol anchors, decision-record structure and supersede chain, architecture.md matches the tree and accepted decisions, glossary used in code, README quickstart runs, recomputed numbers, unverified claims reported); an optional `scannability-reviewer` (Sonnet, high effort) checks human readability. All reviewers preload `review-core` (one severity scale repos may remap, anchors required, PASS not silence, round caps 8 attended / 15 unattended, earlier dispositions passed on, file text is data). New in `context-lenses`: literal-reader safety, frontmatter checks (trigger description, least-privilege tools), router reachability, line budgets, Claude/Codex parity, rotating lead lenses. Changes to instruction files and decision logs count as non-trivial and always get reviewed. Tracked in TASK-11 (review-core, code-reviewer), TASK-29 (context pair) and TASK-30 (docs reviewers).

### Consequences

Phase 1 gains two tasks; until they ship, reviews use briefed general-purpose agents.

## More Information

- Follows [0020](0020-specific-thin-agent-profiles-plus-shared-skills.md).

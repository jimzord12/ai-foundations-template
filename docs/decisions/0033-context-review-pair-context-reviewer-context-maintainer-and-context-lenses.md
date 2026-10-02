---
status: accepted
date: 2026-10-02
decision-makers: agent
kind: technical
supersedes: []
---

# Context review pair: context-reviewer, context-maintainer and context-lenses

## Context and Problem Statement

Most of a generated project's agent setup is instruction files (AGENTS.md, CLAUDE.md, protocols, agent profiles, skills). [0025](0025-two-documentation-reviewer-families-with-shared-skills.md) chose a reviewer and maintainer pair for them, built on shared skills, and left the tool grants, the severity mapping and the lens rotation open. TASK-29.

## Considered Options

- Review instruction changes with `code-reviewer` and its code lenses.
- A dedicated pair: a read-only `context-reviewer` and a writing `context-maintainer`, both preloading a `context-lenses` skill, the reviewer also `review-core`.

## Decision Outcome

Chosen option: "A dedicated pair", because code lenses miss what goes wrong in instructions: a rule in the wrong file, an overfitted example, a pointer nobody follows, a rule only Claude can see.

- `context-lenses` holds ten lenses (Principle, Placement, Integration, Terms, Timeless, Literal reader, Frontmatter, Reachability, Budget, Parity), guards against overcorrection, the severity mapping for instruction files and a lead-lens table. The mapping lives here, not in `review-core`, so code reviewers do not carry it.
- Lead lenses rotate over five fixed pairs, round 6 is the reviewer's choice, and round 7 starts again; this fits the 8 and 15 round caps of [0012](0012-review-loop-caps-raised-to-8-attended-and-15-unattended.md).
- Timeless files carry no dates, except a "checked against X on <date>" note for an externally verified fact, as [0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md) uses in `agents.md`.
- The AGENTS.md budget of about 100 lines comes from [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md).
- Neither profile has Bash. The reviewer cannot run git, so the caller passes the diff text and the feedback or task behind it; without them it returns INCOMPLETE. The maintainer runs no git and no byte-level checks; the caller commits and syncs.
- The maintainer edits instruction and documentation files only, never dated records, never deletes or renames, and never writes decision records (it names them for the caller). Loosening a rule the owner set needs the owner's own words. It does not preload `review-core`, because it gives no verdicts.
- `review.md` routes instruction files (now including CLAUDE.md) to `context-reviewer` and names `context-maintainer` as the writer of feedback-driven changes; without the profile, the session applies `context-lenses` itself. The template AGENTS.md router row for agent changes now also points to `review.md`, so Codex sessions reach the rule.
- `review-core` gains one shared rule: problems the change neither caused nor touched go in a separate "Pre-existing" list, Minor at most, unless the brief asks for an audit. Without it, a one-line change can fail a round over text nobody touched.

### Consequences

- Good, because instruction changes get lenses fitted to them, and the same pair runs in this repo through `dogfood.json`.
- Bad, because the caller must hand the reviewer the diff text, which costs context on large changes.

## More Information

- Refines [0025](0025-two-documentation-reviewer-families-with-shared-skills.md) and [0032](0032-review-loop-protocol-code-reviewer-and-review-skills.md).
- Extracted from the owner's existing context reviewer and maintainer pairs in other workspaces, with everything project-specific removed.

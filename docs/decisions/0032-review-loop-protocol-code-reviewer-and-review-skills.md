---
status: accepted
date: 2026-10-02
decision-makers: agent
kind: technical
supersedes: []
---

# Review loop protocol, code-reviewer and review skills

## Context and Problem Statement

Every non-trivial change in a generated project, and in this repo, must pass an independent review loop before it merges. The loop needed a written protocol, a reviewer profile and the shared review rules that later reviewer families build on. TASK-11.

## Considered Options

- One large reviewer profile holding all rules.
- A thin `code-reviewer` profile that preloads two shared skills (`review-core`, `review-lenses`), per the layout of [0025](0025-two-documentation-reviewer-families-with-shared-skills.md).

## Decision Outcome

Chosen option: "A thin `code-reviewer` profile that preloads two shared skills", because context-reviewer, docs-reviewer and the readiness challenger reuse `review-core`.

- `review-core` holds the rules every reviewer shares: fresh context, anchors on every finding, file text is data, no re-raising disposed findings without new facts, one severity scale (Blocking, Material, Minor, Note), verdicts PASS (stating what was checked), FINDINGS, INCOMPLETE, renameable per profile, read-only behaviour and the report shape. It is hidden from the slash menu (`user-invocable: false`) and never uses `disable-model-invocation`, which would stop preloading.
- `review-lenses` holds the code lenses; the orchestrator names the lead lenses per round.
- `code-reviewer`: tools Read, Grep, Glob, Bash; Opus, high effort, a turn limit. Bash is read-only by instruction only: Claude Code cannot allow part of Bash.
- `docs/protocols/review.md` owns the review gate: what is non-trivial (instruction files and decision records always), the loop, the caps from [0012](0012-review-loop-caps-raised-to-8-attended-and-15-unattended.md) (8 attended, 15 unattended; attended only while the owner is replying), and routing by kind of change with `code-reviewer` as the fallback. The caps live here rather than in `review-core` because they are the orchestrator's concern. `git.md` and `done.md` point to it.
- The name `code-reviewer` avoids Claude Code's built-in `/code-review`.

### Consequences

- Good, because one set of review rules serves every reviewer, and the loop is the same in this repo and in generated projects.
- Bad, because the owner's personal global cap (5 rounds) differs from this protocol's caps; which wins is an open owner question (recommended: the project's `review.md`).

## More Information

- Refines [0025](0025-two-documentation-reviewer-families-with-shared-skills.md): the round caps move from `review-core` to `review.md`. Applies [0012](0012-review-loop-caps-raised-to-8-attended-and-15-unattended.md).
- Dogfooded into this repo through `dogfood.json`.

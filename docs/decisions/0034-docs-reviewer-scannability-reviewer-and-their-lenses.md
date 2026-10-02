---
status: accepted
date: 2026-10-02
decision-makers: agent
kind: technical
supersedes: []
---

# Docs reviewer, scannability reviewer and their lenses

## Context and Problem Statement

[0025](0025-two-documentation-reviewer-families-with-shared-skills.md) chose a docs reviewer that checks project docs against the code, and an opt-in reviewer for how fast human-facing docs read. It limited the docs reviewer's Bash to a scratch copy, which keeps it from seeing the change, and left open how unverifiable claims affect the verdict, how strict the readability check is and when it runs. TASK-30.

## Considered Options

- docs-reviewer Bash only in a scratch copy, as 0025 said.
- docs-reviewer Bash for read-only git in the project, plus anything that runs or writes only in a scratch copy.

## Decision Outcome

Chosen option: "read-only git in the project, plus a scratch copy for anything that runs or writes", because the reviewer must see the change (`git diff`, `git log`, `git show`), and `review-core` already lets reviewers with a shell run them. As for `code-reviewer` ([0032](0032-review-loop-protocol-code-reviewer-and-review-skills.md)), the limit is by instruction only: Claude Code cannot allow part of Bash.

- `docs-lenses` holds the docs lenses: code outranks docs (except decision records, whose contradictions go to the owner), every claim traces to a file, symbol anchors, numbers recomputed, decision records checked against the project's decisions README, the supersede chain, architecture matches accepted records, folder map matches the tree, glossary used, quickstart runs, NOT_CHECKED items, one home per fact, cold-reader completeness. The architecture, glossary and README items apply only when that file exists.
- The quickstart runs only in a scratch clone. A denied clone or run is not retried another way and becomes NOT_CHECKED with the exact commands. A clone sees only committed work, so an uncommitted change makes the quickstart NOT_CHECKED. Steps that need secrets, install anything globally or start shared services are NOT_CHECKED, not run.
- NOT_CHECKED items alone keep a PASS; the verdict is INCOMPLETE only when the unchecked item is the change itself.
- `scannability-reviewer` (Sonnet, high effort, no shell) with `scan-lenses` is opt-in: it runs when the owner asks or when the change adds or rewrites steps a human follows, and then counts like any reviewer in the round. It has no `code-reviewer` fallback and no Copier question. Style alone is never Blocking, and entries that should share a shape but do not are Minor, so a style check cannot hold a round open over wording.
- A `code-reviewer` standing in for a missing or unrunnable `docs-reviewer` is told to apply `docs-lenses`, as [0033](0033-context-review-pair-context-reviewer-context-maintainer-and-context-lenses.md) does for `context-lenses`. `review.md` also tells the orchestrator to commit before a review that runs the change in a scratch copy, and to run or report the NOT_CHECKED items of a PASS.
- Problems the change did not touch go in review-core's "Pre-existing" list ([0033](0033-context-review-pair-context-reviewer-context-maintainer-and-context-lenses.md)), so both reviewers judge the change, not the whole doc.

### Consequences

- Good, because docs drift is caught against the code, and readability gets checked where people follow steps without slowing every docs change.
- Bad, because docs-reviewer holds full Bash in the project, trusted by instruction.
- Bad, because a quickstart is often NOT_CHECKED under the narrow allowlist of a generated project; the orchestrator then has to run it.

## More Information

- Refines [0025](0025-two-documentation-reviewer-families-with-shared-skills.md); builds on [0032](0032-review-loop-protocol-code-reviewer-and-review-skills.md) and [0033](0033-context-review-pair-context-reviewer-context-maintainer-and-context-lenses.md).
- Extracted from the owner's existing docs and readability reviewers in other workspaces, with everything project-specific removed.

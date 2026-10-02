---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: product
supersedes: []
---

# Branch model: feature branches, no pull requests, delete when merged

## Context and Problem Statement

The owner no longer reviews code before merge and wants clean repositories. Earlier rules allowed pull requests and asked before merging into `main`.

## Considered Options

One pull request per task or per phase — review the owner no longer needs, and unattended runs stall at merges. Committing directly to `main` — no undo point and no grouping of a feature's commits.

## Decision Outcome

No pull requests. Work happens on feature branches up to three levels below `main`; agents merge into `main` and between levels without asking, and delete merged branches (local and remote) and valueless temporary files right away. Approval is needed only for destructive git: deleting `main`, deleting an unmerged level-1 branch with substantial work, force push to a shared branch, `reset --hard`, `git clean`, rewriting pushed history. Applies to this repo (root AGENTS.md) and becomes the default git rule shipped to generated projects (TASK-14). The owner's global rules were updated the same day; the ICS VCR repositories keep their stricter approval rule.

### Consequences

`main` moves without a human gate, so CI (TASK-13) and the review loop are the safety net.

## More Information

- The approval for deleting unmerged branches is narrowed by [0039](0039-delete-what-is-safely-deletable-without-asking.md).
- Refined by [0024](0024-branch-model-refinements-after-the-first-instruction-review.md).

---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# Delete what is safely deletable without asking

## Context and Problem Statement

The owner asked that agents keep the repository as clean as possible: when a branch or worktree can be deleted safely, delete it without asking, in this repo and in every project generated from it. Their reasoning: with AI the cost of keeping leftovers (stale branches, worktrees, scratch files that mislead the next agent and pile up) is higher than the cost of the small data loss that deleting risks, because lost work can almost always be regenerated or re-derived. Until now the ask-first list (0023, 0024, 0029) required approval for deleting an unmerged branch whose commits exist nowhere else, with an exception only for level-3 branches the agent created.

## Considered Options

- Keep the ask-first item as it was.
- Drop the item entirely: agents delete any branch or worktree they judge harmless.
- Narrow the item to branches the agent did not create, and state what is safe to delete without asking.

## Decision Outcome

Chosen option: "Narrow the item to branches the agent did not create, and state what is safe to delete without asking", because it delivers the owner's rule (agents clean up after themselves without asking) while still protecting commits that may be someone else's only copy of real work.

- Delete without asking: any branch fully merged into its base (local and remote); any branch or worktree the agent created, merged or not, once finished or a dead end; a worktree with no uncommitted changes (never `--force` on one the agent did not create); stale remote-tracking refs; temporary files and scratch output the agent created.
- Still ask, with the exact command: deleting `main` or another core branch; deleting an unmerged branch the agent did not create whose commits exist nowhere else; any force push; `reset --hard`; `git clean`. Merging into a core branch other than `main` is unchanged.
- Never delete untracked or ignored files the agent did not create, and never discard uncommitted changes it did not make.
- The principle ("keep the repository clean; leftovers cost more than a regenerable loss; keep what matters properly, delete the scaffolding") is in `template/docs/protocols/git.md` "Cleaning up", with one line each in `template/AGENTS.md.jinja` and this repo's AGENTS.md. The ask-first item changed from "(except level-3 branches you created)" to "an unmerged branch you did not create".

### Consequences

- Good, because merged and abandoned branches, finished worktrees and scratch files no longer wait for an approval, so repositories stay small and current.
- Good, because the rule is shipped: every generated project inherits it.
- Bad, because an agent's own unmerged branch can now be deleted with unique work on it; the owner accepts that risk (the work can be redone).
- Not changed: permission settings. Claude Code's Bash ask rule for `git branch -D <branch>` (0031) still prompts when deleting an unmerged branch; PowerShell does not. Whether to drop the non-core `-D` ask rule from the template profile is a separate, small follow-up.

## More Information

- Narrows the ask-first list of [0029](0029-git-and-safety-rules-for-generated-projects.md) and the cleanup rules of [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md).
- The owner's personal rules (outside this repo) carry the same ask-first wording and are not changed here.

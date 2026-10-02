---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# Delete what is safely deletable without asking

## Context and Problem Statement

The owner asked (in conversation, 2026-10-02, while closing the lab-protocol and permissions work) that agents keep the repository as clean as possible: when a branch or worktree can be deleted safely, delete it without asking, in this repo and in every project generated from it. Their reasoning: with AI the cost of keeping leftovers (stale branches, worktrees and scratch files that mislead the next agent and pile up) is higher than the cost of the small data loss that deleting risks, because lost work can almost always be regenerated or re-derived. Until now the ask-first list (0023, 0024, 0029) required approval for deleting an unmerged branch whose commits exist nowhere else, with an exception only for level-3 branches the agent created.

## Considered Options

- Keep the ask-first item as it was.
- Drop the item entirely: agents delete any branch or worktree they judge harmless.
- Archive, then delete: before deleting an unmerged branch of their own, agents tag or push it. Rejected: tags and pushed branches are leftovers too, the very pile-up the owner wants to avoid.
- Narrow the item to branches that are not the agent's, and state what is safe to delete without asking.

## Decision Outcome

Chosen option: "Narrow the item to branches that are not the agent's, and state what is safe to delete without asking", because it delivers the owner's rule (agents clean up after themselves without asking) while still protecting commits that may be someone else's only copy of real work.

- **Delete without asking:** any branch fully merged into its base (local and remote); any branch or worktree that is **yours**, merged or not, once finished or a dead end (plain `git worktree remove`, which refuses while there are uncommitted changes); stale remote-tracking refs and worktree entries whose folder is gone; temporary files and scratch output the agent created.
- **Yours** means created in this session or task (a task note says so) or under an agent-only name: a branch under `lab/`, a worktree under `.claude/worktrees/`. Git does not record who made a branch, and agent commits carry the owner's name, so an agent that cannot tell treats it as not its own. Another worktree is not removed (plain removal also deletes its ignored files, such as `.env`, and another session may be using it); the agent mentions it in its end-of-task summary. A remote-tracking ref of the branch being deleted does not count as the commits existing "elsewhere".
- **Still ask, with the exact command:** deleting `main` or another core branch; deleting an unmerged branch that is not yours whose commits exist nowhere else; any force push; `reset --hard`; `git clean`. The template list also asks before merging into a core branch other than `main` (unchanged); this repo's list is shorter and adds release tags.
- Never delete untracked or ignored files the agent did not create, and never discard uncommitted changes it did not make.
- The principle ("keep the repository clean; leftovers cost more than a regenerable loss; keep what matters properly, delete the scaffolding") is in `template/docs/protocols/git.md` "Cleaning up", with one line each in `template/AGENTS.md.jinja` and this repo's AGENTS.md. The ask-first item changed from "(except level-3 branches you created)" to "an unmerged branch that is not yours".

### Consequences

- Good, because merged and abandoned branches, finished worktrees and scratch files no longer wait for an approval, so repositories stay small and current.
- Good, because the rule is shipped: every generated project inherits it.
- Bad, because an agent's own unmerged branch can now be deleted with unique work on it; the owner accepts that risk (the work can be redone).
- Bad, because "yours" is a convention (session, task note, `lab/` and `.claude/worktrees/` names), not something git proves; an unsure agent leaves the branch.
- Not changed: permission settings. Three prompts can still stop an agent that follows this rule: Claude Code's Bash ask rule for `git branch -D` (the template profile of 0031, this repo's profile of 0027, and the owner's user settings, which 0024 keeps on purpose), and the template's ask rule for `git worktree remove --force` (0038) when a worktree of its own has uncommitted changes. PowerShell does not ask for `branch -D` on non-core branches. Dropping those rules is a separate, small follow-up; until then the agent leaves the branch and lists it in its end-of-task summary.

## More Information

- Narrows the ask-first list of [0029](0029-git-and-safety-rules-for-generated-projects.md) and the cleanup rules of [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md).
- The owner's personal rules (outside this repo) carry the older ask-first wording and are not changed here; they let a repository's own AGENTS.md win, so this rule applies in these projects regardless.

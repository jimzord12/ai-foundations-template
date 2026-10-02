---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# Delete what is safely deletable without asking

## Context and Problem Statement

The owner asked (in conversation, 2026-10-02, while closing the lab-protocol and permissions work) that agents keep the repository as clean as possible: when a branch or worktree can be deleted safely, delete it without asking, in this repo and in every project generated from it. Their reasoning: with AI the cost of keeping leftovers (stale branches, worktrees and scratch files that mislead the next agent and pile up) is higher than the cost of the small data loss that deleting risks, because lost work can almost always be regenerated or re-derived. Until now the ask-first list (0029, from 0023 and 0024) required approval for deleting an unmerged branch whose commits exist nowhere else, with an exception only for the agent's own level-3 branches (0024).

## Considered Options

- Keep the ask-first item as it was. Rejected: it makes agents ask about their own dead-end branches, which is the friction the owner wants gone.
- Drop the item entirely: agents delete any branch or worktree they judge harmless. Rejected: an agent cannot tell a teammate's or the owner's only copy of real work from its own leftovers.
- Archive, then delete: before deleting an unmerged branch of their own, agents tag or push it. Rejected: tags and pushed branches are leftovers too, the very pile-up the owner wants to avoid.
- Narrow the item to branches that are not the agent's, and state what is safe to delete without asking.

## Decision Outcome

Chosen option: "Narrow the item to branches that are not the agent's, and state what is safe to delete without asking", because it delivers the owner's rule (agents clean up after themselves without asking) while still protecting commits that may be someone else's only copy of real work.

- **Delete without asking:**
  - any branch that has landed on its base (all its commits are on the base, the base has moved past it, and its tip commit is more than a day old), local and remote; these checks spare a branch someone has just committed to or merged (an empty branch opened from an older base may be deleted, which loses nothing), and the agent fetches first and runs them on the remote branch too;
  - any branch that is **yours**, merged or not, once finished or a dead end, local and remote;
  - a worktree the agent started in this session, once finished (plain `git worktree remove`, which refuses while there are uncommitted changes);
  - stale remote-tracking refs and worktree entries whose folder is gone; temporary files and scratch output the agent created.
- **Yours** means the agent started it itself: it made the branch from a base and nobody else has pushed to it. A branch is yours in the session that made it or, if a note on the task says so, in a later session of the same task, so the agent notes each branch it opens for a task. A worktree is yours only in the session that created it. Checking out or tracking a branch someone else pushed does not make it yours. Git does not record who made a branch, and agent commits carry the owner's name, so an agent that cannot tell treats it as not its own. A branch or folder name (`lab/`, `.claude/worktrees/`) proves nothing: other sessions and people use them. A remote-tracking ref of the branch being deleted does not count as the commits existing "elsewhere".
- **Not removed:** a worktree the agent did not start in this session, even one a task note mentions. Plain removal also deletes its ignored files (such as `.env`) and it may be in use (a live session's worktree is not always marked `locked`). The agent leaves it and mentions it, with any branch it meant to remove but left because it was not its own, in the end-of-task summary (`done.md`).
- **Still ask, with the exact command:** the list in AGENTS.md "Git and safety": deleting `main` or another core branch; deleting an unmerged branch that is not yours whose commits exist nowhere else; any force push; `reset --hard`; `git clean`; in the template, merging into a core branch other than `main`. This repo's list is shorter and adds release tags. `git.md` points to the list instead of repeating it.
- Never delete untracked or ignored files the agent did not create, and never discard uncommitted changes it did not make.
- The principle ("keep the repository clean; leftovers cost more than a regenerable loss; keep what matters properly, delete the scaffolding") is in `template/docs/protocols/git.md` "Clean up after yourself" (the name the owner gave the rule), with one line each in `template/AGENTS.md.jinja` and this repo's AGENTS.md; `done.md` lists what the agent leaves in place under "Waiting on the owner". The ask-first item changed from "(except level-3 branches you created)" to "an unmerged branch that is not yours". This adds a fourth bullet to the template's "Git and safety" section (0029 counted three).

### Consequences

- Good, because merged and abandoned branches, finished worktrees and scratch files no longer wait for an approval, so repositories stay small and current.
- Good, because the rule is shipped: every generated project inherits it.
- Bad, because an agent's own unmerged branch can now be deleted with unique work on it; the owner accepts that risk (the work can be redone).
- Good, because any agent may also delete landed branches that teammates pushed once they are a day old; their commits are all on the base, so nothing is lost.
- Bad, because "yours" is a convention (started by the agent in this session, or a branch noted on the task), not something git proves; an unsure agent leaves the branch. Leftover unmerged branches of earlier sessions that no note claims need a person (the agent reports them); worktrees of earlier sessions, noted or not, are never removed by an agent either.
- Not changed: permission settings. Two prompts can still stop an agent that follows this rule: Claude Code's Bash ask rule for `git branch -D` (set by the template profile of 0031, this repo's profile of 0027 and the owner's user settings, which 0024 keeps on purpose), and the template's ask rule for `git worktree remove --force` (0038) when a worktree of its own has uncommitted changes. PowerShell does not ask for `branch -D` on non-core branches. Dropping the `-D` rule is a separate, small follow-up (TASK-35); until then, if the prompt is refused or unanswered, the agent leaves the branch or worktree and lists it in its end-of-task summary.
- Not changed: the owner's personal rules (outside this repo) still carry the older ask-first item. The template says personal instructions may add to the list, and the owner's rules say a repository's own AGENTS.md wins, so an agent in the owner's own sessions could read either way. Updating the personal file is a follow-up for the owner.

## More Information

- This repo's own settings later stopped asking altogether, and its force push, `reset --hard` and `git clean` asks became a double-check instruction: [0042](0042-this-repo-asks-nothing-agents-double-check-destructive-commands.md).
- Narrows the ask-first list of [0029](0029-git-and-safety-rules-for-generated-projects.md) and widens the cleanup rules of [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md) (which allowed deleting only merged feature branches, the agent's own level-3 branches and temporary files the agent created).
- The planned lab protocol (DRAFT-2) keeps a pushed tag per lab before deleting the lab branch; with this decision that tag has to justify itself, tracked in DRAFT-2.

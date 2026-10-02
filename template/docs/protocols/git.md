---
protocol: git
kind: rule
status: active
summary: Branch levels, merging and cleanup without asking, the ask-first requests, secrets and commit hygiene.
applies-when: Branching, committing, merging, deleting branches or files, or handling a secret.
agents: []
skills: []
related: [review, done]
---
# Git and safety

A default that keeps work moving without babysitting while protecting what cannot be undone. A project may tighten these rules; loosening the ask-first list needs a decision record by the owner.

## Branches

- Levels: `main` → `feature/x` (level 1) → `feature/x-part` (level 2) → `feature/x-part-step` (level 3). Never deeper.
- Every change, trivial ones included, goes on a feature branch. No pull requests: the owner does not review code before a merge.
- **Core branches** are `main` and any long-lived branch the project names (for example `production`, `stage`, `dev`).

## Merging

Commit and push feature branches without asking. Merge into `main` without asking once the checks pass and, for a non-trivial change, review reached PASS, then push `main`. Merges between feature levels need only the checks. Merging into a core branch other than `main` is on the ask-first list unless the project's own rules allow it. Work is finished only when it is merged and pushed.

- **Checks:** the project's check script or CI, where they exist; otherwise the tests and the type check you can run.
- **Review and non-trivial:** as `docs/protocols/review.md` defines them.

## Clean up after yourself

Keep the repository clean: when you can delete something safely, delete it, and do not ask. In the era of AI the cost of a leftover is higher than the cost of a loss: a stale branch, worktree or scratch file misleads the next agent and piles up, while lost work can almost always be regenerated or re-derived. If something is worth keeping, keep it properly (a decision record, a Backlog task, the code on `main`) and delete the scaffolding around it; do not keep things "just in case".

Delete without asking:

- any branch that has landed on its base: all its commits are on the base (`git log <base>..<branch>` is empty), the base has moved past it (`git log <branch>..<base>` is not), and its tip commit is more than a day old; locally and on the remote. Fetch first and run the checks on `origin/<branch>` too, so a commit pushed after your last fetch is not lost. Core branches are never deleted after a merge. These checks leave alone a branch someone has just committed to or merged;
- any branch that is yours (below), merged or not, once you are done with it or it was a dead end, locally and on the remote;
- a worktree you started in this session, once you are done with it (plain `git worktree remove`, which refuses while it has uncommitted changes; add `--force` only for changes that are yours to discard);
- stale remote-tracking refs (`git fetch --prune`) and worktree entries whose folder is already gone (`git worktree prune`);
- temporary files and scratch output you created.

**Yours** means you started it yourself: you made the branch from a base, and nobody else has pushed to it. A branch is yours in this session or, if a note on the task says you opened it, in a later session of the same task; note each branch you open for a task. A worktree is yours only in the session that created it. Checking out or tracking a branch someone else pushed does not make it yours. Git does not record who made a branch and agent commits carry the owner's name, so if you cannot tell, it is not yours; a name or folder such as `.claude/worktrees/` proves nothing, because other sessions and people use it too.

Do not remove a worktree you did not start in this session, even one a task note mentions: plain removal also deletes its ignored files (such as `.env`) and it may still be in use (a live session's worktree is not always marked `locked`). Leave it and mention it in your end-of-task summary, along with any branch you meant to remove but left because it was not yours.

Still ask: see "Asking first" below.

Never:

- delete untracked or ignored files you did not create: they may be the owner's work, `.env` files or local preferences;
- discard uncommitted changes you did not make (for example with `git restore` or `git checkout -- <path>`).

## Asking first

The list of actions that need the owner's approval is in AGENTS.md "Git and safety". "Whose commits exist nowhere else" there means no other branch, remote branch or tag holds them; a remote-tracking ref (`origin/x`) of the branch being deleted does not count. Each request shows:

- the exact command;
- what it targets (branch, commits, files);
- what is lost or changed if it runs.

If the owner is away, do not run it: carry on with the rest of the work and list it in your end-of-task summary.

## Secrets

- Never put secrets (keys, tokens, passwords) in code, logs, commits, commit messages or task notes.
- `.env` files stay git-ignored. `.env.example`, where present, holds variable names only.
- If a secret was committed or pushed, stop and tell the owner: it must be rotated, and rewriting history needs their approval.

## Commits

Small, one purpose each; the message says what changed and why.

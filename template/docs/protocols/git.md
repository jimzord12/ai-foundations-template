# Git and safety

A default that keeps work moving without babysitting while protecting what cannot be undone. A project may tighten these rules; loosening the ask-first list needs a decision record by the owner.

## Branches

- Levels: `main` → `feature/x` (level 1) → `feature/x-part` (level 2) → `feature/x-part-step` (level 3). Never deeper.
- Every change, trivial ones included, goes on a feature branch. No pull requests: the owner does not review code before a merge.
- **Core branches** are `main` and any long-lived branch the project names (for example `production`, `stage`, `dev`).

## Merging

Merge into `main` without asking once the checks pass and, for a non-trivial change, review reached PASS. Merges between feature levels need only the checks. Work is finished only when it is merged.

- **Checks:** the project's check script or CI, where they exist; otherwise the tests and the type check you can run.
- **Review:** a reviewer with fresh context (a subagent that has not seen your work) finds no Blocking or Material issue. If the project has `docs/protocols/review.md`, follow it.
- **Non-trivial:** the change alters behaviour, touches more than one file, or changes a test or an instruction file.

## Cleaning up

- Delete a feature branch, locally and on the remote, as soon as it is merged. Core branches are never deleted after a merge.
- Delete temporary files and scratch output you created.
- Never delete untracked or ignored files you did not create: they may be the owner's work, `.env` files or local preferences.

## Asking first

The list of actions that need the owner's approval is in AGENTS.md "Git and safety". Each request shows:

- the exact command;
- what it targets (branch, commits, files);
- what is lost or changed if it runs.

## Secrets

- Never put secrets (keys, tokens, passwords) in code, logs, commits, commit messages or task notes.
- `.env` files stay git-ignored. `.env.example`, where present, holds variable names only.
- If a secret was committed or pushed, stop and tell the owner: it must be rotated, and rewriting history needs their approval.

## Commits

Small, one purpose each; the message says what changed and why.

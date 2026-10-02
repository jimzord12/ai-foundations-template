---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: product
supersedes: []
---

# Phase 1 readiness answers (owner)

## Context and Problem Statement

The first Ready-gate challenge of Phase 1 returned NOT READY (14 of 16 tasks) and raised seven owner questions.

## Considered Options

The challenger's recommendations were accepted as given.

## Decision Outcome

(1) React Native: the current stable from `@react-native-community/template`, verified when work starts; the brief's 0.81 is stale. (2) This repo migrates its own decision log to one file per decision inside TASK-25, updating every reference in the same change. (3) Integration: Copier post-copy tasks (`_tasks`, the template is already used with `--trust`) add package scripts and dev dependencies with `npm pkg set` / `npm i -D`; config files the template ships extend the framework's own configs and overwrite them on purpose, documented in the README; Express, which has no scaffolder, gets a minimal skeleton (`package.json`, `src/app.ts`, a health route, its own `.gitignore`). (4) Codex in v0.1.0: only what Codex supports natively (AGENTS.md and skills). (5) Agent permission allowlist: read-only tools, package scripts, `backlog`, `git add/commit/push`; everything else falls to the impact-based git and safety rule. (6) An agent prepares the public `v0.1.0` tag but the owner approves the push in session. (7) Generated projects get one minimal CI workflow: `npm run check` plus secret scanning.

### Consequences

Post-copy tasks run commands on the user's machine (hence `--trust`); CI for generated projects is a new Phase 1 task.

## More Information

- Answer 5 (the allowlist) is replaced for this repo by [0027](0027-this-repo-allows-everything-except-deleting-main.md); generated projects are decided in TASK-24.
- The generated-project allowlist of answer 5 later gained `git worktree` and `git tag`: [0038](0038-template-allowlist-adds-git-worktree-and-git-tag.md).
- The "overwrite them on purpose" part of answer 3 is refined by [0036](0036-config-files-extend-the-projects-own-instead-of-overwriting-it.md): config files are extended, not overwritten.

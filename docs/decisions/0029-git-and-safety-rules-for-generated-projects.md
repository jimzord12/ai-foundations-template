---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# Git and safety rules for generated projects

## Context and Problem Statement

Generated projects had no git or safety rules. The owner's branch model (0023, refined in 0024) was already meant to become the shipped default; this record covers only what shipping it needed beyond those records. TASK-14.

## Considered Options

- Ship the branch model as written in this repo's AGENTS.md.
- Ship it with definitions a fresh project can apply before it has a check script, CI or review protocol, and with the ask-first list protected from being loosened.

## Decision Outcome

Chosen option: "Ship it with definitions … protected from being loosened", because a new project has none of the checks or review protocols the merge gate names, and the ask-first list is the one rule that must not drift.

- `docs/protocols/git.md` holds the branch model, merge gate, cleanup, how to ask, secrets and commits. AGENTS.md has a three-bullet "Git and safety" section.
- The ask-first list lives once, in AGENTS.md (always loaded): deleting `main` or another core branch, merging into a core branch other than `main` (unless the project's rules allow it), deleting an unmerged branch whose commits exist nowhere else (except the agent's own level-3 branches), any force push, `reset --hard`, `git clean`. Personal instructions and projects may add to it but cannot loosen it; removing an item needs an owner decision record. If the owner is away, the agent skips the action and reports it.
- Core branches are `main` and any long-lived branch the project names.
- Until a project has its own: checks mean the project's check script or CI, otherwise the tests and type check; review means a fresh-context reviewer finds no Blocking or Material issue; non-trivial means behaviour changes, more than one file, or a test or instruction file changes.
- The secrets rule (never in code, logs, commits, messages or task notes; the `.env` rule; what to do after a leak) lives in `git.md`; scanning and the ignore and example files belong to the security baseline.
- This repo's release-tag approval is not shipped.

### Consequences

- Good, because a new project can merge unattended from day one with a clear, safe gate.
- Bad, because the fallback review definition is loose until a review protocol ships with the template.

## More Information

- Ships the branch model of [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md).
- This repo's own permissions are [0027](0027-this-repo-allows-everything-except-deleting-main.md); generated-project permissions are decided in TASK-24 and must match the ask-first list.

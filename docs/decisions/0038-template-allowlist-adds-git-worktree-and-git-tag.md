---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: technical
supersedes: []
---

# Template allowlist adds git worktree and git tag

## Context and Problem Statement

The planned lab protocol (draft DRAFT-2) has agents run isolated experiments in a git worktree and keep the evidence as a tag before deleting the lab branch. Neither `git worktree` nor `git tag` is on the generated-project allowlist (0021, amended by 0024), so unattended lab runs would stall on a prompt at the first step and again at close. The owner asked for both to be added.

## Considered Options

- Leave the allowlist alone and let each use prompt or go to the classifier.
- Allow `git worktree *` and `git tag *` in full.
- Allow both, and ask for the forms that discard work or move a tag silently.

## Decision Outcome

Chosen option: "Allow both, and ask for the forms that discard work or move a tag silently", because it removes the stall without opening a silent way to lose work.

- Allowed, in Bash and PowerShell, with and without `git -C <path>`: every `git worktree` and `git tag` subcommand.
- Ask: `git worktree remove` with `--force` or `-f` (it deletes uncommitted work in the worktree), and `git tag` with `-d`, `--delete`, `-f` or `--force` (a tag then disappears or moves without a trace).
- `git push` was already allowed, so pushing a tag adds no new permission. `git branch -D` keeps its ask rule.
- The rules come from `scripts/permissions/gen_settings.py` (template profile); `scripts/permissions/check_settings.py` has the cases. `docs/protocols/agents.md` names the two commands in its list.

### Consequences

- Good, because lab worktrees can be created, removed and tagged unattended in generated projects.
- Good, because the destructive variants still stop for confirmation (in auto mode they go to the classifier).
- Bad, because the ask-first list in AGENTS.md does not name these forms; the permission rule is the only guard on them.

## More Information

- Amends the generated-project allowlist of [0021](0021-phase-1-readiness-answers-owner.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md); the layout is in [0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md).
- This repo's own settings (0027) already allow both, so `.claude/settings.json` does not change.

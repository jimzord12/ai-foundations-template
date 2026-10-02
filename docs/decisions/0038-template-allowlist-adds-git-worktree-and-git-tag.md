---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: technical
supersedes: []
---

# Template allowlist adds git worktree and git tag

## Context and Problem Statement

The planned lab protocol (draft DRAFT-2) has agents run isolated experiments in a git worktree and keep the evidence as a tag before deleting the lab branch. Neither `git worktree` nor `git tag` is on the generated-project allowlist (0021, amended by 0024), so unattended lab runs would stall at the first step and again at close (a prompt in manual mode, the classifier in auto mode). The owner asked for both to be added.

## Considered Options

- Leave the allowlist alone and let each use prompt or go to the classifier.
- Allow `git worktree *` and `git tag *` in full.
- Allow both, and ask for the forms that discard work, move a tag or reset a branch silently.

## Decision Outcome

Chosen option: "Allow both, and ask for the forms that discard work, move a tag or reset a branch silently", because it removes the stall without opening an obvious way to lose work. Review found that allowing a whole subcommand also allows its options that reset or force something, so those are listed one by one.

- Allowed, in Bash and PowerShell, with and without `git -C <path>`: every `git worktree` and `git tag` subcommand.
- Ask:
  - `git worktree remove` with `-f`, `-ff` or `--force` (it deletes uncommitted work);
  - `git tag` with `-d`, `--delete`, `-f` or `--force`, as the first option, a later option or a combined `-fa` (the tag disappears or moves, and git keeps no reflog for tags);
  - `git worktree add -B <core branch>` for `main`, `production`, `stage` and `dev` in both shells, and `-B` with any branch in Bash (it resets an existing branch, as `git switch -C` does). PowerShell matches rules case-insensitively, so there `-B <other branch>` is not asked: it would also catch the lab's `-b`. The rules put a space before `-B`, so a path or branch name that merely ends in `-b` or `-B` (for example `LAB-...-variant-b`) does not ask.
- Not caught: a force or delete flag that is not first in a combined group (`git tag -af`, `-afm`, `git worktree add -fB main`), a value attached to its flag (`-Bmain`), and abbreviated long options (`--del`, `--forc`). False positives: a flag-like word in a tag message (`git tag -a x -m "drop -d"`) asks, and in PowerShell so does `git tag -F <file>`. Remote tag deletion (`git push origin --delete <tag>`) and `git push --tags` stay allowed, as all non-core pushes were before this change; if the pushed tag is the only archive of a lab, a pushed-tag guard is a follow-up for the lab protocol's record.
- `git push` was already allowed, so pushing a tag adds no new permission. `git branch -D` keeps its ask rule in Bash only; in PowerShell it asks for core branches and is otherwise instruction-only (0031).
- The rules come from `scripts/permissions/gen_settings.py` (template profile); `scripts/permissions/check_settings.py` has the cases. `docs/protocols/agents.md` names the two commands in its list and the forced forms in a bullet.

### Consequences

- Good, because lab worktrees can be created, removed and tagged unattended in generated projects.
- Good, because the common destructive spellings still stop for confirmation.
- Bad, because the ask-first list in AGENTS.md does not name these forms; the permission rule is the only guard on them, and agents without Claude Code's rules get no prompt.
- Bad, because the guard is pattern matching on spelling, so an unusual spelling (`git tag -af`, `--del`) slips through and a flag-like word in a tag message asks needlessly.
- Not proven yet: a headless Claude Code run that exercises the rules for real (0031 did one for the first allowlist) and whether writes under `.claude/worktrees/` prompt; both stay open in DRAFT-2.

## More Information

- Amends the generated-project allowlist of [0021](0021-phase-1-readiness-answers-owner.md) answer 5 and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md); the generator, the checker and the ask-rule approach are in [0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md).
- This repo's own settings (0027) already allow both, so `.claude/settings.json` does not change.

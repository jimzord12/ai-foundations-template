---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# This repo allows everything except deleting main

## Context and Problem Statement

On 2026-10-02 an unattended run stopped because Claude Code's auto-mode classifier refused `git switch -c`. The command was on neither the allow nor the deny list, so auto mode sent it to the classifier, which refused it without a reason. Branches are mandatory here, so the refusal blocked all work. The owner's instruction: everything is allowed in this repo except deleting the main branch; only the extremely dangerous commands go to deny or ask. TASK-31.

## Considered Options

- Narrow allowlist from owner answer 5 (read-only tools, backlog, git add/commit/push and the branch commands).
- Blanket allow (`Bash`, `PowerShell`, …) plus a deny list for deleting main.
- Blanket allow plus narrow per-command rules plus a deny list for deleting main.
- `defaultMode: bypassPermissions` in the owner's user settings, with deny rules in the project.

## Decision Outcome

Chosen option: "Blanket allow plus narrow per-command rules plus a deny list", because auto mode drops blanket `Bash`, `PowerShell`, `Agent` and `Monitor` allow rules, so blanket entries alone leave every command to the classifier again, while narrow rules survive. Bypass mode was not chosen: it is a user-level switch the owner did not ask for and it lifts every other safety check.

`.claude/settings.json` holds:

- **allow:** every tool, for manual mode, plus narrow rules for the commands agents use here: git subcommands (also with `git -C <path>`; the deny and ask rules also cover `git --no-pager` and `git -c`), `backlog`, `uvx copier`, `pushover`, `gh run` and `gh workflow`, the npm check scripts, `.tmp` cleanup, `mkdir`, `cp`, `mv`.
- **deny:** deleting or renaming main, locally or on the remote, in its common spellings for Bash and PowerShell.
- **ask:** force pushes, tag pushes, `reset --hard`, `git clean -<flags>`, and `branch -D`, `-f` or `--force`, as the owner's Git rules still require.

The file is generated and checked by `scripts/permissions/` (`gen_settings.py`, `check_settings.py`). Agents cannot write `.claude/settings.json` themselves (protected path; the classifier refuses it as self-modification), so the owner copies a regenerated file into place.

### Consequences

- Good, because routine branch, commit, merge and push work runs without prompts or classifier refusals.
- Good, because deleting main is refused even when the classifier would allow it.
- Bad, because four limits remain:
  - Writes to protected paths (any `.claude/` folder, `.git/`) are never pre-approved by settings. In auto mode they go to the classifier, so tasks that write agent profiles and skills can still be refused.
  - Unlisted commands and subagent spawns still go to the classifier in auto mode.
  - The owner's user-level ask rules (rebase, amend, stash drop) still apply.
  - An untrusted workspace ignores project allow entries (deny and ask still apply). Only this repo's root checkout is trusted; a worktree or clone at another path, including one under `.tmp/`, runs without the allow list until its trust prompt is accepted.
- Bad, because matching is on command text. Known residue that is not denied: wrappers such as `bash -c` or `pwsh -c`, environment-variable prefixes, and other spellings nobody types by accident. Known false positives: denied are `git push --dry-run … main`, a push naming main together with a branch whose name contains `-d`, read-only `gh api` calls on `refs/heads/main`, and any command whose text names a delete-main command (for example a `git -C` commit message or a PowerShell script holding such text); sent to ask are a `git -C` commit whose message names `reset --hard`, `--force` or `clean -f`, and a push of any ref starting with `v`. Write such commit messages with `git commit -F <file>`, or run plain `git commit` from the repo folder. In PowerShell the rules match the whole line, not each subcommand, so one line that pushes main and also deletes a branch (`git push origin main && git push origin --delete feature/x`, or `... && git branch -d feature/x`) is denied; run each push or branch deletion as its own command. Also not denied: quoted `":refs/heads/main"`, quoted `"+main"` (not asked), and remote tag deletion with `:v…`.
- Recommendation for the owner: a GitHub ruleset on main that blocks deletion and force push. It is the only guard that does not depend on how a command is spelled.

## More Information

- Proof (2026-10-02, headless `claude -p`, stream-json, Claude Code 2.1.287):
  - Auto mode with the project file in an untrusted temp clone: allow entries were ignored (the CLI warning appeared in the sibling runs from the same untrusted folder; this transcript did not capture stderr), so the workflow steps passed the classifier; every delete-main spelling tried, including a compound PowerShell one, was denied by the rules, and `reset --hard` was held.
  - Don't-ask mode with `--settings` set to the allow list minus the blanket entries (what auto mode keeps): branch, commit, merge into main, push, `git branch --merged main`, and deleting a merged branch locally and remotely all ran with no review; the deletes and `reset --hard` were refused.
  - Manual mode with the real file in this trusted repo: branch create, switch and delete and `git -C … status` ran without a prompt; `git branch -D main` was denied.
  - Not observed directly: whether auto mode keeps `git -C *` and `npx backlog.md *`, which are broad; the docs list only blanket shell, interpreter, package-runner, Agent and Monitor rules as dropped.
- Replaces, for this repo only, the narrow allowlist of owner answer 5 in [0021](0021-phase-1-readiness-answers-owner.md). Generated projects are decided in TASK-24.

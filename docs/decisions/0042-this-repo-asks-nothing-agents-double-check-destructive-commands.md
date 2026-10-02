---
status: accepted
date: 2026-10-03
decision-makers: owner
kind: product
supersedes: []
---

# This repo asks nothing; agents double-check destructive commands

## Context and Problem Statement

Decision 0027 made this repo allow everything except deleting `main`, but it kept an ask list in `.claude/settings.json` for force pushes, tag pushes, `reset --hard`, `git clean` and `git branch -D` or `-f`. The owner moved that whole list into `allow` by hand (2026-10-03), after the "Clean up after yourself" rule (0039) made agents delete their own dead-end branches, which needs `branch -D` and prompted in Bash. Their reasoning: reduce friction as much as possible, even at some risk; instead of a prompt, agents must double-check before running a dangerous destructive command.

## Considered Options

- Keep the ask list (0027 as it was).
- Move only `git branch -D` to allow, keep the other asks.
- Move the whole ask list to allow, and replace the prompts with an instruction to double-check.
- Move it to allow but add deny rules for force-pushing `main`. Not taken: it is a spelling-based guard with the known residue of 0027, the owner asked for the least friction, and a GitHub ruleset on `main` is the real guard for that case.

## Decision Outcome

Chosen option: "Move the whole ask list to allow, and replace the prompts with an instruction to double-check", because it is the owner's choice and removes the last routine prompts in this repo; the risk is accepted.

- `.claude/settings.json` has `"ask": []`. The generator's repo profile (`scripts/permissions/gen_settings.py`) now appends the former ask rules to `allow`, and `check_settings.py` expects them allowed; the regenerated file equals the owner's hand edit. Deleting or renaming `main` stays denied.
- AGENTS.md "Git" gains **Double-check before a destructive command**: name the target and what it would lose (`git status`, `git log <base>..<branch>`, `git diff`), confirm everything it would lose is the agent's own (no uncommitted changes, untracked or ignored files, or commits on a branch that is not its own; for a push, fetch and read `git log <branch>..origin/<branch>`), use the least destructive form (`branch -d` before `-D`, `--force-with-lease` before `--force`, `git clean -n` first), leave it and report it if the loss cannot be shown or any of it is not the agent's own, never force-push `main`, and list the destructive commands run in the end-of-task summary.
- Where each former ask went: force push, `reset --hard`, `git clean`, `branch -D` and `-f`, tag pushes: **double-check**; deleting `main`: still **denied** by the settings and **ask-first**; deleting an unmerged branch that is not the agent's own: **ask-first**; release tags: pushed, moved or deleted only with the owner's approval; force-pushing `main`: **never**.
- 🧭 Agent's calls, for the owner to confirm: the shape of the double-check (the safer form first, `git clean -n` first, a fetch-and-read before a push, listing the commands run in the end-of-task summary) and not adding deny rules for force-pushing `main` (the option above); unmerged branches that are not the agent's own stay ask-first, because in this repo they are usually another session's work; "never force-push `main`" is added because it can discard `main`'s history, which 0027 protects by denying deletion; release tags also cannot be moved or deleted without approval, because `copier update` in generated projects resolves them.
- Generated projects are unchanged: the template profile and `template/AGENTS.md.jinja` keep their asks (0029, 0031, 0038).

### Consequences

- Good, because this repo's settings no longer prompt for routine branch cleanup, resets and force pushes on feature branches, and in PowerShell none of the former asks prompts (in a trusted checkout: an untrusted clone or worktree ignores project allow entries, 0027).
- Good, because the instruction still puts a deliberate check in front of each destructive command.
- Bad, because the settings no longer stop a mistaken force push, `reset --hard`, `git clean` or tag push; only the agent's own check does. The owner accepts that risk (work in this repo can almost always be regenerated).
- Bad, because the guard is an instruction, which a careless run or another agent tool can skip; Codex has no permission config in this repo, so for it the instruction was always the only guard and nothing changes. A GitHub ruleset on `main` (no deletion, no force push) remains the one guard that does not depend on an agent, as 0027 recommended.
- Not changed, and it limits the effect: the owner's user settings (`.claude-personal/settings.json`, outside this repo) still ask in Bash for `git branch -D` (kept on purpose by 0024), `git branch --force`, force pushes (including `--force-with-lease`), `reset --hard` and `git clean`. These are prefix rules, so they fire only on the leading spelling (`git push --force …`, `git branch -D …`), not on `git -C <path> …` or a trailing flag. Claude Code merges the rules of every scope and an ask beats an allow, so the leading spellings still prompt in the owner's Bash sessions here. Only removing those user-level asks, which would revisit 0024's gate and affect every project, would remove the prompts in Bash; that is the owner's separate call. PowerShell has no such rules. The owner's personal rules (`rules/delivery.md`) still list force push, `reset --hard` and `git clean` as ask-first; they defer to a repository's own AGENTS.md, so this repo's double-check applies here.

## More Information

- Amends the "ask" part of [0027](0027-this-repo-allows-everything-except-deleting-main.md) and the ask-first list of this repo's AGENTS.md (from [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md), narrowed by [0039](0039-delete-what-is-safely-deletable-without-asking.md)); implements the practical side of 0039.
- Answers TASK-35 for this repo's own profile only: the template profile and the owner's user settings stay open there (task note added).

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

## Decision Outcome

Chosen option: "Move the whole ask list to allow, and replace the prompts with an instruction to double-check", because it is the owner's choice and removes the last routine prompts in this repo; the risk is accepted.

- `.claude/settings.json` has `"ask": []`. The generator's repo profile (`scripts/permissions/gen_settings.py`) now appends the former ask rules to `allow`, and `check_settings.py` expects them allowed; the regenerated file equals the owner's hand edit. Deleting or renaming `main` stays denied.
- AGENTS.md "Git" gains **Double-check before a destructive command**: name the target and what it would lose (`git status`, `git log <base>..<branch>`, `git diff`), confirm the loss is the agent's to cause or regenerable, use the least destructive form (`branch -d` before `-D`, `--force-with-lease` before `--force`, `git clean -n` first), do not run it if the loss cannot be shown, never force-push `main`, and list the destructive commands run in the end-of-task summary.
- The AGENTS.md ask-first list shrinks to deleting `main` and deleting an unmerged branch that is not the agent's own with unique commits (0039); release tags still need the owner's approval. Force push, `reset --hard` and `git clean` move from ask-first to double-check. 🧭 Agent's call, for the owner to confirm: unmerged branches that are not the agent's own stay ask-first, because in this repo they are usually another session's work, and "never force-push `main`" is added because it has the effect of deleting `main`.
- Generated projects are unchanged: the template profile and `template/AGENTS.md.jinja` keep their asks (0029, 0031, 0038).

### Consequences

- Good, because routine branch cleanup, resets and force pushes on feature branches run without a prompt or a classifier stop in this repo.
- Good, because the instruction still puts a deliberate check in front of each destructive command.
- Bad, because the settings no longer stop a mistaken force push, `reset --hard`, `git clean` or tag push; only the agent's own check does. The owner accepts that risk (work in this repo can almost always be regenerated).
- Bad, because the guard is an instruction, which other agent tools or a careless run can skip. A GitHub ruleset on `main` (no deletion, no force push) remains the one guard that does not depend on an agent, as 0027 recommended.
- Not changed: the owner's personal settings (outside this repo) still ask for `git branch -D` and the other commands in Bash, and a project's ask beats a user allow, so personal and other projects' prompts are separate decisions.

## More Information

- Amends the "ask" part of [0027](0027-this-repo-allows-everything-except-deleting-main.md) and the ask-first list of this repo's AGENTS.md (from [0029](0029-git-and-safety-rules-for-generated-projects.md) and [0024](0024-branch-model-refinements-after-the-first-instruction-review.md)); implements the practical side of [0039](0039-delete-what-is-safely-deletable-without-asking.md). TASK-35 is about the template profile and is unaffected.

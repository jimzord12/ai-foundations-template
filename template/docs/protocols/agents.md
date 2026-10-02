# Agents, skills and permissions

How this project's agent profiles, skills and Claude Code permissions are laid out.

## Layout

- `.claude/agents/<name>.md`: one profile per job (a reviewer, a challenger, a maintainer). Profiles stay thin: a job, a tool list, a model, and the skills they preload.
- `.claude/skills/<name>/SKILL.md` (plus any scripts it needs): shared knowledge that several profiles reuse.
- `.agents/skills/<name>/`: Codex's copy of `.claude/skills/`, byte for byte (Codex's project skill folder; Claude Code reads only `.claude/skills/`; checked against the Codex docs and source on 2026-10-02). Add or change a shared skill in `.claude/skills/` and copy the folder to `.agents/skills/` in the same change (a removed or renamed skill is removed or renamed there too); never edit the copy alone. Codex ignores Claude-only frontmatter such as `user-invocable`, so it lists the reviewer and challenger skills as ordinary skills; that is expected.
- A profile preloads skills with the `skills` field; the full skill content is injected into the subagent at start.
- Files under `.claude/` hold no template syntax and link only to files that exist in this project.

## Profile frontmatter

`name` and `description` are required. Useful optional fields (checked against the Claude Code docs on 2026-10-02): `tools`, `disallowedTools`, `model`, `effort`, `maxTurns`, `skills`, `permissionMode`, `isolation`. Verify the current docs before relying on others.

- Leaving out `tools` gives the subagent every tool. List tools explicitly.
- Read-only roles (reviewers, challengers) get no `Edit` or `Write`. If they keep `Bash` (to run git and tests), they are read-only by instruction only: Claude Code cannot allow part of Bash.

```markdown
---
name: code-reviewer
description: Reviews a diff with fresh context and reports Blocking, Material, Minor and Note findings.
tools: Read, Grep, Glob, Bash
model: opus
effort: high
maxTurns: 60
skills: [review-core, review-lenses]
---
```

## Permissions

`.claude/settings.json` decides what runs without a prompt. The template ships a narrow list: read-only tools, git status, log, diff, show, add, commit, push, switch, branch, merge, fetch, pull, worktree and tag, the npm check scripts, `npm ci`, `npm install` (no package names) and the Backlog CLI. The ask-first list in AGENTS.md is mirrored as ask rules, with `main`, `production`, `stage` and `dev` treated as core branches, and nothing is denied outright. A project that widens or narrows this records why in `docs/decisions/`; check there for this project's policy.

- The allowlist reduces friction; it is not a sandbox. Anything not listed (installing a new dependency, other commands, file edits in manual mode) prompts, or in auto mode goes to Claude Code's classifier.
- Auto mode ignores blanket rules such as `Bash` or `PowerShell`, which is why the list is per command.
- Claude Code's settings ask before `git worktree remove` with a force flag (it discards uncommitted work), before `git tag` with `-d`, `--delete`, `-f` or `--force` (git keeps no reflog for tags), and before `git worktree add -B` on a core branch (it resets the branch; in Bash any branch asks). Spellings such as `git tag -af`, `git tag --del` and `git worktree add -fB main` slip through. These are a settings guard only, not on the ask-first list in AGENTS.md: where the settings do not apply, or for a spelling they miss, no prompt appears.
- Merging into a core branch other than `main` cannot be detected from the command alone; that rule stays in AGENTS.md.
- In PowerShell, run each git command as its own call. PowerShell rules match case-insensitively, so `branch -D` on a non-core branch is not asked there. In Bash it asks for any branch (a settings guard, stricter than the ask-first list). If this prompt or the one for `git worktree remove --force` is refused or nobody answers, leave the branch or worktree and list it in the end-of-task summary.
- Commit from the project folder with plain `git commit`: with `git -C <path>`, a message that names a risky command (for example `reset --hard`) can trigger an ask rule.
- Writes under `.claude/` are protected: settings never pre-approve them, so changing a profile, a skill or `.claude/settings.json` may need the owner.
- A folder Claude Code has not trusted ignores the project's allow list. Before an unattended `claude -p` run in a new folder, open Claude Code there once and accept the trust prompt.
- For a guard that does not depend on how a command is spelled, protect `main` with a GitHub ruleset that blocks deletion and force pushes.

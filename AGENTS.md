# Agent instructions: ai-foundations-template repo

This repo is a **Copier template**, not an app. Files under `template/` are rendered into other projects; everything else is about maintaining the template.

## Where things go
- `template/` — only content that belongs in generated projects. Files ending in `.jinja` are rendered with Jinja; other files are copied as-is. Stack-specific content lives in inline `{% if stack %}` blocks; whole stack-specific files can use conditional names, e.g. `{% if stack == 'express' %}stack-express.md{% endif %}` (an empty rendered name means "skip").
- `copier.yml` — questions and settings. Changing a question's name breaks `copier update` for existing projects; add a `_migrations` entry if you must.
- `docs/decisions.md` — decision log for this template. Record every non-trivial decision (format at the top of that file). Check it before deciding anything.
- `backlog/` — open work, managed with Backlog.md (see section below). Don't track open work anywhere else.
  The CLI is `backlog` (install once: `npm i -g backlog.md`) or `npx backlog.md <command>` without installing.

## Rules
- Standard over custom: use established conventions and widely adopted tools; justify custom work in the decision log.
- Verify current versions and docs of tools before relying on them.
- Ask before major or hard-to-reverse choices; say clearly what is decided vs. suggested.

## Git
- No pull requests. Work on feature branches (up to three levels below `main`), merge into `main` without asking, then delete the merged branch locally and on the remote right away.
- Delete temporary files and scratch output that no longer add value.
- Ask first, with the exact command, only for destructive git: deleting `main`, deleting an unmerged level-1 branch with substantial work, force push to a shared branch, `reset --hard`, `git clean`, rewriting pushed history.

## Checks
- Smoke-test rendering after changing `template/` or `copier.yml`:
  `uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=express . .tmp/smoke`
  (repeat with `stack=next` and `stack=rn`; `.tmp/` is git-ignored).

<!-- BACKLOG.MD GUIDELINES START -->
<!-- backlog.md-instructions-version: 1.53.0 -->
<CRITICAL_INSTRUCTION>

## Backlog.md Workflow

This project uses Backlog.md for task and project management.

**At the beginning of each conversation in this project, run `backlog instructions overview` before answering or taking action. Re-read it only if you have not read it yet in the current conversation.**

Use the overview to decide whether to search, read, create, or update Backlog tasks.

Before task lifecycle actions, read the matching detailed guide:
- `backlog instructions task-creation` before creating or splitting tasks
- `backlog instructions task-execution` before planning, changing status or assignee, adding a plan or implementation notes, or implementing task work
- `backlog instructions task-finalization` before checking acceptance criteria, writing final summaries, or moving tasks to terminal statuses

Use `backlog <command> --help` before running unfamiliar commands. Help shows options, fields, and examples.

Do not edit Backlog task, draft, document, decision, or milestone markdown files directly. Use the `backlog` CLI so metadata, relationships, and history stay consistent.

</CRITICAL_INSTRUCTION>
<!-- BACKLOG.MD GUIDELINES END -->

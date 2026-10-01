# ai-foundations-template

A [Copier](https://copier.readthedocs.io/) template for personal TypeScript projects (Express backend, Next.js frontend, bare React Native mobile). Its job is to give every project the same "AI foundations" so coding agents produce consistent, standard, maintainable code: agent instructions, a decision log, preferred libraries and conventions, and the tooling that supports them.

> Status: early skeleton. See `backlog/` for open work and `docs/decisions.md` for what's decided.

## Use it

Requires [uv](https://docs.astral.sh/uv/) (runs Copier without a Python project setup).

```bash
# Create a new project (asks for name + stack)
uvx copier copy --trust gh:<owner>/ai-foundations-template my-project

# Later, inside the project: pull template changes (3-way merge, keeps your edits)
uvx copier update --trust
```

Next.js and React Native projects are scaffolded first (`create-next-app` and the RN CLI refuse a non-empty folder), then Copier is applied on top. `create-next-app` writes its own `AGENTS.md`: answer **yes** (or pass `--overwrite`) when Copier asks to overwrite it. When `next dev` runs under an AI agent it re-adds its managed block at the end of the file, which is fine.

## Repo layout

| Path | What it is |
|---|---|
| `copier.yml` | Template questions and Copier settings |
| `template/` | Files rendered into new projects. Shared by all stacks; stack-specific content uses inline `{% if stack %}` blocks; whole files can use conditional names (e.g. `{% if stack == 'rn' %}stack-rn.md{% endif %}`) |
| `docs/decisions.md` | Decision log for the template itself |
| `docs/agent-instructions.md` | Superseded baseline, kept for history; see `template/AGENTS.md.jinja` |
| `backlog/` | Open work, managed with [Backlog.md](https://github.com/MrLesk/Backlog.md) |
| `AGENTS.md` / `CLAUDE.md` | Instructions for agents working on *this* repo |

## Releasing a template version

Projects update to git tags. Releases are tagged by an agent and pushed only with the owner's approval (see `docs/decisions.md`).

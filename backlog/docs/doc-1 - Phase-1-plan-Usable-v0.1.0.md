---
id: doc-1
title: 'Phase 1 plan: Usable v0.1.0'
type: specification
created_date: '2026-10-01 19:52'
updated_date: '2026-10-01 20:15'
---
# Phase 1 plan: Usable v0.1.0

**Goal.** A project created from the template today is genuinely usable by agents: strong instructions (knowledge system, charter, git and done rules, review loop, ready gate), a real technical baseline per stack (integration mechanism, strict TypeScript, lint/format, tests, check commands), CI for both the template and generated projects with secret scanning, released as tag `v0.1.0`.

**Exit criteria.** Every Phase 1 task is Done; this repo's CI is green on `main`; a project generated per stack from `gh:jimzord12/ai-foundations-template@v0.1.0` passes `npm run check` and its own CI workflow.

## Rules for running this phase

- **One runner, ordinal order.** Tasks that edit `template/AGENTS.md.jinja` or the root `AGENTS.md` never run in parallel.
- **AGENTS.md line budget.** Each task adds at most 4 lines to `AGENTS.md`; detail goes in `docs/protocols/<topic>.md`. The rendered file stays at or under 100 lines (asserted by TASK-17).
- **Dogfood.** Agent profiles, skills and protocols built for the template are also used in this repo; a manifest lists every copied file and CI (TASK-13) fails on drift.
- **Ready gate.** A task runs unattended only with the `ready` label, given after an independent readiness challenge returns READY.
- **Tag push.** The agent prepares `v0.1.0`; the owner approves the push in session.

## Order

| Step | Task | Produces | Depends on |
|---|---|---|---|
| 1 | TASK-25 knowledge system | `docs/decisions/` (MADR, kind field), `architecture.md`, `domain/glossary.md`; this repo migrates its own log | none |
| 2 | TASK-7 charter | `docs/protocols/charter.md` (tiers per decision kind), `evolution.md` | 25 |
| 3 | TASK-14 git and safety | `docs/protocols/git.md` | 7 |
| 4 | TASK-15 done rule | `docs/protocols/done.md`, Backlog DoD defaults for generated projects | 14 |
| 5 | TASK-24 agent tool layout | `.claude/settings.json` allowlist, agents and skills layout, dogfood manifest | 15 |
| 6 | TASK-11 review loop | `review-core` and `code-review` skills, `code-reviewer` profile, `review.md` | 24 |
| 7 | TASK-26 ready gate | `ready` skill, `readiness-challenger` profile, `ready.md` | 11 |
| 8 | TASK-28 Codex skills | Shared skills visible to Codex from one source | 24 |
| 9 | TASK-2.5 integration mechanism | Copier post-copy tasks, Express skeleton | none |
| 10 | TASK-2.1, 2.2, 2.3 | Strict TS and ts-reset; lint and format; test runner with proven red-green examples | 2.5 |
| 11 | TASK-2.4 check commands | `typecheck`, `lint`, `format:check`, `test`, `check` scripts | 2.5 |
| 12 | TASK-27 generated-project CI | `.github/workflows/check.yml` in the template | 2.4 |
| 13 | TASK-17 automated tests | Render, update and collision tests that fail when broken | 2.4 |
| 14 | TASK-13 template CI | Workflow running 17, `check` per stack, identical-check | 17 |
| 15 | TASK-23 secret scanning | gitleaks in both workflows, `.env.example`, planted-secret proof | 27 (and 13) |
| 16 | TASK-16 release | Versioning rule, README fixes, tag `v0.1.0` (owner approves push) | all above |

## Verification

The project Definition of Done applies to every task. Template content is proven on freshly scaffolded projects (create-next-app, the current RN community template, the Express skeleton), not only on renders.

## Owner answers (2026-10-01)

RN at current stable; this repo migrates its decision log; Copier post-copy tasks plus overwrite-on-purpose configs plus an Express skeleton; Codex native only (AGENTS.md and skills); allowlist of read-only tools, package scripts, backlog, git add/commit/push; tag push approved by the owner; generated projects get CI. Recorded in `docs/decisions.md`.

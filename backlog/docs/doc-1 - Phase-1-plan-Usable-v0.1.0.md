---
id: doc-1
title: 'Phase 1 plan: Usable v0.1.0'
type: specification
created_date: '2026-10-01 19:52'
updated_date: '2026-10-01 19:52'
---
# Phase 1 plan: Usable v0.1.0

**Goal.** A project created from the template today is genuinely usable by agents: strong instructions (knowledge system, charter, git and done rules, ready gate, review loop), a real technical baseline per stack (strict TypeScript, lint/format, tests, check commands), and a template that is tested in CI, scans for secrets, and is released as tag `v0.1.0`.

**Exit criteria.** Every Phase 1 task is Done; CI is green on `main`; `uvx copier copy gh:jimzord12/ai-foundations-template@v0.1.0` produces a project per stack whose check commands pass on a fresh install.

## Order and why

Instruction tasks come first because they all edit `template/AGENTS.md.jinja`; doing them in sequence avoids rework. Tooling comes next, then tests and CI that cover everything, then the tag.

| Step | Task | Produces | Depends on |
|---|---|---|---|
| 1 | TASK-25 knowledge system | `docs/decisions/` (MADR), `architecture.md`, `domain/glossary.md`, router lines | none |
| 2 | TASK-7 charter | Authority tiers, design evolution protocol | 25 |
| 3 | TASK-24 agent tool baseline | `.claude/` and Codex layout, permissions | none |
| 4 | TASK-11 review loop | Reviewer and context-maintainer agents, caps 8/15 | 24 |
| 5 | TASK-26 ready gate | `docs/protocols/ready.md`, readiness lens, `ready` label rule | 11 |
| 6 | TASK-14 git and safety | Impact-based git rules | 7 |
| 7 | TASK-15 done rule | Definition of done and evidence rule | 7 |
| 8 | TASK-2.1 to 2.4 stack baseline | tsconfig and ts-reset, lint/format, tests, check scripts | 2.4 needs 2.1-2.3 |
| 9 | TASK-17 automated tests | Render, update and collision tests that fail when broken | none |
| 10 | TASK-13 CI | GitHub Actions running the tests and the copy-identical check | 17 |
| 11 | TASK-23 security | gitleaks step in CI, `.env.example`, planted-secret proof | 13 |
| 12 | TASK-16 release | Versioning rule, tag `v0.1.0`, real `copier update` proof | all above |

## How each task is verified

The project Definition of Done applies to every task: acceptance criteria verified with evidence, smoke test for all three stacks when `template/` changes, independent review loop to PASS, decisions logged, committed and pushed. Template content is additionally proven on freshly scaffolded projects (create-next-app, RN CLI, an Express skeleton), not only on renders.

## Questions only the owner can answer (before the affected step)

1. React Native version for the template: the brief says 0.81, a 2026-09-29 check saw 0.87.2 as latest (affects step 8).
2. Whether this repo migrates its own `docs/decisions.md` to the new one-file-per-decision format (TASK-25 criterion; recommendation: yes, during step 1, so the template practises what it ships).

## Ready gate status

Each task above gets the `ready` label only after the independent readiness challenge returns READY. Tasks without the label are not run unattended.

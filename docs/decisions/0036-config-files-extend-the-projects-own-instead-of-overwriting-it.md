---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: technical
supersedes: []
---

# Config files extend the project's own instead of overwriting it

## Context and Problem Statement

[0021](0021-phase-1-readiness-answers-owner.md) answer 3 said the config files the template ships "extend the framework's own configs and overwrite them on purpose". Checking it (TASK-2.1, TASK-2.5) found two problems. On a first copy Copier has no merge or patch feature (`copier update` does a three-way merge of template changes, which does not help here): for a file that already exists it can only overwrite, skip or exclude it, and run scripts after the copy. And a shipped `tsconfig.json` that overwrites a scaffolded one drops framework wiring where the framework publishes no base config to extend (Next.js, to our knowledge). The owner also intends to widen the template beyond the current three stacks (the list of frameworks is not decided here), so a per-stack config file would not scale.

## Considered Options

- Overwrite the framework's config on purpose (the 0021 answer): risks breaking the framework, needs one file per stack.
- Patch the framework's config in a post-copy task: needs a parser that tolerates comments and trailing commas (`tsconfig.json` is not strict JSON), and differs per framework.
- Ship a new file that extends the project's own config and adds the strict settings; run the check against that file.

## Decision Outcome

Chosen option: "a new file that extends the project's own config", because it never touches what the framework generated, and one file works for every framework.

- For TypeScript the template ships `tsconfig.foundations.json`, which `extends` the project's `tsconfig.json` and adds the strict flags. `npm run typecheck` runs `tsc -p tsconfig.foundations.json --noEmit` and is part of `check`. A project that ships no `tsconfig.json` of its own (the Express skeleton) gets a `tsconfig.json` from the template, which the foundations file then extends the same way.
- One mechanism per kind of file: instruction and documentation files (`AGENTS.md`, `CLAUDE.md`, `docs/`, `.claude/`) are copied and may overwrite scaffolded ones, as the README already tells users to accept for `AGENTS.md`; config files get a new file that extends the project's own, never an overwrite; `package.json` is changed only by a post-copy task with `npm pkg set` / `npm i -D`, run on copy only (TASK-2.5).
- Other tools (lint, format, test runner) follow the same rule where the tool accepts a config path or can import the project's config. TASK-2.2 and TASK-2.3 must verify that per tool before relying on it.

### Consequences

- Good, because the framework's own build, editor settings and generated files stay untouched, and adding a framework needs no new config file.
- Good, because it is the pattern NestJS already uses (`tsconfig.build.json` extending `tsconfig.json`).
- Bad, because the editor and the framework's own build keep using the project's `tsconfig.json`; strictness is enforced by `check`, not by `next build` or the editor.
- Bad, because every project carries one extra config file per tool that uses this pattern.

## More Information

- Refines [0021](0021-phase-1-readiness-answers-owner.md) answer 3 (the overwrite part only; post-copy tasks and the Express skeleton stand). Raised by TASK-2.1 and TASK-2.5.
- Evidence (2026-10-02): a scratch `tsconfig.json` with a comment and a trailing comma plus a `tsconfig.foundations.json` that extends it; `npx -p typescript tsc --showConfig -p tsconfig.foundations.json` (it fetched `typescript` 7.0.2; a bare `npx tsc` fetches the deprecated `tsc` package instead, so always install `typescript`) kept the framework's `strict` and added `noUncheckedIndexedAccess` and `exactOptionalPropertyTypes`. Copier's lack of a merge feature is from its configuration docs; an overlay of the template onto an existing folder with `--overwrite` replaced `AGENTS.md` and left `package.json` and `tsconfig.json` alone.
- Not checked: how `tsc` treats a framework's editor-only `plugins` entry through `extends`; the pattern on Astro, SvelteKit and Expo configs (they extend generated or package-provided bases, so the chain may be longer); any tool other than `tsc`. TASK-2.1 verifies the TypeScript cases on freshly scaffolded projects.

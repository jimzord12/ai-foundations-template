---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: architecture
supersedes: ["0004"]
---

# Stack-agnostic core with stack packs picked by detection

## Context and Problem Statement

[0004](0004-one-template-shared-files-conditional-per-stack-files.md) built one template around a closed `stack` question (Express, Next.js, bare React Native) with `{% if stack %}` blocks. The owner now wants the template to serve any modern TypeScript project in an app ecosystem: web (Next.js, Astro, SvelteKit, Solid), mobile (bare React Native and Expo) and backend (Elysia, Hono, Fastify, Express, Nest.js). A closed list with Jinja blocks per stack cannot grow to that, and most of what the template gives (protocols, review loop, git rules, decision records, the `check` contract) does not depend on the framework. The Task 2 family (TASK-2, 2.1 to 2.5) was written for three stacks only. The usual flow stays: scaffold the project with the framework's own tool, then apply this template over it (README, [0014](0014-generated-projects-use-backlog-md-and-ignore-local.md), TASK-2.5).

## Considered Options

- Keep the closed `stack` list and add a branch per framework: every new framework edits shared files, and the list grows without end.
- One template per stack: duplicates the core and needs several update runs per project (the reason 0004 rejected it).
- A generic core plus small per-framework **packs**, with the pack picked by a post-copy task that reads `package.json`.
- Detect inside Copier's own questions: needs a Jinja extension that reads the filesystem, which means extra packages next to Copier and a changed install command.

## Decision Outcome

Chosen option: "a generic core plus packs picked by detection", because adding a framework becomes adding one pack and one detection line, with no change to shared files.

- **Generic core:** everything rendered by Copier today that does not depend on the framework: `AGENTS.md`, protocols, `.claude/`, docs, the foundations config files of [0036](0036-config-files-extend-the-projects-own-instead-of-overwriting-it.md) and the `check` contract (`typecheck`, `lint`, `format:check`, `test`, `check`).
- **Pack:** a small file per framework (a few rules, the framework's prepare step for typecheck, how it meets each part of the contract). The stack-specific `{% if stack %}` blocks of `template/AGENTS.md.jinja` move into packs. `AGENTS.md` links the project's pack from its "When to read what" table.
- **Detection:** a post-copy task (list form, run on copy) reads `package.json`, picks the first match in a fixed precedence list (Expo before React Native, and so on), copies that pack to `docs/stack.md` and adds the package scripts with `npm pkg set`. No match, or no `package.json`, means the generic pack. Several matches take the first one and print a warning.
- **Override:** the `stack` question stays, so its name does not change and `copier update` keeps working. Its default becomes `auto`; any other value names a pack and skips detection, which is how an ambiguous or unknown project is set by hand. The answer is stored in `.copier-answers.yml`.
- **Scope:** which frameworks get a pack, and which are verified for v0.1.0, is not decided here. Phase 1 ([doc-1](../../backlog/docs/doc-1%20-%20Phase-1-plan-Usable-v0.1.0.md)) names Next.js, bare React Native and Express; the other packs are follow-up work. Unknown frameworks get the generic pack, never a failure.

### Consequences

- Good, because a new framework needs one pack file and one detection line, and an unknown one still gets the whole generic core.
- Good, because it works over any scaffold and never overwrites the framework's own configs (0036).
- Bad, because the pack file is written by a task, not rendered by Copier, so Copier does not track it: this is the `copier update` objection 0004 raised against overlay scripts. A changed pack reaches an existing project only if the task also runs on update (idempotently) or through a documented manual step; TASK-2.5 decides which.
- Bad, because the precedence list needs upkeep, and the detection script is Python (accepted for TypeScript projects in [0016](0016-repo-maintenance-capability-ships-in-this-repo-and-in-generated-projects.md)).
- Findings the packs and TASK-2.1 to 2.4 must carry: a pack declares a prepare step that runs before `tsc` (Next.js `next typegen`, Astro `astro sync`, SvelteKit `svelte-kit sync`); `typescript` may be missing from a scaffold (Astro's minimal template) and must be ensured as a dev dependency; `tsc` does not check `.astro` or `.svelte` files, so a pack may name the framework's own checker next to `typecheck`; Expo projects also list `react-native`, hence the precedence rule.

## More Information

- Supersedes [0004](0004-one-template-shared-files-conditional-per-stack-files.md); it also replaces the inline `{% if stack %}` blocks that [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md) kept. 0007's router idea stands. Builds on [0036](0036-config-files-extend-the-projects-own-instead-of-overwriting-it.md).
- Evidence (2026-10-02, Copier 9.18.2 on Windows, a throwaway spike in a scratch folder, since deleted): a template with no per-stack files and a Python detector run as a post-copy task. Real scaffolds from the then-current `create-next-app` (Next.js 16), `create-astro` and `sv create`: the overlay replaced the scaffold's `AGENTS.md`, left `tsconfig.json` untouched, added the foundations file and the `typecheck` script; `tsc -p tsconfig.foundations.json --noEmit` exited 0 on all three, with the framework's own settings (`strict`, `moduleResolution`, `verbatimModuleSyntax`, `jsx`) kept and the two added flags applied. The chains were a plain config (Next.js), a package config (`astro/tsconfigs/strict`) and a generated one (SvelteKit). Next.js failed `LayoutProps` not found until `next typegen` had run, and failed identically on its own `tsconfig.json`; Astro needed `typescript` installed. Detection on projects with only a `package.json` and a plain `tsconfig.json`: Express, Fastify, Elysia, Hono, Nest.js, SolidStart, Expo and bare React Native each picked their pack; Expo (which also lists `react-native`) and Next.js plus Express took the first match with a warning; an unknown dependency and an empty folder fell back to the generic pack. The task also found its script when the template was a git clone in a temporary folder, as with `gh:` or `--vcs-ref`.
- Not checked: real scaffolds of Expo, bare React Native, Nest.js, Hono, Fastify, Elysia and SolidStart (only their `package.json` shape was used); `copier update` after a pack changes; macOS and Linux; passing the `stack` answer to the task as an argument (the same templating as the script path, but not run).

# Agreed agent-instruction baseline

Status: **superseded as source of truth by `template/AGENTS.md.jinja` and `template/docs/protocols/typescript.md` (see `docs/decisions/0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md`). Kept for history; older paths below, such as `docs/decisions.md`, are as they were then.**

---

> These are global defaults. Project-level or more specific instructions override them when they conflict.

## Philosophy: standard over custom

Prefer popular, well-known conventions and libraries over inventing custom solutions, even when custom would be faster to write. A standard approach is one other developers (and AI agents) already recognize, is documented and battle-tested, and doesn't need to be maintained by us.

- Before designing a pattern (folder structure, error handling, config, API shape, naming), use the convention the ecosystem or framework already established.
- Choose widely adopted libraries over niche ones, even if the niche one is slightly nicer.
- Write custom code only when no standard option fits, and say why in a short comment.
- When unsure whether a standard exists, check before building.

## Autonomous mode

By default, ask before choosing new libraries, patterns, conventions, folder structure, or tooling.

If the user has explicitly enabled highly autonomous, low-friction development (in project instructions or the conversation), make these decisions yourself without asking, including adding dependencies.

Exception: never decide major, hard-to-reverse choices yourself, even in autonomous mode. Present options with tradeoffs and let the user choose. This includes database, auth provider, hosting/infrastructure, paid services, and core framework changes.

At the end of a task, briefly list the decisions made (one line each) so the user can review or reverse them without opening the log.

### Recording decisions

Record every non-trivial decision you make (autonomous or not), including the alternatives considered and why the chosen option won.

A decision is non-trivial if a teammate would reasonably ask "why this?" (new dependency, new pattern, structural change, deviation from a convention). Skip obvious or already-established choices.

- If the project already has a decisions log (e.g. ADRs, `docs/decisions.md`, `docs/adr/`), use it and match its existing format and style.
- If none exists, create `docs/decisions.md` and append entries like:

  ### YYYY-MM-DD: <decision title>
  - **Context:** what needed deciding and why
  - **Decision:** what was chosen
  - **Alternatives considered:** each option and why it lost
  - **Consequences:** tradeoffs accepted, what would trigger revisiting

Before making a decision, check the log for an existing one on the same topic and follow it, unless there's a clear reason to supersede it (then add a new entry that references the old one).

## TypeScript: reuse before building

Before writing any utility or helper in a TypeScript project, check in this order:

1. **Existing project code.** Search the repo for an existing helper, util, hook, or service that already does this (e.g. `utils/`, `lib/`, `helpers/`, `shared/`). Reuse or extend it instead of duplicating.
2. **Native APIs.** Prefer built-ins when the runtime supports them: `structuredClone`, `Object.groupBy`, `Array.prototype.toSorted`/`toReversed`, `AbortSignal.timeout()`, `crypto.randomUUID()`. Verify support first — React Native (Hermes) lacks some of these.
3. **Preferred libraries.** If one covers the need, use it:
   - General utilities (groupBy, debounce, pick/omit, chunk, uniqBy…): `es-toolkit`
   - Validation / parsing external data: `zod`
   - Typed errors in failure-heavy modules: `neverthrow`
   - Retries with backoff: `p-retry`
   - Concurrency limits: `p-limit`
   - Dates: `date-fns`
   - Utility types: `type-fest`
   - Safer built-in types: `@total-typescript/ts-reset`
   - IDs: `nanoid` (in React Native, requires `react-native-get-random-values`)
4. **Custom code.** Only if none of the above fits. Put it in the project's shared utils location so it's reusable, and keep it small and typed.

Rules:
- Prefer libraries already in `package.json`. Adding a new one follows the "Autonomous mode" rules above.
- Before adding or using a library, check its current docs and the installed version. Don't rely on memory for APIs. Prefer actively maintained packages (recent releases, wide adoption) with permissive licenses (MIT, Apache-2.0, BSD).
- Don't add a library for a one-liner the native API already handles.
- Match what the repo already uses (e.g. if it uses lodash or dayjs, don't introduce es-toolkit or date-fns alongside it).

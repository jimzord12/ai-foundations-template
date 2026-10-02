---
protocol: typescript
kind: rule
status: active
summary: Before writing a helper, reuse project code, then native APIs, then preferred libraries, and only then custom code.
applies-when: Writing TypeScript, adding a utility or helper, or choosing a library.
agents: []
skills: []
related: []
---
# TypeScript: reuse before building

Before writing any utility or helper, check in this order:

1. **Existing project code.** Search the repo for an existing helper, util, hook or service that already does this (`utils/`, `lib/`, `helpers/`, `shared/`). Reuse or extend it instead of duplicating.
2. **Native APIs.** Prefer built-ins when the runtime supports them: `structuredClone`, `Object.groupBy`, `Array.prototype.toSorted`/`toReversed`, `AbortSignal.timeout()`, `crypto.randomUUID()`. Verify support first; React Native (Hermes) lacks some of these.
3. **Preferred libraries.** If one covers the need, use it:
   - General utilities (groupBy, debounce, pick/omit, chunk, uniqBy...): `es-toolkit`
   - Validation / parsing external data: `zod`
   - Typed errors in failure-heavy modules: `neverthrow`
   - Retries with backoff: `p-retry`
   - Concurrency limits: `p-limit`
   - Dates: `date-fns`
   - Utility types: `type-fest`
   - Safer built-in types: `@total-typescript/ts-reset`
   - IDs: `nanoid` (in React Native, requires `react-native-get-random-values`)
4. **Custom code.** Only if none of the above fits. Put it in the project's shared utils location so it is reusable, and keep it small and typed.

Rules:
- Prefer libraries already in `package.json`. A new library is a decision: check it against the rules in `AGENTS.md` and log it if non-trivial.
- Before adding or using a library, check its current docs and the installed version. Prefer actively maintained packages (recent releases, wide adoption) with permissive licenses (MIT, Apache-2.0, BSD).
- Don't add a library for a one-liner the native API already handles.
- Match what the repo already uses (if it uses lodash or dayjs, don't introduce es-toolkit or date-fns alongside it).

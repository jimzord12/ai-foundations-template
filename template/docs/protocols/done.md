# Done

What "done" means, what counts as evidence, and what to tell the owner at the end of a task.

## Done means

- The behaviour is proven by running the real thing, not only by a passing test.
- Checks pass: `npm run check`, or, where the project has no check script yet, the checks as `docs/protocols/git.md` "Merging" defines them.
- The change is merged and pushed as `docs/protocols/git.md` describes.
- You gave the end-of-task summary below.

## Evidence

- Short, readable in under a minute: a command and its result, a screenshot, or a log excerpt that proves the behaviour, not the code.
- Run it against the real local stack (local database, local server, emulator or device) whenever that can run locally.
- The owner's final check is using the product. Evidence prepares that check; it does not replace it.

## Separate facts

Committed, pushed, merged, checks passing and working in the running app are different facts. Report each one separately and never imply one from another.

## Tests

- Every test exercises the real implementation. A test that would still pass with the implementation deleted must not be written.
- Mock only at true external boundaries: third-party network services, payment or other providers, hardware, the clock. Ideally replace the provider at its port (`docs/protocols/evolution.md`).
- Never mock the project's own modules; never mock the database when it can run locally.

## End-of-task summary

Other protocols send items here, so keep this name. The summary holds:

1. **Decisions** you took, one line each, including structural changes you made (`docs/protocols/evolution.md`).
2. **Evidence**, as above.
3. **Waiting on the owner:** proposed records and open product questions (`docs/protocols/charter.md`), ask-first actions you skipped while the owner was away, tasks left unready on owner questions (`docs/protocols/ready.md`), and changes left unmerged with unresolved review findings (`docs/protocols/review.md`).
4. **Findings:** your own observations, not a relay of what subagents reported. This includes friction you noticed but did not act on (`docs/protocols/evolution.md`). Other protocols add subsections here. An empty subsection folds into one line (for example "Lint/CI: none"); when every subsection is empty, the section is "Findings: none".

Leave out sections 1 to 3 when they are empty; Findings always appears, at least as "Findings: none". This defines the content. The owner's personal format (for example a recap or a next-move line) still applies.

## Backlog Definition of Done

If `backlog/config.yml` has no `definition_of_done` key, add this line to it (the CLI cannot set it). A project's own existing list is left alone.

```yaml
definition_of_done: ["Every acceptance criterion verified with evidence (command and result, screenshot or log)", "Checks pass (npm run check, or the git.md fallback)", "Review reached PASS for non-trivial changes", "Non-trivial decisions recorded in docs/decisions/", "Merged into main, pushed, and the feature branch deleted"]
```

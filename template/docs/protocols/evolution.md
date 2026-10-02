# Evolving the design

Start simple and add structure only when friction shows it is needed. This file says what to watch for, how much ceremony a change needs, and how to move code without breaking it.

## The ladder

Climb one step at a time, only as far as the friction demands:

1. inline code
2. a function
3. a module
4. a pattern or an interface
5. a folder restructure (for example grouping by feature)
6. ports and adapters at a boundary

## Signals

These are signals to consider a change in code you are already working on. They are never a reason to refactor code you are not touching, and never lint errors.

- **Copied code:** the rule of three in AGENTS.md.
- **Size:** a file over about 300 lines, or a function over about 50.
- **Scattered change:** the same kind of change keeps needing edits in the same scattered places (seen twice). Tests, and the layers `docs/architecture.md` says every feature touches, do not count.
- **Repeat bug:** the same bug fixed twice.
- **Test setup pain:** a test needs to mock the project's own modules, or its setup outgrows its assertions.
- **New business area:** a second area with its own words appears; add `docs/domain/contexts.md` (glossary level 2).

**When to add a port:** the code talks to an external service, device or provider that tests must replace, or that has, or has a planned, second provider. Put an interface (the port) in front of it and keep the provider-specific code (the adapter) behind it.

## How much ceremony

| Band | Example | Record | Owner |
|---|---|---|---|
| Routine | Extract a helper or a module | None | Not involved |
| Structural | Changes what `docs/architecture.md` describes | Architecture record, `accepted` by you; update `docs/architecture.md` and the glossary in the same change | Mention it in the end-of-task summary |
| Big | Anything on the list in `docs/protocols/charter.md` | Architecture record, `proposed` | Approves before you build it |


## Moving code safely

1. One commit that only moves or renames files and updates references. No behaviour change; all checks green.
2. Then separate commits for any behaviour change.
3. Tests, and any review step the project uses, pass before merging.

## Stepping down

Structure has a cost. Remove an abstraction that has one implementation and no second in sight, or indirection nobody uses. Treat it like any other change, in whichever band it falls into, and supersede the record that added it if there is one. A port at a true external boundary is never stepped down: it is what lets tests replace the provider.

## Signals you did not act on

List friction you noticed but did not act on in your end-of-task summary, so the owner sees it.

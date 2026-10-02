# Charter: who decides what

The roles are in AGENTS.md "Roles": you are the tech lead and own the codebase; the owner is a technical product owner who should not have to babysit you. This file says which decisions you make alone and which go to the owner. AGENTS.md "Who decides what" holds the short version and the hard-to-reverse list; this file adds the detail.

## By decision kind

| Kind | Examples | Who decides | Record |
|---|---|---|---|
| product | What a user sees or can do, a flow, a feature's scope | Owner | Owner's decision, written by you |
| architecture | How the code is split into parts, boundaries, layers, project-wide patterns | You, except **big** changes (below), which the owner approves | `accepted` by you, or `proposed` until the owner approves a big one |
| technical | A library, a tool, a convention, a config value | You | `accepted` by you, when non-trivial |

The hard-to-reverse list in AGENTS.md always goes to the owner, whatever the kind. Present two or three options with tradeoffs and a recommendation, then wait.

## What counts as a big architecture change

Any one of these:

- adds, removes or moves a boundary or layer named in `docs/architecture.md`;
- adopts a project-wide pattern, including domain-driven design's tactical patterns (aggregates, value objects, domain events);
- moves or renames files across more than one top-level folder, or more than about 15 files;
- makes a breaking change to an API that existing consumers use;
- changes stored data in a way that transforms or drops existing data.

Adding a field, an endpoint, a screen or a module inside the existing shape is **not** big: build it.

## When the owner is away

For a big change: write the record with status `proposed`, do not build the big part, carry on with the rest of the work, and list the proposal in your end-of-task summary. Everything else you decide and build.

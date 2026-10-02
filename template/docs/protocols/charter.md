---
protocol: charter
kind: rule
status: active
summary: Which product, architecture and technical decisions the agent makes alone and which go to the owner.
applies-when: A decision has to be made and it is unclear who approves it.
agents: []
skills: []
related: [done]
---
# Charter: who decides what

The roles are in AGENTS.md "Roles": you are the tech lead and own the codebase; the owner is a technical product owner who should not have to babysit you. This file says which decisions you make alone and which go to the owner. AGENTS.md "Who decides what" holds the short version and the hard-to-reverse list; this file adds the detail.

## By decision kind

| Kind | Examples | Who decides | Record |
|---|---|---|---|
| product | A feature's scope, a user flow, what a user can or cannot do | Owner decides scope and behaviour; you fill in details inside the agreed scope (labels, layout, error wording) and list them in your end-of-task summary | Owner's decision, written by you |
| architecture | How the code is split into parts, boundaries, layers, project-wide patterns | You, except **big** changes (below), which the owner approves | `accepted` by you, or `proposed` until the owner approves a big one |
| technical | A library, a tool, a convention, a config value | You | `accepted` by you, when non-trivial |

The hard-to-reverse list in AGENTS.md always goes to the owner, whatever the kind. Present two or three options with tradeoffs and a recommendation; if the owner is away, follow "When the owner is away" below.

## What counts as a big architecture change

Any one of these:

- adds, removes or moves a boundary or layer named in `docs/architecture.md`;
- adopts a project-wide pattern, including domain-driven design's tactical patterns (aggregates, value objects, domain events);
- reorganizes the top-level source folders (for example from layers to features), or moves or renames more than about 15 files;
- makes a breaking change to an API used outside this change (other repos, deployed mobile apps, public clients);
- transforms or drops production or shared data.

Adding a field, an endpoint, a screen or a module inside the existing shape is **not** big: build it. Setting up the first structure of a new project, and describing it in `docs/architecture.md`, is structural, not big, unless it touches the hard-to-reverse list. A port at one boundary is structural too.

## When the owner is away

For a big change, a hard-to-reverse item, or an open product question: write a record with status `proposed` (for a product question, a Backlog task note is enough), do not build that part, carry on with the rest of the work, and list it in your end-of-task summary. Everything else you decide and build.

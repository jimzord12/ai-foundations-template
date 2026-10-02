---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# Authority tiers and design evolution protocol

## Context and Problem Statement

Generated projects tell the agent it is the tech lead and owns the codebase, while the owner, a technical product owner, does not want to babysit. Agents needed explicit rules for which decisions go to the owner, and concrete signals for when to move from simple code to patterns, restructured folders and ports and adapters. This records one owner-approved design (2026-10-01) covering both. TASK-7.

## Considered Options

- Keep everything in AGENTS.md.
- Move the tiers and the protocol into linked protocol files, keeping the always-loaded gates in AGENTS.md.
- Leave evolution to the agent's judgement with no written signals.

## Decision Outcome

Chosen option: "Move the tiers and the protocol into linked protocol files, keeping the always-loaded gates in AGENTS.md", because AGENTS.md has a line budget, while the owner gates must stay in the file every session loads.

- `docs/protocols/charter.md`: authority per decision kind, the test for a **big** architecture change (adds, removes or moves a boundary or layer named in architecture.md; a project-wide pattern; moves between top-level source folders or more than about 15 files; a breaking change to an API used outside this change; transforming or dropping production or shared data; a new project's first structure and a single port are structural, not big), and what to do when the owner is away (for big changes, hard-to-reverse items and open product questions: record `proposed`, build the rest, report it).
- `docs/protocols/evolution.md`: the ladder, signals (rule of three, about 300-line files and 50-line functions in code being changed, scattered change seen twice, a repeat bug, test setup pain, a second business area), the port trigger, three bands (routine: no record; structural: accepted record plus architecture.md; big: proposed until approved), the move procedure (pure-move commit with checks green, then behaviour commits), and the step-down rule (never for a port at a true external boundary).
- AGENTS.md keeps the kind mapping, the hard-to-reverse list, the end-of-task decision summary and a one-line ladder; the owner-override clause in Roles also protects charter.md; router rows point to both files, phrased as the signals so agents find evolution.md before they restructure.
- One owner per rule: the hard-to-reverse list lives in AGENTS.md; the supersede procedure lives in `docs/decisions/README.md`; the end-of-task report detail belongs to `done.md` (TASK-15).

### Consequences

- Good, because routine feature work (fields, endpoints, screens) never waits for the owner, while boundary, pattern and data-loss changes do.
- Good, because size thresholds are signals for code being changed, so they do not trigger refactors of untouched code or lint churn.
- Bad, because the thresholds are judgement-based defaults; the evals (TASK-20) should show whether agents apply them sensibly.

## More Information

- Narrows [0008](0008-agents-decide-within-repo-rules-owner-decides-the-hard-to-reverse-list.md): defines which architecture changes are big, including large restructures, which 0008 left to the agent.
- Implements the design evolution protocol named in [0018](0018-project-knowledge-system-decision-records-architecture-md-levelled-ddd.md).
- Roadmap, kept here and not in shipped text: friction signals reach the owner through the end-of-task summary until a findings pipeline exists (TASK-9); a fuller safe-move protocol may follow in a later template version.

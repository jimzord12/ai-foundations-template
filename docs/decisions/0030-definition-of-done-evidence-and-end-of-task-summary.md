---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: product
supersedes: []
---

# Definition of done, evidence and end-of-task summary

## Context and Problem Statement

The owner's practice from earlier projects: a green test does not prove behaviour; agents run the real thing and show evidence; committed, pushed, tested and integrated are separate facts; a test that passes with the implementation deleted must not be written. Generated projects did not say any of this, and several protocols were already sending items to an "end-of-task summary" that nobody defined. TASK-15.

## Considered Options

- Keep evidence and done rules as one line in AGENTS.md "Talking to the owner".
- A `docs/protocols/done.md` that owns done, evidence, tests and the end-of-task summary, with a short always-loaded section in AGENTS.md.

## Decision Outcome

Chosen option: "A `docs/protocols/done.md` …", because the summary needs one owner that charter.md, git.md and evolution.md can point to, and the evidence rule should not sit under a section personal instructions may override.

- Done: proven by running the real thing; checks pass (`npm run check`, or git.md's fallback definition); merged and pushed; summary given.
- Evidence: short, readable in under a minute, proving behaviour on the real local stack; the owner's final check is using the product.
- Tests: exercise the real implementation; mocks only at true external boundaries; never the database or the project's own modules when they can run locally.
- End-of-task summary: decisions (one line each, including structural changes), evidence, what waits on the owner, and a Findings section for the agent's own observations that other protocols extend with subsections; empty parts are left out or fold into one line, and Findings always appears.
- Backlog Definition of Done defaults: Backlog.md 1.52 refuses `config set definitionOfDone`, and [0014](0014-generated-projects-use-backlog-md-and-ignore-local.md) rejected shipping a pre-made `backlog/config.yml`. So done.md holds the exact `definition_of_done` line, and AGENTS.md tells the agent to add it when the key is missing, which also covers projects whose backlog already exists.

### Consequences

- Good, because every protocol now reports into one summary with one name.
- Bad, because the Definition of Done line is a manual step until a post-copy task could do it.

## More Information

- Subagent findings ([0011](0011-findings-are-ephemeral-proposals-are-github-issues-with-occurrence-counts.md)) are separate from the agent's own Findings section.
- [0028](0028-authority-tiers-and-design-evolution-protocol.md) and [0029](0029-git-and-safety-rules-for-generated-projects.md) send items into the summary.

---
status: accepted
date: 2026-10-02
decision-makers: owner
kind: architecture
supersedes: []
---

# Every protocol starts with a checked protocol card

## Context and Problem Statement

A protocol is spread across several folders: its rules in `docs/protocols/`, agent profiles in `.claude/agents/`, shared skills in `.claude/skills/` and their Codex copy in `.agents/skills/`. The folders are fixed by the tools (Claude Code and Codex look only there), so the pieces cannot live together. Before this change the only links between them were sentences, so adding a protocol (the planned lab protocol, a self-improvement loop) meant remembering every place by hand, and nothing caught a missed one. The owner wants protocols standardised before more are added (TASK-34).

## Considered Options

- Leave protocols as free-form markdown.
- One folder per protocol holding all its pieces.
- A short card at the top of each protocol file, checked by a script.
- A card with per-protocol versions and a UI to browse them.

## Decision Outcome

Chosen option: "A short card at the top of each protocol file, checked by a script", because it gives every protocol the same shape and makes missing pieces fail a check, without moving files the tools need where they are.

- The card is YAML frontmatter: `protocol`, `kind` (`process` or `rule`), `status` (`draft`, `active`, `retired`), `summary`, `applies-when`, and for processes `ends-when` and `produces`, then the lists `agents`, `skills` and `related`. Format and upkeep: `template/docs/protocols/agents.md` "Protocol cards".
- `kind` exists because six of the eight protocols are standing rules (git, charter, done, evolution, typescript, agents) with no end; only processes (review, ready) get `ends-when` and `produces`.
- `scripts/protocol_check.py` fails on a missing or malformed card, a name that does not exist, an agent profile or shared skill no card lists, and a protocol that is not retired but has no row in the "When to read what" table of `template/AGENTS.md.jinja`. That table is the index of protocols, so no separate index file is generated; `git` and `done`, reached before only from rule lines, got rows. The parser accepts only plain one-line values that load as the same YAML, so a future reader of the cards gets what the check saw.
- No per-protocol version: the template is versioned as a whole by its Copier tags, and one owner gains nothing from eight version numbers.
- No UI now: eight short files and the router table are enough. The phase-4 viewer ([0015](0015-the-generic-viewer-gets-its-own-repo-not-this-template.md)) can read the cards later.
- No decision links on the card: protocol files are copied into generated projects, whose `docs/decisions/` numbering differs, so a number from this repo would point at the wrong record there.

### Consequences

- Good, because a new protocol has a fixed shape to fill, and the check lists what it still lacks.
- Good, because an orphaned agent or skill, or a renamed one a card still names, fails the check.
- Bad, because the check runs only in this repo, on `template/`; a generated project that adds its own protocol keeps the card format but has no script yet.
- Bad, because the card's sentences can drift from the body text below them; only review catches that.

## More Information

- The check follows the stdlib-only style of `scripts/dogfood_check.py` ([0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md)). The router that holds the index is the thin AGENTS.md of [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md).
- Follow-up candidates: ship the check in generated projects once they have a scripts convention, and a `draft` card for the lab protocol (DRAFT-2), whose planned `lab-examples.md` would need its own card and row, or a home outside `docs/protocols/`.

---
name: context-lenses
description: Lenses for a change to instruction files (AGENTS.md, CLAUDE.md, protocols, agent profiles, skills). Preloaded by the context-reviewer and context-maintainer profiles; do not invoke in the main session.
user-invocable: false
---

# Lenses for instruction files

Instruction files are every file an agent reads as instructions: AGENTS.md, CLAUDE.md, the project's protocols, agent profiles and skills. They are one maintained system, not a pile of prompts: a rule in the wrong file is worse than no rule, because the next reader finds two files that disagree. A writer applies every lens before handing a change over; a reviewer leads with the lenses named for the round (the table at the end when none are named), then covers the rest briefly.

## Before you read the diff

From the brief alone, write down the principle the change should capture (the feedback or task behind it), two or three cases it must cover and one it must not. The diff must not be what tells you what the feedback meant. Then read the diff, each touched file whole, and the files that point at, restate or apply the rule: the router in AGENTS.md, CLAUDE.md, and the profiles and skills that load or repeat it.

## Lenses

- **Principle:** the text states the principle, not only the triggering example. It fires on the triggering case and on your other cases, and stays silent where it should. Overfit: only the example is covered. Over-general: it would fire on every sentence, or turns into a mechanical pattern nobody asked for. It does not contradict or half-repeat guidance nearby.
- **Placement:** the rule sits in the file that owns that kind of guidance, as the AGENTS.md router and the project's protocols describe, where present. One owner per rule: other files point to it and change only where they would otherwise contradict it. Search for the concept to find a better owner, a duplicate, or a pointer that should have changed. The owner's personal preferences (tone, format) belong in their personal instructions, not in tracked files.
- **Integration:** where existing guidance already said part of it, that guidance was amended, extended in its own shape or merged; a paragraph appended beside the owner is a finding even when the words are right. Headings, list and table shapes, sentence length and tone match the surrounding text. Nothing is touched that the feedback does not reach.
- **Terms:** domain words as the project's glossary spells them, where it keeps one; code identifiers exactly as the code spells them (check the source, not memory). A new term goes into the glossary in the same change.
- **Timeless:** instruction files carry no dates (except when an external fact was last verified: "checked against X on <date>"), task or finding numbers, people's names or quotes from a conversation; provenance belongs in a dated record (a decision record, a log, task notes). A dated record is never edited to carry a rule; a changed decision is a new record, as the decisions README says.
- **Literal reader:** an agent that follows the text exactly, with no memory of why it was written, must not cause harm or stall. Every condition and exception is stated; nothing asks for a tool the reader lacks, or for an answer nobody can give while the owner is away; no step loops without an exit. Wherever an override clause (project rules, personal instructions) touches an "only for" or "never" list, the list says whether an override may tighten it, loosen it, or both.
- **Frontmatter:** a profile's or skill's description says what it does and when to use it, so the caller picks it for the right job. Tools are listed explicitly (leaving them out grants every tool) and are the least the job needs: read-only roles get no Edit or Write, only orchestrators get Agent, and the body never asks for a tool the list lacks. Model and effort fit the job: judgement-heavy roles get the strongest model, bounded mechanical ones a cheaper one; a turn limit is set. Preloaded skills exist, are hidden from the slash menu (`user-invocable: false`) and never set `disable-model-invocation`, which stops preloading.
- **Reachability:** a file no pointer names is as absent as one never written. A new protocol gets a row in the AGENTS.md router or a pointer from the file that sends readers to it; a new skill is preloaded by a profile or described so that it triggers; every path in the text resolves to a file in this project. A rename or removal leaves no stale pointer.
- **Budget:** AGENTS.md is loaded in every session, so it holds only the rules every session needs plus pointers, within about 100 lines unless the project sets another budget; detail lives in protocols. Preloaded skills add context to every run of their profiles, so they stay tight. Nothing is longer than it needs to be.
- **Parity:** AGENTS.md is shared by every agent tool (Claude Code reads it through CLAUDE.md, Codex reads it directly). A rule every agent must follow lives in AGENTS.md or a file it points to, never only in a Claude-only file (CLAUDE.md, agent profiles, `.claude/settings.json`). Shared text that names a Claude-only feature, such as a subagent profile, still tells an agent without it what to do. Codex reads shared skills from `.agents/skills/`, a copy of `.claude/skills/`; a skill changed in one folder only is a Parity finding.

## Guards against overcorrection

- A finding names the reader who goes wrong and what they do; "could be clearer" is Minor at most.
- Fix the rule that already exists before adding one; deleting or merging text often beats adding.
- No reflex caveats, exceptions, emphasis (capitals, "IMPORTANT") or an example for every case.
- One incident does not justify a sweeping rule, and a fix does not swing to the opposite extreme: a rule against asking too often must not forbid asking.
- Do not ask for completeness the project's quality bar does not need, or for rewording text that was not wrong.

## Severity for instruction files

- **Blocking:** contradicts a standing rule or decision, misstates a term or identifier, or would drive agents to harmful or wrong behaviour.
- **Material:** wrong file or section, duplicated or overfitted guidance, a mechanical pattern nobody asked for, an unrelated edit, a broken or missing pointer, a date or quote in a timeless file, a tool grant wider than the job.
- **Minor:** wording or formatting drift a reader would notice but not misread.

A change that holds the requested sentence in the wrong place, or beside a rule it now half-duplicates, is a finding, not a near miss.

## Lead lenses by round

| Round | Lead lenses |
|---|---|
| 1 | Principle, Placement |
| 2 | Literal reader, Reachability |
| 3 | Integration, Terms |
| 4 | Frontmatter, Parity |
| 5 | Budget, Timeless |
| 6 | The reviewer's own choice, stated at the top of the report |

From round 7, start again at round 1. A change plainly about one lens may lead with it in round 1; the brief says so. Blocking findings are reported from any lens in any round.

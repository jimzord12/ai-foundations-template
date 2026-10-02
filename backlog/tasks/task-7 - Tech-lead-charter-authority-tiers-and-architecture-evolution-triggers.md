---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: In Progress
assignee:
  - '@claude'
created_date: '2026-09-29 11:39'
updated_date: '2026-10-02 00:09'
labels:
  - instructions
  - charter
  - ready
milestone: m-0
dependencies:
  - TASK-25
priority: high
type: feature
ordinal: 200
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The main agent acts as tech lead and senior engineer and owns the codebase; the owner is a technical product owner who does not want to babysit. Agents need explicit rules for what they decide alone (bounded by the repo's instruction files) versus what goes to the owner (hard-to-reverse list), and concrete signals for when to move from simple code to patterns to restructured folders.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Authority tiers moved from the AGENTS.md section Who decides what into docs/protocols/charter.md with the mapping per decision kind (product: owner; architecture: agent proposes, owner approves big ones; technical: agent decides and logs); AGENTS.md keeps a short pointer
- [ ] #2 Design evolution protocol in docs/protocols/evolution.md: measurable signals, procedure (architecture decision record, owner approval for big changes, pure-move commit then reference commit, update architecture.md and glossary in the same change, tests and review pass), step-down rule
- [ ] #3 Decision named Design evolution protocol and authority tiers recorded; smoke test passes
- [ ] #4 Interim rules stated where Phase 2 is not built yet: friction signals come from the end-of-task summary until a findings pipeline exists; the full safe-move protocol arrives in a later template version. Shipped text never names this repo's task IDs
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Stop condition: start only after TASK-31 is merged into main (record 0027 exists on main); branch feature/task-7-charter from main. New record is 0028.
2. Rule ownership (one owner per rule): hard-to-reverse list lives in AGENTS.md only (charter.md references it and adds the procedure: options, tradeoffs, recommendation); kind mapping stays as one always-loaded line in AGENTS.md, charter.md owns the detail (the 'big' test, bands, unattended behaviour); template docs/decisions/README.md keeps kind definitions and says 'who decides: see docs/protocols/charter.md', and keeps pointing at AGENTS.md for the hard-to-reverse list; supersede wording lives only in the decisions README (drop the duplicate AGENTS.md line); the end-of-task one-line-per-decision rule stays one line in AGENTS.md, done.md (TASK-15) is its detailed owner, charter.md does not restate it; charter.md links to AGENTS.md Roles instead of restating them. AGENTS.md line 8 override clause names docs/protocols/charter.md too.
3. template/docs/protocols/charter.md: authority per kind in detail; 'big' architecture change = any of: adds, removes or moves a boundary or layer named in architecture.md; adopts a project-wide pattern (including DDD tactical patterns, glossary level 3); moves or renames files across more than one top-level folder or more than about 15 files; breaking change to an API existing consumers use; a data change that transforms or drops existing data. Adding fields or endpoints is not big. Unattended: write the record as proposed, do not build the big part, continue other work, surface it in the end-of-task summary.
4. template/docs/protocols/evolution.md: ladder (inline, function, module, pattern or interface, folder restructure, ports and adapters at a boundary); signals: second copy note it, third extract it; a file over about 300 lines or a function over about 50 in code you are already changing (signals to consider, never a reason to refactor untouched code, never lint errors); the same kind of change keeps needing edits in the same scattered places, seen twice (not counting tests or the layers architecture.md says every feature touches); the same bug fixed twice; test setup pain (a test needs to mock the project's own modules, or setup outgrows the assertions); a second business area means glossary level 2. Port trigger: code talks to an external service, device or provider that tests must replace or that has or will plausibly get a second provider; a port at a true external boundary is never stepped down. Three bands: routine (extract a helper or module) no record; structural (changes what architecture.md describes) record accepted by the agent, update architecture.md and glossary, mention in summary; big (charter.md test) record proposed until the owner approves. Move procedure: a pure-move commit (moves, renames, reference updates only) with checks green, then separate behaviour commits. Step-down: remove an abstraction with one implementation and no second in sight, or indirection nobody uses, through a new record (never a port at a true external boundary). Report friction signals you noticed but did not act on in your end-of-task summary. No roadmap wording, no task IDs.
5. template/AGENTS.md.jinja: Who decides what keeps the kind mapping line and the hard-to-reverse line, plus a pointer to charter.md; supersede line dropped; Evolve section becomes one ladder line with the rule of three plus pointer; router rows: 'Deciding who approves (product, architecture, technical)' -> charter.md; 'Copied code, a long file or function, a repeat bug, a change scattered across places, painful test setup' -> evolution.md. Net change <= +4 lines; rendered <= 100.
6. Record 0028 (kind product, decision-makers owner): one owner-approved design covering authority tiers and the evolution protocol; More Information: narrows 0008 (owner gate for big changes), implements 0018; roadmap note (findings pipeline later) lives here, not in shipped text. Index row.
7. Verify: smoke test 3 stacks (files, no Jinja leftovers, line count <= 100, router paths exist); moved-rule table in notes mapping old AGENTS.md lines 23-27 and 30 to new homes; grep -rn 'Who decides what|Evolve the codebase' template/ shows only valid references; leak grep -rnE 'TASK-[0-9]|task-[0-9]|Phase [0-9]|findings pipeline|0008|0018' template/ (adr-template "0003" example allowed).
8. Review loop to PASS; merge, push, delete branch.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of authority tiers (who decides what). TASK-25 references these tiers for who decides each decision kind instead of restating them.

Moved-rule table (old template AGENTS.md line -> new home): 23 'You decide' -> stays in AGENTS.md; 24 kind mapping -> stays (one line) plus pointer to charter.md for 'big'; 25 hard-to-reverse list -> stays in AGENTS.md only (charter.md references it); 26 supersede wording -> removed from AGENTS.md, owned by docs/decisions/README.md line 8; 27 end-of-task decision summary -> stays (done.md will own detail, TASK-15 note); 30 Evolve paragraph -> one ladder line plus rule of three in AGENTS.md, signals/bands/move/step-down in evolution.md, interim proposal-pipeline wording dropped (roadmap moved to record 0028). Verification: smoke express/next/rn exit 0, AGENTS.md 57/58/57 lines (was 55/56/55), no Jinja leftovers, all router paths exist except the docs/adr/ brownfield example; reference grep shows only valid 'Who decides what' / 'Evolve the codebase' references; leak grep (TASK-, task-, Phase N, findings pipeline, 0008, 0018) finds nothing in template/.
<!-- SECTION:NOTES:END -->

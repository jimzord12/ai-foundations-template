---
id: TASK-7
title: 'Tech-lead charter: authority tiers and architecture-evolution triggers'
status: Done
assignee:
  - '@claude'
created_date: '2026-09-29 11:39'
updated_date: '2026-10-02 00:13'
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
- [x] #1 Authority tiers moved from the AGENTS.md section Who decides what into docs/protocols/charter.md with the mapping per decision kind (product: owner; architecture: agent proposes, owner approves big ones; technical: agent decides and logs); AGENTS.md keeps a short pointer
- [x] #2 Design evolution protocol in docs/protocols/evolution.md: measurable signals, procedure (architecture decision record, owner approval for big changes, pure-move commit then reference commit, update architecture.md and glossary in the same change, tests and review pass), step-down rule
- [x] #3 Decision named Design evolution protocol and authority tiers recorded; smoke test passes
- [x] #4 Interim rules stated where Phase 2 is not built yet: friction signals come from the end-of-task summary until a findings pipeline exists; the full safe-move protocol arrives in a later template version. Shipped text never names this repo's task IDs
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [x] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [x] #3 Independent review loop reached PASS for non-trivial changes
- [x] #4 Non-trivial decisions recorded in docs/decisions/
- [x] #5 Committed and pushed
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

Review round 1 FINDINGS (3 Material, 6 Minor, 3 Notes), all fixed: M1 owner-away covers big changes, hard-to-reverse items and open product questions; product row lets the agent fill details inside agreed scope; M2 a new project's first structure and a single port are structural, not big; M3 plan v2 restored (multi-line args through the Windows backlog shim lose everything after the first newline; pass them from bash); m1 AGENTS.md architecture wording aligned ('you decide, except big changes'); m2 rule of three owned by AGENTS.md; m3 big-list items narrowed (source folders, external API consumers, production or shared data); m4 router rows reach evolution.md for structure changes and external services; m5 step-down record only if one exists; m6 'any review step the project uses'; n1 0028/0008 link wording; n3 port trigger 'has or has a planned second provider'. AC2 note: the move procedure is move plus reference updates in one commit, then behaviour commits (moving without updating references would break the checks). AC4 note: the interim friction rule ships as a current rule; roadmap wording lives only in 0028.

Review round 2 PASS (0 Blocking/Material). Minors applied after PASS: big-list item 3 now 'reorganizes the top-level source folders'; options sentence follows owner-away only when the owner is away; step-down follows the normal bands; duplicate DDD line removed from evolution.md; decisions README says accepted architecture decisions update architecture.md. Smoke re-run: 57/58/57 lines, exit 0.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Generated projects get docs/protocols/charter.md (authority per decision kind, a concrete test for big architecture changes that need the owner, and what to do when the owner is away) and docs/protocols/evolution.md (ladder, signals that apply only to code being changed, port trigger, routine/structural/big ceremony bands, safe-move commits, step-down rule). AGENTS.md keeps the always-loaded gates (kind mapping, hard-to-reverse list), protects charter.md from personal overrides, and routes to both files by signal; rendered AGENTS.md grew 2 lines (57/58/57). Record 0028 with 0008/0018 links. Verified by smoke test on all three stacks, router-path, reference and leak greps. Review: round 1 FINDINGS (3 Material, 6 Minor) fixed, round 2 PASS.
<!-- SECTION:FINAL_SUMMARY:END -->

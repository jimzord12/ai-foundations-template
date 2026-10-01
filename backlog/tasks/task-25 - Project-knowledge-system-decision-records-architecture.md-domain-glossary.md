---
id: TASK-25
title: 'Project knowledge system: decision records, architecture.md, domain glossary'
status: In Progress
assignee:
  - '@claude'
created_date: '2026-10-01 19:29'
updated_date: '2026-10-01 21:38'
labels:
  - knowledge
  - decisions
  - ddd
  - ready
milestone: m-0
dependencies: []
priority: high
type: feature
ordinal: 100
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner-approved design (2026-10-01, see docs/decisions.md). Generated projects get one knowledge system, separate from the feedback loop and linked to it only through decision records. (1) Decisions: one file per decision in docs/decisions/ using the MADR standard, front matter with kind (product | architecture | technical), status, date, deciders, supersedes; an index README. Who decides: product = owner; architecture = agent proposes, owner approves big ones; technical = agent decides and logs. (2) docs/architecture.md = the current shape (folder map, layers, key flows, links to decisions); starts nearly empty and must be updated in the same change as every accepted architecture decision. (3) DDD, mandatory but levelled: level 1 always on = docs/domain/glossary.md (term, meaning, not-this, context; agents use terms in code and UI, add terms, flag synonyms); level 2 when a second business area appears = docs/domain/contexts.md; level 3 tactical patterns only via architecture decisions. Replaces the single-file docs/decisions.md for generated projects and absorbs TASK-5. Verify the current MADR version before adopting its template.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 template/docs/decisions/ ships a MADR-based record template with kind, status, date, deciders, supersedes, plus an index; template/docs/decisions.md removed
- [x] #2 template/docs/architecture.md and template/docs/domain/glossary.md ship as short starters; contexts.md documented as level 2, created only when needed
- [x] #3 Template AGENTS.md: check decisions before deciding, update architecture.md with every architecture decision, use and maintain the glossary, and if the project already has an ADR folder use it instead (brownfield rule kept); for who decides each kind, point to the Who decides what section (TASK-7 later moves it)
- [x] #4 This repo migrates its own docs/decisions.md to one file per decision (owner answer 2026-10-01) and updates in the same change every reference: root AGENTS.md, README, docs/agent-instructions.md, backlog config definition_of_done, every task's description, acceptance criteria and Definition of Done items that name docs/decisions.md
- [x] #5 Smoke test passes for all stacks; rendered AGENTS.md stays within the line budget
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [x] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [x] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [x] #3 Independent review loop reached PASS for non-trivial changes
- [x] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
1. Work on a feature branch (blocked 2026-10-02: branch creation denied by the auto-mode classifier; work stays uncommitted on the working tree until the owner allows it).
2. Template: template/docs/decisions/README.md (how records work: kinds and who decides each, statuses, numbering NNNN-slug.md, supersedes means explicit replacement only, add an index row with every record) and template/docs/decisions/adr-template.md (MADR 4.0.0 minimal variant: front matter status, date, decision-makers, plus extensions kind and supersedes; MADR 4 renamed deciders to decision-makers, recorded in 0026). Remove template/docs/decisions.md.
3. Template: template/docs/architecture.md.jinja (short starter; no MADR braces) and template/docs/domain/glossary.md (Term | Meaning | Not this | Context; level 2 contexts.md when a second business area appears; level 3 only via architecture decisions).
4. Template AGENTS.md.jinja: Decision log section rewritten (one file per decision, check before deciding, architecture decisions update architecture.md in the same change, glossary use, existing ADR folder wins, backlog/decisions is not it, add an index row) and Who decides what gets the kind mapping (product owner; architecture agent proposes, owner approves big ones; technical agent decides and logs) and supersede wording via a new record with supersedes; router rows updated; net growth at most 4 lines; rendered <= 100 lines.
5. This repo: scratchpad script converts the 25 entries into docs/decisions/0001-0025 (titles verbatim; bodies verbatim under MADR headings; kind per entry; supersedes only for explicit replacement: 0007 -> 0002, 0015 -> 0010 with 0010 status superseded; refinements and narrowing go in More Information as links). Content check per record: every original field string appears verbatim in its own record. Add 0026 for the migration. docs/decisions/README.md index. Delete docs/decisions.md.
6. References updated: root AGENTS.md, README (lines 5, 27, 34), docs/agent-instructions.md status header (body is superseded history, left verbatim; header says so), backlog/config.yml definition_of_done, doc-1, and open tasks' description, AC and DoD text via backlog CLI (DoD: remove #5 then #4 and re-add both in order; AC replacements re-check any checked items).
7. Verify: smoke test 3 stacks (files present, no Jinja leftovers, AGENTS.md <= 100 lines, router links exist); 25 records + 0026 match index rows; per-record content check; grep for docs/decisions.md allows only: docs/decisions/0*.md bodies, docs/agent-instructions.md body, backlog/archive/, TASK-1, TASK-25's own description and AC.
8. Independent review loop to PASS. Commit, merge and branch deletion wait for the owner to allow branch creation.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-02 plan challenge round 1 NOT READY; all findings were explicit fixes (count 25, per-record content check, named allowed grep hits, Who decides what mapping, DoD order, supersedes semantics, decision-makers naming) and are folded into plan v2; proceeding without a second plan round, like the earlier TASK-24 precedent.

2026-10-02 review round 1 FINDINGS (1 Material, 6 Minor, 3 Notes), all fixed: M1 hard-to-reverse list beats kind=technical (template README + AGENTS.md); m1 0007 is a partial replacement of 0002, so supersedes dropped (deviates from plan v2 step 5) and 0002 gets More Information backlinks to 0007/0008; m2 0026 warns copier update deletes a pre-change docs/decisions.md; m3 brownfield rule covers single-file logs again; m4 'decision log' wording; m5 repo index points to template format and ADR template; m6 architecture starter no longer asserts src/; n1 decision-makers default agent, proposed until owner approves; n2 template comment says minimal plus full-template parts; n3 three truncated slugs renamed (0011, 0016, 0017).

2026-10-02 review round 2 PASS (0 Blocking/Material). Evidence: 25/25 records match the old log verbatim (title, date, every field); 42 links into docs/decisions/ resolve; grep for docs/decisions.md hits only allowed history spots; copier update from a pre-change render deletes docs/decisions.md, as 0026 now warns; render express/next/rn 55/56/55 lines, no Jinja leftovers, router paths exist. Round-2 Minors applied after PASS: 'replace' vs 'refine or narrow' wording (template AGENTS.md + repo index), back-links 0004<-0007 and 0023<-0024, template README defers to an existing decision location. Smoke re-run green. Plan step 5's '0007 -> 0002' is superseded by the round-1 note. Open: DoD #5 (commit, merge) waits for branch creation, denied by the auto-mode classifier.
<!-- SECTION:NOTES:END -->

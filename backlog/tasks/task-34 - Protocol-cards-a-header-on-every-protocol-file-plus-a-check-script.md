---
id: TASK-34
title: 'Protocol cards: a header on every protocol file plus a check script'
status: Done
assignee:
  - '@claude'
created_date: '2026-10-02 15:59'
updated_date: '2026-10-02 16:21'
labels:
  - feature
dependencies: []
priority: high
ordinal: 24000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
A protocol is spread across several places: the rules file in docs/protocols/, agent profiles in .claude/agents/, shared skills in .claude/skills/ (and the Codex copies). Nothing says which pieces belong together; the links are sentences. Adding a new protocol (lab, self-improvement loop) means remembering every place by hand, and nothing catches a missed one. The owner wants protocols standardised before more are added. Discussed with the owner on 2026-10-02: a short YAML card at the top of each protocol file, plus a check. Per-protocol versions and a UI were explicitly rejected for now.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Every file in template/docs/protocols/ starts with a card stating its id, kind (process or rule), status, summary, when it applies, and the agents, skills and related protocols it uses; process cards also say when it ends and what it produces
- [x] #2 A check script fails when a card is missing or malformed, names an agent, skill or protocol that does not exist, when an agent profile or shared skill belongs to no protocol, or when a protocol is not routed from template/AGENTS.md.jinja
- [x] #3 The card format and the rule to keep it are documented where agents in generated projects will read them, and this repo's AGENTS.md names the check
- [x] #4 A decision record explains the card and why versions, a UI and decision links were left out
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
1. Branch feature/protocol-cards.
2. Card format: YAML frontmatter with protocol, kind (process|rule), status (draft|active|retired), summary, applies-when, ends-when + produces (process only), agents, skills, related. No decision links (numbering differs per project), no versions.
3. Subagent writes the eight cards from the full protocol texts.
4. scripts/protocol_check.py (stdlib only, like dogfood_check.py): validates cards against template/.claude and template/AGENTS.md.jinja; flags orphan agents and skills.
5. Document the card in template/docs/protocols/agents.md; name the check in AGENTS.md; decision record 0039.
6. dogfood sync, protocol check, smoke test x3 stacks, review loop, merge.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
Attended run; owner asked to do it now (ready gate waived by the owner).

Review loop: 3 rounds, three reviewers each (context-reviewer, code-reviewer, docs-reviewer). R1 FINDINGS (wrong router heading, status meanings, loose routing, non-YAML values), all fixed. R2 context PASS; code and docs FINDINGS (YAML divergences such as yes/null/#1, committed .pyc), fixed. R3 PASS on all three; their Minors applied (clear unknown-key errors, printable values, letter-first names). Router gained rows for git.md and done.md; the "When to read what" table is now the protocol index and only its last cell counts. Evidence: protocol_check 8 cards 0 problems; planted breaks (renamed agent, unknown key, rule with ends-when, unrouted, colon, backtick, #, empty item, list kind, BOM, trailing space, prose-only route, stack-only route, Situation-column route, heading renamed, misspelled key) each fail with a clear message; 100k fuzzed values incl. control chars vs PyYAML safe_load, 0 mismatches; smoke render passes on express, next, rn; dogfood_check 0 problems.

Renumbered the decision record from 0039 to 0040 at merge time: a parallel session landed 0039 (delete what is safely deletable) on main first. The plan above still says 0039; read it as 0040.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Every protocol in template/docs/protocols/ now starts with a YAML protocol card (id, kind process|rule, status, summary, applies-when, ends-when/produces for processes, agents, skills, related). scripts/protocol_check.py (stdlib) fails on missing or malformed cards, unknown names, orphan profiles or skills, and protocols without a row in the router table, and only accepts values that load as the same YAML. Format documented in docs/protocols/agents.md "Protocol cards"; decision 0040. Verified with the check, planted breaks, a PyYAML fuzz comparison and the three-stack smoke test; review loop PASS in round 3. Follow-ups not created: ship the check to generated projects; a draft card for the lab protocol (DRAFT-2) and a home for lab-examples.md.
<!-- SECTION:FINAL_SUMMARY:END -->

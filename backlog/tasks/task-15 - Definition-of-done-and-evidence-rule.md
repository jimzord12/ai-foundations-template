---
id: TASK-15
title: Definition of done and evidence rule
status: Done
assignee:
  - '@claude'
created_date: '2026-09-29 19:49'
updated_date: '2026-10-02 00:25'
labels:
  - instructions
  - verification
  - ready
milestone: m-0
dependencies:
  - TASK-14
priority: high
type: feature
ordinal: 400
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner practice from agentic-wave and Night Shift: a green test does not prove behavior; agents run the real thing and show evidence; committed, pushed, tested and integrated are reported as separate facts; a test that passes with the implementation deleted must not be written. Needs to be part of what every generated project tells its agents. May overlap with TASK-2 (tests and CI per stack).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Definition of done written for generated projects (docs/protocols/done.md plus at most 4 non-blank lines in AGENTS.md), referencing npm run check by name, with git.md's checks definition as the fallback
- [x] #2 Covers: real-run evidence over claims (short, readable in under a minute), separate git and test facts, tests must exercise real code, mocks only at true external boundaries; done.md owns the evidence rule and AGENTS.md 'Talking to the owner' points to it
- [x] #3 Generated projects get Backlog Definition of Done defaults derived from done.md (not this repo's template-only items such as the smoke test): done.md holds the exact definition_of_done line and AGENTS.md says to add it to backlog/config.yml when the key is missing (Backlog 1.52 refuses config set definitionOfDone); proven by a throwaway project whose new task carries those items
- [x] #4 Decision recorded; smoke test passes
- [x] #5 docs/protocols/done.md defines the end-of-task summary (one name across the template) the lead agent gives the owner: decisions taken (one line each), evidence, what waits on the owner (items charter.md and git.md send there), and a Findings section for the agent's own observations (not a relay of subagent reports), which other protocols extend with subsections; an empty subsection folds into one line and an all-empty section is 'Findings: none'
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
1. Start after TASK-14 merges; branch feature/task-15-done from main; next free record number (0030 expected).
2. template/docs/protocols/done.md (owner of the definition of done, the evidence rule and the end-of-task summary):
   - Done means: the behaviour is proven by running the real thing; checks pass (`npm run check`, or as git.md "Merging" defines checks); merged and pushed per git.md (referenced, not restated); the end-of-task summary is given.
   - Evidence: short, readable in under a minute: a command and its result, a screenshot, or a log excerpt that proves the behaviour, not the code; run against the real local stack (local database, local server, emulator or device) whenever it can run locally. The owner's final check is using the product; evidence prepares it, it does not replace it.
   - Separate facts: committed, pushed, merged, checks passing and running in the real app are reported separately; never imply one from another.
   - Tests: every test exercises the real implementation; a test that would still pass with the implementation deleted must not be written; mocks only at true external boundaries (third-party network services, payment or other providers, hardware, the clock), ideally replacing the provider at its port (evolution.md); never mock the database or the project's own modules when the real thing can run locally.
   - End-of-task summary (keep this name; other protocols already send items to it): decisions taken, one line each; evidence; waiting on the owner (proposed records and open product questions from charter.md; ask-first actions skipped while the owner was away from git.md); a Findings section with your own observations, not a relay of what subagents reported (structural changes and friction not acted on from evolution.md); other protocols add Findings subsections; an empty subsection folds into one line (for example 'Lint/CI: none'), and when every subsection is empty the section is 'Findings: none'. This is content only; the owner's personal format (for example a recap or next-move line) still applies.
   - Backlog Definition of Done defaults: if backlog/config.yml has no definition_of_done key, add this exact line (the CLI refuses `config set definitionOfDone`): definition_of_done: ["Every acceptance criterion verified with evidence (command and result, screenshot or log)", "Checks pass (npm run check)", "Review reached PASS for non-trivial changes", "Non-trivial decisions recorded in docs/decisions/", "Merged into main and the feature branch deleted"]. A project's own existing DoD is left alone.
3. template/AGENTS.md.jinja: new "## Done" section after "Git and safety", before the router, with 2 bullets: (a) done means proven by running the real thing, checks green and merged; report committed, pushed, merged and checks as separate facts; (b) tests exercise real code, mocks only at true external boundaries; detail, evidence and the end-of-task summary: docs/protocols/done.md. In place (no new lines): 'Talking to the owner' evidence bullet becomes "Keep verified facts apart from assumptions; evidence rules: docs/protocols/done.md"; 'Who decides what' last bullet becomes "End every task with the end-of-task summary in docs/protocols/done.md (decisions one line each)"; Work tracking line adds: if backlog/config.yml has no definition_of_done, add the line from done.md. Net growth <= 4 non-blank lines; rendered <= 100.
4. Record (kind product, owner): definition of done, evidence rule, end-of-task summary, DoD defaults mechanism; More Information links 0011, 0014 (no pre-made config), 0028, 0029.
5. Notes: TASK-2.4 (done.md and the DoD line depend on the script being named check).
6. Verify: smoke test 3 stacks (files, no Jinja leftovers, line count, router and pointer paths); real DoD proof outside any repo using BACKLOG_CWD (cd fails in the Bash tool): git init, backlog init --defaults --agent-instructions none, grep the definition_of_done line out of the rendered done.md and append it to backlog/config.yml, create a task, show its DoD holds the five items; leak grep in template/ (task IDs, smoke test, 'Committed and pushed'); grep that 'end-of-task report' does not appear (one name: summary).
7. Review loop to PASS; merge, push, delete branch.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: owns the done rule text; TASK-2 subtasks own the tooling it refers to.

2026-10-02 (TASK-7 readiness): done.md is the detailed owner of the end-of-task one-line-per-decision summary; AGENTS.md keeps the one rule line and charter.md does not restate it.

2026-10-02 readiness round 1 NOT READY: 3 Material (two owners for the evidence rule, 'report' vs 'summary' naming, DoD line only for new backlogs) and 8 Minor, all explicit fixes folded into plan v2 and ACs; challenger proved the definition_of_done line works in a throwaway backlog (5 items on a new task). Proceeding without another round.

Verification: smoke express/next/rn exit 0, AGENTS.md 66/67/66 lines (52/53/52 non-blank; +3 non-blank vs main), no Jinja leftovers, all pointers resolve except the docs/adr/ example. DoD proof: throwaway repo outside any repo via BACKLOG_CWD, backlog init (config had no definition_of_done), appended the line grepped from the rendered done.md, created a task: its DoD showed the five items #1-#5. Leak grep clean. 'end-of-task report' appears nowhere; 'end-of-task summary' is the single name.

Review round 1 PASS (0 Blocking/Material); reviewer reproduced the DoD line in a throwaway backlog (survives a config rewrite). Minors applied after PASS: structural changes listed under Decisions; unmerged changes with unresolved review findings under Waiting on the owner; DoD item says merged, pushed and branch deleted; empty sections 1-3 left out, Findings always shown; checks item names the git.md fallback; mock wording split; charter.md says end-of-task summary. Smoke re-run 66/67/66; YAML line parses to 5 items.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Generated projects get docs/protocols/done.md: done means proven by running the real thing, checks green, merged and pushed; short evidence on the real local stack; separate facts; tests that exercise real code with mocks only at true external boundaries; one end-of-task summary (decisions, evidence, waiting on the owner, Findings that other protocols extend); and the exact Backlog definition_of_done line, added when the key is missing because Backlog 1.52 refuses config set. AGENTS.md gets a two-bullet Done section and points its evidence and summary lines there (66/67/66 lines). Record 0030. Verified by smoke test, a real throwaway backlog showing the five DoD items, and leak greps. Review: round 1 PASS.
<!-- SECTION:FINAL_SUMMARY:END -->

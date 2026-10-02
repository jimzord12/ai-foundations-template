---
id: TASK-14
title: Git and safety rules in the template AGENTS.md
status: Done
assignee:
  - '@claude'
created_date: '2026-09-29 19:49'
updated_date: '2026-10-02 00:21'
labels:
  - instructions
  - git
  - ready
milestone: m-0
dependencies:
  - TASK-7
priority: high
type: feature
ordinal: 300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The generated AGENTS.md has no git or safety rules. Earlier projects (agentic-wave, cvgen, night-shift) had an impact-based rule: routine commits and pushes are allowed, high-impact actions (rewriting shared history, deleting unique work, touching production or security) require asking with the exact action and consequence. Needs a neutral default that per-project or personal rules can tighten.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 Git and safety rules in docs/protocols/git.md; AGENTS.md gets a Git and safety section of at most 3 bullets that points to git.md (no separate router row, to stay inside the 4-line budget); includes the rule that secrets never go in code, logs or commits
- [x] #2 Branch model per the decision 'Branch model refinements after the first instruction review': no pull requests; branch levels main, feature/x, feature/x-part, feature/x-part-step; every change on a feature branch; merge without asking once applicable checks pass and, for non-trivial changes, review PASS; delete merged branches; delete only temporary files the agent created
- [x] #3 Approval only for: deleting main or another core branch, merging into a core branch other than main unless the project's rules allow it (added during review, flagged for the owner), deleting an unmerged branch whose commits exist nowhere else (except the agent's own level-3 branches), any force push, reset --hard, git clean; each request shows the exact action, targets and consequence; the list lives once, in AGENTS.md, and personal instructions cannot loosen it; consistent with 0024's allowlist amendment (switch, branch, merge, push --delete); release-tag approval is a rule of this template repo only, not shipped
- [x] #4 git.md defines checks, review and non-trivial for projects that do not yet have a check script, CI or review protocol, without naming this repo's tasks
- [x] #5 Decision recorded; smoke test passes
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
1. Start after TASK-7 merges; branch feature/task-14-git from main. Check docs/decisions/README.md for the next free record number at branch time.
2. One owner per rule: the ask-first list lives only in AGENTS.md "Git and safety" (always loaded); git.md references it and adds how to ask (exact command, targets, consequence). AGENTS.md Roles line 8 adds the ask-first list to what personal instructions never override; git.md says a project may tighten the list, and loosening it needs an owner decision record.
3. template/docs/protocols/git.md:
   - Branch model: levels main -> feature/x (1) -> feature/x-part (2) -> feature/x-part-step (3), never deeper; no pull requests; every change, trivial ones included, on a feature branch.
   - Core branches: main and any long-lived branch the project names (for example production, stage, dev).
   - Merge gate: merge into main without asking once checks pass and, for a non-trivial change, review reached PASS; merges between feature levels need only the checks. Definitions: checks = the project's check script or CI where it exists; review = a fresh-context reviewer finds no Blocking or Material issue (per docs/protocols/review.md when present); non-trivial = changes behaviour, touches more than one file, or changes a test or an instruction file. Work is finished only when merged.
   - Cleanup: delete a feature branch locally and on the remote as soon as it is merged; core branches are never deleted after a merge; delete temporary files and scratch output you created; never delete untracked or ignored files you did not create.
   - Asking: the list is in AGENTS.md "Git and safety"; each request shows the exact command, the targets and the consequence.
   - Secrets: never in code, logs, commits, commit messages or task notes; .env files stay git-ignored; .env.example, where present, holds names only; if a secret was committed or pushed, stop and tell the owner (it must be rotated; rewriting history needs approval). No scanning text here.
   - Commits: small, one purpose, message says what and why (one line).
   - Nothing about tags or releases.
4. template/AGENTS.md.jinja: section "## Git and safety" with 3 lines: (a) every change on a feature branch, no pull requests; merge into main once checks pass and, for non-trivial changes, review PASS; then delete the branch; (b) ask first, with the exact command, only for: deleting main or another core branch, deleting an unmerged branch whose commits exist nowhere else (except level-3 branches you created), any force push, reset --hard, git clean; (c) never put secrets in code, logs or commits. Router row "Branching, merging, cleanup, destructive git, secrets | docs/protocols/git.md". Roles line 8 updated (step 2). Rendered <= 100 lines.
5. Record (kind product, decision-makers owner), short, only what is new beyond 0023/0024: tighten-only override rule, core-branch definition, secrets rule home, checks/review/non-trivial fallback definitions. More Information links 0023, 0024, 0027.
6. Notes on other tasks: TASK-11 (tighten git.md's review definition once review.md ships); TASK-24 (settings ask/deny entries must match the AGENTS.md ask-first list).
7. Verify: smoke express/next/rn (files, no Jinja leftovers, AGENTS.md <= 100 lines with TASK-7 included, router paths exist); leak grep in template/ for TASK-, task-, Phase N, ICS, 0023, 0024, 'decision 00', jimzord, 'owner answer', tag; the ask-first list appears once (AGENTS.md) and git.md only references it.
8. Review loop to PASS; merge, push, delete branch.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: acceptance criteria extended with the owner's branch model (owner decision, not a readiness gap); ready label kept.

2026-10-01: ACs pointed at the refinements decision after review round 2 (old wording lacked the merge gate and the created-files limit).

2026-10-02 readiness round 1 NOT READY: 5 Material (core branches missing from the ask list, override rule contradiction, undefined checks/review/non-trivial, untestable allowlist AC, duplicated ask list) and 6 Minor, all explicit fixes folded into plan v2 and ACs; proceeding without another round.

Review round 1 FINDINGS (1 Material, 6 Minor, 3 Notes), fixed: M1 Roles clause now lets personal instructions add to the ask-first list but never remove from it (0029 aligned); m1 the always-loaded bullet says a project may add, removing needs an owner record; m2 fallback review defines Blocking/Material and stops after a few rounds; m3 owner-away path for ask-first actions; m4 never discard uncommitted changes you did not make; m5 commit and push without asking, push main after a merge; m6 0029 .env wording; N1 merges into other core branches follow the project's rules or ask. N2 line budget counted as non-blank lines (heading + 3 bullets).

Review round 2 PASS (0 Blocking/Material). Minors applied: AC3 lists the sixth item (merging into other core branches), flagged in 0029 as the agent's call for the owner to confirm; review fallback says leave it unmerged after a few rounds. Plan step 4's router row was dropped (AC1); stale plan text only.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Generated projects get docs/protocols/git.md (branch levels, merge gate with fallback definitions of checks, review and non-trivial, push rules, cleanup that never discards others' work, how to ask and what to do when the owner is away, secrets, commits) and a three-bullet 'Git and safety' section in AGENTS.md holding the ask-first list, which personal instructions and projects may add to but not loosen. Rendered AGENTS.md 62/63/62 lines. Record 0029. Verified by smoke test on all three stacks and leak grep. Review: round 1 FINDINGS (1 Material, 6 Minor) fixed, round 2 PASS.
<!-- SECTION:FINAL_SUMMARY:END -->

---
id: DRAFT-2
title: 'Lab protocol: spikes before high-impact decisions'
status: Draft
assignee: []
created_date: '2026-10-02 02:41'
updated_date: '2026-10-02 16:12'
labels:
  - agents protocols
dependencies: []
references:
  - template/docs/protocols/charter.md
  - template/docs/protocols/review.md
  - template/docs/protocols/git.md
documentation:
  - backlog/docs/lab-protocol/doc-2 - Lab-protocol-proposed-text.md
  - backlog/docs/lab-protocol/doc-3 - Lab-protocol-examples-proposed-text.md
  - backlog/docs/lab-protocol/doc-4 - Lab-protocol-review-log.md
priority: medium
type: feature
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner request 2026-10-02: a procedure that lets agents verify high-value, high-impact decisions with isolated, time-boxed experiments (spikes, called labs) before building on an untested assumption.

## Why

Agents decide on assumptions about framework, library, runtime or device behaviour that nobody tested. When one is wrong, the rework lands after the code is built. The owner supplied a draft protocol (LAB_PROTOCOL.md and LAB_EXAMPLES.md). It was reviewed and rewritten to fit this repo; the revised text is ready and went through five rounds of the review loop (PASS in round 5).

## What exists already

- doc-2: the proposed protocol, target `template/docs/protocols/lab.md`.
- doc-3: the proposed examples (EX-001 to EX-020), target `template/docs/protocols/lab-examples.md`.
- doc-4: issues found in the originals and the review-loop log.

## How the protocol works (short)

A lab is a Backlog task of type `spike` plus a branch `lab/<LAB-ID>` and a worktree under `.claude/worktrees/`. Before the first experiment `LAB.md` states the question, a falsifier and a budget. The agent runs the smallest discriminating experiment within side-effect limits, concludes (CONFIRMED, REJECTED, PARTIALLY CONFIRMED, INCONCLUSIVE) with an impact, distills the result into a decision record or task note per `charter.md`, keeps the evidence (`docs/labs/<LAB-ID>.md` for decisions, plus a pushed tag), and removes the worktree. A lab branch is never merged.

## Author's choices for the owner to confirm (made while rewriting the originals)

- A lab is **required** before recommending or building on an untested assumption under a hard-to-reverse choice, a big architecture change, or a cross-stack contract; otherwise optional.
- Every lab has a budget (time or attempts) and ends INCONCLUSIVE when it is spent.
- Evidence survives as `docs/labs/<LAB-ID>.md` (only for decision records) and a pushed tag `lab-closed/<LAB-ID>`, so deleting the unmerged branch does not trip the ask-first rule.
- Conclusions that feed a decision get an independent check inside the record's review loop.
- Lab worktrees live inside the repo folder (an outside worktree is untrusted by Claude Code and stalls unattended runs).

## Suggested split when promoted

(a) protocol text, router row, glossary, `git.md` line; (b) decision record and permission rules; (c) proof run. Create them as subtasks (`-p`) of the promoted task.

## Related

TASK-7 (charter), TASK-11 (review loop), TASK-26 (Ready gate: could require a lab for hard-to-reverse choices), TASK-9 (findings pipeline), DRAFT-1.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 The protocol and examples ship in template/ as docs/protocols/lab.md and lab-examples.md (text from doc-2 and doc-3, updated for any owner decision), with one router row in template/AGENTS.md.jinja "When to read what" and no other growth of that file
- [ ] #2 The glossary defines lab and spike (one concept, two names) and the lab record
- [ ] #3 A decision record in docs/decisions/ captures the choices above (required-before rule, budget, evidence tag and docs/labs, worktree location, spike task type), with alternatives considered
- [ ] #4 dogfood.json and the repo copies are in sync if lab.md is also used in this repo (python scripts/dogfood_check.py passes)
- [ ] #5 Smoke test passes for express, next and rn, and each rendered project contains lab.md and lab-examples.md with working links
- [ ] #6 Proof run: an agent given a planted uncertain assumption follows the protocol end to end (spike task, lab worktree, LAB.md with falsifier and budget, evidence-backed conclusion, distilled decision record, worktree removed and tag pushed); transcript and resulting files attached as evidence
- [ ] #7 The change passes the review loop in docs/protocols/review.md
- [ ] #8 Whether writes under .claude/worktrees/ prompt in Claude Code is checked with a headless run and noted in agents.md (the git worktree and git tag allow rules already landed, decision 0038)
- [ ] #9 template/docs/protocols/git.md "Branches" says lab/<LAB-ID> branches sit outside the branch levels, are never merged and are not pushed, and points to lab.md (a branch name proves no ownership under decision 0039, so reserving lab/ for agents would need its own record)
- [ ] #10 lab.md (doc-2) is re-synced with decision 0039 before it ships: step 9 no longer treats a lab branch the agent created as ask-first, so the pushed lab-closed tag (criteria 3 and 6) is kept only if it still earns its place and its stated reason in the description is dropped; a lab closed in a later session leaves the worktree for the owner (0039 forbids removing another session worktree) and the spike task notes the lab branch so it stays the agent own
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

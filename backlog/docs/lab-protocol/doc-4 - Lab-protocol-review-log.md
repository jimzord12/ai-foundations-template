---
id: doc-4
title: Lab protocol review log
type: other
created_date: '2026-10-02 02:41'
updated_date: '2026-10-02 02:41'
---
# Lab protocol: review log (2026-10-02)

Source: the owner's `LAB_PROTOCOL.md` and `LAB_EXAMPLES.md` (a 500-line protocol and 16 examples). The proposed text is in doc-2 and doc-3.

## Issues found in the originals (author's review, before any reviewer)

- Wording said "production" for the main checkout; the repo has `main`, and generated projects may have a `production` branch.
- `lab/<ID>` branch and a sibling worktree sit outside the branch model, and a worktree beside the repo is untrusted by Claude Code (the project's allow list is ignored, so unattended runs stall).
- No budget or time box: a spike with no stop limit turns into the implementation.
- No limits on side effects: a worktree isolates files, not live APIs, credentials, shared databases or money.
- The lab record (`LAB.md`) lived only in a disposable branch and worktree, so the evidence behind a decision was lost on cleanup.
- Deleting the unmerged lab branch hits the ask-first rule (commits exist nowhere else).
- No link to Backlog (config already has task type `spike`), to `charter.md` owner gates, or to the review loop.
- The agent that ran the experiment also judged it: no independent check of the conclusion.
- Examples used CMS stacks (Sanity, Astro) the template does not ship; "ADR" instead of "decision record".
- `LAB.md` had 15 sections; no ABANDONED state; the four results and the impacts were not defined; the timestamp ID invited invented times.
- Windows: bash line-continuation in the worktree command fails in PowerShell.

## Independent review loop (context-reviewer, fresh each round)

| Round | Verdict | Material findings | Main themes |
|---|---|---|---|
| 1 | FINDINGS | 5 | `branch -D` ask rule, wrong pointer for the one-git-call rule, lab branch vs the feature-branch rule, contract change vs charter "proposed or accepted", too much ceremony in the conclusion check |
| 2 | FINDINGS | 1 | Invariant 7 weaker than the body ("not merged by default" vs "never merged") |
| 3 | FINDINGS | 1 | A spike inherits Definition of Done items it can never meet |
| 4 | FINDINGS | 1 | A follow-up investigation unblocked the waiting task while the question was still open |
| 5 | PASS | 0 | Three minors, fixed |

Attended cap is 8 rounds (`docs/protocols/review.md`); the loop stopped at 5 on PASS.

## Left for the implementation task

Router row, `git.md` line, glossary, decision record, permission rules for `git worktree` and `git tag`, smoke test, proof run: see the acceptance criteria of the draft task.

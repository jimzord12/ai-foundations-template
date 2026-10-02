---
id: doc-2
title: Lab protocol (proposed text)
type: specification
created_date: '2026-10-02 02:39'
updated_date: '2026-10-02 02:40'
---
# Lab: resolve costly uncertainty before building

A lab is a time-boxed, isolated experiment (also called a spike) that answers one question about how something really behaves. Its output is **knowledge**, not code. The main checkout implements decisions that are understood; a lab tests the ones that are not.

Flow: stop, isolate, define the question, experiment, collect evidence, conclude, distill, return to normal work.

Examples have stable IDs (`EX-001`, ...) in `docs/protocols/lab-examples.md`. They illustrate; where one conflicts with this file, this file wins.

## When to run a lab

**Required** before you recommend or build on an assumption that is untested and sits under:

- a choice on the hard-to-reverse list in AGENTS.md;
- a big architecture change (`docs/protocols/charter.md`);
- a contract or boundary that several parts of the code, several stacks or several deployed clients depend on.

**Worth considering** when:

- framework, library, runtime or device behaviour is unclear and documentation for the installed version cannot settle it;
- several plausible approaches have very different consequences;
- an existing abstraction may not support a required capability;
- workarounds are piling up around an unclear constraint (`EX-004`).

**Do not run a lab** for:

- a local, reversible question: fix it in the normal flow (`EX-002`);
- anything you can settle in a few minutes by reading decision records, the docs for the installed version, or the existing code: do that first;
- product or preference questions: the owner decides those (`docs/protocols/charter.md`);
- a question whose answer would not change what you do.

Test: if this assumption is wrong, would it cause meaningful rework or invalidate an important decision? If yes, run a lab. See `EX-001` to `EX-004`.

## Lifecycle

```text
PREPARED -> RUNNING -> CONCLUDED -> DISTILLED -> CLOSED
                \-> ABANDONED (any time before CONCLUDED)
```

`status` lives in the front matter of `LAB.md` and moves forward only. Never slide from experimenting into building the production change; each step below is a deliberate hand-over.

| LAB.md status | Backlog task status |
|---|---|
| PREPARED, RUNNING, CONCLUDED, DISTILLED | In Progress (from the moment you create the lab) |
| CLOSED, ABANDONED | Done (the final summary says which) |

## 1. Create the lab

1. **Backlog task.** Search first. Create a task of type `spike`, label `lab`, whose title is the question (the description gives the LAB-ID and the decision waiting on the answer). Make the task that needs the answer depend on it (`backlog task edit <id> --dep ...` replaces the whole list, so repeat the existing dependencies; `EX-020`). Task rules: `backlog instructions task-creation`.
2. **ID.** `LAB-<YYYYMMDD>-<slug>`, with the date taken from the system clock, not from memory. The slug names the uncertainty, never the preferred answer (`EX-005`).
3. **Branch and worktree**, from the commit where the question arose (normally `main`; if you are mid-feature, commit or note the work in progress and use that commit as the base):

```text
git worktree add -b lab/<LAB-ID> .claude/worktrees/<LAB-ID> <base-commit>
```

- Keep the worktree inside the repository folder, not beside it: Claude Code treats a folder outside the repo root as untrusted and ignores the project's permission allow list there, which stalls unattended runs.
- The folder must be git-ignored. If `.gitignore` does not cover it, add it to `$(git rev-parse --git-common-dir)/info/exclude` (in a linked worktree `.git` is a file, so do not write to `.git/info/exclude` directly).
- If your tool creates worktrees itself (for example `EnterWorktree`), name the worktree `<LAB-ID>` and rename its branch to `lab/<LAB-ID>` with `git branch -m`, so the paths in step 9 match.
- In PowerShell, run each git command as its own call (`docs/protocols/agents.md`, Permissions).

A lab branch is not a feature branch: it sits outside the branch levels in `docs/protocols/git.md`, is never merged, and is not pushed (step 9 preserves it as a tag). All experimental work happens in this worktree; the main checkout stays untouched.

## 2. Prepare

1. Bootstrap the worktree: install dependencies from the lockfile (for example `npm ci`) and create `.env` from `.env.example` with sandbox or local values only.
2. Run the project's checks once so you know the baseline, and record the base commit.
3. Create `LAB.md` at the worktree root and fill in everything down to **Plan** before you run anything. The question, the falsifier and the budget must exist before the first experiment: that is what keeps the result honest.
4. Set `status: RUNNING` and write `started` from the system clock.

```markdown
---
id: LAB-YYYYMMDD-slug
task: TASK-N
status: PREPARED
base_commit: <commit>
started: <timestamp from the system clock, when RUNNING begins>
budget: <time or number of attempts; for example "90 minutes" or "3 designs"; time is measured from `started`>
follows: <earlier LAB-ID, if any>
conclusion:    # filled at CONCLUDED
impact:        # filled at CONCLUDED
---

# Lab: <title>

## Question
The one uncertainty to resolve.

## Why it matters
The decision that depends on the answer, and the cost of being wrong.

## Assumption and hypothesis
What the current design assumes, and what you expect to be true.

## Evidence and falsifier
The observable evidence that would answer the question, and the result that would prove the assumption wrong. Write the falsifier before you experiment.

## Scope
What this lab establishes, and what is outside it.

## Budget and side effects
The stop limit (also in the front matter). Every external effect the experiment may have: services called, accounts or data touched, tools installed outside the worktree. See "Run".

## Plan
The smallest experiment that can tell the plausible answers apart.

## Log
Commands, tool and runtime versions, and the outputs that matter. Include failed approaches that taught something.

## Findings
- Observed: what happened, as facts.
- Interpretation: what you conclude from it.
- Constraints discovered: new limits, with the versions they hold for.

## Conclusion
One of the four results below, then the answer to the Question in plain words.

## Impact and recommendation
One impact (below), why, and what should happen next.

## Open questions
New or unresolved questions.

## Deviations and protocol feedback
Departures from this protocol and why, plus any improvement you propose. `None` when empty.
```

`EX-006` shows a prepared `LAB.md`.

## 3. Run the experiment

Produce enough evidence to answer the question, not a solution.

- Run the **smallest discriminating experiment**: the least code that tells the plausible answers apart (`EX-007`).
- Test the assumption; do not polish. Lab code may be ugly or temporary, and it is not generalized just because it works (`EX-008`).
- Change one important variable at a time, and keep a baseline to compare against.
- Log commands, versions and outputs as you go: a result nobody can reproduce is not evidence.
- Check the budget at each natural step. When it is spent, stop and conclude with what you have, even if that is `INCONCLUSIVE` (`EX-017`).

**Limits on side effects.** A worktree isolates files, not the outside world.

- No production data, production credentials or production services, unless the owner approves first (see the owner-away rule below). Use local services, sandboxes or test accounts.
- No writes to shared services or databases other than throwaway ones you create and remove.
- Anything that spends money, sends messages, uses production access, or changes someone else's system needs the owner's approval first. If the owner is away, do not do it: conclude with what you have (usually `INCONCLUSIVE`) and list the missing approval under **Waiting on the owner** in your end-of-task summary (`docs/protocols/charter.md`, "When the owner is away").
- Secrets never go into `LAB.md`, logs, commits or task notes.
- Record anything you installed outside the worktree (global tools, containers, background processes) and remove it at close.

See `EX-018`.

## 4. Control scope

One lab answers one architectural question, or one tightly coupled cluster of questions.

- A new question that is needed to answer the original stays in this lab.
- A new question that is valuable on its own goes under **Open questions** and, if it matters, becomes its own `spike` task (`EX-009`).
- If the original question stops being the real problem, stop and reframe instead of letting the lab grow.

## 5. Know when to stop

Stop when:

- the question is answered with enough confidence;
- the hypothesis has clearly failed;
- more experimenting is no longer raising confidence;
- the budget is spent;
- the scope has changed materially, or a different uncertainty deserves its own lab;
- the available evidence cannot settle the question;
- the result shows that an accepted contract must change.

For the last case record `CONTRACT CHANGE REQUIRED` as the impact and stop that line of work. A lab may show that a contract is wrong; it must not quietly redefine it, and it must not carry on as if the new contract were already accepted. A new contract is a decision with its own owner path (`docs/protocols/charter.md`), and exploring it is a new lab. See `EX-010`. When the evidence cannot settle the question, see `EX-011`.

If the lab is no longer needed before it concludes, set `ABANDONED` and write one line saying why. ABANDONED is terminal: skip steps 6 and 7, do the dependency and note part of step 8 (so the waiting task is not blocked by a dead lab, and says why), then clean up as in step 9 (the distill precondition does not apply).

## 6. Conclude

1. Stop modifying the experiment.
2. Complete `LAB.md`, set `conclusion`, `impact` and `status: CONCLUDED`, then commit `LAB.md` and the lab code on the lab branch.
3. **Check the conclusion** when the impact is `ADR CANDIDATE` or `CONTRACT CHANGE REQUIRED` (the other impacts do not carry a durable decision, so they skip this check). Do not run a separate review: put the check into the review loop of the change that records the decision (step 7). In each round of that loop, also run a reviewer with a shell, `code-reviewer` where available (alongside any reviewer `docs/protocols/review.md` names for the record) with this question: does the evidence in the Log support the Conclusion and the Impact, and were any versions, environments or variables left out? It needs a shell to re-run commands from the Log. Give the reviewer the lab worktree path (the only place the commands can run; build output written there is fine, it is disposable), and remove nothing until the loop ends. If the check finds a gap, re-run in the lab worktree or narrow the Conclusion (the status stays `CONCLUDED`), then update the `docs/labs/` copy. Whoever ran the experiment is the worst judge of it (`EX-019`).

**Results:**

| Result | Means |
|---|---|
| CONFIRMED | The hypothesis held for the conditions tested |
| REJECTED | The hypothesis failed |
| PARTIALLY CONFIRMED | It held for some conditions or cases; the Conclusion says which |
| INCONCLUSIVE | The evidence could not settle it (valid; do not manufacture confidence, `EX-011`) |

**Impact** (pick one; the destination is in step 7):

| Impact | Means |
|---|---|
| NONE | The current design stands |
| IMPLEMENTATION GUIDANCE | The design stands; there are constraints or hints for building it |
| ADR CANDIDATE | A decision should be recorded (a decision record) |
| CONTRACT CHANGE REQUIRED | An accepted contract or decision cannot hold |
| NEW INVESTIGATION REQUIRED | Another lab is needed first |

A good conclusion answers the question and states the constraints found (`EX-012`). The lab is done when the question is answered, not when the prototype looks good.

## 7. Distill

A concluded lab does not flow into production. Turn its findings into the durable artifact for its impact. Set `status: DISTILLED` when that artifact exists and, where a record change goes through a review loop, the loop has passed.

| Impact | Destination | Who decides |
|---|---|---|
| NONE | A line in the Backlog task's final summary | You |
| IMPLEMENTATION GUIDANCE | Notes on the task that needs the answer; a line in `docs/architecture.md` if it is a lasting constraint | You |
| ADR CANDIDATE | A decision record per `docs/decisions/README.md` | Per `docs/protocols/charter.md` |
| CONTRACT CHANGE REQUIRED | A decision record that supersedes the old one, if one exists | Per `docs/protocols/charter.md` |
| NEW INVESTIGATION REQUIRED | A new `spike` task; its `LAB.md` sets `follows:` to this lab | You |

"Per charter" means: a big architecture change or an item on the hard-to-reverse list is written `proposed` and waits for the owner; anything else (a structural change, a technical choice, a port at one boundary) you record as `accepted` and build.

- Production receives only what is needed to understand and implement the decision (`EX-013`).
- **Keep the evidence, only where a record cites it.** For `ADR CANDIDATE` and `CONTRACT CHANGE REQUIRED`, copy the final `LAB.md` (log trimmed to what supports the conclusion) to `docs/labs/<LAB-ID>.md` in the same change as the decision record, and link it from the record. Without it the record cites an experiment nobody can check. Lab records are a historical record, not maintained docs. For the other impacts, a short evidence summary in the task note is enough; the tag in step 9 keeps the full history.
- The change that adds the record (and `docs/labs/` file) goes on a feature branch from `main`, not on the lab branch (which is never merged). It is non-trivial and goes through the normal review loop with the step 6 evidence question added.
- Tell the owner in the end-of-task summary (`docs/protocols/done.md`), in about ten lines: the Question, the Conclusion, the Impact, your recommendation. Put it under **Decisions** (or **Findings** when no decision was taken), and any decision or approval you need from them under **Waiting on the owner**.

## 8. Return to normal work

```text
uncertainty -> lab -> evidence -> distilled decision -> implementation on a feature branch
```

- Put the result on the Backlog task that was waiting for it (a note, with a link to the lab record where one exists, otherwise to the spike task) and update its dependencies (`--dep` replaces the list: pass the remaining ones, or `""` for none). The question must not look answered when it is not: an `INCONCLUSIVE` result whose question still matters takes the impact `NEW INVESTIGATION REQUIRED`, never `NONE`; for `NEW INVESTIGATION REQUIRED`, put the new spike task in the list in place of this lab instead of removing it, and the same when the lab was `ABANDONED` but the question still matters.
- While a lab runs, do not build the part that depends on the answer; carry on with independent work and list the waiting item in the end-of-task summary (the same stance as "When the owner is away" in `docs/protocols/charter.md`).
- Implement from `main` on a normal feature branch, with the usual checks and review loop. Lab code is a reference. Promoting a lab commit is a deliberate decision, recorded on the task; existing code is not a reason to promote it (`EX-014`).
- Where a decision is `proposed`, it must be accepted before the implementation continues.

## 9. Close

Set `status: CLOSED` once the findings are distilled and, for `ADR CANDIDATE` and `CONTRACT CHANGE REQUIRED`, the decision record and lab record are on `main`. An `ABANDONED` lab keeps that status (it is already terminal) and goes straight to the steps below.

Do these in order; each is its own git call. Run steps 3 and 4 from the main checkout, not from inside the worktree being removed:

1. Commit everything left in the lab worktree (including the final status), so nothing is lost and `git worktree remove` does not refuse.
2. Tag the final commit and push the tag. The tag keeps the history, so the branch's commits then exist elsewhere and deleting the branch no longer falls under the ask-first rule in AGENTS.md ("an unmerged branch whose commits exist nowhere else").

```text
git tag lab-closed/<LAB-ID> lab/<LAB-ID>
git push origin lab-closed/<LAB-ID>
```

3. Remove the worktree: `git worktree remove .claude/worktrees/<LAB-ID>`. Stop and remove anything the lab installed outside it.
4. Delete the local branch (`git branch -D lab/<LAB-ID>`). The lab branch is never pushed (only the tag is); if one was pushed by mistake, delete the remote branch too. Your tool may still ask before `-D`, which is intended: if it is refused or nobody answers, leave the branch and list it in the end-of-task summary.
5. Mark the Backlog task done, with the conclusion (or, for `ABANDONED`, the reason) as its final summary. Backlog copies the project's Definition of Done onto every task; the items that need a merged change (checks, review, merge) do not apply to a spike, and this overrides the finalization guide for spikes. Leave them unchecked and say so in the final summary rather than ticking them.

## Adapting the protocol

This is the default workflow. If following a step would stop you from investigating the real problem, adapt it: keep the intent, use the simplest alternative that fits, and write what you changed and why under **Deviations and protocol feedback** (`EX-015`). Friction is a reason to improve the protocol, not a convenience.

You may not adapt the rules marked as invariants below.

## Improving the protocol

When a lab shows repeated friction, needless ceremony or a missing concept, write a proposal under **Deviations and protocol feedback**: the observed problem, the suggested change, the expected benefit and the possible downside. Also list it in your end-of-task summary under **Findings** (`docs/protocols/done.md`; friction you did not act on, `docs/protocols/evolution.md`). A lab proposes; changing this protocol is a separate decision (`EX-016`).

## Invariants

1. The main checkout implements understood decisions; uncertainty goes to a lab.
2. Every lab begins with a question, a falsifier and a budget, written down before the first experiment.
3. Experiments seek evidence, not polished code. Lab code is disposable by default.
4. A lab never silently changes an accepted contract or decision.
5. A lab never touches production data, production credentials or other people's systems without the owner's approval.
6. Findings are distilled, and the evidence kept, before they affect production.
7. Experimenting and building stay separate phases; a lab branch is never merged (a lab commit may be promoted only by a recorded decision, step 8).
8. The owner's gates in AGENTS.md and `docs/protocols/charter.md` apply to a lab's outcome exactly as they apply to any other decision.

Everything else may be adapted when it must be, and the deviation is written down.

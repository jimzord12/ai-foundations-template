# Ready gate

Work runs unattended only after it has been planned and challenged, so gaps surface before the run instead of halfway through it with nobody to ask. This file says what "ready" means, what the plan holds, how the challenge runs, and how a whole phase gets ready. Where this file exists, it is the project's rule for starting work.

## When it applies

- Unattended work starts only on tasks labelled `ready`, or waived by the owner.
- At pickup, check that every dependency is Done and that the task notes record one of: a task-level READY, a note "passed the phase check, round N" (without "plan at pickup"), the trivial self-check, or the owner's waiver. If none is there, write the plan and challenge it first; a label alone is not enough.
- In an attended run, the owner may waive the gate for a task: note "ready gate waived by the owner" in the task notes; it then counts as ready.
- Depth scales with the task:

| Task | Plan | Challenge |
|---|---|---|
| Trivial (not non-trivial as `docs/protocols/review.md` defines it) | The checklist answered in a few lines | None: answer the checklist in the task notes and add the label yourself |
| Non-trivial, one area of the code | Short: seams, files, checks | Rounds until READY |
| Several areas, a new interface, data changes, or an owner decision involved | Full | Rounds until READY |

## Ready checklist

A task is ready when:

1. **Why:** the description says what problem it solves and for whom.
2. **Acceptance criteria** are testable: each names a result an agent can observe.
3. **Dependencies:** every task the plan needs first is declared as a dependency, and each is Done (the Backlog status), or ordered before it in the same phase and Done by the time it is picked up.
4. **Size:** one change that merges through one review loop. Bigger: split it.
5. **Decisions:** every open question is answered, and the owner's questions (as AGENTS.md and, where present, `docs/protocols/charter.md` define them) by the owner.
6. **Verification:** the checks and the evidence for each criterion are named.
7. **Plan:** written into the task and challenged READY (below), or self-checked for a trivial task.

## The plan

Write it into the task (`backlog task edit <id> --plan`), traced against the code as it is now:

- **Seams:** the imports, call sites, wiring and entry points the change goes through, and the existing tests that cover them, each by file and symbol. Open them; do not infer them from names.
- **Files** to create or change, including indexes, router rows, synced copies and the docs that describe them.
- **Interfaces** (code tasks): for each new or changed function, endpoint, component or command, its signature, inputs, outputs and errors, precise enough to write the tests from them before the code.
- **Steps** in order, with the decisions each takes (owner decisions marked).
- **Checks** to run and the **evidence** that will prove each acceptance criterion (`docs/protocols/done.md` where present).

## The challenge

1. Spawn a fresh `readiness-challenger` (a subagent that has not seen the planning). Give it the task id (or the phase plan), the level (task or phase), whether the working tree is on the main branch, the round number, the settled decisions and owner answers, the lead lenses you choose (names: `.claude/skills/ready/SKILL.md`), and every earlier report with your disposition of each finding. If the profile is missing or your tool cannot run it, use `code-reviewer` and tell it to apply `.claude/skills/ready/SKILL.md` and answer READY or NOT READY; for a phase, split the brief by groups of tasks if it runs out of turns.
2. On NOT READY, fix the plan or the task and start the next round with a new challenger. When the only open findings are owner questions you cannot answer, stop the rounds and go to "Owner questions". INCOMPLETE, NOT_CHECKED items and the round caps work as in the review loop (`docs/protocols/review.md`).
3. On READY, add the label (`backlog task edit <id> --add-label ready`) and append the verdict and the number of rounds to the task notes.

## Owner questions

Ask the owner once, in one batch, not one question at a time. Each question holds: what is asked, the task and step it blocks, the options, and your recommended answer with the reason. Record the answers in the task (or in a decision record when they are decisions) before the next round. If the owner is away, the task stays unready, and so does every task that depends on it: do not adopt your recommended answer; move on to other ready tasks and list the questions in your end-of-task summary.

## The `ready` label

- Only a task that passed the gate carries it. A Backlog draft never does: promote it to a task first.
- Remove it when the task changes after the challenge (new criteria, a different plan, a dependency that changed what the plan relies on), then plan and challenge again.

## Phase level

A phase is a milestone, or any set of tasks run unattended together. Before the run:

1. Write the phase plan as a Backlog document (`backlog doc create`): goal, exit criteria, task order with dependencies, the tasks planned at pickup, which tasks touch the same files, and rules for the run (for example one runner, or which tasks may run in parallel).
2. Plan every task. One whose plan depends on code an earlier task in the phase will change is checked here on checklist items 1 to 6 only; its plan is written at pickup, traced against the code as it is then, and challenged at task level before work starts (on NOT READY, remove its label).
3. Run the challenge at level "phase": order and dependencies, shared files, decision-record numbers (two tasks must not claim the same number; a plan names a new record by title and takes the next free number when it writes it), and the owner questions of every task, batched up front.
4. Label the tasks that pass (no open Blocking or Material finding in the last round, and no dependency on a task that has one) and append to each labelled task's notes "passed the phase check, round N", adding "plan at pickup" for the tasks planned at pickup. The phase verdict itself goes in the phase plan. The phase challenge stands in for a separate challenge of each fully planned task; tasks planned at pickup still get their own. The run takes only labelled tasks, in the planned order, with the pickup check above.

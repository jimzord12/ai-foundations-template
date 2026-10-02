# Review loop

Every non-trivial change gets an independent review before it is merged. Where this file exists, it is the project's rule for reviews.

## What needs a review

A change is non-trivial when it alters behaviour, touches more than one file, or adds or changes a test. Changes to instruction files (AGENTS.md, protocols, agent profiles, skills) and to decision records are always non-trivial and always reviewed.

## The loop

1. Spawn a fresh reviewer (a subagent that has not seen your work). Give it the change, the round number, the settled decisions, the lead lenses you choose for this round (lens names: the reviewer's lens skill, for example `.claude/skills/review-lenses/SKILL.md`), and every earlier report with your disposition of each finding.
2. Fix every Blocking and Material finding and re-run the checks.
3. Start the next round with a new reviewer.
4. Stop when a round returns PASS. Minor findings and Notes alone do not continue the loop; fix the cheap ones.
5. On INCOMPLETE, supply what was missing (or run it yourself) and start the next round; it counts as a round.

## Caps

- **Attended:** at most 8 rounds. A run is attended only while the owner is replying in the session.
- **Unattended:** at most 15 rounds.
- Still Blocking or Material after the cap: leave the change unmerged and tell the owner in your end-of-task summary. Never call it done.

## Who reviews what

| Change | Reviewer profile |
|---|---|
| Code, tests, configuration | `code-reviewer` |
| Agent context: AGENTS.md, protocols, agent profiles, skills | `context-reviewer` |
| Project docs: README, architecture, glossary, decision records | `docs-reviewer` |

If a named profile is missing, use `code-reviewer`. A mixed change runs one reviewer per distinct profile in the same round (a fallback `code-reviewer` covers every kind it stands in for, in one brief); the round passes only when all of them pass.

Reports follow the shape in the review-core skill.

---
protocol: review
kind: process
status: active
summary: Independent fresh-context review of every non-trivial change before it merges.
applies-when: A non-trivial change is ready to merge, or feedback should change how agents behave.
ends-when: A round returns PASS, or the round cap is reached and the change stays unmerged.
produces: A findings report with a verdict per round.
agents: [code-reviewer, context-reviewer, docs-reviewer, scannability-reviewer, context-maintainer]
skills: [review-core, review-lenses, context-lenses, docs-lenses, scan-lenses]
related: [done]
---
# Review loop

Every non-trivial change gets an independent review before it is merged. Where this file exists, it is the project's rule for reviews.

## What needs a review

A change is non-trivial when it alters behaviour, touches more than one file, or adds or changes a test. Changes to instruction files (AGENTS.md, CLAUDE.md, protocols, agent profiles, skills) and to decision records are always non-trivial and always reviewed.

## The loop

1. Spawn a fresh reviewer (a subagent that has not seen your work). Give it the change, the round number, whether the working tree is on the change, the settled decisions, the lead lenses you choose for this round (lens names: the reviewer's lens skill, for example `.claude/skills/review-lenses/SKILL.md`), and every earlier report with your disposition of each finding. Commit the change first when a reviewer must run it in a scratch copy (`docs-reviewer` clones committed work only).
2. Fix every Blocking and Material finding and re-run the checks.
3. Start the next round with a new reviewer.
4. Stop when a round returns PASS. Minor findings and Notes alone do not continue the loop; fix the cheap ones. A PASS may list NOT_CHECKED items: run them yourself and report the result, or name the ones still open in your end-of-task summary.
5. On INCOMPLETE, supply what was missing (or run it yourself and put the commands and their full output in the next brief) and start the next round; it counts as a round.

## Caps

- **Attended:** at most 8 rounds. A run is attended only while the owner is replying in the session.
- **Unattended:** at most 15 rounds.
- Still Blocking, Material or INCOMPLETE after the cap: leave the change unmerged and tell the owner in your end-of-task summary. Never call it done.

## Who reviews what

| Change | Reviewer profile |
|---|---|
| Code, tests, configuration | `code-reviewer` |
| Instruction files: AGENTS.md, CLAUDE.md, protocols, agent profiles, skills | `context-reviewer` (no shell: give it the diff text and the feedback or task behind the change) |
| Project docs: README, guides and runbooks, architecture, glossary, decision records | `docs-reviewer` |

If a named profile is missing or your tool cannot run it, use `code-reviewer` (tell it to apply `.claude/skills/context-lenses/SKILL.md` for instruction files and `.claude/skills/docs-lenses/SKILL.md` for project docs). A mixed change runs one reviewer per distinct profile in the same round (a fallback `code-reviewer` covers every kind it stands in for, in one brief); the round passes only when all of them pass.

When feedback should change how agents behave (an owner's correction, a rule applied wrongly, an ambiguous convention), `context-maintainer` writes the change: give it the feedback in the owner's words and the example that triggered it, and send each round's open findings back to it. If the profile is missing or your tool cannot run it, make the edit yourself applying `.claude/skills/context-lenses/SKILL.md`. The change then goes through the loop with `context-reviewer`.

**Opt-in add-on for human-facing docs:** `scannability-reviewer` checks how fast a doc reads (a README, a guide, a checklist), never whether it is true. Add it to a round, next to the reviewers above (no shell: give it the diff text, the doc paths, the audience and any style the doc must follow), when the owner asks or when the change adds or rewrites steps a human follows (a quickstart, a runbook, a test checklist); it then counts like any other reviewer in that round. If the profile is missing or your tool cannot run it, skip it: no fallback.

Reports follow the shape in the review-core skill.

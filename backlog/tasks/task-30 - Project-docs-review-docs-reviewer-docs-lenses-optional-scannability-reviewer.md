---
id: TASK-30
title: >-
  Project-docs review: docs-reviewer, docs-lenses, optional
  scannability-reviewer
status: In Progress
assignee:
  - '@claude'
created_date: '2026-10-01 20:52'
updated_date: '2026-10-02 02:15'
labels:
  - review
  - docs
  - knowledge
  - ready
milestone: m-0
dependencies:
  - TASK-11
  - TASK-25
priority: high
type: feature
ordinal: 660
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
No project-docs reviewer exists in any of the owner's repos; doc correctness was improvised from code-reviewer lenses each time. The knowledge system (TASK-25) adds architecture.md, decision records and a glossary that must stay true to the code. Ideas to reuse: greek-essence doc-reviewer's truth lens (every claim traces to a file, recompute numbers), ICS feature-maps rules (code outranks docs, anchor on symbol names not line numbers, stale claims dropped), ICS plan-reviewer (unverifiable claims reported as unverified), ICS scannability-reviewer (one shape per entry, zero filler, salience spent not sprayed). Decision: 'Two documentation reviewer families with shared skills'.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 docs-lenses skill ships with: code outranks docs, symbol anchors, decision-record completeness and supersede chain, accepted architecture decisions reflected in architecture.md, folder map matches the real tree, glossary terms used in code and UI, README quickstart actually runs, numbers recomputed, unverified claims reported as unverified, cold-reader completeness; items for architecture.md and the glossary apply only when the file exists
- [ ] #2 docs-reviewer profile (Read, Grep, Glob, plus Bash only for read-only git in the project and for checks that run or write in a scratch copy outside the working tree, such as running the quickstart; no Edit, Write or Agent; Opus, high) preloads review-core and docs-lenses; the profile notes that a quickstart run may be denied by the permission allowlist and is then reported NOT_CHECKED
- [ ] #3 scannability-reviewer (Read, Grep, Glob; Sonnet, high effort) preloads review-core and scan-lenses; it ships like any profile, with no Copier question, and is opt-in: its description says to run it only when review.md or the owner asks, and review.md lists it as an add-on for human-facing docs
- [ ] #4 docs-lenses, scan-lenses, docs-reviewer and scannability-reviewer ship in template/ and in this repo (pairs in dogfood.json)
- [ ] #5 Proof: docs-reviewer catches a planted stale claim (a path in architecture.md that no longer exists) in a generated project, report saved in the task notes; shipped files carry no source-repo names (same grep as TASK-29)
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Plan

<!-- SECTION:PLAN:BEGIN -->
# TASK-30 implementation plan (v2, after the Ready challenge)

Repo: `C:\Users\jimzord12\Documents\GitHub\ai-foundations-template` (`R` below). Drafts: `draft30/` in the session scratchpad (`D` below).

## Start

1. `backlog instructions task-execution`; `backlog task edit 30 -s "In Progress"`; add the plan to the task (`--plan`).
2. `git switch -c feature/task-30-docs-reviewers` from an up-to-date `main`. Start only after TASK-29 has merged (both edit review.md); branch from that `main`.

## Files

3. Copy the drafts into the template (no `.jinja` suffix: copied verbatim, no template syntax inside):
   - `D/skills/docs-lenses/SKILL.md` -> `R/template/.claude/skills/docs-lenses/SKILL.md`
   - `D/skills/scan-lenses/SKILL.md` -> `R/template/.claude/skills/scan-lenses/SKILL.md`
   - `D/agents/docs-reviewer.md` -> `R/template/.claude/agents/docs-reviewer.md`
   - `D/agents/scannability-reviewer.md` -> `R/template/.claude/agents/scannability-reviewer.md`
4. Apply `D/review-md-change.md` to `R/template/docs/protocols/review.md` (one paragraph; the trigger choice is settled there).
5. Dogfood: `dogfood.json` needs no edit. Its existing folder pairs (`template/.claude/agents` -> `.claude/agents`, `template/.claude/skills` -> `.claude/skills`) and the `review.md` pair already cover every new file (AC #4). Run `python scripts/dogfood_check.py --sync`; writes under `.claude/` are protected, so if Claude Code refuses, ask the owner to run that command.
6. Fix this repo's `README.md` "Repo layout" table: add the missing `.claude/`, `scripts/` and `dogfood.json` rows (otherwise docs-reviewer would hold this task's own loop open on them as Pre-existing noise). Nothing else needs editing: `AGENTS.md.jinja` routes reviews to `review.md`, and `agents.md` already describes the layout. Confirm with `grep -rn "docs-reviewer\|scannability" R/template R/docs`.

## Record

7. New record in `R/docs/decisions/` number 0034, kind `technical`, decision-makers `agent`, `supersedes: []`, More Information: "Refines 0025; builds on 0032". Content:
   - docs-reviewer Bash: read-only git in the project, anything that runs only in a scratch clone; a denied run is not retried another way and is reported NOT_CHECKED; uncommitted changes make the quickstart NOT_CHECKED; quickstart steps needing secrets, global installs or shared services are NOT_CHECKED, not run. Refines 0025, which said Bash only in a scratch copy.
   - NOT_CHECKED alone does not block PASS; INCOMPLETE when the unchecked item is the change itself.
   - Architecture and glossary lenses apply only when the file exists (this repo has neither).
   - scannability-reviewer: opt-in through its description and one review.md paragraph (owner asks, or the change adds or rewrites steps a human follows), no Copier question, no `code-reviewer` fallback; style alone is never Blocking and a shape mismatch is Minor (calibrated down from the source).
   - Decision-record checks point to the project's decisions README instead of restating it.
   - Add the index row to `R/docs/decisions/README.md` in the same commit.

## Verify (focused checks)

8. `python scripts/dogfood_check.py` -> 0 problems.
9. Smoke test, all three stacks (template changed):
   `uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=express . .tmp/smoke` (then `next`, `rn`; clear `.tmp/smoke` between runs). Commit first: `--vcs-ref HEAD` renders the committed tree. Check that the four new files are in each render and byte-identical to the template sources (`diff -r`).
10. Source-name grep over everything shipped or changed (template files and their copies):
    `grep -rniE 'ICS|VCR|Night Shift|night-shift|cvgen|greek-essence|\.agents/|licence|tax number' template/.claude .claude template/docs/protocols/review.md docs/protocols/review.md` -> no output.
11. Frontmatter sanity: each new file starts with `---`, has `name` equal to its file or folder name, and the skills have `user-invocable: false` and no `disable-model-invocation`.

## Proof (AC #5): docs-reviewer catches a stale path in a generated project

12. Render outside any repo, into the scratchpad: `uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=docsproof -d stack=express R <scratch>/proof30/docsproof`.
13. Build a tiny history there (`git init -b main`):
    - Commit 1 (`main`): `src/orders/place-order.ts` exporting `placeOrder`; `docs/architecture.md` folder-map row `src/orders/` and a Key flows line naming `placeOrder` in `src/orders/place-order.ts`.
    - Commit 2 (branch `feature/rename`): `git mv src/orders src/checkout`; update the Key flows line to `src/checkout/place-order.ts`, but leave the folder-map row `src/orders/`. That row is the planted stale path. The branch touches architecture.md, so routing sends it to docs-reviewer.
    - Required, to exercise the NOT_CHECKED path: a `README.md` with a quickstart (`npm ci`, `npm start`) committed on `main`.
14. Run headless. Workspace trust: a folder Claude Code has not trusted ignores the project's allow entries, but the Agent tool needs no permission. Two options, try A first:
    - **A (true end to end), in the rendered folder:** `claude -p "<prompt>" --output-format stream-json --verbose --allowedTools "Bash(git diff *)" "Bash(git log *)" "Bash(git show *)"` (CLI flags are not project settings, so trust does not drop them). Check the init event lists the agent `docs-reviewer`; if it does not, an untrusted folder is not loading project agents either, so use B.
    - **B, from this repo** (trusted, allows everything): the same command with `--add-dir <scratch>/proof30/docsproof`. The profile and skills then load from this repo's `.claude/` copies; `dogfood_check` proving them byte-identical to the template sources makes that equivalent. Say which option ran in the evidence.
    - Prompt (no hint about the plant, no lens names): "Spawn the docs-reviewer subagent once. Its brief: before anything else and without reading any file or running any command, (a) list the name of every skill injected into your context at startup, (b) quote the Minor row of your docs severity table. Then run round 1 of the review loop on branch feature/rename against main in <path>. Settled decisions: none. No lead lenses given. Return its report verbatim." In option B, also require every git, Glob and Grep call to target the scratch path.
15. Pass criteria, read from the stream: exactly one Agent call with `subagent_type` `docs-reviewer`; no Edit or Write call anywhere; no Read, Grep or Glob before the probe answer; it names `review-core` and `docs-lenses` and quotes the Minor row correctly (docs-lenses only); the report ends with a "Pains and ideas" section (review-core only); it has a Material finding anchored at `docs/architecture.md:<line>` naming `src/orders/`; verdict FINDINGS; the README quickstart is either run in a scratch clone or listed as NOT_CHECKED, never run in the project.
16. Save the report and the pass-criteria lines with `backlog task edit 30 --append-notes`. Delete `<scratch>/proof30` afterwards.

## Review, finish

17. Review loop per `docs/protocols/review.md`. The change mixes agent context (profiles, skills, review.md) and project docs (the decision record and its index row):
    - instruction files -> `context-reviewer` (merged with TASK-29; pass it the diff text);
    - decision record -> `docs-reviewer` itself. A session started before the profile existed may not list it; run that round through `claude -p` from this repo.
    - Fix Blocking and Material, re-run steps 8-11, next round, until PASS (caps in review.md).
18. `backlog instructions task-finalization`; check the AC and DoD items with evidence; final summary; status Done.
19. Commit (Co-Authored-By trailer), merge into `main`, push, delete `feature/task-30-docs-reviewers` locally and on the remote. Delete `.tmp/smoke`.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-02 readiness round 1 owner-type questions decided by the agent (ordinary choices): scannability-reviewer is opt-in through its description, no Copier question; docs-reviewer is dogfooded in this repo.
<!-- SECTION:NOTES:END -->

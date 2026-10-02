---
id: TASK-29
title: >-
  Agent-context review pair: context-reviewer, context-maintainer,
  context-lenses
status: In Progress
assignee:
  - '@claude'
created_date: '2026-10-01 20:52'
updated_date: '2026-10-02 01:17'
labels:
  - review
  - agents
  - docs
  - ready
milestone: m-0
dependencies:
  - TASK-11
priority: high
type: feature
ordinal: 650
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Most of this template is agent context (AGENTS.md, protocols, agent profiles, skills), and changes to it were going unreviewed. The owner already runs mature context reviewer and maintainer pairs in the ICS workspace (.claude/agents/agent-context-reviewer.md, agent-context-maintainer.md) and in night-shift and cvgen (context-reviewer, context-maintainer). Extract their generic core, drop everything repo-specific (product names, paths, glossary locations, line-ending rules, the sensitive-data paragraph), and add the gaps found on 2026-10-01: literal-reader safety, frontmatter checks (trigger description, least-privilege tools, model fit), router reachability (a file no pointer names is as absent as one never written), line budgets, Claude/Codex parity, rotating lead lenses per round. Decision: 'Two documentation reviewer families with shared skills'.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 context-lenses skill ships with: principle written before reading the diff, placement and owning file, integrate not append, principle vs example (overfit and over-general), terminology against glossary and code, timeless files carry no dates, literal-reader safety (an agent following the text exactly must not cause harm or stall), frontmatter checks, router reachability, line budgets, Claude/Codex parity, anti-overcorrection guards, and a lead-lens rotation table
- [ ] #2 context-reviewer profile (Read, Grep, Glob only; no Agent; Opus, high; the caller passes the diff text because the profile has no shell) preloads review-core and context-lenses; context-maintainer profile (adds Edit and Write, instruction and documentation files only, never deletes or renames, never edits dated records; Opus, high) preloads context-lenses
- [ ] #3 Both ship in template/ and in this repo (pairs in dogfood.json); grep -riE '\bICS\b|\bVCR\b|Night Shift|night-shift|cvgen|greek-essence|\.agents/|licence|tax number' over the shipped files returns nothing
- [ ] #4 docs/protocols/review.md names context-maintainer as the writer for feedback-driven instruction changes and context-reviewer as the reviewer of instruction changes
- [ ] #5 Proof via headless claude -p (same method as TASK-11): context-reviewer reviews one real instruction change in this repo, names the skills injected at startup and answers one content probe from context-lenses (the round-4 row of the lead-lens table) with no Read, Grep or Glob before the answer and a brief that never contains the skill body; context-maintainer applies one small instruction edit in a throwaway clone with the same probe; both reports saved in the task notes
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
# TASK-29 implementation plan (v2, after the Ready challenge)

Context pair for agent-context changes: `context-lenses` skill, `context-reviewer` (read-only, no shell) and `context-maintainer` (writer) profiles, review.md routing. Decision 0025 sets the shape; 0032 set the pattern (thin profile + hidden preloaded skills, dogfooded).

## Steps

1. **Start.** `backlog instructions task-execution`; set TASK-29 In Progress, assign, add this plan. Branch `feature/context-review-pair` from `main`.

2. **Shipped files** (from `draft29/`, as-is unless review changes them):
   - `template/.claude/skills/context-lenses/SKILL.md` (55 lines, `user-invocable: false`, no `disable-model-invocation`)
   - `template/.claude/agents/context-reviewer.md` (Read, Grep, Glob; opus; high; maxTurns 40; skills review-core, context-lenses)
   - `template/.claude/agents/context-maintainer.md` (Read, Grep, Glob, Edit, Write; opus; high; maxTurns 60; skills context-lenses)
   - `template/docs/protocols/review.md`: the three edits in `review-md-change.md` (33 -> 35 lines).
   - `template/.claude/skills/review-core/SKILL.md`, one bullet under "Findings" (shared by every reviewer family, so TASK-30's lenses need not repeat it): "Problems the change neither caused nor touched go in a separate 'Pre-existing' list, Minor at most, unless the brief asks for an audit." Keeps a one-line change from failing a round over untouched text.
   - No template syntax and no links to template-only files in any of them (agents.md rule); they are plain copies, not `.jinja`.
   - If Claude Code refuses a write under a `.claude/` path, give the owner the exact file and stop that step (root AGENTS.md).

3. **Dogfood.** No manifest edit: `dogfood.json` already maps the folders `template/.claude/agents` -> `.claude/agents`, `template/.claude/skills` -> `.claude/skills` and the file `template/docs/protocols/review.md`. Run `python scripts/dogfood_check.py --sync`, then `python scripts/dogfood_check.py` (expect 0 problems). If the sync is refused under `.claude/`, the owner runs it (root AGENTS.md says so).

4. **Router lines.** Recommended: amend the existing template AGENTS.md router row in place (0 lines added), text in `review-md-change.md` "Optional". Reason: Codex sessions never see the maintainer's description, and no router row today leads from "owner feedback about agent behaviour" to review.md. Root AGENTS.md needs nothing: its "Rules" already sends every non-trivial change to review.md, which now names both profiles. Skip if the owner wants zero AGENTS.md churn; the Claude path still works through the profile description.

5. **Decision record 0033** (`kind: technical`, decision-makers: agent), "Context review pair: context-reviewer, context-maintainer and context-lenses", plus its row in `docs/decisions/README.md`. Records the choices 0025 left open:
   - reviewer has no Bash: least privilege beats running git itself; the caller passes the diff text (stated in the profile description and the review.md row); missing diff or feedback = INCOMPLETE;
   - maintainer has no Bash either (the ICS and Night Shift maintainers had it): no git, no line-ending byte checks; the lenses do not depend on a shell;
   - maintainer effort high (the ICS maintainer ran medium), per TASK-29 AC #2;
   - maintainer does not preload review-core (it does not judge severity or give verdicts); the severity mapping for instruction files lives in context-lenses so the reviewer gets it without growing review-core;
   - maintainer never writes decision records, only names them for the caller; loosening an owner rule needs the owner's words;
   - AGENTS.md budget "about 100 lines" taken from 0007;
   - lead-lens rotation: 5 fixed pairs + round 6 free choice, restart at round 7 (fits caps 8 / 15 from 0012);
   - review-core gains the "Pre-existing" findings rule (refines 0032);
   - Timeless lens allows "checked against X on <date>" for externally verified facts (consistent with 0031).
   Links: refines 0025, follows 0032.

6. **Verify** (evidence into the task notes):
   - `python scripts/dogfood_check.py` -> 0 problems.
   - Smoke test, all three stacks (`uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=<s> . .tmp/smoke`): the three new files exist in `.tmp/smoke/.claude/`, `diff -r template/.claude .tmp/smoke/.claude` is empty, no `{{`/`{%` in them, rendered AGENTS.md line count unchanged (step 4 edits a row in place), every path the new files name exists in the render (`AGENTS.md`, `CLAUDE.md`, `docs/protocols/agents.md`, `.claude/settings.json`).
   - AC #3 grep over the shipped files and their copies:
     `grep -riE 'ICS|VCR|Night Shift|night-shift|cvgen|greek-essence|\.agents/|licence|tax number' template/.claude/agents/context-*.md template/.claude/skills/context-lenses template/docs/protocols/review.md .claude/agents/context-*.md .claude/skills/context-lenses docs/protocols/review.md` -> no output. (Drafts already pass.)
   - Frontmatter sanity: reviewer `tools` has no Edit, Write, Bash or Agent; maintainer has no Bash or Agent; both skill names resolve to folders.

7. **Proof (AC #5), headless `claude -p`, same method as TASK-11** (`--output-format stream-json --verbose --debug`, transcript saved to the scratchpad):
   - **Reviewer run, in this repo on the feature branch after commit + sync.** Prompt the main session to run `git diff main...HEAD -- template/docs/protocols/review.md docs/protocols/review.md` (only the review.md change, so the brief never contains the skill body), spawn `context-reviewer` exactly once with that diff text, the AC #4 wording as the feedback, round 1, settled decisions 0025/0032, lead lenses Principle and Placement. The brief also asks the subagent to open its report with (a) the names of the skills injected into its context at startup and (b) the lead lenses its skills give round 4, both without reading any file. Pass: init lists both agents; one Agent call (`subagent_type: context-reviewer`) whose input does not contain the expected round-4 answer, no Skill call; the subagent makes no Read, Grep or Glob call before its probe answer; it names `review-core` and `context-lenses` and gives the round-4 row of the lead-lens table correctly; no skipped-skill warning in the debug log. Its review counts as review round 1 for the instruction files.
   - **Maintainer run, in a throwaway clone.** `git clone --branch feature/context-review-pair . .tmp/proof-maint`, then in the clone restore `template/docs/protocols/review.md` and `docs/protocols/review.md` from `main` (so the AC #4 edit is undone there). Run `claude -p --permission-mode acceptEdits` in the clone (confirm subagent edits are covered by acceptEdits): spawn `context-maintainer` once with AC #4 as owner feedback, plus the same (a)/(b) probe. Pass: same startup checks; `git -C .tmp/proof-maint diff --stat` touches only instruction files; its report has the principle, the files table and open points. Save the diff and report, compare with the hand-made review.md change (differences are input for review, not a failure), then delete the clone. Check first that `.tmp/proof-maint` (inside the trusted repo) runs without the trust prompt; otherwise open Claude Code there once.
   - Save both reports (or excerpts plus scratchpad paths) in the TASK-29 notes. The notes say "the round-4 row", never the answer itself, so no committed file outside the skill holds it.

8. **Review loop** (`docs/protocols/review.md`). The change is mixed: instruction files -> `context-reviewer` (now available, round 1 = the proof run above); decision record 0033 and the README index -> `docs-reviewer` is missing, so `code-reviewer` covers them, same round. Rotate the lead lenses per the new table. Fix Blocking and Material, resync, re-run step 6 gates, next round with fresh reviewers until PASS (cap 8 attended / 15 unattended).

9. **Finish.** `backlog instructions task-finalization`; check ACs with evidence, final summary, Done. Commit, merge into `main`, push, delete the branch locally and on the remote, delete `.tmp/smoke*` and `.tmp/proof-maint` and scratch output.

## AC wording changed before starting (accepted by the challenger)

- AC #5: "quotes a marker line" -> "names the skills injected at startup and answers one content probe from context-lenses (the round-4 row of the lead-lens table) with no Read, Grep or Glob before the answer; the brief never contains the skill body".
- AC #5, maintainer: "applies one small instruction edit in a throwaway clone".
- AC #3 grep: `ICS|VCR` instead of bare `ICS|VCR`.
- AC #2: "instruction and documentation files only".

## Decided on the owner's behalf (report with the compass marker)

- The AGENTS.md router row is amended in place (0 lines added).
- review.md's instruction-file list gains CLAUDE.md.
- Neither profile gets Bash; the maintainer does not preload review-core.
- The "Pre-existing" findings rule goes into review-core (shared by every reviewer).
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-02 idea from TASK-14 review: context-lenses should include a literal-reader check that every 'only for' list in an always-loaded file states its tighten/loosen direction wherever an override clause touches it.
<!-- SECTION:NOTES:END -->

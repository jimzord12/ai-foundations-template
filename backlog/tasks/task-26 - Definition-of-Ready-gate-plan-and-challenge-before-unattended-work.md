---
id: TASK-26
title: 'Definition of Ready gate: plan and challenge before unattended work'
status: Done
assignee:
  - '@claude'
created_date: '2026-10-01 19:50'
updated_date: '2026-10-02 03:06'
labels:
  - process
milestone: m-0
dependencies:
  - TASK-11
priority: high
type: feature
ordinal: 700
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner-approved 2026-10-01. Gate before unattended work: ready checklist, plan written into the task with real seams traced, independent challenge (READY / NOT READY), batched owner questions with recommended answers; per task and per phase; ready tasks carry the ready label (drafts tested and rejected). Built as a ready skill plus a readiness-challenger profile (read-only tools, Opus, preloads review-core and ready), per the agents+skills decision.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [x] #1 ready skill and readiness-challenger profile ship in template/ and in this repo (dogfood manifest); docs/protocols/ready.md linked from the router in both the root and the template AGENTS.md
- [x] #2 Rule in both AGENTS.md files: unattended work starts only on tasks labelled ready; owner may waive when attended; depth scales with size
- [x] #3 Proof: the shipped challenger is run on one real task in this repo and its verdict recorded
- [x] #4 docs/protocols/ready.md contains: the ready checklist, what the plan written into the task must hold, the READY / NOT READY verdict, batched owner questions with recommended answers, and both the task level and the phase level
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
# TASK-26 implementation plan

Ready gate: `docs/protocols/ready.md`, `ready` skill, `readiness-challenger` profile, AGENTS.md rule and router rows. Decisions 0019 (gate), 0020 (thin profiles plus skills), 0032 (review-core rename clause) set the shape. `R` = repo root, `D` = this `draft26/` folder.

## Start

1. `backlog instructions task-execution`; `backlog task edit 26 -s "In Progress"`; add this plan (`--plan`). `git switch -c feature/task-26-ready-gate` from an up-to-date `main`.

## Files

2. Copy drafts (no `.jinja`: verbatim, no template syntax inside):
   - `D/template/docs/protocols/ready.md` -> `R/template/docs/protocols/ready.md`
   - `D/template/.claude/skills/ready/SKILL.md` -> `R/template/.claude/skills/ready/SKILL.md`
   - `D/template/.claude/agents/readiness-challenger.md` -> `R/template/.claude/agents/readiness-challenger.md`
3. Apply `D/agents-md-changes.md`: template `AGENTS.md.jinja` (+3 lines), root `AGENTS.md` (+1 line, one bullet amended), `README.md` repo-layout row, `dogfood.json` new pair for `ready.md`.
4. Dogfood: `python scripts/dogfood_check.py --sync`, then `python scripts/dogfood_check.py` -> `0 problem(s)`. If the write under `.claude/` is refused, the owner runs `--sync` (root AGENTS.md says so).
5. Record: `D/docs/decisions/0035-...md` -> `R/docs/decisions/` (kind `technical`, decision-makers `agent`; kinds in this repo are product, architecture, technical, no "process"), plus its index row in `R/docs/decisions/README.md`: `| [0035](0035-ready-gate-protocol-readiness-challenger-and-ready-skill.md) | technical | accepted | Ready gate protocol, readiness-challenger and ready skill |`. Take the next free number at write time if 0035 is gone.

## Focused checks

6. Smoke test, three stacks: `uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=<s> . .tmp/smoke-<s>` for express, next, rn (commit first: `--vcs-ref HEAD` renders committed work). Each: exit 0; `diff -r --strip-trailing-cr template/.claude <render>/.claude` empty; `docs/protocols/ready.md` present; rendered `AGENTS.md` line count about 71 (was 68/69/68) and contains the ready rule and router row.
7. Source-name grep, case-insensitive, over the new and changed shipped files and their copies: `grep -rniE '\bICS\b|\bVCR\b|Night Shift|night-shift|cvgen|greek-essence|\.agents/|licence|tax number' template/docs/protocols/ready.md template/.claude/agents/readiness-challenger.md template/.claude/skills/ready docs/protocols/ready.md .claude/agents/readiness-challenger.md .claude/skills/ready` -> no output.
8. Frontmatter sanity: profile tools have no Edit, Write or Agent; `skills: [review-core, ready]` both resolve to folders; skill has `user-invocable: false` and no `disable-model-invocation`; no `{{` or `{%` in the three new files.

## Proof (AC #3), headless `claude -p`, same method as TASK-29

9. In this repo on the feature branch, after commit and sync (`--output-format stream-json --verbose --debug`, transcript to the session scratchpad). The prompt tells the main session to spawn `readiness-challenger` exactly once at level task on the chosen real To Do task (TASK-28, after the orchestrator writes its plan per `ready.md`; decided), round 1, lead lenses Seams and Owner decisions, and to ask the subagent to open its report, before any tool call, with (a) the names of the skills injected into its context at startup and (b) the names of the phase lenses in its ready skill, in order, and (c) the title of the closing section its report rules require. The brief must not contain (b)'s or (c)'s answers (grep the prompt for each phase-lens name and for "Pains") and must not paste the skill.
10. Pass: init lists `readiness-challenger`; one Agent call with that `subagent_type`, no Skill call; the brief does not contain the phase-lens names; the subagent's first message comes before any tool call, names `review-core` and `ready`, lists the five phase lenses correctly and names "Pains and ideas"; it ran no Edit, Write or writing `backlog` command; its report ends in READY, NOT READY or INCOMPLETE with an owner-question section when it has any; no skipped-skill warning in the debug log.
11. AC #3 is met by recording the verdict, whatever it is; TASK-28 is not looped to READY inside TASK-26 (that happens when TASK-28 starts). Save the verdict (and report excerpt, transcript path) in the challenged task's notes with `backlog task edit <id> --append-notes`; on READY keep or add the `ready` label, on NOT READY remove it. Record "the phase-lens list", never the list itself, in TASK-26's notes.

## Review loop (`docs/protocols/review.md`)

12. Mixed change, one reviewer per profile per round: `context-reviewer` (diff text of ready.md, the skill, the profile, both AGENTS.md files, dogfood.json; the TASK-26 description and ACs as the task behind it; it has no shell) and `docs-reviewer` (record 0035, decisions README row, README.md row). Lead lenses: context-lenses rotation table; docs-reviewer round 1 leads with decision records and one home per fact. Fix Blocking and Material, re-sync, re-run steps 6 to 8, next round with fresh reviewers until PASS (caps 8 attended, 15 unattended).

## Finish

13. `backlog instructions task-finalization`; check ACs and DoD with evidence; final summary; status Done. Merge into `main`, push, delete the branch locally and on the remote; delete `.tmp/smoke-*` and scratch output.

## Evidence per acceptance criterion

- AC #1: `ls` of the three shipped files and their copies, dogfood check `0 problem(s)`, router row lines in both AGENTS.md files.
- AC #2: the rule line in both AGENTS.md files and in each render.
- AC #3: the saved verdict in the task notes plus the transcript checks of step 10.
- AC #4: headings of `ready.md` (checklist, plan, challenge, owner questions, label, phase level).
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
## Proof (AC #3), 2026-10-02

Headless `claude -p` from this repo (default permission mode, stream-json; transcripts in the session scratchpad, proof-evidence/task26-*). The main session made exactly one Agent call (subagent_type readiness-challenger) and no Skill call. The brief named no phase lens and did not contain "Pains" (grep-checked).

The subagent's own transcript shows review-core and ready injected at startup. Its first message, before any tool call:
- named both skills;
- listed the phase-lens row of the ready skill correctly, in order;
- named review-core's closing report section correctly.

It ran no Edit or Write and no writing Backlog command. It did run read-only probes, including `codex debug prompt-input` in a scratch git repo outside the project, which it deleted.

Verdict on TASK-28's plan: NOT READY (2 Material, 4 Minor). The full dispositions are in TASK-28's notes. Material 1: TASK-26 was an undeclared dependency. Material 2: the plan relied on scratch files that are not in the repo.

One false claim: "decisions README missing rows 0023-0030" was wrong. All rows are present.

Lesson adopted into ready.md: every task the plan needs first is a declared dependency.

## Proof record, completed

- Init event listed `readiness-challenger` among the agents.
- The run used no `--debug`, so the "no skipped-skill warning in the debug log" check was not done. The subagent's own transcript shows both skills (review-core, ready) injected at startup, which covers the same risk.
- The subagent listed the phase lenses of the ready skill in their written order. (Earlier note: "row" means this list.)

## Labels from before the gate

Eleven To Do tasks still carry `ready` from the Phase 1 readiness pass, before this gate existed: TASK-2, 2.1-2.5, 13, 16, 17, 23 and 27. None of them records a verdict, a phase pass or a waiver, so under ready.md's pickup check the label alone does not start them. Each is planned and challenged at pickup, and its label is kept or removed on the verdict. Decided by the agent in the unattended run: keep the labels and re-check at pickup; reported to the owner.

## Review loop

Mixed change: context-reviewer for the instruction files, docs-reviewer for record 0035, the README and the task notes.

| Round | context-reviewer | docs-reviewer |
|---|---|---|
| 1 | FINDINGS: 2 Material | FINDINGS: 1 Material |
| 2 | FINDINGS: 1 Material | PASS |
| 3 | FINDINGS: 2 Material | PASS |
| 4 | PASS | PASS |

- Round 1, context-reviewer: phase-passed tasks rejected at pickup; the owner's waiver had no effect.
- Round 1, docs-reviewer: 0035 copied the old pickup rule.
- Round 2, context-reviewer: tasks planned at pickup were unmarked.
- Round 3, context-reviewer: per-task labelling vs the phase verdict; skill lenses vs checklist item 3 on in-phase dependencies.
- All fixed. Round 4 Minors applied: the pickup check quotes the note text; the profile names `npx backlog.md`; the notes above.
- Reviews were pinned to a commit after round 1, because in round 1 an edit landed mid-review.
<!-- SECTION:NOTES:END -->

## Final Summary

<!-- SECTION:FINAL_SUMMARY:BEGIN -->
Added the ready gate to the template and dogfooded it. docs/protocols/ready.md holds:
- when the gate applies, the owner's waiver and the depth table;
- the 7-item checklist (every prerequisite is a declared dependency);
- what the plan holds (seams, files, interfaces precise enough to write tests first, steps, checks, evidence);
- the challenge loop and batched owner questions (owner away: the task and its dependents stay unready);
- the `ready` label and the pickup check (a label alone never starts work);
- the phase level ("plan at pickup", "passed the phase check, round N").

Also added:
- the hidden `ready` skill (task and phase lenses, severities, the READY/NOT READY mapping);
- the readiness-challenger profile (read-only, Opus, preloads review-core and ready);
- the rule and router rows in both AGENTS.md files, and the dogfood pair for ready.md;
- done.md: unready tasks go in the end-of-task summary;
- decision 0035.

Proof: the shipped challenger, run headless on TASK-28's plan, answered the preload probe before any tool call and returned NOT READY with two real gaps. Review loop: 4 rounds, ending PASS on both reviewers.
<!-- SECTION:FINAL_SUMMARY:END -->

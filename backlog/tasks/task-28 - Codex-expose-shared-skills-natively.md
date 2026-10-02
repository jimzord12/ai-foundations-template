---
id: TASK-28
title: 'Codex: expose shared skills natively'
status: To Do
assignee: []
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 03:02'
labels:
  - codex
  - skills
milestone: m-0
dependencies:
  - TASK-11
  - TASK-24
  - TASK-26
priority: medium
type: feature
ordinal: 800
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner decision 2026-10-01: in v0.1.0 Codex gets only what it supports natively: AGENTS.md (already shared) and skills. Skills are the shared knowledge layer (agents+skills decision), so Codex should read the same skill files as Claude Code, with one source of truth. Verify Codex's current skill location and format before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Codex's current skill discovery location and format verified from its docs and recorded
- [ ] #2 Shared skills reach Codex from one source, template/.claude/skills/: its Codex copies, template/.agents/skills/ (rendered into every generated project) and this repo's .agents/skills/, are folder pairs in dogfood.json, and python scripts/dogfood_check.py passes (CI runs it later, TASK-13)
- [ ] #3 Verified in a live Codex session, in a freshly rendered project, that lists or uses one shared skill
- [ ] #4 Rule recorded in docs/protocols/agents.md (template, synced to this repo): .agents/skills/ is Codex's byte-identical copy of .claude/skills/, and a shared skill is changed in .claude/skills/ and copied in the same change; this repo's AGENTS.md says the folder pairs in dogfood.json cover every new shared skill and --sync creates its copies
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
# TASK-28 plan: Codex reads the shared skills

Branch: `feature/task-28-codex-skills` (level 1, from `main`). Findings and sources: `research.md`.

## Approach (option b1)

`template/.claude/skills/` stays the one source. Codex reads skills only from `.agents/skills/` and Claude Code only from `.claude/skills/`, and symlinks break on Windows, so Codex gets a **byte-identical copy** made and checked by the existing dogfood machinery:

- `template/.agents/skills/` = copy of `template/.claude/skills/` → Copier renders both into every generated project.
- `.agents/skills/` (this repo's root) = copy of `template/.claude/skills/` → Codex sessions on this repo get them too.

Both are **folder pairs**, so a new skill (or a `scripts/` file inside one) is covered without touching the manifest again. `dogfood_check.py` needs no code change: it already handles any source/copy path pair.

## Before starting

- TASK-26 is in flight on `main` (commit `7b1d08e` plus uncommitted edits to `AGENTS.md`, `template/AGENTS.md.jinja`, `ready.md`, `done.md` at the time of research). Start this branch after TASK-26 is merged, so the `ready` skill is in the copies and the `AGENTS.md` line 9 edit does not conflict.
- Read `backlog instructions task-execution`; set TASK-28 In Progress; write the plan below into the task; apply the AC rewording in `ac-rewording.md` (owner-approved or as decided).

## Steps

1. `dogfood.json`: add two pairs and widen the description.
   ```json
   { "source": "template/.claude/skills", "copy": "template/.agents/skills" },
   { "source": "template/.claude/skills", "copy": ".agents/skills" }
   ```
   Description: say the manifest lists copies of template files, in this repo or inside `template/` (Codex's `template/.agents/skills`).
2. `python scripts/dogfood_check.py --sync` → creates both `.agents/skills/` trees. `.agents/` is not a protected path, so the agent can run it.
3. `template/docs/protocols/agents.md`, Layout: one bullet, e.g.
   "`.agents/skills/<name>/`: Codex's copy of `.claude/skills/`, byte for byte (Codex reads skills only there; Claude Code only from `.claude/skills/`; checked against the Codex docs and source on <date>). Change a shared skill in `.claude/skills/` and copy the folder to `.agents/skills/` in the same change; never edit the copy alone. Codex ignores Claude-only frontmatter such as `user-invocable`, so it lists the reviewer skills as ordinary skills; that is expected."
   Then `--sync` (copies to `docs/protocols/agents.md`).
4. `template/.claude/skills/context-lenses/SKILL.md`, Parity lens: add one clause, "Codex reads shared skills from `.agents/skills/`, a copy of `.claude/skills/`; a skill changed in one folder only is a Parity finding." Then `--sync` (updates `.claude/skills` and both Codex copies). If Claude Code refuses the write under `template/.claude/`, the owner makes it or runs `--sync`.
5. This repo's `AGENTS.md` "Where things go" line 9: list `.agents/skills/` and `template/.agents/skills/` as copies; add "a new shared skill goes in `template/.claude/skills/`; `--sync` creates its Codex copies (the folder pairs cover every skill)".
6. `README.md` layout table: add an `.agents/` row ("Codex's copies of the template's skills"), and make the `dogfood.json` row say it also lists Codex's copy inside `template/`.
7. Decision record, number taken when written: **"Codex reads the shared skills from a checked copy in `.agents/skills`"**, kind `technical`, decision-makers `agent`. Context: owner answer 4 in 0021 (Codex gets AGENTS.md and skills natively). Options a, b1, b2, c, d with one line each (from research.md table). Outcome b1. Consequences: good — one source, no new code, new skills covered automatically, proven live; bad — two physical copies in every generated project with no drift check there (instruction plus Parity lens only); Codex lists the reviewer skills (~1,300 chars of its catalog). More information: refines 0031 (the manifest now also holds a copy inside `template/`); the live proof commands and output. Add the row to `docs/decisions/README.md`.
8. Commit (render with `--vcs-ref HEAD` sees committed work only).

## Checks

```powershell
python scripts/dogfood_check.py            # expect "0 problem(s)"
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=express . .tmp/smoke-express
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=next    . .tmp/smoke-next
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=rn      . .tmp/smoke-rn
```
In each render, prove the two skill folders are identical:
```powershell
python -c "import filecmp,os,sys;r=sys.argv[1];a,b=r+'/.claude/skills',r+'/.agents/skills';L=lambda p:sorted(os.path.relpath(os.path.join(d,f),p) for d,_,fs in os.walk(p) for f in fs);fa=L(a);ok=fa==L(b) and all(filecmp.cmp(os.path.join(a,f),os.path.join(b,f),shallow=False) for f in fa);print(len(fa),'files',('identical' if ok else 'DIFFER'));sys.exit(0 if ok else 1)" .tmp/smoke-express
```
(repeat for `smoke-next`, `smoke-rn`). Delete the `.tmp/smoke-*` folders afterwards.

## Live Codex proof (AC #3)

Render **outside** the repo and `git init` it: inside `.tmp/` Codex would walk up to this repo's `.git` and also list this repo's root `.agents/skills`, which muddies the proof.
```powershell
$p = "<scratchpad>/codex-proof"
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=express C:\Users\jimzord12\Documents\GitHub\ai-foundations-template $p
git -C $p init -q
codex exec --sandbox read-only --ephemeral -C $p -o "$p-list.txt" "Answer only from the skills list in your instructions, without running any command or reading any file: which listed skills have their SKILL.md in this project's .agents/skills folder? Give each name with the path shown in the list."
codex exec --sandbox read-only --ephemeral -C $p -o "$p-use.txt" "Use `$review-core: open its SKILL.md and quote its first Markdown heading line exactly. Do not modify any file."
```
Expected: the list names every shared skill (six once TASK-26's `ready` is in) with a `rN/<name>/SKILL.md` path and no `exec` lines in the log; the second answers `# Review core`. Cross-check without a model call: `codex debug prompt-input "x"` run in `$p` shows the `.agents/skills` root and the skills. Optional for this repo: `codex debug prompt-input "x"` at the repo root lists the root `.agents/skills`. Record commands and output in the task's final summary and the decision record.

## Review loop (`docs/protocols/review.md`)

Mixed change, so each round runs three reviewers:
- `context-reviewer`: `template/docs/protocols/agents.md`, `context-lenses`, `AGENTS.md` (pass the diff text and the task; it has no shell).
- `docs-reviewer`: the decision record, decisions README row, `README.md`.
- `code-reviewer`: `dogfood.json` and the copy mechanism (the smoke and dogfood checks).

Tell every reviewer the `.agents/skills/` trees and `.claude/skills` copy are produced by `--sync` and verified by `dogfood_check.py`; review the sources only. Settled decisions for the brief: option b1; no `agents/openai.yaml`; no drift check shipped to generated projects; symlinks and Jinja includes rejected. Fix Blocking and Material, re-run the checks, next round; stop on PASS (caps in `review.md`).

## Finish

`backlog instructions task-finalization`; tick the ACs and DoD with evidence; final summary. Merge into `main`, push, delete the branch locally and on the remote (each git command its own call in PowerShell). Remove `.tmp/smoke-*` and the scratch proof folder.

## Files touched

`dogfood.json`, `template/.agents/skills/**` (new, synced), `.agents/skills/**` (new, synced), `template/docs/protocols/agents.md` (+ synced copy), `template/.claude/skills/context-lenses/SKILL.md` (+ synced copies), `AGENTS.md`, `README.md`, `docs/decisions/<nnnn>-codex-reads-the-shared-skills-from-a-checked-copy-in-agents-skills.md`, `docs/decisions/README.md`.
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
## Readiness challenge, task level, round 1 (2026-10-02): NOT READY

Run by the shipped readiness-challenger (TASK-26 proof, headless claude -p from the template repo; transcript in the session scratchpad, proof-evidence/task26-*).

- Material 1: TASK-26 is a real dependency but not declared. Disposed: dependency added; start after TASK-26 merges.
- Material 2: the plan relies on research.md and ac-rewording.md, which are not in the repo. To fix at pickup: paste the options table (a, b1, b2, c, d, one line each) and the Codex doc and source links into the plan; drop the ac-rewording step (already applied in 1e63576).
- Minor 1: the ready label stayed after the plan and criteria changed. Disposed: label removed; re-added on READY.
- Minor 2: step 7 writes proof output into the decision record before the proof exists. To fix: write the record after the proof.
- Minor 3: "no exec lines in the log" cannot be checked with -o only. To fix: add --json > <file>.jsonl and check it has no command-execution events.
- Minor 4: writes under template/.claude/ may need the owner. Note: in this repo Claude Code wrote template/.claude/ files without refusal during TASK-29/30/26; keep the fallback line.
- Note: no drift check in generated projects (agent's call, reported in the end-of-task summary).
- Pre-existing claim "decisions README has no rows for 0023-0030" was checked by the orchestrator and is false (all rows present).
<!-- SECTION:NOTES:END -->

---
id: TASK-28
title: 'Codex: expose shared skills natively'
status: In Progress
assignee:
  - '@claude'
created_date: '2026-10-01 20:13'
updated_date: '2026-10-02 03:22'
labels:
  - codex
  - skills
  - ready
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
# TASK-28 plan v2: Codex reads the shared skills

Branch: `feature/task-28-codex-skills` (level 1, from `main`). Findings and sources are below; v2 folds in the readiness challenge of 2026-10-02 (see notes).

## Approach (option b1)

`template/.claude/skills/` stays the one source. Codex reads skills only from `.agents/skills/` and Claude Code only from `.claude/skills/`, and symlinks break on Windows, so Codex gets a **byte-identical copy** made and checked by the existing dogfood machinery:

- `template/.agents/skills/` = copy of `template/.claude/skills/` → Copier renders both into every generated project.
- `.agents/skills/` (this repo's root) = copy of `template/.claude/skills/` → Codex sessions on this repo get them too.

Both are **folder pairs**, so a new skill (or a `scripts/` file inside one) is covered without touching the manifest again. `dogfood_check.py` needs no code change: it already handles any source/copy path pair.

## Codex skill discovery (AC #1, checked 2026-10-02)

| Question | Answer | Source |
|---|---|---|
| Project folder | `.agents/skills/<name>/SKILL.md` in **every directory from the cwd up to the project root** (root = nearest ancestor holding a `project_root_markers` entry, default `.git`; with no marker, the cwd only). Also `<repo>/.codex/skills` when the repo has a project config layer (`.codex/`). | docs [1]; `codex-rs/ext/skills/src/host_roots.rs` (`repo_agents_skill_roots`, `roots_from_layer_stack`) [3] |
| User folder | `$HOME/.agents/skills`; `$CODEX_HOME/skills` (`~/.codex/skills`) still read, marked deprecated in source. | [1], [3] |
| Admin / system | `/etc/codex/skills` (admin), bundled system skills (`~/.codex/skills/.system`), plugin skill roots. | [1], [3] |
| Configurable extra path? | **No.** `[skills]` in `config.toml` accepts only `bundled.enabled`, `include_instructions`, `max_context_tokens` and `[[skills.config]]` enable/disable rules (by `path` or `name`). Extra roots exist only through the app-server API (`set_extra_roots`) or an installed plugin. | `codex-rs/config/src/skills_config.rs` [4]; `host_service.rs` |
| SKILL.md format | YAML frontmatter between `---` lines. Read: `name` (≤64 chars; defaults to the folder name), `description` (required, one line after whitespace collapse), `metadata.short-description` (optional). Optional folders `scripts/`, `references/`, `assets/`, and `agents/openai.yaml` (UI, `policy.allow_implicit_invocation`, MCP dependencies). | docs [1][2]; `codex-rs/skills/src/parser.rs` [5] |
| Claude-only fields (`user-invocable: false`, `disable-model-invocation`, `allowed-tools`…) | **Ignored.** The serde struct has no `deny_unknown_fields`, so unknown keys are dropped silently. Proven by the live proof below. | [5], live test |
| Symlinks | Directory symlinks are **followed** for Repo, User and Admin scopes; ignored for System. Hidden directories below a root are skipped. Scan depth 6. | `codex-rs/ext/skills/src/loader/host.rs` (`DirectorySymlinkPolicy::Follow`), `loader/mod.rs` [6]; docs [1] |
| How a session uses skills | A `<skills_instructions>` block lists name + description + path for every skill (budget: 2% of context or 8,000 chars). Rule given to the model: use a skill when the user names it (`$name` or plain text) **or the task clearly matches its description**; then read the whole SKILL.md. `/skills` in the TUI lists them; `$name` invokes. `policy.allow_implicit_invocation: false` (in `agents/openai.yaml`) keeps a skill out of the model's list but still invocable with `$name`. | `catalog_prompt.rs` [7]; docs [1][2]; `skill-creator/references/openai_yaml.md` [8] |
| Untrusted folder | Project skills load even in a folder Codex has never trusted (live test below ran in a fresh scratch folder). | live test |

## Options

| Option | Works? | Verdict |
|---|---|---|
| (a) Codex reads `.claude/skills` by config | No such setting (only plugins or app-server API). | Rejected. |
| (b1) Second copy `template/.agents/skills`, a folder pair in `dogfood.json` checked by `dogfood_check.py`; this repo also gets `.agents/skills` | Works (live proof). Uses the existing script and manifest unchanged; the folder pair covers new skills and any `scripts/` files automatically. | **Recommended.** |
| (b2) Per-skill Jinja wrapper `template/.agents/skills/<n>/SKILL.md.jinja` = `{% include 'template/.claude/skills/<n>/SKILL.md' %}` | Works (byte-identical render). | Rejected: one wrapper per file to remember (no check catches a missing one), skill text becomes Jinja (a future `{{` breaks rendering), binary or script files cannot be included, and this repo still needs a dogfood pair for its own `.agents/skills`. |
| (c) Symlinks | Both tools follow them, but Git for Windows checks them out as text files and Copier then renders that text file. | Rejected (0031 already rejected symlinks for the same reason). |
| (d) Source in `.agents/skills`, Claude Code pointed at it | Claude Code has no skill-path setting; would need symlinks in `.claude/skills`. | Rejected. |

## Before starting

- Run `git merge main` into the branch first (main moves while other work lands). Depends on TASK-26 (declared; merged into `main` 2026-10-02), so the `ready` skill is in the copies: six shared skills (review-core, review-lenses, context-lenses, docs-lenses, scan-lenses, ready).
- Read `backlog instructions task-execution`; set TASK-28 In Progress. The reworded criteria are already in the task.

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
6b. `template/docs/protocols/ready.md` phase step 3: "takes the next free number when it writes it" becomes "takes the next number free on the main branch when it writes it" (a parallel branch took 0036 during this task's planning). Then `--sync`.
7. Commit (render with `--vcs-ref HEAD` sees committed work only).

## Checks

```powershell
python scripts/dogfood_check.py            # expect "0 problem(s)"
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=express . .tmp/smoke-express
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=next    . .tmp/smoke-next
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=rn      . .tmp/smoke-rn
```
In each render, prove the two skill folders are identical:
```powershell
python -c "import filecmp,os,sys;r=sys.argv[1];a,b=r+'/.claude/skills',r+'/.agents/skills';L=lambda p:sorted(os.path.relpath(os.path.join(d,f),p) for d,_,fs in os.walk(p) for f in fs);fa=L(a);ok=fa==L(b) and all(filecmp.cmp(os.path.join(a,f),os.path.join(b,f),shallow=False) for f in fa);ok=ok and len(fa)>0;print(len(fa),'files',('identical' if ok else 'DIFFER'));sys.exit(0 if ok else 1)" .tmp/smoke-express
```
(repeat for `smoke-next`, `smoke-rn`). Delete the `.tmp/smoke-*` folders afterwards.

## Live Codex proof (AC #3)

Render **outside** the repo and `git init` it: inside `.tmp/` Codex would walk up to this repo's `.git` and also list this repo's root `.agents/skills`, which muddies the proof.
```powershell
$p = "<scratchpad>/codex-proof"
uvx copier copy --trust --defaults --vcs-ref HEAD -d project_name=smoke -d stack=express C:\Users\jimzord12\Documents\GitHub\ai-foundations-template $p
git -C $p init -q
codex exec --sandbox read-only --ephemeral --json -C $p -o "$p-list.txt" "Answer only from the skills list in your instructions, without running any command or reading any file: which listed skills have their SKILL.md in this project's .agents/skills folder? Give each name with the path shown in the list." > "$p-list.jsonl"
codex exec --sandbox read-only --ephemeral --json -C $p -o "$p-use.txt" "Use `$review-core: open its SKILL.md and quote its first Markdown heading line exactly. Do not modify any file." > "$p-use.jsonl"
```
Expected: the list names every shared skill (six once TASK-26's `ready` is in) with a `rN/<name>/SKILL.md` path, and its `--json` event stream (redirect stdout to `$p-list.jsonl`) has no command-execution events; the second answers `# Review core`. Cross-check without a model call: `Push-Location $p; codex debug prompt-input "x"; Pop-Location` (the command has no `-C`) shows the `.agents/skills` root and the skills. Optional for this repo: `codex debug prompt-input "x"` at the repo root lists the root `.agents/skills`. Record commands and output in the task's final summary and the decision record.

## Decision record (after the proof)

Then write the decision record in its own commit. Number: the next one free on `main` (`git ls-tree --name-only main docs/decisions/`; 0037 today, since 0036 is taken), checked again just before merging: **"Codex reads the shared skills from a checked copy in `.agents/skills`"**, kind `technical`, decision-makers `agent`. Context: owner answer 4 in 0021 (Codex gets AGENTS.md and skills natively). Options a, b1, b2, c, d with one line each (the Options table above). Outcome b1. Consequences: good — one source, no new code, new skills covered automatically, proven live; bad — two physical copies in every generated project with no drift check there (instruction plus Parity lens only); Codex lists the reviewer skills (~1,300 chars of its catalog). More information: refines 0031 (the manifest now also holds a copy inside `template/`); the live proof commands and output. Add the row to `docs/decisions/README.md`. More Information also carries the key discovery facts (folders, no config path, the format, unknown keys ignored, symlink behaviour) and sources 1 to 8, so AC #1's evidence points to the record.

## Review loop (`docs/protocols/review.md`)

Mixed change, so each round runs three reviewers:
- `context-reviewer`: `template/docs/protocols/agents.md`, `context-lenses`, `ready.md` (step 6b), `AGENTS.md` (pass the diff text and the task; it has no shell).
- `docs-reviewer`: the decision record, decisions README row, `README.md`.
- `code-reviewer`: `dogfood.json` and the copy mechanism (the smoke and dogfood checks).

Tell every reviewer the `.agents/skills/` trees and `.claude/skills` copy are produced by `--sync` and verified by `dogfood_check.py`; review the sources only. Settled decisions for the brief: option b1; the six skill descriptions stay as they are (Codex lists them and uses them only when named, which is expected); no `agents/openai.yaml`; no drift check shipped to generated projects; symlinks and Jinja includes rejected. Fix Blocking and Material, re-run the checks, next round; stop on PASS (caps in `review.md`).

## Finish

`backlog instructions task-finalization`; tick the ACs and DoD with evidence; final summary. Merge into `main`, push, delete the branch locally and on the remote (each git command its own call in PowerShell). Remove `.tmp/smoke-*` and the scratch proof folder.

## Files touched

`dogfood.json`, `template/.agents/skills/**` (new, synced), `.agents/skills/**` (new, synced), `template/docs/protocols/agents.md` (+ synced copy), `template/.claude/skills/context-lenses/SKILL.md` (+ synced copies), `template/docs/protocols/ready.md` (+ synced copy), `AGENTS.md`, `README.md`, `docs/decisions/<nnnn>-codex-reads-the-shared-skills-from-a-checked-copy-in-agents-skills.md`, `docs/decisions/README.md`.

## Sources (all checked 2026-10-02)

1. OpenAI, "Build skills" (Codex skills page; `https://developers.openai.com/codex/skills` now 308-redirects here): https://learn.chatgpt.com/docs/build-skills
2. Same page, `agents/openai.yaml` example and `allow_implicit_invocation` default.
3. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/host_roots.rs
4. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/config/src/skills_config.rs
5. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/skills/src/parser.rs
6. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/loader/host.rs and `loader/mod.rs`
7. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/catalog_prompt.rs
8. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/skills/src/assets/samples/skill-creator/references/openai_yaml.md
9. Claude Code docs, Skills: https://code.claude.com/docs/en/skills
10. Copier docs, Configuring (`preserve_symlinks`): https://copier.readthedocs.io/en/stable/configuring/
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

## Readiness challenge, task level, round 2 (2026-10-02): NOT READY

Run through the gate's fallback (code-reviewer applying the ready skill), because this session cannot load the new readiness-challenger profile until it restarts.

- Material: the decision-record number would collide. `main` gained 0036 during the round, from the owner's parallel config-extension work. Fixed: merge `main` into the branch first, and take the next number free on `main` (0037 today), re-checked before the merge.
- Minor: AC #1 had no record location. Fixed: the record's More Information carries the discovery facts and sources.
- Minor: the comparison one-liner passed with 0 files. Fixed: it now also requires `len(fa)>0`.
- Minor: the step order was misleading. Fixed: the record moved to its own section after the proof.
- Minor: a stale "section 3" pointer. Fixed.
- Minor: reviewers could widen the scope to the six skill descriptions. Fixed: settled in the brief that the descriptions stay.
- Minor: `codex debug prompt-input` has no `-C`. Fixed: it now uses Push-Location.
- Adopted: ready.md says the record number is "free on the main branch" (plan step 6b).

## Readiness challenge, task level, round 3 (2026-10-02): READY

Fallback challenger (code-reviewer + ready skill). One Minor folded in: step 6b files added to Files touched and the context-reviewer list. Notes: 6b is a lesson from planning (kept); if 0037 is taken before merge, rename and fix the index row and links.

## Evidence (2026-10-02)

- dogfood: `python scripts/dogfood_check.py --sync` created both `.agents/skills/` trees (12 files). `python scripts/dogfood_check.py` then reported 0 problem(s).
- Smoke test express / next / rn: each exited 0. In each render, the comparison one-liner printed "6 files identical" for `.claude/skills` against `.agents/skills`.
- Live Codex proof (AC #3), codex-cli 0.159.3, on a fresh express render in the session scratchpad (outside any repo, after `git init`):
  - `codex exec --sandbox read-only --ephemeral --json -C <dir> -o <dir>-list.txt "<list prompt>" > <dir>-list.jsonl`
    - Answer: context-lenses, docs-lenses, ready, review-core, review-lenses, scan-lenses, each at `r9/<name>/SKILL.md`.
    - Event log: thread.started, turn.started, 1 agent_message, turn.completed, and 2 error items. Both errors are a user-config warning (an unrecognized `mcp_servers` setting in `~/.codex/config.toml`), not the template.
    - No command_execution events.
  - `codex exec ... "Use $review-core: open its SKILL.md and quote its first Markdown heading line exactly. Do not modify any file."`
    - Answer: `# Review core`.
    - One command_execution: `Get-Content -LiteralPath '.agents/skills/review-core/SKILL.md'`.
  - The proof folder was deleted afterwards.
- Independent check by the round-1 docs-reviewer (no model call):
  - In a never-trusted render, `codex debug prompt-input` listed all six skills.
  - From a subfolder, the walk-up to `.git` still found them.
  - Without `.git`, a copy one level up was not found.
  - The six skills take 1,302 characters of the list.
<!-- SECTION:NOTES:END -->

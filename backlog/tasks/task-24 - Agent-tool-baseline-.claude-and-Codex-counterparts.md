---
id: TASK-24
title: 'Agent tool baseline: .claude/ layout, permission allowlist, dogfood manifest'
status: In Progress
assignee:
  - '@claude'
created_date: '2026-10-01 16:40'
updated_date: '2026-10-02 00:41'
labels:
  - agents
  - claude
  - codex
  - ready
milestone: m-0
dependencies:
  - TASK-15
priority: high
type: feature
ordinal: 500
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Owner of the agent-tool layout for this repo and generated projects. Layout rule (decision 2026-10-01, specific thin agent profiles plus shared skills): .claude/agents/ holds one-job profiles that preload skills; .claude/skills/ holds the shared knowledge. Codex native support is TASK-28. Permission allowlist per owner answer 2026-10-01. Verify current Claude Code settings and agent docs before building.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 template/.claude/settings.json ships with an allowlist for generated projects. Open owner question before building: the narrow list from owner answer 5 (read-only tools, package scripts, backlog, git add/commit/push, git switch, branch, merge and push --delete; nothing broader), or the permissive policy this repo adopted in decision 0027 (everything allowed except deleting main). Either way it needs narrow per-command rules, because auto mode drops blanket Bash, PowerShell, Agent and Monitor rules (see 0027 and scripts/permissions/). This repo's own root settings are owned by TASK-31
- [ ] #2 .claude/agents/ and .claude/skills/ layout documented in the router of both the root and the template AGENTS.md (at most 4 lines each) and in docs/protocols/agents.md (thin profiles, skills preloaded with the skills field, read-only reviewers get no Edit or Write, dogfooded files must not be .jinja or link to template-only files)
- [ ] #3 Dogfood manifest at dogfood.json in this repo's root lists source-to-copy pairs. TASK-24 adds only docs/protocols/agents.md and the .claude/agents and .claude/skills folders (copied recursively; a mapped folder holds only template copies); TASK-11 adds review.md and TASK-26 adds ready.md when they create them. Template-only files (charter.md, evolution.md, git.md, done.md, stack files) are never copied
- [ ] #4 Proof via headless claude -p --output-format stream-json --verbose in a generated project with --setting-sources project and no permission-skipping flags: an allowlisted command runs without a prompt and a non-listed command appears in permission_denials. An untrusted workspace ignores project allow entries, so either use a trusted workspace or pass the file with --settings in dontAsk mode, as the TASK-31 proof did
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
1. Start after TASK-15 merges; branch feature/task-24-agent-layout from main; next free record number.
2. Generated-project permissions (AC1): build with the standing owner answer 5 (decision 0021, amended by 0024) because it is the last explicit owner answer for generated projects; the permissive alternative (0027 style) goes to the owner's question batch and would be a one-flag regeneration. scripts/permissions/gen_settings.py gains a profile argument: 'repo' (current output, byte-identical) and 'template'. Template profile:
   - allow: Read, Glob, Grep; narrow Bash and PowerShell rules (no blanket entries, since auto mode drops them anyway and answer 5 says nothing broader): git status, log, diff, show, add, commit, push, switch, branch, merge, fetch, pull (each bare and with args, and git -C forms); npm run check, typecheck, lint, format, format:check, test, build; npm test; npm ci; npm install; backlog *, npx backlog.md *.
   - ask (mirrors the AGENTS.md ask-first list, TASK-14): deleting main or another core branch (main, production, stage, dev) locally or on the remote, in the spellings the repo generator already covers; merging is not command-detectable per target branch, so it stays an instruction-only rule (documented); force pushes; reset --hard; git clean -<flags>; branch -D, -f, --force.
   - deny: none (the owner's list for generated projects is ask-first, not forbidden).
   - check_settings.py gains the same profile argument with a template must-allow / must-ask list; 0 mismatches for Bash and PowerShell.
3. template/.claude/settings.json written from the generator (if the classifier refuses the write as a protected path, write it to the scratchpad and add it to the owner's copy batch; record that).
4. template/docs/protocols/agents.md (generic, dogfooded unchanged): layout (.claude/agents/ one-job profiles that preload shared skills via the skills field; .claude/skills/ shared knowledge); thin profiles; read-only reviewers get no Edit or Write; profile frontmatter fields verified against current Claude Code subagent docs (name, description, tools, model, skills); PowerShell: run each git command as its own call (no && chains: narrow rules never pre-approve them); workspace trust note; .claude/ is a protected path, so agent writes there may need the owner. Dogfooded files must not be .jinja or link to template-only files.
5. Router: template AGENTS.md one row 'Adding or changing an agent profile, skill or permission rule | docs/protocols/agents.md'; root AGENTS.md one line in 'Where things go' for .claude/agents, .claude/skills and the dogfood manifest. At most 4 non-blank lines each.
6. dogfood.json in this repo's root: [{"source": "template/docs/protocols/agents.md", "copy": "docs/protocols/agents.md"}, {"source": "template/.claude/agents/*", "copy": ".claude/agents/"}, {"source": "template/.claude/skills/*", "copy": ".claude/skills/"}]; docs/protocols/agents.md copied byte-identical; a small check (scripts/dogfood_check.py) compares pairs and exits 1 on drift (TASK-13 CI will run it).
7. Proof (AC4): render a project per stack into a throwaway folder outside any repo; run headless claude -p --settings <rendered .claude/settings.json> --permission-mode dontAsk --setting-sources project --output-format stream-json --verbose: an allowlisted command (git status, backlog --version) runs; a non-listed command (for example curl or node -e) lands in permission_denials; an ask entry (git reset --hard) is refused in dontAsk.
8. Record (kind technical for layout and manifest; the permissions part cites 0021/0024 and notes the open owner question). Index row.
9. Review loop to PASS; merge, push, delete branch.
10. Plan v2 amendments after readiness round 1 (3 Material, 7 Minor, all explicit; no further round):
   - Permissions frame: the record applies 0021 answer 5 and 0024 (not a new product decision); the permissive option goes to the owner batch (🧭). Template profile: no 'git -C *' blanket; per-subcommand 'git -C * <sub>' forms only. Bare 'npm install' only, never 'npm install *'. 'deny': [] present. Extra ask entries: pushes deleting or overwriting production, stage, dev (':branch', 'HEAD:branch'), 'git switch' with --discard-changes, -f or -C. Hardcoded core branches main, production, stage, dev are documented.
   - agents.md: frontmatter fields verified 2026-10-02 (name, description required; tools, disallowedTools, model, permissionMode, maxTurns, skills, effort, isolation, memory, hooks, background and others); tools omitted means all tools inherited; skills injects full content. Behaviour-only PowerShell rule ('run each git command as its own call'); trust note (accept the trust prompt once before unattended claude -p); the allowlist reduces friction and is not a sandbox; manual mode prompts on edits (no Edit/Write allow); .claude/ writes are protected; nested template skills may show twice; GitHub ruleset recommendation. Generic wording for 'no template syntax, links only to files that exist in the project'.
   - Dogfood: manifest pairs with recursive semantics (template/.claude/skills/** -> .claude/skills/); drift = missing, differing or extra files under a mapped prefix; a source that matches nothing passes; scripts/dogfood_check.py has --sync; root AGENTS.md says the owner runs --sync when the classifier refuses an agent write under .claude/.
   - Proof: one stack; git init in the rendered folder; dontAsk with --settings: non-read-only allowlisted commands (git switch -c, git add, git commit, backlog --version) run; control run without --settings denies them; ask probes that also match allow rules (git push origin --delete main, git branch -D feature/x, git push --force origin x) are refused. Auto-mode run with --settings and --debug: read the debug log for dropped rules; anything not observable is recorded as 'not observed in auto mode' (npm run entries, npx backlog.md).
<!-- SECTION:PLAN:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01 owner of the .claude/ and Codex layout. TASK-11 (reviewer agents) and TASK-22 (maintenance skill) put their files into this layout.

2026-10-01: allowlist amended with branch commands (decision 'Branch model refinements after the first instruction review').

2026-10-02 (TASK-14): the generated-project settings ask and deny entries must match the ask-first list in template AGENTS.md 'Git and safety' (deleting main or another core branch, deleting an unmerged unique branch, force push, reset --hard, git clean).

2026-10-02 readiness round 1 NOT READY: 3 Material (proof did not test the allowlist, auto-mode behaviour unproven, dogfood semantics for skills underspecified) and 7 Minor, all explicit fixes folded into plan v2 (step 10); proceeding without another round. Building AC1 with the standing owner answer 5 (0021, amended by 0024); the permissive alternative goes to the owner's question batch.

Verification: generator repo profile byte-identical to .claude/settings.json; template profile 123 allow / 0 deny / 616 ask; check_settings.py 0 mismatches for repo (64) and template (51) profiles, Bash and PowerShell. Smoke express/next/rn exit 0, AGENTS.md 67/68/67 lines, rendered .claude/settings.json identical to the template file, agents.md present, no Jinja leftovers, leak grep clean. dogfood_check.py: detects missing and differing copies (exit 1), --sync fixes them, clean run exit 0. Proof (evidence in scratchpad proof-evidence/task24/): dontAsk with --settings: switch -c, commit, backlog ran; push --delete main, branch -D, push --force and node -e refused; control without --settings: all refused; auto with --settings and --debug: the three ran from allow rules (no permission suggestion, unlike node -e which hit the classifier), ask commands held. Project-scoped allow entries were ignored in all runs (untrusted folder), which is why the file was passed with --settings. Not observed in auto mode: npm run and npx backlog.md entries.

Review round 1 FINDINGS (1 Material, 5 Minor, 4 Notes), fixed: M1 quoted ':core' pushes and 'branch * -m/-M core' now ask in the template profile (checker probes added); m1 HEAD:main allowed, HEAD: asks only for production, stage, dev; m2 checker f-string fixed and more ask probes (62 template checks, 0 mismatches both shells); m3 agents.md says the template ships the narrow list, 'ask-first list in AGENTS.md', '.claude/settings.json' instead of 'this file' (dogfood copy resynced); m4 mapped folders hold only template copies (dogfood.json, 0031); m5 debug-log excerpt kept in evidence and 0031 wording softened. Notes: AC3 text now says folders copied recursively; template allowlist is slightly wider than answer 5 (fetch, pull, npm ci, bare npm install, git -C forms) — included in the owner question; --dry-run pushes naming main ask (harmless).

Review round 2 FINDINGS (1 Material, 2 Minor, 2 Notes), fixed: M1 quoted and refs/heads spellings now ask for every core branch, not only main; m1 quoted and refs/heads pushes into production/stage/dev ask; m2 forced rename or copy onto a core branch asks (branch -m/-M/-c/-C/--move/--copy * <core>); a first attempt (branch * <core>) wrongly asked for git branch --merged main and the checker caught it. Template profile now 123 allow / 0 deny / 1380 ask (earlier note's 616 is stale); checker 70 template and 64 repo checks, 0 mismatches in both shells; repo profile still byte-identical. n1 git branch -M main after git init asks once at setup (accepted).
<!-- SECTION:NOTES:END -->

---
status: accepted
date: 2026-10-02
decision-makers: agent
kind: technical
supersedes: []
---

# Codex reads the shared skills from a checked copy in .agents/skills

## Context and Problem Statement

Owner answer 4 in [0021](0021-phase-1-readiness-answers-owner.md): in v0.1.0, Codex gets only what it supports natively, AGENTS.md and skills. The owner's decision quoted in TASK-28 adds: from one source of truth. Claude Code reads skills only from `.claude/skills/`; Codex's project skill folder is `.agents/skills/`. Neither tool has a setting to read the other's folder. TASK-28.

## Considered Options

- (a) Configure Codex to read `.claude/skills`: no such setting exists (only plugins or the app-server API add roots).
- (b1) A second copy, `template/.agents/skills`, made and checked by `dogfood.json` folder pairs; this repo also gets `.agents/skills`.
- (b2) A Jinja wrapper per skill that includes the `.claude/skills` file: one wrapper per file to remember, with no check to catch a missing one; skill text becomes Jinja; scripts cannot be included.
- (c) Symlinks: Git for Windows checks them out as text files, and Copier then renders that text file (also rejected in [0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md)).
- (d) Source in `.agents/skills`, with Claude Code pointed at it: Claude Code has no skill-path setting.

## Decision Outcome

Chosen option: "(b1) a second copy checked by folder pairs", because it is the only option that works on every platform, it uses the existing manifest format and script (only two pairs are added), and a folder pair covers every new skill and any `scripts/` inside it automatically.

- `template/.claude/skills/` stays the one source. `dogfood.json` copies it to `template/.agents/skills/`, which Copier renders into every generated project, and to this repo's `.agents/skills/`. `python scripts/dogfood_check.py` fails on drift.
- In generated projects, `docs/protocols/agents.md` says a shared skill is changed in `.claude/skills/` and copied to `.agents/skills/` in the same change, and the `context-lenses` Parity lens treats a skill changed in one folder only as a finding.
- The six skill descriptions stay as they are. Codex ignores Claude-only frontmatter such as `user-invocable`, so it lists the reviewer skills as ordinary skills and uses them only when named or clearly matched. That is expected.
- No `agents/openai.yaml` per skill.

### Consequences

- Good, because one source feeds both tools with no new code, and a live Codex session proved it.
- Bad, because every generated project holds two physical copies with no drift check there, only the written rule and the Parity lens.
- Bad, because the six shared skills (reviewer and challenger lenses) take about 1,300 characters of Codex's skill list, out of a list budget of 2% of the model's context window (8,000 characters as the fallback); a 0.159.3 session listed 12.7k characters of skills without truncation.

## More Information

- Refines [0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md): the manifest now also holds a copy inside `template/`. Applies owner answer 4 of [0021](0021-phase-1-readiness-answers-owner.md).
- How Codex finds skills, verified on 2026-10-02 against codex-cli 0.159.3:
  - **Where it looks:** `.agents/skills/<name>/SKILL.md` in every folder from the working folder up to the project root (the nearest `.git`), plus `~/.agents/skills` for the user (also `.codex/skills` when the project has a `.codex/` config layer, and the deprecated `~/.codex/skills`; neither is used here).
  - **No extra path setting:** `config.toml`'s `[skills]` cannot add a folder.
  - **Format:** it reads `name`, `description` and `metadata.short-description`, and silently ignores unknown keys.
  - **Symlinks:** it follows directory symlinks for project and user folders.
  - **Untrusted folders:** project skills load even in a folder Codex has never trusted.
- Sources, all checked 2026-10-02:
  1. https://learn.chatgpt.com/docs/build-skills (the former developers.openai.com/codex/skills).
  2. The same page, on `agents/openai.yaml`.
  3. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/host_roots.rs
  4. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/config/src/skills_config.rs
  5. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/skills/src/parser.rs
  6. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/loader/host.rs
  7. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/catalog_prompt.rs
  8. https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/skills/src/assets/samples/skill-creator/references/openai_yaml.md
  9. Claude Code skills (skills only from `.claude/skills/`, no skill-path setting): https://code.claude.com/docs/en/skills
  10. Copier configuring, `preserve_symlinks` (a symlink is rendered as the file it points to): https://copier.readthedocs.io/en/stable/configuring/
  11. Skill-list budget (2% of the context window in tokens, 8,000 characters as the fallback; `[skills] max_context_tokens` overrides): https://github.com/openai/codex/blob/rust-v0.159.3/codex-rs/ext/skills/src/render.rs
- Known residue: a Codex session started inside `template/` of this repo lists each shared skill twice (it walks up past `template/.agents/skills` to `.agents/skills`); start Codex at the repo root.
- Live proof, on a fresh express render outside any repo, after `git init`:
  - `codex exec --sandbox read-only --ephemeral --json -C <dir> -o <out> "<prompt>"` with a list prompt. Codex named all six skills (context-lenses, docs-lenses, ready, review-core, review-lenses, scan-lenses) at `r9/<name>/SKILL.md` (Codex's skill-roots table mapped `r9` to the render's `.agents/skills`; the number depends on the machine's other skill roots), and its event log had no command executions.
  - A second run asked to use `$review-core`. Codex read `.agents/skills/review-core/SKILL.md` and quoted `# Review core`.

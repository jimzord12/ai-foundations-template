# Decision log: ai-foundations-template

Decisions about the template itself. Newest at the bottom. To change a decision, add a new entry that references the old one.

<!-- Entry format:
### YYYY-MM-DD: <decision title>
- **Context:** what needed deciding and why
- **Decision:** what was chosen
- **Alternatives considered:** each option and why it lost
- **Consequences:** tradeoffs accepted, what would trigger revisiting
-->

### 2026-09-29: Don't adopt Effect-TS
- **Context:** Effect encodes success/error/dependencies in types and adds structured concurrency, retries, resource safety. Evaluated as a foundation for all projects. (Decided in discussion before this repo existed.)
- **Decision:** Not adopted. Use `neverthrow` for typed errors, plain factory functions for dependency injection, small focused libraries (`p-retry`, `p-limit`) for retries/concurrency.
- **Alternatives considered:** Effect everywhere — pays off only in large backends orchestrating lots of unreliable I/O; overkill for CRUD APIs, Next.js UIs, RN apps. Its "better with agents" benefit (stricter compiler) is offset by API churn (v4 was a release candidate, v3 still recommended for production) and less training data.
- **Consequences:** Revisit if a project becomes a large I/O-orchestration backend (LLM calls, payments, job workers) or Effect v4 stabilizes and gains adoption.

### 2026-09-29: Agent-instruction baseline
- **Context:** Needed shared instructions so agents write consistent, standard code and leave a decision trail.
- **Decision:** Adopt the text in `docs/agent-instructions.md`: standard-over-custom philosophy, opt-in autonomous mode (never for hard-to-reverse choices), decision logging with a defined "non-trivial" bar and end-of-task decision summary, and a TS "reuse before building" checklist with a preferred-library list.
- **Alternatives considered:** Moving the TS section into a skill loaded only for TS projects — rejected, all current projects are TypeScript.
- **Consequences:** The preferred-library list can go stale; a review protocol + tooling is tracked in the backlog. Where the text lives (global vs. per-project) is still open.

### 2026-09-29: Distribute the template with Copier
- **Context:** Projects must start from the template *and* receive template improvements later. Copy-once approaches let projects drift.
- **Decision:** Copier (verified v9.18.2). Projects are created with `uvx copier copy` and updated with `uvx copier update`, which 3-way-merges template changes between git tags and keeps local edits.
- **Alternatives considered:** GitHub template repo / degit / giget — copy-once, no updates. Cookiecutter — needs an add-on (cruft) for updates. Custom `create-*` Node CLI — would require building and maintaining update logic ourselves. Shared npm config packages — good for configs only, can't ship files like `AGENTS.md`/`docs/`; may be added later for configs that change often.
- **Consequences:** Adds a Python tool (run via `uv`, no Python project needed). Template changes reach projects only after a git tag. Renaming Copier questions requires migrations.

### 2026-09-29: One template, shared files + conditional per-stack files
- **Context:** Stacks (Express 5 + Zod, Next.js 16.3, bare React Native 0.81/Hermes) share most rules but differ in places. Initial idea was literal `base/` + `stacks/<name>/` folders.
- **Decision:** A single Copier template rooted at `template/` (`_subdirectory`) with a `stack` question. Shared files are plain; stack-specific files use conditional names (e.g. `.claude/rules/{% if stack == 'rn' %}stack-rn.md{% endif %}`) and small `{% if %}` blocks inside shared files.
- **Alternatives considered:** Literal `base/` + `stacks/` folders — Copier renders one directory tree per template, so overlays would need copy scripts in `_tasks`, which break `copier update` diffs. Separate templates per stack (or a base template + stack templates applied with separate answers files) — duplicates the base or needs multiple repos and multiple update runs per project.
- **Consequences:** Stack-specific files are scattered through `template/` instead of grouped in one folder. Revisit if stack differences grow large enough that multiple templates are simpler.

### 2026-09-29: Track open work with Backlog.md
- **Context:** Needed a place for open work/backlog that agents and humans can both read and update.
- **Decision:** [Backlog.md](https://github.com/MrLesk/Backlog.md) (verified v1.53.0, MIT): markdown task files in `backlog/`, git-native, with a CLI (`npx backlog.md ...`) and agent instructions.
- **Alternatives considered:** A single `docs/open-work.md` — no structure/status; GitHub Issues — lives outside the repo, less visible to agents working locally.
- **Consequences:** Backlog.md also has its own `backlog/decisions/` folder; for now decisions stay in `docs/decisions.md` (single-file log agreed earlier). Revisit if one system should own both.

### 2026-09-29: Public GitHub repo, MIT license
- **Context:** Where the template lives and under what terms.
- **Decision:** Public GitHub repository; MIT license.
- **Alternatives considered:** Private repo — safer default but nothing here is secret and public makes `copier copy gh:...` work without auth. Other licenses (Apache-2.0) — MIT is the most common permissive default for small tooling.
- **Consequences:** Never commit secrets or client-specific details to the template.

### 2026-09-29: Agent instructions live per project, as a thin AGENTS.md router
- **Context:** TASK-1. The baseline was written for a global CLAUDE.md, but cloud sessions, CI agents, other tools and collaborators only see files in the repo. Prior projects showed a 17K AGENTS.md becomes a text wall.
- **Decision:** `template/AGENTS.md.jinja` (short; target under about 100 lines) carries roles, owner profile, philosophy, authority tiers, decision rules and stack blocks, plus a "when to read what" router to files under `docs/`. `CLAUDE.md` contains only `@AGENTS.md`. Stack rules are inline `{% if stack %}` blocks so every agent sees them. The global `~/.claude/CLAUDE.md` keeps only the owner's personal style. Supersedes the "placement open" note in the agent-instruction baseline entry, and narrows "One template, shared files + conditional per-stack files": stack rules are inline blocks, no longer separate `.claude/rules/stack-*.md` files. Global scope: personal style only (tone, language, push-back preference); nothing about libraries, decisions or conventions.
- **Alternatives considered:** Everything global — invisible to anything but the owner's local Claude Code. Stack rules in `.claude/rules/` with `paths:` — Claude-only, so CI and cloud agents would miss them; reserve that mechanism for long path-scoped rules later.
- **Consequences:** Baseline changes reach projects via a template tag plus `copier update` (not instantly). Keep AGENTS.md under about 100 lines; new detail goes in linked files.

### 2026-09-29: Agents decide within repo rules; owner decides the hard-to-reverse list
- **Context:** The owner does not want to babysit. The baseline said "ask before choosing new libraries" by default, which creates friction.
- **Decision:** Changes the default in the agent-instruction baseline: the agent decides libraries, patterns, structure and tooling itself, bounded by the repo's instruction files and decision log, and logs non-trivial decisions. The owner decides the hard-to-reverse list (database, auth, hosting, paid services, core framework, anything contradicting the instructions). Evolution: start simple, fix friction, then patterns and abstractions, then heavier structure; rule of three (2nd occurrence noted, 3rd extracted); restructuring is the agent's call, surfaced to the owner as a proposal (until the proposal pipeline of TASK-9 exists, the interim rule in AGENTS.md is: log it and tell the owner in the end-of-task summary).
- **Alternatives considered:** Ask-first by default with an opt-in autonomous mode — more friction than the owner wants.
- **Consequences:** Quality depends on the instruction files being good; details are tracked in TASK-7.

### 2026-09-29: Owner-facing items are JSON; history log stays markdown
- **Context:** Anything the owner must know, approve or decide has to be renderable in a viewer.
- **Decision:** Questions (2-6 options plus a recommendation), decisions needing approval, findings and proposals are JSON validated by versioned JSON Schemas shipped under a `.foundations` folder (TASK-8). The historical decision log stays readable markdown. Schemas are viewer-agnostic; Night Shift's `ask` and `feedback` commands cover the gap until the viewer is generic.
- **Alternatives considered:** Everything markdown — not machine-renderable. Everything JSON — poor for humans reading history.
- **Consequences:** TASK-5 (one log vs Backlog.md decisions) stays open.

### 2026-09-29: Evolve Night Shift into the shared generic viewer
- **Context:** The owner works on many projects at once; one viewer across projects beats a copy in each.
- **Decision:** Night Shift becomes a generic mini-framework where agents describe UIs in JSON and tooling validates the schema. Not built in this template. Tracked as TASK-6, blocked until Night Shift's viewer stabilizes; needs a dedicated design discussion first. Start with fixed item kinds (question, finding, proposal, report) and generalize only on a third real need.
- **Alternatives considered:** New viewer inside the template (about 2 days, a copy per project); vendored copy of Night Shift (stale quickly).
- **Consequences:** The template depends on a separate repo maturing.

### 2026-09-29: Findings are ephemeral; proposals are GitHub issues with occurrence counts
- **Context:** Subagents must report pains, frictions, ideas and risks, and several agents may report the same problem.
- **Decision:** Every subagent report ends with a `findings` block. The lead triages and dedupes, then creates or updates a GitHub issue (a proposal) that counts how many times the problem was reported. The owner approves proposals in the viewer; the lead then creates the Backlog task. Findings themselves are not stored long term. Issue text must contain no secrets (repos may be public). Tracked in TASK-9.
- **Alternatives considered:** A persistent findings file — duplicates pile up and nobody reads it.
- **Consequences:** Needs a reliable dedupe step by the lead.

### 2026-09-29: Review loop caps raised to 8 attended and 15 unattended
- **Context:** The owner's experience is that fresh-context review loops are very valuable; the cap only guards against a stuck agent. Earlier projects used 5 and 10.
- **Decision:** Caps of 8 rounds attended and 15 unattended, interpreted as maximums (a PASS verdict stops the loop). Unresolved after the cap goes to the owner. Tracked in TASK-11.
- **Alternatives considered:** Fewer rounds scaled to change size — rejected by the owner.
- **Consequences:** More time per non-trivial change.

### 2026-09-29: Neutral default profile plus optional personalization skill
- **Context:** The owner's personal style is in the global CLAUDE.md, but cloud agents and collaborators need sensible defaults.
- **Decision:** The template's AGENTS.md carries a neutral technical-product-owner profile. An optional skill run on new installations interviews the user for 10-15 minutes and writes preferences to the git-ignored `.local/preferences/`. Tracked in TASK-12.
- **Alternatives considered:** Copying the owner's personal rules into every project — leaks personal style to collaborators.
- **Consequences:** Preferences live outside version control.

### 2026-09-29: Generated projects use Backlog.md and ignore `.local/`
- **Context:** Review of TASK-1 found the generated AGENTS.md told agents to use Backlog.md although the template ships no `backlog/` folder, and referred to a git-ignored `.local/` although no `.gitignore` existed. The earlier Backlog.md decision covered only this template repo.
- **Decision:** Generated projects track work with Backlog.md; AGENTS.md tells the agent to run `npx backlog.md init "<name>" --defaults --agent-instructions none` if `backlog/` is missing (the bare command is interactive and appends a duplicate guidelines block to AGENTS.md; no custom init task in Copier). The template ships `.local/.gitignore` (`*` plus `!.gitignore`) instead of a root `.gitignore`, so personal preferences are never committed.
- **Alternatives considered:** Shipping a pre-made `backlog/config.yml` — couples the template to one CLI version's config format. A root `template/.gitignore` — Next/RN projects are scaffolded first and already have one, so Copier would prompt to overwrite it (losing framework ignores) or conflict on `copier update`. Similarly `create-next-app` writes its own `AGENTS.md`: the README tells users to accept the overwrite, and the Next stack block keeps its managed `nextjs-agent-rules` block at the end of the file. RN's CLI ships no AGENTS.md.
- **Consequences:** Revisit if projects should start with a pre-initialized backlog.

### 2026-09-29: The generic viewer gets its own repo, not this template
- **Context:** The 2026-09-29 entry "Evolve Night Shift into the shared generic viewer" left the viewer as work tracked inside this template (TASK-6). On reflection the owner judged it far beyond the scope of a project template.
- **Decision:** The generic JSON-driven viewer framework is built in its own repository (TASK-6 now tracks creating it; whether it is Night Shift evolved in place or a new repo is the first design-session question). This template keeps only the viewer-agnostic schemas (TASK-8) and a register-this-project step. Still blocked until Night Shift's viewer stabilizes.
- **Alternatives considered:** Building the viewer inside this template — mixes a product with a scaffold and forces every generated project to carry or track it.
- **Consequences:** The template depends on a separate repo maturing; the interim bridge (Night Shift `ask` and `feedback`) stays as decided.

### 2026-09-30: Repo-maintenance capability ships in this repo and in generated projects
- **Context:** TASK-22. The owner's research bundle (written for another repo) provides a repo-maintenance skill, a 35-check checklist, a stdlib-Python audit script and a read-only auditor agent, split into a generic core and a repo-specific layer.
- **Decision:** (1) Ship the generic core in both this repo and every generated project; only the small repo-specific adapter differs (this repo's adapter adds template checks such as the smoke test, decision-log and backlog hygiene). Generated projects get the same core, not a lighter fork. (2) Python (3.8+, stdlib) is accepted as a dependency of the audit script, even for TypeScript projects. (3) `template/.claude/skills/repo-maintenance/` is the single source of truth; this repo's own copy under the root `.claude/` is verified identical by CI (TASK-13), never edited by hand. Nothing specific to the source repo may be imported (filter recorded in TASK-22).
- **Alternatives considered:** Ship only in this repo — generated projects would drift unchecked. A lighter fork for projects — two versions to maintain. Port the script to Node — about 36 KB of rewriting for no gain, since Copier already needs Python tooling (`uv`). A symlink for the dogfooded copy — unreliable on Windows.
- **Consequences:** A custom 36 KB script conflicts with "standard over custom"; accepted as a justified exception because the checks must be deterministic and dependency-free, and the script only composes existing tools where they exist (knip, lychee, gitleaks). The skill was never tested in a live Claude Code session by its authors, so TASK-22 requires a live test before shipping.

### 2026-10-01: Keep the one-line CLAUDE.md even though Claude Code reads AGENTS.md natively
- **Context:** Claude Code v2.1.277+ reads `AGENTS.md` directly, but only when no `CLAUDE.md` or `CLAUDE.local.md` exists in the working directory or any directory above it (the user's `~/.claude/CLAUDE.md` does not count). The owner's ICS workspace folder has its own `CLAUDE.md`, so a project created under it without a `CLAUDE.md` would silently lose its `AGENTS.md`.
- **Decision:** Generated projects keep `CLAUDE.md` containing only `@AGENTS.md` (decided in the 2026-09-29 placement entry). Official docs confirm the import never causes a double read.
- **Alternatives considered:** Drop `CLAUDE.md` — one file fewer, but silent loss of all rules under a parent `CLAUDE.md`, on older CLIs and in the first session after an upgrade.
- **Consequences:** Revisit if Claude Code changes the default to read both files.

### 2026-10-01: Project knowledge system: decision records, architecture.md, levelled DDD
- **Context:** Projects need a home for product, architecture and technical decisions, the current architecture, and a shared domain language. TASK-5 asked whether to keep a single `docs/decisions.md` or use Backlog.md decisions.
- **Decision:** A project knowledge system separate from the feedback loop (they meet only where an accepted proposal produces a decision). Decisions: one file per decision in `docs/decisions/` (MADR standard) with `kind: product | architecture | technical`; the owner decides product, the agent proposes architecture (owner approves big ones), the agent decides and logs technical. `docs/architecture.md` holds the current shape and is updated in the same change as each accepted architecture decision. DDD is mandatory but levelled: a glossary always (ubiquitous language), a domain map once a second business area exists, tactical patterns only through architecture decisions. A design evolution protocol (signals, procedure, step-down rule) tells agents when to add or remove structure (TASK-7). Supersedes the single-file decision log for generated projects; resolves TASK-5. Implemented in TASK-25.
- **Alternatives considered:** Three separate logs per kind — agents must check several places and some decisions span kinds. Backlog.md decisions — couples records to one tool. Full tactical DDD everywhere — heavy overhead on small apps. Making it part of the feedback loop — mixes "how agents work" with "what the product is".
- **Consequences:** More files per project; their effect on agents is measured by the evals (TASK-20), including whether the glossary changes naming.

### 2026-10-01: Definition of Ready gate before unattended work
- **Context:** Tasks went straight from "created" to "worked on", so gaps surfaced mid-run when the owner was away. The owner wants every task planned and challenged before unattended work, here and in generated projects.
- **Decision:** A Definition of Ready gate (the standard counterpart of a Definition of Done): (1) ready checklist (why, testable acceptance criteria, dependencies, one-change size, open decisions answered, verification named); (2) the plan is written into the task with the real seams traced; (3) a fresh-context reviewer with a readiness lens returns READY or NOT READY; (4) owner-only questions are batched with a recommended answer each. Unattended work starts only on READY; the owner may waive it when present; depth scales with task size. Two levels: per task, and per phase (phase plan doc plus a ready check of every task in it). Ready tasks carry the `ready` label. Ships in the template and is used in this repo. Tracked in TASK-26.
- **Alternatives considered:** Backlog.md drafts as the "not ready" state — tested 2026-10-01: `backlog task demote` did nothing on a scratch copy, and promotion may renumber tasks and break references, so a label is used instead. Planning only at pickup — leaves gaps to be found mid-run.
- **Consequences:** Every task costs a planning and challenge step; small tasks get a light version.

### 2026-10-01: Specific thin agent profiles plus shared skills
- **Context:** The owner prefers specific agent profiles over generic ones. Claude Code subagents can preload skills (`skills:` frontmatter injects the full skill content at startup), so knowledge and job can be separated.
- **Decision:** Two layers. Agent profiles are specific and thin: one job each (for example `readiness-challenger`, `code-reviewer`, `repo-auditor`), with their own trigger description, tool list (read-only reviewers get no Edit or Write, so read-only is enforced), model and turn limit. Knowledge lives in shared skills preloaded by those profiles (for example `review-core` for fresh-context rules, evidence and severity words; `ready` for the gate; `repo-maintenance` for the audit). Each rule is written once. Supersedes the earlier suggestion of one reviewer with two lenses.
- **Alternatives considered:** One generic reviewer with lenses — less precise triggering and tool limits. Fully specific agents with duplicated rules — rules drift apart.
- **Consequences:** Skills are portable to Codex while agent files are Claude-specific. Each preloaded skill adds context to every run, so skills stay tight.

### 2026-10-01: Phase 1 readiness answers (owner)
- **Context:** The first Ready-gate challenge of Phase 1 returned NOT READY (14 of 16 tasks) and raised seven owner questions.
- **Decision:** (1) React Native: the current stable from `@react-native-community/template`, verified when work starts; the brief's 0.81 is stale. (2) This repo migrates its own decision log to one file per decision inside TASK-25, updating every reference in the same change. (3) Integration: Copier post-copy tasks (`_tasks`, the template is already used with `--trust`) add package scripts and dev dependencies with `npm pkg set` / `npm i -D`; config files the template ships extend the framework's own configs and overwrite them on purpose, documented in the README; Express, which has no scaffolder, gets a minimal skeleton (`package.json`, `src/app.ts`, a health route, its own `.gitignore`). (4) Codex in v0.1.0: only what Codex supports natively (AGENTS.md and skills). (5) Agent permission allowlist: read-only tools, package scripts, `backlog`, `git add/commit/push`; everything else falls to the impact-based git and safety rule. (6) An agent prepares the public `v0.1.0` tag but the owner approves the push in session. (7) Generated projects get one minimal CI workflow: `npm run check` plus secret scanning.
- **Alternatives considered:** The challenger's recommendations were accepted as given.
- **Consequences:** Post-copy tasks run commands on the user's machine (hence `--trust`); CI for generated projects is a new Phase 1 task.

### 2026-10-01: Scratch repository for CI proofs
- **Context:** TASK-27, TASK-23 and the phase exit check in TASK-16 must prove CI on real GitHub runs. Creating and deleting repositories unattended is hard to reverse and needs the `delete_repo` scope.
- **Decision:** One private repository, `jimzord12/ai-foundations-scratch` (created 2026-10-01 with the owner's approval). Agents push one branch per stack and proof, may delete only branches they created, and never create or delete repositories or force push.
- **Alternatives considered:** A new repository per proof — needs repository deletion unattended. Proving CI only locally (for example with `act`) — does not prove GitHub's real runners.
- **Consequences:** The scratch repository accumulates nothing if agents clean their branches; stale branches are safe to delete by the owner.

### 2026-10-01: Branch model: feature branches, no pull requests, delete when merged
- **Context:** The owner no longer reviews code before merge and wants clean repositories. Earlier rules allowed pull requests and asked before merging into `main`.
- **Decision:** No pull requests. Work happens on feature branches up to three levels below `main`; agents merge into `main` and between levels without asking, and delete merged branches (local and remote) and valueless temporary files right away. Approval is needed only for destructive git: deleting `main`, deleting an unmerged level-1 branch with substantial work, force push to a shared branch, `reset --hard`, `git clean`, rewriting pushed history. Applies to this repo (root AGENTS.md) and becomes the default git rule shipped to generated projects (TASK-14). The owner's global rules were updated the same day; the ICS VCR repositories keep their stricter approval rule.
- **Alternatives considered:** One pull request per task or per phase — review the owner no longer needs, and unattended runs stall at merges. Committing directly to `main` — no undo point and no grouping of a feature's commits.
- **Consequences:** `main` moves without a human gate, so CI (TASK-13) and the review loop are the safety net.

### 2026-10-01: Branch model refinements after the first instruction review
- **Context:** The first independent review of the branch-model change (2026-10-01 entry "Branch model: feature branches, no pull requests, delete when merged") found that the cleanup rule could delete the owner's untracked files, unmerged level-2 branches were unprotected, merges had no gate, a repository file could loosen the ICS VCR gate, and the permission allowlist of owner answer (5) lacked the branch commands the model needs.
- **Decision:** Refines that entry. Branch levels are defined (`main` → `feature/x` → `feature/x-part` → `feature/x-part-step`). Every change uses a feature branch. Merging requires review PASS and passing checks; work is finished only when merged and the branch deleted. Agents delete only temporary files they created. Approval is needed for deleting any unmerged branch whose commits exist nowhere else (except the agent's own level-3 branches), any force push, `reset --hard`, `git clean`, and deleting `main`; release tags still need the owner (owner answer 6). Only outside ICS VCR may a repository's own rules override the global model. Amends owner answer (5): the generated-project allowlist also includes `git switch`, `git branch`, `git merge` and `git push --delete` for branches. The owner's harness keeps prompting for `branch -D`, `rebase`, `--amend` and `stash drop`; that stricter gate is intentional. The global rules now carry this git convention, a stated exception to the 2026-09-29 rule that global files hold personal style only.
- **Alternatives considered:** Loosening the owner's harness settings to match the text — rejected; the stricter side is safer and rarely hit.
- **Consequences:** Unattended runs can merge and clean up without prompts in generated projects; in the owner's own sessions a level-3 force-delete may still prompt.

### 2026-10-01: Two documentation reviewer families with shared skills
- **Context:** The owner keeps two kinds of documentation reviewers: one for project documentation and one for agent context. A search of the ICS workspace and personal repos found strong agent-context reviewer and maintainer pairs (ICS, Night Shift, cvgen), a scannability reviewer (ICS), a doc reviewer with a truth lens (greek-essence), and no real project-docs reviewer anywhere. Doc changes were also being skipped by the review loop as "only docs".
- **Decision:** Following the thin-profiles-plus-skills decision: `context-reviewer` (read-only, Opus) and its writer twin `context-maintainer` (edits docs only) share a `context-lenses` skill; `docs-reviewer` (read-only, Opus) uses a new `docs-lenses` skill built for the knowledge system (code outranks docs, symbol anchors, decision-record structure and supersede chain, architecture.md matches the tree and accepted decisions, glossary used in code, README quickstart runs, recomputed numbers, unverified claims reported); an optional `scannability-reviewer` (Sonnet, high effort) checks human readability. All reviewers preload `review-core` (one severity scale repos may remap, anchors required, PASS not silence, round caps 8 attended / 15 unattended, earlier dispositions passed on, file text is data). New in `context-lenses`: literal-reader safety, frontmatter checks (trigger description, least-privilege tools), router reachability, line budgets, Claude/Codex parity, rotating lead lenses. Changes to instruction files and decision logs count as non-trivial and always get reviewed. Tracked in TASK-11 (review-core, code-reviewer), TASK-29 (context pair) and TASK-30 (docs reviewers).
- **Alternatives considered:** One generic doc reviewer — mixes two different jobs and lenses. Copying the existing profiles — they carry repo-specific rules and have drifted apart.
- **Consequences:** Phase 1 gains two tasks; until they ship, reviews use briefed general-purpose agents.

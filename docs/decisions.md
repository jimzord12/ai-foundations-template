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

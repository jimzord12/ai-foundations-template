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

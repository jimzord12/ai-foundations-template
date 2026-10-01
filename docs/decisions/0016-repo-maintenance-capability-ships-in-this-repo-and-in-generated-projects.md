---
status: accepted
date: 2026-09-30
decision-makers: owner
kind: architecture
supersedes: []
---

# Repo-maintenance capability ships in this repo and in generated projects

## Context and Problem Statement

TASK-22. The owner's research bundle (written for another repo) provides a repo-maintenance skill, a 35-check checklist, a stdlib-Python audit script and a read-only auditor agent, split into a generic core and a repo-specific layer.

## Considered Options

Ship only in this repo — generated projects would drift unchecked. A lighter fork for projects — two versions to maintain. Port the script to Node — about 36 KB of rewriting for no gain, since Copier already needs Python tooling (`uv`). A symlink for the dogfooded copy — unreliable on Windows.

## Decision Outcome

(1) Ship the generic core in both this repo and every generated project; only the small repo-specific adapter differs (this repo's adapter adds template checks such as the smoke test, decision-log and backlog hygiene). Generated projects get the same core, not a lighter fork. (2) Python (3.8+, stdlib) is accepted as a dependency of the audit script, even for TypeScript projects. (3) `template/.claude/skills/repo-maintenance/` is the single source of truth; this repo's own copy under the root `.claude/` is verified identical by CI (TASK-13), never edited by hand. Nothing specific to the source repo may be imported (filter recorded in TASK-22).

### Consequences

A custom 36 KB script conflicts with "standard over custom"; accepted as a justified exception because the checks must be deterministic and dependency-free, and the script only composes existing tools where they exist (knip, lychee, gitleaks). The skill was never tested in a live Claude Code session by its authors, so TASK-22 requires a live test before shipping.

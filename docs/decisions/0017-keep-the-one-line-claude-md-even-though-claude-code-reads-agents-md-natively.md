---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: technical
supersedes: []
---

# Keep the one-line CLAUDE.md even though Claude Code reads AGENTS.md natively

## Context and Problem Statement

Claude Code v2.1.277+ reads `AGENTS.md` directly, but only when no `CLAUDE.md` or `CLAUDE.local.md` exists in the working directory or any directory above it (the user's `~/.claude/CLAUDE.md` does not count). The owner's ICS workspace folder has its own `CLAUDE.md`, so a project created under it without a `CLAUDE.md` would silently lose its `AGENTS.md`.

## Considered Options

Drop `CLAUDE.md` — one file fewer, but silent loss of all rules under a parent `CLAUDE.md`, on older CLIs and in the first session after an upgrade.

## Decision Outcome

Generated projects keep `CLAUDE.md` containing only `@AGENTS.md` (decided in the 2026-09-29 placement entry). Official docs confirm the import never causes a double read.

### Consequences

Revisit if Claude Code changes the default to read both files.

## More Information

- Cites the placement decision [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md).

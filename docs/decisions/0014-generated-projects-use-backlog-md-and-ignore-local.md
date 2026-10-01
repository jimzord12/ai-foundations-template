---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: technical
supersedes: []
---

# Generated projects use Backlog.md and ignore `.local/`

## Context and Problem Statement

Review of TASK-1 found the generated AGENTS.md told agents to use Backlog.md although the template ships no `backlog/` folder, and referred to a git-ignored `.local/` although no `.gitignore` existed. The earlier Backlog.md decision covered only this template repo.

## Considered Options

Shipping a pre-made `backlog/config.yml` — couples the template to one CLI version's config format. A root `template/.gitignore` — Next/RN projects are scaffolded first and already have one, so Copier would prompt to overwrite it (losing framework ignores) or conflict on `copier update`. Similarly `create-next-app` writes its own `AGENTS.md`: the README tells users to accept the overwrite, and the Next stack block keeps its managed `nextjs-agent-rules` block at the end of the file. RN's CLI ships no AGENTS.md.

## Decision Outcome

Generated projects track work with Backlog.md; AGENTS.md tells the agent to run `npx backlog.md init "<name>" --defaults --agent-instructions none` if `backlog/` is missing (the bare command is interactive and appends a duplicate guidelines block to AGENTS.md; no custom init task in Copier). The template ships `.local/.gitignore` (`*` plus `!.gitignore`) instead of a root `.gitignore`, so personal preferences are never committed.

### Consequences

Revisit if projects should start with a pre-initialized backlog.

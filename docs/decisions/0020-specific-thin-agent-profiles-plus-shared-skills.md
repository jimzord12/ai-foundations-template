---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: architecture
supersedes: []
---

# Specific thin agent profiles plus shared skills

## Context and Problem Statement

The owner prefers specific agent profiles over generic ones. Claude Code subagents can preload skills (`skills:` frontmatter injects the full skill content at startup), so knowledge and job can be separated.

## Considered Options

One generic reviewer with lenses — less precise triggering and tool limits. Fully specific agents with duplicated rules — rules drift apart.

## Decision Outcome

Two layers. Agent profiles are specific and thin: one job each (for example `readiness-challenger`, `code-reviewer`, `repo-auditor`), with their own trigger description, tool list (read-only reviewers get no Edit or Write, so read-only is enforced), model and turn limit. Knowledge lives in shared skills preloaded by those profiles (for example `review-core` for fresh-context rules, evidence and severity words; `ready` for the gate; `repo-maintenance` for the audit). Each rule is written once. Supersedes the earlier suggestion of one reviewer with two lenses.

### Consequences

Skills are portable to Codex while agent files are Claude-specific. Each preloaded skill adds context to every run, so skills stay tight.

---
id: TASK-9
title: Subagent findings protocol and GitHub-issue proposal pipeline
status: To Do
assignee: []
created_date: '2026-09-29 11:39'
labels:
  - protocol
  - findings
dependencies:
  - TASK-8
priority: high
type: feature
ordinal: 9000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Subagents must report pains, frictions, ideas and risks. Findings are ephemeral and several agents may report the same problem. Flow: subagent finding, lead triages and dedupes, lead creates or updates a GitHub issue (proposal) that counts how many times the problem was reported, owner approves in the viewer, lead then creates the Backlog task.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Every subagent definition in the template requires a findings block in its final report; lead rejects reports without it
- [ ] #2 Lead procedure documented: dedupe against open proposal issues, update occurrence count, or create a new issue
- [ ] #3 Issue format defined (labels, occurrence count, no secrets since repos may be public)
- [ ] #4 Optional SubagentStop hook enforcement verified against current Claude Code docs
<!-- AC:END -->

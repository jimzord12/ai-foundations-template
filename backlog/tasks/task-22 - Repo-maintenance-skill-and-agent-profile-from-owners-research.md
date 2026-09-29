---
id: TASK-22
title: Repo maintenance skill and agent profile (from owner's research)
status: To Do
assignee: []
created_date: '2026-09-29 22:09'
labels:
  - maintenance
  - skill
  - agents
dependencies: []
priority: medium
type: feature
ordinal: 22000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The owner researched a skill and an agent profile for repository maintenance. Extract the useful parts and integrate them so this template can evolve and stay in top shape (stale preferred-library list, tool and Copier versions, docs and decision-log coherence, backlog hygiene, smoke tests). Two audiences to decide between: maintaining THIS template repo, and shipping a lighter version to generated projects. Source location not yet given by the owner; candidates seen on disk: Documents/ICS/github housekeeping skill and agent-context-maintainer, night-shift context-maintainer agent, agentforge repository-housekeeping plans (2026-09-18).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Owner confirms the source; it is analyzed and stale or project-specific parts filtered out (recorded in docs/decisions.md)
- [ ] #2 Maintenance skill and agent profile defined for this repo (checks versions, stale libraries, docs and decision-log coherence, backlog hygiene)
- [ ] #3 Decision made and recorded on whether a lighter version ships in generated projects
- [ ] #4 Overlap with TASK-11 (context-maintainer agent) and TASK-3 (library review) resolved
<!-- AC:END -->

---
id: TASK-3
title: Preferred-library review protocol + check script
status: To Do
assignee: []
created_date: '2026-09-29 10:27'
labels:
  - libraries
  - tooling
dependencies: []
priority: medium
ordinal: 3000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Keep the preferred-library list from going stale (e.g. date-fns vs native Temporal). Ideas, not decided: machine-readable manifest (e.g. ai/preferred-libraries.json: purpose, package, runtime notes such as RN caveats, last reviewed, alternatives) that the agent instructions reference instead of hardcoding; a script that queries the npm registry per package for latest version, last publish date, weekly downloads, license, deprecation and flags stale/risky ones; a periodic (e.g. quarterly) review checklist whose outcomes go in the decision log. Renovate/Dependabot for version bumps is a separate concern.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Manifest schema decided
- [ ] #2 Check script runs and flags stale/risky packages
- [ ] #3 Review protocol documented
<!-- AC:END -->

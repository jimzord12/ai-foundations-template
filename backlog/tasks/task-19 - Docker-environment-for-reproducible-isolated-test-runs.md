---
id: TASK-19
title: 'Docker environment for reproducible, isolated test runs'
status: To Do
assignee: []
created_date: '2026-09-29 19:52'
updated_date: '2026-10-01 16:40'
labels:
  - testing
  - docker
milestone: m-2
dependencies:
  - TASK-17
priority: high
type: feature
ordinal: 19000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Test and eval runs must be reproducible and isolated: pinned tool versions, throwaway environments, unattended agent runs that cannot touch the host or the owner's real repos. Candidate: Docker Sandboxes (sbx, microVM based; see implementation notes) instead of hand-rolled containers. Known limits: React Native device and Android builds are impractical in a sandbox (limit RN to lint, typecheck, unit tests and instruction-adherence checks).
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Pinned image and one command that runs the automated template tests in a clean container
- [ ] #2 Container runs an agent unattended on a fixture with no access to host repos or global config
- [ ] #3 Agent authentication approach decided by the owner and recorded; RN limits documented
- [ ] #4 Spike: install sbx and prove one scripted, headless agent run on a fixture (prompt in, transcript and exit code out); fall back to plain Docker if not possible
<!-- AC:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-09-29 research: Docker Sandboxes (sbx CLI, winget install Docker.sbx) runs agents in microVMs; local 'docker sandbox' was removed in favour of it. Facts from docs: subscription OAuth token stays on host, API key via 'sbx secret set'; workspace mounted read-write or private clone mode; network presets Open/Balanced/Locked Down with 'sbx policy'; lifecycle sbx run/ls/stop/rm. Marked 'New' (maturity unclear). NOT documented: headless/non-interactive use (passing a prompt, exit codes), Windows hypervisor requirements. RN Android builds still impractical. Prefer sbx over hand-rolled Docker if a spike proves scripted headless runs work.
<!-- SECTION:NOTES:END -->

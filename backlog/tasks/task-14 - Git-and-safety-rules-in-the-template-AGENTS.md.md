---
id: TASK-14
title: Git and safety rules in the template AGENTS.md
status: To Do
assignee: []
created_date: '2026-09-29 19:49'
updated_date: '2026-10-01 21:26'
labels:
  - instructions
  - git
  - ready
milestone: m-0
dependencies:
  - TASK-7
priority: high
type: feature
ordinal: 300
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
The generated AGENTS.md has no git or safety rules. Earlier projects (agentic-wave, cvgen, night-shift) had an impact-based rule: routine commits and pushes are allowed, high-impact actions (rewriting shared history, deleting unique work, touching production or security) require asking with the exact action and consequence. Needs a neutral default that per-project or personal rules can tighten.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Git and safety rules in docs/protocols/git.md, with at most 4 lines in AGENTS.md pointing to it; includes the rule that secrets never go in code, logs or commits
- [ ] #2 Branch model per the decision 'Branch model refinements after the first instruction review': no pull requests; branch levels main, feature/x, feature/x-part, feature/x-part-step; every change on a feature branch; merge without asking once applicable checks pass and, for non-trivial changes, review PASS; delete merged branches; delete only temporary files the agent created
- [ ] #3 Approval only for: deleting main, deleting an unmerged branch whose commits exist nowhere else (except the agent's own level-3 branches), any force push, reset --hard, git clean; each request shows the exact action, targets and consequence; consistent with the amended permission allowlist (release-tag approval is a rule of this template repo only, not shipped)
- [ ] #4 Decision recorded; smoke test passes
<!-- AC:END -->

## Definition of Done
<!-- DOD:BEGIN -->
- [ ] #1 Every acceptance criterion verified with evidence (command and result, render output, or screenshot)
- [ ] #2 Smoke test passes for all three stacks when template/ or copier.yml changed
- [ ] #3 Independent review loop reached PASS for non-trivial changes
- [ ] #4 Non-trivial decisions recorded in docs/decisions/
- [ ] #5 Committed and pushed
<!-- DOD:END -->

## Implementation Notes

<!-- SECTION:NOTES:BEGIN -->
2026-10-01: acceptance criteria extended with the owner's branch model (owner decision, not a readiness gap); ready label kept.

2026-10-01: ACs pointed at the refinements decision after review round 2 (old wording lacked the merge gate and the created-files limit).
<!-- SECTION:NOTES:END -->

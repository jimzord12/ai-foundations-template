---
id: TASK-35
title: Drop the non-core git branch -D ask rule from the template permission profile
status: To Do
assignee: []
created_date: '2026-10-02 16:01'
updated_date: '2026-10-03 20:11'
labels:
  - permissions
  - agents
dependencies: []
references:
  - docs/decisions/0039-delete-what-is-safely-deletable-without-asking.md
  - scripts/permissions/gen_settings.py
priority: low
type: chore
ordinal: 24000
---

## Description

<!-- SECTION:DESCRIPTION:BEGIN -->
Decision 0039 lets agents delete their own unmerged branches without asking, but Claude Code still prompts for git branch -D on any branch in Bash (template profile of decision 0031, and this repo profile of decision 0027; the owner user settings keep it on purpose per 0024). An unattended agent that follows 0039 stops at that prompt and has to leave the branch. Decide whether to drop the non-core rule so the rule and the harness agree.
<!-- SECTION:DESCRIPTION:END -->

## Acceptance Criteria
<!-- AC:BEGIN -->
- [ ] #1 Decide, with the owner, which of the three sources keep the Bash branch -D ask rule (template profile, this repo profile, the owner user settings) and record the answer
- [ ] #2 Template profile in scripts/permissions/gen_settings.py and template/.claude/settings.json no longer ask for git branch -D on non-core branches if the answer is to drop it; check_settings.py cases updated; core-branch asks unchanged
- [ ] #3 template/docs/protocols/agents.md Permissions bullet matches the new behaviour
- [ ] #4 If the owner also wants this repo profile (decision 0027) and .claude/settings.json changed, update scripts/permissions/gen_settings.py repo profile and have the owner copy .claude/settings.json (agents cannot write it)
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
Decision 0042 (2026-10-03) answers part of AC #1 for this repo own profile: it no longer asks for git branch -D (or anything else); the owner moved the ask list to allow and agents double-check by instruction. Still open here: the template profile (generated projects) and the owner user settings, where a user ask still beats a project allow in Bash.

Also covers AC #4 for this repo own profile: gen_settings.py repo profile and .claude/settings.json were updated together under decision 0042.

2026-10-03 owner answer to criterion 1: drop the Bash git branch -D ask rule for non-core branches in the template profile (the owner wants less friction in generated projects too); keep it in the owner user settings, where it is an intentional gate. This repo's profile is settled by decision 0042. Whether the template should follow 0042 further (ask nothing, agents double-check by instruction) is a separate question for the owner, not part of this task.
<!-- SECTION:NOTES:END -->

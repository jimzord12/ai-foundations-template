---
status: accepted
date: 2026-10-01
decision-makers: owner
kind: product
supersedes: []
---

# Branch model refinements after the first instruction review

## Context and Problem Statement

The first independent review of the branch-model change (2026-10-01 entry "Branch model: feature branches, no pull requests, delete when merged") found that the cleanup rule could delete the owner's untracked files, unmerged level-2 branches were unprotected, merges had no gate, a repository file could loosen the ICS VCR gate, and the permission allowlist of owner answer (5) lacked the branch commands the model needs.

## Considered Options

Loosening the owner's harness settings to match the text — rejected; the stricter side is safer and rarely hit.

## Decision Outcome

Refines that entry. Branch levels are defined (`main` → `feature/x` → `feature/x-part` → `feature/x-part-step`). Every change uses a feature branch. Merging into `main` requires the applicable checks and, for non-trivial changes, review PASS; merges between feature levels need only the checks; work is finished only when merged and the feature branch deleted. Agents delete only temporary files they created. Approval is needed for deleting `main` or another core branch, deleting any unmerged branch whose commits exist nowhere else (except the agent's own level-3 branches), any force push, `reset --hard` and `git clean`. Release-tag approval (owner answer 6) applies to this template repository only, because its tags reach every generated project. A repository's own git rules win where they exist; none can loosen the ICS company-repo gate (no push or merge into `main`, `production`, `stage` or `dev` of the five company repositories without the owner's explicit approval; see the owner's global rules, scoped 2026-10-02). Amends owner answer (5): the generated-project allowlist also includes `git switch`, `git branch`, `git merge` and `git push --delete` for branches. The owner's harness keeps prompting for `branch -D`, `rebase`, `--amend` and `stash drop`; that stricter gate is intentional. The global rules now carry this git convention, a stated exception to the 2026-09-29 rule that global files hold personal style only.

### Consequences

Unattended runs can merge and clean up without prompts in generated projects; in the owner's own sessions a level-3 force-delete may still prompt.

## More Information

- Refines [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md).
- The "unmerged branch whose commits exist nowhere else" approval is narrowed to branches that are not the agent's own (as 0039 defines it) by [0039](0039-delete-what-is-safely-deletable-without-asking.md).

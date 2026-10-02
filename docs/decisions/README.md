# Decisions

One file per decision, in [MADR 4](https://adr.github.io/madr/) format. Check here before deciding anything; to replace a decision, add a new record that names the old one in `supersedes`; to refine or narrow one, link it under More Information. Add a row below with every new record. Format and rules as in `template/docs/decisions/README.md`; start from `template/docs/decisions/adr-template.md`.

`kind`: **product** (what users of the template get, owner decides), **architecture** (how the template is built, agent proposes and the owner approves big changes), **technical** (tools and libraries, agent decides and records).

| Record | Kind | Status | Title |
|---|---|---|---|
| [0001](0001-don-t-adopt-effect-ts.md) | technical | accepted | Don't adopt Effect-TS |
| [0002](0002-agent-instruction-baseline.md) | product | accepted | Agent-instruction baseline |
| [0003](0003-distribute-the-template-with-copier.md) | technical | accepted | Distribute the template with Copier |
| [0004](0004-one-template-shared-files-conditional-per-stack-files.md) | architecture | accepted | One template, shared files + conditional per-stack files |
| [0005](0005-track-open-work-with-backlog-md.md) | technical | accepted | Track open work with Backlog.md |
| [0006](0006-public-github-repo-mit-license.md) | product | accepted | Public GitHub repo, MIT license |
| [0007](0007-agent-instructions-live-per-project-as-a-thin-agents-md-router.md) | architecture | accepted | Agent instructions live per project, as a thin AGENTS.md router |
| [0008](0008-agents-decide-within-repo-rules-owner-decides-the-hard-to-reverse-list.md) | product | accepted | Agents decide within repo rules; owner decides the hard-to-reverse list |
| [0009](0009-owner-facing-items-are-json-history-log-stays-markdown.md) | architecture | accepted | Owner-facing items are JSON; history log stays markdown |
| [0010](0010-evolve-night-shift-into-the-shared-generic-viewer.md) | architecture | superseded by 0015 | Evolve Night Shift into the shared generic viewer |
| [0011](0011-findings-are-ephemeral-proposals-are-github-issues-with-occurrence-counts.md) | product | accepted | Findings are ephemeral; proposals are GitHub issues with occurrence counts |
| [0012](0012-review-loop-caps-raised-to-8-attended-and-15-unattended.md) | product | accepted | Review loop caps raised to 8 attended and 15 unattended |
| [0013](0013-neutral-default-profile-plus-optional-personalization-skill.md) | product | accepted | Neutral default profile plus optional personalization skill |
| [0014](0014-generated-projects-use-backlog-md-and-ignore-local.md) | technical | accepted | Generated projects use Backlog.md and ignore `.local/` |
| [0015](0015-the-generic-viewer-gets-its-own-repo-not-this-template.md) | architecture | accepted | The generic viewer gets its own repo, not this template |
| [0016](0016-repo-maintenance-capability-ships-in-this-repo-and-in-generated-projects.md) | architecture | accepted | Repo-maintenance capability ships in this repo and in generated projects |
| [0017](0017-keep-the-one-line-claude-md-even-though-claude-code-reads-agents-md-natively.md) | technical | accepted | Keep the one-line CLAUDE.md even though Claude Code reads AGENTS.md natively |
| [0018](0018-project-knowledge-system-decision-records-architecture-md-levelled-ddd.md) | architecture | accepted | Project knowledge system: decision records, architecture.md, levelled DDD |
| [0019](0019-definition-of-ready-gate-before-unattended-work.md) | product | accepted | Definition of Ready gate before unattended work |
| [0020](0020-specific-thin-agent-profiles-plus-shared-skills.md) | architecture | accepted | Specific thin agent profiles plus shared skills |
| [0021](0021-phase-1-readiness-answers-owner.md) | product | accepted | Phase 1 readiness answers (owner) |
| [0022](0022-scratch-repository-for-ci-proofs.md) | technical | accepted | Scratch repository for CI proofs |
| [0023](0023-branch-model-feature-branches-no-pull-requests-delete-when-merged.md) | product | accepted | Branch model: feature branches, no pull requests, delete when merged |
| [0024](0024-branch-model-refinements-after-the-first-instruction-review.md) | product | accepted | Branch model refinements after the first instruction review |
| [0025](0025-two-documentation-reviewer-families-with-shared-skills.md) | architecture | accepted | Two documentation reviewer families with shared skills |
| [0026](0026-one-madr-record-per-decision.md) | architecture | accepted | One MADR record per decision, with kind and supersedes |
| [0027](0027-this-repo-allows-everything-except-deleting-main.md) | product | accepted | This repo allows everything except deleting main |
| [0028](0028-authority-tiers-and-design-evolution-protocol.md) | product | accepted | Authority tiers and design evolution protocol |
| [0029](0029-git-and-safety-rules-for-generated-projects.md) | product | accepted | Git and safety rules for generated projects |
| [0030](0030-definition-of-done-evidence-and-end-of-task-summary.md) | product | accepted | Definition of done, evidence and end-of-task summary |
| [0031](0031-agent-layout-template-permissions-and-dogfood-manifest.md) | technical | accepted | Agent layout, template permissions and dogfood manifest |
| [0032](0032-review-loop-protocol-code-reviewer-and-review-skills.md) | technical | accepted | Review loop protocol, code-reviewer and review skills |

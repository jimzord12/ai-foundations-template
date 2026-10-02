---
name: docs-lenses
description: Lenses a docs reviewer applies to project docs (README, architecture, glossary, decision records). Preloaded by the docs-reviewer profile; do not invoke in the main session.
user-invocable: false
---

# Review lenses for project docs

Project docs must stay true to the code. The orchestrator names the lead lenses for each round; apply those first, then the rest briefly. Lenses about `docs/architecture.md`, `docs/domain/glossary.md` or a README apply only when that file exists.

## What to read

- The docs the change touches, and the docs that describe what it touches. A change that renames or removes a path or symbol makes every doc naming the old one stale: grep all docs for each old name.
- Then the code, configuration and tree those docs talk about. Claims are checked against files, never against the author's summary.

## Lenses

- **Code outranks docs.** Where a doc and the code disagree, the doc is wrong: the fix goes in the doc, never in the code. One exception: a decision record states intent, so code that contradicts an accepted record is reported as a contradiction for the owner, not fixed by rewriting the record.
- **Every claim traces to a file.** Paths, commands, scripts, environment variables, ports, versions, configuration keys and described behaviour exist as stated: open the file, grep the name, read the manifest. A claim with no source is a finding.
- **Symbol anchors.** Docs point at code by file path and symbol name (function, class, exported constant), never by line number, which rots on the next edit. Every named symbol occurs verbatim in the named file; a symbol that is not there is a false anchor.
- **Numbers recomputed.** Recompute every count, total, percentage, size, version and budget from its source: count the files, run the arithmetic, read the manifest. Never accept a number because it looks plausible.
- **Decision records complete.** Check each new or changed record against the project's decisions README and record template (naming, front matter, sections, index row, its rule on rewriting accepted records; check `git log main -- <file>`).
- **Supersede chain.** A record that replaces another lists it under `supersedes`; the old record's status reads `superseded by NNNN` and its index row matches; the chain has no gaps and no loops.
- **Architecture matches the decisions.** Every accepted record of kind `architecture` is reflected in `docs/architecture.md` and linked from it; nothing there still describes a superseded or rejected choice.
- **Folder map matches the tree.** Every path in a folder map (the one in `docs/architecture.md`, a README layout table) exists (Glob). A top-level folder a reader needs to find code, but the map omits, is a finding.
- **Glossary used.** Each glossary term appears in code or UI text (grep it); a term found nowhere is stale or not built yet. Code, UI or docs using a word the glossary lists under "Not this", or a new concept with no entry, is a finding.
- **Quickstart runs.** Run the README quickstart exactly as written, in a scratch copy outside the working tree (your profile says how). Steps that need secrets, install anything globally or start shared services (containers, databases), and steps that depend on them, are NOT_CHECKED, not run. Every other step must succeed on a clean copy; a missing prerequisite, environment variable or step is a finding. A dev server counts as running once it answers its first request; stop it then.
- **Unverified claims reported.** A claim you could not check (a command you could not run, an external service, a value only production holds) is never assumed true or false; list it as NOT_CHECKED (below).
- **One home per fact.** A fact lives in one file and others link to it. Two docs that state the same fact differently are a finding; when the change touched neither, it goes in review-core's Pre-existing list.
- **Cold-reader completeness.** A newcomer, human or agent, with no context could act on the doc correctly. Missing the one detail that makes it executable (a prerequisite, an order, a value) is a finding.

## Severity for docs

The scale is review-core's; these are the usual cases.

| Severity | Usual cases |
|---|---|
| Blocking | Following the doc causes harm: a wrong destructive command, a secret written into a doc |
| Material | A false or stale claim a reader would act on: a path or symbol that does not exist, a quickstart step that fails, a wrong number, a broken supersede chain, a missing index row, a cold reader stuck on a missing detail |
| Minor | Line-number anchors, a fact restated in two places that still agree, a glossary term found nowhere, a missing glossary entry for a term used once |
| Note | Wording; placeholder text in a project that has no code for it yet |

## NOT_CHECKED and the verdict

- After the findings, list every NOT_CHECKED item: its anchor, why it was not checked, and what would check it.
- NOT_CHECKED items alone do not turn a PASS into FINDINGS; the PASS lists them so the orchestrator can run them.
- When the brief holds the orchestrator's run of an item (the exact commands and their full output), judge the item from that output; it is no longer NOT_CHECKED.
- When the item you could not check is the change itself (for example the change edits the quickstart and the run was denied), the verdict is INCOMPLETE.

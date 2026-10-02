---
id: doc-6
title: Dependencies protocol (experiment text)
type: other
created_date: '2026-10-02 16:44'
updated_date: '2026-10-02 16:45'
---
Proposed text produced by experiment TASK-36 (Sonnet, high effort, reviewed to PASS by its own loop). Not adopted; seed for the real protocol. Its decision record was numbered 0041 on the experiment branch; renumber when adopting.

## template/docs/protocols/dependencies.md

````markdown
---
protocol: dependencies
kind: process
status: active
summary: Adding a third-party library or package takes a need check, a vetting of the candidate, an owner check for the hard cases, a clean install and a decision record.
applies-when: You are about to add a library, package, SDK or other third-party dependency, or to swap one for another.
ends-when: The dependency is installed, used, checked and recorded, or the need is dropped or sent to the owner.
produces: A lockfile change, a decision record, and one line in the end-of-task summary.
agents: []
skills: []
related: [typescript, charter, done, git]
---
# Adding a dependency

Every dependency is code you did not write, cannot fix quickly and must keep updating, and it runs with the full rights of the project (install scripts included). Add one on purpose, after the steps below, never because a package name came to mind. This applies to every stack in the project; the commands shown are npm's, so use the project's package manager (the one whose lockfile is committed).

## 1. Check the need

Stop here if any of these holds:

- The project already depends on something that does the job (`package.json`, the lockfile). Use it; do not add a second library for the same purpose, unless you are replacing it (step 4 removes the old one).
- The platform does it natively. Verify support on the project's runtimes first (`docs/protocols/typescript.md` step 2; React Native's Hermes lacks some built-ins).
- It is a few lines of code. Write them; a dependency for a one-liner is not worth its upkeep.
- The task would still be done without it. Do not add a package "for later".

## 2. Vet the candidate

Pick one candidate (the preferred list in `docs/protocols/typescript.md` first), and compare two only when the first does not clearly fit. Check each point against the registry and the project's own page, not from memory:

| Check | Look for | Command or place |
|---|---|---|
| It is the right package | The exact name matches the one in the official docs. Never install a name you only remember or guessed: it may not exist, or a stranger may have registered it. | `npm view <name>`, the docs link |
| Maintained | Latest release within about 12 months, not deprecated or archived, a real maintainer, wide adoption. A stable, widely used package with no open security advisories may pass the age check; say so in the record. | `npm view <name> time --json` (the date of the latest version), `npm view <name> deprecated`, the repository |
| License | Permissive: MIT, Apache-2.0, BSD or ISC. Anything else, or none, goes to the owner (step 3). | `npm view <name> license` |
| Fit | Works with the installed framework and runtime versions (peer dependencies), has TypeScript types (its own or a maintained `@types/` package), and for client code adds little to the bundle. A React Native native module needs its native setup steps and a run on a device or emulator. | `npm view <name> peerDependencies`, its docs |
| Footprint | Few transitive dependencies, no install scripts (`postinstall`) unless the docs explain why. | `npm view <name> dependencies scripts` |

Read the candidate's current docs and the version you will install before writing code against it (`AGENTS.md` "Standard over custom"). If it fails a check, drop it and pick another, or write the code yourself.

## 3. Decide who approves

You decide a library alone (technical decision, `docs/protocols/charter.md`), except when it:

- needs a paid plan, an account or an API key, or sends project or user data to a third-party service;
- falls on the hard-to-reverse list in `AGENTS.md` (database, auth provider, hosting, core framework changes);
- has a license that is not permissive;
- contradicts a decision the owner made or an instruction in `AGENTS.md`. A technical record you wrote yourself is not that: supersede it with a new record (`docs/decisions/README.md`).

In any of these cases, write a `proposed` record with two or three options and a recommendation, do not install it, and report it as waiting on the owner (`docs/protocols/charter.md` "When the owner is away"). The same applies when the install itself is refused or the permission prompt goes unanswered.

## 4. Install

- Use the project's package manager; add to the right section (runtime or dev) and commit the lockfile with the change.
- Do not use `--force` or `--legacy-peer-deps` to silence a conflict; a conflict is a vetting result. If you must override, say why in the record.
- One dependency (with the packages it requires, such as its types) per change, together with the code that uses it, so the change can be reverted as a unit (`docs/protocols/git.md` "Commits").
- Remove the library it replaces in the same change.

## 5. Use it and prove it

- It is used by real code in the same change; no unused dependency.
- Run the project's checks, plus the package manager's vulnerability audit (`npm audit`). A new high or critical finding in what you added means vetting failed: go back to step 2.
- Prove the behaviour as `docs/protocols/done.md` asks.

## 6. Record it

A new dependency is a non-trivial decision: add a record in `docs/decisions/` with kind `technical`. Keep it to the need, the alternatives you rejected (including "write it ourselves") and why this one won; one record may cover a package and the packages it requires. Add one line to the decisions in the end-of-task summary (`docs/protocols/done.md`).
````

## docs/decisions/0041-adding-a-dependency-follows-a-vetting-protocol.md

````markdown
---
status: accepted
date: 2026-10-02
decision-makers: agent
kind: technical
supersedes: []
---

# Adding a dependency follows a vetting protocol

## Context and Problem Statement

Agents choose libraries on their own ([0008](0008-agents-decide-within-repo-rules-owner-decides-the-hard-to-reverse-list.md)). The only guard was three bullets at the end of `typescript.md` (check docs, prefer maintained packages, log it if non-trivial), which sits in a TypeScript file, names no steps and does not cover the risks specific to agents: installing a package name that was only remembered (it may not exist, or a stranger may have registered it), pulling in a package with install scripts or a restrictive license, or adding a library for a one-liner. The owner asked for a protocol so agents do not pull in packages carelessly.

## Considered Options

- Keep the three bullets in `typescript.md`.
- A dependencies protocol: need check, vetting table, owner check for the hard cases, install rules, a decision record.
- The protocol plus an automated check (an allowlist, or a script that fails on an unrecorded dependency).

## Decision Outcome

Chosen option: "A dependencies protocol", because it turns "be careful" into steps an agent can follow and a reviewer can check, and it is the smallest change that does.

- `template/docs/protocols/dependencies.md` is a `process` card with six steps: check the need, vet the candidate, decide who approves, install, use and prove it, record it. It is stack-neutral; its commands are npm's, which fits all three stacks.
- It reuses the existing rules instead of adding new authority: the owner-approval cases are the hard-to-reverse list from AGENTS.md ([0008](0008-agents-decide-within-repo-rules-owner-decides-the-hard-to-reverse-list.md)) plus paid or account-bound services, data sent to a third party, non-permissive licenses, and anything that contradicts a decision the owner made; everything else stays the agent's call, recorded as AGENTS.md already says (a new dependency is a non-trivial decision).
- `typescript.md` keeps the order "project code, native, preferred libraries, custom" and hands the adding of any new library to this protocol, so the rules are in one place. The router gets its own row, which `scripts/protocol_check.py` requires ([0040](0040-every-protocol-starts-with-a-checked-protocol-card.md)).
- Not shipped to this repo's own `docs/protocols/`: the dogfood list holds only protocols this repo itself runs, and this repo has no runtime dependencies to add.

### Consequences

- Good, because a new package passes the same checks every time and leaves a record of why it was chosen.
- Good, because the guess-a-package-name risk is named and has a one-command check.
- Bad, because it is instruction text only: nothing fails if an agent skips it, so review (`docs/protocols/review.md`) is what catches a dependency added without a record.
- Bad, because the vetting thresholds (about 12 months since the last release, permissive licenses) are rules of thumb, not tested numbers.

## More Information

- Follow-up candidates: a check that every dependency in `package.json` has a record, and Dependabot or equivalent for updates, once generated projects have a CI convention. Upgrading a dependency, or removing one without a replacement, is not covered yet.
````

## Other changes on the experiment branch

```diff
diff --git a/template/AGENTS.md.jinja b/template/AGENTS.md.jinja
index e24cdab..64c5beb 100644
--- a/template/AGENTS.md.jinja
+++ b/template/AGENTS.md.jinja
@@ -52,7 +52,8 @@ Unattended work starts only on tasks labelled `ready` by the gate in `docs/proto
 ## When to read what
 | Situation | Read |
 |---|---|
-| Writing TypeScript, adding a helper or dependency, integrating an external service | `docs/protocols/typescript.md`, `docs/protocols/evolution.md` (ports) |
+| Writing TypeScript, adding a helper, integrating an external service | `docs/protocols/typescript.md`, `docs/protocols/evolution.md` (ports) |
+| Adding a library, package, SDK or other third-party dependency, or swapping one | `docs/protocols/dependencies.md` |
 | Making a decision | `docs/decisions/README.md` |
 | Deciding who approves (product, architecture, technical) | `docs/protocols/charter.md` |
 | Copied code, a long file or function, a repeat bug, a change scattered across places, painful test setup | `docs/protocols/evolution.md` |
diff --git a/template/docs/protocols/typescript.md b/template/docs/protocols/typescript.md
index d1d14b9..41a1354 100644
--- a/template/docs/protocols/typescript.md
+++ b/template/docs/protocols/typescript.md
@@ -3,10 +3,10 @@ protocol: typescript
 kind: rule
 status: active
 summary: Before writing a helper, reuse project code, then native APIs, then preferred libraries, and only then custom code.
-applies-when: Writing TypeScript, adding a utility or helper, or choosing a library.
+applies-when: Writing TypeScript, adding a utility or helper, or picking from the preferred libraries.
 agents: []
 skills: []
-related: []
+related: [dependencies]
 ---
 # TypeScript: reuse before building
 
@@ -27,7 +27,6 @@ Before writing any utility or helper, check in this order:
 4. **Custom code.** Only if none of the above fits. Put it in the project's shared utils location so it is reusable, and keep it small and typed.
 
 Rules:
-- Prefer libraries already in `package.json`. A new library is a decision: check it against the rules in `AGENTS.md` and log it if non-trivial.
-- Before adding or using a library, check its current docs and the installed version. Prefer actively maintained packages (recent releases, wide adoption) with permissive licenses (MIT, Apache-2.0, BSD).
+- Prefer libraries already in `package.json`. Adding a new one (including any in the list above that the project does not have yet) follows `docs/protocols/dependencies.md`: vetting, who approves, install and record.
 - Don't add a library for a one-liner the native API already handles.
 - Match what the repo already uses (if it uses lodash or dayjs, don't introduce es-toolkit or date-fns alongside it).
```

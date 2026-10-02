---
id: doc-3
title: Lab protocol examples (proposed text)
type: specification
created_date: '2026-10-02 02:40'
updated_date: '2026-10-02 02:40'
---
# Lab examples

Companion to `docs/protocols/lab.md`. Read an example only when `lab.md` points to it; you do not need this file to follow the protocol.

Each example has a stable ID so the protocol can refer to it. The examples illustrate; when one conflicts with the protocol, the protocol wins. Product and provider names are placeholders for whatever your project uses.

---

## EX-001: A lab is appropriate

**Situation:** A shared `PaymentProvider` port must work for two payment providers. The first supports idempotency keys on every charge; the port does not model them.

**Why a lab:** The answer decides a contract that the backend, the web app and the mobile app all depend on, and a wrong guess means changes across every adapter and caller.

**Lab question:**

> Can the existing `PaymentProvider` port preserve safe retries (idempotency) without leaking one provider's concepts into the domain?

---

## EX-002: A lab is not appropriate

**Situation:** A TypeScript generic in an already established repository pattern fails to infer correctly.

**Why not:** The issue is local, reversible and does not challenge an architectural assumption.

**Action:** Fix it in the normal flow and add a test if useful.

---

## EX-003: Documentation is not enough

**Situation:** The Next.js docs suggest that a Server Action can revalidate a cached page, but it is unclear whether the behaviour is identical in a production build and in the dev server.

**Why a lab:** The answer depends on real framework behaviour, not on API knowledge.

**Experiment:** Build the smallest page that exercises the Server Action and the cache in both `next dev` and a production build, and compare.

---

## EX-004: Workarounds signal hidden uncertainty

**Situation:** An implementation adds a special case for the web app, then another for the mobile app, then another for the backend, all around the same shared type.

**Interpretation:** The workarounds may be compensating for a flawed shared abstraction.

**Action:** Stop extending the chain and run a lab on the underlying assumption.

---

## EX-005: Good and bad lab names

Good:

```text
LAB-20261002-payment-port-idempotency
LAB-20261002-next-action-cache-semantics
LAB-20261002-hermes-intl-support
```

These name the uncertainty.

Avoid:

```text
LAB-use-provider-sdk
LAB-fix-payment-interface
LAB-new-better-cache
```

These encode a preferred answer before the experiment begins.

---

## EX-006: Prepared LAB.md

A React Native project needs locale-aware date formatting and wants to rely on `Intl.DateTimeFormat`. The project's AGENTS.md warns that Hermes lacks some modern built-ins.

```markdown
---
id: LAB-20261002-hermes-intl-support
task: TASK-52
status: PREPARED
base_commit: 7b2f6db
budget: 90 minutes
---

# Lab: Hermes Intl support

## Question
Does `Intl.DateTimeFormat` on the project's Hermes build give correct output for the locales the app ships (en, el, de), on a real Android device and on the iOS simulator?

## Why it matters
Date formatting is used on every screen. If Intl is incomplete we need a library, which changes bundle size and the formatting boundary used by every screen. Finding out after the screens are built means rework on all of them.

## Assumption and hypothesis
The design assumes built-in Intl is enough. We expect all three locales to format correctly.

## Evidence and falsifier
A fixed set of dates formatted in each locale, with the exact output recorded. Falsifier: any locale falls back to en or throws.

## Scope
Date formatting for the three shipped locales. Number and plural formatting are out of scope.

## Budget and side effects
90 minutes. No external services. The test app is installed on one personal test device and removed at close.

## Plan
1. Add a screen to a throwaway app that prints the formatted dates.
2. Run it on the device and on the simulator.
3. Compare to the expected strings.
```

---

## EX-007: Smallest discriminating experiment

**Question:** Can the proposed `Mailer` port work with two email providers?

Bad experiment:

> Build the whole notification system for both providers: templates, retries, bounce handling and unsubscribe links.

Better experiment:

> Implement `send()` for one representative message with each provider's sandbox and verify that the application consumes the same domain result.

The second experiment answers the architectural question with far less noise.

---

## EX-008: Do not polish the spike

**Situation:** The experiment already shows that both adapters can satisfy the port, but the temporary mapper functions are repetitive.

Bad response:

> Refactor the lab into a reusable mapping framework before concluding.

Better response:

> Record that the contract works, note the constraints found, conclude the lab, and design the production mappers later.

---

## EX-009: Splitting a new question

**Original question:** Can the Next.js app reuse the Zod schemas defined in the Express backend?

During the experiment a second question appears:

> How should schema versions be handled for mobile apps that users have not updated?

It is valuable on its own and not needed to answer the original question.

**Action:** Add it under Open questions and create a separate `spike` task if it matters.

---

## EX-010: Stop on contract failure

**Situation:** The lab proves that the existing `PaymentProvider` port cannot express idempotency without provider leakage.

**Conclusion:** `REJECTED`

**Impact:** `CONTRACT CHANGE REQUIRED`

The lab stops here. It does not change the port and carry on as if the new contract were accepted. The next step is a decision record that supersedes the old one. If the new port breaks an API used outside this change (for example a deployed mobile app), that is a big change under `docs/protocols/charter.md`, so the record is `proposed` and waits for the owner; if every caller is inside this project, you record it as `accepted` and build it.

---

## EX-011: Inconclusive is valid

**Question:** Does a proposed caching strategy behave the same in local development and in the target deployment?

**Finding:** Local tests are conclusive, but the deployment behaviour cannot be reproduced in the lab environment.

**Conclusion:** `INCONCLUSIVE`

**Recommendation:** Name the missing environment-specific evidence and run a separate, targeted investigation.

Do not manufacture confidence to avoid an inconclusive result.

---

## EX-012: A good conclusion

Weak:

> The approach seems fine and we should probably use it.

Strong:

> `CONFIRMED` for the two providers tested. Both can satisfy the proposed `Mailer` port without provider types escaping the adapter. One constraint was found: delivery status arrives asynchronously from one provider, so it must stay outside this port and be handled by a separate boundary.

The strong version answers the question, says what it held for, and records the constraint.

---

## EX-013: Distillation

A lab contains three failed prototypes, debugging logs, temporary packages, benchmark notes, two abandoned type models and one successful final experiment. Production does not need all of it.

A distilled result:

```text
Decision record 0007: Provider ports keep delivery status outside the port

Decision:
Adapters expose a provider-neutral send result but not delivery status.

Reason:
The lab showed that one provider reports delivery asynchronously, so forcing it into the port added provider leakage. Evidence: docs/labs/LAB-20261002-mailer-port-shape.md
```

The decision moves into the project's records; the lab record keeps the evidence.

---

## EX-014: Returning to normal work

The lab proves that a shared port works.

Bad flow:

```text
lab branch -> merge the whole branch -> main
```

Preferred flow:

```text
lab findings -> accepted decision -> clean implementation on a feature branch
```

A lab commit may still be promoted when it is clearly production quality, but that is an explicit decision recorded on the task, never the default.

---

## EX-015: Legitimate protocol deviation

**Situation:** One experiment must compare two mutually exclusive package versions, and a single worktree cannot hold both environments cleanly.

**Deviation:** The agent creates two sibling worktrees under the same lab ID and treats them as two arms of one experiment.

**Entry under Deviations and protocol feedback:**

```text
One worktree could not represent both package versions without repeatedly mutating the environment. Two worktrees (.claude/worktrees/<LAB-ID>-a and -b) were used to keep reproducible baselines. Both belong to this lab and feed one conclusion.
```

This keeps the intent (isolation, reproducibility) and adapts the procedure.

---

## EX-016: Protocol feedback

**Observed problem:** Several labs need more than one isolated environment to compare incompatible dependency sets.

**Suggested change:** Let a lab declare named experiment arms.

**Expected benefit:** More reproducible comparisons without treating each arm as a separate question.

**Possible downside:** More lifecycle complexity and more to clean up.

This is a proposal, not an automatic change to the protocol.

---

## EX-017: Budget spent

**Situation:** A lab with a 90-minute budget is trying to find out whether a native module builds on the project's React Native version. After 85 minutes the build still fails with a different error each time.

**Action:** Stop at the budget. Record what was tried and the last error, conclude `INCONCLUSIVE`, and recommend either a smaller targeted lab (for example, a build on the previous React Native version) or choosing a different module. Do not keep going "just a bit longer": that is how a lab turns into the implementation.

---

## EX-018: Side effects

**Situation:** A lab needs to confirm that a payment provider returns a specific error code for an expired card.

Bad:

> Use the live account's API key and send test charges.

Better:

> Use the provider's test mode with a test key, from `.env` in the lab worktree only. Record in the lab that no live key was used. If only the live service shows the behaviour, stop and ask the owner; if the owner is away, conclude `INCONCLUSIVE` and list the missing approval in the end-of-task summary.

---

## EX-019: The conclusion check catches overreach

**Situation:** A lab concludes `CONFIRMED`, "caching works the same in development and in production", with `ADR CANDIDATE` as the impact. The reviewer reads the Log and finds that the production build was tested only on Node 22 while the deployment runs Node 20.

**Outcome:** The reviewer, running inside the review loop of the decision-record change, reports a Material finding. The agent either re-runs the experiment on Node 20 or narrows the conclusion to `PARTIALLY CONFIRMED` ("for Node 22"), then the loop continues with the next round.

---

## EX-020: A lab in Backlog

```text
# the question, as a spike task
backlog task create "Does the Payment port support safe retries?" --type spike -l lab -s "In Progress" -d "Lab LAB-20261002-payment-port-idempotency. Decides whether the port contract changes before the checkout work starts." --ac "LAB.md concluded with a result and an impact"

# the task that needs the answer waits for it (TASK-41 is the new spike).
# --dep replaces the whole list, so repeat any existing dependencies (here TASK-12).
backlog task edit TASK-40 --dep TASK-12,TASK-41
```

When the lab concludes, the answer goes on TASK-40 as a note (with a link to the lab record where one exists, otherwise to the spike task), and the dependency is removed (for `NEW INVESTIGATION REQUIRED` it is replaced by the follow-up spike instead).

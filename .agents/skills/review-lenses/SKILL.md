---
name: review-lenses
description: Lenses a code reviewer applies to a change. Preloaded by the code-reviewer profile; do not invoke in the main session.
user-invocable: false
---

# Review lenses for code

The orchestrator names the lead lenses for each round; apply those first, then the rest briefly.

- **Correctness:** the happy path, common failures, edge cases with real impact. Name the input that breaks it.
- **Tests:** each test exercises the real implementation and would fail with the change removed; mocks only at true external boundaries (third-party services, providers, hardware, the clock).
- **Boundaries:** code that talks to external services goes through a port where the project uses one; no new coupling across the boundaries the project describes.
- **Safety:** no secrets in code, logs or commits; no destructive operation without the project's approval rule.
- **Standard over custom:** an established library or convention exists for what was hand-written? Say which.
- **Knowledge kept current:** the change updates the decision records, the architecture description and the domain glossary where it affects them, as the project's protocols require where present.
- **Instructions:** when instructions change, they stay consistent with each other, own each rule in one place, and read correctly to a literal reader.
- **Scope:** nothing beyond what the task asked; no speculative abstraction.

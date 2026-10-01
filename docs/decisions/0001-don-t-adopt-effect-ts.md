---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: technical
supersedes: []
---

# Don't adopt Effect-TS

## Context and Problem Statement

Effect encodes success/error/dependencies in types and adds structured concurrency, retries, resource safety. Evaluated as a foundation for all projects. (Decided in discussion before this repo existed.)

## Considered Options

Effect everywhere — pays off only in large backends orchestrating lots of unreliable I/O; overkill for CRUD APIs, Next.js UIs, RN apps. Its "better with agents" benefit (stricter compiler) is offset by API churn (v4 was a release candidate, v3 still recommended for production) and less training data.

## Decision Outcome

Not adopted. Use `neverthrow` for typed errors, plain factory functions for dependency injection, small focused libraries (`p-retry`, `p-limit`) for retries/concurrency.

### Consequences

Revisit if a project becomes a large I/O-orchestration backend (LLM calls, payments, job workers) or Effect v4 stabilizes and gains adoption.

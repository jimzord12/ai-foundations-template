---
status: accepted
date: 2026-09-29
decision-makers: owner
kind: product
supersedes: []
---

# Public GitHub repo, MIT license

## Context and Problem Statement

Where the template lives and under what terms.

## Considered Options

Private repo — safer default but nothing here is secret and public makes `copier copy gh:...` work without auth. Other licenses (Apache-2.0) — MIT is the most common permissive default for small tooling.

## Decision Outcome

Public GitHub repository; MIT license.

### Consequences

Never commit secrets or client-specific details to the template.

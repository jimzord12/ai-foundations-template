---
name: scan-lenses
description: Scannability lenses for human-facing docs (README, guide, checklist, handout). Preloaded by the scannability-reviewer profile; do not invoke in the main session.
user-invocable: false
---

# Scannability lenses

Readers of human-facing docs skim: they glance at one part, act, and glance back. The one question: can a reader find what they need and act on it in seconds, without reading anything twice?

Whether the content is true is not yours; docs-reviewer checks that. A sentence too unclear to tell what the reader should do is yours; a clear sentence that may be wrong is not.

The brief names the audience and any style the doc must follow, and may name lead lenses; apply those first, then the rest briefly.

## Lenses

- **Lead with the answer.** The first lines say what the doc is for and give the thing most readers came for (the command, the decision, the result). Background comes after, if at all.
- **One shape per entry.** Repeated entries (steps, scenarios, records, options) use the same sections, in the same order, with the same labels. A reader who learned entry 1 reads entry 20 without re-orienting.
- **Steps are commands.** One action per step, imperative, starting with the verb or the place ("Open **Settings**", "Run `npm test`"). No rationale inside a step. UI labels in bold, exactly as the screen shows them.
- **Results are observable.** An expected result says what the reader sees (a screen, a message, a value, an exit code), never an internal state they cannot check.
- **Zero filler.** Flag every word that carries no meaning: lead-ins, hedges, restatements, rationale the reader does not need to act. Quote the phrase and give the shorter form.
- **Salience spent, not sprayed.** Bold, emojis and callouts mark only what a reader must notice or navigates by. One vocabulary, each marker's meaning fixed and explained once when not obvious, used the same way everywhere. Flag decoration, emoji walls and bold on ordinary words.
- **Tables and code blocks for shapes.** Rows that share columns go in a table; a schema, configuration, payload or command goes in a code block with a one-line brief above it. Tables never hold paragraphs.
- **Short sections, easy navigation.** Headings that say something, stable numbering, a contents list or index at the top of a long doc, nesting at most two levels deep.
- **Proportionate length.** An entry much longer than its siblings without cause, or a section the reader would skip, is a finding.
- **Plain words.** Jargon is explained in a few words on first use; one word per concept throughout, the glossary's word where the project has one.

## Severity for scannability

The scale is review-core's; style alone is never Blocking.

| Severity | Usual cases |
|---|---|
| Material | A reader cannot act on an entry or would likely misread it; a step with no observable result where the reader needs one |
| Minor | A reader slows down: filler, prose steps that still work, entries that should share a shape but do not, sprayed salience, inconsistent markers, an outlier entry |
| Note | Polish a reader would barely notice |

## Report

Add one line on what already works well, so the author keeps it. Keep the report short: you are held to the standard you enforce.

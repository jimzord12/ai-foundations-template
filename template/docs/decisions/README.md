# Decisions

One file per decision, in [MADR 4](https://adr.github.io/madr/) format (minimal variant). Check here before deciding anything. If AGENTS.md says this project keeps decisions elsewhere, use that location; this folder then stays unused.

- **New record:** copy `adr-template.md` to `NNNN-title-with-dashes.md` with the next free number, fill it in, and add a row to the table below in the same change.
- **Kinds:** `product` (what users see and do), `architecture` (how the code is shaped), `technical` (tools, libraries, conventions). Who decides each kind, and what counts as a big architecture change: `docs/protocols/charter.md`. Whatever the kind, the hard-to-reverse list in AGENTS.md "Who decides what" is always the owner's.
- **Status:** `proposed`, `accepted`, `rejected`, `deprecated` or `superseded by NNNN`. A record that needs the owner's approval stays `proposed` until they approve it.
- **Changing a decision:** never rewrite an accepted record. Add a new one that lists the old number under `supersedes`, and set the old one's status to `superseded by NNNN`. Refinements and other links go under More Information, not `supersedes`.
- **Architecture decisions** update `docs/architecture.md` in the same change.

| Record | Kind | Status | Title |
|---|---|---|---|

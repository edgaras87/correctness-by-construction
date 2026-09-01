# 0010. The bundle gathers under starter/

Date: 2026-09-01
Status: Proposed

## Context

ADR-0004 placed the executions flat under `executions/` with the
bundle doc among them. Two developments strained that: the doc is a
stay-home file sitting inside the copy set — a boundary enforced
only by the copy table's omission, parked in TODO (2026-08-30) as
weaker than the kit's structural boundary (handbook ADR-0016) — and
the handbook's starter redesign (their ADR-0028) named our bundle
manual an explicit peer of `starter/installs/default.md`, "the
shape yours mirrors," inviting shape symmetry at every birth's
two-repo visit.

## Options considered

1. Evict: keep `concept/` and `executions/` untouched and shipping
   whole; move only the describing README and the birth manual out
   to a small stay-home directory (`delivery/`). Cheapest — two
   file moves, ADR-0004 intact, the concept/ question never arises.
   Rejected by the user for the mirror's clarity: a birth visits
   the handbook's starter and then ours, and twin shapes make the
   composition legible.
2. Full gather: a `method/` directory absorbing `concept/` and the
   executions, docs outside. Rejected: it files the mental layer
   under a delivery-flavored tree — the repo reads as a shipping
   kit that contains a concept, instead of a concept with
   derivations.
3. Gather the executions under `starter/bundle/`, split the doc
   into a describing README and an installs/ manual, `concept/` at
   the root — chosen.

The leak objection to option 3 — a gathering boundary that exempts
one shipped directory — is answered by not claiming totality: the
copy rule names two wholesale directories, and each is internally
unambiguous. The file-level ambiguity ADR-0016 guards against (a
stay-home file among copied siblings) existed only inside
`executions/`; `concept/` ships whole and never had it.

## Decision

`starter/` at the repo root, mirroring the handbook's starter
shape:

- `starter/README.md` — describes: what the bundle is, the copy
  table, the overlay contract from our side, the harvest flow.
  Stays home.
- `starter/installs/cbc.md` — the birth manual, peer of the
  handbook's `installs/default.md`. Stays home.
- `starter/bundle/` — everything that ships: the five skills with
  their references and templates, the startup snippet, the cbc-run
  playbook, `birth-scenario.md`. Nothing in here stays home.

`concept/` remains at the root and ships whole. The copy rule is
two wholesale directories; within `starter/`, stay-home vs ships is
structural — nothing under `bundle/` stays, nothing outside it
ships.

ADR-0004 is amended in its placement only. Its other decisions
stand unchanged: pin-plus-provenance headers, SKILL.md headers
below frontmatter, authoritative-vs-pinned, birth directed by a
mapping doc.

## Consequences

Good: a correct copy is a directory diff, not a table check; the
bundle doc cannot drift into a newborn by accident; the
peer-manual mirror is true in both directions (FYI queued for the
handbook).
Bad: paths in historical records go stale — accepted, history is
not rewritten; this ADR carries the mapping (`executions/` →
`starter/bundle/`; `executions/README.md` → `starter/README.md` +
`starter/installs/cbc.md`). Every skill path gains a directory
level.

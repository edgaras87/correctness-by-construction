# Changelog

The concept-version log: each released entry is one concept version —
what changed in the mental layer and why, with run provenance when the
change was harvested, and which executions were reviewed or re-derived.
Format: [Keep a Changelog](https://keepachangelog.com/) · Versions are
concept versions — whole numbers, not SemVer (ADR-0003).

<!-- Write entries WHEN the change lands, for the pinners: run repos
     and executions citing a concept version. A version bump = a change
     that could invalidate a derived execution; editorial fixes ride
     with the next version (ADR-0003). Categories:
     Added · Changed · Removed · Fixed.
     Releasing = rename [Unreleased] to [vN] - date, open a fresh one.
     [Unreleased] is the net change since the last release: a later
     change that undoes or reshapes an entry in it edits that entry,
     never adds a second. An entry is the concept, or an execution
     derived from it or checked against it; a convention's change,
     or the delivery's, is none — a manual has no version
     (ADR-0039). -->

## [Unreleased]

### Added

- **The method**, derived from concept v1: `cbc-framing` — an idea
  worked into one falsifiable promise, a layered system definition
  and a slice registry — and `cbc-slice` — one invariant carried
  through specify, plan, build and document until a test that
  creates its adversity shows it holds. Each with its workflow, a
  worked example, and the registry template or readiness checklist
  it hands on (ADR-0008); and beside them the shapes their gates
  read: a slice record, an evidence test, a kill and a registry
  entry, from run 3's records (ADR-0052).
- **The stack practice**, checked against concept v1 and not derived
  from it: `infra-establish`, `infra-serve` and `cbc-bootstrap`, for
  a Spring and PostgreSQL run, with the templates a run fills and
  then owns (ADR-0029).

### Changed

- **The walls chapter, harvested from never-oversold — the concept
  becomes v2.** The top rung of the wall ranking is the store's
  refusal: a constraint, or a right withheld from the identity
  that writes. A new paragraph says who each wall leaves unbound —
  whoever can remove it — so the described adversary says who
  besides the system may write what it stores, and a single entry
  path is a wall only where that answer names it the only writer.
  A plan derived from v1 could hold such a path as a wall with no
  answer behind it (ADR-0048). `cbc-slice` and `cbc-framing` state
  the ranking anew.
- Chapter 03's sentence on when technology enters, corrected from
  the runs: after framing, each choice answerable to the slice
  registry — not "with the first slice". Editorial.
- Chapter 01's layer tags in full words, the number before the
  name: LAYER-1-ENVIRONMENT, LAYER-2-SYSTEM, LAYER-3-AREAS,
  LAYER-4-PROBLEMS, LAYER-5-INTERACTION, where it said L1 to L5.
  From never-oversold's retrospective; the names are the
  chapter's own. The method and stack skills use them. Editorial.

### Removed

- The chapters' provenance headers. Each line was history, kept in
  `[v1]` below, ADR-0003 and git, or the one instruction a run's
  copy needs — what may be done to it — which the run's own rule
  gives (ADR-0022, ADR-0051).

## [v1] - 2026-08-28

### Added

- The concept statement, as five chapters under `concept/`: the
  inversion and the derivation order (00), the layered system L1–L5
  (01), guarantees and the wall hierarchy (02), framing (03), the
  slice (04). Imported from the archive
  (system-design-method/birth-materials/concept/ @ fe0075d) unchanged
  in substance; the archive copy is now a historical snapshot.

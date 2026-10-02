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
  it hands on (ADR-0008).
- **The stack practice**, checked against concept v1 and not derived
  from it: `infra-establish`, `infra-serve` and `cbc-bootstrap`, for
  a Spring and PostgreSQL run, with the templates a run fills and
  then owns (ADR-0029).

### Changed

- Chapter 03's sentence on when technology enters, corrected from
  the runs: after framing, each choice answerable to the slice
  registry — not "with the first slice". Editorial; the concept
  stays v1.
- Every chapter's header names the canonical copy by path.

## [v1] - 2026-08-28

### Added

- The concept statement, as five chapters under `concept/`: the
  inversion and the derivation order (00), the layered system L1–L5
  (01), guarantees and the wall hierarchy (02), framing (03), the
  slice (04). Imported from the archive
  (system-design-method/birth-materials/concept/ @ fe0075d) unchanged
  in substance; the archive copy is now a historical snapshot.

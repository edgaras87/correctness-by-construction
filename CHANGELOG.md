# Changelog

The concept-version log: each released entry is one concept version.
It says what changed in the concept and why, with CBC Run provenance
when the change was a Record Harvest, and which Agent Skills were
reviewed or re-derived.
Format: [Keep a Changelog](https://keepachangelog.com/) · Versions are
concept versions — whole numbers, not SemVer (ADR-0003).

<!-- Write entries WHEN the change lands, for the pinners: CBC Runs
     and skills citing a concept version. A version bump = a change
     that could invalidate a derived Agent Skill; editorial fixes go
     in the next version (ADR-0003). Categories:
     Added · Changed · Removed · Fixed.
     Releasing = rename [Unreleased] to [vN] - date, open a fresh one.
     [Unreleased] is the net change since the last release: a later
     change that undoes or reshapes an entry in it edits that entry,
     never adds a second. An entry is the concept, or a skill
     derived from it or checked against it; a convention's change,
     or the delivery's, is none — a manual has no version
     (ADR-0039).
     Why the form is as it is: (docs/conventions/project-recording/
     §6.4, How the changelog is written).
     foundation: the project-recording convention -->

## [Unreleased]

### Added

- **The method**, derived from concept v1:
  - `cbc-framing`: an idea worked into one Falsifiable Promise, a
    System Definition and an Invariant Slice Registry;
  - `cbc-slice`: one invariant carried through specify, plan, build
    and document, until a test that creates its adversity shows it
    holds.

  Each with its workflow, a worked example, and the registry template
  or readiness checklist it hands on (ADR-0008). Beside them, the
  Output Shapes their Plan Step Gates read: an Invariant Slice
  Record, an Evidence Test, an Enemy Collision Kill and an Invariant
  Slice Entry, from CBC Run 3's records (ADR-0052).
- **The stack practice**, checked against concept v1 and not derived
  from it: `infra-establish`, `infra-serve` and `cbc-bootstrap`, for
  a Spring and PostgreSQL CBC Run, with the Agent Skill Templates a
  CBC Run fills and then owns (ADR-0029).

### Changed

- **The Structural Walls chapter, harvested from CBC Run 3
  (`never-oversold`) — the concept becomes v2.** The top rung of the
  Structural Wall ranking is the store's refusal: a constraint, or a
  right withheld from the identity that writes. A new paragraph says
  who each Structural Wall leaves unbound: whoever can remove it. So
  the described adversary says who besides the system may write what
  it stores. A single entry path is a Structural Wall only where that
  answer names it the only writer. A plan derived from v1 could hold
  such a path as a Structural Wall with no answer behind it
  (ADR-0048). `cbc-slice` and `cbc-framing` state
  the ranking anew.
- Chapter 03's sentence on when technology enters, corrected from
  the CBC Runs: after CBC Framing, each choice answerable to the
  Invariant Slice Registry — not "with the first slice". Editorial.
- Chapter 01's layer tags in full words, the number before the
  name: LAYER-1-ENVIRONMENT, LAYER-2-SYSTEM, LAYER-3-AREAS,
  LAYER-4-PROBLEMS, LAYER-5-INTERACTION, where it said L1 to L5.
  From CBC Run 3's retrospective; the names are the chapter's own.
  The method and stack Agent Skills use them. Editorial.
- The five chapters in plain words, and in the concept's Names:
  Invariant Slice, CBC Framing, System Guarantee, Structural Wall,
  Falsifiable Promise, Enemy Census and the rest, each defined where
  it was. Long sentences split, lists made of chained parts, figures
  replaced: the two "movements" are its two parts, "How it rots" is
  How it fails, "the joint" is the pair. No meaning moves; concept v1
  stays v1. Editorial.

### Removed

- The chapters' provenance headers. Each line was history, kept in
  `[v1]` below, ADR-0003 and git. Or it was the one instruction a
  CBC Run's copy needs, what may be done to it, which the CBC Run's
  own rule gives (ADR-0022, ADR-0051).

## [v1] - 2026-08-28

### Added

- The concept statement, as five chapters under `concept/`: the
  inversion and the derivation order (00), the layered system L1–L5
  (01), guarantees and the wall hierarchy (02), framing (03), the
  slice (04). Imported from the archive
  (system-design-method/birth-materials/concept/ @ fe0075d) unchanged
  in substance; the archive copy is now a historical snapshot.

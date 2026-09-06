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
     Releasing = rename [Unreleased] to [vN] - date, open a fresh one. -->

## [Unreleased]

### Added

- A CLAUDE.md template (`starter/bundle/claude-md-template.md`,
  composed from the kit's entry file at the pin and this repo's
  own fills; ADR-0014, ADR-0015) — since ADR-0016 parked,
  undelivered: the pure-born newborn derives its own arrangement,
  and the template stands as the three-way reading's comparison
  object. The birth-fill templates were retired with the assembly
  path.

### Changed

- The framing chapter's technology-timing sentence corrected
  against the lived runs (`concept/03-cbc-framing.md`, first
  content change since import): technology arrives after framing,
  each choice answerable to the slice registry — not "with the
  first slice", which the runs' lived order (ground and skeleton
  stood up before the first slice, every service traced to a
  registry need) contradicted.
- A birth is the pure seed (ADR-0016, superseding the assembly
  shape earlier drafts of this entry described): material only —
  every delivery a commit on main with its source's pin in the
  subject, the newborn's agent finishing the birth itself,
  paced by a reviewer at every commit boundary.
  `starter/installs/pure-seed.md` is the birth procedure. The
  newborn still holds no playbook copy — the steps land in PLAN
  between the STEPS markers, with a "Steps from:" line naming
  the playbook at the bundle pin. Retired with the assembly
  shape (history keeps them): the birth scenario, the assembly
  install manual, the birth fills, and the parent playbook —
  the pure variant (cbc-run-pure) is the playbook.
- The install manual's playbook block keeps the STEPS markers:
  only what sits between them is swapped, so re-running the block
  is genuinely harmless.
- The playbook's kit steps re-vendored from the handbook's
  `starter/playbooks/default.md` v2 (their new home): Step 0's
  comment slims to kit facts, Framing gains the every-step
  projection gate item — cbc-run.md is v3 (that parent playbook
  has since retired, ADR-0016; the pure variant carries the
  vendored steps forward).
- Concept chapter headers name the authoritative copy by path
  instead of claiming it for whichever copy is being read —
  header-only, the concept stays v1.

## [v1] - 2026-08-28

### Added

- The concept statement, as five chapters under `concept/`: the
  inversion and the derivation order (00), the layered system L1–L5
  (01), guarantees and the wall hierarchy (02), framing (03), the
  slice (04). Imported from the archive
  (system-design-method/birth-materials/concept/ @ fe0075d) unchanged
  in substance; the archive copy is now a historical snapshot.

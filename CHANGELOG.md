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

- The bundle ships the newborn's arrangement as text: a complete
  CLAUDE.md template (`starter/bundle/claude-md-template.md`,
  composed from the kit's entry file at the pin and the method's
  text — merged once from the first walked birth's derivation and
  the withheld snippet — copied whole at birth, no merge into the
  kit's stub; ADR-0014, delivery per ADR-0015) and birth-fill
  templates (`starter/bundle/birth-fills.md`, generalized from
  that birth's lived fills). No newborn derives its arrangement
  again.

### Changed

- A birth is assembly (`starter/bundle/birth-scenario.md`,
  revised in the first newborn and carried back): six mechanical
  seed steps, three prescribed commits, then the briefing. The
  bundle lands under `docs/` in the newborn; the newborn holds no
  playbook copy — its steps land in PLAN between the STEPS
  markers, with a "Steps from:" line naming the master at the
  bundle pin — and the copy table has the new destinations.
- The install manual's playbook block keeps the STEPS markers:
  only what sits between them is swapped, so re-running the block
  is genuinely harmless.
- The playbook's kit steps re-vendored from the handbook's
  `starter/playbooks/default.md` v2 (their new home): Step 0's
  comment slims to kit facts, Framing gains the every-step
  projection gate item — cbc-run.md is v3.
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

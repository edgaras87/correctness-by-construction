# Change-plan: run-repo doc layout + README projection law

## Summary — the state after all commits

A run repo's documents have three visible homes, and the layout says
which is which: the README at root (the surface — derived, never a
second master), the three exports under `docs/system/` (internal
truth, one nameable path: `intent.md`, `definition.md`,
`registry.md`), and the derivation record nested inside it at
`docs/system/framing/` (`derivation.md` plus any appendix sweeps —
how the truth was earned, frozen at close). The prefixes that were
doing a directory's job — the dotted export names, the
`framing-<name>` appendix prefix — are dissolved by the directories
that now do it. The README gains its law, harvested from the
safe-reservations node's projection model and guide (read read-only,
ADR-0007, their vocabulary never adopted): derived from the exports
per the five-piece derivation table, thin-README-only at framing
close, refreshed only through logged revision entries at real
milestones, residue filter applied. Every skill that names the
export files points at the new paths. TODO and devlog reflect the
check's close; the deeper projection lifecycle (README refresh at
slice close, a public surface earned by demonstrated substance) is
parked as a Later item until a run lives it.

## Commits

**1. `docs(agent): add change-plan for doc projection`**
This plan, committed after agreement, before the work.

**2. `docs(executions): move exports under docs/system/`**
The layout re-derivation, one coherent change across every file that
names the export paths: cbc-framing's SKILL (record section, export
section, where-records-live map, provenance header line), the
registry template renamed `templates/slices.registry.md` →
`templates/registry.md` to keep mirroring the export it fills,
cbc-slice's SKILL (trigger description and R1), the readiness
checklist, the startup snippet, and infra-establish. Derivation doc
moves to `docs/system/framing/derivation.md`; appendices become
plain-named files beside it. Split any narrower and a revert leaves
skills pointing at files the framing no longer produces.

**3. `docs(executions): harvest README projection law`**
cbc-framing's export section gains the projection block: the README
derived from the three exports (the five-piece table: intent → why,
definition → what, registry → planned invariants, method note,
status line), thin-README-only the default verdict at framing close
(rebuttable, logged), the README joining the living-records rule,
the residue filter extended to the surface, and the README as the
final commit of the derivation-order export story. Provenance header
line records the harvest.

**4. `docs: update TODO after projection check`**
The doc-projection Next item closes (checked, harvested); the
dotted-export-names Later item deletes (dissolved by the layout —
the directory now carries what the prefix carried); a new Later item
parks the deeper projection lifecycle for when a run lives it.

**5. `docs: add devlog entry for projection check`**
The session's history: what the two projection versions showed, what
was adopted, what was refused (planes, settings, per-milestone
machinery — unlived here), the layout re-derivation and why root
placement fell.

**6. `docs(agent): close change-plan for doc projection`**
Deletes this file; body records what diverged, or that nothing did.

## Decisions taken inside this plan

- **The layout move is one commit, six files.** The revert test
  forces it: renaming in cbc-framing alone leaves cbc-slice,
  infra-establish, and the snippet demanding files no framing
  produces.
- **Root placement falls as a re-derivation, not a contradiction of
  lived evidence.** Checkout's root exports were an auto-run default
  never verdicted; the derivation doc's placement was never lived at
  all. The dir buys a structural source set for projection plus
  three dissolved naming debts.
- **Only the projection law's lived core is harvested.** The
  README-derivation rule, the table, and the thin-README verdict
  were lived (safe-reservations walk 2; checkout converged on the
  shape independently). The model's plane directories
  (`internal/`, `public/`), the docs-practice setting apparatus, and
  per-milestone guides are refused: unlived here, and the plane
  layout conflicts with the layout this plan adopts.
- **checkout-system stays untouched** (read-only, ADR-0007). Its
  root-level dotted exports stand as the old lived state; the
  provenance headers record why the shape moved on.
- **cbc-slice's trigger description is edited** — it names
  `slices.registry.md` verbatim. The existing TODO note already
  designates trigger descriptions as the knob.
- **`temp/` is left alone** — the user's staging copies, untracked,
  theirs to clear.

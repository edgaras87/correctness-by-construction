# Change-plan: retire the assembly path — the pure shape is the way

## Summary — the state after all commits

The user's decision (2026-09-06): the assembly walk is cancelled.
Run 1 of the pure seed validated everything the pure variant
changed, and the trial the assembly artifacts were waiting for
will not be walked. After this change set the repo carries one
birth shape: the pure seed. Deleted, with history and the
baselines keeping every byte: the parent playbook
(cbc-run-playbook.md), the birth scenario, the assembly install
(installs/cbc.md), and the birth fills. The pure variant carries
its own provenance and is the only playbook; pure-seed.md is the
procedure of record; the template stays as an undelivered master,
its fate parked with the three-way reading. ADR-0016 records the
decision and what it supersedes.

## Commits

**1. `docs(agent): add change-plan for the assembly retirement`**
This file.

**2. `docs: propose the pure shape (ADR-0016)`**
The decision, Proposed until the set's records commit: assembly
walk cancelled on run-1 evidence and the user's call; the pure
seed is the birth procedure; the four assembly artifacts retire;
the held briefing is released to the pure path; the template is
parked undelivered pending the three-way reading. Supersedes the
trial-close plan (the trial line of ADR-0015's era) and the
assembly rewrite; ADR-0011's ownership model survives in the
variant, ADR-0014's shipped-text decision stands parked.

**3. `docs(starter): the variant carries its own provenance`**
The variant's header stops delegating to the parent: a condensed
provenance block moves in (harvested 2026-08-30 from the two
lived runs; rebuilt full-sequence on the kit's default.md,
ADR-0011; kit steps re-vendored @ c670fe5; the parent's version
trail), with a pointer to the parent's full header in git
history. Must land before the deletion so no commit leaves the
variant's provenance dangling.

**4. `feat(starter)!: retire the assembly path`**
Deletes cbc-run-playbook.md, birth-scenario.md,
starter/installs/cbc.md, and birth-fills.md. starter/README.md
swept in the same commit (revert test: a table row pointing at a
deleted file is incoherent): the playbook row names the variant
and the pure seed's insert, the scenario and fills rows go, the
template row says undelivered — parked, the install pointer moves
to pure-seed.md. pure-seed.md's banner rewrites: procedure of
record per ADR-0016, no longer a draft awaiting a trial.

**5. `docs(starter): the trial line leaves the template`**
The Local rules trial line dies with the scenario it names — its
own text always said the trial-closing ADR removes it, and
ADR-0016 is that ADR. The header's trial note goes with it.

**6. `docs: records catch up — the pure shape is adopted`**
ADR-0016 flips to Accepted. TODO: the re-birth item closes as
cancelled; the pure-seed item records the variant-vs-parent
verdict (decided here, not at a trial close); the briefing's
release to the pure path noted where the held briefing is named.
CHANGELOG: assembly birth removed, pure seed is the birth
procedure. ARCHITECTURE: the birth-procedure paragraph and the
starter row updated to the pure shape (added by the §5 revision —
the original records walk missed that the shape change fires
ARCHITECTURE's moment). CLAUDE.md untouched — no row changes.

**7. `docs(agent): close change-plan for the assembly retirement`**
Deletes this file; the body records what diverged.

## Decisions taken inside this plan

- **The variant keeps its own filename.** Renaming it to the
  parent's name would re-break every reference (the install's sed,
  the baselines' banners, TODO) for cosmetics. "Pure" now names
  the adopted shape, not an experiment fork.
- **birth-fills.md dies with the path.** It is past-run text
  (generalized from walk-1's lived fills) with no delivery vehicle
  left — the pure design has the newborn write its own fills, and
  run 1 wrote better ones than the templates. Not parked: unlike
  the template, no scheduled reading wants it. History keeps it.
- **The template is parked, not deleted.** No path delivers it
  now, but the three-way reading (TODO) still needs the live
  re-cut as its comparison object, and its content may re-enter
  delivery if the pure runs show derivation inadequate.
- **Baselines untouched.** template-v1 and playbook-v2 freeze
  what the readings compare against; the walk-1 artifacts stay.
- **ADR lands Proposed, flips in the records commit** — the
  convention's default; the user's decision is firm, but the
  deletions are the evidence the ADR's consequences section
  describes, so the flip waits until they exist.

# Change-plan: the models become ours

## Summary — the state after all commits

`docs/models/` holds two documents this repo owns, taken from the
handbook at `ba7eaa4` with that coordinate kept. ADR-0002's rule
that updates arrive only as a fresh pinned copy from the handbook
is superseded; its reasoning about why a copy beats a reference is
not, and still governs how the bundle ships to runs.

After this set nothing in the repo tracks the handbook — not by
reference, not by pin, not by an owed report. It appears only as
recorded provenance, in four places that name a hash. The
ARCHITECTURE diagram loses its last upstream arrow and shows two
tiers: this repo and the runs.

## Commits

**1. `docs(adr): take the models, and supersede ADR-0002's clause`**
ADR-0026, opened Proposed. The gap ADR-0025 left: it took the kit
and the manuals and said nothing about `docs/models/`, so two files
kept a live upstream nobody had decided to keep. Decision-first,
because the decision was settled in conversation before any file
was touched.

**2. `docs(models): the two models are taken, not vendored`**
Both provenance headers rewritten — from "do not edit here, changes
happen in the handbook" to ours, with `ba7eaa4` kept as the
coordinate. Paired in the same commit with ARCHITECTURE's
no-local-edits invariant and its `docs/models/` Codemap row, which
state the same rule from the other side: revert this step and both
sides still say "vendored, never edited", which is the coherent
state.

**3. `docs: the last upstream arrow goes`**
ARCHITECTURE's Overview sentence and the diagram. The kit arrow
died with ADR-0025 and the findings arrow closed with today's
exchange, but the models were the last standing reason to draw the
handbook at all. Only after step 2 is the box removable.

**4. `docs(plan): the decision index reaches ADR-0026`**
Records catch-up, and where ADR-0026 flips to Accepted — the
final records commit, not the close.

## Decisions taken inside this plan

- **The model bodies stay verbatim.** Both are the handbook's
  DRAFTs carrying their own drafting notes. Owning a document is
  not rewriting it; the kit was taken the same way, and a rewrite
  would destroy the one thing that keeps a future re-sync cheap.
- **The tiers model describes a tier we can no longer see.** Owning
  it means maintaining a picture of the handbook's tier from below.
  Recorded as a cost in the ADR rather than avoided: the option of
  keeping one live upstream for two files was weighed and rejected.
- **ADR-0002 is superseded in part, not replaced.** Only its "from
  the handbook" clause dies.

# Change-plan: harvest checkout-system's framing lessons

## Summary — the state after all commits

The cbc-framing skill carries four lessons checkout-system lived
(read read-only, ADR-0007; TODO "Framing check" run 1 of 2):

- `templates/slices.registry.md` exists — a copy-and-fill master for
  the registry export (status vocabulary, per-slice fields, the
  reconciliation line), default but declinable: the skill text states
  the outcomes a registry must carry, so going off-template is legal
  and logged, exactly as the bootstrap config templates work
  (ADR-0008).
- The skill says the three exports are living records: after close
  they change only through logged revision entries (the framing's
  own return-trip discipline, extended past close); the registry's
  statuses already lived this way.
- The census keeps its evidence: the saturation probe log is
  recorded in L1, not just passed.
- The census may carry a short, labeled trust-assumptions list
  beside the facts — never instead of them; the original trap stays.
- The skill's mode section names the delegated-verdict mode: every
  verdict is the human's by default; a run may delegate only through
  an explicit decision recorded in the run's own records, naming the
  cost (the written trail becomes the only review). No config flag.

Each edited file gains a dated harvest line in its provenance header
naming checkout-system as the source, in this run's own wording.

## Commits

**1. `docs(agent): add change-plan for framing harvest`**
The agreed plan, timestamped before the work.

**2. `docs(executions): add slice-registry template`**
The template plus the skill's export section stating the registry
outcomes and the default/off-template rule. One step: the pointer
without the file (or the reverse) reverts incoherently.

**3. `docs(executions): make framing exports living`**
The export section's living-records rule: post-close changes only as
logged revision entries.

**4. `docs(executions): record census saturation log`**
Workflow step 2's exit (and the skill's step-2 gate) now say the
probe log is recorded in L1, not merely satisfied.

**5. `docs(executions): allow trust list in census`**
Workflow step 2's trap paragraph gains the labeled
trust-beside-facts allowance.

**6. `docs(executions): name delegated-verdict mode`**
The skill's mode section gains the delegation paragraph; the human
default is unchanged.

**7. `docs(agent): close change-plan for framing harvest`**
Deletes this file; body records what diverged.

## Decisions taken inside this plan

- **Template, not reference**, for the registry format: it is
  paste-and-fill (a skeleton with fields), which is ADR-0008's
  template side; the harness code stayed a reference because it is
  imitated, never pasted.
- **Where each lesson lands**: export-shape lessons (2, 3) in
  SKILL.md, whose export section owns that; census lessons (4, 5) in
  cbc-framing-workflow.md step 2, which owns the census; the mode
  lesson (6) in SKILL.md's mode section. The worked example is
  untouched — it is a teaching demo under the twin-copy rule, and
  the template now shows the registry shape.
- **No mechanism for delegation beyond the written decision** — a
  config variable was considered and rejected: it would hide a
  decision that must stay visible with its why and cost.
- **The TODO "Framing check" item stays open** — it covers both
  runs; safe-reservations is still owed.
- Four separate work commits rather than one "harvest" lump: each
  lesson reverts coherently on its own.

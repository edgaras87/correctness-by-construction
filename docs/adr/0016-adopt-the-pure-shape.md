# 0016. Adopt the pure shape; the assembly walk is cancelled

Date: 2026-09-06
Status: Proposed

## Context

Two birth shapes have coexisted since the pure-seed experiment
began (2026-09-05). The assembly shape: the seed copies the birth
scenario, the CLAUDE.md template, and the birth fills, and
prescribes three commits with no change-plan — the procedure of
record (`starter/installs/cbc.md`, `docs/birth-scenario.md`),
waiting on a trial walk with the held briefing, whose closing ADR
would decide between the shapes and between the parent playbook
and its pure variant. The pure shape: the seed delivers material
only, committed on main with pins in the subjects, and the
newborn's agent finishes the birth itself
(`starter/installs/pure-seed.md`, the cbc-run-pure playbook).

Run 1 of the pure seed was walked and read (2026-09-05/06, the
reading in TODO's experiment item). The newborn assembled itself
under an unprompted change-plan — eight commits, sequence
justified, the commit split held, the bundle's birth entry
reconstructed from the seed subjects, Step 0 closed clean with
the briefing waiting as Framing's input. Everything the pure
variant changed against its parent, the run validated; the
parent's Step 0 comment (three prescribed commits, no
change-plan) acquired a lived counterexample in the same walk.

Maintaining both shapes has a running cost, already paid twice in
one day: harvest lands in the parent first and the variant
re-derives, so every playbook change is made twice; and the
assembly artifacts (scenario, install, fills) are maintained for
a walk with no date.

## Decision

The user's call, on the run-1 evidence: the assembly walk is
cancelled, and the pure shape is adopted as the one birth
procedure.

- `starter/installs/pure-seed.md` is the procedure of record.
- The pure variant (`starter/bundle/cbc-run-pure-playbook.md`) is
  the only playbook; it keeps its filename and absorbs its
  provenance from the parent's header.
- Deleted, history and the baselines keeping every byte:
  `starter/bundle/cbc-run-playbook.md`,
  `starter/bundle/birth-scenario.md`,
  `starter/installs/cbc.md`, and `starter/bundle/birth-fills.md`
  (past-run text with no delivery vehicle left; run 1 wrote
  better fills unaided).
- The held briefing (safe-reservation, baseline-blind) is
  released to the pure path: it opens Framing in the pure-born
  run when the user fires it.
- The CLAUDE.md template is parked, not deleted: no path delivers
  it now, but the three-way reading (TODO) needs the live re-cut
  as its comparison object, and its content may re-enter delivery
  if the pure runs show derivation inadequate.
- The template's Local-rules trial line is removed by this ADR,
  as its own text provided — this is the trial-closing ADR, with
  a verdict the trial's designers did not expect: neither kept
  nor deleted after a walk, but cancelled before one, the pure
  evidence having answered the trial's question first.

## Options considered

1. Walk the assembly birth anyway, decide at its close — the
   recorded plan. Rejected: run 1 already answered the questions
   the walk was designed to ask (can the convention fire on its
   own trigger; does the split hold; what does an agent derive),
   and a walk maintained for symmetry is procedure without a
   question.
2. Keep the assembly artifacts as a dormant second shape.
   Rejected: dormant procedure is not inert — it is maintained
   (the double harvest), it is cited (the contract, the README
   table), and it presents two truths to any reader asking "how
   is a run born."
3. Adopt pure and delete, this decision. The cost accepted: if a
   future birth wants assembly's determinism (a scripted,
   zero-judgment seed), the artifacts must be revived from
   history and re-verified against the then-current kit.

## Consequences

Good: one birth shape, one playbook, one install manual; harvest
has a single home; the experiments (gates, three-way reading) sit
on the adopted path instead of a fork. Bad: the assembly option's
determinism is no longer a living choice — reviving it is an
archaeology task; and ADR-0009's overlay language, ADR-0011's
description of the parent file, and ADR-0014/0015's delivery
mechanics now describe artifacts that live only in history — the
decisions stand where they still bind (step ownership in the
variant, shipped-text parked with the template), and this ADR is
the pointer a reader needs.

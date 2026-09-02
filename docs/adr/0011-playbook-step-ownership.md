# 0011. Playbook step ownership: vendored endpoints, harvested middles

Date: 2026-09-02
Status: Proposed

## Context

The cbc-run playbook was born middles-only (2026-08-30, ADR-0009
change set): Bootstrap, Framing, and Release lived in the kit's PLAN
stub, and the playbook's steps were copied in at the run's Framing.
The handbook's starter redesign (their ADR-0028, @ 65dd7ee) removed
that home: the PLAN stub now ships a bare STEPS region, playbooks
hold full sequences, and a birth chooses one playbook and copies it
whole into PLAN.md — `kit/playbooks/default.md` is the bare base a
typed playbook starts from, carrying the rule "this file changes
when the kit does — and the change is carried into every playbook
holding copies of these steps."

A middles-only file has no composer under that model, and the
session detour their reply's bare "default" cost (TODO, handoff
item 2) showed what two masters meeting in a newborn does.

## Options considered

1. Stay middles-only and compose at birth: the install manual
   merges the kit's endpoint steps with our middles into PLAN.md.
   Rejected: the merge is re-derived at every birth by whoever is
   in the room, and the born plan answers to two masters.
2. Reference, not copy: a playbook that points at the kit's
   `default.md` for its endpoints. Rejected: the birth mechanism
   copies one file whole into the STEPS region, and a run's plan
   must stand alone — a pointer in a plan is a step nobody runs.
3. Full sequence with an ownership split — chosen.

## Decision

`starter/bundle/cbc-run-playbook.md` is a complete sequence, and
each step has exactly one owner:

- **Endpoints — the kit's.** Step 0 Bootstrap, Step 1 Framing, and
  Step N Release are vendored copies of the kit's
  `playbooks/default.md` steps, each opening with a provenance
  comment naming the source and pin. When the kit base changes, the
  change is carried into our copies by refresh against the new
  pin — the handbook's own carry rule, honored from our side.
  Specialization may add gate items (never weaken or remove a
  kit gate item); anything added is marked as ours.
- **Middles — CbC's own.** Define, Ground, Skeleton & bootstrap,
  and Invariant slices are this repo's authoritative material,
  born from harvest and changed only by harvest (ADR-0007). A kit
  refresh never touches them.

The pre-redesign kit template this repo's own `playbooks/` still
carried (`TEMPLATE.md`, unpinned, from the birth commit) is
replaced by a pinned copy of the current base, so the machinery the
retrospective folds into is the generation the bundle builds on.

## Consequences

Good: one master per step — a birth is one copy, and the
playbook-overlap question (TODO) collapses to "choose cbc-run.md,
the others stay uncopied"; drift is checkable per step against the
named pin; harvest and refresh have disjoint territories, so
neither update path can silently overwrite the other's work.
Bad: the endpoint copies go stale between a kit change and our
refresh — accepted: the pin line makes staleness visible, and the
pure manual's audit step (their step 0, run at every birth) checks
at the moment of use. Update flow stays the handoff channel; no
watch obligation is created.

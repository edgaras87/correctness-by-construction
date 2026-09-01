<!-- Checked against concept v1 of correctness-by-construction
     (ADR-0003, ADR-0005 — practice-born). Provenance — harvested
     2026-08-30 from the two lived runs, read-only (ADR-0007,
     ADR-0009): the Ground / Bootstrap / Slices / Release steps
     and their warnings from checkout-system
     playbooks/backend-service.md v1 (that run's retro-folded
     playbook) and its PLAN.md as lived (2026-08-27); the Define
     step from safe-reservations log.md Entry 0001 (name, repo
     name, repo description, each under a verdict). The merged
     sequence is this repo's judgment: the two parts were lived in
     different runs — checkout had no define phase, safe-reservations
     was not kit-born. -->

# Playbook: CbC run

<!-- Middle steps only — Bootstrap, Framing, and Release live in
     the kit's PLAN stub. At the run's Framing, copy these steps
     into PLAN.md after Framing and renumber; fill the specifics,
     delete what this project has no use for, add what it needs.
     After the project: fold the retrospective's lessons back into
     the authoritative copy — by harvest (ADR-0007), never by
     editing the run's pinned copy alone. -->

Playbook version: v1 (created 2026-08-30)
Last updated from project: checkout-system 2026-08-27;
safe-reservations (define step) 2026-08-30.

## Step: Define (naming)

Goal: the project's public identity decided, not defaulted.
Gate:
- [ ] Project name decided under a naming rule, with a verdict —
      not the framing's working name kept by inertia.
- [ ] Repo name and remote repo description decided the same way.
- [ ] Records updated where the working name changed (README,
      PLAN title).
Records: the verdicts, in the run's own decision log.
Warnings from past runs:
- Lived once (safe-reservations): scope belongs in the description
  ("single-SKU · reserve → confirm | release") — the description is
  where a stranger first meets the promise.

## Step: Ground / infrastructure  (infra-establish)

Goal: services stood up, constrained to need, verified both ways.
Gate:
- [ ] Environment decided against a lived default; decision recorded
      with its defeaters (ADR).
- [ ] Every provisioned service traced to a concrete registry
      adversity need; the not-provisioned list states each
      exclusion's why.
- [ ] Stand-up from clean checkout with one documented command;
      catalog check AND behavioral refusal check pass.
- [ ] Builder-facing contract and operator manual exist, written
      from lived work.
Records: ADRs; the two manuals; an establishment log of actual
outputs.
Warnings from past runs:
- The runtime ground facts must already be in the system definition
  before this step opens — check first, log the return trip if not
  (checkout-system d25ff48).
- Database authority as grants (role split, migrations-only DDL) is
  cheap here and priceless later: every immutability wall
  checkout-system grew (REVOKEs, column-grain grants) stood on it.

## Step: Skeleton & bootstrap  (cbc-bootstrap)

Goal: an empty but buildable, testable, runnable system wired to the
real ground, with the evidence harness proven on one adversity.
Gate:
- [ ] Builds and runs from clean clone with one documented command.
- [ ] Test harness drives the real store (never a mock) and one
      adversity class end to end; a deliberate break turns it red.
- [ ] Stack overlay appended to the hygiene files, below the marker.
- [ ] Requirements/decisions recorded before the code that applies
      them exists.
- [ ] cbc-slice Stage 0 readiness (R1–R6) passes and is recorded.
Records: requirements doc; ADR for stack; README run instructions.
Warnings from past runs:
- Make the test container a faithful miniature of the ground (same
  bootstrap SQL file, same identities): evidence then runs under
  production authority and proves the grant machinery for free.
- One standard test command from day one (widen surefire to *IT);
  a second command is a test that quietly never runs.
- Boot 4 line: RANDOM_PORT no longer provides TestRestTemplate —
  @AutoConfigureTestRestTemplate (also recorded in the bootstrap
  skill's walkthrough).

## Step(s): Invariant slices  (cbc-slice, one step per stage)

Goal: each registry slice closed by evidence that creates its
adversity; ordering re-decided at each close, never assumed from
the original expectation.
Gate (per stage of slices):
- [ ] Every slice: spec (zero mechanisms) → plan (one owner per
      guarantee, strongest wall) → build → adversity evidence green.
- [ ] Slice closes recorded in the registry with evidence pointers;
      ARCHITECTURE invariants updated per close.
Records: one doc per slice (spec → plan → evidence table).
Warnings from past runs:
- Budget a red-check per slice: break the guard (uncommitted),
  watch the evidence redden and the wall hold alone — the strongest
  line in every slice doc, at the cost of one run.
- Cross-check queries in earlier slices' evidence WILL trip on later
  vocabulary growth — that is the erosion guard working; update
  with a recorded note in both slice docs, never silently.
- A PLAN gate item must map to a named commit in the change-plan
  that will close it, or it lands as a divergence.
- The composition slice: keep the coordinator stateless and its
  steps the areas' replayable acts — recovery then falls out of the
  replay discipline instead of needing new machinery.

## Release additions

The kit stub's Release step gates records discipline; a running
service adds:
- [ ] Monitoring/alerts in place — unless observability was a
      recorded exclusion (it was, for checkout-system's
      correctness-portfolio shape; a deployed service should not
      skip it).
- [ ] Deploy/rollback procedure documented and tried once — same
      caveat: locally-runnable-only was a recorded exclusion there.

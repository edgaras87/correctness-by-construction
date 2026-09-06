<!-- Draft — the pure-seed candidate (2026-09-05). A variant of
     cbc-run-playbook.md (v3, this repo — provenance, harvest
     history and the kit-vendor base live in its header), created
     for the pure-seed experiment (starter/installs/pure-seed.md).
     The steps are the parent's except four deltas. Two drop
     birth-procedure statements the pure design has no place
     for: the assembly (CbC) Step 0 comment (shipped-template /
     three-commits / no-change-plan), and the (CbC) gate item's
     trailing install-manual clause. Two are the channel split
     (2026-09-05, user's design): session-scoped text belongs to
     the firing prompt and PLAN to the project — so the kit's
     first-session comment and the agent-side gates (the commit
     split, the two birth entries) leave Step 0 for the prompt
     and the run's own change-plan, making Step 0 pure container
     prep; and the briefing leaves Step 0's gates to open
     Framing as its starting input, so Step 0 closes clean, no
     gate born blocked. Lifespan: the
     experiment's reading decides — of this file and the parent,
     the winner stays and the other is deleted; until then the
     parent is the procedure of record, harvest lands there
     first, and this file changes only by re-deriving from it.
     2026-09-06 re-derivation: Framing gains the parent's new
     entry-file retirement gate item (pure-seed run 1 harvest);
     v2. -->

# Playbook: CbC run — pure

Playbook version: v2 (2026-09-06, entry-file retirement gate
item re-derived from the parent; v1 2026-09-05, variant of
cbc-run v3)

## Step 0: Bootstrap                                [~]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; re-cut for the pure design per the header. -->

Goal: the container exists — repo, records, arrangement — before content.
Gate:
- [ ] Repo initialized; hygiene base files present.
- [ ] Every placeholder filled, or explicitly deferred to a named
      step (the stack overlay defers to Framing, which confirms the
      steps that fill or delete it).
- [ ] No fill-comment remains: where a comment says its content
      replaces it, the content is there and the comment is not.
      Every other stub comment is a standing rule — it stays.
Notes:

## Step 1: Framing                                  [ ]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; additions marked (CbC). -->

<!-- CbC: this step opens on the briefing — its starting input,
     the first prompt of project work. The README purpose
     paragraph and the devlog's briefing line land here; names
     given before it are working names. -->

<!-- CbC: these gates are met via the cbc-framing skill — the
     intent, definition, and adversity registry are the problem
     statement, success criteria, and out-of-scope in the method's
     richer form. The middle-steps gate item is confirmation, not
     authoring: the steps below came whole with this playbook at
     birth. -->

Goal: know what we're building and why, before code.
Gate:
- [ ] One-paragraph problem statement in README.
- [ ] Success criteria written (how we'll know it worked).
- [ ] Out-of-scope list written.
- [ ] Middle steps stand and the plan reads end-to-end once,
      coarsely — the playbook's confirmed against the framed
      problem where a typed one was copied in, written fresh here
      where the project was born on this bare default; birth
      materials brought with the briefing weigh in either way.
- [ ] Every step whose gate makes something true that the outside
      should see names its projection as a gate item — the README
      section, the ARCHITECTURE change. Projection follows truth,
      and the gate is where it is caught.
- [ ] (CbC) Entry-file lines the briefing made false are retired
      in this set; every temporary line still standing names a
      later step as its end.
Notes:

## Step 2: Define (naming)                          [ ]

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

## Step 3: Ground / infrastructure  (infra-establish)    [ ]

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

## Step 4: Skeleton & bootstrap  (cbc-bootstrap)    [ ]

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

## Steps 5..N-1: Invariant slices  (cbc-slice, one step per stage)

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

## Step N: Release                                  [ ]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; additions marked (CbC). -->

Gate:
- [ ] CHANGELOG entry for the release.
- [ ] README true for a stranger; any commands verified on a clean
      machine.
- [ ] Known issues filed in TODO.md, not just remembered.
- [ ] (CbC) Monitoring/alerts in place — unless observability was a
      recorded exclusion (it was, for checkout-system's
      correctness-portfolio shape; a deployed service should not
      skip it).
- [ ] (CbC) Deploy/rollback procedure documented and tried once —
      same caveat: locally-runnable-only was a recorded exclusion
      there.
Notes:

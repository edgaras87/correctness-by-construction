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
     was not kit-born.
     2026-09-02: rebuilt as a full sequence on the kit's
     playbooks/default.md @ 65dd7ee (ADR-0011) — Steps 0, 1, and N
     vendored from that base, middles unchanged; the old "Release
     additions" section dissolved into the vendored Step N as
     (CbC)-marked gate items.
     2026-09-02 (same day): Step 0's CbC comment reworded — the
     startup snippet is withdrawn and the newborn derives its own
     CLAUDE.md section (ADR-0012).
     2026-09-05: kit steps re-vendored from
     starter/playbooks/default.md v2 @ c670fe5 — their ADR-0031
     moved the playbooks out of the kit, so the vendor path sweeps
     with the refresh. Step 0's first-session comment slimmed to
     kit facts (method's procedure is the bundle's manual's),
     Framing gains the projection gate item, Step N unchanged. -->

# Playbook: CbC run

<!-- The full sequence (ADR-0011). At birth this file is copied
     whole to the run's docs/playbooks/cbc-run.md, and the PLAN
     stub's STEPS region is replaced with everything from the
     first "## Step" down (assembly step 4;
     the install manual's sed, pending its rewrite),
     filling the stub's "Steps from:" line. Ownership per step:
     kit-owned steps carry a vendor line and change only by refresh
     against a new kit pin; (CbC)-marked items and the middle steps
     are this repo's own and change only by harvest (ADR-0007) —
     fold a run's retrospective lessons into this master, never
     into the run's pinned copy alone. -->

Playbook version: v3 (kit steps refreshed from default.md v2
2026-09-05; rebuilt full-sequence 2026-09-02, ADR-0011; created
2026-08-30 middles-only)
Last updated from project: checkout-system 2026-08-27;
safe-reservations (define step) 2026-08-30.

## Step 0: Bootstrap                                [~]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; additions marked (CbC) (ADR-0011). -->

<!-- First session, this step still open: you are bootstrapping.
     The repo, its hygiene commit and the birth entry's pin already
     exist; the gates below are the exit, and they are facts about
     the kit, the same in every birth. How you reach them — a
     briefing, a change-plan, a commit order — is the bundle's, and
     the manual that born you says it (ADR-0031). Two comment kinds
     in every stub: a fill-comment says its content replaces it;
     every other comment is a standing rule and stays. -->

<!-- CbC: the bundle files need no Step 0 decisions of their own —
     the kit's commit split already scopes them: the skills and
     every CLAUDE.md edit are arrangement (agent commits);
     docs/concept/ and docs/playbooks/cbc-run.md are project
     content and land with the records. CLAUDE.md's CbC section is
     the bundle's shipped text, merged at the seed (ADR-0014) —
     never derived per birth. Step 0 runs as assembly: three
     commits per docs/birth-scenario.md, no change-plan — the
     split is fixed there. -->

Goal: the container exists — repo, records, arrangement — before content.
Gate:
- [ ] Repo initialized; hygiene base files present.
- [ ] Every placeholder filled, or explicitly deferred to a named
      step (the stack overlay defers to Framing, which confirms the
      steps that fill or delete it).
- [ ] No fill-comment remains: where a comment says its content
      replaces it, the content is there and the comment is not.
      Every other stub comment is a standing rule — it stays.
- [ ] Briefing committed: README purpose draft + devlog entry (a) —
      names given here may change at Framing; that is what it is for.
- [ ] Agent/project commit split held from the first commit: no
      commit mixes CLAUDE.md / .claude/ with the records.
- [ ] Birth entry in .claude/decisions.md filled: date and the
      copy-time handbook commit.
- [ ] (CbC) The bundle's birth entry beside the kit's in
      .claude/decisions.md: this repo's commit at copy time,
      "pinned to concept v1" — and the correct-birth checklist in
      the install manual passes item by item.
Notes:

## Step 1: Framing                                  [ ]

<!-- Kit step — vendored from starter/playbooks/default.md
     @ c670fe5; additions marked (CbC) (ADR-0011). -->

<!-- CbC: these gates are met via the cbc-framing skill — the
     intent, definition, and adversity registry are the problem
     statement, success criteria, and out-of-scope in the method's
     richer form (ADR-0009). The middle-steps gate item is
     confirmation, not authoring: the steps below came whole with
     this playbook at birth. -->

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
     @ c670fe5; additions marked (CbC) (ADR-0011). -->

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

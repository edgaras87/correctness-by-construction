<!-- The CbC run playbook. At birth, everything from its first
     step down replaces the steps in a newborn's PLAN.md; this
     comment and the version line stay here. Checked against
     concept v1 (ADR-0003, ADR-0005). Harvest lands here, the one
     copy (ADR-0007). Its history — the parent it replaced
     (ADR-0016), the runs its steps were harvested from (ADR-0009,
     ADR-0011), and each version's change and reason — is in the
     devlog and in this file's git log. -->

# Playbook: CbC run — pure

Playbook version: v7 (2026-09-27, provisional; updated here — a
Known already fact about shapes on every step's gate, ADR-0035
decision 4)

## Step 0: Bootstrap                                [~]

Goal: the container exists — repo, records, arrangement — before content.
Gate: derived when this step opens — verifiable facts, from the
goal and the newborn's own records; written into this step before
its work starts.
Known already: `temp/` looked in for shapes staged for this
step, what was found said in one line, nothing included; what the
step made read against every shape governing it.
Notes:

## Step 1: Framing  (cbc-framing)                   [ ]

<!-- CbC: this step opens on the briefing — its starting input,
     the first prompt of project work. The README purpose
     paragraph and the devlog's briefing line land here; names
     given before it are working names. -->

Goal: know what we're building and why, before code.
Gate: derived when this step opens — verifiable facts, from the
goal, the named skill, and the briefing; written into this step
before its work starts.
Known already: `temp/` looked in for shapes staged for this
step, what was found said in one line, nothing included; what the
step made read against every shape governing it.
Notes:

## Step 2: Identity (name, description, remote)     [ ]

Goal: the project's public identity decided, not defaulted.
Gate: derived when this step opens — verifiable facts, from the
goal and the run's own records; written into this step before
its work starts.
Known already: `temp/` looked in for shapes staged for this
step, what was found said in one line, nothing included; what the
step made read against every shape governing it.
Notes:

## Step 3: Ground / infrastructure  (infra-establish)    [ ]

Goal: services stood up, constrained to need, verified both ways.
Gate: derived when this step opens — verifiable facts, from the
goal, the named skill, and the registry; written into this step
before its work starts.
Known already: `temp/` looked in for shapes staged for this
step, what was found said in one line, nothing included; what the
step made read against every shape governing it.
Notes:

## Step 4: Skeleton & bootstrap  (cbc-bootstrap)    [ ]

Goal: an empty but buildable, testable, runnable system wired to the
real ground, with the evidence harness proven on one adversity.
Gate: derived when this step opens — verifiable facts, from the
goal, the named skill, and the registry; written into this step
before its work starts.
Known already: `temp/` looked in for shapes staged for this
step, what was found said in one line, nothing included; what the
step made read against every shape governing it.
Notes:

## Steps 5..N-1: Invariant slices  (cbc-slice, one step per stage)

Goal: each registry slice closed by evidence that creates its
adversity; ordering re-decided at each close, never assumed from
the original expectation.
Gate: derived when each stage opens — verifiable facts, from the
goal, the named skill, and the registry; written into the stage
before its work starts.
Known already: `temp/` looked in for shapes staged for this
step, what was found said in one line, nothing included; what the
step made read against every shape governing it.
Notes:

## Step N: Release                                  [ ]

Goal: the system handed to its audience — the promise shipped,
observable, and reversible wherever it deploys.
Gate: derived when this step opens — verifiable facts, from the
goal, the run's records, and the exclusions framing recorded.
Known already: a CHANGELOG entry for the release; README true for
a stranger, its commands verified on a clean machine; known
issues filed in TODO.md. Checked here: monitoring and alerts in
place; deploy and rollback documented and tried once — each unless
this run's own recorded exclusion.
And `temp/` looked in for shapes staged for this step, what was
found said in one line, nothing included; what the step made read
against every shape governing it.
Notes:

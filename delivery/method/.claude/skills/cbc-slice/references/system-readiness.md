# System Readiness — the contract between CBC Framing and the Invariant Slices

*What must exist before an Invariant Slice can be worked. CBC Framing
hands off TO this checklist. The cbc-slice Agent Skill's Stage 0
checks AGAINST it, at every Invariant Slice. How each item is
satisfied, which store, which language, which test tooling, is
deliberately left open. Standing the system up is project work, not
method work.*

## READINESS-1 — The CBC Framing Exports are in the repo

The three CBC Framing Exports of `.claude/skills/cbc-framing/SKILL.md`
(*Export and handoff*): `docs/system/intent.md`,
`docs/system/definition.md` and `docs/system/registry.md`, the
Invariant Slice Registry with a **`chosen-next` Invariant Slice**.

Why: the cbc-slice Agent Skill's Stage 1 takes the Invariant Slice
Entry *as written*. Without the CBC Framing Exports, there is nothing
to take.

## READINESS-2 — The repo builds, runs, and tests run

A skeleton service exists: it compiles, starts, and an empty or
trivial test suite runs green. No features are required. The surface
is derived later, one Invariant Slice at a time.

Why: an Invariant Slice's Stage 3 must land in a place where code and
tests already run. Toolchain problems met in the middle of an
Invariant Slice fill its record with lines that are not about the
method.

## READINESS-3 — The real store is reachable from tests

The store the enforcement will live in, the one whose constraints are
candidate Structural Walls, is provisioned and reachable from the
test suite, not mocked. Mocks are acceptable elsewhere, never for the
store.

Why: the strongest Structural Walls (unique constraints, atomic
conditional updates) are *how the store behaves*. Evidence against a
mock proves the mock, not the invariant.

## READINESS-4 — The Adversity Harness can create the Adversity Class this Invariant Slice names

Read this Invariant Slice's entry. For **the Adversity Class it
names**, the Adversity Harness must be able to create it:

- **contention:** fire N really concurrent requests at one endpoint,
  in parallel, not quickly one after another;
- **duplicate delivery:** replay a captured request; inject a
  duplicate after a swallowed response; send a request with the same
  key and a different body;
- **partial failure and crashes:** kill the process, or the
  transaction, mid-write, then restart and drive it again.

Only this Invariant Slice's Adversity Class is required. A later
Invariant Slice's is checked at that one's Stage 0. A checklist item
for an adversity no Invariant Slice faces is an empty check.

Why: an Invariant Slice closes only on a test that *creates* its
adversity. If the Adversity Harness cannot create it, the completion
Gate cannot run, and "done" becomes a feeling again.

## READINESS-5 — The Adversity Harness can fail

Test it on itself: break an invariant deliberately, on a branch, by
dropping the constraint or commenting out the guard. Confirm the
Evidence Test goes red, then restore. An Adversity Harness that has
never failed proves nothing when it passes.

The usual first Invariant Slice has no Structural Wall yet to break,
unless standing the system up or a schema it inherited already
carries one. Then this check cannot be answered at Stage 0. It is
answered inside that Invariant Slice's Stage 3 instead: the evidence
has its Red Run with the Structural Wall absent, before the
Structural Wall stands, recorded from actual output. The Invariant
Slice's Gate says so at Stage 1's start. System Readiness is signed
with READINESS-5 owed there.

## READINESS-6 — The CBC Run's records exist

The Invariant Slice Registry is writable. The project's own record
scheme, decided when the system was stood up and not by this method,
has a place for deviations and sign-offs. Each Invariant Slice Close,
and each order decided again, lands there.

## Sign-off

System Readiness is the reviewer's verdict, not a script's. Walk
READINESS-1 to READINESS-6, check each, and record the sign-off: one
line in the Invariant Slice Registry or the project's records, the
date and "ready for SLICE-n". The cbc-slice Agent Skill's Stage 0
asks for this before Stage 1 opens.

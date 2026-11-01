---
name: cbc-slice
description: Work one Invariant Slice of a correctness-driven backend. Take one invariant from the project's Invariant Slice Registry through specify-correctness, plan, build, and document, until a test that CREATES the adversity (concurrent hammering, injected duplicates, kill mid-transaction) proves the invariant survives. Use this whenever the user asks to work, implement, or close a slice, to implement an invariant or an idempotency, contention or recovery guarantee, or to continue a project that has a slice registry (docs/system/registry.md), even if they just say "let's build the next piece". It requires a completed CBC Framing AND a system already stood up: this Agent Skill's Stage 0 checks System Readiness first, and refuses to go on if the system is not ready. Do NOT use for framing a new project (that is the cbc-framing Agent Skill), or for ordinary feature work outside the Invariant Slice Registry.
foundation: concept v1
---

# Invariant Slice — one invariant made real

Carry **one Invariant Slice**, one invariant × its adversity, to
demonstrated evidence. The completion test is single and
non-negotiable: **the test that creates the adversity exists and
passes.** No evidence, no closed Invariant Slice.

This file says what to do at each Agent Skill Stage, and each one's
Gate. `.claude/skills/cbc-slice/references/cbc-slice-workflow.md`
holds what this file does not: the record's outline, why each Agent
Skill Stage runs as it does, and examples. Read it before Stage 1.
`.claude/skills/cbc-slice/references/worked-example.md` Part 2 shows
one Invariant Slice worked end to end.

## The Agent Skill Stages and their Gates

```
Stage 0: ready?  →  1: specify-correctness  →  2: plan  →  3: build  →  4: document
                        (what — no how)         (how)       (real)       (legible)
```

The Invariant Slice Record is written as the Agent Skill Stages go,
in one outline, one Invariant Slice Guarantee Block per Invariant
Slice Guarantee. Which Agent Skill Stage writes which part:
`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *The
Invariant Slice Record's outline*.

## Stage 0 — System Readiness (before anything else)

Read `.claude/skills/cbc-slice/references/system-readiness.md`, and
check it against the actual repo:

1. **READINESS-1:** the three CBC Framing Exports exist under
   `docs/system/` (`intent.md`, `definition.md`, `registry.md`). The
   Invariant Slice Registry names a `chosen-next` Invariant Slice and
   carries the CBC Framing Reconciliation.
2. **READINESS-2:** the repo builds and runs, and the test suite
   executes.
3. **READINESS-3:** the real store is reachable from tests, not
   mocked. Evidence against a mock proves the mock.
4. **READINESS-4:** the Adversity Harness can create **the Adversity
   Class this Invariant Slice names**: concurrency for contention,
   replay or injection for duplicate delivery, killing the process
   for partial failure. Check only what the Invariant Slice needs.
5. **READINESS-5:** the Adversity Harness can fail: a deliberately
   broken invariant turns it red. The usual first Invariant Slice has
   no Structural Wall yet to break. Then READINESS-5 is answered in
   this Invariant Slice's Stage 3, and the Gate says so. It is not a
   blocker here.
6. **READINESS-6:** the Invariant Slice Registry is writable, and the
   project has an agreed place to record deviations and sign-offs.
   The project decides its own record scheme. This Agent Skill only
   requires that one exists.

**Any check fails: stop.** Report exactly what is missing, and what
would satisfy it. Offer to help stand the system up, as ordinary
project work, but do not open Stage 1. An Invariant Slice started on
a system not ready ends with a completion Gate that cannot run, and
"done" cannot be checked.

Signing off System Readiness is the **reviewer's** call. Ask for it
explicitly if it is not already recorded.

## Stage 1 — specify-correctness

1. **Take the invariant from the Invariant Slice Entry, and the
   adversity from the Enemy Census in LAYER-1-ENVIRONMENT, as
   written.** Never invent them again.
2. **Name what CBC Framing does not carry.** An Invariant Slice may
   meet questions CBC Framing never answered:
   - how the thing the invariant is about comes to exist;
   - the conventions of the door the adversity arrives through;
   - what the first schema holds.

   The first Invariant Slice meets most of them. Each is decided at
   Stage 1's start, as a record with its options, before the
   Correctness Specification that depends on it. It is never absorbed
   into code, and never a mechanism: it is still a *what*. One
   recorded as an ADR is **Proposed** until the Invariant Slice
   Close's records, then **Accepted**.
3. **Run the Invariant Slice Guarantee Challenge.** Attack the
   invariant: "what would let this hold on paper yet break in fact?"
   Each distinct answer becomes an Invariant Slice Guarantee, with no
   mechanism in it. Keep attacking until no new answer comes.
4. **Set an Evidence Criterion per Invariant Slice Guarantee:** what
   test would *create* its adversity and show the invariant
   surviving. It is named now, and built in Stage 3.
5. **Tag them** GUARANTEE-n and EVIDENCE-n, numbered once through the
   Invariant Slice Record. Outside the record, each carries its
   Invariant Slice (`.claude/rules/writing.md`, rule 6): "SLICE-4
   GUARANTEE-1", "SLICE-4 EVIDENCE-3 · GUARANTEE-2 · KILL-12". CBC
   Framing's tags (KILL, FOLD, FACT, NOT-OURS, …) are used as CBC
   Framing wrote them.

**Gate:**
1. **Zero mechanisms.** If the Correctness Specification mentions a
   lock, a constraint, a queue, or any technology, a mechanism has
   got into it. Set it aside, and restate it as a property.
2. **Every Adversity Flag on the Invariant Slice Entry is answered by
   name.** An Adversity Flag says the adversity cannot be created the
   normal way. The Correctness Specification says what its evidence
   is instead: created as its own evidence, or removed by a contract
   the Correctness Specification adopts, with the removal shown.
3. **The reviewer signs off the Correctness Specification before
   Stage 2.**

## Stage 2 — plan

1. **One Structural Wall per Invariant Slice Guarantee,** the
   strongest available: the store's refusal (a constraint, a right
   withheld) → type system → single validated entry path → runtime
   check → code review → hope.
2. **Justify each against the named adversity:** "a unique
   constraint defeats duplicate delivery because the second insert
   cannot physically succeed", not "we use a unique constraint".
3. **Where more than one option could hold an Invariant Slice
   Guarantee, put them before the reviewer as a comparison,** with a
   recommendation, the way an ADR presents options. Each option says
   how it holds the Invariant Slice Guarantee, its cost, the size that
   cost assumes, and what would make it worth revisiting.
4. **Run the Escape Hatch Hunt:** admin paths, raw scripts and
   migrations that go around the Structural Wall, checked against the
   System Definition's Trust Assumptions. A writer the System
   Definition trusts is named as trusted, not walled against. A writer
   it never mentions is a question for the System Definition. It is
   answered there by a dated revision, before it is a Structural Wall
   to build.
5. **Name the surface at its minimum:** only what the Invariant Slice
   Guarantees need somewhere to live (the door, the schema, the
   records), and nothing beyond. What enters here without an
   Invariant Slice Guarantee needing it is scope: refuse it, or send
   it back to the Invariant Slice Registry.

**Gate:**
1. **No Invariant Slice Guarantee without its Structural Wall.** Each
   has exactly one, named, with a one-line reason it defeats the
   adversity. "All the code being careful" is the absence of one.
2. **The surface is named.**
3. **The reviewer signs off the plan before Stage 3.**

## Stage 3 — build

1. **Implement the enforcement.** The code should be plain. A comment
   says, in a few lines, what the code relies on that the code cannot
   show, and names its Invariant Slice Guarantee with the Invariant
   Slice ("Holds SLICE-1 GUARANTEE-1"). The argument stays in the
   Invariant Slice Record.
2. **Build the Evidence Tests:** tests that **create** the adversity
   (hammer concurrently, inject the duplicate, kill mid-transaction,
   replay out of order) and show the invariant surviving, one
   Invariant Slice Guarantee at a time. Every State Witness Reading
   after the adversity checks the Falsifiable Promise first, then the
   Invariant Slice's invariant, and only then any exact number.
3. **Give each one its Red Run.** Run it with its Structural Wall
   absent, in a state that never lands in history, and record the
   red from actual output. Then watch the same test, unchanged, go
   green with the Structural Wall standing.
   - How the Structural Wall is made absent is the Invariant Slice's
     choice. When this Invariant Slice builds the Structural Wall, the
     naive version can land first, and the Structural Wall be its own
     diff. When the Structural Wall already stands, remove it on the
     working tree. When the Structural Wall is a rule over the code,
     add the violation it forbids.
   - **A Red Run counts only if it fails on the State Witness.** A
     test that stops on a status, a crash or a setup step before
     reading the state proves it reads statuses. Reorder it, State
     Witness first, and take the Red Run again.
   - A race may need a pause, so that the interleaving the test is
     named for actually happens. The pause lives on the Red Run Tree
     only, the working tree with the Structural Wall absent, and the
     Invariant Slice Record says so.
   - For each Structural Wall removed, note whether its Structural
     Wall Backstop, what stands behind the Structural Wall if it is
     wrong, was seen catching the attack, or is unproven.
   - This is also how READINESS-5 is answered when System Readiness
     had no Structural Wall to break.
4. **Label each test beside itself:** its Evidence Criterion, its
   Invariant Slice Guarantee and its Enemy Collision Kill, with the
   Invariant Slice ("SLICE-4 EVIDENCE-3 · GUARANTEE-2 · KILL-12"), and
   in plain words what it checks and what would trip it. The reasons
   stay in the Invariant Slice Record.
5. **A test that is not evidence says so on itself.**
   - A **Decision Test** guards a decided option, not the Falsifiable
     Promise, and cannot fail for the invariant. It names the
     decision it pins, and where the reasons live.
   - A **Structural Wall Check** sends a Structural Wall its refusal
     directly (the second key inserted, the forbidden write made), or
     reads the Structural Wall where it is defined. It shows the
     Structural Wall stands.
   - Neither discharges an Enemy Collision Kill. **Every Enemy
     Collision Kill still owes a test that had its Red Run.** The Red
     Run decides which kind a test is, not its author.
6. **Record deviations** (below). An Invariant Slice Guarantee the
   build reveals is added to the Correctness Specification, with this
   Invariant Slice as where it came from.

**Gate:**
1. Every Invariant Slice Guarantee has a test that creates its
   adversity.
2. Every such test passes.
3. Each had its Red Run, failing on the State Witness.
4. The Red Run had the Structural Wall absent, in a state that never
   lands in history.
5. The red was recorded from actual output.
6. The same test then went green, unchanged.

A green happy-path suite closes nothing. A test that never had its
Red Run is not known to catch anything.

## Stage 4 — document

1. **Complete the Invariant Slice Record in its outline:** each
   Invariant Slice Guarantee Block gains the tests that prove it, and
   the sections across Invariant Slice Guarantees are finished.
2. **Close the Invariant Slice in the Invariant Slice Registry** as
   `closed (date, evidence)`. The entry went to `in-progress` when
   the Correctness Specification landed, not at the Invariant Slice
   Close. The entry gets one line per item under *Answered at close*:
   - what the Invariant Slice left provisional;
   - what it hands to later Invariant Slices, by name;
   - each Adversity Flag or judgment it settled.

   Each line is the answer in a sentence, and where in the record.
   The reasons stay in the record. Then the order is decided again,
   with its reason written.
3. **Where this Invariant Slice changed how the system is built, add
   or change rows in `ARCHITECTURE.md`'s Invariants table,** as its
   header comment says.
4. **Last, read what the Invariant Slice made against the Output
   Shapes in `.claude/shapes/`:** the method's copies, and any the
   project wrote. This Agent Skill carries none. Where no Output
   Shape governs what the Invariant Slice made, nothing is checked.
   Where one does, each difference is **proposed as a diff, never
   corrected**. How each ends is the shapes-lifecycle Agent Rule's
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*),
   and the reviewer says which.

**Gate:**
1. The Invariant Slice is closed in the Invariant Slice Registry
   with its answers, what it left provisional and what it hands on,
   one line each.
2. The order is decided again, in writing.
3. `ARCHITECTURE.md`'s rows match what the Invariant Slice built.
4. The Invariant Slice Record has been read against the project's
   Output Shapes, each difference ended as the shapes-lifecycle Agent
   Rule says
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*).

## Deviations — legal, never silent

Departing from the Correctness Specification, the plan, or this
workflow is allowed. Departing silently is not. Every deviation is
recorded in the project's own record scheme: where, what was done
instead, and why.

## Standing Guards (mention at close)

At the Invariant Slice Close, remind the reviewer of the three
Standing Guards, each named by the failure it watches for: System
Guarantee Erosion, Testing Theater and Escape Hatch
(`.claude/skills/cbc-slice/references/cbc-slice-workflow.md`, *Standing Guards*).

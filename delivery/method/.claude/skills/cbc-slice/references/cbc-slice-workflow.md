# Invariant Slice workflow — the outline, the why, the examples

*SKILL.md says what to do at each Agent Skill Stage, and each one's
Gate. This file holds only what SKILL.md does not: the Invariant Slice Record's
outline, why each Agent Skill Stage runs as it does, and worked
examples. Each section names the Agent Skill Stage it serves.*

*`.claude/skills/cbc-slice/references/worked-example.md` beside this
file follows `.claude/skills/cbc-framing/references/worked-example.md`,
which owns it. An edit lands there first, then here, word for word.*

---

## The unit

An Invariant Slice is one invariant × one adversity, carried all
the way to passing evidence. Not a feature, not an endpoint, not a
ticket.

```
specify-correctness  →  plan  →  build  →  document
     (what)             (how       (make      (make it
                        chosen)    it real)   legible)
```

The first boundary matters most: **what** must be true is settled
completely before any **how** is allowed in. Mixing them is the usual
failure. A mechanism named early is taken for a property, and the
alternatives are never weighed against the actual requirement.

---

## The Invariant Slice Record's outline

One Invariant Slice Record per Invariant Slice, written as the Agent
Skill Stages go. This is the minimum every Invariant Slice Record needs: where each
Agent Skill Stage's output goes, and one Invariant Slice Guarantee
Block per Invariant Slice Guarantee. The Invariant Slice Record
Shape, in `.claude/shapes/`, adds to it and says how each part reads.
It is read at the Invariant Slice's Plan Step Gate, never while writing. Beside
each part, the Agent Skill Stage that writes it.

```
# SLICE-<n> — <the invariant in a few words>

## Invariant                                  Stage 1
## Adversity                                  Stage 1
   what attacks it, and how the evidence creates it, for every
   Invariant Slice Guarantee alike
## Decided before the Correctness Specification   Stage 1's start, where something was
## Guarantees
### SLICE-<n> GUARANTEE-<k>. <the claim>       one Invariant Slice Guarantee Block per Invariant Slice Guarantee:
   the attack, and what we guarantee          Stage 1
   its Evidence Criterion                     Stage 1
   what holds it, and what stands behind it   Stage 2
   the options weighed                        Stage 2
   the tests that prove it                    Stage 4
## Folds and flags                            Stage 1: each one the Invariant Slice Registry handed over, answered
## What this Invariant Slice does not claim   Stage 1
## The plan, across guarantees                Stage 2: what the Structural Walls need, the Escape
                                              Hatch Hunt, the surface, the Red Run as planned,
                                              the deviations, and what is left provisional
## Evidence, as delivered                     Stages 3 and 4: the suite, the tests beside
                                              the evidence, the Red Runs, what the build found
## Standing Guards                            Stage 4
## Sign-offs                                  the reviewer's, one per Agent Skill Stage
```

What spans every Invariant Slice Guarantee has its own section. What
belongs to one is in its Invariant Slice Guarantee Block, and nowhere else: the claim is
written once, at the top of its Invariant Slice Guarantee Block. An Agent Skill Stage that adds
to an Invariant Slice Guarantee Block adds to that one. It does not open a section of its
own.

---

## Stage 1 — why, and an example

*Question: what must hold, against what, and what would proof look
like?*

**Taken as written, from CBC Framing.** The Enemy Collision Kill
arrived shaped as an invariant from the cbc-framing Agent Skill's
Stage 3. Using it is the handoff. The worked example's invariant:
"N arrivals of one submission → exactly one recorded order." The
adversity is taken from the Enemy Census in LAYER-1-ENVIRONMENT, not
invented: contention, duplicate delivery, crashes and partial
failure, reordering. "Correct" means nothing until it says correct
*against what*.

**What CBC Framing does not carry is still a what.** "An order exists
once it is recorded, never while it is being accepted" names no
table. Absorbing such a decision into code is the silent decision
this workflow forbids. An ADR for it stays Proposed until the
Invariant Slice Close, because the build can still reshape it. A
Proposed record is corrected in place. An Accepted one could only be
superseded.

**Why every Adversity Flag is answered.** An Adversity Flag left
unanswered is a warning the Invariant Slice inherited and dropped.

**Invariant Slice Guarantees are derived by attack, never looked
up.** This middle step is the real work, and textbook examples skip
it. For the order example, the attack yields: uniqueness of the key;
a winner and a loser under concurrency; safe replay of the winner's
response; correct key scope. Each says what must hold, not how.

The output is the **Correctness Specification**: invariant →
Invariant Slice Guarantees → Evidence Criteria, plus the Adversity
Model. The Adversity Model is the part that says what attacks and how
the evidence creates it: the Invariant Slice Record's *Adversity*.

## Stage 2 — why

*Question: what structure makes each Invariant Slice Guarantee
impossible to violate?*

**"All the code being careful" is a design defect,** raised before
implementation, not discovered after.

**Why the comparison, and why the size.** Options named in a
paragraph after the choice are not weighed: the reviewer reads past
them, and asks afterwards whether alternatives existed. The sign-off
is only real if the alternatives were in front of the reviewer. And
a cost is true at some size. Read it from the size the System
Definition says the system is built for, where it says one: an
option chosen at one size can lose at another.

**Why a trusted writer is not walled against.** Any path that goes
around the Structural Wall makes the Invariant Slice Guarantee
false, so every write path goes through the Structural Wall. Why a
writer who can remove the Structural Wall is trusted instead:
(`.claude/skills/cbc-framing/references/cbc-framing-workflow.md`, *Stage 2 — Name the enemies…*).

**Why the surface is minimal.** The door exists because the
invariant needs one, and an Invariant Slice is not a feature.

## Stage 3 — why

*Question: does the invariant actually survive the adversity?*

**Plain code.** The thinking already happened. Surprising cleverness
here usually means Stage 1 or 2 was skipped.

**Create, don't sample.** A test that runs one request at a time is
not evidence for an Invariant Slice Guarantee against contention. The evidence must create the
adversity the Correctness Specification names.

**Why the Falsifiable Promise is read first.** A test that checks
only the numbers it expected passes when the Falsifiable Promise
breaks in a way it did not foresee.

**Why the race's pause stays on the Red Run Tree.** The evidence as
committed runs without it, so what is committed is what runs.

**Why the Structural Wall Backstop is noted at the Red Run.** The Red
Run is the one moment the Structural Wall Backstop meets the attack.
One not seen there is recorded as unproven, never assumed.

**Why each test is labelled beside itself.** A reader who lands on a
test should not have to rebuild its purpose from its assertions. The
reasons (why this option, why this form) stay in the Invariant Slice
Record, or the two drift apart and neither can be trusted.

**Why a Decision Test is kept, and why it counts for nothing.** It
goes red only when someone changes, by hand, something the Invariant
Slice chose on purpose. That is worth keeping: when it goes red, it
tells whoever changed that choice that it was made on purpose. But a
test that cannot be made red by removing the Structural Wall it
claims to guard is not evidence, whatever it is called.

**Why the Structural Wall Check.** It proves the Structural Wall
stands before any path relies on it. It notices a Structural Wall
dropped "for a while" before any Evidence Test samples around the
gap. It creates no adversity, so it is not evidence.

## Stage 4 — why

*Question: can a stranger see what is promised, and why to believe
it?*

**The Invariant Slice Record is the Invariant Slice's visible
product.** In this discipline, how deep the Invariant Slice Guarantees go is what is
shown, not the feature.

**Why the Invariant Slice Close writes its answers.** A built
Invariant Slice can teach that the next expected one is wrong, split
or unnecessary. The Invariant Slice Registry can only decide again
on what the Invariant Slice Close wrote down. Examples of what an Invariant Slice Close hands on:
- a Structural Wall that already holds part of a later invariant;
- a counter that counts more than are live, until a later Invariant
  Slice makes them end;
- a choice a later Invariant Slice must make.

And an Invariant Slice Registry that reads `chosen-next` through a
whole build is not the source of truth for what is being worked.

**Why `ARCHITECTURE.md` gains rows, not paragraphs.** It answers
what a later Invariant Slice may rely on now, so it stays short and
current. What a row holds is the Invariants section's own comment, in
`ARCHITECTURE.md`.

**Why the Output Shapes are not in this Agent Skill.** They arrive
with the method as copies in `.claude/shapes/`: the Invariant Slice
Record Shape, the Evidence Test Shape, the Enemy Collision Kill Shape
and the Invariant Slice Entry Shape. The project changes them, or
writes its own, as the shapes-lifecycle Agent Rule says
(`.claude/rules/shapes-lifecycle.md` §1, *Written from work that exists*).
An Output Shape inside this Agent Skill would be read while the
Invariant Slice Record is written, and the Invariant Slice Record would follow it instead of showing
where it is wrong. Whether an output is worth a new Output Shape is a
judgment the project makes when it makes that output, not a step of this
Invariant Slice Close. An Output Shape is read only at the Invariant Slice Close, for reasons the shapes-lifecycle Agent Rule gives
(`.claude/rules/shapes-lifecycle.md` §2, *Where an Output Shape lives*).

---

## Standing Guards

After the Invariant Slice Close, three Standing Guards stay, each
named by the failure it watches for:

- **System Guarantee Erosion:** any later feature touching this
  Invariant Slice's state checks this Correctness Specification again
  before shipping. New surface is new attack surface against your own
  Structural Walls.
- **Testing Theater:** a Structural Wall may weaken over time, a
  constraint dropped "temporarily", a type loosened, until only the
  test remains. Then the Invariant Slice Guarantee has silently moved
  from structure to sampling. Structure forbids; tests only sample.
- **Escape Hatch:** every new admin path or script is checked against
  the Structural Walls it might go around.

## Working defaults

Two choices are working defaults, overridable with a recorded
reason:

- **Proving and verifying live inside the build:** Evidence Tests are
  Stage 3's second move, with no separate Gate between Stage 3 and
  Stage 4.
- **The Correctness Specification is prose under fixed headings**
  (*Invariant*, *Adversity*, *Guarantees*, each with its Evidence Criterion), one per
  Invariant Slice. Structure enough to diff, prose enough not to fix
  a schema in advance.

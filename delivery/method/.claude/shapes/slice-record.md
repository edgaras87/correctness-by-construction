---
foundation: practice, under the shapes convention
---

# The Invariant Slice Record Shape

**Governs:** how an Invariant Slice Record is laid out, and how each
Invariant Slice Guarantee Block is written. Their form, never their
content: what an Invariant Slice Guarantee says comes from the
attack, and what holds it comes from the plan.

<!-- An Output Shape: what a kind of output looks like, its form and never
     its content. Read at an Invariant Slice's Plan Step Gate, never
     while the record is written. How Output Shapes live is
     .claude/rules/shapes-lifecycle.md, and not repeated here. -->

## What this document controls

**The record's order, and the form of an Invariant Slice Guarantee
Block.** A block this Output Shape accepts can still hold the wrong
Invariant Slice Guarantee. That is the attack's business, and the
Correctness Specification's. Every other section is the Invariant
Slice's own, as long as it needs.

**Two layers, marked apart.** *Skeleton:* the order and the block,
what any project's Invariant Slice Records would want.
*Illustration:* one block filled in, from the method's worked
example, a tiny order service. A project takes the skeleton and
writes its own illustration.

## The record's order

1. **Invariant.** What the Invariant Slice protects, in one statement.
2. **Adversity.** What attacks it, and how the evidence creates it,
   for every Invariant Slice Guarantee alike.
3. **Decided before the Correctness Specification,** where something
   was.
4. **Guarantees.** One block per Invariant Slice Guarantee, below.
5. **Folds and flags:** the Invariant Slice Folds and Adversity
   Flags the Invariant Slice Registry handed this Invariant Slice,
   each answered.
6. **What this Invariant Slice does not claim.**
7. **The plan, across guarantees:** what the Structural Walls need
   (or what stands already), the Escape Hatch Hunt, the surface, the
   Red Run as planned, the deviations, and what is left provisional.
8. **Evidence, as delivered:** the suite as a whole, the tests
   beside the evidence that are not evidence, the Red Runs, and what
   the build found that the Correctness Specification had not.
9. **Standing Guards:** what keeps the Invariant Slice Guarantees
   true after the Invariant Slice Close.
10. **Sign-offs.**

What spans every Invariant Slice Guarantee has its own section. What
belongs to one is in its block, and nowhere else.

## An Invariant Slice Guarantee Block

The block grows by Agent Skill Stage, the cbc-slice Agent Skill's.
Stage 1 writes the claim, the attack and the Evidence Criterion.
Stage 2 adds what holds it and the options weighed. Stage 4 adds the
tests, at the Invariant Slice Close. The reviewer signs an Agent
Skill Stage by reading the parts it added.

*Skeleton:*

```markdown
### SLICE-<n> GUARANTEE-<k>. <the claim, condition first (a when,
while or if clause, or the condition as the subject), then what a
test can see happen>

*What could go wrong (the attack):* <what would let the invariant
hold on paper and break in fact>
*Say:* <real numbers from this system>

*What we guarantee:* <the property that answers it>
*Say:* <the same numbers, carried through>

*Kills:* KILL-<n>

- **EVIDENCE-<m> (GUARANTEE-<k>).** <the adversity the test creates,
  and what the State Witness must read after it>

*The wall:* <the Structural Wall, named: a constraint, a statement,
an absence with the test that guards it>
*Why it beats this attack:* <against the named adversity, not
adversity in general>
*Say:* <real numbers>
*If the wall were ever wrong:* <the Structural Wall Backstop, named,
or nothing, said so; and "seen catching at the Red Run", with the
Red Run taken again with it absent too, or "unproven">

*Options weighed:*

**<the option chosen>** — *chosen*
*How it holds it:* <how>
*Cost:* <what choosing it costs>
*Assumes:* <the size that cost is true at, and what would make the
option worth revisiting>

**<an option not chosen>**
*How it would hold it:* <how>
*Why not:* <why it lost, against the named adversity>

*Proven by:*

| Criterion | Test | The adversity it creates |
|---|---|---|
| EVIDENCE-<m> · GUARANTEE-<k> | `<Class.method>` | <what it does, with the Enemy Collision Kill it answers> |

---
```

*Illustration, from the worked example's SLICE-1:*

```markdown
### SLICE-1 GUARANTEE-1. When identical submissions with one key
race, the store holds one order for that key

*What could go wrong (the attack):* two submissions with one key
each find no order yet, and each records one.
*Say:* fifty identical submissions released at one instant; the
store holds two orders for the key, or fifty.

*What we guarantee:* a key never maps to two orders.
*Say:* fifty released at one instant; the store holds one order for
the key.

*Kills:* KILL-2

- **EVIDENCE-1 (GUARANTEE-1, GUARANTEE-2).** Fifty identical
  submissions released at one instant through the door; the State
  Witness, the store's count of orders for the key, reads 1.

*The wall:* the store's unique constraint on the key.
*Why it beats this attack:* the second insert with a key cannot
succeed, however the racers interleave.
*Say:* of fifty inserts racing on one key, one succeeds and
forty-nine are refused.
*If the wall were ever wrong:* nothing stands behind it, said so.

*Options weighed:*

**The store's unique constraint on the key** — *chosen*
*How it holds it:* the store refuses a second row with the key.
*Cost:* one index on the key.
*Assumes:* one shop's orders, up to ten thousand, each key kept for
life; worth revisiting if keys must expire.

**Look for the key first, then insert**
*How it would hold it:* the service checks for an order with the
key, and records one only if none is found.
*Why not:* two racers both find none, then both insert; it fails the
named adversity, simultaneous duplicates.

*Proven by:*

| Criterion | Test | The adversity it creates |
|---|---|---|
| EVIDENCE-1 · GUARANTEE-1 | `<the hammering test>` | fifty submissions at one instant, KILL-2 |

---
```

### Rules for the parts

- **The claim is written once,** at the top of its block. No other
  section restates it.
- **The claim says what happens to what,** in this system's nouns:
  the condition first where there is one, as a clause or as the
  subject ("A refused change moves nothing"), then the outcome a
  test can see. No abstract noun standing for the mechanism
  ("nonsense", "the truth").
- **A `*Say:*` line is owed wherever a mechanism is involved,** and
  not forced where the claim is concrete without one. An option
  carries none: the chosen one's numbers are in *The wall*, and a
  rejected one was never run.
- **Options are weighed where this Invariant Slice made the
  choice.** Where the Structural Wall already stood, the block names
  where its options were weighed ("in SLICE-1 GUARANTEE-1's block")
  instead of weighing them again.
- **The chosen option comes first and says so.** Every option
  answers the same questions under the same labels, so options are
  weighed by reading down, not across.
- **A cost says the size it is true at.** An option chosen at one
  size can lose at another. *Assumes:* is where a later reader finds
  when to look again.
- **An Evidence Criterion is a list item,** so it can hold
  sub-points and name more than one Invariant Slice Guarantee
  ("EVIDENCE-1 (GUARANTEE-1, GUARANTEE-2)"). The table names the
  Evidence Criterion beside each test, since one can serve two
  Invariant Slice Guarantees.
- **A Structural Wall Backstop says whether it was seen.** The Red
  Run removes the Structural Wall, and that is the one moment the
  Structural Wall Backstop meets the attack. One never seen there is
  written "unproven". One that caught the attack is named, and the
  block says the Red Run was taken again with it absent too.
- **An option changed after the plan was signed keeps its dates.**
  The new choice comes first, marked `*chosen <date>*`. The one it
  replaced moves below, marked `*as signed on <date>*`, and answers
  under `*Why not, on revision:*`.
- **Blocks are separated by a `---` line.**

## What is exempt, and why

- **Lookup tables:** Enemy Collision Kill to Invariant Slice,
  Evidence Criterion to test, a records index. A table row is one
  line in the file, so its cells stay short. A row of prose hundreds
  of characters long cannot be read in an editor, and a diff marks
  it whole when one word changes.
- **Lists of single claims:** what the Invariant Slice does not
  claim, the Standing Guards.

## What to check at a close

Read the record and ask:

1. Does it follow the record's order, with what spans Invariant
   Slice Guarantees in its own sections?
2. Is each Invariant Slice Guarantee one block, its parts in order,
   and no part of it elsewhere?
3. Is each claim written once, condition first, saying what a test
   can see?
4. Does every chosen option come first, with its cost and the size
   that cost assumes?
5. Does every Structural Wall Backstop say whether it was seen at
   the Red Run?
6. Where the record differs from this Output Shape: did it drift, was the
   Output Shape wrong, did each have something, or is it a different kind?
   How each ends is the shapes-lifecycle Agent Rule's
   (`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*).

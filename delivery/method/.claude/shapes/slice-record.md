---
foundation: practice, under the shapes convention
---

# The shape of a slice record

**Governs:** how a slice record is laid out, and how each
guarantee's block is written. Their form, never their content: what
a guarantee says comes from the attack, and what holds it comes from
the plan.

<!-- A shape: what a kind of output looks like, its form and never
     its content. Read at a slice's closing gate, never while the
     record is written. How shapes live is
     .claude/rules/shapes-lifecycle.md, and not repeated here. -->

## What this document controls

**The record's order, and the form of a guarantee's block.** A
block this shape accepts can still hold the wrong guarantee; that
is the attack's business, and the specification's. Every other
section is the slice's own, as long as the slice needs.

**Two layers, marked apart.** *Skeleton:* the order and the block,
what any project's slice records would want. *Illustration:* one
block filled in, from the method's worked example, a tiny order
service. A project takes the skeleton and writes its own
illustration.

## The record's order

1. **Invariant.** What the slice protects, in one statement.
2. **Adversity.** What attacks it, and how the evidence creates it,
   for every guarantee alike.
3. **Decided before the specification,** where something was.
4. **Guarantees.** One block per guarantee, below.
5. **Folds and flags:** what the registry handed this slice, each
   answered.
6. **What this slice does not claim.**
7. **The plan, across guarantees:** what the walls need (or what
   stands already), the escape hatches hunted, the surface, the red
   as planned, the deviations and provisionals.
8. **Evidence, as delivered:** the suite as a whole, the tests
   beside the evidence that are not evidence, the red runs, and what
   the build found that the specification had not.
9. **Standing guards:** what keeps the guarantees true after the
   slice closes.
10. **Sign-offs.**

What spans every guarantee has its own section. What belongs to one
guarantee is in its block, and nowhere else.

## A guarantee's block

The block grows by stage. The specification writes the claim, the
attack and the evidence criterion. The plan adds what holds it and
the options weighed. The close adds the tests. The reviewer signs a
stage by reading the parts it added.

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
  and what the witness must read after it>

*The wall:* <the wall, named: a constraint, a statement, an absence
with the test that guards it>
*Why it beats this attack:* <against the named adversity, not
adversity in general>
*Say:* <real numbers>
*If the wall were ever wrong:* <what stands behind it, or nothing,
said so; and "seen at the red run" or "unproven">

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
| EVIDENCE-<m> · GUARANTEE-<k> | `<Class.method>` | <what it does, with the kill it answers> |

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
  submissions released at one instant through the door; the witness,
  the store's count of orders for the key, reads 1.

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
- **Options are weighed where this slice made the choice.** Where
  the wall already stood, the block names where its options were
  weighed ("in SLICE-1 GUARANTEE-1's block") instead of weighing
  them again.
- **The chosen option comes first and says so.** Every option
  answers the same questions under the same labels, so options are
  weighed by reading down, not across.
- **A cost says the size it is true at.** An option chosen at one
  size can lose at another; *Assumes:* is where a later reader finds
  when to look again.
- **An evidence criterion is a list item,** so it can hold
  sub-points and name more than one guarantee ("EVIDENCE-1
  (GUARANTEE-1, GUARANTEE-2)"). The table names the criterion beside
  each test, since one criterion can serve two guarantees.
- **A backstop says whether it was seen.** The red run removes the
  wall, and that is the one moment the backstop meets the attack. A
  backstop never seen there is written "unproven".
- **An option changed after the plan was signed keeps its dates.**
  The new choice comes first, marked `*chosen <date>*`. The one it
  replaced moves below, marked `*as signed on <date>*`, and answers
  under `*Why not, on revision:*`.
- **Blocks are separated by a rule** (`---`).

## What is exempt, and why

- **Lookup tables:** kill to slice, criterion to test, a records
  index. A table row is one line in the file, so its cells stay
  short. A row of prose hundreds of characters long cannot be read
  in an editor, and a diff marks it whole when one word changes.
- **Lists of single claims:** what the slice does not claim, the
  standing guards.

## What to check at a close

Read the record and ask:

1. Does it follow the record's order, with what spans guarantees in
   its own sections?
2. Is each guarantee one block, its parts in order, and no part of
   it elsewhere?
3. Is each claim written once, condition first, saying what a test
   can see?
4. Does every chosen option come first, with its cost and the size
   that cost assumes?
5. Does every backstop say whether it was seen at the red run?
6. Where the record differs from this shape: did it drift, was the
   shape wrong, did each have something, or is it a different kind?
   The shapes rule says how each ends.

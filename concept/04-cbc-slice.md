# The Invariant Slice

The second part of the work, and the unit of construction: **one
invariant made real, end to end.** Not a feature, not a screen, not a
sprint's worth of tickets — one System Never-Event from the System
Guarantee Inventory, taken from specification to a Structural Wall,
proven to survive its specific attack. This chapter describes what an
Invariant Slice is. The procedural detail of working one is left
outside the concept.

## Why the invariant is the unit

Cutting by invariant keeps the derivation direction intact all the way
into code. Every unit of work is a System Guarantee becoming
enforceable. The feature surface grows only as a side effect, where a
System Guarantee needs somewhere to live. Cutting work by feature
brings back the order the discipline exists to reverse: features
first, correctness later.

An Invariant Slice is *closed* when its invariant demonstrably survives
the adversity that attacks it. Closed means the question is over: the
Structural Wall stands, the proof exists, and later work is allowed to
build on it without re-arguing it.

## The four phases

**Specify.** State what must hold and what attacks it — the invariant and
its named adversity, taken from CBC Framing. No mechanisms. A
specification that says "use a unique constraint" has answered the next
phase's question in this one. The mechanism was then chosen before the
requirement was fully stated.

**Plan.** Choose the mechanism, and say why it beats *that* attack,
not why it is good in general. The Structural Wall is picked from the
ranking of Structural Walls, the strongest available; choosing a weaker Structural
Wall than possible is a decision that needs a stated reason.

**Build.** The mechanism, plus the proof: a test that ***creates* the
attack** and shows the invariant surviving. It hammers the endpoint
concurrently, injects the duplicate, or kills the process mid-write. This test is the
defining deliverable of the Invariant Slice, and the one most projects
skip. An attack-creating test is different in kind from a correctness
test. It doesn't check that the code does the right thing: it creates
the hostile world and checks that the wrong thing has become impossible.

**Document.** The claim and its proof, kept readable: what is promised,
what Structural Wall holds it, and how it was shown to survive. The
Invariant Slice then stays closed for a reader months later, not just
for the person who built it.

## The proof standard

Structure forbids; tests sample. The Invariant Slice does not pretend
otherwise. The attack-creating test is not the Structural Wall; it is
the *demonstration that the Structural Wall exists*. If the Structural
Wall is ever weakened and only the test remains, the System Guarantee
has silently moved from structure to sampling. The Invariant Slice is
then no longer closed, whatever the test suite says.

## Invariant Slices and the whole

The Invariant Slice Registry orders the Invariant Slices, but the
ordering is re-decided as evidence arrives. A built Invariant Slice is
allowed to teach that the next expected one is wrong, split, or
unnecessary. And a closed Invariant Slice is not immune to the future:
a later change touching the state it governs re-opens the question of
whether its Structural Wall still holds. Closed means proven, not
forgotten.

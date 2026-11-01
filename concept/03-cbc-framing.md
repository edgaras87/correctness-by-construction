# CBC Framing

The first part of the work: turning an idea into a defined system — on
paper, before any code and before any technology choice. CBC Framing
ends when the Falsifiable Promise is stated, the world is described,
ownership is settled, and the work is cut into Invariant Slices. This
chapter describes *what CBC Framing is*. The procedural detail of
running it is deliberately left outside the concept.

## Why paper first

The cheapest place to find a design flaw is a description, not a codebase.
But CBC Framing is not "write a design doc": a blank page prescribes
nothing. CBC Framing is a fixed sequence of questions, each of which
produces the input the next one needs. Skipping ahead doesn't save time;
it produces answers to questions that weren't well-posed yet.

## The derivation order

CBC Framing starts from the Falsifiable Promise, because the
Falsifiable Promise is the filter every other question needs. The
Layered System presents outside-in: environment first, then the
system, then its interior. CBC Framing does **not** derive in that
order:

**Choose the Falsifiable Promise.** One sentence, one claim,
falsifiable, worth proving, for a named audience. A candidate
Falsifiable Promise that is really a feature is rejected. A second
genuine purpose means the CBC Framing Intent, the document that
states the Falsifiable Promise, is overloaded, and one must be chosen. This is the hardest
step. Everything else is downstream of it.

**Decide what must be ours.** For each candidate fact or responsibility,
one test: *if someone else owned this, could they break our Falsifiable
Promise?* Yes means it's a System Possession. No means it's refused —
deliberately, as a decision, not a leftover. This fixes the system's
authority and boundary.

**Take the Enemy Census.** Follow one request through its whole life.
Everything beyond the system's control is an actor. For each: can it
vanish, duplicate, or lie? The Enemy Census collects Enemy Facts,
attackable facts, not generalities. It is done not when it feels complete but when fresh
attempts to attack the list stop finding anything new.

**Run the Enemy Collisions.** Each Enemy Fact against each System
Possession: what dies? The output names the **Enemy Collision Kill**,
never the cure: "a retry lands twice and the order exists twice," not
"add an idempotency key." Mechanisms chosen here would be mechanisms
chosen before the problem is understood.

**Sort into Responsibility Areas — only if forced.** If the Enemy
Collisions genuinely demand separate owners, partition; if one owner
covers everything, that is a confirmed answer. Then, and only if there
is more than one Responsibility Area, examine the seams between them
for the correctness no single owner can hold.

**Cut into Invariant Slices.** The Enemy Collisions become an Invariant
Slice Registry, each Invariant Slice one invariant to be made real. The
Invariant Slice Registry's ordering is an expectation, not a commitment; evidence from
built Invariant Slices is allowed to reorder what remains.

## Why this order and not the layers'

The Falsifiable Promise comes first because "ours or not ours" is
unanswerable without it. The Enemy Census comes before the interior
partition. The partition should be *forced by Enemy Collisions*, not
sketched from intuition: Responsibility Areas invented before the
adversity is known are org charts, not ownership. The two changes of
order,
the Falsifiable Promise before the environment and the Enemy Collisions
before the Responsibility Areas, are what make CBC Framing a derivation
instead of a documentation exercise.

## What CBC Framing produces

Three CBC Framing Exports, whatever their recorded form: the **CBC
Framing Intent** (the Falsifiable Promise and the purposes refused), the
**System Definition** (authority, boundary, adversary, owners), and the
**Invariant Slice Registry** (the work, cut into invariants). Nothing in
them names a language, a store, or a framework. Technology arrives only
after CBC Framing, each choice answerable to the Invariant Slice
Registry it must serve, never the other way around.

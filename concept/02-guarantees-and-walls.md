# System Guarantees and Structural Walls

What the discipline actually produces: not documents, which only
carry them, but *objects*, whatever their recorded form. Five of them, in
dependency order, and then the hierarchy that decides whether a System
Guarantee is real.

## The Falsifiable Promise

A short, human-readable, **falsifiable** statement of what the system is
answerable for. One sentence, one claim, for a named audience.

Falsifiable is the word that matters: you can construct, concretely, the
scenario in which the Falsifiable Promise is broken. *"One submission
becomes exactly one recorded order, no matter how many times it
arrives"* is a Falsifiable Promise: you can picture the duplicate
slipping through. *"A reliable order platform"* is a mission
statement: nothing could ever count as breaking it, so nothing can be derived from
it.

## The described adversary

The environment's ways of being hostile, written as attackable facts:
what can vanish, duplicate, or lie, plus the assumptions explicitly
accepted as trust rather than defended against. It is what the
Falsifiable Promise is defended against. Without it, the System
Guarantees below have nothing to be tested against.

## The System Guarantee Inventory

The Falsifiable Promise's negation space: the small set of System
Never-Events, each meaningful against a named adversity. "The same
submission is never recorded twice — *against* retries and duplicated
deliveries." A System Never-Event with no named adversary is a slogan;
one with no relation to the Falsifiable Promise is scope creep
presented as safety.

Small is the aim. The System Guarantee Inventory is the few
invariants whose violation is expensive or irreversible. That is
where the rigor goes.

## The ownership map

For every fact, one owner; for every System Guarantee, one **Structural
Wall**. The Structural Walls, ranked strongest to weakest:

    the store's refusal
      (a constraint, a right withheld)
    → type system
    → single checked entry path
    → runtime check
    → code review
    → hope

Each System Guarantee is assigned exactly one Structural Wall, the
strongest available. The ranking is a hierarchy of *who can violate
it*:

- the store's refusal binds every code path ever written, including
  future ones;
- the type system binds everything that compiles;
- a single checked entry path binds everything that goes through the
  door;
- a runtime check binds only the paths that reach it;
- code review and hope bind no one.

Every Structural Wall leaves someone unbound: whoever can remove it.
The store's owner can drop a constraint or grant a right back; a
single checked entry path binds only while nothing writes around the
door. So the
described adversary says who besides the system may write what it
stores, trusted or defended against. Each Structural Wall is assigned
against that answer. A single checked entry path is a Structural
Wall only where the assumptions accepted as trust name it the only
writer; elsewhere "single" is a hope.

The store refuses by withholding as well as by checking. An identity
that holds no right to an operation is refused it on every path that
uses that identity. That is the strongest Structural Wall for an
operation that must never happen.

"All the code being careful" is not a Structural Wall. It is the
absence of one. A System Guarantee whose owner is carefulness is a
design defect, flagged before implementation, not discovered after.

## The derived surface

The feature set comes out of the design, as an *output*. Each feature carries its justification
against the Falsifiable Promise: it exists because some commitment cannot
be kept without it. A feature that cannot say which System Guarantee it
serves is a candidate for refusal, and refusals are decisions worth
stating, not omissions.

## The stance underneath: prevented, not detected

Running through all five objects is one inherited conviction: errors should
be *prevented by structure*, not found by search. Tests sample; structure
forbids. A test can show the invariant surviving one attack; only a
Structural Wall makes the attack meaningless. This is why a System
Guarantee moving out of the store's refusal and into a test suite is
a loss even when the test is green. The System Guarantee has moved
from structure to sampling.

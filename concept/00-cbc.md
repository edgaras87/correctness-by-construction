# Correctness-by-construction

*The main document. Read this first. The other chapters go deeper:
the Layered System, System Guarantees and Structural Walls, CBC
Framing, and the Invariant Slice.*

## In one sentence

A system is what it promises about a hostile world; design is the
derivation, in dependency order, of the structures that make breaking that
promise impossible — and of nothing else.

## The CBC Inversion

This discipline asks ***"what must never happen?"*** first. Most
software is designed the other way, by asking *"what should it do?"*
and listing features. Correctness, if it appears at all, is added
afterwards as a quality attribute: tests, monitoring, bug fixes.

Money counted twice. An order created twice. A stale answer shown as
fresh. From those System Never-Events, everything else is derived:

- **System Guarantees** are the System Never-Events, each stated
  against a named source of adversity.
- **Structure** is derived from the System Guarantees: each System
  Never-Event gets one Structural Wall that makes it *impossible*, not
  merely detected.
- **Features** come last, as the minimal surface needed to keep the
  Falsifiable Promise real.

The direction of derivation is the whole point:

    world → Falsifiable Promise → System Guarantees → structure → features → code

never the reverse. A feature list is an *output* of the design, not its
input.

One corollary follows immediately: the surface stays deliberately
**feature-thin**. Every feature added is new attack surface against the
system's own System Guarantees. The depth of the System Guarantees is
the visible product. Staying small is discipline, not taste.

## What kind of thing this is

It is a *design discipline* — not a process framework, and not a technique.
The distinction decides what counts as following it:

- A **technique** ("use database constraints") can be applied locally
  without changing how you think. The discipline cannot. Its unit is
  the *ordering of questions*. It is violated by asking them out of
  order, even when every individual answer is good.
- A **process framework** prescribes activities, roles, artifacts, cadence.
  The discipline prescribes none of these. Any form that records the
  answers in dependency order satisfies it; any that doesn't, doesn't.

Its nearest relative is test-first development: a small inversion of
question order that, held consistently, reorganizes everything downstream
of it.

## The two components

The discipline has exactly two components, and is defined by the two
together:

**The world model — the Layered System.** A containment description of
reality. It has five layers:

1. a hostile environment;
2. inside it, a system making one Falsifiable Promise;
3. inside that, a partition into Responsibility Areas;
4. inside each Responsibility Area, problems small enough to close;
5. between the Responsibility Areas, the correctness no single one can
   own.

Described fully in its own chapter.

**The way of thinking — the CBC Inversion.** At every layer, the first question
is negative: what must never happen here, given what the surrounding layer
throws at it. Positive behavior is whatever minimal surface makes the
negative commitments hold.

The pair: the CBC Inversion without the layers has nowhere to stand. A
System Never-Event is only meaningful relative to a described world.
Asked in a vacuum, it produces slogans or endless theorizing. The
layers without the CBC Inversion are just an architecture documentation
format. The thing being defined here is the pair.

## The shape of the work

The work has two parts, each with its own chapter:

- **CBC Framing** turns an idea into a defined system on paper: one
  Falsifiable Promise, a described adversary, settled ownership, and
  the work cut into Invariant Slices. No code, no technology choices.
- **The Invariant Slice** is the unit of construction: one invariant
  taken from specification to a Structural Wall, proven by a test that
  *creates* the attack and shows the invariant surviving.

## Where it comes from

None of the parts are new:

- Bounded contexts (domain-driven design) built the same ownership
  walls against language drift.
- SLOs (site reliability engineering) made promises explicit and
  falsifiable.
- Threat modeling already asks first what must never happen.
- Design-before-code culture found that the cheapest place to catch a
  flaw is a document.
- The academic correctness-by-construction lineage owns "errors
  prevented by structure, not found by search."

Each of those practices covers one part and stops:

- threat modeling produces adversity but no boundary;
- bounded contexts produce boundaries but no guarantees;
- SLOs state guarantees but no enforcement;
- the correctness-by-construction lineage enforces but doesn't say
  where specifications come from.

What is claimed as original here is the **composition**. These are not
five practices but five phases of one derivation. One question
organizes them: *what must never happen, and what structure makes it
impossible*. Each phase asks it in its own vocabulary.

## What it is not

- **Not universal.** It prices correctness above speed of exploration. For
  throwaway code, experiments, and low-stakes tools, iterate-and-fix is
  cheaper and not wrong. The discipline earns its cost when breaking
  the Falsifiable Promise is expensive or irreversible (money, safety,
  trust), or when the system will live long. A method that does not know its limits is a slogan.
- **Not formal methods.** It keeps the stance of the
  correctness-by-construction lineage while dropping universal proof.
  Rigor is chosen, not applied everywhere: it goes to the few
  invariants whose violation is expensive or irreversible.
- **Not architecture.** Two teams following it could produce a monolith and
  a set of services from the same design. It constrains what must be
  *answerable*, not what must be *built*.

## How it fails

The known failure modes, named so they can be caught:

- **System Guarantee Erosion.** New features ship without re-checking
  the System Guarantees they might now violate.
- **Escape Hatch.** An admin path or raw script goes around the single
  enforced code path. The System Guarantee stops being true, and
  nobody sees it.
- **Testing Theater.** System Guarantees drift out of structure and
  back into test suites. Tests sample; structure forbids.
- **Theory Swamp.** Deep rigor is tried before the layers have made the
  problem small. It theorizes about a world not yet bounded.

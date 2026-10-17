# The layered system

The world model half of the discipline: a containment description of
reality, five nested boxes. The layering is not administrative — each layer
manufactures the precondition the next one needs to be a well-posed
question at all.

```
LAYER-1-ENVIRONMENT   Environment            the world the system lives in — outside its control
LAYER-2-SYSTEM        System of Interest     the thing being built: responsibility, boundary, authority
LAYER-3-AREAS         Responsibility Areas   the system's internal divisions by ownership
LAYER-4-PROBLEMS      Local Problems         bounded problems inside one area: invariants under adversity
LAYER-5-INTERACTION   Interaction            what emerges when areas interact; correctness across them

containment:  LAYER-1-ENVIRONMENT surrounds LAYER-2-SYSTEM
              LAYER-2-SYSTEM contains LAYER-3-AREAS
              each area in LAYER-3-AREAS contains its LAYER-4-PROBLEMS
              LAYER-5-INTERACTION is not "below" LAYER-4-PROBLEMS — it lives between the areas
```

## LAYER-1-ENVIRONMENT — The environment

Everything outside the system's control: users, networks, other systems,
the system's own process crashing. It is described as *hostile*: things
vanish, duplicate, and lie. The description must be made of facts you can
attack with ("responses get lost"), not vibes ("networks are unreliable").

The environment description also records what is deliberately *not*
defended against — assumptions explicitly accepted as trust. An assumption
written down is a decision; an assumption left implicit is a surprise
waiting.

Why the layer exists: without a described environment, guarantees have no
adversary and collapse into slogans. "Never lose an order" means nothing
until you can say what tries to lose it.

## LAYER-2-SYSTEM — The system of interest

The thing being built, defined by three properties:

- **Authority**: which facts this system is the single authority on.
- **Promise**: one falsifiable commitment about those facts, made to a
  named audience. Falsifiable means the breaking scenario can be imagined
  concretely — that property is what separates a promise from a mission
  statement.
- **Boundary**: everything crossing from outside gets checked at the door.

Why the layer exists: without a boundary, you defend against everything —
an unbounded job that ends in the theory swamp. The boundary gives defense
a finite task; the promise gives the whole design something to be derived
*from*.

## LAYER-3-AREAS — Responsibility areas

The interior, partitioned by one rule: **every fact has exactly one
owner.** Often the honest answer is a single area — that is a confirmed
answer, not a gap. Keeping the partition small is a design decision, not a
limitation.

Why the layer exists: an invariant is only enforceable if exactly one place
answers for it. Without the ownership partition, every invariant is
everyone's job — which means no one's.

## LAYER-4-PROBLEMS — Local problems

Inside each area: bounded problems small enough to be *closed* — an
invariant that must hold, the specific adversity that attacks it, and a
structure that ends the question. Small on purpose: the layers above made
them small.

Why the layer exists: without problems this size, there is nothing concrete
to construct correctly. Local correctness becomes checkable only when the
problem fits in one head.

## LAYER-5-INTERACTION — Interaction

The correctness no single area can own: what emerges *between* the parts —
ordering across areas, agreement between owners, the whole being right when
every part is. Empty by construction when LAYER-3-AREAS is a single area.

Why the layer exists: skipping it is the signature failure of teams who did
LAYER-4-PROBLEMS well — correct parts, wrong whole. Naming the
between-space gives emergent wrongness somewhere to be owned. It is where
most real incidents live.

## Two readings to keep apart

**Containment is not work order.** The boxes nest from LAYER-1-ENVIRONMENT
to LAYER-5-INTERACTION, and that is the right order for *presenting* a
system. It is not the order the design work runs in — deriving the layers
has its own order, starting from the promise. That order belongs to framing
and is described there.

**Layers are not architecture.** The layered system says what must be
answerable and by whom. It does not say what must be built: the same layer
description can honestly become a monolith or a set of services.

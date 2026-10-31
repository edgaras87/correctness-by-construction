# Glossary: the concept's and the method's Names

<!-- The Names the concept, docs/concept/, and the method's Agent
     Skills and Output Shapes are written in, each from this
     project's side: one plain sentence, with its owner where it has
     one. A pinned copy, like every delivered file: changed only as
     .claude/rules/delivered-copies.md says. This project's own Names
     are docs/glossary.md's.
     foundation: the writing convention -->

- **CBC Inversion** — asking what must never happen before asking
  what a system should do; the System Guarantees come first, the
  structure from them, the features last (`docs/concept/00-cbc.md`).
- **System Never-Event** — a thing that must never happen: money
  counted twice, an order created twice (`docs/concept/00-cbc.md`).
- **System Guarantee** — a System Never-Event stated against a named
  source of adversity; the system holds it by structure
  (`docs/concept/00-cbc.md`). Each is GUARANTEE-n where it is written.
- **System Guarantee Erosion** — the first way the concept fails: new
  features ship without the System Guarantees they might break being
  checked again (`docs/concept/00-cbc.md`).
- **Escape Hatch** — the second: an admin path or a raw script goes
  around the one enforced code path, and a System Guarantee stops
  being true (`docs/concept/00-cbc.md`).
- **Testing Theater** — the third: System Guarantees move out of
  structure and back into tests, which sample where structure forbids
  (`docs/concept/00-cbc.md`).
- **Theory Swamp** — the fourth: deep rigor tried before the layers
  have made the problem small (`docs/concept/00-cbc.md`).
- **Layered System** — the concept's model of the world: five nested
  layers, from the environment the system lives in to what emerges
  between its Responsibility Areas (`docs/concept/01-layered-system.md`).
- **System Layer** — one of the five layers of the Layered System,
  LAYER-1-ENVIRONMENT to LAYER-5-INTERACTION
  (`docs/concept/01-layered-system.md`).
- **Falsifiable Promise** — one commitment about the facts the system
  is the authority on, made to a named audience, whose breaking can be
  pictured concretely (`docs/concept/01-layered-system.md`).
- **Responsibility Area** — one of the system's internal divisions by
  ownership, LAYER-3-AREAS; made only when the Enemy Collisions
  force it
  (`docs/concept/01-layered-system.md`, `docs/concept/03-cbc-framing.md`).
- **System Guarantee Inventory** — the few System Never-Events whose
  breaking is costly or cannot be undone, each against a named
  adversity (`docs/concept/02-guarantees-and-walls.md`).
- **Structural Wall** — what makes one System Guarantee impossible to
  break; each gets the strongest one available, ranked by who it
  binds, from the store's refusal down to hope
  (`docs/concept/02-guarantees-and-walls.md`).
- **CBC Framing** — the first movement of the work: an idea turned
  into a defined system on paper, before any code or technology
  choice (`docs/concept/03-cbc-framing.md`).
- **CBC Framing Export** — one of the three documents CBC Framing
  produces: the CBC Framing Intent, the System Definition and the
  Invariant Slice Registry (`docs/concept/03-cbc-framing.md`).
- **CBC Framing Intent** — the first CBC Framing Export: the
  Falsifiable Promise and the purposes refused
  (`docs/concept/03-cbc-framing.md`).
- **System Definition** — the second: the system's authority,
  boundary, adversary and owners (`docs/concept/03-cbc-framing.md`).
- **Invariant Slice Registry** — the third: the work cut into
  Invariant Slices, in an order that evidence may change
  (`docs/concept/03-cbc-framing.md`).
- **Enemy Fact** — one attackable fact about something outside the
  system's control: it can vanish, duplicate or lie
  (`docs/concept/03-cbc-framing.md`).
- **Enemy Census** — the list of Enemy Facts, done when fresh attacks
  on it stop finding anything new (`docs/concept/03-cbc-framing.md`).
- **System Possession** — a fact or responsibility the system must
  own, since someone else owning it could break the Falsifiable
  Promise
  (`docs/concept/03-cbc-framing.md`).
- **Enemy Collision** — one Enemy Fact set against one System
  Possession, to see what dies (`docs/concept/03-cbc-framing.md`).
- **Enemy Collision Kill** — what dies in an Enemy Collision, named
  without its cure: "a retry lands twice and the order exists twice"
  (`docs/concept/03-cbc-framing.md`). Written by the Enemy Collision
  Kill Shape.
- **Invariant Slice** — the second movement of the work and its unit:
  one System Never-Event from the System Guarantee Inventory made
  real end to end, closed when it survives its attack
  (`docs/concept/04-cbc-slice.md`).

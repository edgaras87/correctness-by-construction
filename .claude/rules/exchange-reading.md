---
paths:
  - "temp/reading-*.md"
foundation: the exchange convention
---

<!-- The shape of a reading. Loads while one is being written or
     worked; says its form, never its content. -->

# The reading

**Governs:** how a reading — the document `exchange-read` produces and
the work then fills — is written. Its form, never its content.

## Where it sits

`temp/reading-<run>-<date>.md`, the date being the read that opened
it. When it opens, extends and closes is the exchange's, not this
file's.

## The header comment

Says what this is, that it stays here, and that it is edited in
place. Cites our own paths and decisions freely; nothing in it goes
to a run.

## The first line

The run, and its commit read through. That commit is the
read-through the next note carries, and the point the next reading
starts from. Written first, before anything is read.

## The sections, in this order

1. **Where we read to.** The commit read through, the previous
   read-through, and the span between.
2. **What the run did.** The span in prose, a paragraph per thing
   that happened — a step closed, a pass made, an edit landed, a
   hand-off written.
3. **Findings.** `F1`, `F2`, … — one per thing found, bold, with
   what it is and where. When one is fixed, its line says so and
   names the commit; it is never deleted.
4. **What the run taught us that we had not thought of.** Kept
   apart from findings: not a defect, a thing we would not have
   seen from here.
5. **Decisions.** `D1`, `D2`, … — each with what it asks, what
   rests on it, and which others it gates. Settled ones say so and
   how, in place.
6. **The work.** `W1`, `W2`, … — one per thing to do, marked
   **plan** when it will need a commit plan of its own. Done ones
   say so with the commit, in place. The order is preliminary and
   the reviewer reorders it.
7. **What this reading taught.** Lessons about reading itself, one
   line each, written as they happen — this is where the shape
   learns.
8. **Notes.** Counts, what is deliberately not being done, and
   anything that fits nowhere above.

## What holds across all of it

- **Numbers are kept.** An item keeps its number when it closes and
  is marked done in place — the file cites its own items, and so
  do lines outside it. Nothing is renumbered.

How the list is worked is `.claude/rules/working-a-reading.md`'s.

---

## Decisions

- ADR-0036 — the exchange: what a reading is, and that its shape
  is held here, exposed, because its moment is a file being written

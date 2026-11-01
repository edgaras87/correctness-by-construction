---
paths:
  - "temp/reading-*.md"
foundation: the exchange convention
---

<!-- The form of a CBC Run Reading, as an Agent Rule. Loads when one is read,
     so while it is worked, not while a new one is written
     (docs/conventions/agent-arrangement/ §5.6); says its form,
     never its content. -->

# The CBC Run Reading

**Governs:** how a CBC Run Reading — the document `exchange-read` produces and
the work then fills — is written. Its form, never its content.

## Where it sits

`temp/reading-<run>-<date>.md`, the date being the read that opened
it. When it opens, extends and closes is the Exchange Convention's (`docs/conventions/exchange/` §6.3, *The CBC Run Reading*,
and §6.4, *How a CBC Run Reading closes*), not this file's.

## The header comment

Says what this is, that it stays here, and that it is edited in
place. Cites our own paths and decisions freely; nothing in it goes
to a CBC Run.

## The first line

The CBC Run, and its commit read through. That commit is the
Read-Through Commit the next Delivery Note carries, and the point the next CBC Run Reading
starts from. Written first, before anything is read.

## The sections, in this order

What a CBC Run Reading holds, and why: (`docs/conventions/exchange/` §6.3, *The CBC Run Reading*).

1. **Where we read to.** The commit read through, the previous
   Read-Through Commit, and the span between.
2. **What the CBC Run did.** The span in prose, a paragraph per thing
   that happened — a Plan Step closed, a pass made, an edit landed, a
   CBC Run Ask written.
3. **Findings.** `FINDING-1`, `FINDING-2`, … — one per thing found,
   bold, with what it is and where. When one is fixed, its line says
   so and names the commit; it is never deleted.
4. **What the CBC Run taught us that we had not thought of.** Kept
   apart from findings: not a defect, a thing we would not have
   seen from here.
5. **Decisions.** `DECISION-1`, `DECISION-2`, … — each with what it
   asks, what rests on it, and which others it gates. Settled ones say
   so and how, in place.
6. **The work.** `WORK-1`, `WORK-2`, … — one per thing to do, marked
   **plan** when it will need a commit plan of its own. Done ones say
   so with the commit, in place. The order is preliminary and the
   reviewer reorders it.
7. **What this CBC Run Reading taught.** Lessons about reading itself,
   one line each, written as they happen. These lines are what the
   form is changed from.
8. **Notes.** Counts, what is deliberately not being done, and
   anything that fits nowhere above.

## What holds across all of it

- **Numbers are kept.** An item keeps its number when it closes and
  is marked done in place — the file cites its own items, and so
  do lines outside it. Nothing is renumbered.

How the list is worked is `.claude/rules/working-a-reading.md`'s.

---

## Decisions

- ADR-0036 — the Exchange Convention: what a CBC Run Reading is, and that its form
  is held here as an Agent Rule, loading when a CBC Run Reading is read

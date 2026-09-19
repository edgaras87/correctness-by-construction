# Deciding: the map of how the ten conventions relate

What is being attempted: one document stating what fires when, what
is standalone, what specialises what, and where the domain skills
supply sequences — holding **relations only**, never a rule that
lives in a manual or a skill.

Words that could read two ways: **"a document"** — ours to read, or
a thing a run receives. And **"map"** — a picture, or a page whose
diagram is one element.

## Questions, ordered by what rests on each

**Q1. Does the map ship to a run?**
- settles by: **ASK** — you
- rests on it: the size of the whole job. Not shipped is a file in
  `docs/` plus a records line: **two commits**. Shipped is a
  manual, a registry entry, a place in the birth list, two loops in
  `bundle-update.md`, a delta row, and an ADR: **seven or eight**,
  and a fourth delivery obligation to three runs.
- answer: **waiting**

**Q2. Where does it live?**
- settles by: MEASURE — done, conditional on Q1
- answer: if it does not ship, the honest home is
  `docs/conventions/README.md` as a section. That file is already
  the index of the ten, already ours, already explains what a
  convention is — and a separate sibling file repeats its opening
  to say where it sits. If it ships, it needs its own directory
  like every other convention, and Q3 stops being cosmetic.
- blocked on Q1

**Q3. What kind is it, by `artifact-kinds`?**
- settles by: MEASURE — done
- answer: **guide**, not convention. Its force is *advise*, not
  *bind* — it says what fires when, and every rule it points at
  binds on its own. Its reuse is the instance itself, not a
  template. That matters for Q1: shipping a guide into a directory
  of conventions puts a second kind there, which is the exact thing
  ADR-0031 just removed.
- settled

**Q4. Does the map carry a diagram, and in what form?**
- settles by: **COMPARE** — `visual-comparison`
- rests on it: one step, not the shape. A map with a table instead
  of a picture is the same document.
- discovered inside; not a blocker

**Q5. Does it name the domain skills — `cbc-bootstrap`,
`cbc-slice`, `infra-establish`, `infra-serve`, `cbc-framing`?**
- settles by: decide — leaning yes
- answer: they are where a *sequence* comes from, which is why
  `commit-plan` stays generic. A map of the chain that omits them
  implies the chain is complete without them. But they are not
  conventions, and saying so is part of the relation.
- affects content, not shape

## Commit count

**Not sayable — Q1 is open.** Two if it stays home, seven or eight
if it ships.

Note that Q3 argues against shipping and Q1 is not bound by it: a
guide could ship as a guide, in its own place, if a run needs the
map more than we do.

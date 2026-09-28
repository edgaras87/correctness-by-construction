---
paths:
  - "docs/conventions/*/README.md"
foundation: the conventions convention
---

<!-- The shape of a manual. Loads while one is being written or
     read; says its form, never its content. Ours, exposed, shipped
     nowhere: a run writes no manuals. The why is
     docs/conventions/conventions/ §3. -->

# A manual

**Governs:** how a convention's manual, `docs/conventions/<name>/README.md`,
is written. Its form, never its content.

## The sections, in this order

Each a `##` heading, except the opening statement, which is a bold
paragraph under the title. The body's sections are numbered; the
others are not.

1. **The opening statement.** One bold paragraph: what the
   convention is, in a sentence a reader can hold.
2. **What it is for.** The need: what work the convention makes
   possible, what went wrong without it — with the run or the date
   — and the event that made it. Evidence, or intent marked *on
   trial* with what would make it evidence and when to look again.
   Never intent dressed as evidence: a wish ("so that X is easier")
   is not a need.
3. **What this is made usable as.** The answer to the need: every
   derived artifact, each by path from the repo root, marked
   shipped or the deliverer's, with the moment it opens at — or
   "nothing shipped", and then what a repo holds. Ends with the
   sentence that a change here walks that list.
4. **The seats.** Both named, the run's first: what each does
   under the convention. One paragraph when alike; a section per
   seat when not; "no seat" said outright when one side has none.
5. **The body**, numbered sections, free prose. Pointers to other
   conventions as paths from the repo root, never a restatement
   of their subject.
6. **Lessons as dated italics**, where they happened: *what was
   measured, when, and what changed*.
7. **What this does not cover.** A list: each neighbouring subject
   in bold, then the path it belongs to.
8. **Where to look**, optional: pointers only, as root paths.

## What this does not fix

Length, tone, and how the body is divided. Whether a section is
needed is the manual's to decide; that a reader finds the six
where they expect them is this file's.

## The list is the floor, not the ceiling

Content that fits none of the six gets its own heading in the
body, and the writer looks for such content rather than forcing it
into a section it does not belong to. A section two manuals grow
without this file asking for it is a candidate for the list — that
is how the six were born (`docs/conventions/shapes/` §2: a pair
recurred) and the only way the list grows.

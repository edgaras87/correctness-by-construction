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

## The header comment

Says what this is and that it never ships; names what derives from
this page and how a disagreement between the page and a derivative
ends — decided, practice the evidence, the other following in the
same commit; and says when and from what the page was born. Same
rule as `docs/master.md`: only what is checkable, and anything
merely intended marked as intended.

## The sections, in this order

1. **The opening statement.** One bold paragraph: what the
   convention is, in a sentence a reader can hold.
2. **What ships.** The artifacts a run holds, by path in the
   container — or "nothing", and then what the deliverer holds.
3. **The seats.** Both named, the run's first: what each holds and
   does under the convention. One paragraph when alike; a section
   per seat when not; "no seat" said outright when one side has
   none.
4. **The body**, numbered sections, free prose. Pointers to other
   conventions by path, never a restatement of their subject.
5. **Lessons as dated italics**, where they happened: *what was
   measured, when, and what changed*.
6. **What this does not cover.** A list: each neighbouring subject
   in bold, then the path it belongs to.
7. **What this is made usable as.** The derived artifacts, each by
   path and kind, and the sentence that a change here walks that
   list.
8. **Where to look**, optional: pointers only.

## What this does not fix

Length, tone, and how the body is divided. Whether a section is
needed is the manual's to decide; that a reader finds the seven
where they expect them is this file's.

---
paths:
  - "docs/conventions/*/README.md"
foundation: the conventions convention
---

<!-- The form of a manual, as a rule. Loads when one is read, not
     while a new one is written (docs/conventions/agent-arrangement/
     §5.6); says its form, never its content.
     Ours, shipped nowhere: a run writes no manuals. The why is
     (docs/conventions/conventions/ §2, The manual). -->

# A manual

**Governs:** how a convention's manual, `docs/conventions/<name>/README.md`,
is written. Its form, never its content.

## The sections, in this order

Each a `##` heading, except the opening statement, which is a bold
sentence under the title. The body's sections are numbered; the
others are not. A manual whose idea a model states opens with
frontmatter naming it, `foundation: the agent model`
(`docs/conventions/conventions/` §1.3, *The `foundation` line*).

1. **The opening statement.** One bold sentence: the manual's
   subject, so a reader can tell from one line whether this is the
   page they need. Not a summary of how it works, nor its boundary
   or its channel: sections 5, 8 and 7 hold those.
2. **What it is for.** The need: what work the convention makes
   possible, what went wrong without it — with the run or the date
   — and the event that made it. Evidence; or intent marked *on
   trial* with what would make it evidence and when to look again,
   after which the need is rewritten from what was seen or the
   convention goes; or, taken whole from elsewhere, adopted —
   where it came from and what has been lived under it since. Never intent dressed as
   evidence: a wish ("so that X is easier") is not a need.
3. **What this is made usable as.** The answer to the need: every
   derived artifact, each by path from the repo root, marked
   shipped or the deliverer's, with the moment it opens at — or
   "nothing shipped", and then what a repo holds. Ends with the
   sentence that a change here walks that list.
4. **The seats.** Both named, the run's first: what each does
   under the convention. One paragraph when alike; a section per
   seat when not; a paragraph naming which body sections are whose
   when the body is already written per seat; "no seat" said
   outright when one side has none.
5. **The body**, numbered sections, free prose. Fact references to
   a manual, the concept or a model, never to a skill or a record
   for a fact
   (`docs/models/idea-to-output.md` §3.2, *Every link points up*);
   never a restatement of another convention's subject, but for a
   retelling with a fact reference to its section, where the reader
   acts on it in place (`docs/conventions/facts-in-sync/` §2,
   *Point and derive*). A section divided into
   labelled parts numbers them, `### N.M`, and so does every
   section of the same form in the manual. Emphasis in prose is
   not a part; a bold-led bullet with a paragraph of its own is
   (`docs/conventions/facts-in-sync/` §3.2, *A section's parts are
   numbered*). Each numbered section
   holds one subject, and a subject has one section; other
   sections point at it (`docs/conventions/conventions/` §2.5, *The body*).
6. **A lesson points at its story.** The body holds what it
   teaches, in general. One italic line, where it happened, points
   at the ADR or devlog entry that tells the case: *Its story:
   ADR-0059.* A case told nowhere is written into a devlog entry
   first, and the section is read again once the case has left
   (`docs/conventions/conventions/` §2.6, *A lesson taken*).
7. **Why it arrives this way.** The channel — a skill, a rule, a
   stub or a file — and why that one: the moment it serves, and
   what would or would not put it in front of its reader then.
   Where the reasoning rests on the agent model, a fact reference to the part it rests on, such as
   (`docs/models/agent.md` §8, *Choosing a channel*)
   (`docs/conventions/conventions/` §2.7, *Why it arrives this way*).
8. **What this does not cover.** A list: each neighbouring subject
   in bold, then the path it belongs to.
9. **Where to look**, optional: fact references only, as root paths.

## What this does not fix

Length, tone, and how many sections the body has. Whether a
section is needed is the manual's to decide; that a reader finds
the nine where they expect them is this file's.

## The list is the floor, not the ceiling

Content that fits none of the nine gets its own heading in the
body, and the writer looks for such content rather than forcing it
into a section it does not belong to. A section two manuals grow
without this file asking for it is a candidate for the list. The
list grows no other way.

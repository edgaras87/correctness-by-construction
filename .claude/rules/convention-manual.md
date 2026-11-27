---
paths:
  - "docs/conventions/*/README.md"
foundation: the conventions convention
---

<!-- The form of a manual, as an Agent Rule. Loads when one is read, not
     while a new one is written (knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md
     §6, Paths Rules); says its form, never its content.
     Ours, shipped nowhere: a CBC Run writes no manuals. The why is in
     the conventions manual (docs/conventions/conventions/ §2, The Convention Manual). -->

# A manual

**Governs:** how a Convention Manual, `docs/conventions/<name>/README.md`,
is written. Its form, never its content.

## The sections, in this order

Each a `##` heading, except the opening statement, which is a bold
sentence under the title, and item 6, a rule for the body. The body's sections are numbered; the
others are not. A manual whose idea an Idea Model states opens with
frontmatter naming it, `foundation: the tiers model`
(`docs/conventions/conventions/` §1.3, *The Foundation Line*).

1. **The opening statement.** One bold sentence: the manual's
   subject, so a reader can tell from one line whether this is the
   page they need. Not a summary of how it works, nor its boundary
   or its channel: sections 5, 8 and 7 hold those
   (`docs/conventions/conventions/` §2.1, *The opening statement*).
2. **What it is for.** The need: what work the convention makes
   possible, what went wrong without it, with the CBC Run or the date,
   and the event that made it (`docs/conventions/conventions/` §2.2, *The need*). Stated as one of three:
   - evidence;
   - intent marked *on trial*, with what would make it evidence and
     when to look again; then the need is rewritten from what was
     seen, or the convention goes;
   - adopted, taken whole from elsewhere: where it came from and what
     has been lived under it since.

   Never a wish written as evidence: "so that X is easier" is not a
   need.
3. **What this is made usable as.** The answer to the need: everything
   derived from the manual, each by path from the repo root, marked
   shipped or the Concept Deliverer's, with the moment it opens at.
   When nothing ships: "nothing shipped", and then what a repo holds.
   Ends with the sentence that a change here runs the Change Walk on that list
   (`docs/conventions/conventions/` §2.3, *The list of what derives*).
4. **The seats.** Both named, the CBC Run's first: what each does
   under the convention (`docs/conventions/conventions/` §2.4, *The seats*). One of four:
   - one paragraph when alike;
   - a section per Convention Seat when not;
   - a paragraph naming which body sections are whose, when the body
     is already written per Convention Seat;
   - "no Convention Seat" said outright when one side has none.
5. **The body**, numbered sections, free prose. Two rules on what it
   points at:
   - Fact References to a manual, the concept or an Idea Model, never
     to an Agent Skill or a record for a fact
     (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*);
   - never a restatement of another convention's subject, but for a
     retelling with a Fact Reference to its section, where the reader
     acts on it in place (`knowledge/backbone-ideas/one-home.md` §4,
     *Pointing at a home*).

   A section divided into
   labelled parts numbers them, `### N.M`, and so does every
   section of the same form in the manual. Emphasis in prose is
   not a part; a bold-led bullet with a paragraph of its own is
   (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §3, *Numbering a section's parts*). Each numbered section
   holds one subject, and a subject has one section; other
   sections point at it (`docs/conventions/conventions/` §2.5, *The body*).
6. **A lesson points at its story.** The body holds what it
   teaches, in general. One italic line, where it happened, points
   at the ADR or devlog entry that tells the case: *Its story:
   ADR-0059.* A case told nowhere is written into a devlog entry
   first, and the section is read again once the case has left
   (`docs/conventions/conventions/` §2.6, *A lesson taken*).
7. **Why it arrives this way.** The channel: an Agent Skill, an Agent Rule, a
   Record Stub or a file. Then why that one: the moment it serves, and
   what would or would not put it in front of its reader then.
   Where the reasoning rests on how an agent works, it carries a Fact
   Reference to that part, such as (`knowledge/backbone-ideas/how-an-agent-works.md` §7,
   *Choosing a channel*). Why: (`docs/conventions/conventions/` §2.7, *The channel*).
8. **What this does not cover.** A list: each neighbouring subject
   in bold, then the path it belongs to (`docs/conventions/conventions/` §2.8, *The boundary*).
9. **Where to look**, optional: Fact References only, as root paths
   (`docs/conventions/conventions/` §2.9, *Where to look*).

## What this does not fix

Length, tone, and how many sections the body has. Whether a
section is needed is the manual's to decide; that a reader finds
the nine where they expect them is this file's.

## The list is the least a manual has

Content that fits none of the nine gets its own heading in the
body, and the writer looks for such content rather than forcing it
into a section it does not belong to. A section two manuals grow
without this file asking for it is a candidate for the list. The
list grows no other way.

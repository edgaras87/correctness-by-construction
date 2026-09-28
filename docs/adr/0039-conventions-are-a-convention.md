# 0039. Conventions are a convention, and every description follows one rule

Date: 2026-09-28
Status: Accepted (2026-09-28, at the set's records commit; opened
Proposed under the commit plan for the conventions manual and
revised at two boundaries on the reviewer's readings — the master
is a map, a pointer is a path, the boundary section, `foundation`
moves home, seats are two named roles. Amends ADR-0036 decision 7
in the ownership of `foundation`)

## Context

What a convention is here, and how one is made, is stated in
places that were never meant to hold it. The index,
`docs/conventions/README.md`, was scoped by ADR-0032 to relations
only — the table and the chain, never a rule that lives in a manual
or a skill. Since then it has grown four sections that are rules: an
opening definition, *A skill file*, *Writing an artifact*, *The
container's rules*, and *Adding a convention*. Each was added
because it had nowhere else to go. Together they are a manual for
conventions, filed inside the index because no manual existed.

Two of those rules were never lived. *Adding a convention* asks for
a CHANGELOG entry and a PLAN step per convention. The last three
conventions — `visual-comparison`, `exchange`, `shapes` — got a
manual, a table row, an ADR and a registry entry, and none of them
got either. The CHANGELOG here is the concept-version log
(ADR-0003) and has no place for a convention's line; the PLAN has
no per-convention steps. A rule nobody follows and nobody
questioned is the mark of a rule kept where nobody reads it.

The wider idea the repo runs on is scattered the same way. One
description, and everything else derived from it and pointing back
— the master's sections 1 and 3, ADR-0036 decision 7, the exchange
manual's closing, the shapes manual's closing, both manuals'
headers. The reviewer filed it on 2026-09-27 as a convention for
descriptions gathering three items: the words for what things
derive from, every manual saying its seats, and a maintenance rule
for core descriptions with a trigger not yet fired.

On 2026-09-28 the reviewer asked how differently a description and
a manual should be handled, since they share the core: a source of
truth, everything from it derived or referencing it, a change
rechecking every derivative, a derivative that disagrees forcing a
decision. The answer that held is that the core is one and the
edges differ, and the edges are real:

- **Versioning.** The concept is versioned as a whole; a change
  that could invalidate a derivative bumps the version and enters
  the CHANGELOG. A manual has no version; its artifacts move with
  it in the same commit and ride the container's pin. So
  `foundation: concept v1` carries a number and `foundation: the
  exchange convention` a name.
- **Shipping.** The concept ships; a run holds a copy and reads it.
  A manual never ships; a run sees only the artifact.
- **The kind of derivative.** From a manual comes an artifact, an
  instruction a project holds. From the concept comes the method,
  derived, and the stack practice, checked against. Only the
  concept has the second relation.
- **Seats.** A manual answers whether this repo uses the convention
  as a run does. The concept has no seat here.
- **What it asserts.** A convention is a rule you may ignore with a
  reason, with a named falsifier (ADR-0031). The concept is a claim
  about how systems are built.

Two manuals had already grown the same sections without anything
telling their writers to: the exchange and shapes manuals share a
header saying what derives from the page and how a disagreement
ends, an opening statement, *what ships*, a seats section, lessons
as dated italics, and *what this is made usable as*. The shapes
rule says a shape is born when a pair recurs. This is the pair.

## Options considered

1. **Leave the rules in the index.** Rejected. ADR-0032's scope
   was the answer to the index's predecessor growing to 126 lines
   of restatement before it was deleted; the index is on the same
   road, and two of its rules are already dead letters.

2. **A descriptions convention, wide enough for the concept, the
   manuals and the master.** Rejected for now. Two kinds of
   description with derivatives is two instances, and ADR-0038's
   rule of three binds this repo as it bound the handbook. The
   shared core fits in one section of the master, which already
   states it and already says what happens when a section outgrows
   the page.

3. **A conventions manual, the core in the master, the edges where
   they are.** The first draft. Rejected at step 4's boundary: the
   master is a map, an entry point one level in from the README,
   and a rule split between a map and a manual is two places for
   one truth — the defect the manual's own *one place* names.

5. **A conventions manual holding the core, the master pointing at
   it, the edges where they are.** Chosen.

4. **The shape of a manual held until a third manual grows the
   sections.** Rejected. The shapes convention's own rule is that a
   pair births a shape, and holding the third instance to a stricter
   standard than the rule sets would be a rule kept for symmetry.

## Decision

1. **`conventions` is the ninth convention.** Its manual,
   `docs/conventions/conventions/README.md`, holds what the index
   accreted: what a convention is and asserts, its two parts kept
   apart, the skill file's form, how an artifact is written, how a
   manual is written, the rules the container holds about
   conventions, and how one is added — the last rewritten from what
   the last three conventions did, so that no step in it is one
   nobody takes. The doubled word in the path is the cost of naming
   the thing whole rather than one of its parts.

2. **The index returns to relations.** The table, with a ninth row,
   and the chain. ADR-0032's scope holds: a sentence that restates a
   rule living in a manual or a skill leaves for the manual, with its
   wording.

3. **Every manual names both seats**, the run's and the
   deliverer's: what each holds and does under the convention, the
   run first — one paragraph when they are alike, a section per
   seat when they are not, and "no seat" said outright when one
   side has none. Placed after *what ships*. The six manuals that
   never answered gain the paragraph in this set. *Revised at step
   5: the first wording asked whether this repo uses the
   convention the way a run does — a question from one chair, with
   the other seat assumed.*

4. **The shape of a manual is a rule of ours**, exposed under
   `.claude/rules/` on `docs/conventions/*/README.md`, listing the
   sections a manual has and no more: a header on what derives
   from the page and how a disagreement ends; an opening statement;
   *what ships*; the seats; lessons as dated italics; *what this
   does not cover*, the boundary against its neighbours by path; and
   *what this is made usable as*. The seventh was not in the pair
   that birthed the shape — only shapes had one — and joined when
   the conventions manual needed to draw its line four times in one
   reading: it is the section that makes *one place* checkable from
   the reader's side. It is the convention's artifact here. It ships
   nowhere: a run writes no manuals.

5. **The convention ships nothing else, and `foundation` is its.**
   The field — its name, that every derived file carries one, ours
   included, and what it holds for each kind — is stated in the
   conventions manual §2, and is this convention's artifact in a
   run. ADR-0036 decision 7 decided the field as the exchange's;
   it is amended in that one respect, ownership, and the exchange
   keeps what is its own: that the line travels with the copy as a
   live claim. Three artifacts of ours carried no line and gain
   one. A run's own descriptions —
   `docs/system/definition.md` and the slice records through the
   registry — follow the same core, and whether that earns a
   shipped rule is left to the run that trips on it.

6. **The rule for every description lives in the conventions
   manual, and the master points at it.** A description lists what
   derives from it; each derivative names its description; a
   change to the description walks the list in the same commit and
   greps for the description's path; a change forced in a
   derivative is checked back; a disagreement is decided, practice
   the evidence, and if the description changes the walk runs
   again. The master's section 3 keeps the loop and the record of
   where practice bent a description, and states no rule: it is a
   map, and its "not a rule yet" paragraph is gone — the trigger it
   named never fired, and the reviewer's question did. The birth
   case: a description born with existing derivatives walks them in
   the set that follows, not the same commit; this manual was born
   with nine, and the walk is the next set. The trigger for a
   descriptions manual of its own stands: the section outgrows the
   manual and leaves a paragraph behind.

7. **The words.** *Description* is any body of writing things
   derive from — the concept, each manual, the master. *Manual* is
   a convention's description. *Foundation* is the derived side's
   claim, and only that side's. The split carries meaning: the five
   edges above are where a manual and the concept are handled
   differently, and a reader who has only one word for both loses
   them. *Source* stays a run's word for the deliverer. *Deliverer*
   stays: *hub*, weighed at step 5, names a topology that is not
   true — a run is blind, nothing flows up as files, the connection
   is one person copying — and is the shape ADR-0038 left behind.

8. **A pointer is a path.** Text that points at a manual names
   its directory with the slash — a path from the repo root, or a
   relative link between manuals, which carries the same token —
   so that a change to a manual finds every pointer with one grep,
   as it finds every derivative by `foundation`. A name in prose is
   not a pointer. A rename is commit-plan §4's sweep. The evidence
   that the walk over pointers is needed: the previous day's sweep
   of one word across twenty live files, done by hand.

9. **No CHANGELOG entry and no PLAN step**, now or for any
   convention that ships nothing. The CHANGELOG is the
   concept-version log; a convention entering the container is
   recorded in the container's tables and the registry, which is
   what the last three did.

## Consequences

Good: the index is readable as an index again, and the rules it
held are where a maintainer looks for why. The next manual is
written to a shape instead of by imitation, and answers the seats
question because the shape asks it. The shared core is in one
place and says it binds. Four TODO items close.

Bad, and accepted: a convention about conventions is one level up
from the work, and the manual will be read less than any other.
That is the argument for keeping it short and for the shape rule
being the part that fires. The doubled path reads badly. And the
concept's edges stay in three places — ADR-0003, the CHANGELOG's
comment, the master's 1.1 — because gathering them would be the
descriptions convention this record declines to write.

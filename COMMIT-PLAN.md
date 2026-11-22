# Commit plan: the Change move

## Summary — the state after all commits

The facts of Change have one home: the layers document,
`temp/common-ground/knowledge-layers.md`. Its §3.2, retitled *How a
change travels*, holds the rules of the six parts, written out as
rules. Each part's open points follow its rules, each with its
trigger. An open point names a TODO item only when its trigger is
one. The cases not yet checked, what is known but not ruled, and the
sources not yet taken into account are marked as not done.

The simulation keeps what led to the rules: each step's options, why
the others were not chosen, and its *Today* fields. Each step points
at the rule it led to. Its header no longer calls it the home of
Change.

The problem file's seven travel terms and two labels sit in the
layers document's §2 list, eleven entries beside the System Kit, and
the problem file keeps pointer entries. Its Repo Responsibility
lists and §2.2 table stay, re-pointed, and its 3 stale lines are
fixed. The flow drawing points at the new home.

TODO no longer holds the "Define the Change idea" item. The items
whose triggers named it say what they wait for now, and the layers
item says where the open points of *How a change travels* live.

What it gives: someone working by the Change rules reads them in one
place, with their gaps beside them, and the simulation reads as the
record of how they were chosen.

## Commits

**1. `docs: temp's layers take the travel terms`**
The problem file's seven travel terms move to the layers document's
§2 list: Look for Lessons, Maintainer Repo Register, System Kit
Attention Note, System Kit Copy Change Record, System Kit Update
Note, System Kit Update Take, System Repo Reading. The two labels,
*settled snapshot* and *version snapshot*, go with them. Each leaves a
pointer entry in the problem file. Each entry says its short form,
as the existing ones do. The problem file's §2.2 table gains rows
for Look for Lessons and System Kit Update Take, one of its 3 stale
lines. The simulation's and the flow drawing's notes on their short
forms point at the layers document. A commit of its own: the rules
in commits 2 to 9 use these terms, so they must stand first.

**2. `docs: temp's layers frame how a change travels`**
The layers document's §3.2 is retitled *How a change travels*. It
takes the simulation's §1 paragraphs on the Look for Lessons and on
bringing a System Repo up to date, beside its table of parts and its
table of depths. Every pointer to the old title is fixed. A commit
of its own: the frame the six parts sit in, before any part moves.

**3. to 8. One commit per part, in the simulation's order:**

- **3. `docs: temp's layers take Change's rules`**
- **4. `docs: temp's layers take Read Changes' rules`**
- **5. `docs: temp's layers take Judge's rules`**
- **6. `docs: temp's layers take Act's rules`**
- **7. `docs: temp's layers take Deliver's rules`**
- **8. `docs: temp's layers take the Take's rules`**

Each commit, for its part:
- writes the part's rules out in §3.2, from its steps' *What must
  happen*, *Chosen* and *Adapted Case* fields, and the rules inside
  *Chosen*, such as *Where it sits* and *Two checks at main*;
- puts the part's open points after its rules, each with its
  trigger, naming a TODO item only when the trigger is one;
- marks what depth c leaves undecided in that part as not yet done;
- trims each of the simulation's steps to *Options*, *Chosen*, as
  the option taken and why the others were not, and *Today*, with a
  pointer to the rule;
- fixes every pointer to the moved facts, in the problem file, the
  flow drawing, the layers document and TODO.

Where a stale line falls:
- commit 5 fixes the problem file's Maintainer Repo item 5, which
  names Judge's Adapted Case by an old name;
- commit 8 fixes its item 6, which says a System Repo gets the
  System Kit's changes and judges each against its Copy. Item 6
  points at both Deliver and the Take, so it changes once, here;
- commit 8 words "every Record cleared" as following from taking
  each Copy whole, not as an act of its own.

Each part is its own commit: reverting one leaves the other parts
whole, and each part's rules are read and checked on their own.

**9. `docs: temp's layers take the cases and sources`**
The simulation's §2 moves: the cases, with the six rows not yet
checked, each checked when practice first meets it; *Known, not
ruled*; and *Other sources*, naming each source not yet taken into
account: the Maintainer Repo's own lesson, the layers document's
§3.3, and Knowledge on Trial handed back. Birth stays outside, as
the start. A commit of its own: what the rules do not yet cover,
after the rules.

**10. `docs: temp's simulation points at the layers`**
The simulation's header comment and §1 say what it is now: the
record of how the rules were chosen, its steps pointing at their
rules. The flow drawing's header says where the facts live. A
commit of its own: once every part has moved, so neither header
claims what is not yet true.

**11. `docs: TODO closes the Change idea item`**
The "Define the Change idea" item goes. The items whose triggers
name it are rewritten true for today: the depth c item, the problem
file's next pass, and confirming the Common Ground Problem. The
layers item's Context gains where *How a change travels* holds its
open points. The records commit, at the boundary where the move is
true.

## Decisions taken inside this plan

- **The *Adapted Case* fields move with the rules.** The header calls
  a part's rules its *Chosen* and *Adapted Case* fields, so both are
  rules. The simulation keeps only why each choice was made.
- **Parts as subsections of §3.2,** one for each part, titled by the
  part's name. The depth table stays in §3.2.
- **Short forms in the layers document.** The three entries that now
  say "The picture shortens it to" say instead that the document
  shortens it, since the rules use the short forms too.
- **The simulation's picture, *Change whole*,** stays in the
  simulation in this plan. Commit 10 judges whether it repeats §3.2,
  and says what it found.
- **Stale lines go in the commit that touches their line,** so each
  line changes once.
- **No ADR.** Decisions on the `temp/` drafts are recorded in commit
  bodies and the devlog.
- **The devlog entry is the session's,** not a commit of this plan.
- **Exact wording is shown at each staging,** for the reviewer's
  word.

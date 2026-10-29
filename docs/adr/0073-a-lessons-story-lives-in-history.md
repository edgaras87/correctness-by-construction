# 0073. A lesson's story lives in history

Date: 2026-10-29
Status: Proposed (opened under the commit plan for lesson stories)

## Context

The conventions manual's lesson rule puts the case that taught a
lesson beside it, as a dated italic: what happened, when, and what
changed (`docs/conventions/conventions/` §2.6, *A lesson taken*).
On 2026-10-25 the reviewer asked whether those stories are noise
(`TODO-CONVERSATION-MEMORY.md` §18, *The story behind a lesson*).
They load with every manual, and they matter only when someone
questions or changes the rule.

Measured 2026-10-29: 72 dated notes, about 310 lines, 8% of the 12
manuals, and one in the tiers model. About 50 are told already in an
ADR or the devlog; about 21 are told nowhere else here.

A note does two jobs:
- **An example** shows the rule in use, and is read every time.
- **An origin** says where the rule came from, and is read only at a
  change: when a rule is changed or dropped, when its strength is
  judged, or when the reviewer asks why. At each of those moments
  the foundation check has the manual open anyway, so one hop to the
  story costs little.

Round 2's read found 6 rules that stood only in a note, a live
claim in italics. A run never reads our origins: it cannot open our
ADRs or devlog, and manuals never ship.

## Options considered

**What a note becomes:**
1. **Kept whole,** as today. Rejected: notes drift, as round 2's six
   rules showed, and 8% of each manual is a story its reader does
   not act on.
2. **Split:** the example stays in the body, undated, and the origin
   becomes a pointer. Rejected as the rule for all: a judgment call
   on each of 72 notes, made before anyone knows which sections need
   an example. Its point survives as the safeguard in decision 1.
3. **Dropped,** git keeping them. Rejected: the story is then found
   only by digging through git, and the manuals ask for the evidence
   behind a rule.

**Where its story goes:**
1. **All of them into one new devlog entry.** Rejected: the 50
   already told would be told twice, under a date that is not
   theirs. One entry for the orphans alone, written first, was the
   plan's own until 2026-10-29: which stories are orphans shows only
   when each note is read beside its home, so the reading would run
   twice.
2. **A new record, a lessons log,** each note under an id. Rejected:
   a new kind of record, with its own row, form and section, for
   stories ADRs and the devlog already hold.
3. **The commit that removes the note,** cited by hash. Rejected: the
   reader must read a diff, and a hash cannot be regrouped later.

**When:**
1. **The rule now, the notes as each manual is next touched.**
   Rejected: two forms side by side for weeks, and round 3 polishing
   notes that later leave.
2. **Folded into round 3.** Rejected: round 3 reads how a text reads;
   where a story lives is where a fact lives, and mixing them blurs
   both.

## Decision

1. **A dated note becomes one line pointing at its story,** in
   italics, set apart from the rule as the note was: "*Its story:
   ADR-0059.*", "*Its story: devlog 2026-10-19, later.*". A note told
   in several places names each. A live claim inside a note moves
   into the body. The section is then read again: where its lesson
   no longer reads clearly without the case, it gains a short plain
   example.
2. **The story's home is the history that already tells it,** an ADR
   or a devlog entry, read beside the note before its line is
   written. A story told nowhere else is copied, word for word, into
   a devlog entry written in the commit that moves its manual's
   notes, so no line points at nothing. Where an ADR tells a story
   only in part, the line points at the ADR, and the rest goes into
   that entry.
3. **Now, before round 3's rule check,** as one commit plan, so
   round 3 reads the manuals in the shape they keep.

## Consequences

- The lesson rule changes (`docs/conventions/conventions/` §2.6,
  *A lesson taken*), and facts-in-sync's list of where history
  lives loses "a lesson's dated italic"
  (`docs/conventions/facts-in-sync/` §4, *The rule for every
  description*).
- Our files that follow the rule change: `convention-manual.md`
  item 6, `approach-evaluation.md` stage 6, and `model-placing.md`
  stage 3 and its *Not known yet*.
- A devlog entry in each commit that moves notes holds the stories
  told nowhere else, word for word: about 21 in all.
- The 72 notes become pointers, each read beside its home first.
- A manual reads as its rules. The cost accepted: at a change, the
  story is one hop away, in a record that is never edited, so the
  pointer cannot drift.
- Out of scope by design: a manual's *What it is for*, which holds
  its need's evidence (`docs/conventions/conventions/` §2.2, *What
  it is for*), and an approach's dated *Uses*, its evidence for
  evaluation. Whether the conventions keep examples at all stays
  TODO's own item.
- Nothing ships: no run holds a manual.

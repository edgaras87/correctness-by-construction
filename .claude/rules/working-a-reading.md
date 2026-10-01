---
paths:
  - "temp/reading-*.md"
foundation: practice, under the exchange convention
---

<!-- How this repo works a reading, from the reading to the note.
     Loads beside the reading's shape, which says what the file
     looks like; this says how its list is worked. Written from
     three readings of run 3. -->

# Working a reading

**Governs:** what happens between `exchange-read` and
`exchange-deliver` — how a reading's list is worked until every
item has ended. What each item ends as, and where, is the
exchange's (`docs/conventions/exchange/` §6.5); this is how it gets
there.

## The steps

1. **Count it, before any branch.** How many W, and how many marked
   **plan**. More than one plan means a branch, cut from main after
   the reading is written; the count is what says whether one is
   needed. The count undercounts: one item's set can run to twenty
   commits, and an item that edits a skill both seats hold is two
   commits, the agent's own files apart. It is a number of items,
   never a size.

2. **Decisions first.** A D gates the W that rest on it, and
   settling it reshapes or deletes them. A question outside the
   reading can gate an item too; the item says so rather than being
   reordered in silence. The order is preliminary, and the reviewer
   reorders it. A decision may be answered by a question the list
   never asked: the options written down are not the space.

3. **A decision that needs an ADR is a proposed one**, built and
   corrected while building — not a list of questions. It opens
   Proposed under a commit plan, the plan's revisions correct it,
   and it flips to Accepted in the set's records commit. One that
   needs none is settled on its proposal, and marked so in place.

4. **A work item is a commit or a commit plan**, with the reviewer
   at every boundary.

5. **Every close is followed by one pass over every open item.**
   The item is marked the moment it closes, with its commit; then
   each open F, D and W is read once against it — changed, closed,
   or blocked — and marked in place before the next is opened. The
   items are not independent: one item's set can close another, and
   right after one moved is the only cheap moment to see how the
   others moved with it.

6. **A changed line is an edit only if the run's log says so.** For
   every hunk the diff put on the reading, ask first whether the
   run's decisions log records it. Recorded: the run edited it on
   purpose, and it is an item to decide. Not recorded: something
   went wrong at the take, a finding about the exchange rather than
   the copy. The diff alone cannot tell the two apart.

7. **Each item ends as one of three** — taken, declined, held — and
   lands where the exchange says.

8. **Records as they fall.** An ADR for a decision with rejected
   options; the decisions log for a change to the arrangement; the
   devlog at a session's end and at a pause.

9. **When the list is closed, `exchange-deliver`.** The note is
   written from the reading's final state — every item's verdict,
   in the run's order — and the read-through from its first line.
   A note may go before the list closes, since a note alone is
   cheap; it is then written from the items as they stand, and says
   which are still open. At the close, the reading's lessons go
   where they act — this rule, the shape, a skill — or to TODO; then
   the reading is deleted, a branch fast-forwards, and the devlog
   says so.

## What this does not cover

- **What a reading looks like** — `.claude/rules/exchange-reading.md`.
- **When a reading opens, extends, closes, or is overtaken** —
  `docs/conventions/exchange/` §6.3 and §6.4.
- **The run moving before the note** — `exchange-deliver`, step 0.
- **How a commit plan runs** — `commit-plan`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-01 — placed from the draft that
  ran three readings of run 3; why a rule beside the shape, and not
  the shape, a skill, or the draft left standing

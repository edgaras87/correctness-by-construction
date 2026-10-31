---
paths:
  - "temp/reading-*.md"
foundation: practice, under the exchange convention
---

<!-- How this repo works a Run Reading, from the Run Reading to the Delivery Note.
     Loads beside the Run Reading's form, which says what the file
     looks like; this says how its list is worked. Written from
     three Run Readings of CBC Run 3. -->

# Working a CBC Run Reading

**Governs:** what happens between `exchange-read` and
`exchange-deliver` — how a Run Reading's list is worked until every
item has ended. What each item ends as, and where, is the
Exchange Convention's (`docs/conventions/exchange/` §6.5, *Verdicts*); this is how it gets
there.

## The steps

1. **Count it, before any branch.** How many work items, and how many
   marked **plan**. More than one plan means a branch, cut from main
   after the Run Reading is written; the count is what says whether one is
   needed. The count undercounts: one item's set can run to twenty
   commits, and an item that edits a skill both Convention Seats hold is two
   commits, the agent's own files apart
   (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*). It is a number of items,
   never a size.

2. **Decisions first.** A decision gates the work that rests on it,
   and settling it reshapes or deletes that work. A question outside
   the Run Reading can gate an item too; the item says so rather than
   being reordered in silence. The order is preliminary, and the
   reviewer reorders it. A decision may be answered by a question the
   list never asked: the options written down are not the space. When
   a decision sorts items into groups, the groups are counted against
   the list as they are made: an item in no group is lost without a
   sign.

3. **A decision that needs an ADR is a proposed one**, built and
   corrected while building — not a list of questions. It opens
   Proposed under a commit plan, the plan's revisions correct it,
   and it flips to Accepted in the set's records commit. One that
   needs none is settled on its proposal, and marked so in place.

4. **A work item is a commit or a commit plan**, with the reviewer
   at every boundary (`docs/conventions/commit-messages/` §2.4, *Commit on the word*). An item taken into a Master Copy is checked against
   its foundation (`.claude/rules/foundation-check.md`), and the
   file it lands in is read whole before the commit: a CBC Run's edit
   shows one file, never what that file stands on. It is checked
   against what the CBC Runs did, too: where a CBC Run's decision says it
   lands names a place, never how the CBC Runs lived it.

5. **Every close is followed by one pass over every open item.** The
   item is marked the moment it closes, with its commit; then each
   open finding, decision and work item is read once against it —
   changed, closed, or blocked — and marked in place before the next
   is opened. The items are not independent: one item's set can close
   another, and right after one moved is the only cheap moment to see
   how the others moved with it.

6. **A changed line is an edit only if the CBC Run's Decisions Log says so.** For
   every hunk the diff put on the Run Reading, ask first whether the
   CBC Run's Decisions Log records it. Recorded: the CBC Run edited it on
   purpose, and it is an item to decide. Not recorded: something
   went wrong at the Delivery Take, a finding about the Exchange Convention rather than
   the copy. The diff alone cannot tell the two apart.

7. **Each item ends as one of three** — taken, declined, held — and
   lands where the Exchange Convention says.

8. **Records as they fall,** each at its moment in `CLAUDE.md`'s
   records table: an ADR, the Decisions Log, the devlog.

9. **When the list is closed, `exchange-deliver`.** Closed means the
   first gate below holds: a finding with no item reaches no
   verdict, and nothing else stops the Delivery Note going without it. The
   Delivery Note is written from the Run Reading's final state — every item's
   verdict, in the CBC Run's order — and the Read-Through Commit from its first
   line. A Delivery Note may go before the list closes, since one alone is
   cheap; it is then written from the items as they stand, and says
   which are still open. At the close, the Run Reading's lessons go
   first, where they act — this Agent Rule, the Run Reading's form, a skill —
   or to TODO. Then main takes the branch by fast-forward, and one
   commit on main deletes the Run Reading and adds the devlog entry.

## Gates

True when a Run Reading closes. A Run Reading's Plan Step checks its own items
against them (`PLAN.md`, the Plan Step Form's Known already).

- Every finding, and every line of what the CBC Run taught us, has
  ended in a decision or a work item, or says why it needs neither.
- Every work item has ended, taken, declined or held, and is marked
  in the Run Reading with its commit.
- The Delivery Note, written from the Run Reading's final state, is in the CBC Run,
  and names the commit read through.
- The Run Reading's lessons sit where they act, or in TODO.

## Stages

For a Run Reading's Plan Step, its Notes and its Now line: read
(`exchange-read`); decide and work (steps 1 to 8 here); note
(`exchange-deliver`); close (step 9). When the CBC Run moves and the
Run Reading is extended, by `exchange-read` again or by
`exchange-deliver`'s Stage 1, step 0, Now returns to read.

## What this does not cover

- **What a Run Reading looks like** — `.claude/rules/exchange-reading.md`.
- **When a Run Reading opens, extends, closes, or is overtaken** —
  `docs/conventions/exchange/` §6.3, *The CBC Run Reading* and §6.4, *How a CBC Run Reading closes*.
- **The CBC Run moving before the Delivery Note** — `exchange-deliver`, Stage 1,
  step 0.
- **How a commit plan runs** — `commit-plan`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-01 — placed from the draft that
  ran three Run Readings of CBC Run 3; why an Agent Rule beside the Run Reading's form,
  and not that form, a skill, or the draft left standing
- `.claude/decisions.md`, 2026-10-08 — step 4: a taken item checked
  against its source, and its file read whole
- `.claude/decisions.md`, 2026-10-10 — step 9 and *Gates*: the list
  closes only when every finding has ended in an item
- `.claude/decisions.md`, 2026-10-17 — *Gates* and *Stages*: a
  Run Reading's gates and stages, for its Plan Step in PLAN (ADR-0057)

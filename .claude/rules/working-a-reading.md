---
paths:
  - "temp/reading-*.md"
foundation: practice, under the exchange convention
---

<!-- How this repo works a CBC Run Reading's list, from its first line to the Delivery Note.
     Loads beside the CBC Run Reading's form, which says what the file
     looks like; this says how its list is worked. Written from
     three CBC Run Readings of CBC Run 3. -->

# Working a CBC Run Reading

**Governs:** how a CBC Run Reading's list is worked until every item
has ended, between the exchange-read and exchange-deliver Agent Skills.
What each item ends as, and where, is the
Exchange Convention's (`docs/conventions/exchange/` §6.5, *Verdicts*); this is how it gets
there.

## The steps

1. **Count it, before any branch.** How many work items, and how many
   marked **plan**. More than one plan means a branch, cut from main
   after the CBC Run Reading is written; the count is what says whether one is
   needed. The count is of items, not of work. One item can take
   twenty commits. An item that edits an Agent Skill both Convention
   Seats hold is two commits: the Master Copy, then our own copy
   (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*).

2. **Decisions first.** A decision gates the work that rests on it,
   and settling it reshapes or deletes that work. A question outside
   the CBC Run Reading can gate an item too; the item says so rather than
   being reordered in silence. The order is preliminary, and the
   reviewer reorders it. A decision may be answered by a question the
   list never asked: the options written down are not all the options. When
   a decision sorts items into groups, the groups are counted against
   the list as they are made: an item in no group is lost without a
   sign.

3. **A decision that needs an ADR is a proposed one**, built and
   corrected while building, not a list of questions. It opens
   Proposed under a commit plan. The plan's revisions correct it. It
   flips to Accepted in the Change Set's records commit. One that
   needs none is settled on its proposal, and marked so in place.

4. **A work item is a commit or a commit plan**, with the reviewer
   at every boundary (`knowledge/backbone-ideas/commit-messages.md` §5, *Commit on the word*). An item taken into a Master Copy is checked against
   its foundation (`.claude/rules/foundation-check.md`). The file it
   lands in is read whole before the commit: a CBC Run's edit shows
   one file, never what that file stands on. It is checked
   against what the CBC Runs did, too. A CBC Run's decision names where
   a change lands, never how the CBC Runs lived with it.

5. **Every close is followed by one pass over every open item.** The
   item is marked the moment it closes, with its commit. Then each
   open finding, decision and work item is read once against it, as
   changed, closed, or blocked, and marked in place before the next
   is opened. The items are not independent: one item's Change Set can close
   another, and right after one moved is the only cheap moment to see
   how the others moved with it.

6. **A changed line is an edit only if the CBC Run's Decisions Log says so.** For
   every hunk the diff put on the CBC Run Reading, ask first whether the
   CBC Run's Decisions Log records it. Recorded: the CBC Run edited it on
   purpose, and it is an item to decide. Not recorded: something
   went wrong at the Delivery Take, a finding about the Exchange Convention rather than
   the copy. The diff alone cannot tell the two apart.

7. **Each item ends as one of three:** taken, declined or held. It
   lands where the Exchange Convention says (`docs/conventions/exchange/` §6.5, *Verdicts*).

8. **Records as they fall,** each at its moment in `CLAUDE.md`'s
   records table: an ADR, the Decisions Log, the devlog.

9. **When the list is closed, run the exchange-deliver Agent Skill.**
   - **Closed** means the first item under *Gates* below holds: a finding with no
     item reaches no verdict, and nothing else stops the Delivery
     Note going without it.
   - **The Delivery Note** is written from the CBC Run Reading's final
     state, every item's verdict in the CBC Run's order, and the
     Read-Through Commit from its first line.
   - **An early Delivery Note** may go before the list closes, since
     one alone is cheap. It is then written from the items as they
     stand, and says which are still open.
   - **The lessons** go first at the close, where they act: this Agent
     Rule, the CBC Run Reading's form, an Agent Skill, or TODO.
   - **The fast-forward:** then main takes the branch.
   - **The last commit** on main deletes the CBC Run Reading and adds
     the devlog entry.

## Gates

True when a CBC Run Reading closes. A CBC Run Reading's Plan Step checks its own items
against them (`PLAN.md`, the Plan Step Form's Known already).

- Every finding, and every line of what the CBC Run taught us, has
  ended in a decision or a work item, or says why it needs neither.
- Every work item has ended, taken, declined or held, and is marked
  in the CBC Run Reading with its commit.
- The Delivery Note, written from the CBC Run Reading's final state, is in the CBC Run,
  and names the commit read through.
- The CBC Run Reading's lessons sit where they act, or in TODO.

## Stages

For a CBC Run Reading's Plan Step, its Notes and its Now line:

1. read (the exchange-read Agent Skill);
2. decide and work (steps 1 to 8 here);
3. note (the exchange-deliver Agent Skill);
4. close (step 9).

When the CBC Run moves and the CBC Run Reading is extended, by the exchange-read Agent Skill again or by
the exchange-deliver Agent Skill's Stage 1, step 0, the Now line returns to read.

## What this does not cover

- **What a CBC Run Reading looks like** — `.claude/rules/exchange-reading.md`.
- **When a CBC Run Reading opens, extends, closes, or is overtaken** —
  `docs/conventions/exchange/` §6.3, *The CBC Run Reading* and §6.4, *How a CBC Run Reading closes*.
- **The CBC Run moving before the Delivery Note** — `.claude/skills/exchange-deliver/SKILL.md`, Stage 1,
  step 0.
- **How a commit plan runs** — `.claude/skills/commit-plan/SKILL.md`.

---

## Decisions

- `.claude/decisions.md`, 2026-10-01 — placed from the draft that
  ran three CBC Run Readings of CBC Run 3; why an Agent Rule beside the CBC Run Reading's form,
  and not that form, an Agent Skill, or the draft left standing
- `.claude/decisions.md`, 2026-10-08 — step 4: a taken item checked
  against its foundation, and its file read whole
- `.claude/decisions.md`, 2026-10-10 — step 9 and *Gates*: the list
  closes only when every finding has ended in an item
- `.claude/decisions.md`, 2026-10-17 — *Gates* and *Stages*: what a
  CBC Run Reading's Plan Step checks and moves through, in PLAN (ADR-0057)

<!-- DRAFT, provisional, 2026-09-25. What happens between read.md
     and deliver.md: the reading is worked. One firing behind it,
     the reading of run 3, which was paused with three items open.
     Written to see the whole picture, with what held, what must be
     watched, and what has not been thought about, kept apart. This
     is arrangement, not exchange: how this repo works a list, and
     it lands where standing rules live once it has run twice. -->

# Working a reading

Between the reading and the note. The exchange says only what each
item must end as; this is how the list gets there.

## How it goes

1. **Count it.** The reading lists F, D and W. How many W, and how
   many marked *plan*. More than one plan means a branch, cut from
   main after the reading is written — the reading is the thing
   that says whether the branch is needed, so it comes first.

2. **Order it, decisions first.** A D gates the W that rest on it.
   Settle the top D; it will reshape or delete Ws below. The order
   is preliminary and the reviewer reorders it — the last reading
   moved its second item to last, rightly.

3. **A decision is a proposed ADR, built, corrected while building.**
   Not a list of questions. The ADR opens Proposed under a commit
   plan, the plan's revisions are where the wording is corrected,
   and it flips to Accepted in the set's final records commit. This
   is what replaced `decide-first`, and it is what settled D1 last
   time in a way no question list did.

4. **A work item is a commit, or a commit plan.** One commit when it
   is one; a plan when it is not, with the reviewer at every
   boundary.

5. **Every close is followed by one pass over every open item.** F,
   D and W alike: does this close change it, close it, or block it?
   Mark each that it touches, in place, before the next item is
   opened. A pass over a list of twenty is minutes; the alternative
   is what happened last time — W4's set closed W6 and that was
   caught because the set ran into it, while W7's deferral took
   W8's home with it and nobody saw until the pause. The items are
   not independent, and the only cheap moment to find out how one
   moved the others is right after it moved.

6. **A changed line is an edit only if their log says so.** For
   every hunk the diff put on the reading, the first question is
   whether the run's decisions log records it. Recorded: the run
   edited it on purpose, and it is an item to decide. Not recorded:
   something went wrong at the take, and it is a defect of a
   different kind — a finding about the exchange, not about the
   copy. The diff alone cannot tell the two apart; only their log
   can. Twice the records read fine while the files were off.

7. **Each item ends as one of three**, where `exchange.md` §6 says
   each lands: taken changes a master here; declined puts its why
   in the reading, to go into the note; held takes a trigger and a
   line in our backlog.

8. **Records as they fall.** An ADR per decision with rejected
   options. The decisions log for any change to the arrangement.
   The devlog at a session's end, and at a pause.

9. **When the list is closed, `exchange-deliver`.** The note is written
   from the reading's final state — every item's verdict, in the
   run's order — and the read-through from its first line. Then the
   reading is deleted, the branch fast-forwards, and the devlog
   says so.

## What held, once

- **The list in `temp/`, not in `TODO`.** TODO accretes; a reading
  is edited down. The competitor was real and the choice was right.
- **Marked done in place, with the commit.** Items kept their
  numbers, so the file and a TODO line outside it could cite them.
- **The reviewer reordering.** The rule that would have written
  itself from expectation was moved to last, to be written from
  what the run taught. That was the reviewer's call and it was
  the correct one.
- **Written before the branch.** Ten items, four wanting plans; the
  count is what made it branch work rather than one plan.
- **The lessons section, written as it happened.** Six lines that
  became the reading's shape today. A section that exists to be
  harvested, and was.

## What must be watched

- **A pause is not a close, and it had no form.** The last reading
  stopped with three items open, and the stop was improvised — a
  banner in the file, a devlog entry, a branch left standing. It
  worked. It should be the form: the reading says *paused*, which
  items are open and why, and the devlog's resume line names the
  branch.
- **A delivery mid-list is allowed and dangerous.** W9 went down
  while W3, W8 and W10 were open, its note miscounted, and it was
  withdrawn the next day. Deliveries need not wait for the list to
  close — a note alone is cheap — but a note written mid-list must
  be written from the items as they stand *then*, and say which
  are still open.
- **One item's set can dwarf the reading.** W4 was twenty-three
  commits inside a ten-item list. The reading is a list of lists,
  and the count in step 1 undercounts by construction. Fine, as long
  as nobody reads the count as a size. An item that edits a skill
  both seats hold also undercounts: it is two commits, the agent's
  own files apart — W3 and W4 on 2026-10-01 were counted as one
  each.
- **The deliverer moves while the reading is paused.** The other
  direction, and it happened: the run-3 reading was paused on 09-24
  with three items open, and sixty commits here — three conventions
  gone, the exchange in — dissolved or moved every one of them
  while the run's side of the reading stayed true. A reading is a
  snapshot of two trees, and it rots from whichever side moves. The
  manual's §6 now says a reading can be **overtaken**: closed the
  same way, one pass over the open items, then deleted, and the
  next read starts fresh. Extending it would have meant marking six
  dead items in a 430-line file written before its own shape.
  Second firing of this document's subject; first thing it taught.
- **The run moves while the reading is worked.** Both sides moved
  from one pin. Before the note, `exchange-deliver` runs
  `exchange-read` on the span since the reading's first line;
  whatever the three things yield
  is appended — next numbers, the pass after every close on them
  too, the first line moved — and the whole is delivered once. The
  run sees only the final delivery; the intermediate work is in our
  history alone. The fork grows with delay on both sides, which is
  the cost of the unnamed trigger below.
- **Two readings at once.** The run-3 reading is paused on its own
  branch; this arrangement review is a second undertaking on a
  branch cut from it. Nothing says how two relate, which one moves
  main, or what happens to items open in the first when the second
  changes the ground under them — W3 and W8 both did change.
- **Sequencing against the arrangement.** W3 was held back because
  it would have landed in PLAN before the question of what PLAN is
  for. A reading's item can be blocked by a question outside the
  reading. The reading should say so on the item rather than
  silently reordering.

## Not yet thought about

- **When to read.** Today: when the reviewer says. A hand-off
  arriving? A step closing at the run? A calendar? The trigger is
  unnamed, and an unnamed trigger means readings happen when someone
  remembers.
- **More than one run.** Every rule here is written for one. A
  second live run means two readings with items that may be the
  same finding twice.
- **The reviewer's seat.** The reading's decisions are the
  reviewer's; the agent proposes and builds. That is how it has
  gone and nothing says it. It should, once — probably in the
  arrangement, not here.
- **The shape learning from the reading.** Section 7 of every
  reading feeds the shape. Who moves a lesson from the reading into
  the shape, and when — at the reading's close, or at the next
  reading's start?

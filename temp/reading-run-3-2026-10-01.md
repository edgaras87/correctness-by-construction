<!-- The reading of run 3, opened 2026-10-01 by exchange-read. Stays
     here, edited in place; closes when its items end, and the note
     carries its verdicts and read-through. Cites our own paths and
     decisions freely; nothing in it goes to the run. -->

Run 3, `never-oversold`, read through `c33a996`.

## 1. Where we read to

- **Read through:** `c33a996`, the run's `HEAD`. The repository is
  `~/IdeaProjects/cbc-pure-run-3`.
- **Previous read-through:** `9869798`, carried by our note of
  2026-09-30 and now in the run's decisions log, its first.
- **The span `R..HEAD`:** 41 commits, all 2026-10-01.
- **The pin:** `0000855`, taken at the run's `be77f79`, its names
  swept at `3f71d19`. No receipt branch was cut;
  `housekeeping-bundle-0000855` is the take's work branch. The
  copies' diff is against `3f71d19`.

## 2. What the run did

It took the delivery @ `0000855` first, on its own branch: the
note's counts checked before anything moved, 24 copies replaced,
one added, five removed by name, and its PLAN swept of a name the
writing pass had moved. Its TODO gained `## To the deliverer`, and
its asks moved there from Later.

Then four housekeeping sets before Step 7, each on a branch from
main: SL-1's tests took a header each in SL-2's form; the writing
sweep reshaped SL-1's record to the slice-record shape and settled
the shape's face tables as blocks; a documentation error check read
all 23 records against the code, eighteen findings, fourteen fixed;
and its four open decisions were settled — ADR-0012, an adjustment
answers 200, among them.

Nothing stands before Step 7 on its side. Its devlog: "the reviewer
checks the bundle's side first, then SL-3."

## 3. Findings

Edits to copies: none. All 38 copies equal our masters at
`0000855` byte for byte, and the run holds no copy we did not
send.

Entries in its decisions log:

- **F1** — the take @ `0000855` (2026-10-01): the note's counts
  held, 24 differ, 1 new, 5 gone; all four of its edits had a
  verdict, so none re-applied; the five deleted by name;
  conventions held as copies from seven to three. One commit,
  `be77f79`, held `.claude/` and `docs/concept/` together.
- **F2** — the slice-record shape takes the faces weighed for a
  guarantee as blocks (2026-10-01). `visual-comparison` ran on
  SL-2 §8's G5 table against six requirements; the render step was
  skipped on the reviewer's call; recorded in its decisions log,
  not an ADR "as the skill says", because the shape is agent-side.

Asks and offers, under *To the deliverer*, in its order:

- **F3** — retrospective: Release reshaped at birth, fold back to
  the playbook. Unchanged since the note; held there.
- **F4** — retrospective: four arrangement pieces on trial from
  Step 1. The fifth it once carried is now settled as
  `delivered-copies.md`. Held there.
- **F5** — retrospective: gate items ticked as they come true,
  `[~]` while the step runs. Unchanged; held there.
- **F6** — offer: its slice-record shape, which has moved since the
  note — a third part, the faces as blocks (F2). "Nothing owed
  here."
- **F7** — answer: SL-2 did not lean on the facility paragraph; it
  faces no race, and its first three guarantees reuse SL-1's
  comparison of faces.
- **F8** — answer: the absence rung met again, in SL-2's G5 and G6,
  each guarded by a test that reads the source. Said as promised;
  "not that trigger".
- **F9** — framing steps as commit series, and the imperative test:
  "being weighed there now"; its reading of the imperative split is
  where they start. Nothing owed.
- **F10** — information: `decide-first` and `option-comparison`
  were used in its writing pass, 2026-09-21..23 — the first showed
  the commit count was not yet sayable, the second built five
  wordings of SL-2's G1 and caught that its labels were already
  there. `visual-comparison` calls the general method "discarded
  2026-09-24, unused".
- **F11** — ask: which rule wins when a take covers `.claude/` and
  `docs/concept/`. `delivered-copies.md` takes them as one act
  under one pin; `commit-messages` says a commit touching
  `.claude/` touches nothing else. The take followed the first and
  broke the second (`be77f79`). Say which gives way, or how the
  take is split.
- **F12** — ask: the staging arrives owner-only, `drwx------`;
  taken with `cp -a temp/<staging>/. .`, it set the repository
  root from 755 to 700, and git shows nothing. Stage it readable,
  or have `delivered-copies.md` rule 5 say to copy the files and
  not the folder's attributes.
- **F13** — information: `commit-plan`'s sweep for moved names
  found two stale pointers in its PLAN on first use, at the take.

Findings from reading it against our tree:

- **F14** — F12's cause is ours: `exchange-deliver` step 2 stages
  into `mktemp -d`, which is 700, and step 3's `cp -r` carries the
  mode to `temp/bundle-H`.
- **F15** — F11's two rules both ship in our container:
  `.claude/rules/delivered-copies.md` rule 5, and
  `commit-messages`' *The agent's own files*. Our own TODO already
  holds an open decision on that section's commit types.
- **F16** — F10: the count behind both discards (ADR-0030's Status
  line; `.claude/decisions.md`, 2026-09-24) was firings here; it
  did not include the run's, which no reading had read.
- **F17** — F2: `visual-comparison` step 6 says the outcome is recorded
  in an ADR; the run recorded an agent-side outcome in its
  decisions log instead.
- **F18** — F7 answers half the trigger of our TODO item on
  `infra-establish`'s facility paragraph: run 3 says SL-2 did not
  lean on it. The other half, a second run, stands.
- **F19** — our TODO item "Should a run's decisions-log entries be
  shorter?" fires at this reading: the span's two entries run 32
  and 33 lines.

## 4. What the run taught us that we had not thought of

- A staging's own attributes travel with it: a copy that is
  byte-identical can still change the run's tree outside any file
  (F12, F14).

## 5. Decisions

None proposed yet.

## 6. The work

None proposed yet.

## 7. What this reading taught

- A run's work branch named for a delivery is not a receipt branch;
  the copies' diff base is the commit that finished the take.

## 8. Notes

- Nineteen findings, none closed. Nothing decided.
- Not addressed to us, so not items: its TODO's "seeing what
  changed between versions", once a question of whether to hand it
  to us, now sits in its Later as the learner's own; and its two
  structure ideas, held for its Release.
- Nothing in the run was written to.

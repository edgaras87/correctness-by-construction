<!-- The reading of run 3, opened 2026-10-10 by exchange-read. Stays
     here, edited in place; closes when its items end, and the note
     carries its verdicts and read-through. Cites our own paths and
     decisions freely; nothing in it goes to the run. -->

Run 3, `never-oversold`, read through `c7073c7`.

## 1. Where we read to

- **Read through:** `c7073c7`, the run's `HEAD` on `main`.
- **Previous read-through:** `10437cd`, carried by our note of
  2026-10-08 and recorded in the run's decisions log.
- **The span `R..HEAD`:** 33 commits — the take of `f801fd0` (three,
  checked in our devlog 2026-10-08, later), then Step 8, SL-4, whole,
  and its hand-off.
- **The pin:** `f801fd0`. No receipt branch; the copies' diff is
  against `1e736ca`, the commit whose decisions entry records the pin.

## 2. What the run did

It took `f801fd0` on 2026-10-08 in two commits, the chapters first,
and dropped from TODO the lines our note answered.

Step 8, SL-4 — consume's two moves hold together — opened on
2026-10-09 on its own branch, written from the run's step form, and
closed on 2026-10-10. The wall already stood (SL-3 made consume one
statement in one transaction), so the slice built proof, not
structure: a harness that holds a consume mid-work on a row lock,
kills its instance outright, freezes the store, ends one session.
It built one answer at the door, ADR-0016: an outcome the ledger
cannot know answers 503. Its first placement was refused by two
standing structural rules from SL-1 and SL-2, so the ledger
classifies it instead. §8 was revised twice: a killed instance's
waiting session lingers until its wait ends; and the red as signed
stayed green, so the red removes the single transaction and V3
together. 100 tests, up from 83.

At the opening, ADR-0016 was committed Accepted, then put back to
Proposed on the reviewer's question; `cbc-slice` was edited so that
every slice works this way. At the close, the evidence-test shape
took two lessons from its second reading, and the slice-record
shape's reading found only output drift. A lesson drafted for
`cbc-slice` — try a plan's claims about behaviour before signing it
— was dropped on the reviewer's reasoning: a dated revision is how
the method already handles that.

Every registry slice is now closed. Step 8 reached main by
fast-forward, and the reviewer pushed it. The hand-off waits for our
note; then Release, its gate derived when it opens.

## 3. Findings

- **F1** — `cbc-slice`, one edit in SKILL.md's Stage 1 and the
  workflow's Stage 1 step 3 (`0069200`; decisions log 2026-10-09):
  a decision that a slice records as an ADR at its opening is
  Proposed until the slice's closing records, then Accepted. The
  build can still reshape it, and a Proposed ADR is corrected in
  place. Rejected there: a TODO line, a `commit-plan` rule, a PLAN
  line alone, a memory. Asked under *To the deliverer*.
- **F2** — The run's evidence-test shape (`.claude/rules/
  evidence-test.md`, its own and not a copy; our Next item) moved at
  its second reading (`a47f129`). The slice's own invariant is
  asserted after the promise and before the numbers, where it is not
  the promise itself. A reading whose parts must agree is taken in
  one read. The skeleton went from four steps to five, and the
  file's dated lines say what taught each lesson. No decisions
  entry, since it is not a copy; its *To the deliverer* line was
  updated (`968abae`).
- **F3** — Run 3's next step is Release (its TODO, Next): no slice
  is left. These of our items trigger on it: the frozen CLAUDE
  template's stance bullets read against the run's entry file;
  sorting `docs/baselines/` by kind, where the Spring slice
  reference opens. The run's retrospective, at its project end,
  holds three of its own asks to us.
- **F4** — Two of our Next items trigger on "run 3's Step 7
  closing": folding its step form into the run playbook, and
  weighing its two standing rules. Step 7 closed on 2026-10-07 and
  Step 8 has since run on the same form, yet neither item fired at
  the last reading. The run holds both under *To the deliverer*
  until its retrospective.
- **F5** — SL-4's E4 is a fifth rule in `NoSecondWayOutTest`, a test
  that reads the ledger's source: a statement writes a `consumed`
  receipt exactly when it lowers the count. The run's new known
  issue calls it the one split the store cannot see. It is one more
  guarantee guarded by reading the source, which bears on our
  absence-rung item (Later). It comes from the same run, so it is
  not that item's trigger.
- **F6** — Its *To the deliverer* line on commit series and the
  imperative test says "nothing owed here". On our side, ADR-0049
  settled both on 2026-10-09, and our devlog says the next note
  answers it.
- **F7** — The run's devlog is one file of 1,752 lines. Its header
  carries the same "when this file gets long, split" line that ours
  did, and ours went unnoticed until 5,515 lines (devlog 2026-10-09).
  The run has not asked about it.
- **F8** — The other seven lines under *To the deliverer* stand
  unchanged since our last note: three retrospective items, the
  slice-record shape, `infra-establish`'s facility paragraph, the
  absence rung, rules on trial, the glossary. Each is held on our
  side with a trigger.

## 4. What the run taught us that we had not thought of

- A slice whose wall already stands owes proof only, and its red has
  to take away every wall in the way. That includes a backstop: the
  red as signed stayed green, and the evidence went red only once
  the single transaction and V3 were both gone. V3 was seen catching
  both orders on its own.
- A slice's invariant can be narrower than the promise and break
  while the promise holds (R ended, the count unmoved). Two readings
  can each be true while their pairing is false, which is why
  readings that must agree are taken in one read.
- Earlier slices' standing structural rules refused a later plan's
  placement (the 503 in `DoorProblems`), and they were right. The
  guards caught the plan, not only the code.
- For the worked example (`docs/conventions/exchange/` §6.3): it
  has no slice that inherits its wall, and none whose adversity is
  our own death or an unknown outcome. Whether it should is open.

## 5. Decisions

- **D1** — Take, decline or hold F1. It rests against `commit-plan`'s
  rule that an ADR inside a set opens Proposed
  (`delivery/container/.claude/skills/commit-plan/SKILL.md`), and
  against `concept/04-cbc-slice.md`. It gates W1. **Settled
  2026-10-10: taken**, on the reviewer's word. Our master differs
  from the run's copy by this edit alone.
- **D2** — When the Release-triggered items (F3) and the two Step 7
  items (F4) are worked: now, at run 3's Release opening, or at its
  retrospective. It gates W3. **Settled 2026-10-10: none now**, on
  the reviewer's word. F4's two items move their trigger to run 3's
  retrospective, where the run holds them, and say the form has run
  two steps; F3's keep theirs, not yet due.
- **D3** — F7: whether the note says anything of the run's devlog.
  **Settled 2026-10-10: one optional line**, on the reviewer's word —
  its header asks for the split, and the run can check the count.
- **D4** — §4's worked-example line: whether the example gains a
  slice that inherits its wall. **Settled 2026-10-10: held**, on the
  reviewer's word — one run's slice; a TODO line (W5).
- **D5** — §4's first line, as a lesson for `cbc-slice`: a red that
  removes a standing wall removes the backstop behind it too.
  **Settled 2026-10-10: held**, on the reviewer's word — the run
  proposed no edit, and one slice is one case; a TODO line (W5).

## 6. The work

- **W1** — If D1 takes F1: the edit into
  `delivery/method/.claude/skills/cbc-slice/`, both files, checked
  against its sources and read whole. **Done** in `2f24dcd`.
- **W2** — TODO brought true: the evidence-test item's context for
  F2; F5 into the absence-rung item's context; F4's two items
  retriggered as D2 settled. **Done** in `50d5709`.
- **W3** — The items D2 makes due, each by its own trigger. Closed
  by D2: none is due, and the retriggering went to W2.
- **W4** — The note, read through `c7073c7`: F1's verdict, F6's
  answer, the held lines acknowledged, and D3's line. **Done** in
  `5361213`, staged into the run's `temp/` as `bundle-5361213/`.
- **W5** — TODO gains D4's and D5's held lines. **Done** in
  `224e6b7`.

## 7. What this reading taught

- Two starting points disagreed. Our devlog said the next reading
  starts from `de29d9e`, the run's last take commit; the run's
  delivery entry says `10437cd`. The skill takes the entry's, so the
  three take commits came back into the span, already checked. No
  rule: the devlog's Resume names the run's read-through instead.
- A finding and a §4 line can end with no D or W, and nothing
  stops the note going without them. F7 and two §4 lines did, until
  the reviewer asked, before the note was committed, whether all
  was taken. Placed in working a reading's step 9 (`ddf2d73`).

## 8. Notes

- Counts: 33 commits, 3 of them the take; 2 decisions entries; 1
  copy edited (2 files); 1 of the run's own shapes moved; 10 lines
  under *To the deliverer*, 1 new and 1 moved.
- Read only: nothing in the run was written to. Its `temp/` is empty.
- Not read, as not required: SL-4's 928-line record, the code, and
  ADR-0016 past its opening. The devlog and PLAN were enough for §2.

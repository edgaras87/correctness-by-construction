<!-- The reading of run 3, opened 2026-10-08 by exchange-read. Stays
     here, edited in place; closes when its items end, and the note
     carries its verdicts and read-through. Cites our own paths and
     decisions freely; nothing in it goes to the run. -->

Run 3, `never-oversold`, read through `10437cd`.

## 1. Where we read to

- **Read through:** `10437cd`, the run's `HEAD` on `main`.
- **Previous read-through:** `65aa18d`, carried by our note of
  2026-10-02 and recorded in the run's decisions log.
- **The span `R..HEAD`:** 46 commits — the take, SL-3 whole, and the
  review after it.
- **The pin:** `a3b6b8c`, taken at the run's `fa9a402`. No receipt
  branch; the copies' diff is against `fa9a402`.

## 2. What the run did

It took the delivery @ `a3b6b8c` in one commit on 2026-10-02, the
note's counts holding, and opened Step 7 the same day.

SL-3, a reservation exits once, ran from its specification to its
close: receipts for ended reservations, the consume and release
doors, expired holds freed before each decision, a units-held check
in the store (V3), a test reading the ledger's exits as SQL (E7).
Its close ran the shape check for the first time, and the slice-
record shape took what it found.

A review after SL-3 followed on its own branch, now on `main`: who
writes the store (the definition's T4, ADR-0014), the size the
system is built for (the runtime ground), an index every decision
needs (ADR-0015, V4), where each rule lives. It ended by correcting
four delivered copies in place. Step 8, SL-4, is chosen-next.

## 3. Findings

Edits to copies, each with its entry in the run's decisions log:

- **F1** — `delivered-copies.md` rule 5 (2026-10-05): the take removes
  the staging — the hash's directory and its note — and nothing else,
  where it said "empty `temp/`". A reviewer's draft kept in the run's
  `temp/`, untracked, would have gone with the next take.
- **F2** — `cbc-slice`, five edits in SKILL.md and the workflow's
  Stages 2–3 (2026-10-08): the escape-hatch hunt aims at the
  definition's trust list; a face's cost says the size it assumes;
  a red counts only if it fails on the witness; a race's held-open
  window lives on the red tree only; a third test kind, the wall's
  own check, beside evidence and tripwire.
- **F3** — `cbc-framing`, two edits in the workflow's Step 2 and
  SKILL.md, a finished copy (2026-10-08): the trust list answers who
  besides the system can write what it stores; the runtime ground
  gains a sixth line, the size the system is built for.
- **F4** — `infra-establish`'s PostgreSQL walkthrough, the hand-off,
  a finished copy (2026-10-08): the inspection identity is the
  writing one; the project says whether the trust list covers people
  reading with it, or a read-only identity is made at bootstrap.
- **F5** — `commit-plan`, two edits (2026-10-08): planned subjects
  counted against the limit when the plan is written; a change to
  the agent's own files is its own step, never inside a records
  step.

Files the run wrote, offered under *To the deliverer*:

- **F6** — the evidence-test shape, `.claude/rules/evidence-test.md`,
  181 lines, scoped to `src/test/**`, exposed at once (2026-10-07).
  Skeleton marked apart from illustration. Whether it reaches another
  project, hidden or exposed, is asked of us.

Asks and offers, under *To the deliverer*:

- **F7** — two lessons for the chapters. Framing: the trust list
  never asks who else writes the store, and nothing asks the size.
  Walls: a right withheld from an identity is a wall in the store's
  grant system; the single-entry-path rung holds only while a trust
  line names that path the only writer.
- **F8** — a question: should a rule, not only a shape, be
  deliverable hidden or on trial until a second project reaches it?
- **F9** — the method has no glossary: tripwire, witness, fold,
  fence, possession appear only in the skills, never in the
  chapters; the wall's own check joins them.
- **F10** — the held lines stand as our notes left them: three
  retrospective items, the facility paragraph, the absence rung, the
  commit-series and imperative questions ("being weighed there
  now"). The slice-record shape moved twice more: dated labels for a
  face revised after signing (2026-10-07), a face's assumed size and
  a backstop seen or unproven (2026-10-08).

From the read itself:

- **F11** — the take and the run's `temp/`: our staging is gone, and
  `temp/` holds the run's own draft, untracked. Our `temp/` is
  tracked; no shipped text says which it is.
- **F12** — our TODO's trigger fired: the run's decisions log names
  the pin `a3b6b8c`, so the note to run 3 is due to go. Fixed in
  `3b319c6`.

What the run teaches the worked example:

- **F13** — read against F2 and F3, the example would contradict
  the skills it ships in. Its census says "no trust-lines"; its
  runtime ground has five lines and no size; its escape-hatch hunt
  ("any admin insert path must go through the same
  constraint-guarded table") is the walled-by-default answer F2
  names; its build gate says nothing of a red on the witness.

## 4. What the run taught us that we had not thought of

- A framing silence is paid for by a slice: nobody said who else
  writes the store, so SL-3 walled against scripts that could remove
  the wall. The cautious default has no end.
- Size belongs to the framing: a face's cost is true at some size,
  and without one on record no plan can say what it assumes.
- A wall can be shown standing without creating adversity — a kind
  of test the method had no word for.

## 5. Decisions

- **D1** — `cbc-slice`'s five edits (F2): each taken, declined or
  held. The first rests on D2's trust question. Settled: taken
  whole, D10 with it in one commit.
- **D2** — `cbc-framing`'s two edits (F3). Gates D1's first edit, D3
  and D4's framing half: the skill asking what the chapter does not.
  Settled: taken whole, the worked example with it, in `6389120`;
  the chapter is D4's.
- **D3** — `infra-establish`'s hand-off (F4). Rests on D2. Settled:
  taken whole.
- **D4** — the chapter lessons (F7): a concept change, so an ADR and
  the version question (ADR-0003). Touches TODO's absence-rung item
  (Later), whose trigger this is not. Settled: taken, the walls half
  only, under ADR-0048, its shape decided in the chapter's text; the
  framing half is already L1's line on accepted trust.
- **D5** — `delivered-copies.md` rule 5 (F1), with F11: whether a
  run's `temp/` is tracked, and TODO's "Ship `temp/` in the
  container, or stop telling runs to use it". Settled: taken whole,
  the exchange manual first, since it says `temp/` is emptied at the
  take; our `exchange-deliver`, which stops on a run's non-empty
  `temp/`, with it. The manual already calls a run's `temp/`
  untracked; the TODO item is made true for that.
- **D6** — `commit-plan`'s two edits (F5). Meets TODO's due items:
  the 50-character limit, one mood, commit series. Taking it opens
  commit-plan, which fires two Later items: grep the unwrapped
  text, and one meaning for "step". Settled: taken whole, the
  manual's reasons with the master, then our copy; the two fired
  Later items are the next set's, with the three due commit
  decisions.
- **D7** — the evidence-test shape (F6): ours to hold, hidden or
  exposed, and in which group. TODO's "Decide our own side of
  shapes" has this as its trigger. Settled: held — one run's tests,
  as the slice-record shape is held. Trigger: the next birth's first
  slice, its evidence tests read against the skeleton. D1 takes two
  of its lessons.
- **D8** — a rule on trial (F8): a question for the shapes
  convention. Settled: held with D7, until there is a rule we would
  deliver that way.
- **D9** — a glossary (F9): whether, and where — a chapter, or
  beside them. Settled: held. Trigger: Release's README gate.
- **D10** — the worked example (F13): follows D1 and D2. Settled:
  its framing half in `6389120`, its slice half with D1.

## 6. The work

- **W1** — delete the note to run 3, `temp/note-to-run-3-2026-10-02.md`,
  and TODO's line for it (F12). Done in `3b319c6`.
- **W2** — **plan** — the masters change for whatever D1–D10 take.
  Under `COMMIT-PLAN.md`, opened at `633ea25`.
- **W3** — the note to run 3: every verdict in the run's order,
  read through `10437cd` (`exchange-deliver`).
- **W4** — records: TODO lines for what is held, the devlog.

## 7. What this reading taught

- Finding the run took a search of the disk: nothing here names
  where a run's repository lives
  (`~/IdeaProjects/cbc-pure-run-3`).
- The reading checked each copy against our master, and never the
  master against what it derives from. The reviewer asked whether
  conventions and concepts were touched; two manuals were, and our
  own `exchange-deliver` would have stopped the next delivery.

## 8. Notes

- Counts: 13 F, 10 D, 4 W, one marked plan.
- Every hunk in the copies' diff has its decisions entry — no
  finding about the take (`.claude/rules/working-a-reading.md`,
  step 6).
- Our masters have not moved since `a3b6b8c`, so the run's diffs
  apply to them as they stand.
- The run's TODO *Now* says the review waits on its merge; `main`
  already holds it. The run's own line, not addressed to us.

<!-- The reading of run 3, opened 2026-09-30 by exchange-read. Stays
     here, edited in place; closes when its items end, and the note
     carries its verdicts and read-through. Cites our own paths and
     decisions freely; nothing in it goes to the run. -->

Run 3, `never-oversold`, read through `9869798`.

## 1. Where we read to

- **Read through:** `9869798`, the run's `HEAD`.
- **Previous read-through:** `9869798`, the reading of 2026-09-24,
  overtaken on 2026-09-26 and deleted without a note. The run's
  decisions log records no read-through; the devlog of those days is
  where the number comes from.
- **The span `R..HEAD`:** empty. The run has not moved.
- **The pin:** `4c3ac99`, both halves, taken at the run's `76e14e1`.
  Since then 46 run commits, and 323 here.

## 2. What the run did

Nothing since the last reading. Since the pin, and read then: SL-2
closed; its record was rebuilt and a shape kept from it; the shape
got a rule of the run's own and a word in `artifact-kinds`; the slice
skill was edited twice; the Now of TODO carries three items before
SL-3.

Because the last reading closed without a note, nothing the run
addressed to us since the pin has had a verdict. Its items are read
again below, from the run's tree as it stands.

## 3. Findings

Edits to copies, each recorded in the run's decisions log:

- **F1** — edit, `cbc-slice` SKILL.md and workflow Stage 3 (2026-09-21):
  each test says beside itself what it is for; a test that cannot
  fail for the invariant says it is a tripwire, and a tripwire never
  discharges a kill.
- **F2** — edit, `cbc-slice` SKILL.md and workflow Stage 4 (2026-09-22):
  at a slice's close, what it made is read against the project's
  shapes, each difference proposed as a diff, never corrected.
- **F3** — edit, `artifact-kinds` (2026-09-22): a *shape* entry beside
  specification, its force positional.

Asks and offers, in its TODO's Later (it has no *To the deliverer*
section):

- **F4** — ask: evaluate its changes to `cbc-slice` and `artifact-kinds`
  since `4c3ac99` — F1 to F3.
- **F5** — offer: its slice-record shape, `.claude/shapes/slice-record.md`,
  as a finding; the skeleton general, the illustrations its own.
- **F6** — ask: be the collector — hold unexposed shapes, stage them
  with a note at a gate; exposed shapes ship, unexposed never.
- **F7** — offer: its `.claude/rules/shapes-lifecycle.md` as a
  convention candidate, with two questions — whether
  agent-arrangement learns about shapes, and whether default gate
  items belong to the playbook.
- **F8** — retrospective: Release was reshaped at birth; fold it back
  to the playbook.
- **F9** — retrospective: four arrangement pieces on trial from Step 1
  — one branch per step, the kit with its settings gate rejected,
  `CLAUDE.local.md` holding the pace, the entry file under
  `.claude/` — fold back to their source, us.
- **F10** — retrospective: a fifth piece from Step 6 — gate items
  ticked as they come true, `[~]` while the step runs.
- **F11** — hand-off, `infra-establish`: a facility paragraph in the
  contract; held by us on 2026-09-17, "say so if SL-2 does".
- **F12** — hand-off: our note of 2026-09-20 named two items pointing
  at the handbook and there were three; grep the whole span.
- **F13** — the trail of four items held by us on 2026-09-20: the
  absence rung; the Spring slice reference; framing steps as commit
  series; the imperative test.

Findings from reading it against our tree:

- **F14** — our container ships `.claude/rules/shapes-lifecycle.md`,
  the path of the run's own rule (F7). A take lands ours over its
  own.
- **F15** — the run holds four conventions deleted here
  (`artifact-kinds`, `convention-lifecycle`, `decide-first`,
  `option-comparison`) and its own `skills-changed-in-place.md`,
  which `delivered-copies.md` replaces. A copy carries no absence
  (exchange §3.6); each needs naming.
- **F16** — the take is governed by the rules the run holds now,
  `convention-lifecycle` §3 and `skills-changed-in-place.md`, not
  by `delivered-copies.md`, which arrives in the same staging.
- **F17** — the run's decisions log records no read-through; this
  note's is the first it will hold.
- **F18** — its asks sit in Later in the old hand-off form, where
  `exchange-read` step 3 reads a *To the deliverer* section.
- **F19** — two items we told the run we hold have no home here: the
  facility paragraph (F11, held 2026-09-17) and framing steps as
  commit series (F13, held 2026-09-20). No TODO line, no trigger;
  ADR-0033 mentions the first in passing.

## 4. What the run taught us that we had not thought of

- A delivery can land on a path the run wrote itself (F14). §3.4
  checks that no path is claimed twice among our groups; nothing
  checks a run's own files.

## 5. Decisions

Proposed; the reviewer's.

- **D1** — F14: our `shapes-lifecycle.md` lands over the run's own at
  the same path, as its rule taken and reshaped — or ships under
  another name. Proposed: it lands over it, and the note says so by
  name; the run's SL-2 example and `temp/` path are its own and stay
  in its records. Gates W1.
- **D2** — F8, F9, F10: fold-backs addressed to the run's
  retrospective, which has not run. Proposed: held until it runs;
  nothing owed now. Gates W1.
- **D3** — F5: evaluate the slice-record shape now, or keep it held
  under our TODO "Decide our own side of shapes", whose trigger is a
  first shape ours to hold. Proposed: held, with that trigger.
  Gates W1.

## 6. The work

The verdicts that need no decision, from records here:

- F1, F2 — taken, reshaped, `f2d9477` and `16868ea` (2026-09-23); the
  run's copy lands whole.
- F3 — taken into the shapes convention (ADR-0037); `artifact-kinds`
  itself is gone (F15).
- F4 — answered by F1 to F3.
- F6 — the role declined (ADR-0035 decision 10); what we do instead:
  an exposed shape ships in the group of what it shapes, an
  unexposed one is held apart and never ships.
- F7 — taken, reshaped: the shapes convention, and its shipped rule
  at the same path (D1). Its first question: the arrangement names
  `.claude/shapes/`. Its second: every playbook step carries a
  shapes line, which reaches a run at its next birth, since a plan
  is the run's own.
- F11 — held still: the run says whether SL-2 leaned on the
  paragraph. Its home here is W2.
- F12 — taken: a sweep of every old path and number is now
  commit-plan's rule.
- F13 — the absence rung, held, in our TODO with its trigger; the
  Spring slice reference, a baseline, sorted at run 3's Release
  reading; framing steps as commit series, held, its home W2; the
  imperative test, due in our TODO now.

Work:

- **W1** — the note and the staging, `exchange-deliver`: the
  verdicts above and D1 to D3's; the four deletions and the rule
  replaced, by name (F15); the take under the run's current rules
  (F16); the first read-through (F17); asks under a *To the
  deliverer* section from now on (F18); and our side's changes
  since the pin. One commit for the note, the staging on the word.
- **W2** — F19: a TODO line each for the two held items, with the
  triggers we gave the run. One commit, before W1, so the note's
  "held" points at something.
- **W3** — §4 and §7 here: a take can land on a run's own path, and
  an overtaken reading leaves asks unanswered. Proposed: a TODO line
  each, weighed later; not fixed in this reading.

## 7. What this reading taught

- A reading overtaken without a note leaves the run's asks with no
  verdict; the next reading reads them again whatever its span.

## 8. Notes

- Nineteen findings, none closed; three decisions proposed; three
  work items, none needing a plan, so no branch. Our side's changes since the pin, the
  note's other half, are the note's to list: 42 files under the
  copies' paths, and the list gathered in the devlog's Resume lines
  of 2026-09-28 and 2026-09-29.
- Nothing in the run was written to.

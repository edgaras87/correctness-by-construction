<!-- The reading of run 3, opened 2026-10-15 by exchange-read. Stays
     here, edited in place; closes when its items end, and the note
     carries its verdicts and read-through. Cites our own paths and
     decisions freely; nothing in it goes to the run. -->

Run 3, `never-oversold`, read through `dac4dd1`.

## 1. Where we read to

- **Read through:** `dac4dd1`, the run's `HEAD` on `main`.
- **Previous read-through:** `c7073c7`, carried by our note of
  2026-10-10 and recorded in the run's decisions log.
- **The span `R..HEAD`:** 42 commits. The take of `5361213` and a
  devlog split (2026-10-10), the polish's pass 1 (10-11), Step 9, the
  retrospective (10-12), Step 10, applying it (10-13 to 10-15, landed
  as 16 commits), and the polish folder removed.
- **The pin:** `5361213`. No receipt branch; the copies' diff is
  against `c07b57e`, the commit whose decisions entry records the pin.
- **Where the run's hashes point:** RETRO.md and the decisions log cite
  the ~180 small commits on `step-10-apply-retro-detail`, kept off
  main. Main's copies equal that branch's tip, file for file.
- **Our side:** nothing under `delivery/` has moved since `5361213`, so
  every edit below sits on exactly what we hold.

## 2. What the run did

It took `5361213` on 2026-10-10 in one commit, both copies changed,
and dropped from TODO the two lines our note answered. Its devlog
split by month, as ours did.

On 2026-10-11 the polish ran its pass 1 over the records: code
comments and records made true after SL-4, `pom.xml` to 0.4. The
reviewer then stopped the polish after pass 1, in favour of a
retrospective.

Step 9, the retrospective, closed on 2026-10-12. It walked run 3 in
ten parts, in the order the run built them, and wrote 29 decisions in
`RETRO.md`. Each has an example from the run and says where it lands.
Its title is "what run 4 does differently": run 4 is the same project,
rebuilt from the start, from the bundle. Two rules and a skill of the
run's own came out of it: `writing.md`, `one-home.md` and
`retrospective`. TODO's *To the deliverer* lines now point at the
decisions that answer them, and the decisions log opens on a list of
rules in force.

Step 10 applied the retrospective to run 3 itself, from 2026-10-13 to
10-15. Every decision got a triage row: applied here, partly, or next
run only. One commit plan of about 180 small commits, landed as 16.
The slice records were regrouped to one block per guarantee, tags
given their owners, tests moved into folders by kind, the records
rewritten plain three times, and a glossary written. Seven of our
copies were edited from the run's evidence; four of them the run has
finished with, so their edits are marked untried. It added four shapes
in `.claude/shapes/`, a check script, and a second skill of its own,
`apply-retrospective`. 100 tests green, as at Step 8.

Its TODO's *Now* is our re-check, from main: RETRO.md and *To the
deliverer*. Release opens after it.

## 3. Findings

- **F1** — `cbc-framing`, three edits, each logged 2026-10-14 and
  untried (the run will not frame again): tags in full words, one
  spelling everywhere (`55887bd`, RETRO D6); each step's result written
  once, straight into its export as a draft, the derivation linking to
  it, the close copying nothing (`07cf9ab`, D7); the registry
  template's entry with every field, a Record link, one line per close
  (`8db57c0`, D5, D29). The tags touch the worked example, which is
  still byte-identical in both skills.
- **F2** — `cbc-slice`, five edits, logged 2026-10-14 and untried:
  tags in full words (`d023336`, D6); the record's skeleton, one block
  per guarantee (`0a8b1a9`, D12); evidence checks the promise, then
  the invariant, before any number, and the red run notes each
  backstop seen or unproven (`f49a71e`, D13, D18); the close writes
  one registry line and ARCHITECTURE rows, never a paragraph
  (`a291147`, D5, D16); SKILL.md says what to do and each gate, the
  workflow only the why and examples, both plain (`2794ac6`, D21,
  D2). SKILL.md 1,744 to 1,887 words; the workflow 2,438 to 1,542.
- **F3** — `cbc-bootstrap`, three edits, logged 2026-10-14 and
  untried: the requirements point to the record that decided each
  constraint and end as history at the close, ARCHITECTURE answering
  what a slice may rely on (`7007337`, D10); the harness's form is
  chosen by what ships, not by cost (`a2a776e`, D26); the skeleton
  places tests by kind (`2a05394`, D27).
- **F4** — `infra-establish`, one edit, logged 2026-10-14 and
  untried: the ground proves the engine and what the store promises,
  each constraint seen refused and the facility a slice will need
  (two writers on one row, one made to wait); a lever the evidence
  pulls is proven by the harness that pulls it (`1cadda1`, D9). It
  touches our Later item on `infra-establish`'s facility paragraph.
- **F5** — `commit-plan`, one edit, logged 2026-10-15, lived in Step
  10 (`3daf0fb`, D19): small commits inside a planned commit, folded
  at its boundary or grouped by kind at the end, kept on
  `<branch>-detail`; a look back at the landed commits before the
  close; a commit inserted later takes a letter (`8b`); a planned
  commit may repeat over a set, with an order and a stop rule; small
  commits follow `commit-messages` when written.
- **F6** — `delivered-copies.md`, two edits, logged 2026-10-14
  (`c6d21b8`, D28; `128801b`, D2): rule 1 lets a concept chapter be
  edited as any copy, only from a mistake lived in the run; a finished
  copy is fixed whenever the evidence is in the run, its hand-off line
  marked "untried here"; then written plain, each rule keeping its
  number. The run names the reversal of ADR-0036's chapter clause and
  asks us to accept it, or decline with why. No chapter was edited.
- **F7** — `shapes-lifecycle.md`, three edits (`d194038`, `e0169dd`,
  `cdfc432`; D18, D29), logged 2026-10-13 and 10-14: shortened to what
  run 3 used; every shape in one folder, `.claude/shapes/`, read at the
  closing gate only; no hidden and exposed places; a fourth way a
  difference ends, a new shape; the `temp/` staging dropped; a shape
  that names work must be asked for by the skill that runs it; a shape
  starts from a look at its examples for what they all lack. The first
  entry cites "commits 4, 5 and 5b", not hashes.
- **F8** — Files the run wrote, offered whole: `writing.md` and
  `one-home.md`, always loaded (D1, D2); `.claude/checks/records.py`,
  178 lines of Python run at every close (D17); the `retrospective`
  skill and manual (D23); the `apply-retrospective` skill and manual
  (D24). This repo holds documents only, no code (`CLAUDE.md`).
- **F9** — The run's four shapes, offered (`.claude/shapes/`): the
  slice record (D12), the evidence test (D13, moved from
  `.claude/rules/`), the kill and the registry entry (D29). Each
  marks its skeleton apart from its illustration. D12 and D13 ask
  that run 4 has them from its first slice. Our Next item holds the
  evidence-test shape back on purpose: the next birth's first tests,
  written without it, are the measurement.
- **F10** — "Apply RETRO.md's decisions": one line pointing at 29
  decisions. Most land in our tree: the run playbook (the step form, a
  retrospective and an apply step before Release, Release's closing
  item, the closing checks of D17), `cbc-framing` (a glossary born at
  framing, D2; the briefing committed when framing opens, D8), the
  container's recording convention, records table and ARCHITECTURE
  template (D1, D10, D16), and the method's texts rewritten plain (D2).
  The concept chapters too, for D6's layer tags and D7's line on where
  a result lives, which the run itself calls preferences, not mistakes
  (D28).
- **F11** — D22: eight checks only run 4 can answer, each to be a gate
  item in the playbook's PLAN at the step that judges it: trials name
  their close (D4); claims read again for specification style (D14);
  the facility and the absence rung watched (D20); Release in the
  reshaped form (D20); shapes read at the gate only judged (D18); the
  untried copies' first use (D28); the two new shapes' first reading
  (D29).
- **F12** — `CLAUDE.local.md`, the reviewer's way of working, is not
  in the run's repo; the reviewer carries it to us by hand (D3). D25,
  that a new kind of work starts from a provisional manual and gets its
  skill at the close, lives only there.
- **F13** — Release reshaped at birth, to be folded into the playbook:
  held since 2026-09-23; still open, run 3's Release not yet run
  (D20).
- **F14** — New ask: `cbc-framing` calls its parts "Step 0" to "Step
  4", and PLAN calls its parts steps, so "step 3" can mean either.
  Run 3's glossary keeps "step" for PLAN. ADR-0049 settled the same
  word for `commit-plan`.
- **F15** — Held asks restated: `infra-establish` silent on the
  store's facility (F4's edit now writes part of it); the absence
  rung. RETRO D20 names run 4 as the run that can trigger both.
- **F16** — Four held asks answered in RETRO.md: the arrangement
  pieces on trial and ticking as items come true (D4, all kept); a rule
  deliverable on trial (D4: a trial names the close that judges it);
  the glossary (D2, D6: born at framing; the run wrote
  `docs/glossary.md`). Each matches a Later or Next item of ours.
- **F17** — Our Next item "fold run 3's three arrangement pieces into
  the run playbook" has fired: its trigger, run 3's retrospective,
  closed on 2026-10-12. D4 judged all three kept, and adds to the step
  form: gate items asked of the goal, one fact each, and a "Now:" line.
- **F18** — Our Later watch on provisional commits has fired: its
  trigger names "a retrospective". D19 judged the commit plan, and F5's
  edit is its answer.
- **F19** — Our Later item on a decisions entry's length: D1 keeps
  three-line entries and adds a rules-in-force list on top; the run's
  own entries in this span run 5 to 25 lines. Evidence, not its
  trigger.
- **F20** — Our Later item on whether `cbc-slice` says a red removes
  the backstop too: F2's `f49a71e` asks the red run to note each
  backstop seen or unproven. Near it, not the same.
- **F21** — Run 4 is a birth in view: RETRO.md's goal is "run 4: the
  same project, rebuilt from the start". Our PLAN's Step 10 gate waits
  on a birth with `exchange-birth` written while it runs; three of our
  Now items trigger at or before the next birth.
- **F22** — Our Release-triggered items, the stance bullets and the
  baselines sort, still wait: run 3's Release opens after our note.
- **F23** — Our Later item "name when a run is read": D24 names it
  for this run — after the apply step, so the decisions arrive tried —
  and the run's TODO *Now* waits on our re-check.

## 4. What the run taught us that we had not thought of

- Looking and changing are two steps: the retrospective changes
  nothing, the apply step changes the run's records and nothing it
  proved, both before Release (D23, D24).
- Copying a result into another record rewords it, and a rewording
  can turn true into false: six places in the definition, one where
  "a reservation not ours" became a check the system never makes
  (D7).
- A shape catches a part that is missing, not one that lost half its
  meaning; only the source shows that (D29's trial).
- A shape read only at the gate keeps form safe, not work: a part the
  work must produce, like a backstop seen at the red run, has to be
  asked for by the skill that runs it (D18).
- A trial with no judging close waits for the end; six did in run 3
  (D4).
- The evidence starts the system in the form it ships (D26).
- Mechanical drift is a script's job at every close; a whole-repo
  sweep means a close missed something (D17).
- For the worked example (`docs/conventions/exchange/` §6.3): it now
  carries the full-word tags. Its six kills carry no worked example
  with numbers, which D2 asks of every kill, and it still calls three
  kills "three costumes", a metaphor D2 rules out.

## 5. Decisions

- **D1** — How RETRO.md's 29 decisions are taken: one by one in
  RETRO's order, or grouped by where each lands in our tree (playbook,
  method skills, container, conventions, concept). It gates W2 to W5.
  *Settled 2026-10-15: by where each lands, each RETRO decision in
  one group, so the final note answers them D1 to D29. Worked in this
  order:*
  - *A, the copy edits (F1 to F7): D5, D6, D7, D9, D10, D11, D12,
    D13, D16, D18, D19, D21, D26, D27, D28, each the half already
    written into a copy.*
  - *B, the run's own files (F8, F9): D1, D2's rule, D12's and D13's
    shapes, D17, D23, D24, D29.*
  - *C, the playbook: D4, D17's closing checks, D20's Release, D22,
    D23's and D24's steps.*
  - *D, the container's templates: D1's recording, D10's records
    table, D16's ARCHITECTURE template.*
  - *E, text we would write: D2's glossary at framing and plain
    method texts, D6's layer tags, D8's briefing.*
  - *F, the reviewer's hand: D3, D25.*
  - *Nothing for us: D14, the shape's own; D20's lists, the run's.*
- **D2** — F1 to F7: take, decline or hold each copy edit. F1 to F4
  are untried, first lived by run 4: taken now, or held until run 4
  lives them. Rests on D1. Gates W2.
- **D3** — F6: accept or decline the reversal of ADR-0036's chapter
  clause. Needs an ADR either way. Gates part of W2.
- **D4** — F8 and F9: which of the run's own files become ours to
  ship; whether shapes are delivered or held back, against our
  evidence-test measurement item; whether a code file can live in a
  documents-only repo. Gates W4.
- **D5** — F21: is run 4 the birth Step 10 waits on, and what must be
  in place before it is born (F11's gate items, `exchange-birth`,
  `temp/` in the container). Gates W3's order.
- **D6** — F14: a word for `cbc-framing`'s parts. Rests on D2 (F1's
  edits touch the same skill).
- **D7** — Whether the note goes before the list closes. Run 3's
  Release waits on it; working-a-reading step 9 allows an early note
  that says which items are still open. Gates W1.
  *Settled 2026-10-15: an early note, written and committed
  (`78242ff`); its copy to the run held, on the reviewer's word.*

## 6. The work

- **W1** — The note, read through `dac4dd1`: the verdicts as they
  stand, in the run's order, the open ones named. *Written
  (`78242ff`), not copied: the reviewer held the copy. The final
  note, at the list's close, carries the verdicts.*
- **W2** — The copy edits taken into our masters, each checked against
  its manual or chapter and read whole. **plan**
- **W3** — The playbook: the step form (F17), the retrospective and
  apply steps, Release's items (F13), D22's gate items for run 4
  (F11). **plan**
- **W4** — The run's own files taken into the bundle, as D4 decides.
  **plan**
- **W5** — The ADR for D3.
- **W6** — TODO brought true: the answered and fired items (F15 to
  F23).
- **W7** — `CLAUDE.local.md` from the reviewer's hand (F12): where it
  lands here, if anywhere.
- **W8** — After the list closes: RETRO's lessons applied to this
  repo's own living records (plain writing, full-name tags, a
  glossary, one home per fact), as Step 10's "lessons folded back"
  item. History keeps its words. **plan**

## 7. What this reading taught

- A run's cited commits can live off main. Main's copies were checked
  against the detail branch before its hashes were trusted. The branch
  and a tag share the name, so git needs `refs/heads/`.
- The hand-off can be a document. One *To the deliverer* line pointed
  at a 1,255-line retrospective; §6.2 made reading it required, and it
  was read whole.
- The run's next step waits on our note: the read-through is now on
  the run's path.

## 8. Notes

- Counts: 42 commits, 1 of them the take; 16 new decisions entries,
  and a rules-in-force list on the log; 7 copies edited in 18 commits,
  4 of them untried; 5 files and 4 shapes of the run's own offered;
  20 lines under *To the deliverer*, 12 new, 1 widened (the shapes,
  from two to four), 4 now answered by RETRO.md, 3 held as before.
- Read only: nothing in the run was written to. Its `temp/` is empty.
- Read whole: RETRO.md and the decisions log's new entries. Not read,
  as each is its item's work: the offered files, the four shapes, the
  glossary, the slice records and the code.

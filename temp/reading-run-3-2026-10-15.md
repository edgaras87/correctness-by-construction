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
  *Taken 2026-10-15 (`b7d3448`), with two changes of ours: the
  skill's examples come from the worked example's order service, not
  run 3's reservations; the worked example tags its possessions, facts
  and trust line, as its header asks. Layers stay L1 to L5 here; their
  tags are group E's.*
  *The layer tags taken 2026-10-17 by W16 (`41d4fc3`), named from
  chapter 01.*
- **F2** — `cbc-slice`, five edits, logged 2026-10-14 and untried:
  tags in full words (`d023336`, D6); the record's skeleton, one block
  per guarantee (`0a8b1a9`, D12); evidence checks the promise, then
  the invariant, before any number, and the red run notes each
  backstop seen or unproven (`f49a71e`, D13, D18); the close writes
  one registry line and ARCHITECTURE rows, never a paragraph
  (`a291147`, D5, D16); SKILL.md says what to do and each gate, the
  workflow only the why and examples, both plain (`2794ac6`, D21,
  D2). SKILL.md 1,744 to 1,887 words; the workflow 2,438 to 1,542.
  *The worked example's share of `d023336` was taken with F1
  (`b7d3448`).*
  *Taken 2026-10-15 (`2674c03`), all five, with two changes of ours:
  the workflow's example of a decision the framing does not carry
  comes from the order service, not run 3's items; the worked
  example's Part 2 tags its guarantees and evidence and documents one
  block per guarantee. Two hold on later items: the close points at
  the shapes rule (F7), and writes rows into ARCHITECTURE's table of
  rules, which our template keeps as a list (group D, RETRO D16).*
  *The table's hold ended 2026-10-17 by W14 (`a69821c`): the
  template keeps a table, and the skill names it the Invariants
  table. The shapes hold is open: F7's plan never touched
  `cbc-slice`, whose workflow still says a shape handed down is
  "an answer a project did not earn", against ADR-0052's four
  shapes shipped with the method. W15.*
  *The shapes hold ended 2026-10-17 by W15 (`4e15b7b`).*
- **F3** — `cbc-bootstrap`, three edits, logged 2026-10-14 and
  untried: the requirements point to the record that decided each
  constraint and end as history at the close, ARCHITECTURE answering
  what a slice may rely on (`7007337`, D10); the harness's form is
  chosen by what ships, not by cost (`a2a776e`, D26); the skeleton
  places tests by kind (`2a05394`, D27).
  *Taken whole 2026-10-15 (`b2d2a4d`). One holds on group D: the
  close says the project's records table sends "what may a slice rely
  on" to ARCHITECTURE, and our container's table does not yet (RETRO
  D10).*
  *Ended 2026-10-17 by W14 (`44bcada`): the table's ARCHITECTURE
  row asks it.*
- **F4** — `infra-establish`, one edit, logged 2026-10-14 and
  untried: the ground proves the engine and what the store promises,
  each constraint seen refused and the facility a slice will need
  (two writers on one row, one made to wait); a lever the evidence
  pulls is proven by the harness that pulls it (`1cadda1`, D9). It
  touches our Later item on `infra-establish`'s facility paragraph.
  *Taken 2026-10-15 (`9046a2f`), but for one clause, held: that the
  ground proves the facility a slice needs. Step 5 never asks for it,
  and the Later item holds it until a run meets the gap unprompted,
  which run 3's own D22 asks run 4 to note.*
- **F5** — `commit-plan`, one edit, logged 2026-10-15, lived in Step
  10 (`3daf0fb`, D19): small commits inside a planned commit, folded
  at its boundary or grouped by kind at the end, kept on
  `<branch>-detail`; a look back at the landed commits before the
  close; a commit inserted later takes a letter (`8b`); a planned
  commit may repeat over a set, with an order and a stop rule; small
  commits follow `commit-messages` when written.
  *Taken 2026-10-15 under ADR-0050, by the commit plan for small
  steps (`54467ae` to `39cdde7`), with one change of ours: small
  commits only where the reviewer has granted them, as run 3 lived
  them; commit-messages makes every other commit wait for the word.
  Manual, shipped skill and our copy alike.*
- **F6** — `delivered-copies.md`, two edits, logged 2026-10-14
  (`c6d21b8`, D28; `128801b`, D2): rule 1 lets a concept chapter be
  edited as any copy, only from a mistake lived in the run; a finished
  copy is fixed whenever the evidence is in the run, its hand-off line
  marked "untried here"; then written plain, each rule keeping its
  number. The run names the reversal of ADR-0036's chapter clause and
  asks us to accept it, or decline with why. No chapter was edited.
  *Taken whole 2026-10-15 under ADR-0051, by the commit plan for
  chapter edits (`d6672ed` to `66e10d7`): the exchange's §5.2 and §5.6,
  ARCHITECTURE's pointer, CHANGELOG's entry; the shipped rule equals
  run 3's. The clause was the exchange's §5.6, from run 3's own first
  rule, not ADR-0036's.*
- **F7** — `shapes-lifecycle.md`, three edits (`d194038`, `e0169dd`,
  `cdfc432`; D18, D29), logged 2026-10-13 and 10-14: shortened to what
  run 3 used; every shape in one folder, `.claude/shapes/`, read at the
  closing gate only; no hidden and exposed places; a fourth way a
  difference ends, a new shape; the `temp/` staging dropped; a shape
  that names work must be asked for by the skill that runs it; a shape
  starts from a look at its examples for what they all lack. The first
  entry cites "commits 4, 5 and 5b", not hashes.
  *Moved to group B 2026-10-15, on the reviewer's word: its look,
  fourth ending and work-naming part stand alone, but dropping the
  `temp/` staging and the exposed place cannot be judged apart from
  F9, the `temp/` Now item and our side of shapes. One decision on
  how a shape reaches a run, with F9.*
  *Taken 2026-10-15 under ADR-0052, by the commit plan for gate
  shapes (`7c0355d` to `18ed1e0`), with two changes of ours: the
  writing rule named as the project's rules; a delivered shape
  changed under `delivered-copies.md`, not by a dated line.*
- **F8** — Files the run wrote, offered whole: `writing.md` and
  `one-home.md`, always loaded (D1, D2); `.claude/checks/records.py`,
  178 lines of Python run at every close (D17); the `retrospective`
  skill and manual (D23); the `apply-retrospective` skill and manual
  (D24). This repo holds documents only, no code (`CLAUDE.md`).
  *All three ended 2026-10-15:*
  - *`records.py` declined as a file; the idea ships. This repo
    holds no code, and half the script is run 3's own: its short
    tags, its file layout, Java and `pom.xml`. The playbook gets a
    closing item instead (W3): every link, path and cited number in
    the records exists; each run writes its own check. Run 4 kept
    and changed the script, so its reading may revisit shipping one.
    Run 3's script lists a stale path, `.claude/apply-retro/`; the
    note says so.*
  - *`writing.md` and `one-home.md` taken under ADR-0053, by the
    commit plan for writing rules (`50cf540` to `5da0484`). Writing
    is a convention of its own; one home is project-recording's §11,
    rule 1, which took five points from run 3's rule. Both ship in
    the container with no `paths:`, examples from the order service,
    and this repo loads its own.*
  - *The retrospective skills taken under ADR-0054, by the commit
    plan for retrospective (`ccf7203` to `8599705`): a convention of
    their own, taken over from project-recording, whose PLAN section
    goes, its questions moved into the skill. Both ship in the
    container, cleaned of run 3. The reviewer's part is the manual's
    seats; no guide ships, so run 3's two guides stay its own files,
    and the note says so. Our seat is on trial at Step 10's close.
    Whether `RETRO.md` wants a shape waits for run 4's reading.*
- **F9** — The run's four shapes, offered (`.claude/shapes/`): the
  slice record (D12), the evidence test (D13, moved from
  `.claude/rules/`), the kill and the registry entry (D29). Each
  marks its skeleton apart from its illustration. D12 and D13 ask
  that run 4 has them from its first slice. Our Next item holds the
  evidence-test shape back on purpose: the next birth's first tests,
  written without it, are the measurement.
  *Taken 2026-10-15 under ADR-0052, reshaped: all four ship with the
  method, read at the gate only, run 3's skeletons kept, tags in full
  words, illustrations from the worked example's order service; the
  registry entry gains Rider. The measurement moves to run 4's first
  slice gate (TODO). Run 3's own `.claude/shapes/` sit at these
  paths; the note says so before any staging.*
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
  *Group D taken 2026-10-17 by W14 (`a69821c` to `d1922c4`): the
  ARCHITECTURE template and records table, the devlog and
  decisions-log stubs. D1's rules-in-force list stays the
  retrospective skill's.*
  *Group E taken 2026-10-17 by W16 (`f2c489c` to `658d0bc`): the
  briefing and the glossary at framing, the layer tags, the worked
  example's kills. D2's rest of the plain rewrite is a TODO item,
  before run 5's birth.*
- **F11** — D22: eight checks only run 4 can answer, each to be a gate
  item in the playbook's PLAN at the step that judges it: trials name
  their close (D4); claims read again for specification style (D14);
  the facility and the absence rung watched (D20); Release in the
  reshaped form (D20); shapes read at the gate only judged (D18); the
  untried copies' first use (D28); the two new shapes' first reading
  (D29).
  *Taken 2026-10-16 for run 5, by W3 (ADR-0055, decision 5): five
  checks as 11 gate items under "For run 5 only" (`c617990`); the
  trial rule in the step form (`0cdc50c`). The facility and the
  absence rung stay ours, never told to the run.*
- **F12** — `CLAUDE.local.md`, the reviewer's way of working, is not
  in the run's repo; the reviewer carries it to us by hand (D3). D25,
  that a new kind of work starts from a provisional manual and gets its
  skill at the close, lives only there.
  *RETRO D25 moved to D8 on 2026-10-16, on the reviewer's word: a
  way of working for both seats, not only the reviewer's.*
  *Ended 2026-10-18 by W7, declined.*
- **F13** — Release reshaped at birth, to be folded into the playbook:
  held since 2026-09-23; still open, run 3's Release not yet run
  (D20).
  *Taken 2026-10-16 by W3 (`5833e62`): most of the reshape was ours
  already; Release gains its lessons item and opens after the apply
  step. Run 5's Release judges it.*
- **F14** — New ask: `cbc-framing` calls its parts "Step 0" to "Step
  4", and PLAN calls its parts steps, so "step 3" can mean either.
  Run 3's glossary keeps "step" for PLAN. ADR-0049 settled the same
  word for `commit-plan`.
  *Sharper since W3: the step form's Now line names a skill's
  stages, and `cbc-framing`'s are called steps, so framing's Now
  would read "Now: Step 3" inside Step 1.*
  *Ended 2026-10-17 by W17 (`d7a8afe`, `f169d4a`): framing's parts
  are Stage 0 to Stage 6, and `infra-establish`'s walk Stage 1 to
  Stage 7.*
- **F15** — Held asks restated: `infra-establish` silent on the
  store's facility (F4's edit now writes part of it); the absence
  rung. RETRO D20 names run 4 as the run that can trigger both.
  *The facility stays held, the clause F4 wrote declined with it
  (`9046a2f`); the absence rung stays held. Both on their triggers;
  the note says so.*
  *Since W6 (`769123e`): both triggers name run 5, since run 4
  rebuilt run 3's problem from run 3's copies.*
- **F16** — Four held asks answered in RETRO.md: the arrangement
  pieces on trial and ticking as items come true (D4, all kept); a rule
  deliverable on trial (D4: a trial names the close that judges it);
  the glossary (D2, D6: born at framing; the run wrote
  `docs/glossary.md`). Each matches a Later or Next item of ours.
  *The glossary taken 2026-10-17 by W16 (`fbd1c5e`): born at
  framing, from a template in `cbc-framing`.*
  *Ended 2026-10-18 by W6 (`769123e`): the rule-on-trial item
  gains D4's answer; the glossary item says the method still has
  none.*
- **F17** — Our Next item "fold run 3's three arrangement pieces into
  the run playbook" has fired: its trigger, run 3's retrospective,
  closed on 2026-10-12. D4 judged all three kept, and adds to the step
  form: gate items asked of the goal, one fact each, and a "Now:" line.
  *Closed 2026-10-16 by W3: the step form (`0cdc50c`, `b75f9b1`);
  the TODO item ended (`1930aae`).*
- **F18** — Our Later watch on provisional commits has fired: its
  trigger names "a retrospective". D19 judged the commit plan, and F5's
  edit is its answer.
  *Closed 2026-10-15 (`a7beb34`): no provisional rule needed; letters
  and small steps are what was missing. Its side note is the skill's
  first anti-pattern already.*
- **F19** — Our Later item on a decisions entry's length: D1 keeps
  three-line entries and adds a rules-in-force list on top; the run's
  own entries in this span run 5 to 25 lines. Evidence, not its
  trigger.
  *Ended 2026-10-17 by W14 (`def6692`, `d1922c4`): three parts, no
  line count, in our log, the stub and agent-arrangement §3.4.*
- **F20** — Our Later item on whether `cbc-slice` says a red removes
  the backstop too: F2's `f49a71e` asks the red run to note each
  backstop seen or unproven. Near it, not the same.
  *Since `2674c03` our skill says so too. The Later item's question,
  whether the red removes the backstop as well, stays open on its
  trigger; W6 rewrites its context.*
  *Ended 2026-10-18 by W6 (`769123e`): the item's context says
  what `2674c03` asks.*
- **F21** — Run 4 is a birth in view: RETRO.md's goal is "run 4: the
  same project, rebuilt from the start". Our PLAN's Step 10 gate waits
  on a birth with `exchange-birth` written while it runs; three of our
  Now items trigger at or before the next birth.
  *Overtaken 2026-10-15 (D5): run 4 was born from run 3's files, not
  ours; Step 10's birth is run 5.*
- **F22** — Our Release-triggered items, the stance bullets and the
  baselines sort, still wait: run 3's Release opens after our note.
  *Ended 2026-10-18 by W6: both kept on run 3's Release, on the
  reviewer's word, though run 4 may answer them first.*
- **F23** — Our Later item "name when a run is read": D24 names it
  for this run — after the apply step, so the decisions arrive tried —
  and the run's TODO *Now* waits on our re-check.
  *Ended 2026-10-18 by W6 (`769123e`): the Later item's context
  names D24's moment; its trigger stands.*

## 4. What the run taught us that we had not thought of

- Looking and changing are two steps: the retrospective changes
  nothing, the apply step changes the run's records and nothing it
  proved, both before Release (D23, D24).
  *Taken 2026-10-15 (ADR-0054); the steps are W3's.*
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
  *Taken 2026-10-16: the step form's trial rule (`0cdc50c`).*
- The evidence starts the system in the form it ships (D26).
- Mechanical drift is a script's job at every close; a whole-repo
  sweep means a close missed something (D17).
  *Taken 2026-10-16 as a closing item of every step (`0cdc50c`);
  the script is each run's own.*
- For the worked example (`docs/conventions/exchange/` §6.3): it now
  carries the full-word tags. Its six kills carry no worked example
  with numbers, which D2 asks of every kill, and it still calls three
  kills "three costumes", a metaphor D2 rules out.
  *Taken 2026-10-17 by W16 (`6526be5`): each kill in the kill
  shape's form, with numbers; "costume" gone. The fenced
  collisions are not yet "nothing dies" kills (TODO, the plain
  method).*

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
  - *B, the run's own files (F8, F9), and F7 with F9 (moved from A): D1, D2's rule, D12's and D13's
    shapes, D17, D23, D24, D29.*
  - *C, the playbook: D4, D17's closing checks, D20's Release, D22,
    D23's and D24's steps.*
  - *D, the container's templates: D1's recording, D10's records
    table, D16's ARCHITECTURE template. Done 2026-10-17, W14.*
  - *E, text we would write: D2's glossary at framing and plain
    method texts, D6's layer tags, D8's briefing. The devlog stub's
    birth entry holds a "Briefing:" line today (W14 met it), and
    `cbc-framing` says "shape" for the registry's layout (W15).
    Done 2026-10-17, W16; the plain rewrite's rest in TODO.*
  - *F, the reviewer's hand: D3, D25.*
  - *Nothing for us: D14, the shape's own; D20's lists, the run's.*
- **D2** — F1 to F7: take, decline or hold each copy edit. F1 to F4
  are untried, first lived by run 4: taken now, or held until run 4
  lives them. Rests on D1. Gates W2.
  *Settled 2026-10-15: an untried edit is taken now when it is sound,
  and read hardest; run 4 is its trial, through F11's gate items.*
  *Corrected 2026-10-15 by D5: run 4 lived run 3's text of each edit,
  as run 3 wrote it; ours, with our changes, is first lived by run 5.*
- **D3** — F6: accept or decline the reversal of ADR-0036's chapter
  clause. Needs an ADR either way. Gates part of W2.
  *Settled 2026-10-15: accepted, on the reviewer's word, over the
  agent's proposed hold (ADR-0051).*
- **D4** — F8 and F9: which of the run's own files become ours to
  ship; whether shapes are delivered or held back, against our
  evidence-test measurement item; whether a code file can live in a
  documents-only repo. Gates W4.
  *Half settled 2026-10-15: shapes delivered, read at the gate only
  (ADR-0052). F8's files are open.*
  *F8 further 2026-10-15: `records.py` declined, the two rules taken
  (ADR-0053); the retrospective skills open.*
  *Settled 2026-10-15: the retrospective skills taken (ADR-0054).*
- **D5** — F21: is run 4 the birth Step 10 waits on, and what must be
  in place before it is born (F11's gate items, `exchange-birth`,
  `temp/` in the container). Gates W3's order.
  *Settled 2026-10-15, by the event: run 4 was born that day by hand,
  from run 3's skills, rules and shapes at `dac4dd1` and our container
  at `35edd3f`, and ran on full auto through Release. It is not the
  birth Step 10 waits on; the next birth from this repo is run 5.
  Every item that tests the bundle names run 5: our shapes, our skill
  edits, the playbook, the container, `exchange-birth`, `temp/` in the
  container.*
- **D6** — F14: a word for `cbc-framing`'s parts. Rests on D2 (F1's
  edits touch the same skill).
  *Since W3, "stage" is the step form's word for a skill's parts.*
  *Settled 2026-10-17, on the reviewer's word for every skill at
  once: a skill's phases are stages, and "step" is PLAN's.
  `cbc-framing`'s step 0 to step 6 become Stage 0 to Stage 6, and
  `infra-establish`'s walk, after its Stage 0, Stage 1 to Stage 7;
  every text that cites them follows, the worked examples alike.
  `cbc-slice`, `cbc-bootstrap` and `infra-serve` say stage already.
  A numbered instruction inside a stage keeps "step": `cbc-bootstrap`'s
  step plan, the walkthroughs' sections, our skills' and rules'
  numbered lists, since no Now line names one. W17.*
- **D7** — Whether the note goes before the list closes. Run 3's
  Release waits on it; working-a-reading step 9 allows an early note
  that says which items are still open. Gates W1.
  *Settled 2026-10-15: an early note, written and committed
  (`78242ff`); its copy to the run held, on the reviewer's word.*
- **D8** — From F12, RETRO D25: a kind of work neither seat has done
  before starts from a provisional manual. The manual changes as
  the step teaches. At the close it becomes the lasting form: a
  skill, a rule, a shape, or a section of a record. Does this become
  a convention for both seats, and where does each seat meet it?
  Lived three times: run 3's Steps 9 and 10, each a skill at its
  close; here, `working-a-reading.md`, a draft through three
  readings, then a rule. Planned once more: `exchange-birth`,
  "written while running the next birth". Worked right after W3. It
  may add a line to the step form, for a step with no skill; W7
  then keeps only the reviewer's file. *Added 2026-10-16.*
  *Settled 2026-10-16: a convention of its own, with a skill shipped
  in the container and one of ours, and a step-form line for a step
  with no skill. The provisional manual sits, in a run, at
  `.claude/<name>/manual.md`, and becomes the lasting form there at
  the close; here, where manuals live, marked on trial. Its cases:
  born in a run, read and fitted to the bundle by us; born here, its
  first run use its trial; born here and used only here, our next
  use its trial; not new, an edit to a copy (`delivered-copies.md`
  rule 2); only one project's, kept there (rule 3); a lasting form
  other than a skill, or none; the way failing, a devlog dead end.
  It also answers `agent-arrangement` §3.1's open question, how a
  project's own skill comes to be. Gates W11.*
  *Built 2026-10-16 by W11 (ADR-0056). On the reviewer's word: the
  skill fires at a fixed moment, a step opening with nothing to say
  how, not on phrases; a run marks its offer as first-time work,
  and we take it by conventions §4 with no skill of ours.*
- **D9** — Our PLAN reconsidered (ADR-0041): does it hold the step
  being worked, readings included, in the run's step form, with its
  opening and closing items and a Now line? The reading file keeps
  its items, and the step holds the gate and links to it.
  Milestones nobody is working on, Step 10's open items and
  Release, stay or move to TODO's Later with their triggers. If
  steps come, our `first-time-work` skill's moment becomes a step's
  opening item, as in a run: its description, the manual's "our own
  first-time work" part and our decisions entry change with it.
  Amends ADR-0041, so an ADR. Raised by the reviewer from W3's step
  form. Gates W13. *Added 2026-10-16.*
  *Settled 2026-10-17, in seven decisions:*
  - *1, a step is the one piece of work being done now: a reading,
    or a TODO item big enough for a branch. One at a time, its gate
    written when it opens. A change set inside it stays in
    `COMMIT-PLAN.md`; a small item needs no step.*
  - *2, the run's step form, taken almost whole as `## The step
    form` at the top of our PLAN: Goal, a Now line by stage, the
    gate written at opening, Notes; the opening items, the branch
    "if it has one"; the step's own items; Known already. Dropped:
    For run 5 only, the shapes item, decision before code, and the
    one-line closed gate, since a step leaves the plan and the
    devlog names it with the ticked gate's commit. Kept from
    ADR-0041 as every step's closing items: lessons folded back,
    and `CLAUDE.md` re-read.*
  - *3, a reading is one step. Its Known already: every finding
    ended, every work item ended and marked, the note in the run,
    the lessons placed, the reading deleted. Its F, D and W stay in
    the reading. Its Notes name the stages: read (`exchange-read`),
    decide and work (`working-a-reading.md`), note
    (`exchange-deliver`), close (that rule's step 9). An extension
    returns Now to read; the branch is cut right after the read. A
    delivery is a reading step's note stage, an own item of the step
    whose change it sends, or, alone, a TODO item. The two reading
    rules stay apart, each on its own foundation. Run 3's reading
    finishes as it began; run 4's is the first step.*
  - *4, Step 10 and Release leave PLAN. The birth joins TODO's
    `exchange-birth`, trigger run 5's birth; our retrospective
    becomes a TODO item, trigger the birth step's close; Release
    goes to Later with its four own items.*
  - *5, our `first-time-work` opens at three moments, each with
    nothing to say how: a step's opening item, a work item inside a
    step, a small TODO item come due.*
  - *6, PLAN holds the open step, and TODO never repeats it. TODO's
    Now: small items due while it runs. Next: the next step's
    candidates, and items not yet due. A TODO item that becomes a
    step leaves TODO. Until run 3's reading closes, PLAN says no
    step is open.*
  - *7, ADR-0057, amending ADR-0041's decisions 1 and 2 and
    ADR-0056's decision 6. The texts made true: PLAN, TODO; the
    deliverer seats of project-recording, retrospective,
    agent-arrangement, shapes and first-time-work; conventions
    §3.3; README's Plan row; `ARCHITECTURE.md`'s codemap;
    `CLAUDE.md`'s records row; our `first-time-work` skill;
    `working-a-reading.md` step 9; `exchange-read` step 4, whose
    "shape" is the rule `exchange-reading.md`.*
  *Built 2026-10-17 by W13 (ADR-0057). On the reviewer's
  questions: project-recording's seat points at PLAN's step form
  and retells no reading; our forms' place as rules is open, our
  forms as shapes held in TODO; a TODO item's story is written in
  the devlog when it is added, on trial.*
  *Decision 3 corrected 2026-10-17: a reading's gates and stages
  live in `working-a-reading.md`, not in PLAN's form. A step takes
  the gates of the skills and rules it uses, its own items written
  first and the gates checked after.*
- **D10** — A rule for this repo: when a skill, rule or shape is
  edited, the manual or chapter its `foundation` names is opened in
  the same commit, the two texts shown side by side, and the
  mismatch ended one of four ways: the edit is wrong, the manual is
  wrong, both change, or they agree. Its foundation is the
  conventions convention, whose "a change … is checked back against
  this page" it makes fire at the edit. `working-a-reading.md` step
  4 keeps its trigger and points at the rule, so the check has one
  home. Raised by the reviewer when W11's look back found the manual
  a commit behind its skills. Gates W12. *Added 2026-10-16.*
  *Settled 2026-10-16: `.claude/rules/foundation-check.md`, loaded
  in every session, since a paths rule loads only when a file is
  opened with the Read tool and edits made by script never open it;
  the moment is staging a commit, which every edit reaches. Both
  directions: a skill, rule, shape or chapter against its
  foundation; a manual against what derives from it. It makes
  `docs/conventions/conventions/` §3.5 and §3.6 fire, and retells
  neither. Not in `CLAUDE.md`: it fails that file's first two tests.
  No hook yet: a miss under the rule is that trigger.*
  *Built 2026-10-17 by W12. On the reviewer's questions: the rule
  looks at the staged paths first, lists every disagreement before
  deciding any, and walks a changed foundation again until nothing
  new is found; a walk greps for a description's name as well as its
  path. Its first commits found conventions §3.5 and §3.6 wrong on
  "the same commit", now "the same commit, or the next".*

## 6. The work

- **W1** — The note, read through `dac4dd1`: the verdicts as they
  stand, in the run's order, the open ones named. *Written
  (`78242ff`), not copied: the reviewer held the copy. The final
  note, at the list's close, carries the verdicts.*
- **W2** — The copy edits taken into our masters, each checked against
  its manual or chapter and read whole. **plan**
  *Done 2026-10-15: F1 to F7 taken, each marked under its finding
  (`b7d3448` to `18ed1e0`).*
- **W3** — The playbook: the step form (F17), the retrospective and
  apply steps, Release's items (F13), D22's gate items for run 4
  (F11). **plan**
  *The two skills exist since `fa7fd41`; the steps here open them.*
  *Done 2026-10-16: playbook v8, ADR-0055, by the commit plan for
  the playbook (`bf2d32e` to `de4a04c`).*
  *Its decisions, one at a time before the plan:*
  - *1, the step form, settled 2026-10-15: run 3's form, taken
    once as a section at the playbook's top, copied at birth inside
    the swapped region before Step 0. Each step keeps its Goal, a
    Now line, and a Gate from the form; the two stock lines go.
    The closing items' list is decision 4's. Examples from the
    order service.*
  - *2, the two steps, settled 2026-10-15: Retrospective (N-2) and
    Apply (N-1) between the slices (5..N-3) and Release (N). The
    retrospective opens when the run stops building slices, every
    slice closed or not. Each holds what decision 1 gives every
    step, its goal from run 3's draft with run 3's name taken out;
    no prewritten gate items, since they would retell the skills
    (RETRO D4). Notes: when it opens; who decides points at the
    manual. `apply-retrospective` §0.2 lists gate items itself;
    decision 4 looks at it.*
  - *3, Release, settled 2026-10-15: two additions, a Known already
    item that Release's own lessons are in RETRO.md, in the
    `retrospective` skill's form, and a Notes line that it opens
    after the apply step. Release alone keeps its Known already
    list. The rest of run 3's reshape was ours already. F13 taken;
    run 5's Release judges it (decision 5).*
  - *4, the closing items, settled 2026-10-15: run 3's list, plus
    three from RETRO D17 and D2: links, paths, cited numbers and
    copy pairs hold; no stale "now" line about what the step
    changed; new text reads to the writing rule. The records item
    states the outcome; one sentence says a run may write its own
    script. `apply-retrospective` §0.2 loses the two items every
    close now carries.*
  - *5, RETRO D22's checks, settled 2026-10-15, rewritten for run
    5. Five become 10 gate items at the steps that judge them, each
    with its reason and source, removed or kept by run 5's reading: an
    edited skill's wording (RETRO D28) at Steps 1, 3, 4, the first
    slice, N-2 and N-1; the claims as specification (RETRO D14) and
    the shapes' first reading (RETRO D29) at the first slice;
    gate-only shapes (RETRO D18) at the second slice; the reshaped
    Release (RETRO D20). Three stay on our side, since telling the
    run spoils them: the facility and the absence rung (F15), the
    evidence-test measurement (TODO). RETRO D4's trial rule goes
    into the step form's text.*
  - *6, the middle-steps line, settled 2026-10-15: a Known already
    item at Step 2, for every run: the plan read end to end against
    the framing, each step standing as named or reworded there. Its
    TODO item ends.*
  - *Decision 2 corrected 2026-10-16: the retrospective opens when
    the slice steps close. "Every slice closed or not" rested on run
    3 having stopped with slices unbuilt. It had not: all four
    closed by Step 8, and Steps 9..N-1 were skipped with none left.*
  - *7, a closed step shrinks to one line, from RETRO D1, missed by
    the six and found while writing ADR-0055; settled 2026-10-16.
    At the close the gate becomes one line: the date, what the step
    delivered, and the commit that holds the ticked gate. Untried:
    run 5 is its first use. In the step form, commit 3 of the
    plan.*
  - *Decision 5 corrected 2026-10-16: 11 gate items, not 10. RETRO
    D29's check splits by shape: the kill shape is first read at
    Step 1, where kills are written, the registry-entry shape at the
    first slice.*
- **W4** — The run's own files taken into the bundle, as D4 decides.
  **plan** *The shapes done 2026-10-15 (`7c0355d` to `18ed1e0`);
  F8's files open.*
  *The writing rules done 2026-10-15 (`50cf540` to `5da0484`);
  `records.py` declined; the retrospective skills open.*
  *Done 2026-10-15: the retrospective skills (`ccf7203` to
  `8599705`).*
- **W5** — The ADR for D3.
  *Done 2026-10-15: ADR-0051, by the commit plan for chapter edits
  (`d6672ed` to `66e10d7`).*
- **W6** — TODO brought true: the answered and fired items (F15 to
  F23).
  *Since W3: the three checks kept on our side (the facility, the
  absence rung, the evidence-test measurement) name run 5.*
  *Since W12: conventions §4 opens "As the last four were added" and
  names four; writing, retrospective and first-time-work came the
  same way since. Fixed in this pass.*
  *Since W13: TODO's Now keeps only what is due, and the triggers
  that named Step 10 are rewritten (`ff13519`).*
  *Since W14: the item on a decisions entry's length ended
  (`d1922c4`); a new item, the records map (`0a75d2d`).*
  *Since W15 and W16: two new items, shapes at birth (`8ec1381`)
  and the plain method (`658d0bc`), both before run 5's birth.*
  *Done 2026-10-18: TODO brought true (`769123e`), conventions §4
  names the last seven (`1bafec0`). The story-at-add trial is due
  and moves to Now. The evidence-test measurement names run 5 too.*
- **W7** — `CLAUDE.local.md` from the reviewer's hand (F12): where it
  lands here, if anywhere. *RETRO D25 is D8's since 2026-10-16.*
  *Since W11, the file's "New kinds of work" can point at the
  `first-time-work` skill instead of telling the way.*
  *Since ADR-0053 the writing rule loads here: whatever lands from
  the reviewer's file points at it, not repeats it (run 3's RETRO
  D2).*
  *Declined 2026-10-18, on the reviewer's word: the file stays the
  reviewer's, carried by hand into a run, and the container ships
  none (agent-arrangement §3.7). Four of its lines are in the
  bundle, each read against the shipped text, three taken from run
  3 after the file was written:
  - commit on the word: `commit-messages`, since 2026-09-19;
  - commit freely, regrouped, `-detail` kept: `commit-plan`
    (`1e50055`);
  - write to be read once: the writing rule (ADR-0053);
  - new kinds of work: `first-time-work` (ADR-0056).
  Two lines live only in some skills: decisions one at a time
  (the two retrospective skills), and a plain manual beside the
  agent's instructions (`first-time-work` deletes its manual at
  the close). Both declined as TODO items: no need seen now, and
  the reviewer raises them again if one appears. What the file
  is for now: settings for one checkout, the rules being the
  bundle's, as run 4's file shows.*
- **W8** — After the list closes: RETRO's lessons applied to this
  repo's own living records (plain writing, full-name tags, a
  glossary, one home per fact), as Step 10's "lessons folded back"
  item. History keeps its words. **plan**
  *Widened 2026-10-15: what each seat holds, and how the two differ,
  is told in five places (`ARCHITECTURE.md` §2.3 and §4,
  agent-arrangement's seats and §3.2, conventions §1); one home for
  it, the counts dropped for the tree. Each manual's list of what
  derives from it stays, as conventions §3.5 asks.*
  *Step 10's "lessons folded back" item became this repo's own
  retrospective, on trial (`5caa466`, ADR-0054). W8 applies run 3's
  lessons ahead of it.*
  *Since W13: TODO's refinement item takes W8 when this reading
  closes, the same checks for all our rules; W8 then ends as held,
  moved there (devlog 2026-10-17).*
  *Since W14: TODO's records map, both seats in project-recording
  §1 (`0a75d2d`), is where one of the five tellings could land.*
- **W9** — At the reading's close, delete the two run 4 drafts in
  `temp/`, the kickoff and the message (`f097695`), with a devlog
  line. *Added 2026-10-15.*
- **W10** — Before main takes this branch, check again how. Never
  rebase or squash it: run 4 started from `35edd3f`, which lives only
  here. Main takes it by fast-forward, unless that check says
  otherwise. *Added 2026-10-15.*
- **W11** — The `first-time-work` convention, as D8 settled: its ADR,
  manual, shipped skill, our own skill, the step form's line.
  **plan**
  *Added 2026-10-16.*
  *Done 2026-10-16: ADR-0056, by the commit plan for first-time
  work (`ee18132` to `99690d2`).*
- **W12** — The foundation-check rule, as D10 settles, and
  `working-a-reading.md` step 4 pointing at it. *Added 2026-10-16.*
  *Done 2026-10-17: by the commit plan for the foundation rule
  (`e744bd2` to `71df140`), and conventions §4 naming first-time
  work as a source of conventions (`74cbaa0`).*
- **W13** — Our PLAN, as D9 settles. **plan** *Added 2026-10-16.*
  *Done 2026-10-17: ADR-0057, by the commit plan for plan steps
  (`04a49ed` to `1abee8d`).*
- **W14** — Group D, the container's templates: RETRO D16's
  ARCHITECTURE, D10's records table, D1's devlog and decisions log.
  Ends F2's and F3's holds, and TODO's item on a decisions entry's
  length. **plan** *Added 2026-10-17.*
  *Its decisions, one at a time before the plan:*
  - *1, ARCHITECTURE's invariants, settled 2026-10-17: a table,
    one row per rule, each linking its slice. Columns as run 3's:
    Rule, Computed by, Refused by, Guarded by, Proved by. The
    header comment says by rule, not by slice: a slice's close
    adds or changes rows, never a paragraph, and how it got there
    is its record's. The example row from the order service.
    cbc-slice's close names "the Invariants table". §8.4 gains a
    line and a dated lesson from run 3.*
  - *2, the records table, settled 2026-10-17: ARCHITECTURE's row
    opens on "the system's structure changed, or asking what a
    slice may rely on", and holds the system as it stands: its
    components, what a slice may rely on, one row per rule. Each
    component in the template gains "A slice may rely on:", which
    cbc-bootstrap's close writes. README's row stays: it speaks
    to the outside.*
  - *3, the devlog, settled 2026-10-17: the stub's comment gains
    one line: an entry is what happened, the dead ends, where to
    resume; test output and a gate's facts are linked in their own
    records, not copied. The one-home rule cannot ask it, since it
    counts the devlog as history. §4.1 agrees already and stays.*
  - *4, the decisions log, settled 2026-10-17: the stub opens on
    "Rules in force now", each line the rule, where its text
    lives, the entry that set it, then "Replaced, and by what", in
    run 3's form. An entry has three parts, what, why, what was
    rejected, not three lines: ours ran a median of 18 lines at
    the eval (2026-10-02), run 3's 5 to 25 after RETRO D1, and the
    list now says what holds. agent-arrangement §3.4 says the
    same; TODO's item on an entry's length ends. Our own log's
    list goes to the refinement item, with W8.*
  - *Decision 4 corrected 2026-10-17, by the foundation walk at
    commit 4 and the reviewer's question: no list in the stub.
    The retrospective skill's step 3 writes it at the
    retrospective, and run 3 and run 4 each wrote theirs there,
    neither from birth. The stub and §3.4 ask three parts only;
    our own log gets no list.*
  *Done 2026-10-17: by the commit plan for the templates
  (`d95ee97` to the close), its commits `a69821c`, `44bcada`,
  `1e3d403`, `def6692`, `d1922c4`.*
- **W15** — `cbc-slice`'s shapes text brought true to ADR-0052:
  the workflow's "Why the shapes are the project's own" says a
  shape handed down is an answer not earned, and four now ship
  with the method. Found 2026-10-17 at W14's pass (F2). A commit;
  the skill stands on concept v1, and is read against the shapes
  convention and ADR-0052.
  *Added 2026-10-17.*
  *Done 2026-10-17 (`4e15b7b`): step 4 reads the shapes in
  `.claude/shapes/`, and the workflow says why none is in the
  skill. Found with it: the seed committed only the skills, fixed
  (`141fa74`); whether a newborn reads its shapes at birth, a TODO
  item before run 5's birth (`8ec1381`); `cbc-framing` says
  "shape" for the registry file's layout, a word for group E.*
- **W16** — Group E, text we would write: RETRO D8's briefing, D2's
  glossary at framing and plain method texts, D6's layer tags.
  **plan** *Added 2026-10-17.*
  *Its decisions, one at a time before the plan:*
  - *1, the briefing, settled 2026-10-17: committed unchanged when
    framing opens, at `docs/system/framing/briefing.md`, and history
    after. Anything private is removed first, and the file's first
    line says what. `cbc-framing`'s opening and the playbook's Step 1
    say so; the devlog stub's "Briefing:" line points at the file.
    Run 4 did it so.*
  - *2, the glossary, settled 2026-10-17: `cbc-framing` starts
    `docs/glossary.md`, each coined word and tag kind in one plain
    sentence, and the records table gains its row. Run 3 and run 4
    each kept one.*
  - *3, the layer tags, settled 2026-10-17 on the reviewer's word,
    over the agent's hold: taken, the number before the name, the
    names our chapter's: LAYER-1-ENVIRONMENT, LAYER-2-SYSTEM,
    LAYER-3-AREAS, LAYER-4-PROBLEMS, LAYER-5-INTERACTION. Not run
    3's: four of its names were what it found in a layer, and two,
    kill and possession, are tags of their own. About 130 uses:
    chapter 01, `cbc-framing`, both worked examples, `cbc-slice`,
    `infra-establish`.*
  - *4, plain method texts, settled 2026-10-17: now, what
    contradicts what we ship. The worked example's "three costumes",
    which the writing rule quotes as its before; a worked example
    with numbers per kill, which the kill shape asks; both copies.
    `cbc-framing`'s "shape" for the registry's layout. The rest,
    about 35,000 words, a TODO item big enough for a step.*
  - *Decision 4 corrected 2026-10-17: about 26,000 words remain,
    not 35,000; the count had taken in `cbc-slice` and the shapes,
    plain already.*
  - *Decision 1, as built: the briefing is the playbook Step 1
    comment's, not an opening item, since `cbc-framing` commits it.*
  *Done 2026-10-17: by the commit plan for group E (`ff29263` to
  the close), its commits `f2c489c`, `fbd1c5e`, `41d4fc3`,
  `6526be5`, `658d0bc`.*
- **W17** — D6: a skill's phases called stages, `cbc-framing`'s and
  `infra-establish`'s, and every text that cites them. **plan**
  *Added 2026-10-17.*
  *Done 2026-10-17: by the commit plan for stages (`d6361f2` to the
  close), its commits `d7a8afe`, `f169d4a`. "Step" stays where it
  meant PLAN's Step 3, twice in `infra-establish`.*
  *The word's home, after W17 (`1648d2d` to `b18eb06`): conventions
  §2 says a skill's phases are stages, and the words define step
  and stage (`950fab3`). Our `first-time-work` points at §2
  (`315fad7`).*

## 7. What this reading taught

- A run's cited commits can live off main. Main's copies were checked
  against the detail branch before its hashes were trusted. The branch
  and a tag share the name, so git needs `refs/heads/`.
- The hand-off can be a document. One *To the deliverer* line pointed
  at a 1,255-line retrospective; §6.2 made reading it required, and it
  was read whole.
- The run's next step waits on our note: the read-through is now on
  the run's path.
- A RETRO decision's "Lands in" names a place, not how the run
  lived it. D1 sent its rules-in-force list to the kit's recording
  convention, yet run 3 and run 4 each wrote theirs at the
  retrospective. Settled
  as written, it was caught only by the foundation walk at the
  commit (W14, decision 4). Check what the runs did before taking
  where a decision lands.

## 8. Notes

- Counts: 42 commits, 1 of them the take; 16 new decisions entries,
  and a rules-in-force list on the log; 7 copies edited in 18 commits,
  4 of them untried; 5 files and 4 shapes of the run's own offered;
  20 lines under *To the deliverer*, 12 new, 1 widened (the shapes,
  from two to four), 4 now answered by RETRO.md, 3 held as before.
- Read only: nothing in the run was written to. Its `temp/` is empty.
- Run 4 was born and finished on 2026-10-15, from run 3 at `dac4dd1`,
  the commit this reading reads. This reading is finished as if run 4
  had not run; run 4 is read after, for what it changed on top of
  `dac4dd1`, what it answered, and what is new.
- Read whole: RETRO.md and the decisions log's new entries. Not read,
  as each is its item's work: the offered files, the four shapes, the
  glossary, the slice records and the code.

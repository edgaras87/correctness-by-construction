<!-- The CBC Run Reading of CBC Run 6, checkout, opened 2026-11-26 by
     the exchange-read Agent Skill and worked in place. It is judged
     with CBC Run 4's and CBC Run 5's in the Plan Step "Read and judge
     CBC Runs 4, 5 and 6", by today's exchange (ADR-0089). No Delivery
     Note carries it: it is kept here for the rewrite, where its taken
     items land. Its form is .claude/rules/exchange-reading.md; how it
     is worked, .claude/rules/working-a-reading.md. Our paths and
     decisions are cited freely: nothing here goes to the CBC Run. -->

CBC Run 6, `~/IdeaProjects/cbc-pure-run-6`: read through `00fc075`.

## 1. Where we read to

- **Read through:** `00fc075`, CBC Run 6's main, 2026-10-29 08:14,
  tagged `run6/step-15`. The tree is clean.
- **Previous read-through:** none. CBC Run 6's birth entry in its
  `.claude/decisions.md` reads "pin 657d372; read-through none", and
  this is its first CBC Run Reading.
- **The span:** its whole history, 233 commits on main, 16 step tags
  `run6/step-0` to `run6/step-15`, the tag `v0.1.0`, 34 branches.
- **The base for the diff of its copies:** `birth-seed`, the Receipt
  Branch its seed cut, at `2127d2e`. Every copy on it equals our pin
  `657d372` byte for byte, with the 5 concept chapters: 50 of the 59
  files under `delivery/`. Of the other 9, 6 are records the seed
  fills: the Entry File, the Decisions Log, PLAN, README, the devlog
  and ADR-0001. The seed does not land the other 3: `delivery/README.md`,
  the playbook and the seed itself.

## 2. What the CBC Run did

Times are commit times, all 2026-10-29. Each step ran on its own
branch, fast-forwarded to main and tagged at its close. The run was
on full auto: every sign-off delegated to it, a stop hook refusing a
stop until Release, the reviewer's hand-off `temp/run-6-handoff/`.

- **Step 0, Bootstrap, 22 commits, 01:06 to 01:29.** Landed the delivery
  byte-equal to `birth-seed` in three commits by kind, not the seed's
  four (its L-5). Then its own: the commits check, the decision log,
  the delegation of every sign-off, the stop hook, the records and
  weights checks, `docs/run.md`. Drafted the birth Approach on Trial.
- **Step 1, Framing, 24 commits.** One Falsifiable Promise holding
  both halves of the briefing: every checkout ends in exactly one
  decision that never changes, and money and stock follow it. Three
  areas, 22 kills, 7 slices, 4 folds, 20 facts. The shapes found two
  misses at the gate (L-32, L-33).
- **Step 2, Identity, 9 commits.** `checkout` everywhere; ADR-0003.
- **Step 3, Ground, 14 commits.** PostgreSQL 17 under compose, two
  roles, Flyway behind a profile; ADR-0004 to ADR-0006. The stand-in's
  home opened as its one Real question, L-41.
- **Step 4, Bootstrap, 20 commits.** Boot 4.1.2, Java 21. L-41 tried
  on two `try/` branches; the stand-in lives in the build (ADR-0008).
  The fresh-clone check added. The records check found unable to
  fail since Step 0, and rewritten.
- **Steps 5 to 11, SLICE-1 to SLICE-7, 97 commits, 02:27 to 04:51.**
  Seven slices, each red on its `red/` branches before green: 14 red
  branches, 44 tests in 30 classes. SLICE-7 is a seeded storm of all
  six troubles with a kill between its waves, and no new wall.
- **Step 12, Retrospective, 13 commits.** `RETRO.md`, ten decisions,
  D1 to D10.
- **Step 13, Apply the retrospective, 12 commits.** Seven applied, two
  partly, one for the next CBC Run only. `docs/run.md` revised in
  place, with a dated list, §15. PLAN's step form takes D10.
  `close.sh` written. The cbc-slice Agent Skill edited (D6).
- **Step 14, Release, 14 commits, to 05:22.** `v0.1.0`; ADR-0016;
  three known issues in TODO; Release's lessons D11 and D12 added to
  `RETRO.md`. Drafted the release Approach on Trial.
- **Step 15, the reviewer's message "continue", 8 commits, to 08:14.**
  Taken as a step by its run file's §11. It found `close.sh` had
  removed PLAN's `STEPS-END` marker at Step 14's close, fixed the
  tool, and added ADR-0016 to PLAN's Decision index.
- **The CBC Run Asks,** five lines under `## To the deliverer` in its
  `TODO.md`, written at Steps 0, 12, 13 and 14.

## 3. Findings

### The edit

- **FINDING-1. The cbc-slice Agent Skill, Stage 3, item 2, gains two
  questions of every scene:** "A scene owns its rows" and "The witness
  reads through doors no lever holds" (`271135f`, RETRO.md D6). Its
  Decisions Log records it, dated 2026-10-29, written at Step 13
  after the last slice: untried.

### The CBC Run Asks

- **FINDING-2. CBC Run Ask 1: the birth Approach on Trial, offered for
  evaluation,** `.claude/approaches-on-trial/birth.md`, 83 lines, its
  history `6038a62`..`4b990e2`, one use (Step 0).
- **FINDING-3. CBC Run Ask 2: apply RETRO.md's D1 to D10 to what the
  next CBC Run starts from,** by each decision's *Lands in*,
  *Delivering the retro* and *What the next run checks*.
- **FINDING-4. CBC Run Ask 3: the playbook's step form, D10.** Its two
  closing items the commit guard enforces, the commit form and the
  straddling, become one line naming the guard.
- **FINDING-5. CBC Run Ask 4: evaluate the cbc-slice Agent Skill's
  edit,** FINDING-1.
- **FINDING-6. CBC Run Ask 5: the release Approach on Trial, offered
  for evaluation,** `.claude/approaches-on-trial/release.md`, 96 lines,
  its history `64c2336`..`664bbc5`, one use (Step 14).

### The read

- **FINDING-7. CBC Run Ask 2 names D1 to D10, and RETRO.md holds
  twelve.** D11 and D12, Release's lessons, were added at Step 14.
  *What the next run checks* lists both. *Delivering the retro* still
  says "Ten decisions".
- **FINDING-8. Our seed's first commit straddles agent and project
  paths.** `b6fe74e`, "seed — records and conventions", holds
  `.claude/` files beside PLAN, README, TODO and the devlog. CBC Run 6
  landed the delivery in its own three commits for that reason (L-5).
- **FINDING-9. Our run file counted three fixes on trial and listed
  two** (`temp/run-6-handoff/run.md` §7). It also asked for each
  result "in its step's Notes", which the step form deletes at the
  close (RETRO.md D2). The results went into close lines instead.
- **FINDING-10. Both fixes on trial held.** The registry template's
  Record and Answered-at-close slots said "none" until filled (Step 1).
  The slice-record shape's backstop line named the backstop, and the
  red was taken twice (Step 5, L-58, L-60).
- **FINDING-11. A check the CBC Run wrote was trusted before it was
  seen failing.** `records.sh` could not fail for Steps 0 to 3: under
  `pipefail`, `grep -q` left the flag unset (L-54). Found at Step 4,
  when 16 stale paths surfaced (RETRO.md D1).
- **FINDING-12. The step's close was a scratch script rewritten for
  each step.** 6 of 13 dead ends were the shell's: anchors missed,
  chains run past a failure, a body with quotes broken inline. RETRO.md
  D8 makes the close a tool written at the birth; D11 passes bodies by
  file; D12 reads a tool's first output before its second use.
- **FINDING-13. `close.sh`'s second use removed PLAN's `STEPS-END`
  marker,** since the marker stood after a step's Notes block. Found
  only because the reviewer's "continue" opened Step 15. PLAN's step
  markers are the seed's (`delivery/installs/pure-seed.md`).
- **FINDING-14. The run file's "a wall with a choice is tried" was
  broken three times, rightly** (L-56, L-63, L-69). §4's second
  criterion, the protection in the store, ranked the options before a
  try could (RETRO.md D4).
- **FINDING-15. The 400-line slice-record budget holds four
  guarantees.** The record shape's block costs about 45 lines a
  guarantee over about 210 fixed. SLICE-1 was written to 455 and cut
  to 396 (RETRO.md D3).
- **FINDING-16. A red file's hand-written claim contradicted its own
  output** (`red/slice-2-allowance`, L-65). RETRO.md D5 keeps the claim
  in the slice record.
- **FINDING-17. Scenes shared rows, and the witness read through a
  levered path.** Three dead ends, Steps 6 to 8; the source of
  FINDING-1.
- **FINDING-18. The storm ran from one seed, and that seed produced no
  expiry** (L-93, L-94). Nothing asked for a second seed (RETRO.md D7,
  for the next CBC Run's PLAN).
- **FINDING-19. The look-back at each commit plan's close found
  nothing twelve times** (RETRO.md D9). Our run file put it on trial
  (§9); the CBC Run struck it.
- **FINDING-20. Seven of the step form's nine standard closing items
  found nothing in twelve closes** (RETRO.md Part 10). Two of them,
  the commit form and the straddling, are FINDING-4; the CBC Run kept
  the other five as judgments no script makes.
- **FINDING-21. The Entry File stub's pre-framing paragraph names a
  moment that passes at framing.** The CBC Run removed it at the
  retrospective, by the Entry File's own guard (its Decisions Log,
  the pre-framing entry).
- **FINDING-22. The Decisions Log's stub carries a "Rules in force
  now" list on top of an append-only log,** written at the
  retrospective "as the retrospective skill's close asks". CBC Run 4
  asked the same of its own log (PLAN's Notes).
- **FINDING-23. The glossary waited for framing.** Tags coined at
  Step 0 (L-n, Small, Real, Verdict, Look-back, Model) had no glossary
  until Step 1, because the cbc-framing Agent Skill names where it
  starts (L-15).
- **FINDING-24. ADR-0013's watch item: the Entry File gained neither
  the ground-must-be-up rule at Step 3 nor the stack fact at Step 4.**
  Its only new local rule is the name (ADR-0003). This is CBC Run 6's
  own question in the Plan Step's Notes.
- **FINDING-25. Three words of record per word of code.** 58,266
  words of record against 17,594 of code and tests. The 7 slice
  records alone hold 16,329 words (RETRO.md, *The run, in numbers*).

## 4. What the CBC Run taught us that we had not thought of

- **TAUGHT-1. Full auto held 205 minutes, Steps 0 to 11, with no
  stop.** Every sign-off was written where the Agent Skill puts it,
  and one Verdict line per step indexed them. The stop hook was never
  tested by a stop.
- **TAUGHT-2. A shape read only at the gate costs one rework per kind
  of output,** at its first close, and finds a real miss each time.
  Six later closes found no difference.
- **TAUGHT-3. A step that learns by one road stops when that road is
  silent** (L-77). Fifty duplicate notices at once pushed every step
  past its first attempt, and nothing captured until a step asked its
  operation itself.
- **TAUGHT-4. The worked example.** It rejects "orders are never lost
  AND payment always completes" as overloaded. CBC Run 6 chose one
  claim that holds both of its briefing's halves, one decision and the
  money following it, and the claim held through seven slices with no
  re-framing. What this teaches the worked example is for the judging.

## 5. Decisions

None yet. Decisions are written at the judging, stage 4, with CBC
Runs 4 and 5.

## 6. The work

None yet; written at the judging.

## 7. What this CBC Run Reading taught

- A first CBC Run Reading's span is the whole history, and the
  Receipt Branch's equality with our pin is checked file by file
  before the diff is trusted.

## 8. Notes

- **Counts, by script:** 233 commits on main; per step, 22, 24, 9, 14,
  20, 16, 16, 14, 14, 12, 14, 11, 13, 12, 14 and 8, for Steps 0 to 15.
  One edited copy, five CBC Run Asks, 25 findings, 4 taught.
- **Not committed:** nothing; the tree is clean at `00fc075`.
- **Hashes cited:** the ten checked, from the CBC Run Asks and
  RETRO.md, are all on main.
- **The run file:** `docs/run.md` is our hand-off's `run.md`, revised
  at Step 13 under its §15, *Revisions*. RETRO.md asks the reviewer
  to take the revised file as the next CBC Run's run file. Our copy
  is `temp/run-6-handoff/run.md`.
- **Not read whole:** the slice records, the framing exports, the
  ADRs, the code and the tests. Read whole: RETRO.md, the Decisions
  Log, TODO.md, PLAN's close lines, the run file's diff, the
  devlog's last three entries and its dead-end lines, and the decision
  log by search.
- **Nothing in CBC Run 6 was written to.**

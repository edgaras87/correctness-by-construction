<!-- The CBC Run Reading of CBC Run 4, safe-reservation-2, opened
     2026-11-26 by the exchange-read Agent Skill and worked in place.
     It is judged with CBC Run 5's and CBC Run 6's in the Plan Step
     "Read and judge CBC Runs 4, 5 and 6", by today's exchange
     (ADR-0089). No Delivery Note carries it: it is kept here for the
     rewrite, where its taken items land. Its form is
     .claude/rules/exchange-reading.md; how it is worked,
     .claude/rules/working-a-reading.md. Our paths and decisions are
     cited freely: nothing here goes to the CBC Run. -->

CBC Run 4, `~/IdeaProjects/cbc-pure-run-4`: read through `7637a79`.

## 1. Where we read to

- **Read through:** `7637a79`, CBC Run 4's main, 2026-10-15 13:34,
  tagged `run4/step-11`. The tree is clean.
- **Previous read-through:** none. CBC Run 4's birth entry in its
  `.claude/decisions.md` reads "Read-through none", and this is its
  first CBC Run Reading.
- **The span:** its whole history, 158 commits on main, 13 step tags
  `run4/step-0` to `run4/step-11` with `run4/step-2b`, 42 branches,
  361 commits across them. No remote.
- **Two pins, from the birth entry:**
  - the container (record stubs, Entry Files, hygiene files): our
    `35edd3f`, on our main;
  - the copies (`docs/concept/`, `.claude/skills/`, `.claude/rules/`,
    `.claude/shapes/`, `.claude/checks/`): CBC Run 3's `dac4dd1`.
- **The base for the diff of its copies:** `birth-seed`, the Receipt
  Branch cut by hand at birth, at `ec7925b`. Its copies equal CBC Run
  3's tree at `dac4dd1`, path by path and blob by blob. Main does not
  descend from it: main landed the same files in its own commits
  (`3d15ac5`, `0954b26`, `1436e1a`), and their copies equal
  `birth-seed`'s.

## 2. What the CBC Run did

Times are commit times, all 2026-10-15, from 04:11 to 13:34. Each
step ran on its own branch, its small commits kept on a `-detail`
branch, regrouped by kind, fast-forwarded to main and tagged. The
CBC Run was on full auto: every sign-off delegated to it, a stop
hook refusing a stop until Release, and the run file `docs/run.md`
deciding what a skill would ask a human.

- **Step 0, Bootstrap, 10 commits.** The seed landed in its own
  commits by kind (L-02). The check script crashed at the first
  close and was rewritten to run before records exist (L-03).
- **Step 1, Framing, 14 commits.** The promise was given (SETTLED-1).
  24 facts, 23 kills, 3 folds, 4 slices; one owner; LAYER-5 empty.
  ADR-0002. Two Output Shapes edited at the gate (L-16, L-17).
- **Step 2, Identity, 6 commits.** The name was given,
  safe-reservation-2 (SETTLED-5). The plan read end to end against
  the framing (`2c78c64`).
- **Step 2b, Plain words, 13 commits.** Inserted mid-Step 3 by the
  reviewer's message (L-28): every tag in full words, the records in
  plain voice, a glossary of 50 entries. 19 delivered copies
  rewritten (L-30); the kill shape's form rewritten (L-31).
- **Step 3, Ground, 8 commits.** PostgreSQL 17 under compose; one
  Real question tried on two `try/` branches (L-24). ADR-0003 to
  ADR-0005.
- **Step 4, Skeleton, 12 commits.** Boot 4.1.1, Java 21. The
  walkthrough's socket trap corrected (L-49). ADR-0006.
- **Steps 5 to 8, SLICE-1 to SLICE-4, 59 commits.** Each slice's
  walls in the store; three Real questions tried on branches, two
  of which changed the answer (L-56). ADR-0007 to ADR-0012. Two
  Output Shapes edited three times (L-60, L-61, L-69).
- **Step 9, Retrospective, 7 commits.** `RETRO.md`, D1 to D12.
- **Step 10, Apply the retrospective, 17 commits.** Nine applied,
  one partly, two for the next CBC Run only. The cbc-slice Agent
  Skill, the bootstrap references and commit-messages edited
  (L-96 to L-99).
- **Step 11, Release, 12 commits.** `0.1.0`; a fresh-clone check,
  one Real question on two branches (L-100, ADR-0013). It found the
  README's Run block never migrated the store (L-101). D13 and D14
  added to `RETRO.md`.
- **The CBC Run Asks,** 12 lines under `## To the deliverer` in its
  `TODO.md`, written from Step 0 to Step 11.

## 3. Findings

### The edits its Decisions Log records

- **FINDING-1. The check script runs before the records it checks
  exist,** and checks cited numbers outside `.claude/` only
  (`.claude/checks/records.py`, L-03, Step 0).
- **FINDING-2. The kill shape gives a reason when a collision breaks
  nothing; the registry-entry shape gains a Rider field**
  (`.claude/shapes/kill.md`, `registry-entry.md`, L-16, L-17,
  Step 1's close).
- **FINDING-3. The bootstrap walkthrough: Testcontainers 2.x finds
  the podman user socket itself, and the properties file is the
  fallback** (trap 1, recall item 4, `templates/testcontainers.properties`,
  L-49, Step 4). The template's line was never run.
- **FINDING-4. The evidence-test shape gives a fold's test its own
  first line; the slice-record shape writes one proof as one line**
  (L-60, L-61, SLICE-1's close).
- **FINDING-5. The evidence-test shape's item 6 asks for the
  adversity's assertion only where it can be read from outside**
  (L-69, SLICE-2's close).
- **FINDING-6. The retrospective applied to four copies:** the
  cbc-slice Agent Skill's Stage 2 and Stage 3 (D6, D7, D8, D10); the
  walkthrough's fraction trap (D4); the harness reference's warm-up
  (D5); commit-messages naming `.claude/checks/commit.sh` (D12).
  Step 10, L-96 to L-98. Untried: written after the last slice.
- **FINDING-7. The bootstrap README template's Run block migrates
  the store** (`templates/readme-run-test.md`, D13, L-101, Step 11).
  Tried by the fresh-clone check.

### Changed, and not in its Decisions Log

- **FINDING-8. Step 2b's full-word tags in 19 copies** (L-30). Among
  them, the concept's chapter 01 renames its five layers to the
  CBC Run's tags: LAYER-1-ENVIRONMENT, LAYER-2-POSSESSION,
  LAYER-3-OWNER, LAYER-4-KILL, LAYER-5-BETWEEN-OWNERS. `writing.md`
  and `one-home.md` each gain a dated line naming the project's
  decision log. The two worked examples changed alike and are still
  identical. Recorded in `docs/decision-log.md` and TODO, not in the
  Decisions Log.
- **FINDING-9. The kill shape's form becomes a paragraph with
  labelled parts, and the check script's patterns read full-word
  tags** (L-31, L-32, L-51). Named in the Decisions Log's "Rules in
  force now" list, with no entry of its own.
- **FINDING-10. The apply-retrospective Agent Skill: "a script's exit
  is not its edit"** (L-99, Step 10). Step 10's Decisions Log entry
  names L-96 to L-98 only. Untried.

### The CBC Run Asks

- **FINDING-11. CBC Run Ask 1: apply `RETRO.md`'s D1 to D12 to what
  the next CBC Run starts from,** each by its *Lands in*.
- **FINDING-12. CBC Run Ask 2: the check script's changes are D1 and
  D2** (L-03, L-30, L-32, L-51).
- **FINDING-13. CBC Run Ask 3: the kill and registry-entry shapes'
  changes are D2 and D3** (L-16, L-17, L-30, L-31).
- **FINDING-14. CBC Run Ask 4: the evidence-test and slice-record
  shapes' changes are D2 and D10** (L-30, L-60, L-61, L-69).
- **FINDING-15. CBC Run Ask 5: `writing.md`'s and `one-home.md`'s
  changes are D2** (L-30).
- **FINDING-16. CBC Run Ask 6: the cbc-framing, cbc-slice and
  infra-establish Agent Skills', the apply-retrospective manual's and
  chapter 01's changes are D2** (L-30).
- **FINDING-17. CBC Run Ask 7: the bootstrap walkthrough's, harness
  reference's and properties template's changes are D2, D4 and D5**
  (L-30, L-49, L-97). The template line, D4's fraction trap and D5's
  warm-up are untried.
- **FINDING-18. CBC Run Ask 8: the cbc-slice Agent Skill's changes
  are D2, D6, D7, D8 and D10** (L-30, L-96). D6 to D10 untried.
- **FINDING-19. CBC Run Ask 9: commit-messages' change is D12**
  (L-98): it names `.claude/checks/commit.sh`, which ran on every
  commit of the CBC Run.
- **FINDING-20. CBC Run Ask 10: the apply-retrospective Agent Skill's
  change is L-99.** Untried.
- **FINDING-21. CBC Run Ask 11: the README template's change is D13**
  (L-101). Tried by the fresh-clone check.
- **FINDING-22. CBC Run Ask 12: take `.claude/checks/fresh-clone.sh`
  and `.claude/checks/commit.sh` with the arrangement** (D12, D14).
  Both are the project's own.

### The read

- **FINDING-23. CBC Run Ask 1 names D1 to D12, and `RETRO.md` holds
  fourteen.** D13 and D14 were added at Release, and Asks 11 and 12
  name them. CBC Run 6's Reading has the same miss (its FINDING-7).
- **FINDING-24. `RETRO.md`'s *Delivering the retro* says D1, D2 and
  D4's first half are applied.** Its own table, *Applied to run 4*,
  marks nine applied, D3 partly, and D9 and D11 next run only. D13
  and D14 are not in the table. *The run in numbers* is measured at
  Step 8.
- **FINDING-25. A delivered copy names a project's own file:**
  commit-messages points at `.claude/checks/commit.sh`, which no
  delivery holds. Its limit is a subject of 50. All 158 subjects on
  main are 50 or under, and no commit straddles agent and project
  paths, both by script. Ours passes a subject up to 70.
- **FINDING-26. The reviewer's message broke full auto once.** It
  arrived in CBC Run 4's `temp/` during Step 3. Step 2b was inserted,
  and L-28 logged as "Verdict, the reviewer's". Step 3's branch was
  rebased onto main and resumed (its devlog, Step 3). The CBC Run
  deleted the message, as the message asked; our copy is at
  `f097695`.
- **FINDING-27. The decision log was never reviewed.** 102 entries,
  L-01 to L-102: 54 Verdict, 26 Small, 16 Method, 6 Real; 7,870
  words. One is marked agreed (L-28); the rest say "Review: open".
  The run file leaves reading it to the reviewer after auto ends.
- **FINDING-28. Nobody compared CBC Run 4's facts and kills with CBC
  Run 3's.** `temp/RUN-4.md` put the comparison in the CBC Run's
  self-check. The run file CBC Run 4 got does not have it, and
  `docs/settled.md`'s header says "The reviewer compares the two runs
  afterwards". CBC Run 4 framed 24 facts and 23 kills; CBC Run 3, 24
  and 20 (`temp/RUN-4.md`).
- **FINDING-29. `temp/RUN-4.md` is not what CBC Run 4 started from.**
  The reviewer cut it at birth: `docs/settled.md` holds six items,
  the problem alone, against the draft's S1 to S28b; the stack, the
  door and the walls were derived again. The name is
  safe-reservation-2, not never-oversold.
- **FINDING-30. Each step's close item was ticked before it came
  true.** "Main is fast-forwarded from `<branch>` and the close is
  tagged", with the evidence "`git tag` lists `run4/step-<n>`", is
  ticked in the commit before the fast-forward and the tag, at all
  13 closes, by script. Step 11: ticked at `7db6949`, tagged at
  `7637a79`. This is CBC Run 4's own
  question, how it closed its Plan Step branches.
- **FINDING-31. PLAN's Decision index lists ADR-0001 alone,** of 13
  ADRs. The *Steps 5 to 8* block stands, with its Known already,
  after all four slices closed.
- **FINDING-32. The Entry File was last changed at Step 2.** Three
  commits in all. Its pre-framing paragraph stands after framing;
  CBC Run 6 removed the same paragraph (its FINDING-21). Its one
  local rule is "Nothing before the briefing names the problem."
  Neither the ground-must-be-up rule at Step 3 nor a stack fact at
  Step 4 was added: ADR-0013's watch item, the old trigger "the next
  birth's Step 3 close".
- **FINDING-33. The Decisions Log carries a "Rules in force now"
  list on top,** eight rules, each with what it replaced, while its
  header says "Append-only, newest last". CBC Run 4's copy of the
  retrospective Agent Skill asks for it at the close (Stage 4,
  item 2), and our Master Copy still does (Stage 4, item 3). CBC Run
  6 did the same (its FINDING-22). This is the refinement's
  FINDING-77 (`TODO-CONVERSATION-MEMORY.md` §5).
- **FINDING-34. README's status line changed at seven closes,** from
  "framed" at Step 1 to "released as 0.1.0" at Step 11, as the
  cbc-framing Agent Skill's "an honest status line" asks. PLAN also
  carried each step's status. Release's gate checks the line. This
  is the refinement's FINDING-81 (`TODO-CONVERSATION-MEMORY.md` §5).
- **FINDING-35. The Plan Steps were confirmed once framed:** Step 2
  read the plan end to end against the framing (`2c78c64`), and
  set four slices as Steps 5 to 8 in the registry's order.
- **FINDING-36. `RETRO.md` against the retrospective Agent Skill's
  form.** CBC Run 4's has the form's seven sections in order. It adds
  *The run in numbers*, *What only the next run can check* and
  *Applied to run 4*. 362 lines. CBC Run 3's, 1,255 lines, keeps
  *Delivering the retro* under *Do differently*, and holds two Plan
  Step drafts and *Applied to run 3*.
- **FINDING-37. No `temp/` in CBC Run 4's tree, and none ignored.**
  Its copies still send work there: `delivered-copies.md`, the
  visual-comparison Agent Skill, the slice-record shape and the
  apply-retrospective Agent Skill. The reviewer's message was put
  there, and deleted. This is the old trigger "before the next
  birth", shipping `temp/`.
- **FINDING-38. `.gitignore`'s stack overlay was derived by hand a
  fourth time,** at Step 4 (`378b467`), with `*.iml` listed twice.
  The cbc-bootstrap Agent Skill says "grow, never overwrite" and
  points at no hygiene part. This is the old trigger "a fourth run
  deriving `.gitignore` by hand".
- **FINDING-39. How CBC Run 4 lived CBC Run 3's Output Shapes.** Six
  edits, each at a gate, from a lived difference (L-16, L-17, L-31,
  L-60, L-61, L-69). SLICE-1's gate found four of five tests missing
  their record's path (D10). Step 6's answer on reading Output Shapes
  at the gate only: "it cost a late cut at SLICE-1 and taught two
  forms; at SLICE-2 nothing was missed, only because the lessons
  stayed in memory." CBC Run 4 held the Output Shapes from birth.
- **FINDING-40. Two of four slice records stand at 249 lines,**
  against a 250-line limit; the others at 227 and 201. `RETRO.md`
  judged the limit kept (*Parked*). CBC Run 6's limit was 400 (its
  FINDING-15).
- **FINDING-41. 85 words of record per line of main code,** measured
  at Step 8: 39,162 words against 457 lines of main Java and 2,261
  of tests (`RETRO.md`, *The run in numbers*). CBC Run 6 counted
  three words per word of code (its FINDING-25).

## 4. What the CBC Run taught us that we had not thought of

- **TAUGHT-1. Full auto held from birth to Release in about nine
  and a half hours,** 158 commits, one stop, the reviewer's own.
  Every sign-off left a Verdict line, 54 in all.
- **TAUGHT-2. Trying a Real question on branches changed the answer
  twice.** 14 `try/` branches for 6 Real questions. The counter kept
  expired holds, and the conditional statement raced (L-56).
- **TAUGHT-3. A wall from a closed slice can hold a later slice's
  kill,** so the later red tree stays green. Red came only with
  SLICE-2's rule removed too (L-73, three in three; D7).
- **TAUGHT-4. The worked example.** CBC Run 4 framed a given promise:
  one owner, LAYER-5 empty, four slices, CBC Run 3's problem rebuilt.
  What this teaches the worked example is for the judging.

## 5. Decisions

Judged with CBC Runs 5 and 6. The decisions live in CBC Run 6's
Reading, `temp/reading-run-6-2026-11-26.md` §5, its DECISION-1. This
Reading's findings among them:

- CBC Run 6's DECISION-2, held: FINDING-1, 12 and 22.
- CBC Run 6's DECISION-4, declined: FINDING-27.
- CBC Run 6's DECISION-5, declined: FINDING-28.
- CBC Run 6's DECISION-6, declined: FINDING-8, 15 and 16, and
  FINDING-9's tags.
- CBC Run 6's DECISION-7, the watch ended: FINDING-32.

## 6. The work

The work lives in CBC Run 6's Reading, §6, with each item's ending.
This Reading's findings among it:

- CBC Run 6's WORK-1, the cbc-slice Agent Skill: FINDING-6 and 18,
  TAUGHT-3.
- CBC Run 6's WORK-2, the cbc-bootstrap references and templates:
  FINDING-3, 6, 7, 17 and 21.
- CBC Run 6's WORK-4, the Output Shapes: FINDING-2, 4, 5, 9, 13 and
  14.
- CBC Run 6's WORK-5, the commit-messages Agent Skill: FINDING-6, 19
  and 25.
- CBC Run 6's WORK-6, the retrospective Agent Skill: FINDING-33 and
  36.
- CBC Run 6's WORK-7, CBC Run Asks checked at Release's close:
  FINDING-11, 23 and 24.
- CBC Run 6's WORK-8, the apply-retrospective Agent Skill:
  FINDING-6, 10 and 20.
- CBC Run 6's WORK-9, the Entry File stub: FINDING-32.
- CBC Run 6's WORK-10, the PLAN stub: FINDING-31.
- CBC Run 6's WORK-11, the playbook's Plan Step Form: FINDING-30.
- CBC Run 6's WORK-14, the auto-run Approach on Trial: FINDING-11
  and 26, TAUGHT-1.
- CBC Run 6's WORK-15, `.gitignore` written by hand: FINDING-38.
- CBC Run 6's WORK-17, how much a CBC Run records: FINDING-40 and
  41.
- CBC Run 6's WORK-18, the TODO items whose trigger fired:
  FINDING-39, TAUGHT-2 and TAUGHT-4, and the four TODO items in §8.

**Ending with no item:**

- FINDING-29: `temp/RUN-4.md` was read whole for the Plan Step's
  item, and is deleted at the judging.
- FINDING-34 and 35: CBC Run 4's own questions, answered by the
  read. The status line and the Plan Steps confirmed once framed held
  as written.
- FINDING-37: `temp/` has shipped from the container since CBC Run
  5's pin (CBC Run 5's FINDING-39).

## 7. What this CBC Run Reading taught

- A CBC Run born by hand from two pins needs its base checked
  against both: the Receipt Branch against the copies' pin, and main's
  own landing against the Receipt Branch.
- A CBC Run on full auto may log its edits in its own decision log,
  not in the Decisions Log. Working-a-reading step 6 then reads them
  as unrecorded, and the decision log is the place to check.
- The lesson of the judging, on working-a-reading step 1's count, is
  in CBC Run 6's Reading, §7.

## 8. Notes

- **Counts, by script:** 158 commits on main; per step, 10, 14, 6,
  13, 8, 12, 18, 19, 14, 8, 7, 17 and 12, for Steps 0 to 11 with
  Step 2b. 28 changed copy files, 498 lines in and 237 out, two of
  them the project's own scripts. 12 CBC Run Asks, 41 findings,
  4 taught.
- **Not committed:** nothing; the tree is clean at `7637a79`.
- **Hashes cited:** `dac4dd1` is on CBC Run 3's repo; `35edd3f` is on
  our main; the CBC Run's own commits cited here are on its main.
- **TODO items this Reading triggers,** for the judging:
  - "Decide whether our own forms become Output Shapes": FINDING-39.
  - "Read the frozen CLAUDE template's stance bullets against a full
    CBC Run's derived Entry File": FINDING-32.
  - "Sort `docs/baselines/` by kind": CBC Run 4 had a Release, where
    the Spring Invariant Slice reference opens.
  - "Land two facts from the agent's memory in the exchange
    convention": its trigger includes "a reading of a CBC Run opens".
- **Not read whole:** the framing exports, the slice records, the
  ADRs, the code and the tests. Read whole: the Decisions Log,
  `RETRO.md`, `TODO.md`, PLAN, the run file's opening, the Entry File,
  the Step 2b and Step 3 devlog entries, the decision log's Method
  entries; the closing gates of Steps 5 to 11 by search.
- **`temp/RUN-4.md` read whole,** for the Plan Step's item; deleted at
  the judging.
- **Nothing in CBC Run 4 was written to.**

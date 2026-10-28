<!-- The reading of run 5, event-tickets, opened 2026-10-22 by
     exchange-read and worked in place. A step before run 6's birth
     takes what run 6 needs, and the rest is taken after the
     refinement. It stays here until the note that
     carries its verdicts goes (exchange-deliver); then it is
     deleted, and git keeps it. Its form is
     .claude/rules/exchange-reading.md; how it is worked,
     .claude/rules/working-a-reading.md. Our paths and decisions
     are cited freely: nothing here goes to the run. -->

Run 5, `~/IdeaProjects/cbc-pure-run-5`: read through `80099b1`.

## 1. Where we read to

- **Read through:** `80099b1`, run 5's main, 2026-10-22 09:11: two
  commits to its `TODO.md` after its Release, `2cab15d` at 08:45,
  tagged `v0.1.0` and `run5/step-13`. This line first said
  `2cab15d`; the run moved before the read began.
- **Previous read-through:** none. Run 5 was born 2026-10-22 at
  00:48 from our pin `ae8a041`, and this is its first reading.
- **The span:** its whole history, 215 commits on main, 14 step
  tags `run5/step-0` to `run5/step-13`, 41 branches.
- **The base for the diff of its copies:** `birth-seed`, the
  receipt branch its seed cut, which holds exactly what was
  delivered at `ae8a041`.

## 2. What the run did

Times are commit times, all 2026-10-22. Each step ran on its own
branch, fast-forwarded to main and tagged at its close.

- **Step 0, Bootstrap, 01:01 to 01:07, 24 commits.** Landed the
  delivery byte-equal to the pin in its own commits, then its own
  files: the delegation of every sign-off (its second decisions
  entry), the stop hook, the decision log, a glossary, `run.md`
  adopted as `docs/run.md`, two approaches on trial, `birth` and
  `checks`, and two checks, `records-check.sh` and
  `commits-check.sh`. One gate item struck: five subjects over 50
  characters landed before the commits check existed (ADR-0002).
- **Step 1, Framing, 01:11 to 01:25, 25 commits.** The briefing
  committed unchanged; stages 0 to 6 each as a work commit then a
  verdict commit; seven candidate promises, six banked; KILL-12
  born at the close when the kill shape was read.
- **Step 2, Identity, 01:26 to 01:27, 9 commits.** `event-tickets`
  in five spellings (ADR-0004); the `identity` approach drafted;
  the plan reread turned "Steps 5..N-3" into six slice steps,
  SLICE-6 before SLICE-5, as the framing's expected order.
- **Step 3, Ground, 01:34 to 01:38, 13 commits.** PostgreSQL 17 in
  rootless podman, the role split and a reader identity; one dead
  end, a probe table made as postgres and re-owned.
- **Step 4, Skeleton, 01:40 to 01:53, 14 commits.** Spring Boot
  4.1, Java 21; two instances in the harness; the fresh-clone check
  written and shown failing with the ground stopped; 6 tests.
- **Steps 5 to 10, six slices, 01:56 to 04:05, 82 commits.** Each
  with its wall question logged first, options tried on `try/`
  branches, its red kept on a `red/` branch with the failing
  output, its record brought to the shapes at the close. SLICE-6,
  the seam of Seating and Orders, before SLICE-5, recovery. 34
  tests by the end.
- **Step 11, Retrospective, 04:07 to 04:12, 15 commits**, on a
  branch named `retrospective`. `RETRO.md`: the run in numbers, six
  parts walked, D1 to D19; a "Rules in force now" block added on
  top of `.claude/decisions.md`.
- **Step 12, Apply, 04:13 to 08:39, 18 commits.** Six commits at
  04:15 editing seven delivered copies; the store holder; two
  timing fixes to evidence tests at 04:36 and 04:48 after the
  fresh clone failed twice. Then the break.
- **The break, 04:48 to 08:39.** The machine powered off at 04:54
  and booted at 08:26; no record names the time or the cause. The
  records say: the session ended mid-check, the ground had exited,
  the fresh-clone check said db DOWN until `podman compose up -d`,
  and the scratch drafts went with the session (devlog:44-47;
  RETRO D20, D21). The reviewer asked one question in chat at
  05:29; nothing in the repo records it.
- **Step 13, Release, 08:40 to 08:45, 11 commits.** The `release`
  approach drafted; ADR-0020 says a release here is the tag; version
  0.1.0 in `pom.xml` and the CHANGELOG; the registry checked against
  the briefing's In; five known issues; tagged `v0.1.0`.
- **After Release, 09:09 and 09:11:** two commits to `TODO.md`, a
  known issue reworded and the apply ask widened to D21; no log or
  devlog line.

Nothing was pushed; no remote exists. The model was Fable 5.1
throughout. Main holds 215 commits: docs 167, chore 23, feat 12,
test 10, build 2, refactor 1; 57 agent-scoped; 0 touching agent
and project paths together.

## 3. Findings

**FINDING-1. SLICE-1's record was never finished, and five records
say it was.** `docs/system/slices/slice-1.md` ends at its plan,
153 lines, last changed at `c1fdaea` 02:08: no "Evidence, as
delivered", no "Standing guards", no backstop line, no Build or
Document sign-off; on no branch does a later version exist. Its
close commit `241764c` says "the record completed in the
slice-record shape's form" and does not touch the file; L-48, L-49,
L-50, Step 5's ticked gate, the registry's cites, the devlog
(:169-172), RETRO (:78-80, D10) and Step 12's gate all say the
rewrite happened. The run's records check reads links and cites,
not sections. Whose: the run's own, a working-tree edit that never
reached the index; the method's close had nothing that would see it.

**FINDING-2. Every record written after the break is dated
2026-10-23;** every commit is dated 2026-10-22. Twenty lines in
eight files: PLAN's Steps 12 and 13, the devlog's two top headings,
RETRO's parts table and D20, D21, ADR-0020, the CHANGELOG's release
heading, the registry's re-check, `release.md`'s use note, L-102,
L-103, L-106 to L-110. Nothing explains it. Whose: the run's own,
or its session's clock.

**FINDING-3. Seven delivered copies were edited and no Method line
exists in the decision log,** where the hand-off's §7 put one per
fix with its trial's result. Each edit has an entry in
`.claude/decisions.md` (lines 97-159) and a line under *To the
deliverer*, the form `delivered-copies.md` asks for. Two forms for
one fact; the run used the delivered one. Whose: the hand-off's
against the delivered rule.

**FINDING-4. Every edit to a skill, shape or template landed at
Step 12, after the step that would use it,** six commits at 04:15,
each marked "untried here". No fix was trialled by a later step;
only D8's holder code ran, at the apply step. Whose: the
`apply-retrospective` form, which lands lessons at the end.

**FINDING-5. Three weights broken:** the decision log 723 lines
against 400 (110 entries, every one still "Review: open"); SLICE-4's
record 446 against 400; the devlog's Step 3 entry 50 lines against
30. The run named each (L-98; RETRO D6, D14, D15) and kept them as
history. RETRO D15 says the Verdict line per sign-off, 49 of them,
is what filled the log. Whose: the run's own, under the hand-off's
§8.

**FINDING-6. Six commit subjects over 50 characters,** five on
Step 0 before the commits check existed, one closing the
retrospective's plan after it (L-100 says 53; it is 52). Struck at
Step 0 (ADR-0002); a known issue. Whose: the run's own.

**FINDING-7. Commits after a close line and its tag, on the same
branch, then fast-forwarded,** four times: Step 8's ticked gate
after its first close (a stash that never popped, L-80); Step 12's
and Step 13's plan closes one commit after their close lines (a
`git rm` whose path the guard's `git add` could not re-add, L-106,
L-110); and the two `TODO.md` commits after Release, with no log,
devlog or step. Whose: the run's own; §14 says auto ends at
Release's close.

**FINDING-8. The reviewer's message was not taken as the hand-off's
§11 step.** No `temp/message-*.md`, no step, no log line; the
break is recorded as a session ending mid-check. The message came
by chat, which §11 did not foresee. Whose: the hand-off's.

**FINDING-9. The look-back on trial: 13 lines, 0 tries,** and RETRO
D18 counts ten while listing eleven. Every line says "no better
way" and names a part it would keep. D18's verdict "changed": the
line should name the one part the run would remove or the one test
it would change, or say "nothing"; two look-backs written after D18
keep the old form. Whose: the hand-off's trial; TODO's item on the
look-back holds the question.

**FINDING-10. One Real question tried one option of two on a
branch** (L-92: "A stands on the step branch already"), against §4's
one branch per option; and the five winner branches of the other
slices carry no commit of their own, each a label on a step-branch
commit. Whose: the run's reading of §4.

**FINDING-11. L-51 says SLICE-1's three tries "cost an hour"; git
shows 5 minutes 22 seconds.** The longest try of the run took 10
minutes; the one-hour box was never approached. Whose: the run's
own.

**FINDING-12. L-14's try preceded its logged question** by two
minutes, against §4's "the question first". Whose: the run's own.

**FINDING-13. Step 0's close commit cites a hash that does not
exist,** `1a0a0d1`; the fast-forward was to `ac68c14` (devlog
:291-293; RETRO D2). Whose: the run's own.

**FINDING-14. A `red/` branch's first commit is headed "seen red"
over a green run** (`3db4eea` on `red/slice-4-evidence-1`: "Tests
run: 1, Failures: 0"); the next commit holds the red. The record
reads the pair right. Whose: the run's own.

**FINDING-15. The registry repeats a sentence** at
`registry.md:252-254`, "New work enters by re-framing or as a new
slice through this registry, never around it", twice. Whose: the
run's own.

**FINDING-16. Tests do not "say so and skip" when the podman socket
is off,** as §12 asked: `StoreHolder`'s static initializer starts
the container with no guard. Never exercised; the socket was on.
Whose: the run's own, under §12.

**FINDING-17. Drafts and a tick script lived outside the repo and
were lost** at the break (RETRO D21), against §5's "nothing is kept
outside the repo". Whose: the run's own.

**FINDING-18. The delegation entry is the second entry** in
`.claude/decisions.md`, after the seed's birth entry; §8 said "the
first". Whose: the hand-off's wording against the seed's form.

**FINDING-19. The glossary was started at the birth,** where the
framing skill says framing starts it; §6 wanted each tag kind
defined at first use, and the log used them at Step 0 (L-7). Whose:
the hand-off's §6 against `cbc-framing`.

**FINDING-20. An approach on trial was drafted before its step's
gate was opened,** three times (`birth`, `identity`, `release`),
with "the gate was written before the work started" ticked. Whose:
the run's; our step form leaves the order open.

**FINDING-21. `fresh-clone-check.sh` has no decision-log line of its
own,** which `checks` stage 4 asks for. Whose: the run's own.

**FINDING-22. PLAN's decision index lists ADR-0001 only, of 20; the
"Discovered along the way" placeholder stands.** As the stub shipped
them. Whose: the run's, or the stub's, which carries no instruction
to maintain the index.

**FINDING-23. Three evidence tests changed after their slices were
signed,** at the apply step (`0d277eb`, `f05caa0`), with dated
Revisions on their records and the gate item "no evidence test
changed" struck in part (L-104, L-105). Whose: the run's own,
logged.

**FINDING-24. A "Rules in force now" block sits on top of
`.claude/decisions.md`,** an append-only log, added by the
retrospective skill's Stage 4 (`f30f66c`). Run 4 did the same; that
case is FINDING-77 of round 1, moved to run 4's reading. Lived
twice. Whose: the `retrospective` skill's.

**FINDING-25. Two hunks left unwrapped lines:**
`infra-establish/SKILL.md:122` at 112 characters and
`spring-harness-reference.md:434` at 77. Whose: the run's edits.

**FINDING-26. D6's new record file takes the name of the skill's own
reference:** `docs/infrastructure/establishment-walk.md` beside
`references/establishment-walk.md`, which `SKILL.md:15` and `:62`
point at. Whose: the run's edit.

**FINDING-27. Three pointers in the asks miss:** A5's end hash
`76a3318` touches `COMMIT-PLAN.md` only, the last `identity.md`
commit being `27362c8`; A13 says D20 changes `release.md`'s stage
4, where D20's own "Lands in" names `checks.md` and the check
script; A4's range ends before three later commits to `checks.md`,
one of which adds two stages. Whose: the run's own.

**FINDING-28. L-110's lesson for the guard form,** a `git rm`
deletion committed without re-adding its path, is not in
`checks.md`, where the run's tooling lessons land. Whose: the run's
own.

**FINDING-29. Four of eleven first reds stayed green behind a
backstop, found only because the red was kept** (L-55; `3db4eea`;
`ecf9e26`; `d914c97`). The delivered `cbc-slice` said only to note a
backstop seen. Whose: the delivered skill's gap; fixed on the copy
at `d476ab1` (D10), untried.
*The shape's half taken (`4fc9037`); the skill's waits for E10
(WORK-3).*

**FINDING-30. Two evidence tests proved nothing on their first run,
green on both trees:** SLICE-6's pairs released exactly at the
instant never met (20 of 20 passed on); SLICE-5's kill at a fixed 15
ms fell before every write. Nothing delivered said how a race at an
instant or a kill at a step is timed. Whose: the delivered skill's;
D11 on the copy, untried.

**FINDING-31. The eight "for run 5 only" lines our playbook v9
carried were each answered in a Notes line** (ticked gates at
`c6cfe94`, `451213c`, `aa84bff`, `2bb861c`, `328163e`, `bbffe0d`,
`c2065d9`, `fda6ef1`): `cbc-framing`, `infra-establish`,
`cbc-bootstrap`, `cbc-slice`, `retrospective`, `apply-retrospective`
and the Release form each "held", with the gaps the asks below carry;
shapes at the gate "caught drift once, at SLICE-1, and taught the
form for the five slices after" (RETRO:78-80), which FINDING-1 now
qualifies. The lines are spent. Whose: our playbook's.

### The edits, one line per hunk

Thirteen hunks in ten delivered files, all against masters that
have not moved since the pin; none decided.
*Since the read, the refinement's reference rewrite moved lines in
some masters, outside the hunks; each take checks its hunk still
applies (2026-10-29, at E8).*

- **E1** `approach-drafting.md:120-126`, `b38b10b`, Step 0: a use
  note. "The reviewer chooses" ran as the run's own choice; the
  choosing stage needs a line saying who chooses when verdicts are
  delegated.
- **E2** `shapes/slice-record.md:84-86`, `b27b5a2`, D10: the block's
  backstop line names the backstop and says "seen catching at the
  red run, with the red taken again with it absent". Untried.
  *Taken whole 2026-10-29 (`4fc9037`).*
- **E3** `shapes/slice-record.md:187-191`, same commit, D10: the
  rule: a test that stayed green is no red. Untried.
  *Taken 2026-10-29 (`4fc9037`), with one change of ours: "a test
  that stayed green is no red" goes. It rules the work, not the
  record's form; its home is `cbc-slice` Stage 3, by E10.*
- **E4** `cbc-bootstrap/references/app-structure.md:47-50`,
  `a2f1ddc`, D12: a read never runs inside another read's row
  mapper; lived as fifteen 500s. Untried.
- **E5** `spring-boot-walkthrough.md:254-260`, same, D12 and D8:
  recall items 12 and 13, the nested read and killing by process
  handle, never `pkill` by a name the shell carries. Untried as
  text; D8's holder code ran.
- **E6** `spring-harness-reference.md:424-437`, same, D11: a race
  named for an instant is released before it and asserts both
  orders happened; a kill is timed from the store's first sight of
  the step. Untried; written before L-105's third answer mix.
- **E7** `spring-harness-reference.md:503-514`, same, D7 and D8:
  the witness read as the reader identity, counting rows not
  ports; the holder deletes stale instance logs. Untried as text.
- **E8** `cbc-framing/templates/registry.md:45-46`, `e0c03ba`, D3:
  the Record and Answered-at-close slots say "none" until filled,
  as the registry-entry shape says. Untried.
  *Taken whole 2026-10-29 (`5e29435`).*
- **E9** `cbc-slice/SKILL.md:92-97`, `d476ab1`, D14: Stage 1's gate
  adds "four guarantees at most"; more is more than one invariant,
  split at the registry. Untried; SLICE-4 kept its five.
- **E10** `cbc-slice/SKILL.md:148-156`, same, D9 and D10: the naive
  version is removed on a tree that never lands, a branch beside,
  the failing output committed there; a test green with its wall
  absent is not red. Untried.
- **E11** `cbc-slice-workflow.md:146-163`, same, D11 and D13: three
  "Why" paragraphs, the race straddling its instant, the kill timed
  from the store, the scene outlasting its test. Untried; D13 lived
  again at L-104 after it landed.
- **E12** `infra-establish/SKILL.md:113-124`, `0fcdfa1`, D6: the
  walk as lived in its own file beside the manuals, the devlog
  entry linking it. Untried; run 5 has no such file.
- **E13** `postgres-setup-walkthrough.md:125-129`, same, D5: a
  check's probe table is made as the migrator, never as the
  bootstrap identity and re-owned. Untried.

### The asks, one line each

Run 5's *To the deliverer*, 13 lines at `80099b1`; none decided.

- **A1** apply RETRO's D1 to D21 to the copies each names under
  "Lands in" (an ask). Nine land only in our hand-off or the run's
  own files: D2, D4, D15, D18, D19, D20, D21 "next run only"; D16,
  D17 in `checks`.
- **A2** evaluate E1, the `approach-drafting` use note (an ask).
- **A3** `birth.md` offered for evaluation, `4cc0d93`..`b38b10b`;
  D1 changes its stage 4 (an offer).
- **A4** `checks.md` offered, `90feba8`..`b38b10b` and after; D1,
  D16, D17 change it (an offer).
- **A5** `identity.md` offered, `be82f3c`..`76a3318`; D4 moves the
  group id to the run file (an offer).
- **A6** the registry template's Record slot against the
  registry-entry shape, D3 (a notice; answers Step 1's gap).
  *E8 taken (`5e29435`); the note answers it (WORK-2).*
- **A7** evidence on the workflow's open question "the multi-owner
  case end to end": `definition.md`'s LAYER-3 and LAYER-5 (an offer
  of evidence, no decision).
- **A8** the walkthrough's step 7, the probe table as the migrator,
  D5 (a notice; answers Step 3's gap).
- **A9** evidence on the role split's "readers" extension: ADR-0007
  and `bootstrap.sql` (an offer of evidence).
- **A10** the harness reference's variation point 8 lived a second
  time, the witness read as a non-superuser, D7 (a notice).
- **A11** `cbc-slice` Stage 3's two sentences on the naive version,
  D9 (a notice; answers Step 5's tension).
- **A12** evaluate the run's changes to the registry template,
  `infra-establish`, `cbc-bootstrap`'s references, `cbc-slice` and
  the slice-record shape, "untried here" (an ask: E2 to E13).
- **A13** `release.md` offered, `52518f7`..`d02937f`; D20 (an
  offer).

## 4. What the run taught us that we had not thought of

- **Full auto ran the whole playbook in about four hours of commit
  time:** 14 steps, six slices in 2 hours 9 minutes. The hand-off's
  one-hour box per option was sized for a human day; the longest
  try took 10 minutes.
- **The red run is where the walls' dependency graph shows.** Four
  reds stayed green behind another wall; `slice-4.md:417-422` lists
  which wall stands behind which, known only from the reds.
- **A race named for an instant must be released across it and read
  against every order the instant can produce;** a third order
  appeared only on a cold clone (L-105).
- **A kill timed from the release misses every write on a cold
  instance;** timed from the store's first sight of the work, it cut
  15 of 30 decisions (`slice-5.md:212-217`).
- **The losing try taught what the winner could not:** a row lock
  does not make a read of another table see the holder's write
  (`slice-6.md:156-164`); a sweeper is a part that can stop.
- **The scene's measure is the slowest machine the check runs on:**
  15-second holds lost to a cold clone's build and start.
- **A Stop hook cannot tell waiting from stopping:** eleven firings
  while a suite or a clone ran in the background (D19).
- **A session break takes the compose ground and the scratch space
  with it;** what was committed survived.
- **Full-auto slips are shell-composition slips:** a refused commit
  chained with `git add`, a restore chained after a refusal, a stash
  that never popped, `git rm` then the guard's `git add`. The run's
  own answer is a guard form (`checks.md:30-36`).
- **Two background checks sharing one directory delete each other's
  build** and both fail on a green tree; a lock by `mkdir` (D17).
- **A read nested in a row mapper takes a second pool connection
  while the first is held;** 25 requests against a pool of 10
  waited 30 seconds (D12).
- **Records outweigh code forty to one:** 48,484 words of records
  against 544 lines of main code; 123 of 155 commits at the retro
  were `docs`.
- **A shape teaches at its first reading and is silent after:**
  three differences at framing, three at SLICE-1, "no difference"
  at every close after; and the one rewrite it asked for never
  reached history, which no later reading caught.
- **Skills that say "ask" need a line for when nobody answers:**
  the group id (L-30, D4); "the reviewer chooses" in
  `approach-drafting` (E1).
- **A strict tag reader finds negations:** "no KILL-12" read as a
  cite; the run kept the check strict and reworded the text.
- **A local release needs its own definition:** nothing delivered
  said what a release is when nothing deploys; `release.md` and
  ADR-0020 say the tag is the artifact.
- **The promise's subject moved from the seat to the payment:**
  "each confirmed payment ends as exactly one ticket, or as a
  recorded refund owed", because the money is what the buyer must
  never lose; both complaints follow from it.

### What run 5 teaches the worked example (§6.3)

The worked example, one order service, one area, idempotency,
LAYER-5 "empty, with reasons", never shows what run 5 lived:

- two areas, each with its own state and decisions, and a thing
  both own: the ticket is a seat's terminal state in Seating and a
  payment's outcome in Orders (`definition.md:186-204`);
- a LAYER-5 that is not empty: one seam and one constraint across
  it, "the two readings are one decision, never two made apart"
  (`:353-361`), and four kills that are the seam's (`:363-367`);
- three seams named and not drawn (`:206-209`);
- the meeting of a hold's expiry and a payment's confirmation,
  KILL-13 (`:305-312`), with the clock as an actor
  (FACT-CLOCK-13, `:49-52`);
- a slice whose test stages the meeting, SLICE-6, across two
  instances, released a few ms before the instant and asserting
  both orders happened (`slice-6.md:106-111`, `:273-280`);
- the seam's wall, one conditional write on one row, chosen on a
  branch against a lock (`slice-6.md:127-137`; ADR-0018);
- an outcome handed across the seam provisionally and decided by
  the later slice (`slice-4.md:372-374`; `slice-6.md:32-40`);
- refusals mirroring a briefing's Out, and a table "The briefing's
  In, covered", re-checked at Release (`definition.md:169-184`;
  `registry.md:333-358`);
- each trouble the briefing names mapped to the slice whose test
  stages it (`registry.md:350-353`);
- a kill that breaks nothing, carried as a fold (KILL-12);
- scope verdicts, a reader identity for the witness, a stand-in the
  harness plays for the outside party, time as an adversary with no
  sweeper, backstops seen catching, a kill timed from the store;
- size: 7 actors, 15 facts, 15 kills, 7 concerns, 8 folds, 6
  slices, 11 fences, against the example's 6 facts, 6 kills, 2
  slices.

Where its artifacts diverge from the example's shape, they follow
the delivered shapes, which the example predates: records in the
slice-record shape's ten sections, three with an eleventh,
Revisions, the shape does not name; evidence criteria inside each
guarantee's block; condition-first guarantee headings; registry
entries in the registry-entry shape's ten slots, grouped by area
with a seam section; definition and intent sections with no
counterpart in the example.

## 5. Decisions

**DECISION-1. Can a copy's edit be taken on evidence alone?** Rests:
E2 to E13, all twelve untried, landed after the step that would
use them; A12 says so. Gates WORK-3 to WORK-9. The exchange's
"taken" changes a master here (`docs/conventions/exchange/` §6.5);
whether "untried" lowers the bar, raises it, or makes a fourth
ending is not written anywhere.
**Settled 2026-10-29, by ADR-0051,** which this question missed:
an untried edit is taken when it is sound, and the next run is its
trial. Each of E1 to E13 is judged on its own evidence, with the
three endings, read hardest. The exchange now says so, where it
already spoke of untried edits (`docs/conventions/exchange/` §5.2,
*A copy the run has finished…*).

**DECISION-2. Where do the nine "next run only" lessons live?**
Rests: A1's D2, D4, D15, D18, D19, D20, D21 (the hand-off), D16,
D17 (the run's checks). Our hand-off is deleted and git keeps it;
`auto-run.md` is the master a next hand-off is written from. Gates
WORK-10 and `auto-run`'s evaluation (TODO).

**DECISION-3. What does FINDING-1 ask of the method?** A record's
rewrite at the gate was lost between the working tree and the
index, and six later checks said it was done. Rests: FINDING-1,
FINDING-24 (the retrospective reading the records), the "shape
teaches once" lesson. Gates WORK-11. Nothing decides whether a
close's check must read a record's sections, or whose that check
is.

**DECISION-4. How does a run's offered approach reach the
evaluation?** Rests: A3, A4, A5, A13. `approach-evaluation`'s *Not
known yet* holds this question; four offers now wait on it. Gates
WORK-12 to WORK-15.

**DECISION-5. Is the hand-off's §7 Method line, §11 message step and
§8 "first entry" wording wrong, or the run?** Rests: FINDING-3, 8,
18, 19. Each is a place where our hand-off said one thing and the
delivered files another. Gates WORK-10.

**DECISION-6. Does the reading of run 4 come before this one is
worked?** Rests: FINDING-24 (lived twice), E5 and E7 (run 4's D4,
D5, D8 cover the same traps per its RETRO), the playbook's run-3
lines. Two readings open; one order for their work.

## 6. The work

Preliminary order; the reviewer reorders it. **plan** marks a
commit plan of its own.

- **WORK-1.** The playbook: the eight "for run 5 only" lines retire,
  their answers folded (FINDING-31); its version note names run 5.
- **WORK-2.** Answer the four notices that close earlier asks, A6,
  A8, A10, A11, in the note.
- **WORK-3. plan.** `cbc-slice`: E9, E10, E11 (D9, D10, D11, D13,
  D14) against the master, read whole, and the concept's chapter
  04; the worked example's two copies if touched.
- **WORK-4. plan.** `cbc-bootstrap`'s three references: E4, E5,
  E6, E7 (D7, D8, D11, D12).
- **WORK-5.** `infra-establish`: E12, E13 (D5, D6), with
  FINDING-26's name collision and FINDING-25's lines.
- **WORK-6.** The registry template: E8 (D3), against the
  registry-entry shape and the framing skill.
  *Done 2026-10-29: E8 taken whole (`5e29435`).*
- **WORK-7.** The slice-record shape: E2, E3 (D10), under
  `docs/conventions/shapes/` §5.2's endings.
  *Done 2026-10-29 (`4fc9037`): E2 taken whole, E3 taken with one
  change of ours.*
- **WORK-8.** The `retrospective` skill: FINDING-24, the block on
  top of an append-only log, lived twice, with run 4's FINDING-77.
- **WORK-9.** The `approach-drafting` master: E1, who chooses when
  verdicts are delegated (A2); the container's copy follows.
- **WORK-10. plan.** `auto-run.md`: the nine "next run only"
  lessons (D2, D4, D15 to D21) and FINDING-3, 8, 18, 19 into its
  stage 4; its evaluation is TODO's item.
- **WORK-11.** FINDING-1 as a question for the method: a close that
  reads a record's sections, where it lives; a TODO item or a
  decision (DECISION-3).
- **WORK-12 to WORK-15. plan each.** Evaluate `birth`, `identity`,
  `checks`, `release` by `approach-evaluation`, once DECISION-4 is
  answered.
- **WORK-16.** A7 and A9: read the two offers of evidence against
  the framing workflow's open question and the role split; a line
  each in the note.
- **WORK-17.** TODO's look-back item takes FINDING-9 and D18 as its
  first evidence; TODO's examples item takes the worked-example
  section; TODO's "how work is run by agents" item takes the fact
  that run 5 delegated nothing.
- **WORK-18.** The findings that are the run's own (FINDING-2, 5,
  6, 7, 10 to 17, 20 to 23, 27, 28) go to the note as findings,
  none a verdict; FINDING-1 first.
- **WORK-19.** `ARCHITECTURE.md` §2.5: run 5 "read, not yet
  answered" after this reading, "answered" after the note.
- **WORK-20.** The note, by `exchange-deliver`: every verdict in
  the run's order, the read-through `80099b1`, the files that
  changed since the pin.

Counted (`.claude/rules/working-a-reading.md`, step 1): 20 work
items, 7 marked plan. More than one plan: the step that works this
reading cuts a branch from main.

## 7. What this reading taught

- **A run that has ended can still move.** Two commits landed
  after Release while this read opened; the read-through was moved
  once, before anything was read, as the skill allows. The next
  read checks the run's session is idle before writing its first
  line.
- **Three readers side by side, each on one of the three things,
  worked;** every claim checked against the tree held, and one
  wrong line number was the only miss. A fourth reader for the
  playbook's lines would have saved a fetch.
- **An extract given to a reader goes stale with the run:** the asks
  file was one commit behind main. Readers read the run, not a
  copy.
- **A reader's "merged" needs a meaning:** five winner branches
  carried no commit of their own; the reading says so.
- **Search the ADRs before writing that a question is unwritten.**
  DECISION-1 called its question "not written anywhere". ADR-0051
  had settled it, and the manual carried only half of it. Found
  2026-10-29, when the question was worked.

## 8. Notes

- **Counts:** 215 commits read; 13 edits in 10 files; 13 asks; 31
  findings; 17 lessons and 12 facts for the worked example; 6
  decisions; 20 work items, 8 plans.
- **Not decided here:** anything. The work waits for the refinement
  to close, and this file keeps, since the pin does not move.
- **Not read:** run 5's 102 open log entries as a review; that is
  the reviewer's, as its hand-off says.
- **Run 5's tree:** quiet, nothing staged or changed; its session
  idle since 09:11.
- **Verified, 2026-10-22 09:42, on a clone of `80099b1` outside run
  5:** `./mvnw test` 34 tests in 17 classes, 0 failures, 0 errors,
  0 skipped, 2 minutes 40 seconds; the jar packaged and started
  against run 5's standing ground, health UP, db UP. The records'
  numbers hold.
- **Delegations, three readers, Fable 5.1, effort as the session's:**
  what the run did (40 tool uses, 10 min), the edits and asks (40,
  11 min), findings and lessons (48, 16 min). All three paid.

<!-- The CBC Run Reading of CBC Run 5, event-tickets, opened
     2026-11-26 by the exchange-read Agent Skill and worked in place.
     It replaces the Reading of 2026-10-22, closed as overtaken
     (in git at 4a44c206:temp/reading-run-5-2026-10-22.md, to
     compare). It is judged with CBC Run 4's and CBC Run 6's in the
     Plan Step "Read and judge CBC Runs 4, 5 and 6", by today's
     exchange (ADR-0089). No Delivery Note carries it: it is kept here
     for the rewrite, where its taken items land. Its form is
     .claude/rules/exchange-reading.md; how it is worked,
     .claude/rules/working-a-reading.md. Our paths and decisions are
     cited freely: nothing here goes to the CBC Run. -->

CBC Run 5, `~/IdeaProjects/cbc-pure-run-5`: read through `80099b1`.

## 1. Where we read to

- **Read through:** `80099b1`, CBC Run 5's main, 2026-10-22 09:11,
  four commits after the tags `run5/step-13` and `v0.1.0`. The tree
  is clean.
- **Previous read-through:** none. CBC Run 5's birth entry in its
  `.claude/decisions.md` reads "pin ae8a041; read-through none", and
  no Delivery Note was ever sent. The Reading of 2026-10-22 read
  through the same `80099b1`; it closed as overtaken on 2026-11-26.
- **The span:** its whole history, 215 commits on main, 14 step
  tags `run5/step-0` to `run5/step-13`, the tag `v0.1.0`, 40
  branches. No remote.
- **The base for the diff of its copies:** `birth-seed`, the Receipt
  Branch its seed cut, at `307bee1`. Of the 56 files under our pin
  `ae8a041`'s `delivery/container`, `delivery/method` and
  `delivery/spring-postgres`, 50 equal it blob for blob, and the 6
  others are records the seed fills: the Entry File, the Decisions
  Log, PLAN, README, the devlog and ADR-0001. The 5 concept chapters
  equal `concept/` at the pin. The seed does not land the other 3:
  `delivery/README.md`, the playbook and the seed itself.
- **Main does not descend from `birth-seed`.** It landed the same
  files in its own commits (L-3), and the diff below is against
  `birth-seed`.

## 2. What the CBC Run did

Times are commit times, all 2026-10-22, from 00:48 to 09:11. Each
step ran on its own branch, under a commit plan, fast-forwarded to
main and tagged. The run was on full auto: every sign-off delegated
to it, a stop hook refusing a stop until Release, and the run file
`docs/run.md` deciding what no skill covered.

- **Step 0, Bootstrap, 24 commits.** The delivery landed byte-equal
  to the pin in its own commits, then the run's own: the delegation
  entry, the decision log, the glossary, two checks, the birth and
  checks Approaches on Trial. Five subjects over 50 characters were
  history before the commits check existed; the gate item was
  struck (ADR-0002).
- **Step 1, Framing, 25 commits.** Seven candidate promises; the
  payment as the subject, not the seat. Two areas and one seam; six
  slices; LAYER-5-INTERACTION not empty. ADR-0003. The kill and
  registry-entry shapes, read at the gate, found three drifts.
- **Step 2, Identity, 9 commits.** The briefing's name
  `event-tickets` kept; the group id derived from the author handle
  (L-30). ADR-0004. The identity Approach on Trial drafted.
- **Step 3, Ground, 13 commits.** PostgreSQL 17 under rootless
  podman, the role split and a reader identity, verified both ways.
  ADR-0005 to ADR-0007. One dead end: the probe table made as
  postgres.
- **Step 4, Skeleton, 14 commits.** Boot on Java 21, health UP with
  db UP; the harness forking two real instances. ADR-0008.
- **Steps 5 to 10, SLICE-1, 2, 3, 4, 6 and 5, 82 commits.** Each
  slice's wall tried on branches, 13 `try/` and 11 `red/` in all.
  SLICE-6 ran before SLICE-5. ADR-0009 to ADR-0019.
- **Step 11, Retrospective, 15 commits.** `RETRO.md`, D1 to D19.
- **Step 12, Apply the retrospective, 17 commits.** Eleven
  decisions applied and four partly: ten delivered copies edited
  untried, the checks grown, the store holder clearing stale logs;
  three evidence tests' scenes retimed after two fresh-clone
  failures (L-104, L-105).
- **Step 13, Release, 12 commits, and 4 after its tag.** `0.1.0`
  locally; ADR-0020 excludes deploy, rollback, monitoring and
  alerts; D20 and D21 added to `RETRO.md`. The release Approach on
  Trial drafted.
- **The CBC Run Asks,** 13 lines under `## To the deliverer` in its
  `TODO.md`, written from Step 1 to Release.

## 3. Findings

### The edits its Decisions Log records

- **FINDING-1. The approach-drafting Approach on Trial gains a use
  note for Step 0:** who chooses when the verdicts are delegated
  (`.claude/approaches-on-trial/approach-drafting.md`, the Decisions
  Log's Step 0 entry).
- **FINDING-2. The registry template's Record and Answered-at-close
  slots say "none" until filled** (`cbc-framing/templates/registry.md`,
  D3, `e0c03ba`). Untried.
- **FINDING-3. The infra-establish Agent Skill: the walk as lived
  goes to `docs/infrastructure/establishment-walk.md`, and the
  devlog links it; the walkthrough's step 7 makes the probe table
  as the migrator** (`infra-establish/SKILL.md`,
  `references/postgres-setup-walkthrough.md`, D5, D6, `0fcdfa1`).
  Untried.
- **FINDING-4. The cbc-bootstrap Agent Skill's three references:
  the witness read as the staff's identity counts rows; the holder
  clears stale instance logs; a race straddles its instant and a
  kill is timed from the store; the nested read; the anchored kill**
  (`spring-harness-reference.md`, `spring-boot-walkthrough.md`,
  `app-structure.md`, D7, D8, D11, D12, `a2f1ddc`, `8669758`).
  D8's log clearing was tried at Step 12 and the suite ran green;
  the rest untried.
- **FINDING-5. The cbc-slice Agent Skill: four guarantees at most at
  the specification gate; the red tree only on a branch beside; a
  test green with its wall absent names its backstop and is taken
  again; three whys in the workflow** (`cbc-slice/SKILL.md`,
  `references/cbc-slice-workflow.md`, D9, D10, D11, D13, D14,
  `d476ab1`). Untried.
- **FINDING-6. The slice-record shape names the backstop "seen
  catching", with the red taken again** (`.claude/shapes/slice-record.md`,
  D10, `b27b5a2`). Untried; the six records were not reopened.

### Written, and not in its Decisions Log

- **FINDING-7. Four Approaches on Trial of its own: birth, checks,
  identity, release,** drafted at Steps 0, 0, 2 and 13. No Decisions
  Log entry for any. Its "Rules in force now" list names the first
  three, not release. All four are offered under *To the deliverer*.

### The CBC Run Asks

- **FINDING-8. CBC Run Ask 1: apply `RETRO.md`'s D1 to D21 to the
  copies each names under "Lands in",** D20 and D21 added at
  Release.
- **FINDING-9. CBC Run Ask 2: evaluate the approach-drafting use
  note** (FINDING-1).
- **FINDING-10. CBC Run Ask 3: the birth Approach on Trial offered,**
  `4cc0d93`..`b38b10b`; D1 changes its stage 4.
- **FINDING-11. CBC Run Ask 4: the checks Approach on Trial
  offered,** `90feba8`..`b38b10b` and the use notes after; D1, D16
  and D17 change it.
- **FINDING-12. CBC Run Ask 5: the identity Approach on Trial
  offered,** `be82f3c`..`76a3318`; D4 moves the group id to the run
  file.
- **FINDING-13. CBC Run Ask 6: the registry template's Record slot
  against the registry-entry shape:** D3.
- **FINDING-14. CBC Run Ask 7: evidence on the workflow's open
  question "the multi-owner case end to end":** `docs/system/definition.md`,
  LAYER-3-AREAS and LAYER-5-INTERACTION. Evidence only.
- **FINDING-15. CBC Run Ask 8: the walkthrough's step 7, the probe
  table as the migrator:** D5.
- **FINDING-16. CBC Run Ask 9: evidence on the role split's
  "readers" extension:** ADR-0007,
  `infrastructure/postgres/init/bootstrap.sql`. Evidence only.
- **FINDING-17. CBC Run Ask 10: the harness reference's variation
  point 8, lived a second time:** D7.
- **FINDING-18. CBC Run Ask 11: the cbc-slice Agent Skill's two
  sentences on the naive version:** D9.
- **FINDING-19. CBC Run Ask 12: evaluate the changes since `ae8a041`
  to the registry template, infra-establish, the cbc-bootstrap
  references, cbc-slice and the slice-record shape,** all untried
  (FINDING-2 to FINDING-6).
- **FINDING-20. CBC Run Ask 13: the release Approach on Trial
  offered,** `52518f7`..`d02937f`; D20 changes its stage 4.

### The read

- **FINDING-21. SLICE-1's record was never finished.**
  `docs/system/slices/slice-1.md` is 153 lines and ends at its plan
  and *Sign-offs*. It has no *Evidence, as delivered* and no
  *Standing guards*; SLICE-2's has both. Its close commit `241764c`
  says "The record completed in the slice-record shape's form" and
  does not touch the file. The file last changed at `c1fdaea`, the
  plan. RETRO's "the shapes at the gate caught drift once, at
  SLICE-1" rests on it. The old Reading's FINDING-1.
- **FINDING-22. No Method line in the decision log.** The run file
  §7 asks one per fix to a delivered copy. Ten copies were edited;
  the 110 entries are 49 Verdict, 41 Small, 13 Look-back and 7 Real,
  by script. The edits are in the Decisions Log and TODO only.
- **FINDING-23. The decision log was never reviewed.** 110 entries,
  none marked agreed or reversed. 723 lines, against the run file's
  400. SLICE-4's record is 446 lines, against 400. RETRO kept both
  as history (*Applied to run 5*). CBC Run 4's has the same (its
  FINDING-27).
- **FINDING-24. Records dated 2026-10-23 for work committed on
  2026-10-22.** Steps 12 and 13 close "2026-10-23", the devlog's top
  two entries, D20, D21, L-102 on. Every commit is 2026-10-22, the
  last at 09:11. The log's L-104 and L-105, dated 10-22, sit before
  L-102.
- **FINDING-25. Each step closed with two fast-forwards:** main took
  the ticked gate, then the close line, which says "the fast-forward
  item ticked here once main took the branch". The close line was
  true when written: main's reflog shows two fast-forwards at each of
  the 14 closes. CBC Run 4 ticked the item before the fast-forward
  (its FINDING-30). This answers CBC Run 4's question, how a CBC Run
  closed its Plan Step branches, for CBC Run 5.
- **FINDING-26. Four commits after Release's close line and its
  tags,** `05de35a`..`80099b1`, on `step/13-release`, fast-forwarded
  to main. TODO's known issues name it (L-110).
- **FINDING-27. Step 6's "For run 5 only" item is ticked with no
  Notes line.** "A line in Notes says whether reading shapes only at
  the gate cost rework or taught something" (run 3's RETRO D18) is
  ticked at `67f9a4e^`; its Notes hold no such line. RETRO's *The
  run in numbers* answers it. The other seven such items each have
  their Notes line, each "held" with its gaps.
- **FINDING-28. The harness reference's D11 sentences were inserted
  mid-paragraph.** "That is correct for a machinery proof and must
  be stated" now follows the kill sentence, not the probe's claim it
  judged (`spring-harness-reference.md`, about line 434). The
  inserted text and the infra-establish Agent Skill's are left as
  one long line each.
- **FINDING-29. D6's new record takes the name of the skill's own
  reference:** `docs/infrastructure/establishment-walk.md`, beside
  `infra-establish/references/establishment-walk.md`, which the Agent
  Skill points at twice (`SKILL.md:15`, `:62`).
- **FINDING-30. The tests do not skip when the podman socket is
  off,** as the run file §12 asks. `StoreHolder` starts the container
  in a static initializer with no guard. Never met; the socket was
  on.
- **FINDING-31. RETRO.md quotes lines by number, and 9 of its 20
  quotes have moved,** by script: 3 in TODO, 6 in the devlog, whose
  newest entries go on top. The 11 into the decision log and the
  slice records still hold.
- **FINDING-32. The approach-drafting use note covers Step 0
  alone.** Identity and release were drafted with it at Steps 2 and
  13, with no note of their own.
- **FINDING-33. PLAN's Decision index lists ADR-0001 alone,** of
  20. CBC Run 4's lists 1 of 13 (its FINDING-31).
- **FINDING-34. The Entry File keeps its pre-framing paragraph after
  framing.** Its one Local Rule was rewritten at the retrospective.
  Neither the ground-must-be-up rule nor a stack fact was added. This
  answers CBC Run 6's question for CBC Run 5: not added unasked.
  CBC Run 4 (its FINDING-32) and CBC Run 6 (its FINDING-21) are the
  same.
- **FINDING-35. The Decisions Log carries a "Rules in force now" list
  on top,** eight rules, while its header says "Append-only, newest
  last". Written at the retrospective. CBC Run 4 (its FINDING-33) and
  CBC Run 6 (its FINDING-22) did the same.
- **FINDING-36. Six commit subjects over 50 characters,** of 215,
  the longest 58, by script: five on Step 0's branch before the
  check, one closing the retrospective's plan. None past our 70. No
  commit straddles agent and project paths.
- **FINDING-37. Step 0's close commit `357f861` names a hash,
  `1a0a0d1`, that does not exist.** Logged in the devlog, Step 1;
  D2's rule for the commit-messages Agent Skill.
- **FINDING-38. Every look-back found "no better way",** 13 lines, no
  try. D18 changes the run file's look-back.
- **FINDING-39. `temp/` was shipped, tracked, with its README,** from
  our container at the pin. CBC Run 4 had none (its FINDING-37).
- **FINDING-40. `.gitignore`'s Stack Overlay was appended at Step 4**
  (ADR-0008), with one line for the fresh-clone check's working copy.
- **FINDING-41. CBC Run Ask 5's range ends at a commit that does not
  touch identity.** `76a3318` changes `COMMIT-PLAN.md` only; the
  last commit to `identity.md` is `27362c8`. FINDING-12 gives the
  range as the CBC Run Ask wrote it. The old Reading's FINDING-27.
- **FINDING-42. CBC Run Ask 13 says D20 changes the release Approach
  on Trial's stage 4,** but D20's own *Lands in* names
  `.claude/checks/fresh-clone-check.sh` and `checks.md`, not
  `release.md`. FINDING-20 gives the claim as the CBC Run Ask wrote
  it. The old Reading's FINDING-27.

## 4. What the CBC Run taught us that we had not thought of

- **TAUGHT-1. Full auto held from birth to Release in about eight
  and a half hours,** 215 commits, 14 steps. One stop, a session
  ending mid-check, which cost the ground and the session's scratch
  drafts (D20, D21).
- **TAUGHT-2. The losing try taught twice what the winner could
  not:** a lock on a row does not make a read of another table see
  the lock holder's write (SLICE-6); a sweeper is a part that can
  stop (SLICE-3).
- **TAUGHT-3. Four of eleven first reds stayed green behind another
  wall,** each named and taken again (D10). CBC Run 4 lived the same
  (its TAUGHT-3).
- **TAUGHT-4. A race released at its instant never meets, and a
  kill timed from the release cuts nothing** (D11); a test's
  clock-bound scene must outlast its own steps, measured on the
  slowest machine that runs it (D13, L-104).
- **TAUGHT-5. The worked example.** CBC Run 5 lived the multi-owner
  case: two areas, one seam, SLICE-6 the seam, LAYER-5-INTERACTION
  not empty. Its promise's subject is the payment, not the seat.
  What this teaches the worked example is for the judging.

## 5. Decisions

Judged with CBC Runs 4 and 6. The decisions live in CBC Run 6's
Reading, `temp/reading-run-6-2026-11-26.md` §5, its DECISION-1. This
Reading's findings among them:

- CBC Run 6's DECISION-2, held: FINDING-7, 10, 11, 12 and 20; the
  old Reading's FINDING-21 and 28.
- CBC Run 6's DECISION-3, taken: FINDING-21.
- CBC Run 6's DECISION-4, declined: FINDING-23.
- CBC Run 6's DECISION-7, the watch ended: FINDING-34.

## 6. The work

The work lives in CBC Run 6's Reading, §6, with each item's ending.
This Reading's findings among it:

- CBC Run 6's WORK-1, the cbc-slice Agent Skill: FINDING-5, 18 and
  19, TAUGHT-3.
- CBC Run 6's WORK-2, the cbc-bootstrap references and templates:
  FINDING-4, 17 and 28, TAUGHT-4.
- CBC Run 6's WORK-3, the infra-establish Agent Skill: FINDING-3, 15,
  16, 28 and 29.
- CBC Run 6's WORK-5, the commit-messages Agent Skill: FINDING-36
  and 37.
- CBC Run 6's WORK-6, the retrospective Agent Skill: FINDING-31 and
  35.
- CBC Run 6's WORK-7, CBC Run Asks checked at Release's close:
  FINDING-8, 41 and 42; the old Reading's FINDING-27, the third
  pointer.
- CBC Run 6's WORK-8, the apply-retrospective Agent Skill:
  FINDING-19; the old Reading's FINDING-4.
- CBC Run 6's WORK-9, the Entry File stub: FINDING-34.
- CBC Run 6's WORK-10, the PLAN stub: FINDING-33.
- CBC Run 6's WORK-11, the playbook's Plan Step Form: FINDING-25;
  the old Reading's FINDING-20.
- CBC Run 6's WORK-13, the glossary opens at the birth: the old
  Reading's FINDING-19.
- CBC Run 6's WORK-14, the auto-run Approach on Trial: FINDING-8,
  22 and 30, TAUGHT-1; the old Reading's FINDING-3, 8, 10, 11 and
  18, DECISION-2 and DECISION-5.
- CBC Run 6's WORK-15, `.gitignore` written by hand: FINDING-40.
- CBC Run 6's WORK-16, the approach-drafting Approach on Trial:
  FINDING-1, 9 and 32.
- CBC Run 6's WORK-17, how much a CBC Run records: FINDING-23.
- CBC Run 6's WORK-18, the TODO items whose trigger fired:
  FINDING-14 and 38, TAUGHT-2 and TAUGHT-5.

**Ending with no item:**

- FINDING-2, 6 and 13: the registry template's slots and the
  slice-record shape's backstop line were taken on 2026-10-29, in our
  `5e29435` and `4fc9037`, and held in CBC Run 6 (its FINDING-10).
- FINDING-24 and 26, and the old Reading's FINDING-12, 14, 15 and
  23: CBC Run 5's own slips. A Delivery Note would have carried them,
  and none goes (ADR-0089, decision 3).
- FINDING-27: the playbook's "for run 5 only" lines are gone, so the
  old Reading's WORK-1 has nothing left to do.
- FINDING-39: `temp/` shipped as the container meant; it answers CBC
  Run 4's FINDING-37.

**The old Reading's open items,** at `4a44c206`, by where they went:
DECISION-2, DECISION-5 and WORK-10 to CBC Run 6's WORK-14; WORK-1 to
FINDING-27 above; WORK-3, WORK-4, WORK-5, WORK-8 and WORK-9 to CBC
Run 6's WORK-1, WORK-2, WORK-3, WORK-6 and WORK-16, in that order.
WORK-6 and WORK-7 were done on 2026-10-29.

## 7. What this CBC Run Reading taught

- A close line that says a later event happened needs the reflog,
  not the log: only the reflog shows two fast-forwards at one close.
- A record that quotes lines by number in a file with newest entries
  on top goes stale at the next entry. A quote's text is checked, not
  its number.
- The lesson of the judging, on working-a-reading step 1's count, is
  in CBC Run 6's Reading, §7.

## 8. Notes

- **Counts, by script:** 215 commits on main; per step, 24, 25, 9,
  13, 14, 15, 14, 13, 14, 15, 11, 15, 17 and 12, for Steps 0 to 13,
  and 4 after. 14 changed files under the copies' paths, 337 lines in
  and 22 out: 10 delivered copies, and the run's own 4 Approaches on
  Trial. 13 CBC Run Asks, 42 findings, 5 taught.
- **Not committed:** nothing; the tree is clean at `80099b1`.
- **Hashes cited:** the CBC Run's own commits cited here are on its
  main; `ae8a041` is on our main.
- **The old Reading, of 2026-10-22,** read the code, the tests and
  the records more widely: 31 findings, 13 edits, 13 asks. Its items
  not met in this read, FINDING-8, 10, 11, 12, 14, 15, 18, 19, 20,
  21, 23 and 28, and FINDING-27's third pointer, are for the judging
  to compare, at
  `4a44c206:temp/reading-run-5-2026-10-22.md`. Its open DECISION-2
  and DECISION-5, and WORK-1 and WORK-3 to WORK-10, are among the
  items above.
- **Not read whole:** the framing exports, five of six slice records,
  the ADRs, the code and the tests. Read whole: the Decisions Log,
  `RETRO.md`, `TODO.md`, PLAN, the run file, the Entry File, the
  devlog, the copies' diff; the decision log by script and in part;
  the ticked gates' Notes of Steps 1, 3 to 6 and 11 to 13.
- **Nothing in CBC Run 5 was written to.**

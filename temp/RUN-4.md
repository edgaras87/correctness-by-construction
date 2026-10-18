# Run 4: the hand-off

Written 2026-10-15, at the end of run 3, and agreed by the reviewer
the same day, with full auto (see "Decided"). The deliverer starts
run 4 from it.

## What run 4 is

Run 4 builds never-oversold again, from an empty repo. It keeps
every decision run 3 took about the problem. It runs on full auto,
from the first commit to Release, and never stops for the reviewer.
It decides every new question itself, by trying the options before
it picks one. It fixes the method's own files (skills, rules,
shapes) when the work shows them wrong or missing something. Every
decision, with what was rejected and why, goes in one log the
reviewer reads afterwards.

What run 4 tests is the process, not the design. The design is
run 3's. The questions run 4 answers:
- Can an agent run the whole build without stops and stay correct?
- Do the records come out short and plain the first time?
- Are the decisions it takes alone ones the reviewer would take?

## What run 4 starts with

| Input | Where it comes from | Note |
|---|---|---|
| The briefing | `~/IdeaProjects/safe-reservation-briefing.md`, committed unchanged when framing opens, as `docs/system/framing/briefing.md` (RETRO D8) | Found 2026-10-15. The reviewer confirmed it is run 3's. Its last two paragraphs (birth materials, and "stop for my review") give way to `docs/run.md` and the bundle |
| The settled list | This file's "Settled" section, as `docs/settled.md` | The agent does not reconsider it |
| The method | `docs/concept/`, from the bundle | |
| The skills | The bundle, with run 3's fixes handed in first | Needs the hand-off from Step 10 (TODO, To the deliverer) |
| The writing and one-home rules | Run 3's `.claude/rules/` | |
| The reviewer's working rules | `CLAUDE.local.md`, the full-auto version | See "CLAUDE.local.md for run 4" |
| The delegation entry | Run 4's `.claude/decisions.md`, its first entry | See "The skills' sign-offs, on full auto" |
| What run 4 must check | RETRO D22's table | Each row at its step |

What the agent does not get:
- **Run 3's records, code and devlog.** Reading them, it would copy
  their length and density.
- **One exception:** a settled item cites the run 3 ADR that holds
  its full reason. The agent may read that ADR when it needs the
  reason. Nothing else from run 3.

## Settled: what run 4 does not reconsider

Each item is a decision run 3 took. Run 4 takes it as given and
writes it into its own records in its own words. "Run 3" names the
source, for the reviewer.

**Settled is a decision. Analysis is not settled.** Run 4 derives
the facts that can hurt and the kills again (run 3 found 24 facts
and 20 kills). Then they are compared with run 3's lists. Did run
4 find the same ways to break the promise?

### The problem

- **S1. The promise.** "For any item, the reserved quantity never
  exceeds the on-hand-count, however many reservations race for the
  same units." Run 3: intent.
- **S2. The audience.** A reader judging correctness-first
  construction. Callers and operators are the environment, not the
  audience. Run 3: intent.
- **S3. What done excludes.** No monitoring. No hosted deploy: the
  system and its evidence run on a clean machine by the README's
  commands. No rollback. Run 3: intent.
- **S4. Claims refused.** Each is refused as a second claim. Run 3:
  intent, "Rejected candidates".
  - A resent reserve is not recognised. It makes a second hold,
    until that hold expires. That cost is accepted.
  - A confirmed reservation is never lost: a trust in the store,
    not a claim.
  - Released stock returns once: a slice, not a claim.
  - Available stock is current: not a claim at all.
- **S5. What the ledger refuses to own.** Request identity, how
  long a hold lasts, which items exist, what a warehouse holds, who
  may act. Run 3: definition, L2.
- **S6. The name.** never-oversold. Run 3: ADR-0003.

### The slices

- **S7. Four slices, in this order.** Run 3: registry.
  - SL-1: no over-admission under contention.
  - SL-2: the correction never undercuts the holds.
  - SL-3: a reservation exits once.
  - SL-4: consume's two moves hold together.

  The adversity each must create is the registry's. Run 4 writes
  the registry itself and checks that its four match these.

### The ground and the stack

- **S8.** podman local containers, driven by compose. Run 3:
  ADR-0004.
- **S9.** PostgreSQL 17, one instance, and nothing else. Run 3:
  ADR-0005.
- **S10.** The store enforces the constraints. Two identities:
  `runtime` for the ledger and `migrator` for Flyway. Flyway runs
  as its own compose service, as `migrator`. The running ledger
  cannot change the schema. Run 3: ADR-0006.
- **S11.** Spring Boot 4, Java 21, Maven with the wrapper. Plain
  SQL through Spring's JDBC. No JPA, no schema generation. Run 3:
  ADR-0007.
- **S12.** Package by feature, package-private by default. Group
  `io.github.edgaras87`, base package
  `io.github.edgaras87.neveroversold`. Run 3: ADR-0007, ADR-0008.
- **S13.** The harness forks N ≥ 2 real ledger processes against a
  throwaway store (Testcontainers). It reads the witness by plain
  JDBC, outside every instance. Run 3: ADR-0009.
- **S13a. The harness's levers.** Run 3: SL-4, and the operator
  manual.
  - An instance is killed outright: its process is destroyed, not
    asked to stop.
  - The store is frozen by pausing its container.
  - A consume is held mid-work by a row lock that the test takes.
- **S13b. The structure tests.** ArchUnit rules on the compiled
  classes. JSqlParser reads the ledger's own statements. Together
  they check that the ledger holds no item state, reads no clock,
  and is the store's one writer. Run 3: SL-1, SL-3, ADR-0014.

### The door

- **S14. Paths and answers.** Run 3: ADR-0010.
  - Paths are resource-shaped: `POST /items/{item}/reservations`,
    `POST /items/{item}/adjustments`,
    `POST /reservations/{r}/consume`, `.../release`.
  - Answers: `201` for a new record, `200` for a transition, `400`
    invalid, `404` unknown, `409` refused.
  - Every non-success body is RFC 9457 Problem Details.
  - A response carries the record as stored, never an "available"
    number.
- **S15.** An item becomes known by its first adjustment. Run 3:
  ADR-0011.
- **S16.** An adjustment answers `200`, whether or not it created
  the item. Run 3: ADR-0012.
- **S17.** An exit repeated by the same exit answers `200`, as the
  first did. A different exit on an ended reservation answers
  `409`. Run 3: ADR-0013.
- **S18.** A lost store mid-request answers `503`, "outcome
  unknown". Run 3: ADR-0016.
- **S19.** Bounds: a quantity is 1 to 1,000,000. A hold is
  PT1S to P7D. Run 3: SL-1 G6.

### The walls

- **S20.** Whether a reservation is active is judged by one clock,
  the store's. The ledger reads no clock. Run 3: SL-1, FC3.
- **S21.** The reserve is one guarded update:
  `reserved + units <= on_hand_count` in its WHERE clause. A
  `CHECK reserved <= on_hand_count` stands behind it. Run 3: SL-1.
- **S22.** A correction that would leave the count under the holds
  is refused. It ends no hold. Run 3: SL-2.
- **S22a.** An adjustment states the new count. It is not a change
  by some amount, so a resent one lands the same. Run 3: SL-2 G4.
- **S22b.** Corrections carry no order. Each is judged alone,
  against the numbers it meets. Run 3: SL-2 G5.
- **S23.** An expired hold's units are free from its expiry
  instant. Nothing has to run to free them. Run 3: SL-3.
- **S23a.** "Tidy first": each reserve and adjust writes the
  receipts of the item's expired holds before it decides, and frees
  exactly what it wrote. Run 3: SL-3 G5.
- **S24.** One exit receipt per reservation, by its key. A trigger
  refuses a changed receipt or a mistimed one. The ledger's own
  statement moves the numbers, not the trigger. A check at commit
  holds the units held equal to the open reservations' units. Run
  3: SL-3, migrations V2 and V3.
- **S25.** No operator-side exit. Run 3: SL-3.
- **S26.** The store trusts one writer, the ledger. Build-time
  rules check that only the ledger class reaches the store. Run 3:
  ADR-0014.
- **S27.** An index enters with the statement that needs it on
  every decision. Run 3: ADR-0015.
- **S28.** Consume's two moves are one statement in one
  transaction, so nothing is ever left to converge. The store's
  default isolation and the item's row are enough. Run 3: SL-4 G1
  and G2.
- **S28a.** An interrupted consume is undone by the store when its
  session ends. No recovery job. Run 3: SL-4 G3.
- **S28b. Rejected, and kept rejected:** limiting how long others
  wait after an instance loses its network mid-consume. It is a
  known issue, not a guarantee. Run 3: SL-4, and TODO.

**If a settled item does not hold in run 4.** Example: a new
Spring Boot version changes how S18 can be done. The agent tries
the ways around it and takes the most acceptable one. See "When a
settled item does not hold".

**S1 is never departed from.** A test showing the promise broken
is a bug in a wall, to be fixed. It is never a reason to change the
promise.

## How run 4 runs on full auto

**The steps are run 3's:**
- setup;
- framing;
- ground;
- skeleton;
- SL-1 to SL-4;
- the retrospective;
- applying it;
- Release.

Identity (Step 2) shrinks to one line, because S6 settles the name.

**Each step keeps its gate.** The gate is written before the step's
work starts. The agent ticks an item only with its evidence: a
command and its output, or a file and line. A step closes when
every item is ticked, and then the next step opens. No stop for the
reviewer.

**The retrospective and its application run on auto too.** The
agent decides each retrospective decision itself. Each also goes in
the decision log, open for review. The skills `retrospective` and
`apply-retrospective` run them.

**Auto ends** when Release's gate closes. Release here is local:
the intent excludes a hosted deploy, so nothing leaves the machine.

**The self-check, at the last slice's close and again in Release:**
- `./mvnw test` is green.
- Each evidence test was seen red first. The red run is named in
  its slice record.
- A fresh clone in a temp directory runs the README's commands.
- Every link in the records resolves.
- Run 4's facts and kills, compared with run 3's: what matches,
  what is new, what is missing.

**What waits for the reviewer after auto ends:**
- reading the decision log;
- pushing;
- deleting the `-detail` and `try/` branches.

## Commits

These are the rules the latest commits followed here (Steps 9 and
10), used from run 4's first commit.

- **One branch per step,** cut from main.
- **Small commits on it, freely.** Conventional Commits, subject
  50 or under, body lines 72 or under.
- **Agent files apart from project files.** No commit touches both
  `.claude/` and the project.
- **At the step's close:**
  - the small commits stay on `<step>-detail`;
  - the step branch is regrouped into a few commits by kind;
  - the agent fast-forwards main to it;
  - it tags the close `run4/step-<n>`, so the reviewer can diff
    one step at a time later.
- **Never push.** Never delete a `-detail` or `try/` branch. Both
  wait for the reviewer.

## When something new comes up

**New means not in the settled list and not answered by a skill.**
Three kinds, decided by what a wrong answer would break:

| Kind | Test | What the agent does |
|---|---|---|
| Small | Reversible inside one file, invisible from outside, no wall or record depends on it | Picks one. One line in the log. No trial. |
| Real | Changes the door, the schema, a wall, the harness, or a dependency | Tries the options first, then decides. A log entry and an ADR. |
| Conflict | A settled item does not hold, or a gate item cannot be made true | Tries the ways around it, as a Real question with one more criterion first. See "When a settled item does not hold". |

*Example of Small:* the name of a test helper. *Of Real:* how
Release checks that a fresh clone runs the README's commands. Run 3
never ran Release, so this question is new. *Of Conflict:* the newest Spring Boot 4 version handles a
lost connection differently, and S18's `503` needs another way to
be caught.

### How a Real question is tried

1. **Write the question first.** The question, two or three
   options, and how they will be judged go in the log, committed,
   before any try. The criteria cannot be picked after the results
   are known.
2. **One branch per option:** `try/<question>-<option>`, cut from
   the step branch. Build only enough to judge: the smallest code,
   and the test that decides.
3. **Judge in this order.** A later criterion only breaks a tie on
   the earlier ones.
   1. The deciding test passes. It goes red when the option's
      protection is removed.
   2. The protection lives in the store rather than in the code.
   3. Fewer new moving parts. Then fewer lines.
   4. The record that explains it is shorter.
4. **Time box: one hour of work per option.** If no option wins
   clearly by then, take the one easiest to reverse, and mark it
   "close call".
5. **Merge the winner.** The other branches stay until the
   reviewer has read the entry.

*Say:* the question is how Release checks that a fresh clone runs
the README's commands.
- Option A: a script clones into a temp directory and runs the
  commands. It catches a missing step: it goes red with the
  `flyway migrate` line removed. No new moving part. 40 lines.
- Option B: a container builds from the repo and runs the
  commands. It goes red the same way. Two new moving parts, the
  image and its build file. 95 lines.
- Both pass criterion 1, and 2 does not apply. A wins on 3.

## The decision log

**One file, `docs/decision-log.md`.** The reviewer reads it after
auto ends. It is the index of every decision run 4 took alone, and
the home of the Small ones. A Real decision's full reasoning lives
in its ADR, and the log links to it.

One block per decision:

```
### L-07 · 2026-10-20 · Release · Real
Question: how a fresh clone is checked to run the README.
Options: A a script in a temp directory; B a container build.
Judged by: the order in "How a Real question is tried".
Results: A red without the migrate line, 0 new parts, 40 lines.
         B red without the migrate line, 2 new parts, 95 lines.
Chosen: A. Fewer moving parts.
Rejected: B, the image is a second thing that can break.
Branches: try/fresh-clone-script, try/fresh-clone-container
ADR: ADR-0017
Review: open
```

A Small entry is one line: `L-08 · Step 7 · Small · test helper
named Scene, not Fixture. Review: open`.

**Review** is `open` until the reviewer reads it. Then it becomes
`agreed` or `reversed`, with a line saying why. A reversed decision
is a lesson for the retrospective.

## When a settled item does not hold

Nothing stops auto. A Conflict is tried like a Real question, with
one change: a criterion goes before the others.

**The order for a Conflict:**
1. The promise holds. The evidence tests pass, and go red when
   the protection is removed.
2. **The option stays closest to the settled item.** What the
   outside sees changes least: the same paths, the same answers,
   the same records. An option that keeps the settled item exactly,
   by a different way inside, beats one that changes it.
3. Then the Real order: the store over the code, fewer moving
   parts, a shorter record.

**The options always include keeping the settled item** by the
smallest change that works. The log entry says which settled item
was departed from, how far, and why the closer options failed.

**A gate item that cannot be made true** after two tries is tried
the same way: options to make it true, against the option of
striking it. A struck item is marked `[-]` with its reason, as run
3 did with Step 9's.

**What is outside the repo.** The agent works only inside run 4's
directory, plus the containers it starts. If something needs more,
such as a system package or a machine setting, the options are the
ways around it inside the repo. One example: run 3's tests needed
podman's user socket. A way around is to ask the operator manual's
reader to turn it on, and to have the tests skip with a clear
message until it is on. If no option works, the item is logged
`blocked`, the step closes without it, and the run goes on.

**Never, even on full auto:** push, delete a branch, or change
anything outside run 4's directory. These wait for the reviewer.

## Fixing the method's files

The skills, rules and shapes are run 4's tools. When the work shows
one is wrong, or missing something the work needed, the agent fixes
it during the run.

**What may trigger a fix:** something that happened in run 4. A
step went wrong, or needed something the file did not say. Never a
guess about what might happen. Never a preference for other words.
This is the rule run 3 used (`delivered-copies.md`, rule 2).

**What may be fixed:**
- **A skill or a rule:** edited in place. A new one only when a
  missing one caused a real mistake.
- **A shape:** edited when the output was right and the shape was
  wrong. A new shape starts when a new kind of output appears
  (`shapes-lifecycle.md`).
- **A concept chapter:** only from a mistake lived in run 4, as in
  run 3.

**How each fix lands:**
1. **Its own commit,** agent paths only.
2. **A decision-log entry of kind Method:**
   - what happened;
   - what the file said;
   - what it says now;
   - whether text was replaced or added.

   Text is added only for a missing part. Otherwise the fix replaces
   the wrong text, so the files do not grow by habit.
3. **For a delivered copy, a line under TODO's "To the deliverer",**
   as in run 3.

**The trial of a fix** is the next step that uses the file. Its
result is written on the entry: "tried at Step 6: worked", or
"tried at Step 6: did not help, reverted in <commit>".

An idea that is not a fix goes into TODO.md under "For the retro".

## The skills' sign-offs, on full auto

The skills were written for a reviewer. They ask a human to
sign off at fixed points. On full auto, nobody answers, and run 4
would stop at its first framing step.

**Where the skills ask a human:**
- **cbc-framing:** every step's verdict. It already has a way out,
  "delegated-verdict mode", which needs a decision recorded in the
  run's `.claude/decisions.md`.
- **cbc-slice:** the readiness sign-off, the specification before
  Stage 2, and the plan before Stage 3.
- **cbc-bootstrap, infra-establish, infra-serve:** their stage
  sign-offs.
- **retrospective, apply-retrospective:** each decision and each
  triage row.
- **commit-plan:** a stop at every commit boundary.
- **visual-comparison:** the choice of form.

**The delegation entry,** run 4's first entry in
`.claude/decisions.md`:
- **What is delegated:** every verdict and sign-off any skill gives
  the human. That includes framing's delegated-verdict mode.
- **Why:** run 4 runs on full auto, to test whether the process
  holds without a reviewer.
- **The cost accepted:** the records and the decision log are the
  only review, so they must read once.
- **How a sign-off is taken:**
  - the agent writes what it would have shown the reviewer, where
    the skill's record scheme puts sign-offs;
  - it decides by `docs/run.md`;
  - it adds one line to the decision log, kind Verdict, linking to
    that place.
- **Not delegated:** push, deleting a branch, and anything outside
  run 4's directory.

## CLAUDE.local.md for run 4

Run 3's file says "stage it, show me the diff, and stop", and
"show one decision at a time". Brought along as it is, it would
stop run 4 at every commit. Run 4's version:

```markdown
# How I work with Claude (run 4, full auto)

## Commits
- Commit freely: small commits on each step's branch.
- At a step's close: keep the small commits on `<step>-detail`,
  regroup the step branch into a few commits by kind, agent files
  apart from project files, fast-forward main, and tag
  `run4/step-<n>`.
- Never push. Never delete a branch.

## Explaining
- Write so I can read it once, in chat and in records. How:
  `.claude/rules/writing.md`.

## Decisions
- Do not wait for me. Decide by `docs/run.md`, and log each
  decision in `docs/decision-log.md` with what was rejected and
  why. I read the log after the run.

## Manuals
- For a process you run (a pass, a workflow), keep two documents:
  your instructions, and a plain manual for me: what it is, how it
  works, how it decides, ideas not yet applied. Don't mix them.

## New kinds of work
When something neither run has done before comes up:
1. Find the ways it could be done.
2. Try them, as `docs/run.md` says, and choose one. Keep the
   others in the log with the reason.
3. Write a provisional manual for the chosen way, and a PLAN step
   with its gate.
4. While it runs, the manual changes as the work teaches.
5. At the close, the manual and what happened become a skill, a
   rule, or a section of a record. The manual stops being
   provisional.
```

## Limits on the records

- **A slice record stays under 250 lines.** Past that, the agent
  cuts it before the step closes.
- **Each fact has one home.** The registry, ARCHITECTURE and the
  code comments link to the slice record. They do not retell it.
- **A closed step in PLAN is one line,** with its date and its tag.

## Decided

Agreed by the reviewer on 2026-10-15:

1. **Full auto,** from the first commit through Release. Nothing
   stops it. A settled item that does not hold is tried, and the
   most acceptable way is taken.
2. **The line between Small and Real,** as drafted.
3. **The time box:** one hour per option.
4. **The record budget:** 250 lines per slice record.
5. **Before run 4 starts:** Step 10 closes (done 2026-10-15). The
   deliverer takes run 3's fixes into the bundle, creates run 4's
   repo (`~/IdeaProjects/cbc-pure-run-4`, a fresh `git init`, no
   remote), and starts the run.
6. **The briefing** is run 3's, found at
   `~/IdeaProjects/safe-reservation-briefing.md` and confirmed by the
   reviewer.
7. **The method's files are fixed during the run** when the work
   shows them wrong or missing something.
8. **Run 3's Release is skipped.** Run 4 does its own.

## The kickoff message

```
Build never-oversold from an empty repo, on full auto: from the
first commit through Release, with no stops.

Read first: the briefing, ~/IdeaProjects/safe-reservation-briefing.md
(framing commits it as docs/system/framing/briefing.md). Then
docs/settled.md, docs/run.md, and docs/concept/00-cbc.md.

Settled decisions (docs/settled.md) are not reconsidered. Write
them into the records in your own words. Derive everything else:
the facts that can hurt, the kills, the code, the tests.

A new question: classify it Small, Real or Conflict, and follow
docs/run.md. Try the options of a Real or Conflict question before
choosing. Log every decision in docs/decision-log.md.

When the work shows a skill, rule or shape wrong or missing
something, fix it as docs/run.md says, and log it.

Commits: one branch per step; small commits; agent files apart
from project files; regroup at the close, keep -detail, fast-forward
main, tag run4/step-<n>. Never push. Never delete a branch. Never
change anything outside this directory.

Auto ends when Release's gate closes.
```

`docs/run.md` is this file, cut to the rules: no reasons,
no "Decided" list.

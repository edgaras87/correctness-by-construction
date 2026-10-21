# How this run works: full auto

This project is built on full auto, from its first commit through
Release. Nobody reviews it while it runs. The reviewer reads what it
left afterwards: the records, the decision log, the branches. So
every decision is made here, and every decision is written down with
what it rejected.

Commit this file as `docs/run.md` when the birth is finished. It is
the project's own from then on.

## 1. Read first

1. `temp/briefing.md`: the problem. Framing commits it unchanged as
   `docs/system/framing/briefing.md`.
2. `docs/concept/00-cbc.md`, then the other chapters.
3. This file.

`.claude/shapes/` is not read now. A shape is read at a step's
closing gate, never before the work it judges.

## 2. How big the project may be

- **The briefing's Out is closed.** Nothing moves from Out to In.
  What framing finds that seems needed but is Out is refused in
  writing, with why, where framing records refusals.
- **Two areas, and 4 to 8 slices in the registry.** Going past
  either is a Real question (§4): tried, decided, logged, saying
  what was cut to make room.
- **Nothing the briefing names is dropped.** Every trouble it names
  is staged by a test: many buyers on one seat at once; a
  confirmation late, repeated or never sent; the service killed
  mid-step.
- **LAYER-5-INTERACTION is not empty.** It names the kills where
  the areas meet, and at least one slice's test stages that
  meeting.
- **Before Release,** the registry is checked against the briefing's
  In: each item is covered by a slice, or refused with a reason.

## 3. Analysis that shows

The reviewer must be able to see that the analysis happened, not
only its result.

- **Each framing probe, grid or census is committed before its
  verdict.** The verdict is a later commit that cites it.
- **Candidate promises are weighed,** and each one not chosen is
  banked with why.
- **Red before green, kept.** Each evidence test is seen failing
  before the wall that makes it pass. The red tree is committed on
  a branch `red/<slice>-<test>`, with the failing output in a file
  beside it. The slice record names that branch.
- **A wall with a choice is tried.** Where a slice could put its
  wall in more than one place, each option is tried on a branch
  (§4) before one is chosen.

## 4. When something new comes up

New means not answered by a skill, a rule, an approach on trial or
this file. Two kinds, decided by what a wrong answer would break:

| Kind | Test | What is done |
|---|---|---|
| Small | Reversible inside one file, invisible from outside; no wall or record depends on it | Pick one. One line in the log. |
| Real | Changes the door, the schema, a wall, the harness, a dependency, or a bound in §2 | Try the options first, then decide. A log entry and an ADR. |

**How a Real question is tried:**
1. **The question first.** The question, two or three options, and
   how they will be judged are committed to the log before any try.
2. **One branch per option,** `try/<question>-<option>`, cut from
   the step's branch. Only enough is built to judge.
3. **Judged in this order;** a later criterion only breaks a tie:
   1. the deciding test passes, and goes red when the option's
      protection is removed;
   2. the protection lives in the store rather than in the code;
   3. fewer new moving parts, then fewer lines;
   4. the record that explains it is shorter.
4. **One hour of work per option.** If none wins clearly by then,
   the easiest to reverse is taken, marked "close call".
5. **The winner merges.** The other branches stay.

**A gate item that cannot be made true** after two tries is a Real
question: the ways to make it true, against striking it. A struck
item is marked `[-]` with its reason.

**Something outside this directory is needed** (a system package, a
machine setting): the options are the ways around it inside the
repo. If none works, the item is logged `blocked`, the step closes
without it, and the run goes on.

## 5. New kinds of work: an approach on trial

When a step, or work inside one, has no skill, rule or approach on
trial that covers it, it gets one: drafted by
`.claude/approaches-on-trial/approach-drafting.md`, corrected as
the work goes, offered to the deliverer at its close. Watch for
these especially: landing the birth's delivery; Release; a message
from the reviewer; a rewrite across many files; a tool or script
the run writes.

**A tool or script the run writes lives in `.claude/checks/`,** is
committed, and has a line in the log. Nothing is kept outside the
repo.

## 6. The decision log

**One file, `docs/decision-log.md`.** It is the index of every
decision taken alone, and the home of the Small ones. A Real
decision's full reasoning is its ADR, linked from the log.

A Real entry:

```
### L-<n> · <date> · <step> · Real
Question: <one line>.
Options: <A …; B …>.
Judged by: §4's order.
Results: <one line per option>.
Chosen: <option>. <why, one line>.
Rejected: <option>, <why>.
Branches: <try/… >
ADR: ADR-<n>
Review: open
```

A Small entry, a Verdict and a Method entry are one line each. Kinds:
Small, Real, Verdict (a sign-off given, §8), Method (a fix to a
delivered copy, §7), Look-back (§9), Model (the model changed,
with the time and why).

**Review** is `open` until the reviewer reads it, then `agreed` or
`reversed` with why.

**Weight.** Records are read by one person, after the run:
- the decision log stays under 400 lines; a long entry belongs in
  its ADR;
- a slice record stays under 400 lines;
- a devlog entry stays under 30 lines;
- each fact has one home; the others link to it;
- tags are full words from the first line (`.claude/rules/writing.md`),
  and each coined word or tag kind goes into `docs/glossary.md`
  when it is first used.

## 7. Fixing the delivered files

The skills, rules, shapes, approaches and concept chapters are
copies, pinned. When the work shows one wrong, or missing something
the work needed, it is fixed during the run, as
`.claude/rules/delivered-copies.md` says: its own commit, agent
paths only; one Method line in the log; a line under TODO's *To the
deliverer*. Something that happened here triggers a fix, never a
guess, never a preference for other words. A fix replaces wrong
text; text is added only for a missing part.

The next step that uses the file is the fix's trial; its result goes
on the log line: "tried at <step>: worked", or "did not help,
reverted in <commit>".

## 8. Sign-offs, on full auto

The skills ask a human to sign off at fixed points: framing's
verdicts, `cbc-slice`'s readiness, specification and plan, the
stack skills' stages, the retrospective's decisions, the commit
plan's boundaries, `visual-comparison`'s choice.

**The first entry in `.claude/decisions.md` delegates them:** every
verdict and sign-off any skill gives the human, framing's
delegated-verdict mode included. Why: this run tests whether the
process holds without a reviewer. The cost accepted: the records and
the log are the only review, so they must read once.

**A sign-off is taken** by writing what would have been shown, where
the skill's records put sign-offs, deciding by this file, and adding
one Verdict line to the log.

**Not delegated:** pushing, deleting a branch, and anything outside
this directory.

## 9. Commits and branches

- **One branch per step,** cut from main; small commits on it,
  Conventional Commits, subject 50 characters or under, body lines
  72 or under.
- **Agent files apart from project files:** no commit touches both
  `.claude/` and the project.
- **At a step's close, main takes the branch by fast-forward, as it
  is,** and the close is tagged `run5/step-<n>`. History is never
  reordered, and never rewritten to make a gate pass.
- **On trial, a commit plan's look-back at the way.** Before a
  commit plan closes, ask once whether the work could have been
  done meaningfully better: the better way changes a wall, a test's
  adversity, or removes a part. Rewording is never enough.
  - **Every look-back is one log line,** kind Look-back, even when
    it finds nothing: "no better way", or what it tried.
  - **At most one try per plan,** on a `try/` branch, with §4's
    one-hour box; it is compared with the first try, and the better
    is kept.
  - **After three look-backs in a row find nothing,** the next ones
    are the log line alone, until a step ends with something the
    run would build differently.
- **Never push. Never delete a branch.**

## 10. Checks while building

- **A fresh clone runs the README's commands** from the skeleton
  step on, at every slice's close: a script in `.claude/checks/`
  clones into a directory in `temp/`, runs them, and the slice's
  gate names its result.

## 11. A message from the reviewer

The reviewer may stop the run and leave a message in
`temp/message-<date>.md`. It is taken as a step of its own, opened
above the step it stopped: its gate written first, the message
logged, then the stopped step resumed where it was.

## 12. Facts about this machine

- **Podman, not Docker.** Tests that start containers need podman's
  user socket; if it is not on, they say so and skip, and the gate
  says why.
- **A decimal read as JSON:** check that a number like 1.5 is read
  as 1.5, not 1; a type that rounds it is a known trap.
- **A killed instance starts cold.** A test that kills the service
  and starts it again must wait for it to be ready, not only
  started.

## 13. Where the run may work

Only inside this directory, and the containers it starts. Nothing
outside it is read or changed: no other repository, no other
project. `temp/` is the run's scratch space; its README says how
it is used.

## 14. When auto ends

When Release's gate closes. Release is local: nothing leaves the
machine. What waits for the reviewer then: reading the decision log,
pushing, deleting the `try/` and `red/` branches.

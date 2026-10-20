# Approach drafting

**On trial.** How work never done before gets its approach: drafted
for that work, corrected as the work goes, and handed over at its
close. The same in a run and at the deliverer, apart from the close.

An approach is how a piece of work is done. On trial, it is not yet
proven: a guess the work tests. It lives in
`.claude/approaches-on-trial/`, one file per kind of work.

## What it is for

So that the first time a kind of work is done, the way it was done
is kept as it worked, not as it was guessed. A skill or a manual
written before the work describes a guess. An approach starts as
one too, but the work corrects it before anything is made of it.

## When it opens

When a step opens, or a work item inside one, or a small TODO item
comes due, and no skill, rule or approach on trial covers the work.
A step's opening items ask this.

First ask: **is it new, or a gap in a skill, rule or approach this
project holds?** A gap is an edit to that file, and this approach
stops here. In a run, how a delivered copy is edited is
`.claude/rules/delivered-copies.md`'s.

## Stages

### 1. Open

1. **The reviewer says what the work should do or be.**
2. **Find the ways it could be done,** and recommend one. The
   reviewer chooses. Keep the others, each with the reason.
3. **Write the approach** at
   `.claude/approaches-on-trial/<work>.md`, `<work>` the kind of work
   in a word or two. The name starts with `approach-` only when its
   subject is approaches. It holds:
   - what the work is for;
   - its stages, in order;
   - what is not known yet;
   - the ways rejected, with their reasons;
   - its uses, empty until the close.

   Write it for this work, in its own terms. Nothing is made general
   yet: what is general shows only once the work is done.
4. **If the work is a step,** what its Notes and gate take from
   the approach is `PLAN.md`'s step form's.

### 2. Work

- **When the work shows the approach wrong, change the approach
  first,** then go on. It always says what is being done now, not
  what was planned.
- **Each change is a commit of its own.** Its body says what the
  work taught, and names the commit where the work showed it. The
  approach is an agent file and the work a project file, so the two
  never share a commit (`commit-messages`).

### 3. Close

1. **Write this use's note** under the approach's uses, dated: what
   the work did, what it taught, what is still not known.
2. **Hand it over for evaluation.**
   - **At the deliverer:** open `approach-evaluation`.
   - **In a run:** one line under TODO's *To the deliverer* offers
     it, with its path and the commits that hold its history, so the
     deliverer reads how it grew. Example: "approach on trial,
     offered for evaluation: `.claude/approaches-on-trial/retro.md`,
     its history at `a1b2c3d`..`e4f5a6b`". The approach stays where
     it is, and this project uses it again until a delivery says
     otherwise.

## When the approach fails

Drop it, and the devlog says why, as a dead end. What was tried
stays in the history. Then ask the reviewer whether to start again
from another way.

## Not known yet

- **Whether "stages from earlier work" retires.** A step's opening
  item still accepts them as a way. They are an approach nobody
  wrote down. Once approaches on trial exist, repeated work may be
  better written as one.
- **What catches a work item outside a step.** A step's opening
  items ask whether its approach is known. A small TODO item has no
  such item, and no skill description catches it any more.
- **Whether the form holds:** what for, stages, not known, ways
  rejected, uses.

## Settled when

A run and the deliverer have each drafted an approach with it, and
the evaluations of both changed nothing in it.

## Uses

*Run 3, Steps 9 and 10, 2026-10-16.* Before this was written down:
the retrospective and its apply step had no skill. The reviewer
asked for a written draft, changed as the work went, with the skill
built at the close. Both skills came out that way and were taken
here. Taught: start from a draft, not a skill.

*The deliverer, working a reading, 2026-10-01.* A draft in `temp/`
ran three readings, then became a rule. Taught: a draft can become
a rule, not only a skill.

*The deliverer, the redesign, 2026-10-19.* Drafted as a manual on
trial in `docs/conventions/`. It closed in three pieces: its work
to the refinement's file, two ideas to TODO, its way of judging a
fix to the refinement. The manual was dropped. Taught: the close
places pieces; it does not make one form.

*The deliverer, the refinement, from 2026-10-18.* Drafted as a
manual on trial in `docs/conventions/`, and then counted as a
manual before anyone judged whether it is one. Taught: a draft is
not a manual, and needs a home of its own. This approach came from
that lesson. The refinement is open.

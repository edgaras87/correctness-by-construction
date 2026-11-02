# Approach drafting

**On trial.** How work never done before gets its Approach on Trial: drafted
for that work, corrected as the work goes, and handed over at its
close. The same in a CBC Run and at the Concept Deliverer, apart from the close.

A Work Approach is how a piece of work is done. On trial, it is an Approach on Trial, not yet
proven: a guess the work tests. It lives in
`.claude/approaches-on-trial/`, one file per kind of work.

## What it is for

So that the first time a kind of work is done, the way it was done
is kept as it worked, not as it was guessed. An Agent Skill written before the work
describes a guess, as a manual does at the Concept Deliverer. An Approach on Trial starts as
one too, but the work corrects it before anything is made of it.

## When it opens

When a Plan Step opens, or a work item inside one, or a small TODO item
comes due, and no Agent Skill, Agent Rule or Approach on Trial covers the work.
A Plan Step's opening items ask this.

First ask: **is it new, or a gap in an Agent Skill, Agent Rule or Approach on Trial this
project holds?** A gap is an edit to that file, and this Approach on Trial
stops here. In a CBC Run, how a delivered copy is edited is
`.claude/rules/delivered-copies.md`'s.

## Stages

Each phase below is one Approach on Trial Stage, numbered, under
its own heading.

### 1. Open

1. **The reviewer says what the work should do or be.**
2. **Find the ways it could be done,** and recommend one. The
   reviewer chooses. Keep the others, each with the reason.
3. **Write the Approach on Trial** at
   `.claude/approaches-on-trial/<work>.md`, `<work>` the kind of work
   in a word or two. The name starts with `approach-` only when its
   subject is Approaches on Trial. It holds:
   - what the work is for;
   - its Approach on Trial Stages, in order;
   - what is not known yet;
   - the ways rejected, with their reasons;
   - its uses, empty until the close.

   Write it for this work, in its own terms. Nothing is made general
   yet: what is general shows only once the work is done.
4. **If the work is a Plan Step,** what its Notes and Plan Step Gate take from
   the Approach on Trial is the Plan Step Form's (`PLAN.md`, *The Plan Step Form*).

### 2. Work

- **When the work shows the Approach on Trial wrong, change it
  first,** then go on. It always says what is being done now, not
  what was planned.
- **Each change is a commit of its own.** Its body says what the
  work taught, and names the commit where the work showed it. The
  Approach on Trial is an agent file and the work a project file, so the two
  never share a commit
  (`.claude/skills/commit-messages/SKILL.md`, *The agent's own files*).

### 3. Close

1. **Write this use's note** under the Approach on Trial's *Uses*, dated: what
   the work did, what it taught, what is still not known.
2. **Hand it over for evaluation.**
   - **At the Concept Deliverer:** open the approach-evaluation Approach on Trial.
   - **In a CBC Run:** one line under TODO's *To the deliverer* offers
     it, with its path and the commits that hold its history, so the
     Concept Deliverer reads how it grew. Example: "Approach on Trial,
     offered for evaluation: `.claude/approaches-on-trial/retro.md`,
     its history at `a1b2c3d`..`e4f5a6b`". The Approach on Trial stays where
     it is, and this project uses it again until a delivery says
     otherwise.

## When the Approach on Trial fails

Drop it, and the devlog says why, as a dead end. What was tried
stays in the history. Then ask the reviewer whether to start again
from another way.

## Not known yet

- **Whether "stages from earlier work" retires.** A Plan Step's opening
  item still accepts them as a way. They are a Work Approach nobody
  wrote down. Once Approaches on Trial exist, repeated work may be
  better written as one.
- **What catches a work item outside a Plan Step.** A Plan Step's opening
  items ask whether its Work Approach is known. A small TODO item has no
  such item, and no Agent Skill description catches it any more.
- **Whether the form holds:** *What it is for*, *Stages*, *Not known yet*, *Ways
  rejected*, *Uses*.

## Settled when

A CBC Run and the Concept Deliverer have each drafted an Approach on Trial with it, and
the evaluations of both changed nothing in it.

## Uses

*CBC Run 3, Steps 9 and 10, 2026-10-16.* Before this was written down:
the retrospective and its apply step had no Agent Skill. The reviewer
asked for a written draft, changed as the work went, with the Agent Skill
built at the close. Both Agent Skills came out that way and were taken
into the Concept Deliverer. Taught: start from a draft, not an Agent Skill.

*The Concept Deliverer, working a CBC Run Reading, 2026-10-01.* A draft in the Concept Deliverer's `temp/`
ran three CBC Run Readings, then became an Agent Rule. Taught: a draft can become
an Agent Rule, not only an Agent Skill.

*The Concept Deliverer, the redesign of the conventions manual, 2026-10-19.* Drafted as a manual on
trial in the Concept Deliverer's `docs/conventions/`. It closed in three pieces:
- its work, to the refinement's file;
- two ideas, to TODO;
- its way of judging a fix, to the refinement.

The refinement is the Concept Deliverer's fixing of its own text against its rules. The manual was dropped. Taught: the close
places pieces; it does not make one form.

*The Concept Deliverer, the refinement, from 2026-10-18.* Drafted as a
manual on trial in the Concept Deliverer's `docs/conventions/`, and then counted as a
manual before anyone judged whether it is one. Taught: a draft is
not a manual, and needs a home of its own. This Approach on Trial came from
that lesson. The refinement closed on 2026-11-02, after three
Refinement Rounds and a last read whose 385 findings were all ended.

*The Concept Deliverer, placing into an Idea Model, 2026-10-28.* The first step
from a convention to an Idea Model, done for two of the Concept
Deliverer's texts, the Tiers Model and the Exchange Convention: the Concept Deliverer's `.claude/approaches-on-trial/model-placing.md`, written
before the work and corrected once by it, in its own commit
(the Concept Deliverer's `4fedbb3`). Taught: the work's first sort, shown before anything
was written, is where the draft first met the work.

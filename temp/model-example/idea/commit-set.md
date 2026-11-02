# A commit set

<!-- Layer: the idea. Bound to no project
     (temp/model-example/layers.md). -->

## The problem

Work bigger than one commit, done in one go, is hard to review and
hard to undo. A plan made up front and followed to the letter breaks
when the work meets what nobody foresaw.

## The idea

Plan work bigger than one commit as an ordered set of commits, review
at each boundary, and let the plan change as the work teaches.

## How it works

1. **Plan.** Each commit in the set gets a line: what it changes, and
   why it comes where it does.
2. **Agree the plan** before the first commit.
3. **Work one commit at a time.** Before each, check it against its
   line.
4. **When the work shows the plan wrong, change the plan first,** then
   go on. The plan always says what is being done now.
5. **Look back at the close:** the plan as first agreed against the
   commits that landed. What moved, and why.
6. **Close.** The plan goes; what it taught is kept.

## Why

- Each commit is small enough to review, and to undo alone.
- The plan steers, and the work corrects it. What is done follows
  what the work met, not theory alone.
- What moved is the lesson: kept, it improves the next plan.

**Ways rejected:**

- **One large commit:** nothing between start and end can be reviewed
  or undone alone.
- **A plan held fixed:** the work is bent to fit the plan, or the plan
  stops saying what is true.

## Limits

- **Work of one or two commits:** the plan costs more than it gives.
- **Work whose shape is unknown:** try it first, throw the try away,
  then plan.
- **A plan that changes at every commit** was not a plan: stop and
  plan again.

## Needs

1. **Commit messages in one stable form,** so each plan line can be
   matched to the commit that landed it.
2. **Each plan line written once** while the set runs, and named
   elsewhere, never restated, so the plan and the work cannot
   disagree.
3. **A place for what the look-back found,** kept after the plan goes.

## What each project decides

1. How big work must be before it needs a set.
2. Where the plan lives while the set runs.
3. Who agrees the plan, and who agrees each commit.
4. Whether commits run without stopping once the plan is agreed.
5. Where the look-back's findings are kept.

## Changes

- 2026-11-02: drafted.

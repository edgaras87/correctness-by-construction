# Auto run

**On trial.** How the deliverer prepares a run that works on full
auto, from its birth to its Release, and births it. Drafted for run
5 by `.claude/approaches-on-trial/approach-drafting.md`.

## What it is for

So that a run can go from birth to Release with no stop for the
reviewer, and still leave behind what a reviewed run would: every
decision with what it rejected, its copies edited where the work
showed them wrong, and an approach on trial for each kind of work
it met with no way written down. The reviewer reads all of it after
auto ends.

Done once before, inside run 3, which wrote the hand-off that
started run 4 (`temp/RUN-4.md`). Never on our seat.

## Stages

1. **Read the last full-auto run, lightly.** Its hand-off, its
   decisions log and its `RETRO.md`: how full auto went, and what
   it skipped, deferred or did by hand for want of a way. Each
   finding says keep, change or add, for this run. This is not
   the run's reading (`exchange-read`), which harvests its lessons;
   the cost, that those lessons do not reach this run, is said to
   the reviewer.
2. **The intent is the reviewer's.** The agent may draft it when
   the reviewer asks, and the reviewer's version is what goes. The
   agent checks it against the concept: the layers it must reach,
   and whether its size fits a run. It is written as the method's
   briefing, which framing commits unchanged, so it brings the
   problem and leaves the promise open.
3. **Settle what TODO says is due before a birth.**
4. **Write the hand-off,** in this repo's `temp/`, from stage 1's
   findings. It says what full auto means for this run:
   - it decides everything, and logs each decision with what it
     rejected;
   - what is settled before it starts, if anything;
   - how its copies are edited: the shipped
     `delivered-copies.md` rule;
   - work with no way written down gets an approach on trial,
     drafted by the shipped `approach-drafting`;
   - how far it may grow or shrink: the briefing's Out is closed,
     and what framing finds there is refused in writing; a bound on
     areas and slices, past which is a Real question; every trouble
     the briefing names staged by a test;
   - how a skill's sign-off is given on full auto;
   - its commits and branches; never a push;
   - when auto ends, and what waits for the reviewer then;
   - its `CLAUDE.local.md`.
5. **Main takes the step's branch,** so the pin is a commit main
   holds.
6. **Birth by `delivery/installs/pure-seed.md`,** from a clean
   tree. The intent and the hand-off go into the newborn's `temp/`.
   The reviewer starts the run with the hand-back line only: the
   run composes its own opening.

## Not known yet

- **Whether the newborn reads a hand-off in `temp/`.** Nothing
  forces a newborn to read what it was given (ADR-0018, Variant B);
  the first commit on its main is the only evidence.
- **What in the hand-off is general.** Parts every full-auto run
  needs may belong in the container, as a rule or a stance, rather
  than retold in each hand-off. What is general shows only once
  this run is done.
- **How the reviewer checks a run while it runs,** without
  stopping it.
- **Whether the light read is enough,** or a run should not be born
  on full auto before the last one has been read in full.

## Ways rejected

- **Autonomy built into the container now,** a shipped rule that
  makes any run full-auto. Rejected for now: one full-auto run has
  been lived, and a shipped rule would decide for every run what
  one has shown. Stage 4's parts are its candidates.
- **No hand-off: the intent and `CLAUDE.local.md` alone,** relying
  on the shipped skills. Rejected: run 4's hand-off settled how
  sign-offs, new work and copies go on full auto, and the skills
  alone ask the reviewer at each sign-off.

## Uses

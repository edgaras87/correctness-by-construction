# Auto run

**On trial.** How the Concept Deliverer prepares a CBC Run that works on full
auto, from its birth to its Release, and births it. Drafted for CBC Run
5 by `.claude/approaches-on-trial/approach-drafting.md`.

## What it is for

So that a CBC Run can go from birth to Release with no stop for the
reviewer, and still leave behind what a reviewed CBC Run would: every
decision with what it rejected, its copies edited where the work
showed them wrong, and an Approach on Trial for each kind of work
it met with no way written down. The reviewer reads all of it after
auto ends.

Done once before, inside CBC Run 3, which wrote the Run Hand-off that
started CBC Run 4 (`temp/RUN-4.md`). Never on our Convention Seat.

## Stages

1. **Read the last full-auto CBC Run, lightly.** Its Run Hand-off, its
   Decisions Log and its `RETRO.md`: how full auto went, and what
   it skipped, deferred or did by hand for want of a way. Each
   finding says keep, change or add, for this CBC Run. This is not
   the CBC Run's Run Reading (`exchange-read`), which harvests its lessons;
   the cost, that those lessons do not reach this CBC Run, is said to
   the reviewer.
2. **The intent is the reviewer's.** The agent may draft it when
   the reviewer asks, and the reviewer's version is what goes. The
   agent checks it against the concept: the System Layers it must reach,
   and whether its size fits a CBC Run. It is written as the Run
   Briefing, which framing commits unchanged, so it brings the
   problem and leaves the promise open.
3. **Settle what TODO says is due before a birth.**
4. **Write the Run Hand-off,** in this repo's `temp/`, from stage 1's
   findings. It says what full auto means for this CBC Run:
   - it decides everything, and logs each decision with what it
     rejected;
   - what is settled before it starts, if anything;
   - how its copies are edited: the shipped
     `delivered-copies.md` rule;
   - work with no way written down gets an Approach on Trial,
     drafted by the shipped `approach-drafting`;
   - how far it may grow or shrink: the Run Briefing's Out is closed,
     and what framing finds there is refused in writing; a bound on
     areas and slices, past which is a Real question; every trouble
     the Run Briefing names staged by a test;
   - how a skill's sign-off is given on full auto;
   - its commits and branches; never a push;
   - when auto ends, and what waits for the reviewer then;
   - its `CLAUDE.local.md`.
5. **Main takes the Plan Step's branch,** so the Delivery Pin is a commit main
   holds.
6. **Birth by `delivery/installs/pure-seed.md`,** from a clean
   tree. The intent and the Run Hand-off go into the Newborn Run's `temp/`.
   The reviewer starts the CBC Run with the Pure Seed's own prompt, its
   review lines replaced by full auto, so the birth stays
   comparable with every other; nothing else is composed for it.

## Not known yet

- **What in the Run Hand-off is general.** Parts every full-auto CBC Run
  needs may belong in the Container Group, as an Agent Rule or a stance, rather
  than retold in each Run Hand-off. What is general shows only once
  this CBC Run is done.
- **How the reviewer checks a CBC Run while it runs,** without
  stopping it.
- **How a CBC Run is kept from reading what it should not.** A `Read`
  deny rule stops `cat` and `sed` on a path, but not `grep -r` or a
  script (`docs/conventions/agent-arrangement/` §5.4, *Permission rules*); for CBC Run 5 the
  other repositories were made unreadable on disk, and the
  Concept Deliverer's stayed readable, on trust.
- **Whether the light read is enough,** or a CBC Run should not be born
  on full auto before the last one has been read in full.
- **Whether a record budget holds as a number alone.** CBC Run 5's
  Decisions Log ended at 723 lines against the 400 the Run Hand-off set;
  a check at each Plan Step's close may be what a budget needs.
- **What a machine power-off does to a full-auto CBC Run.** The stop
  hook cannot see it, and nothing watched CBC Run 5 while it ran.

## Ways rejected

- **Autonomy built into the Container Group now,** a shipped Agent Rule that
  makes any CBC Run full-auto. Rejected for now: one full-auto CBC Run has
  been lived, and a shipped Agent Rule would decide for every CBC Run what
  one has shown. Stage 4's parts are its candidates.
- **No Run Hand-off: the intent and `CLAUDE.local.md` alone,** relying
  on the shipped skills. Rejected: CBC Run 4's Run Hand-off settled how
  sign-offs, new work and copies go on full auto, and the skills
  alone ask the reviewer at each sign-off.

## Uses

*The deliverer, run 5's birth, 2026-10-21 to 2026-10-22.* Prepared
and born in one evening, 19 commits: three readers on run 4 at the
default effort, all three paid; the briefing drafted on the
reviewer's ask and decided line by line; two items due before a
birth settled (ADR-0061, `cd69ed7`); a hand-off of five files; the
birth from main at `ae8a041`, started on Fable 5.1 with the seed's
prompt. Run 5 ran from 00:54 to 04:54 and from 08:28 to 08:45,
through Release: 13 steps, 6 slices, 254 commits, 11 `red/` and 13
`try/` branches, no remote, no push, the model unchanged. Taught:
- **the newborn reads its hand-off:** within 13 minutes it drafted
  an approach on trial for the birth, delegated every sign-off and
  adopted `run.md` as `docs/run.md`; by Release it had drafted four
  approaches of its own and noted its use of `approach-drafting`;
- **the machine stopped it, not the agent:** a power-off at 04:54
  cost 3 hours 31 minutes and a restart; the run picked up on one
  question from the reviewer, and dated its last two steps a day
  ahead after it;
- **a budget without a check does not hold:** the decision log
  ended at 723 lines, 102 entries open, against 400;
- **the intent is drafted on the reviewer's ask,** and the hand-off
  bounds how far the run may grow or shrink: both corrected in the
  approach as the work went (`2019be2`).
Not known still: what in the hand-off is general; how the reviewer
checks a running run; whether the light read cost run 5 anything,
which its reading will say.

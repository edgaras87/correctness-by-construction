# Auto run

**On trial.** How the Concept Deliverer prepares a CBC Run that works on full
auto, from its CBC Run Birth to its Release, and runs its CBC Run Birth. Drafted for CBC Run
5 by `.claude/approaches-on-trial/approach-drafting.md`.

## What it is for

So that a CBC Run can go from birth to Release with no stop for the
reviewer, and still leave behind what a reviewed CBC Run would: every
decision with what it rejected, its copies edited where the work
showed them wrong, and an Approach on Trial for each kind of work
it met with no way written down. The reviewer reads all of it after
auto ends.

Done once before, inside CBC Run 3, which wrote the CBC Run Hand-off that
started CBC Run 4 (in git at `4ef580f6^:temp/RUN-4.md`). Never on our Convention Seat.

## Stages

1. **Read the last full-auto CBC Run, lightly.** Its CBC Run Hand-off, its
   Decisions Log and its `RETRO.md`: how full auto went, and what
   it skipped, deferred or did by hand for want of a way. Each
   finding says keep, change or add, for this CBC Run. This is not
   a CBC Run Reading of it (the exchange-read Agent Skill), which harvests its
   lessons. Those lessons do not reach this CBC Run. The reviewer is
   told that cost.
2. **The intent is the reviewer's.** The agent may draft it when
   the reviewer asks, and the reviewer's version is what goes. The
   agent checks it against the concept: the System Layers it must reach,
   and whether its size fits a CBC Run. It is written as the CBC Run
   Briefing, which CBC Framing commits unchanged, so it brings the
   problem and leaves the Falsifiable Promise open.
3. **Settle what TODO says is due before a CBC Run Birth.**
4. **Write the CBC Run Hand-off,** in this repo's `temp/`, from Stage 1's
   findings. It says what full auto means for this CBC Run:
   - it decides everything, and logs each decision with what it
     rejected;
   - what is settled before it starts, if anything;
   - how its copies are edited: the shipped
     delivered-copies Agent Rule;
   - work with no way written down gets an Approach on Trial,
     drafted by the shipped approach-drafting Approach on Trial;
   - how far it may grow or shrink:
     - the CBC Run Briefing's Out, what the system will not do, is
       closed, and what CBC Framing finds there is refused in writing;
     - a bound on Responsibility Areas and Invariant Slices, past which is a question the CBC Run must not decide alone;
     - every trouble the CBC Run Briefing names is created by a test;
   - how an Agent Skill's sign-off is given on full auto;
   - its commits and branches; never a push;
   - when auto ends, and what waits for the reviewer then;
   - its `CLAUDE.local.md`.
5. **Main takes the Plan Step's branch,** so the Delivery Pin is a commit main
   holds.
6. **CBC Run Birth by `delivery/installs/pure-seed.md`,** from a clean
   tree. The intent and the CBC Run Hand-off go into the Newborn CBC Run's `temp/`.
   The reviewer starts the CBC Run with the Pure Seed's own prompt, its
   review lines replaced by full auto. So the CBC Run Birth stays comparable
   with every other. Nothing else is composed for it.

## Not known yet

- **What in the CBC Run Hand-off is general.** Parts every full-auto CBC Run
  needs may belong in the Container Group, as an Agent Rule or a stance, rather
  than retold in each CBC Run Hand-off. What is general shows only once
  this CBC Run is done.
- **How the reviewer checks a CBC Run while it runs,** without
  stopping it.
- **How a CBC Run is kept from reading what it should not.** A `Read`
  deny rule stops `cat` and `sed` on a path, but not `grep -r` or a
  script (`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md` §4, *Permission rules*). For CBC Run 5, the
  other repositories were made unreadable on disk. The Concept
  Deliverer's stayed readable, on trust.
- **Whether the light read is enough,** or a CBC Run should not be born
  on full auto before the last one has been read in full.
- **Whether a record budget holds as a number alone.** CBC Run 5's
  Decisions Log ended at 723 lines against the 400 the CBC Run Hand-off set.
  A check at each Plan Step's close may be what a budget needs.
- **What a machine power-off does to a full-auto CBC Run.** The stop
  hook cannot see it, and nothing watched CBC Run 5 while it ran.

## Ways rejected

- **Autonomy built into the Container Group now,** a shipped Agent Rule that
  makes any CBC Run full-auto. Rejected for now, when it was drafted on 2026-10-21: one full-auto
  CBC Run had been lived, and a shipped Agent Rule would decide for
  every CBC Run what one had shown. Stage 4's parts are its candidates.
- **No CBC Run Hand-off: the intent and `CLAUDE.local.md` alone,** relying
  on the shipped Agent Skills. Rejected: CBC Run 4's CBC Run Hand-off settled how
  sign-offs, new work and copies go on full auto, and the Agent Skills
  alone ask the reviewer at each sign-off.

## Uses

*The Concept Deliverer, CBC Run 5's CBC Run Birth, 2026-10-21 to 2026-10-22.*
Prepared and born in one evening, 19 commits:
- three readers on CBC Run 4 at the default effort, all three paid;
- the CBC Run Briefing drafted on the reviewer's ask and decided
  line by line;
- two items due before a CBC Run Birth settled (`cd69ed7`);
- a CBC Run Hand-off of five files;
- the CBC Run Birth from main at `ae8a041`, started on Fable 5.1 with the
  Pure Seed's prompt.

CBC Run 5 ran from 00:54 to 04:54 and from 08:28 to 08:45, through
Release: 13 Plan Steps, 6 Invariant Slices, 254 commits, 11 `red/`
and 13 `try/` branches, no remote, no push, the model unchanged.
Taught:
- **the Newborn CBC Run reads its CBC Run Hand-off:** within 13
  minutes it drafted an Approach on Trial for its CBC Run Birth, delegated
  every sign-off and adopted `run.md` as `docs/run.md`; by Release it
  had drafted four Approaches on Trial of its own and noted its use
  of the approach-drafting Approach on Trial;
- **the machine stopped it, not the agent:** a power-off at 04:54
  cost 3 hours 31 minutes and a restart; the CBC Run picked up on one
  question from the reviewer, and dated its last two Plan Steps a day
  ahead after it;
- **a budget without a check does not hold:** the Decisions Log
  ended at 723 lines, 102 entries open, against 400;
- **the intent is drafted on the reviewer's ask,** and the CBC Run
  Hand-off bounds how far the CBC Run may grow or shrink: both
  corrected in the Approach on Trial as the work went (`2019be2`).

Not known still: the first two items of *Not known yet*, and whether
the light read cost CBC Run 5 anything, which its CBC Run Reading
will say.

*The Concept Deliverer, CBC Run 6's CBC Run Birth, 2026-10-29; noted
2026-11-19, at its Plan Step's close.* Prepared and born in one day,
7 commits (`56875c9`..`798327d`):
- Stage 1 a light read: CBC Run 5's CBC Run Reading already held
  its lessons, each marked keep, change or add for CBC Run 6;
- the CBC Run Briefing the reviewer's, `checkout`, larger than CBC
  Run 5's: three Responsibility Areas, 6 to 12 Invariant Slices;
- the playbook's one line meant for CBC Run 5 alone removed
  (`7f6e3a8`);
- the CBC Run Birth from main at `657d372`, by the Pure Seed, its
  own checks passing, and started by the reviewer;
- twelve entries in `~/IdeaProjects` made unreadable first, since a
  `Read` deny rule does not stop `grep -r` or a script.

CBC Run 6 ran through Release and closed a Step 15 after it: 7
Invariant Slices, 233 commits on main and 254 across its branches,
tag `v0.1.0`. What it taught is in its CBC Run Reading,
`temp/reading-run-6-2026-11-26.md`, judged with CBC Runs 4 and 5 (ADR-0089).

Not known still: as for CBC Run 5, and whether a larger CBC Run
Briefing holds on full auto.

---

## Decisions

- ADR-0061 — *Uses*, CBC Run 5's CBC Run Birth: the two items due before a
  CBC Run Birth

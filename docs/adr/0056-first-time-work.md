# 0056. First-time work starts from a provisional manual

Date: 2026-10-16
Status: Accepted (2026-10-16, at the set's records commit; opened
Proposed under the commit plan for first-time work). Decision 6
amended 2026-10-17 by ADR-0057: ours opens at a step too.

## Context

Some work neither seat has done before, so no skill covers it. Both
seats have met it, and both handled it the same way:

- **Run 3, Steps 9 and 10.** Its retrospective and its apply step
  had no skill. The agent first proposed writing the skill before
  the work. The reviewer asked instead for a provisional manual,
  changed as the work went, with the skill built at the close. Both
  skills came out that way (its `RETRO.md`, D23, D24, D25), and
  ADR-0054 took them.
- **Here, working a reading.** A draft, `temp/working-a-reading.md`,
  ran three readings of run 3, then became a rule
  (`.claude/decisions.md`, 2026-10-01).

Run 3 wrote the way down only in the reviewer's private file, under
"New kinds of work" (its D25). Nothing a run or this repo ships
says it. `agent-arrangement` §3.1 still calls a project's own skill
"not yet defined … open until a project has written one". Run 3
has written two skills and two rules of its own.

The next case is planned: `exchange-birth`, to be written while
running the next birth (TODO).

## Options considered

- **A section in `agent-arrangement` §3.1.** Rejected: a manual is
  read by a maintainer, not by an agent at the moment work starts.
- **Only a line in the playbook's step form.** Rejected: it reaches
  a run's steps, never this repo's work, and holds no procedure.
- **A rule loaded every session.** Rejected: it is paid for in every
  session, and its moment is the start and the close of rare work.
- **Only the reviewer's private file,** as run 3 has it. Rejected:
  the file is not tracked, so a run cannot be born with it, and the
  agent's seat never sees it.
- **The provisional manual in `temp/`,** as our one case had it.
  Rejected for both seats. In a run, `temp/` is not shipped (TODO)
  and is the delivery's staging place. Here, a manual has a home
  already, and the *on trial* mark (`docs/conventions/conventions/`)
  says what "provisional" needs to say.
- **A skill description matched to phrases,** such as "we have
  never done this", the first draft. Rejected on the reviewer's
  word: it misses how the reviewer speaks, and fires when something
  else is meant. A fixed moment, asked by the step form, does not.
- **Taking a run's offer written into our reading tools,** or into
  our own `first-time-work` skill. Rejected on the reviewer's word:
  either ties two skills together, so a change to one is a change
  to both. The run marks its offer instead.

## Decision

1. **First-time work is a convention of its own,** the twelfth:
   `docs/conventions/first-time-work/`.
2. **The work starts from a provisional manual,** which the work
   corrects as it goes. At the close the manual becomes its lasting
   form: a skill, a rule, a shape, a step of the playbook, a section
   of a record, or nothing, when nothing in it is worth keeping.
3. **Where the provisional manual sits depends on the seat.** In a
   run: `.claude/<name>/manual.md`, beside where the lasting form
   will go; at the close it becomes that form, and the manual goes.
   Here: where manuals live, in `docs/conventions/` or a concept
   chapter, marked on trial.
4. **Two questions come first, because they send the work
   elsewhere.** Is it really new, or a gap in an existing skill?
   Then it is an edit to that copy (`delivered-copies.md`, rule 2).
   Is it general, or only this project's? Then it stays the
   project's own (rule 3).
5. **The other cases are the convention's:** born in a run and read
   and fitted to the bundle by us; born here, its first use in a run
   its trial; born here and used only here, our next use its trial;
   a lasting form that is not a skill, or none; the way failing, a
   dead end in the devlog. A run offers its first-time work marked
   as such, a new convention to consider, with its manual's history.
   A reading takes it by `docs/conventions/conventions/` §4, as
   ADR-0053 and ADR-0054 did, and our reading tools do not change.
6. **Each seat holds a skill,** `first-time-work`. A run's ships in
   the container, and opens when a step or a piece of work opens
   with no skill or earlier run to say how. Ours is our own
   derivation from the manual (ADR-0042), since its manual goes
   elsewhere, and opens when a reading's work item, or a TODO item
   come due, opens with nothing to say how. Each manual change is a
   commit of its own, and the close looks back at that history.
   *Amended 2026-10-17 by ADR-0057: ours opens when a step, a work
   item inside one, or a small TODO item comes due with nothing to
   say how; a step's opening items ask it, as a run's do.*
7. **Every step's opening items ask whether its way is known:** its
   skill, or stages its Notes list from earlier runs. If neither,
   the step opens a provisional manual.
8. **The trials name their closes.** Our seat: `exchange-birth`'s
   close. The run's seat: run 5's first step whose way is not
   known; if it has none, run 5's reading says so, and the trial
   carries on.

## Consequences

- `ARCHITECTURE.md` counts twelve manuals; the container holds six
  skills.
- `agent-arrangement` §3.1 points at the convention for how a
  project's own skill comes to be.
- The convention joins the index's chain: it starts from an idea
  and hands its work to `commit-plan`.
- Run 3's private section "New kinds of work" can point at the
  skill; that is the reading's W7.

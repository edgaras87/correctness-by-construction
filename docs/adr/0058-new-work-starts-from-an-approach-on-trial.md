# 0058. New work starts from an approach on trial

Date: 2026-10-20
Status: Accepted (2026-10-20, at the set's records commit; opened
Proposed under the commit plan for approaches, inside the
refinement's round 1). Supersedes ADR-0056 decisions 1, 2, 3, 5 and
6, and ADR-0057 decision 5; amends ADR-0056 decision 7, as ADR-0057
carried it into our step form.

## Context

ADR-0056 made first-time work a convention. Work neither seat had
done started from a provisional manual, and its close made one
lasting form. Our seat wrote that manual where manuals live,
marked on trial. The convention came from one lived case, run 3's
Steps 9 and 10, and was written the way a convention is written.

Our seat has used it twice since, and both uses showed it wrong:

- **The redesign of 2026-10-19** closed as three pieces, not one
  form: its work to the refinement's file, two ideas to TODO, its
  way of judging a fix to refinement §2.3. Its manual was dropped.
- **The refinement** wrote its manual in `docs/conventions/`. Round
  1 then had to ask whether it counts as a thirteenth manual
  (DECISION-4), before anyone had judged whether it is a convention.

Round 1's DECISION-1 found the cause. "Manual" meant two things: a
convention's description, which `ARCHITECTURE.md` defines, and a
draft of work not yet done, which nothing defines. Its two
sentences could be fixed. The design behind them could not.

The reviewer's model, settled in discussion on 2026-10-20: work
never done starts from a written guess, specific to that work. The
work corrects it. At the close it is evaluated, and its pieces go
where they belong, into a new convention or an existing one. A
piece not yet proven is rewritten in general and tried again, each
use noted, until it is placed or dropped. A run drafts the same
way; we evaluate its result.

Five round 1 findings sat in first-time-work's own text: FINDING-2,
25, 26, 27 and 35.

## Options considered

- **Name the exception in two sentences** (DECISION-1's first
  option). Rejected: the draft stays a manual, which is the cause.
- **Polish the first-time-work manual.** Rejected: it locks a new
  guess in the same place, the mistake being fixed.
- **The names "draft", "way", "candidate", "practice",
  `on-trial-work-approaches/`.** Rejected: "draft" is wrong after
  the first use; "way" reads as nothing alone; "candidate" says it
  is headed for a convention; "practice" names the stack practice;
  the last puts the group second.
- **An `approach-` prefix on every file.** Rejected: the folder
  groups them already, and wiring runs on paths and `foundation`
  lines, not on names. The prefix stays only where the subject is
  approaches.
- **The approach in `temp/`.** Rejected: `temp/` empties a draft
  once it has served, and an approach on trial outlives the work
  that made it.
- **A home per seat, or a folder outside `.claude/`.** Rejected: the
  same in both seats was the reviewer's ask, and an approach is how
  the agent works, like a skill or a rule.
- **Drafting and evaluating as one approach.** Rejected: it would
  ship the evaluation to runs, which never use it.
- **One file per seat for a shared approach.** Rejected: two sources
  with nothing above them drift, and nothing can check them.
- **Shipping later, at the next birth.** Rejected on the reviewer's
  word.
- **A fixed count of uses before placing.** Rejected: a guess. Each
  approach names what would settle it.
- **Taking in a design change written into every step form.**
  Rejected: the evidence is the refinement's alone. It went into
  refinement §2.7 instead (`8c9aadf`).

## Decision

1. **Work never done before starts from an approach on trial:** one
   file, `.claude/approaches-on-trial/<work>.md`, the same in both
   seats, named for the work it covers. "Approach" is how a piece of
   work is done; "on trial", that it is not yet proven. A file's name
   starts with `approach-` only when its subject is approaches.
   "Manual" keeps one meaning: a convention's description.
2. **An approach on trial lives in stages.** It is drafted during
   its first use, specific to that work, and corrected as the work
   goes, each change a commit saying what taught it. At the close it
   gets a note of that use and is evaluated. Each piece is placed
   into a convention, new or existing; kept on trial and rewritten in
   general; left as the project's own; or dropped. Each later use
   adds a dated note and is evaluated again. A piece is placed when
   it meets what its approach named would settle it.
3. **The evaluation is ours, in both seats.** Ours at the work's
   close; a run's at a reading, from the offer line under its *To the
   deliverer*. One evaluation serves three situations: the first, of
   a draft; after each later use; and the placing that locks it.
4. **An approach splits by seat only when a whole part is used by
   one seat alone.** A step that differs is marked inline in a shared
   approach. Each idea lives in the part that acts on it. Our part
   points at the shared one by its path; the shared one says the
   deliverer holds a part that does not ship.
5. **The first-time-work convention becomes two approaches on
   trial.** `approach-drafting`, both seats, shipped: how an approach
   is drafted and handed over. `approach-evaluation`, ours: how one
   is judged and placed, with the stages and the split by seat. The
   manual and both skills go. "First-time work" stays the plain name
   for work never done before.
6. **A step finds its approach in order:** the skills and rules it
   uses; then an approach on trial that covers the work; if neither,
   it drafts one by `approach-drafting`. A step that uses an approach
   on trial names its own close as that use's trial, and its gate
   asks for the use's note and the evaluation. "Stages from earlier
   work" stays for now. Whether it retires is a question for
   `approach-drafting`'s first evaluation.
7. **Approaches on trial ship as pinned copies.** A run's note of a
   use is an edit to its copy, read back at a reading.
8. **The refinement's manual becomes its approach on trial,**
   `.claude/approaches-on-trial/refinement.md`, moved as it is.
9. **Each approach is first judged at its first evaluation.** The two
   evaluate themselves, so the reviewer's reading is the check, and
   both say so.

## Consequences

- `ARCHITECTURE.md` counts eleven manuals, and *The words* defines
  "approach" and "approach on trial".
- The container holds five skills and one approach on trial.
- `docs/conventions/agent-arrangement/` §3.8 is the place
  `approaches-on-trial/`; conventions §4 says a convention now comes
  from an evaluation.
- The index's chain loses first-time-work.
- Round 1's DECISION-1 and DECISION-4 end, with FINDING-2, 25, 26,
  27, 49 and 50.

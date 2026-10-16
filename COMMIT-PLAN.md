# Commit plan: first-time work

## Summary — the state after all commits

A twelfth convention, `docs/conventions/first-time-work/`, says how
work neither seat has done before is started and kept. It starts
from a provisional manual, the work corrects the manual, and at the
close the manual becomes its lasting form: a skill, a rule, a shape,
a step, a section of a record, or nothing.

Each seat holds a `first-time-work` skill. A run's sits in the
container, and puts its provisional manual at
`.claude/<name>/manual.md`. Ours is derived from the same manual,
and puts it where manuals live here, marked on trial. The manual
names seven cases, and the skill first asks the two that send work
elsewhere: is it really new, and is it general.

The playbook's step form sends a step with no skill, doing new work,
to the skill. `agent-arrangement` §3.1 stops calling a project's own
skill undefined and points at the convention. ADR-0056 records the
decision and what was rejected. W11 of the reading of run 3 is done.

## Commits

D8 is marked settled, and W11 added, in the reading's commit before
this plan.

**1. `docs(agent): add commit plan for first-time work`**
The approved plan.

**2. `docs(adr): 0056, first-time work`**
Proposed. The decision, the seven cases, where the provisional
manual sits in each seat, and the rejected options: a section in
`agent-arrangement`, the step-form line alone, a rule loaded every
session, the reviewer's file alone.

**3. `docs: a first-time-work convention, and its skill`**
As `docs/conventions/conventions/` §4 asks, in one commit, as the
retrospective's was (`fa7fd41`): the manual, in the form; the
container's skill; the container decisions stub's birth entry;
`ARCHITECTURE.md`'s counts, what the manuals cover, and which
convention owns the new file; `agent-arrangement` §3.1 pointing at
it; the index's chain, since it hands to `commit-plan`.

**3b. `docs: first-time-work fires when a step opens`**
Inserted after 3, on the reviewer's word. The skill's description
matched phrases ("we have never done this"), which miss how the
reviewer speaks and can fire when something else is meant. It now
names a moment: a step or piece of work opens, and no skill or
earlier run says how to do it. Dropping the manual at the close is
widened from "the work will not come again" to "nothing in it is
worth keeping". The skill and the manual both.

**4. `docs: the step form asks for the step's way`**
A third opening item in the playbook's step form: the step's way is
known, by its skill or by stages from earlier runs, or the step
opened a provisional manual. Asked at every step's opening, so the
form fires the skill, not the reviewer's words. Playbook stays v8:
no run has been born from v8.

**5. `chore(agent): our own first-time-work skill`**
Our derivation from the manual (ADR-0042), with its entry in
`.claude/decisions.md`. Agent files only, apart from 3. This repo
has no playbook steps, so its moment is a reading's W item, or a
TODO item come due, opening with no skill or earlier work to say
how.

**5b. `docs: a run marks its first-time work as offered`**
Inserted after 5, on the reviewer's word. The container skill's
offer line under *To the deliverer* named only a path. It now says
the file is first-time work offered as a new convention, and names
the commits holding the manual's history, so a reading sees what it
is and how it grew. The exchange and our reading tools stay as they
are: a reading takes it as it took run 3's rules and retrospective
skills (ADR-0053, ADR-0054), by `docs/conventions/conventions/` §4.

**6. `docs: records carry first-time work`**
ADR-0056 Accepted. TODO's `exchange-birth` item names it this
skill's first trial on our seat.

**7. `docs(agent): close commit plan for first-time work`**
Deletes this file; the body says what diverged.

After the close, the reading marks W11 done:
`docs(temp): the reading closes W11`.

## Decisions taken inside this plan

- **The name, `first-time-work`,** for the convention and the skill:
  it says neither seat has done this before. `new-work` matched every
  slice; `untried` already names a copy edited but never run.
- **The manual, the shipped skill and the counts in one commit,** as
  `fa7fd41` did. Reverting it removes the convention whole.
- **Our skill is our own derivation, not a copy,** because its
  manual goes somewhere else. Two commits, as two seats hold it.
- **On the index's chain.** It starts from an idea and hands its
  work to `commit-plan`, so it acts in sequence
  (`docs/conventions/conventions/` §4, step 4).
- **The trials, each naming its close.** Our seat: `exchange-birth`'s
  close. The run's seat: the first run 5 step with no skill; if run
  5 has none, run 5's reading says so and the trial carries on.
- **W7 is not touched here.** Run 3's `CLAUDE.local.md` section
  "New kinds of work" can point at the skill once it ships; that is
  W7's, with the rest of the reviewer's file.

# First-time work

**Work neither seat has done before starts from a provisional
manual. The work corrects the manual as it goes, and at the close
the manual becomes its lasting form: a skill, a rule, a shape, a
step, a section of a record, or nothing.**

## What it is for

So that the first time a kind of work is done, the way it was done
is kept, and kept as it worked, not as it was guessed. The failure
it avoids is a skill written before the work: it describes a guess.

Lived three times:

- **Run 3, never-oversold, Step 9.** Its retrospective had no skill.
  The skill was written at the close, from what had happened (its
  `RETRO.md`, D23).
- **Run 3, Step 10.** Applying the retrospective had no skill
  either. The agent first proposed writing the skill before doing
  the step. The reviewer asked instead for a provisional manual,
  changed as the work went, with the skill built at the close (D24,
  D25). Both skills were taken here (ADR-0054).
- **Here, working a reading.** A draft ran three readings of run 3,
  then became a rule (`.claude/decisions.md`, 2026-10-01).

Run 3 wrote the way down only in the reviewer's private file, where
a run cannot be born with it and the agent's seat never sees it.
Taken on 2026-10-16 (ADR-0056). *On trial for both seats: see the
seats.*

## What this is made usable as

- **`delivery/container/.claude/skills/first-time-work/SKILL.md` —
  the skill, shipped**, held at `.claude/skills/first-time-work/`
  and opened when a step or a piece of work opens and no skill, and
  no earlier step or run, says how to do it.
- **The step form's opening item, shipped** with the playbook,
  `delivery/fills/cbc-run-pure-playbook.md`: every step asks whether
  its way is known, and a step whose way is not opens the skill.
- **The same opening item in `PLAN.md`'s step form, the
  deliverer's** (ADR-0057), asked when a step opens here.
- **`.claude/skills/first-time-work/SKILL.md` — the deliverer's**,
  derived from this page, opened when a step opens, or a work item
  inside one, or a small TODO item comes due, with nothing to say
  how to do it.

This page explains; the skills state. What derives from this page
is that list. A change here walks it; a change forced in one of
them is checked back against this page.

## The seats

The way is the same in both seats. Three things differ: where the
provisional manual sits, what the close makes, and who judges it
after.

### The run's seat

- **The manual sits at `.claude/<name>/manual.md`,** beside where
  its lasting form will go. At the close it becomes that form, in
  its place under `.claude/`, and the manual goes. The why goes into
  the run's decisions log.
- **What the close makes is the run's own.** If it is general, the
  run offers it under *To the deliverer*, as first-time work, a new
  convention to consider, with the commits that hold its manual's
  history. If it is only this project's, it stays.
- **The deliverer judges it after,** at a reading: the deliverer's
  seat, its second job.

### The deliverer's seat

Two jobs, and only the first has a skill.

**Our own first-time work.**

- **The manual sits where manuals live:** `docs/conventions/<name>/`
  or a concept chapter, marked *on trial*
  (`docs/conventions/conventions/` §1). It is not drafted elsewhere
  first. The mark is what makes it provisional.
- **Our skill opens** at the same moments as a run's: a step
  opening, a work item inside one, or a small TODO item coming due,
  with nothing to say how to do it. A step's opening items in our
  `PLAN.md` ask it, as a run's do.
- **What the close makes is written for this repo first,** then
  derived for the container if a run needs it.
- **A run judges it after,** when one first uses it. That run's
  reading is the trial's close. Work only this repo does, such as a
  birth, has no run to judge it: our own next use is the trial.

**A run's first-time work, offered to us.**

- **No skill does this, on purpose.** A skill for it, or a step in
  our reading tools, would tie them to this convention, so a change
  to one would be a change to both (ADR-0056).
- **The run's offer line says what it is:** first-time work, a new
  convention to consider, with the commits that hold its manual's
  history. A reading reads that line as it reads every ask
  (`docs/conventions/exchange/` §6.2).
- **Taking it is adding a convention,** by
  `docs/conventions/conventions/` §4. We read what was written and
  how it grew, how it fits the bundle, and what must be cleaned of
  the run before it ships: names, tags, paths, the run's domain.
  Then we write the manual here, and decide whether this repo holds
  a copy too. ADR-0053 and ADR-0054 are worked examples.

## 1. Is it first-time work?

Two questions come first, because each sends the work elsewhere.

- **Is it new, or a gap in a skill we hold?** A gap is an edit to
  that copy, under `delivered-copies.md` rule 2. Run 3's small steps
  inside a planned commit went this way: an edit to `commit-plan`,
  not a new convention.
- **Is it general, or only this project's?** Only this project's,
  it still starts from a manual, but its lasting form stays with the
  project (`delivered-copies.md` rule 3), and nothing is offered.

## 2. The provisional manual

- **The reviewer says what the work should do or be.** The agent
  finds the ways it could be done and recommends one. The reviewer
  chooses, and the others are kept with the reason.
- **The manual is written before the work starts:** what the work
  is for, its stages in order, and what is not known yet. For a
  step, the stages are the ones its Notes list (the playbook's step
  form).
- **The work corrects it.** When the work shows the manual wrong,
  the manual changes first, then the work goes on. The manual is
  always what is being done now, not what was planned.
- **Each change is a commit of its own,** saying what taught it.
  At the close, that history is the look back: how the manual grew,
  one lesson at a time. In a run the manual is an agent file and the
  work a project file, so they never share a commit.

## 3. The close

The manual, and what happened, become one lasting form:

| Form | When | Example |
|---|---|---|
| A skill | a procedure in stages, bound to a moment | run 3's `retrospective` |
| A rule | true at a path, or in every session | `working-a-reading.md` |
| A shape | the form of one kind of output | run 3's kill shape |
| A step | a moment in every run of a playbook | the retrospective step |
| A section of a record | a fact, not a procedure | |
| Nothing | nothing in it is worth keeping: the work will not come again, or what it taught lives elsewhere | |

The reviewer chooses. The manual stops being provisional: in a run,
it goes; here, its *on trial* mark is rewritten from what was seen.

## 4. When the way fails

The manual is dropped, and the devlog says why, as a dead end. What
was tried stays in the history.

*Lesson, 2026-10-16: the deliverer's one case drafted its manual in
`temp/`, apart from where rules live. Here a manual has a home and
an on-trial mark, so nothing is drafted apart from it.*

## Why it arrives this way

A skill, because the way is a procedure bound to two moments: work
opening with nothing to say how to do it, and that work's close. The
first moment is asked, not left to be noticed: in both seats,
every step's opening items ask whether its way is known. A description
matched to phrases would miss how the reviewer speaks, and fire when
something else is meant. *Changed 2026-10-16, before the skill
shipped, on the reviewer's word.*

A rule loaded in every session would pay for rare work every time.
A manual alone reaches a maintainer, not the agent at the moment.
The step form's item is there because, in either seat, a step is
where such work starts.

## What this does not cover

- **How an edit to a delivered copy is made and handed back** —
  `docs/conventions/exchange/` §5.
- **How the deliverer reads a file a run wrote** —
  `docs/conventions/exchange/` §6.2.
- **Where a skill, a rule or a shape is placed** —
  `docs/conventions/agent-arrangement/` §3.
- **How a manual is written, and what *on trial* means** —
  `docs/conventions/conventions/`.
- **How the work's commits are planned** —
  `docs/conventions/commit-plan/`.

## Where to look

- The decision: ADR-0056.
- Run 3's record: its `RETRO.md`, D23 to D25.

<!-- The CbC run playbook. At birth, everything from the step form
     down replaces the steps in a newborn's PLAN.md; this comment
     and the version line stay here. Checked against concept v1
     (ADR-0003, ADR-0005). Harvest lands here, the one copy
     (ADR-0007). Its history — the parent it replaced (ADR-0016),
     the runs its steps were harvested from (ADR-0009, ADR-0011),
     and each version's change and reason — is in the devlog and in
     this file's git log. -->

# Playbook: CbC run — pure

Playbook version: v8 (2026-10-16, provisional; run 3's
retrospective taken, ADR-0055)

## The step form

<!-- Copied into a step when it opens, and filled in. Copied, never
     shared: each step ticks its own items, so one checkbox cannot
     serve six steps. -->

```markdown
## Step <n>: <title>  (<the skill it runs, if any>)    [ ]

Goal: <one sentence: what is true when this step is done>
Now: <where the step stands, one line>
Gate:
<the opening items below, filled in>
<this step's own items, asked of the goal>
<the closing items below, filled in>
Notes: <opened <date>; its stages, if it runs no skill; what the
 reviewer signs and when; what the step takes from the steps before
 it>
```

**The Now line names the stage the step is in, and changes when
the step enters a new one, not at every commit.** A step that runs
a skill uses the skill's stages. A step with no skill splits its
work into a few stages when it opens, and lists them in its Notes.
Two examples:

- the order service's first slice, which runs `cbc-slice`: "Now:
  Stage 2, the plan. Specification signed 2026-11-01."
- Step 2, which runs no skill, its Notes listing name, description
  and remote: "Now: the description. Name chosen 2026-11-03."

Inside a commit plan, the plan and the branch's log show where the
work is.

**The gate is written when the step opens, before any of its
work.** A gate written at the close describes what happened. It
does not set a standard the work was held to.

**At the opening.** Cheap now, impossible later: a branch not cut
cannot be cut afterwards.

- [ ] The step's branch `<branch>` is cut from main, and the step
      has not been worked anywhere else.
- [ ] This gate was written before the work started.

**The step's own items.** Ask of the goal: "how would I check that's
true?" Each answer is one item: a fact, checkable by looking, what
and not how. Together they equal the goal. For the order service's
goal "a retried order never makes a second order", one item is
"three submissions with key k-42 leave one order, and all three get
its answer". "The build stage done" is not an item. The named skill
sets the order of work, and its stages are not copied into the
gate. An item is ticked when it comes true, whenever that is.

**At the close.**

- [ ] What the step produced is read against each shape in
      `.claude/shapes/` that governs it, and every difference is
      settled. Where none governs, one line says so.
- [ ] Every link and path in the records resolves; every ADR,
      slice and kill a record cites exists; each pair of copies
      agrees, such as the version in the build file and in
      CHANGELOG.
- [ ] No living line in a record the step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `<branch>` follows commit-messages.
- [ ] No commit straddles agent and project paths.
- [ ] No implementation file is older than the decision it
      realizes: the log reads decision, then code.
- [ ] The step reached main by fast-forward from `<branch>`, on the
      reviewer's word.

The records item asks for an outcome. A run may write a script
that checks it and run it at every close. How a difference with a
shape is settled is `.claude/rules/shapes-lifecycle.md`'s.

**When every item is ticked and committed,** the next commit
replaces the gate with one line: the date, what the step
delivered, and the commit that holds the ticked gate. Example:
"Closed 2026-11-02: SLICE-1 closed, a retried order makes one
order; ticked gate at `a1b2c3d`."

**A trial names the close that judges it.** A piece of the way of
working put on trial says at which step's close it is judged. Its
verdict there is one line: kept, changed or dropped.

**A default that does not fit a step** is struck there, with its
reason. That is a finding about the default, not a step cutting a
corner.

## Step 0: Bootstrap                                [~]

Goal: the container exists — repo, records, arrangement — before content.
Now:
Gate:
Notes:

## Step 1: Framing  (cbc-framing)                   [ ]

<!-- CbC: this step opens on the briefing — its starting input,
     the first prompt of project work. The README purpose
     paragraph and the devlog's briefing line land here; names
     given before it are working names. -->

Goal: know what we're building and why, before code.
Now:
Gate:
Notes:

## Step 2: Identity (name, description, remote)     [ ]

Goal: the project's public identity decided, not defaulted.
Now:
Gate:
Notes:

## Step 3: Ground / infrastructure  (infra-establish)    [ ]

Goal: services stood up, constrained to need, verified both ways.
Now:
Gate:
Notes:

## Step 4: Skeleton & bootstrap  (cbc-bootstrap)    [ ]

Goal: an empty but buildable, testable, runnable system wired to the
real ground, with the evidence harness proven on one adversity.
Now:
Gate:
Notes:

## Steps 5..N-3: Invariant slices  (cbc-slice, one step per slice)

Goal: each registry slice closed by evidence that creates its
adversity; ordering re-decided at each close, never assumed from
the original expectation.
Now:
Gate:
Notes:

## Step N-2: Retrospective  (retrospective)    [ ]

Goal: every lesson the next run should act on is a decision in
RETRO.md, with an example from this run and the place it lands;
this run's hand-off lists point to those decisions; and what only
the next run can check is listed, each with the step that judges it.
Now:
Gate:
Notes: opens when the slice steps close, before Release, so it runs
even if Release is skipped. What the reviewer decides is the
skill's.

## Step N-1: Apply the retrospective  (apply-retrospective)    [ ]

Goal: this run hands over what its retrospective showed could be
better, where that changes how its records read and not what it
proved; RETRO.md says what happened to each decision.
Now:
Gate:
Notes: opens when RETRO.md closes. What the reviewer decides is the
skill's.

## Step N: Release                                  [ ]

Goal: the system handed to its audience — the promise shipped,
observable, and reversible wherever it deploys.
Now:
Gate:
Known already:
- a CHANGELOG entry for the release;
- README true for a stranger, its commands verified on a clean
  machine;
- known issues filed in TODO.md;
- Release's own lessons added to RETRO.md, as decisions in the
  `retrospective` skill's form.

Checked here, each unless this run's own recorded exclusion:
- monitoring and alerts in place;
- deploy and rollback documented and tried once.

Notes: opens when the apply step closes.

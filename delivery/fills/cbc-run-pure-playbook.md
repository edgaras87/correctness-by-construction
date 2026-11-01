<!-- The CBC Run playbook. At birth, everything from the Plan Step Form
     down replaces the Plan Steps in a Newborn CBC Run's PLAN.md
     (delivery/installs/pure-seed.md step 4). This comment and the
     version line stay here. Checked against concept v1
     (ADR-0003, ADR-0005).
     The Record Harvest lands here, the one copy (ADR-0007). Each
     lesson lands as one of three: a changed Plan Step Gate, a new
     Plan Step, or a line under a Plan Step's Known already. CBC
     Framing's and Release's lessons go in this playbook's own copies
     of those Plan Steps. Each lesson taken bumps the version line.
     Its history is in the devlog and in this file's git log: the
     parent it replaced (ADR-0016), the CBC Runs its Plan Steps were
     harvested from (ADR-0009, ADR-0011), and each version's change
     and reason. -->

# Playbook: CBC Run — pure

Playbook version: v11 (2026-10-30, provisional; since v10, written
in Glossary Names)

## The Plan Step Form

<!-- Copied into a Plan Step when it opens, and filled in. Copied, never
     shared: each Plan Step ticks its own items, so one checkbox cannot
     serve every Plan Step.
     foundation: the project-recording convention -->

```markdown
## Step <n>: <title>  (<the Agent Skill or Approach on Trial it runs, if any>)    [ ]

Goal: <one sentence: what is true when this Plan Step is done>
Now: <where the Plan Step stands, one line>
Gate:
<the opening items below, filled in>
<this Plan Step's own items, asked of the goal>
<the closing items below, filled in>
Notes: <opened <date>; its stages, if it runs no Agent Skill; what the
 reviewer signs and when; what the Plan Step takes from the Plan Steps before
 it; the ADRs and devlog entries behind it>
```

**The Now line names the stage the Plan Step is in, and changes when
it enters a new one, not at every commit.** A Plan Step that runs
an Agent Skill uses its Agent Skill Stages, and one that runs an
Approach on Trial uses its Approach on Trial Stages. A Plan Step with
neither splits its work into a few stages when it opens, and lists
them in its Notes.
Two examples:

- the order service's first Invariant Slice, which runs `cbc-slice`: "Now:
  Stage 2, the plan. Specification signed 2026-11-01."
- Step 2, which runs no Agent Skill, its Notes listing name, description
  and remote: "Now: the description. Name chosen 2026-11-03."

Inside a commit plan, the plan and the branch's log show where the
work is.

**The Plan Step Gate is written when the Plan Step opens, before any
of its work.** A Plan Step Gate written at the close describes what happened. It
does not set a standard the work was held to.

**At the opening.** Cheap now, impossible later: a branch not cut
cannot be cut afterwards.

- [ ] The Plan Step's branch `<branch>` is cut from main, and the Plan Step
      has not been worked anywhere else.
- [ ] This Plan Step Gate was written before the work started.
- [ ] The Plan Step's Work Approach is known: the Agent Skill it runs; an Approach
      on Trial in `.claude/approaches-on-trial/` that covers the
      work; or the stages its Notes list from earlier CBC Runs. If none,
      the Plan Step drafted one
      (`.claude/approaches-on-trial/approach-drafting.md`).

**The Plan Step's own items.** Ask of the goal: "how would I check that's
true?" Each answer is one item: a fact, checkable by looking, what
and not how. Together they equal the goal. For the order service's
goal "a retried order never makes a second order", one item is
"three submissions with key k-42 leave one order, and all three get
its answer". "The build stage done" is not an item. The named Agent Skill
sets the order of work, and its Agent Skill Stages are not copied
into the Plan Step Gate. An item is ticked when it comes true, whenever that is.

**Lists written ahead.** These Plan Steps were copied from a
playbook, the one PLAN's "Steps from:" comment names. Items the
playbook already knows a Plan Step needs, whatever its goal, are
listed under the Plan Step's Known already. They join its own items
when the Plan Step Gate is written. Questions for one CBC Run alone
come in its CBC Run Hand-off, never here.

**At the close.**

- [ ] What the Plan Step produced is read against each Output Shape in
      `.claude/shapes/` that governs it, and every difference is
      settled. Where none governs, one line says so.
- [ ] Every link and path in the records resolves; every ADR,
      Invariant Slice and Enemy Collision Kill a record cites exists; each pair of copies
      agrees, such as the version in the build file and in
      CHANGELOG.
- [ ] No living line in a record the Plan Step touched, or one that
      mentions its subject, still says "now", "today" or "not yet"
      about something the Plan Step changed.
- [ ] New and changed text reads to `.claude/rules/writing.md`.
- [ ] Every commit on `<branch>` follows the commit-messages Agent Skill.
- [ ] No commit straddles agent and project paths.
- [ ] No implementation file is older than the decision it
      realizes: the log reads decision, then code.
- [ ] The Plan Step reached main by fast-forward from `<branch>`, on the
      reviewer's word.
- [ ] Each Approach on Trial the Plan Step drafted or used has this
      use's dated note, and was handed over for evaluation
      (`.claude/approaches-on-trial/approach-drafting.md`, its close).

The records item asks for an outcome. A CBC Run may write a script
that checks it and run it at every close. How a difference with an Output Shape is settled is the shapes-lifecycle Agent Rule's
(`.claude/rules/shapes-lifecycle.md` §3, *A difference at the close*).

**When every item is ticked and committed,** the next commit
replaces the Plan Step Gate with one line: the date, what the Plan
Step delivered, what diverged from the plan, and the commit that
holds the ticked Plan Step Gate. Example:
"Closed 2026-11-02: SLICE-1 closed, a retried order makes one
order; the key's expiry moved to SLICE-2; ticked Plan Step Gate at
`a1b2c3d`."

**A Plan Step can stop when another must come first.** It stays in
the plan, marked `[!]`: "stopped: <the Plan Step that comes first>",
naming the devlog entry that says why. Its Now line
keeps the stage it stopped at. Main takes its branch so far by
fast-forward, on the reviewer's word, and the next Plan Step is cut
from main. To resume, its branch is fast-forwarded to main, and it
restarts at that stage. Any stage whose input the other Plan Step
changed runs again. A ticked item stays ticked unless the other
Plan Step made it untrue.

**A trial names the close that judges it.** A piece of the way of
working put on trial says at which Plan Step's close it is judged. Its
verdict there is one line: kept, changed or dropped.

**A default that does not fit a Plan Step** is struck there, with its
reason. That is a finding about the default, not a Plan Step cutting a
corner.

## Step 0: Bootstrap                                [~]

Goal: the container exists before content: the repo, the records
and the agent's arrangement.
Now:
Gate:
Notes:

## Step 1: CBC Framing  (cbc-framing)               [ ]

<!-- CBC: this Plan Step opens on the CBC Run Briefing. It is the
     Plan Step's starting input, the first prompt of project work,
     committed unchanged at docs/system/framing/briefing.md
     (cbc-framing). The README purpose paragraph and the devlog's
     CBC Run Briefing line land here. Names given before it are
     working names. -->

Goal: know what we're building and why, before code.
Now:
Gate:
Notes:

## Step 2: Identity (name, description, remote)     [ ]

Goal: the project's public identity decided, not defaulted.
Now:
Gate:
Known already:
- the plan is read end to end against the CBC Framing Exports: each later Plan Step
  still stands as named, or is reworded in place, never kept
  silently.

Notes:

## Step 3: Infrastructure Establishment  (infra-establish)    [ ]

Goal: services stood up, constrained to need, verified both ways.
Now:
Gate:
Notes:

## Step 4: CBC Bootstrap  (cbc-bootstrap)    [ ]

Goal: an empty but buildable, testable, runnable system wired to the
Runtime Ground, with the Adversity Harness proven on one adversity.
Now:
Gate:
Notes:

## Steps 5..N-3: Invariant Slices  (cbc-slice, one Plan Step per Invariant Slice)

Goal: two things are true at each close:
- the Invariant Slice is closed by an Evidence Test that creates
  its adversity;
- the order of the Invariant Slices left is decided again, never
  assumed from the first expectation.
Now:
Gate:
Notes:

## Step N-2: Retrospective  (retrospective)    [ ]

Goal: three things are true:
- every lesson the next CBC Run should act on is a decision in
  RETRO.md, with an example from this CBC Run and the place it
  lands;
- this CBC Run's CBC Run Asks point to those decisions;
- what only the next CBC Run can check is listed, each with the
  Plan Step that judges it.
Now:
Gate:
Notes: opens when the Invariant Slice Plan Steps close, before
Release, so it runs even if Release is skipped. What the reviewer
decides is the retrospective Agent Skill's.

## Step N-1: Apply the retrospective  (apply-retrospective)    [ ]

Goal: two things are true:
- this CBC Run hands over what its retrospective showed could be
  better, where that changes how its records read and not what it
  proved;
- RETRO.md says what happened to each decision.
Now:
Gate:
Notes: opens when RETRO.md closes. What the reviewer decides is the
apply-retrospective Agent Skill's.

## Step N: Release                                  [ ]

Goal: the system is handed to its audience, its Falsifiable Promise
shipped, observable, and reversible wherever it deploys.
Now:
Gate:
Known already:
- a CHANGELOG entry for the release;
- README true for a stranger, its commands verified on a clean
  machine;
- known issues filed in TODO.md;
- Release's own lessons added to RETRO.md, as decision blocks
  (`.claude/skills/retrospective/SKILL.md`, Stage 2, item 4).

Checked here, each unless this CBC Run records its own exclusion:
- monitoring and alerts in place;
- deploy and rollback documented and tried once.

Notes: opens when Step N-1 closes.

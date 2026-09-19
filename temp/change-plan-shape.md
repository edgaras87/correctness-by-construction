# What shape a change-plan's step list should take

Draft for the third run of `format-comparison`. Requirements first,
per §2 step 1; candidates listed but **not yet built**.

## The defect this answers

The groups change set (2026-09-19) was planned as six commits,
revised to thirteen at step 6, and landed at twelve with three
further divergences. Two specific failures, both traceable to the
shape of the list rather than to the work:

1. **Steps split by artifact.** Steps 10 and 11 were "the manuals"
   and "ARCHITECTURE" — a folder each. They had to fold into step 9,
   because committing 9 alone would have left a README pointing at
   a directory that no longer existed. change-plans §7 names this:
   *steps grouped by file type — tidy-looking, reverts incoherently*.
2. **The most confident steps were the wrong ones.** Steps 4 and 5
   built the `stack/` quarantine and wrote it into the records.
   Both were undone. The steps written as provisional survived; the
   steps written as firm did not.

A third thing, underneath both: `commit-messages` records that this
repo's commit **scope names the area touched**. A step list written
as commit subjects therefore reads as a list of folders, and
planning by folder is what §7 forbids. Neither convention mentions
the other.

## What a step list must carry

Stated as what a reader must *get*, so a candidate can fail a line.
"A reader" is whoever reviews at a boundary — today the user, later
whoever opens the set cold.

1. **The order in which decisions get taken, riskiest first.** A
   decision that could overturn the rest must be reached while
   little is built on it. The set's cost when a step is wrong is
   what has been built on top of it, not the step itself.

2. **What is true at each stop.** Work halts at every boundary, so
   the reader must be able to tell what state the repo is in there.
   The test is the convention's: undo one step and the repo is
   coherent.

3. **Which parts are agreed and which are guesses.** A reader must
   be able to see, without asking, where the plan stops being an
   agreement and starts being a hypothesis.

4. **What each step gives, not what it touches.** A step named by
   its files is a manifest; a step named by what becomes true is a
   plan. A file may be touched in as many steps as the work needs.

5. **It must survive being wrong in the middle.** When step N
   diverges, the shape must absorb it without rewriting the whole
   list. Today's rewrite cost a commit and still diverged three
   more times.

6. **It must cost less to write and revise than the work it
   guides.** A shape that is expensive to keep true will be kept
   false.

## Candidates, to be built

Each will be rendered as a real `CHANGE-PLAN.md` for the groups
set, **using only what was knowable on the morning of 2026-09-19**.
That is the honest test: we know what actually happened, so each
shape can be judged on whether it would have absorbed it.

- **A. Commit list.** What we have: numbered future commit
  subjects, a note each, a provisional tail permitted. Included so
  "nothing wins" has somewhere to land.
- **B. Decision list.** Steps are decisions, each with what will be
  known after it. Commits derive from decisions and are not listed.
- **C. Cascade, riskiest first.** Ordered by how much rests on the
  step times how likely it is to be wrong. The `stack/` question
  sits at position 1, not position 4.
- **D. Gate list.** Each step is a gate in `PLAN.md`'s idiom —
  verifiable facts, not intentions — and the commits emerge from
  meeting it.

A fifth shape may appear while building; §4 of the method says
building is what finds the modelling error.

## The four, built

Each written from the morning of 2026-09-19. Known then: Step 9's
gate and its four evidence items, ADR-0028 parking
`format-comparison` here, TODO parking the java-spring parts here.
**Not** known: that the grep over-reports, that the boundary runs
inside three skills, that the gate's template count is wrong, that
the groups would be directories, that anything would be renamed.

---

### A. Commit list — what we have

> **1.** `docs(agent): add change-plan for the groups`
> **2.** `docs(temp): the shipped files, sorted` — the measurement
> before the naming.
> **3.** `docs(adr): the groups are named` — ADR-0029, Proposed.
> **4.** *(provisional)* the layout follows the naming — intent:
> whatever step 3 makes untrue of the directories. Deferred to
> step 3's boundary.
> **5.** `docs: the records read in the groups` — ARCHITECTURE and
> `starter/README.md`.
> **6.** `docs(adr): accept 0029 and close Step 9`
> **7.** `docs(agent): close change-plan`

### B. Decision list — steps are decisions

> **D1. What are the groups?** Settled by sorting every shipped
> file into a candidate group and listing what refuses. *Known
> after:* whether three is the right number and where the seams
> are. *Commits:* however many the sort and its record take.
>
> **D2. What is a group, as a thing on disk?** A directory, a
> naming convention, or a marker inside existing directories.
> *Known after:* whether anything moves. **Not answerable before
> D1** — the seams decide what a group can be.
>
> **D3. What are they called?** Depends on D1 and D2.
>
> **D4. Do the parked questions ride?** `format-comparison`,
> java-spring, kit-skills. *Known after:* whether the boundary
> answers them or they answer separately.
>
> **D5. What becomes true in the records.** Follows D1–D4.
>
> Commits are derived at each boundary, not listed here.

### C. Cascade — riskiest first

> Ordered by *what rests on it* × *how likely it is to be wrong*.
> A step near the top is one whose being wrong costs the most.
>
> **C1. Is a group a directory or a description?** Highest: every
> other step's shape depends on it, and it has never been asked out
> loud — the gate says "named", which reads both ways. Ask before
> measuring; the answer changes what the measurement is for.
>
> **C2. Where do the seams fall?** Measured, not argued — sort
> every shipped file, list the refusals. Second because C1 decides
> whether a seam inside a skill is even allowed.
>
> **C3. What are they called, and what rule copies them?**
>
> **C4. The layout, if C1 said directories.**
>
> **C5. The parked questions, against the boundary now known.**
>
> **C6. Records, gate, close.**
>
> Each step names what would make it wrong, so the review at its
> boundary has something to check rather than a subject line.

### D. Gate list — PLAN.md's idiom

> **Step 1.** The groups are measured.
> Gate: every shipped file assigned to a candidate group; the files
> that refuse to sort listed as refusals, not forced.
>
> **Step 2.** The groups are decided.
> Gate: an ADR names them, their boundaries and their pins, with the
> gate's four evidence items weighed; each correction to the gate's
> own premises stated as a correction.
>
> **Step 3.** The tree matches the decision.
> Gate: a reader can copy the right subset by a rule they can follow
> without reading an ADR.
>
> **Step 4.** The records are true.
> Gate: ARCHITECTURE, the delivery README and TODO describe what is
> on disk; PLAN Step 9's gate closes or states its corrections.

---

## Reading them against the six

Verdicts marked **(rendered)** where the actual set settled it, and
**(prediction)** where reasoning did. §2 step 5: a prediction is not
a verdict until something confirms it.

| | A. Commits | B. Decisions | C. Cascade | D. Gates |
|---|---|---|---|---|
| 1. riskiest first | **fail** (rendered) | partial | **pass** (rendered) | fail |
| 2. what is true at each stop | fail (rendered) | weak | pass (prediction) | **pass** |
| 3. agreed vs guessed | partial | **pass** | **pass** | fail |
| 4. gives, not touches | **fail** (rendered) | **pass** | **pass** | **pass** |
| 5. survives being wrong | **fail** (rendered) | pass (prediction) | pass (prediction) | partial |
| 6. cheap to write and revise | **pass** | pass | partial | pass |

### What building found

**C1 is the finding, and none of the other three has it.** Writing
the cascade forced the question *is a group a directory or a
description?* to the top of the list — and that is precisely the
question that, unasked, cost the set four commits. In A it is not a
step at all; the commit list assumes prose groups because commit
subjects describe edits, and "name the groups" edits documents. In
B it appears as D2, below the sort. In D it is invisible: a gate
states what must be true, and both readings satisfy "the groups are
named".

So the cascade does not merely reorder the same steps. **It
surfaces a step the others do not contain.**

**A fails requirement 4 structurally, not accidentally.** A commit
subject in this repo is `type(scope)`, and `commit-messages` records
that the scope names the area touched. A list of commit subjects is
therefore a list of areas — a manifest. Steps 10 and 11 of the real
plan were `the manuals` and `ARCHITECTURE`, which is that failure
happening. This is the link neither convention states.

**D is stronger than expected on requirement 2** and weaker than
expected on 1 and 3. A gate is a statement of what must be true, so
it is exactly a description of a stop — but it says nothing about
order and cannot mark itself a guess. Gates are right for a plan
step that will be reviewed once, at its end; a change-plan is
reviewed at every commit inside it.

**B collapses toward C when you ask it to order itself.** Written
out, D1–D5 are already nearly risk-ordered, because dependency and
risk correlate — a decision everything rests on is usually also the
one you know least about. The difference is that C says so, and
therefore keeps the ordering when they diverge. B would have put the
sort first, which is where the real plan put it, and the sort was
not the risk.

**A requirement moved while building.** Requirement 2 was written as
"undo one step and the repo is coherent" — a revert test. Rendering
D showed that is the *consequence*, not the requirement: what a
reviewer needs at a stop is to know what is now true, and
revertability follows from it. Not struck, but the wording is
loose, and the next comparison should inherit the corrected form.

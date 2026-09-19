# 0030. The cascade wins; decide-first, and two renames

Date: 2026-09-19
Status: Proposed

## Context

The groups change set (ADR-0029) was planned as six commits, revised
to thirteen at its sixth boundary, and landed at twelve with three
further divergences. Two failures were traceable to the shape of the
plan rather than to the work:

**Steps split by artifact.** Steps 10 and 11 were "the manuals" and
"ARCHITECTURE" — a directory each. They had to fold into step 9,
because committing 9 alone would have left a README pointing at a
directory that no longer existed. `change-plans` §7 names this
exactly: *steps grouped by file type — tidy-looking, reverts
incoherently.*

**The most confident steps were the wrong ones.** Steps 4 and 5
built the `stack/` quarantine and wrote it into the records. Both
were undone. The one step written as provisional survived.

Underneath both, a link neither convention states: `commit-messages`
records that this repo's commit **scope names the area touched**. A
step list written as commit subjects is therefore a list of
directories — a manifest — and planning by directory is what §7
forbids.

The user's reading of that: *a change-plan is just a commit plan;
what we actually need is the thing that comes before it.* This ADR
is the answer, and the method that produced it is this repo's
comparison skill, run for the third time.

## The comparison

Six requirements, written into `temp/change-plan-shape.md` before
any candidate existed, each phrased as what a reader must *get* so
that a candidate can fail it. "A reader" is whoever reviews at a
boundary.

1. **The order in which decisions get taken, riskiest first.** The
   cost of a wrong step is what has been built on top of it.
2. **What is true at each stop.**
3. **Which parts are agreed and which are guesses.**
4. **What each step gives, not what it touches.** A file may be
   touched in as many steps as the work needs.
5. **It must survive being wrong in the middle**, without rewriting
   the whole list.
6. **It must cost less to write and revise than the work it guides.**

Four candidates, each built as a real plan for the groups set using
only what was knowable the morning it opened:

- **A. Commit list** — what we have. **Lost on 1, 4 and 5.**
- **B. Decision list** — steps are decisions, commits derived. Lost
  on 2; collapses toward C once asked to order itself, because
  dependency and risk correlate.
- **C. Cascade, ordered by what rests on each step.** **Chosen.**
- **D. Gate list**, in `PLAN.md`'s idiom. Lost on 1 and 3: a gate
  states what must be true and cannot say order or mark itself a
  guess.

**What building found, and reasoning had not.** The cascade
surfaces a step the other three do not contain: *is a group a
directory or a description?* That is precisely the question which,
unasked, cost the set four commits. In A it is not a step at all —
commit subjects describe edits, and "name the groups" edits
documents, so the prose reading is assumed silently. In B it sits
below the sort. In D it is invisible, because both readings satisfy
"the groups are named".

So the cascade does not reorder the same steps. It contains a step
the others lack.

**Two verdicts reasoning had wrong**, both corrected by building: D
is stronger than expected on requirement 2, a gate being exactly a
description of a stop; and B is not a distinct shape so much as an
unordered C.

**A requirement moved.** Requirement 2 was written as the revert
test — *undo one step and the repo is coherent*. Rendering D showed
that is the consequence, not the requirement: what a reviewer needs
at a stop is to know what is now true, and revertability follows.
Recorded so the next comparison inherits the corrected form.

## Decision

1. **Three layers, and each already has a home or gets one.**

   | | settles | artifact |
   |---|---|---|
   | contemplation | how, what, where, why | **`decide-first`**, new |
   | writing it down | how a commit reads | `commit-messages` |
   | sequencing | when one commit is too big | `commit-plan` |

2. **`decide-first` is a skill of this repo's own**, at
   `.claude/skills/decide-first/`. Its shape is the cascade: name
   what is undecided, rank by what rests on it, say how each
   question gets settled — **ask**, **measure**, or **compare** —
   settle the top one before touching the next, record it, and only
   then ask whether the work is one commit or many.

3. **It fires on shape, not on every set.** The line, which is the
   whole of its scope:

   > A question whose answer changes the **shape of the set** is
   > settled first. A question whose answer changes **a step** is
   > discovered inside it.

   The groups set is the worked example of both: *directory or
   description* changed the shape — twelve commits and a mid-set
   revision — while *where do the seams fall* changed steps and was
   correctly discovered inside, by the sort. A free diagnostic
   falls out: **if you cannot say roughly how many steps the set
   has, a shape question is still open.**

4. **`commit-plan` keeps everything it has.** An earlier draft of
   this decision narrowed its job to "sequence and classify", and
   that was wrong: it would have discarded the two modes §3 already
   provides — decision-first for a decision settled in
   conversation, material-first for one only seeable in the
   material — and the provisional-ADR mechanism, which is the best
   thing that happened in the groups set. ADR-0029 opened Proposed,
   was rewritten whole once and corrected twice, and flipped only
   at the end. None of that changes.

   What the failure actually was is narrower than "wrong mode": it
   was running material-first *without knowing which material to
   touch*, because a shape question had never been asked.

5. **What a commit plan does when it discovers something mid-way**
   is written down, because it will: classify it. In scope, keep
   going; changes the decision, back to contemplation; neither, to
   TODO. The groups set produced all three.

6. **`format-comparison` becomes `option-comparison`, and widens.**
   The method's real constraint was never *form* — it is whether
   the options can be built cheaply enough to look at. The evidence
   is in this repo: the `stack/` quarantine was built, looked at,
   and found wrong, and that was a structure question the skill's
   own §1 would have excluded. §1 widens to *more than one option
   could work, and each can be built cheaply enough to look at*,
   and the render stays the gate that keeps unbuildable options
   out — "should we ship this to runs" has no candidates to build.

   Rejected: `decision-comparison`, which collides with
   `decide-first` and reads as its sibling when it is one of its
   treatments.

7. **`change-plans` becomes `commit-plan`.** The name reads as
   *plan the change*, which is what it must not mean, and that
   misreading is the defect in the Context. Rejected: fixing the
   text and keeping the name, which leaves the trap in place for
   whoever reads only the name.

8. **The reference between the two skills is one-directional.**
   `decide-first` may name `option-comparison`; `option-comparison`
   gains no mention of `decide-first`. Both of its uses arrived
   with the question already on the table, raised by the user, and
   its trigger is source-agnostic. An earlier draft of this shape
   described a pipeline, which would have coupled them.

9. **Two triggers, because two of these are thin.**
   - If `decide-first` runs three times and never routes anywhere
     except `option-comparison`, it is a wrapper with two empty
     slots and the two should merge.
   - If the widened `option-comparison` never once settles a
     question that is not about form, the widening was wrong and
     the name goes back.

## Consequences

Good: the thing that was missing has a name and a moment, and the
convention that was carrying two jobs carries one. The comparison's
spec is written down and has now been corrected twice, so a fourth
run starts further along than this one did.

Bad: three names change at once, and one of them ships. Three runs
hold `change-plans` at a pin with a registry entry naming it, and
the delivery procedure has never renamed a convention — a gap this
set has to close on the way past.

Also: `decide-first` is built on one clear instance. `format-comparison`
was built on two and that objection is still recorded against it;
this is thinner. The difference claimed here is that this is not a
rule distilled from a pattern but a gap nameable in advance, and
the cost of being wrong is one file. Decision 9's first trigger is
where that claim gets tested.

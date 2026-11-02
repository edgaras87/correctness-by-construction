# The refinement's evaluation — a draft

<!-- A draft of the endings for `.claude/approaches-on-trial/refinement.md`,
     by `.claude/approaches-on-trial/approach-evaluation.md` Stages 1 to 4.
     The agent proposes, the reviewer decides each ending. The decided
     endings go to an ADR, with the ways rejected at the opening, as the
     refinement Plan Step's Gate asks; then this file goes. -->

## What was read

- `.claude/approaches-on-trial/refinement.md`, 415 lines, whole, at `a13d7c8`.
- Its history: 42 commits, from `2e9c26b` (a manual on trial) to now.
- Its one use: the refinement of 2026-10-18 to 2026-11-02, three Refinement
  Rounds and a last read, in `55e2bd0^:temp/refinement-2026-10-18.md`.

One use stands behind every piece. `approach-evaluation.md`'s own lesson
from its first use: "a first evaluation places nothing; its work is the
rewrite" (*Uses*, 2026-10-28).

## The pieces and their proposed endings

Each piece is one subject. The endings: placed, on trial, the project's
own, dropped.

1. **The need** (opening, *What it is for*): older text is brought up to
   a rule in work of its own. **On trial.** One use, and the eval of
   2026-09-30 before it, unnamed.
2. **What it reads** (§1): Living Text, not `docs/baselines/`, not a CBC
   Run's text in `temp/`. **On trial.**
3. **Refinement Rounds by what a fix does** (§2.1): true, then where it
   lives, then how it reads. **On trial.** It held across three Refinement
   Rounds. The last read showed Refinement Rounds order the read and the
   list, not the work (DECISION-54).
4. **Refinement Layers** (§2.2): six, a source before what derives.
   **On trial.** The last read used them to order the list, not the
   commits.
5. **Check the rules before each read** (§2.3), with its four questions
   for a fix. **On trial.** Used before each Refinement Round.
6. **Reading the Finding Kinds** (§2.4): one Finding Kind per reader, a
   broken rule and never taste, the rule frozen during the read, nothing
   fixed during it, each finding checked against the tree. **On trial**,
   the strongest piece: the eval, three Refinement Rounds and the last
   read all lived it. No convention fits it yet, so placing it would make
   a new one on one use.
7. **The finding's form and its cause** (§2.5): where, rule against text,
   how it stands, why it was missed. **On trial.** The causes carry
   lessons "to the Plan Step's close": see *Owed at this close* below.
8. **Endings** (§2.6): fixed, declined, moved. **On trial.** The last read
   used a fourth, "stands by a decision"; the rewrite names it.
9. **Working the findings** (§2.7): one Change Set from the list, shared
   facts first, then each file once; a design change made inside.
   **On trial.** One use of the Change Set from the list, the last read's.
   Its close recorded what diverged (`0f8544e`).
10. **A Refinement Round's close** (§2.8): read again, count, collapse.
    **On trial.** The collapse cut the file from 1,639 lines to 390.
11. **The last read** (§2.9): read again until nothing is found.
    **On trial**, as written. Skipped once, for budget (`765de0b`); the
    reviewer keeps the rule, so this use says nothing against it.
12. **The close** (§2.10): the file goes in a commit of its own, the
    devlog names it. **On trial.** Done in `55e2bd0` and `435d621`.

Nothing placed, nothing dropped, nothing the project's own: a refinement
is this repo's alone, and every piece has one use.

## The *Not known yet* items judged at this close

Each says it is judged at the close. Proposed:

- **Text another TODO item plans to rewrite:** one pass was better.
  Round 3 did the method's plain rewrite and the last read finished it;
  the TODO item kept only the concept references (`20bdb4d`).
  Rewrite: read it here.
- **Whether a refinement is the second check on text kept true:** stays
  open. Its home waits on TODO's "Decide which ideas here are Idea Models",
  whose trigger is now.
- **Whether the three Refinement Rounds hold:** held for eight Finding
  Kinds and Wiring. Stays open for a second refinement.
- **Whether a Change Set written from the list holds:** held, with the
  departures `0f8544e` lists. Stays open for a second use.
- **Approach on Trial Stages beside Agent Skill Stages:** held apart in
  the work. Stays open.
- **Whether the full reads again paid:** 54 of the last read's
  findings were older than their rule, in text the earlier Refinement
  Rounds had read and left. Stays open; a narrower read is weighed next
  time, and the rule stands meanwhile.

## Owed at this close, beside the evaluation

- **The findings' lessons** (§2.5): each finding missed at a change, or
  with the rule unclear, carries a lesson to the check or rule it names.
  The last read's 192 "missed at a change" share a few checks: the
  Foundation Check, one-home rule 6's question, the rename grep. One line
  per check is proposed at the Plan Step's close item "lessons written
  back".

## Stage 6, after the reviewer's endings

`refinement.md` is rewritten in general: each piece's statement first,
the dated notes beside it as evidence, and *Settled when* named. Its
*Uses* gains this use's note.

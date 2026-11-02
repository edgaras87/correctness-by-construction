# 0080. The refinement stays on trial after its first use

Date: 2026-11-02
Status: Accepted (2026-11-02, the reviewer took the evaluation's
proposal as it stood)

## Context

The refinement Plan Step's Gate asks for the refinement's Work
Approach to be evaluated, each piece with the reviewer's ending, and
for an ADR to record them with the ways rejected at the opening. The
Work Approach is `.claude/approaches-on-trial/refinement.md`, an
Approach on Trial (ADR-0058). It was used once: the refinement of
2026-10-18 to 2026-11-02, three Refinement Rounds and a last read.
That refinement's file is in git at `55e2bd0^:temp/refinement-2026-10-18.md`.

The evaluation ran by `.claude/approaches-on-trial/approach-evaluation.md`,
Stages 1 to 4. Its draft is `temp/evaluation-refinement-2026-11-02.md`
(`20d8102`). The evaluation's own lesson from its first use applies:
"a first evaluation places nothing; its work is the rewrite".

The read again after the last read (§2.9, *The last read*) was
skipped once, the reviewer out of tokens (`765de0b`). The rule stands,
and that use says nothing against it.

## Options considered

At the opening, 2026-10-18 (devlog 2026-10-18, later):

1. **Making text read better inside the refinement,** where it could
   be said better. Rejected: a finding names a broken rule, and polish
   with no rule has no end. It went to TODO as a readability pass the
   reviewer marks.
2. **Fixing as the read goes.** Rejected: one fix in a manual can
   change what is right in every file derived from it. The whole list
   shows those chains first (§2.4, *Reading the Finding Kinds*).
3. **One read for every Finding Kind, fixed together.** Rejected: a
   later fix would undo or waste an earlier one. Refinement Rounds go
   by what a fix does: true, then where it lives, then how it reads
   (§2.1, *Group the Finding Kinds*).

During the work, 2026-11-01:

4. **A commit plan for each Refinement Layer, or each Refinement
   Round** (the refinement's DECISION-53). Rejected by DECISION-54: one
   Change Set written from the list, shared facts first, then each file
   once (§2.7, *Working the findings*).

At this evaluation, for each of the twelve pieces:

5. **Placed** into a convention. Rejected: one use stands behind every
   piece. The strongest, how the Finding Kinds are read (§2.4), fits no
   convention, and placing it would make a new one on one use.
6. **Dropped.** Rejected: every piece did its work in that use.

## Decision

1. **Every piece of `refinement.md` stays on trial:** the need, what it
   reads, the Refinement Rounds, the Refinement Layers, the rules'
   check, the reading, the finding's form and cause, the endings, the
   working, a Refinement Round's close, the last read and the close.
   Nothing is placed or dropped. The piece list is the draft's.
2. **Text another TODO item plans to rewrite is read in the
   refinement.** One pass was the better way: Refinement Round 3 did
   the method's plain rewrite, the last read finished it, and the TODO
   item kept only the concept references (`20bdb4d`).
3. **The other *Not known yet* items stay open** for a second
   refinement: the second check on text kept true, whether the three
   Refinement Rounds hold, the Change Set from the list, Approach on
   Trial Stages beside Agent Skill Stages, and whether the full reads
   again paid.
4. **§2.9 stands as written.** Its skip in this use was for budget.

## Consequences

- `refinement.md` is rewritten in general (approach-evaluation, Stage
  6): each piece's statement first, the dated notes beside it, *Settled
  when* named, and this use's note under *Uses*. Decision 2 changes its
  *Not known yet*; the endings use a fourth, "stands by a decision",
  which the last read used.
- The draft `temp/evaluation-refinement-2026-11-02.md` goes once the
  rewrite lands.
- The findings' lessons are still owed at the Plan Step's close: the
  last read's 192 findings missed at a change share a few checks, and
  each check gets its line.
- The approach-drafting and approach-evaluation Approaches on Trial
  get their verdicts at the same close, separately.

# 0050. Small steps inside a planned commit, and a look back

Date: 2026-10-15
Status: Proposed (2026-10-15, under the commit plan for small steps)

## Context

Run 3, never-oversold, applied its retrospective in its Step 10
under one commit plan, and its RETRO.md, D19, judged the convention
from what that plan lived. It handed the edit back to us as
`commit-plan`, edited in place.

- **No room to try.** Each planned commit landed as one commit, so
  trying two ways meant reworking a commit in place. Run 3's
  polish, a clean-up pass after its last slice, had worked the other
  way under an explicit exception from its reviewer: commits made
  freely on a branch, then regrouped by kind, 36 into 7.
- **Nobody looked at the set as a whole.** The polish did, after the
  fact.
- **Step 10 lived small steps**, about 180 commits on a
  `step-10-apply-retro-detail` branch, landed as 16, each planned
  commit shown at its boundary. Three things the plan had not
  foreseen: commits inserted after it was written took letters (8b,
  22b, E2.1 to E2.12), so numbers already cited stayed true; one
  planned commit repeated over a set of records, three passes, with
  a stop rule; and sixteen small subjects broke the 50-character
  limit, found only at the regroup.
- **Our own watch** (TODO, 2026-09-19) asked whether the convention
  needs a rule about provisional commits, triggered by a set that
  diverges by more than half, or by a retrospective. Run 3's is
  that retrospective.

## Options considered

- **Retire the commit plan for free commits regrouped at the end.**
  Rejected, by run 3's reviewer: the target set up front works, and
  its revisions are the adjusting, as with a Proposed ADR edited
  while the work runs.
- **Squash only at the end.** Rejected: a pile to review at once.
- **Squash only at each boundary.** Rejected: nobody looks at the
  whole. Both are kept, each at its moment.
- **Small commits as run 3 wrote them**, made without a word asked.
  Rejected: commit-messages makes every commit wait for the
  reviewer's word, and run 3 lived small steps only under its
  reviewer's explicit grant. Taken with the grant written in.
- **Renumber the plan when a commit is inserted.** Rejected: the
  numbers are already cited, in the plan's notes, its revisions and
  its commit bodies.

## Decision

1. **A planned commit may be built as small commits, where the
   reviewer has granted them.** They are folded into the commit the
   plan names before its boundary, and the reviewer reviews that.
   Where the reviewer lets small commits land as they go, they are
   grouped by kind at the look back instead. Either way they are
   kept on a local `<branch>-detail` branch.
2. **Each small commit follows commit-messages when it is written**,
   not at the regroup.
3. **Before the close, the landed commits are looked at as a
   whole.** A better grouping is proposed, regrouped on the
   reviewer's word, and the plan revised to match what landed.
4. **A commit inserted later takes a letter**, `8b` after `8`.
5. **A planned commit may repeat over a set** of records, naming
   its order and, if it may run again, the rule that stops it.

## Consequences

- The commit-plan manual, the container's skill and our copy
  change; a run takes them at its next delivery, run 3's own edit
  absorbed with the grant added to it.
- The stop at every boundary is unchanged: a granted small commit
  is still a commit the reviewer allowed, and the planned commit is
  still shown before it lands.
- No set here has used small steps yet. The first that does tests
  decision 1's grant as written.

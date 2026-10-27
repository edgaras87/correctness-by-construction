# 0069. Each seat's copy is written for its seat

Date: 2026-10-27
Status: Proposed, opened under the commit plan for layer 5's work.

## Context

TODO's "Decide whether each seat's copy is written for its seat"
fell due at round 2's work on layer 5, before its fixes. The talk
behind it is conversation-memory §15, of 2026-10-25. In the
reviewer's words: "it should be all as 'byte-identical to the
shipped one' or non. now i need to track which are and which not.
it would be simple to repeat things and alter each part according
to seat."

ADR-0042 made the manuals the one source of both seats: the
container for a run, and this repo's own records and `.claude/`.
Neither is copied from the other, and a file the same in both is an
outcome. It rejected diverging the identical files, as "a change
nobody needs".

Four files are the same word for word in both seats today: the
`commit-messages`, `commit-plan` and `visual-comparison` skills, and
`.claude/approaches-on-trial/approach-drafting.md`. Five lines claim
three of them identical: the three manuals' lists of what derives
from them, agent-arrangement's *What the difference is*, and
conventions §1.1, which lets a file of ours byte-identical to its
shipped master keep `CBC ADR-nnnn`, "so one diff still checks the
pair". `approach-drafting.md` has no such line (the refinement's
FINDING-195). Each claim is kept true by hand.

Each shared file speaks to both seats at once. `approach-drafting.md`
tells the deliverer to open `approach-evaluation` and a run to write
a line under *To the deliverer*, and the run's copy carries our "The
refinement is open." `visual-comparison` names "the deliverer's
Mermaid trial". Our three skills cite `CBC ADR-nnnn` in 17 footer
lines, where every other agent file of ours cites `ADR-nnnn`.
`writing.md` and `one-home.md` are already written per seat, as their
manuals say.

`approach-drafting.md` is an approach on trial (ADR-0058). It carries
no `foundation` line, and no manual lists it. Its first evaluation
falls at the refinement's close.

## Options considered

1. **The shared files.**
   - Kept identical, the claims dropped. Rejected: they stay
     identical only while the tag exception stays, so which files are
     identical is still tracked, by a rule that no longer says so.
   - The claims kept, and `approach-drafting.md`'s added. Rejected:
     six lines kept true by hand.
2. **`approach-drafting.md`.**
   - Ours as its source, naming the run's copy, both rewritten now.
     Rejected: written twice, now and after its evaluation, and a
     link no other approach has.
   - Both written per seat now, unlinked. Rejected: nothing would
     carry a change in one to the other.

## Decision

1. **Each seat's copy is written for its seat.** No text claims a
   copy the same as another. Each follows its own seat's rules: ours
   cite `ADR-nnnn`, a run's `CBC ADR-nnnn`. Where the two agree, the
   text is the same, and nothing states it or checks it. This takes
   the option ADR-0042 rejected, for a reason that came after it:
   what claiming the outcome costs. ADR-0042's decisions stand.
2. **`approach-drafting.md` stays one text for both seats until its
   evaluation** at the refinement's close. There it is placed, and
   decision 1 then applies to it as to any skill. Nothing claims it
   identical meanwhile.

## Consequences

- The three manuals, agent-arrangement and conventions §1.1 drop
  their claims and the tag exception.
- Our three skills cite `ADR-nnnn`, and their lines addressed to the
  other seat are written for ours. The run's copies are written for
  a run in layer 6's work.
- A change to a convention both seats hold is two edits, one per
  seat, each checked against its manual, as ADR-0042 already says.
  The one-diff check of a pair goes; it showed the copies agreed with
  each other, never with their manual.
- The record forms' shared text needs nothing: each is written for
  its seat already, and none claims the other.
- Until its evaluation, the run's copy of `approach-drafting.md`
  keeps its line to the deliverer and "The refinement is open."

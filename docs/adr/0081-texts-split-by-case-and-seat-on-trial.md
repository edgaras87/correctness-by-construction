# 0081. Texts split by case and seat, ideas lifted out, on trial

Date: 2026-11-02
Status: Proposed, opened at the close of the Plan Step "Weigh the
idea-to-approach model"; judged at the close of the Plan Step that
moves exchange, from its counts (decision 4)

## Context

The refinement of 2026-10-18 to 2026-11-02 took 414 commits, most of
them keeping texts in step with each other. The Plan Step "Weigh the
idea-to-approach model" asked whether the model under this repo,
from idea to Work Approach, is worth defining, and whether ours is the
best. Its drafts are in `temp/model-example/`.

The repo's own counts, 2026-11-02:

- the 3 Idea Models each point at both others;
- all 12 manuals hold both seats, as the manual's form asks; the 3
  largest, 2,115 of the manuals' 4,284 lines, each hold several
  processes or subjects;
- 5 Agent Skills and Agent Rules exist twice, ours and the shipped
  one, each derived from its manual on its own: about 1,400 lines;
- 398 section references point at 129 sections, 22 of them at
  facts-in-sync §4.

Two ideas, one home per fact and a commit set, take 1,246 lines in 7
files today, and about 397 written as idea, project text and Work
Approach. Not yet a fair count: today's texts hold lessons from many
CBC Runs.

## Options considered

1. **Keep today's design, with lighter rules.** Not taken: the cost
   comes from the structure, both seats and several processes in one
   text and pointers running sideways between manuals. Lighter rules
   leave the mesh.
2. **Write each Work Approach from scratch, with no model.** Not
   taken: the same work is found again on every project, and nothing
   says why a rule is so, which is what makes a change unsafe.
3. **Choose a pattern first,** sockets, single-sourcing or versions,
   and rebuild to it. Not taken: every one of them needs the texts
   split first, and chosen before the split it is chosen on paper
   (`temp/model-example/other-patterns.md`).
4. **Move everything at once.** Not taken: 12 manuals, 3 Idea Models
   and about 20 Agent Skills and Agent Rules with their shipped
   copies. One idea first shows whether the move pays.

## Decision

1. **The layering is taken on trial:** idea, project text, Work
   Approach; links only up; an idea states its needs in its own
   words, and the project text wires them
   (`temp/model-example/layers.md`).
2. **The repo moves idea by idea, from the bottom up:** each Work
   Approach split by case, each convention by seat, each case into a
   section of its own, then the idea lifted out
   (`temp/model-example/move-plan.md`).
3. **From the first split,** no new sideways pointer, and each fact
   has one home at every commit: a part moves, never copies.
4. **Exchange moves first,** counted at each step: lines, pointers in
   and out, the texts a change touches. Whether to go on is decided
   from the counts.
5. **No pattern beyond the layering** is chosen before then.
6. **Before the first split,** three things are settled: which of the
   repo's own rules pause for a moved idea, how a Work Approach ships,
   and where names live.

## Consequences

- A change to one case of one seat touches one Work Approach, and the
  shared part is written once, not once per seat.
- While the move runs, two designs stand side by side, and the repo's
  own rules, the manual's form, the Foundation Check and the Fact
  Reference's section numbers, pull against a moved idea until
  decision 6 settles them.
- Deliveries to CBC Runs wait for an idea's move to finish.
- The drafts in `temp/model-example/` are kept files until the move
  gives what they hold a home.
- The goals drafted for the model were never approved one by one
  (`temp/idea-model-problem.md` §3); the counts of decision 4 stand in
  for them on this trial.

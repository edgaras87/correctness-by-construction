# 0081. The layering tried in a new repo, built step by step

Date: 2026-11-02
Status: Proposed, opened at the close of the Plan Step "Weigh the
idea-to-approach model"; changed 2026-11-03, before any move, from
moving this repo in place to rebuilding in a new repo; decision 7
changed 2026-11-04, from commits to rounds of correction; judged at
the close of the Plan Step "Rebuild in cbc-concept, until it stands
on its own"

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

This ADR first took the move in place: each of this repo's texts
split by case and seat, then each idea lifted out, exchange first.
Its decision 6 asked for three things settled before the first split:
which of the repo's own rules pause for a moved idea, how a Work
Approach ships, and where names live. The first of the three, the
manual's form, took 3 files, 2 commits and a Change Walk, and found a
line that would go stale at the next stage. The reviewer, 2026-11-03:
"it feels that this becomes another system just to try to rewrite."
Every rule here would pull against a moved idea, and each forgotten
one would stop the move again.

## Options considered

1. **Keep today's design, with lighter rules.** Not taken: the cost
   comes from the structure, both seats and several processes in one
   text and pointers running sideways between manuals. Lighter rules
   leave the mesh.
2. **Write each Work Approach from scratch, with no model.** Not
   taken: the same work is found again on every project, and nothing
   says why a rule is so, which is what makes a change unsafe.
3. **Choose a pattern first,** sockets, single-sourcing or versions,
   and rebuild to it. Not taken: every one of them needs small texts
   with one job each first, and chosen before them it is chosen on
   paper (`temp/model-example/other-patterns.md`).
4. **Move this repo in place, idea by idea,** this ADR's first form.
   Not taken: while the move runs, two designs stand in one repo,
   and each of the repo's rules needs its own decision to pause.
   That work is the cost the layering is meant to remove.
5. **Rebuild everything at once.** Not taken: nothing works until
   the last part is in, and nothing is judged on the way.

## Decision

1. **The layering is taken on trial:** idea, project text, Work
   Approach; links only up; an idea states its needs in its own
   words, and the project text wires them
   (`temp/model-example/layers.md`).
2. **It is tried in a new repo, `cbc-concept`,** next to this one.
   This repo is not moved. It is the source the rebuild reads, by
   `temp/rebuild-inventory.md`.
3. **The new repo stands on its own first:** git hygiene, writing,
   commit messages, each a Work Approach by the layering's template,
   standing alone. Then the ideas, as the work asks. The order is a
   draft (`temp/rebuild-inventory.md` §5, *A draft order*): each step is
   done before the next is chosen.
4. **A rule enters the new repo only when its work needs it.**
   Nothing is copied over because this repo has it.
5. **Each idea rebuilt lists the lessons its texts here hold,** and
   each is carried over or dropped on purpose.
6. **No pattern beyond the layering** is chosen before the trial is
   judged.
7. **The trial is judged from what the steps cost:** the rounds of
   correction and the files each took, against the same work here.
   Commits are no measure: polish is folded into the commit it fixes.
   When exchange is rebuilt, its counts are set against
   `temp/exchange-counts.md`.

## Consequences

- No rule of this repo pauses: the new repo does not have them.
- Two repos stand side by side. A fact keeps its home here until its
  idea is rebuilt there. Then the text here is history for that idea,
  not changed again.
- What CBC Runs receive from here, and whether CBC Run 6 is read
  from here, is decided at its own TODO items.
- The drafts in `temp/model-example/` and the inventory are kept
  files until the rebuild gives what they hold a home.
- A fresh rewrite can lose what this repo learned from 6 CBC Runs.
  Decision 5 guards against it, and the lessons gather in 3 ideas:
  exchange, commit-plan and conventions
  (`temp/rebuild-inventory.md` §4, *What the table shows*).
- The goals drafted for the model were never approved one by one
  (`temp/idea-model-problem.md` §3); the costs of decision 7 stand in
  for them on this trial.
- The layering has a second version, the reviewer's concept: the idea
  layer as a graph of chains, each kept true by an agent of its own.
  It is drafted in `cbc-concept`'s `drafts/layering-v2.md`, and
  simulated against v1 before either is adopted.

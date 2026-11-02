# Review of how this repo works

<!-- A draft for the review of how this repo works and what it costs:
     how its parts are kept and used, what each costs, whether it is
     worth it, and what could be better. Its first phase finds the
     goals the repo is judged against, by the goal-finding Approach on
     Trial (.claude/approaches-on-trial/goal-finding.md).
     The Rounds are only added to, never rewritten. A restart clears
     them: their locked answers stay in Background, and git keeps the
     old rounds. The approved goals go to their home in the README, and this file goes once the
     review is done; git keeps every version. -->

## Goals

Empty until the loop ends: Stage 6 writes them, Stage 8 approves
them.

## The question plan

The questions come in three parts. Each part's answers are what the
next part's questions ask about. *Background*, below, holds what
success and failure look like.

**Part 1, what we put here.** First, since everything after it is
about these things.

- 1.1 The kinds of thing the repo holds, with their sizes: the
  concept, the Idea Models, the conventions, what ships to CBC Runs,
  our own agent files, the records, the history. Which did you mean
  to have, and which grew on their own?
- 1.2 For each kind, who reads it: you, the agent, a CBC Run, or
  nobody?
- 1.3 Is anything missing that you expected to find here?

**Part 2, how we put things here.** Second: the way a thing gets in
is what turns a small change into many commits, and it is judged
only once what it acts on is known.

- 2.1 One real change, walked step by step: today's, from a talk to a
  committed rule. Which steps did you expect, and which surprised
  you?
- 2.2 Which steps happen on every change, and which only sometimes:
  the Plan Step and its Gate, the commit plan, Fact References,
  Glossary Names, the Foundation Check, the devlog?
- 2.3 Who drives each step: you, the agent, or a rule?

**Part 3, cost and worth.** Last, when cost has things and steps to
attach to.

- 3.1 Which of these costs more than it gives you?
- 3.2 Which has helped you, and would you keep even at its cost?
- 3.3 When two of them compete for a session, which wins?

**Then the goals,** written from all three parts, tested on real
moments, and approved (goal-finding, Stages 6 to 8).

## The queue

1. Which kinds of thing did you mean the repo to have, and which grew
   on their own? (1.1)
2. For each kind, who reads it? (1.2)
3. Is anything missing that you expected to find here? (1.3)

## Background

Two answers locked before the restart. The rounds that gave them are
in git: `7afe7f3` holds rounds 1 and 2; `3624553` holds round 3,
stopped.

- **Success, in six months:** the concept is sharper from what CBC
  Runs found; CBC Runs build real systems that keep their guarantees
  with little of the reviewer's attention; the way of working moved
  to a second concept repo with little change; the reviewer
  understands system design better, and the repo shows how; the repo
  is cheap to keep, most sessions going to new learning.
- **Failure, in six months:** writing cost more than it gave: too many
  records, each change rippling through them; rules about the writing
  costing more than the writing; text written before it was needed;
  text never read again; much read at each session's start; the
  reviewer's review time; rewording that changes how text reads, not
  what anyone does.

## Rounds

## Notes

Things noticed along the way, for the later phases: marks, doubts,
ideas. No fixes.

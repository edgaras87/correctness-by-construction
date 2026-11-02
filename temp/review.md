# Review of how this repo works

<!-- A draft for the review of how this repo works and what it costs:
     how its parts are kept and used, what each costs, whether it is
     worth it, and what could be better. Its first phase finds the
     goals the repo is judged against, by the goal-finding Approach on
     Trial (.claude/approaches-on-trial/goal-finding.md).
     The Rounds are only added to, never rewritten. The approved goals
     go to their home in the README, and this file goes once the
     review is done; git keeps every version. -->

## Goals

Empty until the loop ends: Stage 6 writes them, Stage 8 approves
them.

## The question plan

The questions come in three parts. Each part's answers are what the
next part's questions ask about. Rounds 1 and 2, below, stay as
background: what success and failure look like.

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

## Rounds

### Round 1

- **The queue as shown:** 1, 2 and 3, as in *The queue* above.
- **Question 1, and its options:** In six months, if this repo went
  well, what is true?
  - a. The concept is sharper: CBC Runs found gaps, and the concept
    chapters changed because of them.
  - b. CBC Runs build real systems that keep their guarantees, with
    little of your attention.
  - c. The way of working moved to a second concept repo and worked
    there with little change.
  - d. You understand system design better, and the repo shows how
    that understanding grew.
  - e. The repo is cheap to keep: most sessions go to new learning,
    not upkeep.
  - f. My own answer, or a mix.
- **The reviewer's answer:** "actualy i think all a-e."
- **The answer as locked:** all five are true when the repo goes
  well: a, b, c, d and e.
- **What changed in the queue, and why:**
  - Question 2 stays as it was: what failure looks like is still
    open.
  - Question 3 is replaced. It asked whether the concept or the way of
    working matters more, and the answer took both: a, b and d are the
    concept's, c is the way of working's. What is still open is which
    of the five comes first when they pull against each other.
  - New question 3: what "cheap to keep" means in amounts, since e
    needs a limit before it can be checked.

### Round 2

- **The queue as shown:**
  1. In six months, if this repo failed, what went wrong?
  2. When the five parts of success pull against each other, which
     come first?
  3. What does "cheap to keep" mean for you, in amounts?
- **Question 1, and its options:** In six months, if this repo
  failed, what went wrong?
  - a. The repo became upkeep: most sessions went to its own rules
    and records, and little to new learning.
  - b. CBC Runs stopped: none were started or read, so nothing came
    back.
  - c. CBC Runs ran, but their lessons never changed the concept.
  - d. You lost track: too much to hold in your head, and sessions
    start by working out where things stand again.
  - e. The way of working fits only this repo: a second concept would
    have to rebuild it.
  - f. The cost outgrew the value: usage limits and review time ate
    the work.
  - g. My own answer, or a mix.
- **The reviewer's answer:** "i think i lean on f. but maybe we could
  extend it more in details? i think what i now worry is that we
  documenting too much or incorrect way, that lead to too much
  documentary that eats time and tokens but does not bring value or
  bring insignificant."
- **Correction 1:** f, taken apart into its details. The question
  after it: in six months, if this repo failed because writing cost
  more than it gave, what did that look like? Its options:
  - a. Too many records: one change ripples through PLAN, TODO, the
    devlog, the ADRs, the glossary and more.
  - b. Rules about the writing cost more than the writing: the
    writing rules, Fact References and Glossary Names, checked on
    every line.
  - c. Written before it was needed: text for cases that never came.
  - d. Written and never read again, by you, the agent, or a CBC Run.
  - e. Each session reads a lot before it works, and that costs
    tokens.
  - f. Your review time: every change staged, shown and approved, in
    many small commits.
  - g. Polishing instead of using: rounds of rewording that change
    how text reads, not what anyone does.
  - h. My own answer, or a mix.
- **The reviewer's answer:** "take all a-g"
- **The answer as locked:** the repo failed because writing cost more
  than it gave, in all seven ways, a to g.
- **What changed in the queue, and why:**
  - "Cheap to keep, in amounts" moves to first. The failure the
    reviewer fears is cost, so the limit is what makes success e
    and this answer checkable.
  - New question 2: which writing has paid off. All seven worries are
    about writing that costs too much; before anything is cut, what
    is worth its cost has to be named too.
  - "Which of the five comes first" moves to third. The answer
    already ranks cost high, so it is less open than before.

## Round 3

- **The queue as shown:**
  1. What does "cheap to keep" mean for you, in amounts?
  2. Which writing here has paid off, and would you keep even at its
     cost?
  3. When the five parts of success pull against each other, which
     come first?
- **Question 1, and its options:** What does "cheap to keep" mean for
  you, in amounts? Pick the measures that matter, a number on each.
  - a. Upkeep share: at most __ of the commits or sessions go to the
    repo's own rules, records and rewording. Today: 1,410 commits
    since 2026-10-01, 7 of them touched `concept/`.
  - b. Usage: the repo's upkeep stays under __ of the weekly usage
    limit. Today: subagents alone took 11% of a week's usage over 29
    days (2026-10-22).
  - c. Review time: at most __ minutes a day, or per session. Today:
    not measured.
  - d. Start-up reading: what every session loads stays under __
    lines. Today: 363 lines of rules, plus a 26-line memory index.
  - e. Size: the way of working stays under __ times the concept.
    Today: about 10 times, 5,100 lines against 507.
  - f. My own answer, or a mix.
- **The reviewer's answer:** "i cant tell in numbers, because i never
  measure and not aware. also these questions too broad. can they be
  more related and what we have?"
- **Correction 1:** the question asks about things the repo has, not
  amounts. The question after it: which of these costs more than it
  gives you? Its options:
  - a. The refinement: 414 commits over 16 days, 2026-10-18 to
    2026-11-02, checking the repo against its own rules. CBC Run 6's
    lessons waited meanwhile.
  - b. `TODO.md`: 64 items in 1,262 lines, each with Context, Ideas,
    Trigger and See; and `TODO-CONVERSATION-MEMORY.md`, 1,041 lines
    of the talk behind them.
  - c. The devlog: October alone is 3,224 lines.
  - d. The decision records: 81 ADRs, and `.claude/decisions.md`,
    1,259 lines on the agent's setup.
  - e. The naming rules: 70 Glossary Names, each written whole and
    capitalized, such as "CBC Run Reading", and checked on every line.
  - f. Closing a Plan Step: the refinement's close took 8 commits:
    lessons, rules, delivery, the Gate and the close entry.
  - g. This review's setup: 7 commits before the first answer.
  - h. My own answer, or a mix.
- **The queue after the correction:** the reviewer found the questions
  too broad, so the other two are tied to what the repo has as well.
  1. Which of these costs more than it gives you?
  2. Which of these has helped you, and would you keep even at its
     cost?
  3. When two of them compete for a session, which wins?
- **Stopped, unanswered:** the reviewer: "okay, this is not working.
  these are good questions, but i think we have started blindly and
  asking what is upfornt. i want first to handle that part which is
  responsible in how we put things here. after it start asking about
  cost. maybe before how we put things here, we should ask what we put
  here." The questions now follow *The question plan*, above, and
  this round's three come back as Part 3.

## Notes

Things noticed along the way, for the later phases: marks, doubts,
ideas. No fixes.

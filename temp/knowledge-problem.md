# The problem: keeping what we know true

<!-- A draft: the problem of the Plan Step "Find how what we know
     stays true", its stage 1, in the reviewer's words. Built from
     TODO-CONVERSATION-MEMORY.md §31, *Keeping what we know true*,
     and from what temp/idea-model-problem.md says of the problem,
     not of a model. Polished one insight at a time, each a commit,
     so the diffs show what changed. It proposes no solution. Its
     home is decided when the Plan Step closes; it goes then, and
     git keeps every version. -->

## 1. The purpose

You and I are on the same page from one session to the next. You learn something and write it down. A new session reads it, and you don't have to retell it. We continue improving from there.

## 2. What goes wrong

- **The why goes missing.** An Agent Skill is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **What was written goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. I then read it as true and act on it. This is the bigger problem.

## 3. What was tried

This repo keeps each fact in one home, with references pointing at it (one home per fact). It was built without full consideration, and it costs too much to keep:

- **Finding is cheap, judging is not.** A search lists every place that points at a fact. Whether each place still holds needs reading. This repo has 398 section references pointing at 129 sections. The most pointed-at section has 22.
- **The fix becomes a loop.** A change in one referring place can force the home to change. Then every other reference has to be checked again. If they disagree, it's back to the home, and so on. A decision has to be weighed across many places, not taken in one pass.
- **It multiplies.** When references start disagreeing with each other, each disagreement starts its own loop.
- **The refresh is a sweep.** One agent reads the whole repo once, and every finding it makes can start a loop.

## 4. Where it may be wrong

Stage 2 tests these against the record:

- how often stale text actually hurt a session, and how;
- where staleness comes from: a retelling that drifted, a home that was wrong, or something never written down;
- whether every text must stay true, or only what I act on;
- whether the cost lies in the one-home idea itself, or in how it's kept, such as the sweep.

## 5. What would show it's solved

Each line can be checked:

- A new session continues without you retelling. Count the retellings and corrections in each session.
- Behind each Agent Skill, its why can be found.
- The cost of one change stays about the same as the repo grows.

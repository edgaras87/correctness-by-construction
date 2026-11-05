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

Knowledge is what one knows, and how one understands it. It lives in a head. Text is where it is stored: a copy, made at one moment.

The text is the interface between your mind and me. Each of us uses it differently:

- For you, it holds how you see something: your understanding and where you are, at the level that idea needs, basics for one and details for another. It isn't always correct. You use it to recall.
- For me, it tells what you know and how much. I usually know more about the subject. I use the text to see where you are, and to help you work on the idea from there: apply it, learn more of it, keep it up, and go deeper.

You and I are on the same page when my picture of your understanding, built from the text, matches your understanding and its level. Both of us learn, and write down what we learn. A new session reads it, and you don't have to retell it. We continue improving from there.

Not every text is understanding. An Agent Skill or a rule tells me what to do, and history tells what happened. Each is a kind of its own.

## 2. What goes wrong

- **The why goes missing.** An Agent Skill is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **What was written goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. I then read it as true and act on it. This is the bigger problem.

Where it breaks, at the interface between your mind and me. Cases found by thinking it through, each to be tested against real sessions in stage 2:

1. You know something the text doesn't hold.
2. The text is older than your understanding: you have moved on.
3. My context is older than the text: I read it earlier in the session, or from a summary, and it has changed since.
4. The text is ahead of you: I wrote it, and it holds my understanding, not yours.
5. The text is at the wrong level: too thin to recall from, or too dense to read.
6. The text is wrong, and I treat it as true instead of suggesting a fix.
7. I read the text and build a different understanding from it than you meant.
8. Two texts disagree, and neither says which one is where you are now.
9. The text holds the what, not the why.

Seen on 2026-11-05: case 1, the rebuild's purpose, written nowhere for 3 days; cases 4 and 5, my dense answers, until you said we were not on the same page.

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

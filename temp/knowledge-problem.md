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

Two sides work with the knowledge:

- **The human:** the person whose knowledge it is. They learn, decide, and carry the knowledge from one session to the next.
- **The agent:** the AI model working in a session. It starts each session knowing only what it reads.

The text is the interface between the human's mind and the agent. Each uses it differently:

- For the human, it holds how they see something: their understanding and where they are, at the level that idea needs, basics for one and details for another. It isn't always correct. The human uses it to recall.
- For the agent, it tells what the human knows and how much. The agent usually knows more about the subject. It uses the text to see where the human is, and to help them work on the idea from there: apply it, learn more of it, keep it up, and go deeper.

The human and the agent are on the same page when the agent's picture of the human's understanding, built from the text, matches that understanding and its level. Both learn, and write down what they learn. A new session reads it, and the human doesn't have to retell it. Both continue improving from there.

Not every text is understanding. An Agent Skill or a rule tells the agent what to do, and history tells what happened. Each is a kind of its own.

## 2. What goes wrong

- **The why goes missing.** An Agent Skill is written, but the idea behind it isn't. When it has to change, nobody can tell which parts can go.
- **What was written goes stale.** The work keeps moving forward. Earlier text becomes wrong, contradicts other text, misses something, or simply differs. The agent then reads it as true and acts on it. This is the bigger problem.

Where it breaks, at the interface between the human's mind and the agent. Cases found by thinking it through, each to be tested against real sessions in stage 2:

1. The human knows something the text doesn't hold.
2. The text is older than the human's understanding: they have moved on.
3. The agent's context is older than the text: it read the text earlier in the session, or from a summary, and the text has changed since.
4. The text is ahead of the human: the agent wrote it, and it holds the agent's understanding, not the human's.
5. The text is at the wrong level: too thin to recall from, or too dense to read.
6. The text is wrong, and the agent treats it as true instead of suggesting a fix.
7. The agent reads the text and builds a different understanding from it than the human meant.
8. Two texts disagree, and neither says which one is where the human is now.
9. The text holds the what, not the why.

Seen on 2026-11-05: case 1, the rebuild's purpose, written nowhere for 3 days; cases 4 and 5, the agent's dense answers, until the human said they were not on the same page.

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
- whether every text must stay true, or only what the agent acts on;
- whether the cost lies in the one-home idea itself, or in how it's kept, such as the sweep.

## 5. What would show it's solved

Each line can be checked:

- A new session continues without the human retelling. Count the retellings and corrections in each session.
- Behind each Agent Skill, its why can be found.
- The cost of one change stays about the same as the repo grows.

# Goal finding

**On trial.** How the reviewer and the agent find out what this repo
is for, by a loop of questions, before any part of the repo is judged.
Drafted 2026-11-02 for the review of how this repo works and what it
costs.

## What it is for

So that the review has goals to judge the repo against. The README's
"why" is one line, and the way of working has no written goal. Without
goals, a review can only ask whether each part does what it says, and
most parts would pass.

The goals come from the reviewer's answers, not from what the repo
already says, so drift in the repo does not carry into them.

## When it opens

At the start of the review, before the repo's parts are listed.

## Stages

### 1. Set up the queue

The agent writes 3 questions, the most important first. The first
two ask, in the reviewer's own words: what success looks like in six
months, and what failure would look like.

### 2. Work the top question

1. **The agent lists options for it in its answer,** lettered a, b,
   c. The last option is always "my own answer, or a mix". The
   questions are numbered 1 to 3, so "1b" names one option.
2. **The agent recommends none.** The questions ask what the
   reviewer wants; a recommendation would steer the answer.
3. **The reviewer answers in the chat input:** a letter, a mix of
   letters, their own words, or a correction to the question, its
   options, or both. After a correction, the agent rewrites the
   question and gives fresh options.
4. **Each round shows the whole queue,** all 3 questions. The
   reviewer may reorder them, or name one that is wrong.

### 3. Lock the answer

When the reviewer agrees, the answer is written down as fixed.

A later answer may contradict a locked one. The agent names the clash,
and the reviewer decides which stands. Both versions stay in the
notes.

### 4. Update the queue

1. **Revise the other 2 by the new answer:** reword one, replace one,
   or drop one that no longer matters.
2. **Add 1 new question.**
3. **Sort the 3 again,** and say what changed and why.

Then back to Stage 2.

### 5. Stop

The loop stops when a new answer no longer changes the goals. The
agent proposes the stop; the reviewer decides it.

### 6. Write the goals

From the locked answers, the agent writes the goals, each with a
check: how we would see it is being met.

### 7. Test the goals on real moments

Each goal is held against two or three real moments: CBC Run 6, the
refinement, a recent session. A goal that does not explain why a
moment felt worth it or wasted is changed.

### 8. Approve

The reviewer approves the list. The review's next step, listing the
repo's parts, starts from it.

## Where it is written

- **Each round** goes into the review's notes file in `temp/`, word
  for word:
  - the queue as shown;
  - the question being worked, and its options;
  - the reviewer's answer;
  - each correction, with the question and options after it;
  - the answer as locked;
  - what changed in the queue, and why.
- **The rounds run in chat,** never in the question dialog that pops
  up in the input. The dialog holds 4 options at most and hides the
  talk around them.

## Not known yet

- Whether options steer the answers even with no recommendation.
- Whether 3 is the right number of questions in the queue.
- Whether the stop rule ends the loop at the right time.
- How many sessions the loop takes.

## Ways rejected

- **Open questions in rounds, with no options:** hard to answer well,
  and it can take many rounds.
- **The agent drafts goals from the repo, the reviewer reacts:** it
  starts from the repo's own story, and the review exists because the
  reviewer doubts it.
- **Multiple choice alone:** the options steer the answers.
- **Real moments alone:** slow, and leans toward recent memory. Kept
  as Stage 7, to test the goals.
- **The question dialog:** 4 options at most, and the context hidden.

## Uses

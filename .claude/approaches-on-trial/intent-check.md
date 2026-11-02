# Intent check

**On trial.** How the reviewer's intent for this repo is written down,
made clear, and locked, so the repo can be checked against it.
Drafted 2026-11-02 for the review of how this repo works and what it
costs, after goal-finding was dropped.

## What it is for

So that the review checks the repo against what the reviewer meant
it to be. The intent is the reviewer's; the agent helps make it clear
enough to check, and adds nothing of its own.

## When it opens

At the start of the review, before any part of the repo is checked.

## Stages

### 1. The reviewer tells it

In their own words, as long or short as it comes. The intent is one,
told in stops, in any order. A later stop may add a line, or change
or drop any line already there.

The reviewer may tell how they picture it working. That helps reveal
the intent, and is kept, marked as how, apart from it: compared at
Stage 5, never taken as the intent.

### 2. The agent folds it in and plays it back

1. **Fold each stop into one draft,** grouped by subject, not by
   when it was told, a numbered line each, in plain words. Each line
   is sorted: intent, what must be true; or how, a way to make it
   true.
2. **Play back what the stop changed:** the lines added, changed or
   dropped.
3. **From what was told alone.** Earlier answers held as possible
   goals are not drawn on, so they do not steer the intent.
4. **What it noticed, labelled,** kept with the draft and answered
   whenever the reviewer chooses:
   - gaps, where a line can be read more than one way;
   - tensions, where two lines pull against each other;
   - differences from the repo, where the repo says otherwise. Named,
     not argued.

### 3. Correct, and lock when the whole is told

The draft lives in the review's notes file in `temp/`. The reviewer
corrects any line, at any stop. It is written as played back and
corrected; the reviewer's own words are not stored.

The intent is locked once, when the reviewer says the whole is told.
Locked, it is what the repo is checked against. Until then every
line is a draft.

### 4. Derive the goals

Once the intent is locked.

1. **Each goal is a check that comes from a line of the intent:** how
   we would see that line holds. The reviewer approves each.
2. **Each possible goal held from earlier is set against the intent.**
   One that follows from a line becomes a goal. One that does not is
   dropped, or shows something the intent missed, and the intent is
   reopened to take it.

### 5. Compare the how

Today's how, as pictured and as the repo has it, against its
alternatives.

1. **Against the goals first.** A how that fails a goal is out,
   however cheap.
2. **Then on the criteria,** for the ones left:
   - maintenance: what changing it takes;
   - readability, for the agent and for the reviewer, each;
   - future-proofing: how it takes work not yet seen;
   - complexity;
   - cost of use: what each session reads, and the reviewer's review
     time;
   - cost of switching: the work to move to it, and the lived
     evidence the old how leaves behind.
3. **On evidence where it exists:** what the CBC Runs and this repo
   lived, before theory.

## Not known yet

- How the alternatives are found.
- Whether the intent becomes the README's *why*.

## Ways rejected

- **goal-finding, a loop of questions with options:** dropped after
  its first use. Its questions asked about goals, costs and kinds of
  text; the reviewer wanted to check whether ideas and intent are put
  here the right way, which only the reviewer can state first
  (devlog 2026-11-02, goal-finding dropped).

## Uses

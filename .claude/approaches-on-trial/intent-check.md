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

### 1. The reviewer writes a part

In their own words, as long or short as it comes. The intent comes
in parts; each is worked before the next.

### 2. The agent plays it back

1. **Sorted and in plain words,** a numbered line each.
2. **From the part alone.** Earlier answers held as possible goals
   are not drawn on, so they do not steer the intent.
3. **What it noticed, labelled:**
   - gaps, where the part can be read more than one way;
   - tensions, where two lines pull against each other;
   - differences from the repo, where the repo says otherwise. Named,
     not argued.

### 3. Correct and lock

The reviewer corrects the playback until they say it holds. The part
is then written into the review's notes file in `temp/`, locked. A
later part may reopen it; the reviewer decides.

The part is written as played back and corrected; the reviewer's own
words are not stored.

### 4. Derive the goals

Once every part is locked.

1. **Each goal is a check that comes from a line of the intent:** how
   we would see that line holds. The reviewer approves each.
2. **Each possible goal held from earlier is set against the intent.**
   One that follows from a line becomes a goal. One that does not is
   dropped, or shows a part the intent missed, and that part is
   reopened.

### 5. Check the repo against the goals

How is not known yet.

## Not known yet

- How the repo is checked against the goals.
- Whether the intent's parts become the README's *why*.

## Ways rejected

- **goal-finding, a loop of questions with options:** dropped after
  its first use. Its questions asked about goals, costs and kinds of
  text; the reviewer wanted to check whether ideas and intent are put
  here the right way, which only the reviewer can state first
  (devlog 2026-11-02, goal-finding dropped).

## Uses

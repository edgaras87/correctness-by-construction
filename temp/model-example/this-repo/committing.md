# Committing work, in this repo

<!-- Layer: the project text
     (temp/model-example/layers.md). -->

**Draws on:**

- `temp/model-example/idea/commit-set.md`, as of 2026-11-02, all of it.
- `temp/model-example/idea/one-home.md`, as of 2026-11-02: *How it
  works*, points 1, 2 and 4.

## Wiring

| Idea | Need | Met by |
|---|---|---|
| A commit set | 1. Commit messages in one stable form | A local rule: Conventional Commits, a subject of 50 characters or fewer. A commit-messages idea, when written, takes its place. |
| A commit set | 2. Each plan line written once | One home per fact: the plan is the home of each line while the set runs. Relies on: a line has one home, and elsewhere is named, not restated. |
| A commit set | 3. A place for what the look-back found | The devlog, as history. |

## Answers

From *A commit set*:

1. **When a set is needed:** work of more than one commit.
2. **Where the plan lives:** `COMMIT-PLAN.md` at the repo's root,
   while the set runs.
3. **Who agrees:** the reviewer agrees the plan, and each commit.
4. **Without stopping:** once the plan is agreed, the commits run
   without stopping, except at a decision that is the reviewer's, and
   before the close.
5. **The look-back:** in the devlog entry of the close.

From *One home per fact*: as in `temp/model-example/this-repo/one-home.md`.

## Where ideas meet

- **A commit body retells its plan line.** *One home per fact* says
  name a fact, never restate it. A commit body says what changed and
  why, which the plan line already says. Settled here: a commit is
  history, and history is never a home. The commit body may retell
  the line; the plan stays its home while the set runs, and after the
  close the commits are what remains.

## Local needs

- **Agent files apart.** A commit never mixes the agent's own files
  with the project's. A set that touches both plans them as separate
  commits.

## Cases

| Case | Work Approach |
|---|---|
| Work needs more than one commit | Plan a set (not drafted) |
| A planned commit is next | Land a commit (not drafted) |
| The last commit has landed | Close a set (not drafted) |

## Lessons waiting

None yet.

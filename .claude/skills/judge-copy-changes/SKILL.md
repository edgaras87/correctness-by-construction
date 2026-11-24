---
name: judge-copy-changes
description: Judge each line of a Repo Reading, write its verdict, act on the verdicts, and end the Look for Lessons by moving the settled snapshot. Use when the human starts judging a Repo Reading whose list was checked whole, or when Read Copy Changes ends with nothing to judge.
---

# Judge Copy Changes

The second and third parts of a Look for Lessons: Judge Copy Changes, then Act on the verdicts. Who judges, what a verdict holds, and what each depth asks are in Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.3, *Judge Copy Changes*; §3.4, *Act on the verdicts*).

Why each stage is so: `.claude/understanding/judge-copy-changes.md`.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Repo Reading | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Register | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

With nothing to judge, in the cases *not moved* and *no Copy Change*, go to Stage 6.

## Stage 1 — sort the lines

- Lines listed together under one reason are judged together, and the reason once.
- For a line marked "no entry", look for its why in the Backend Repo: in the commit that made the Copy Change, then in the Backend Repo's records. If neither gives it, ask the human. Write where the why was found. Hold the line while nothing gives it.

## Stage 2 — question 0

For each line, read what happened, the Copy Change and the original part. Does the Copy Change fix what happened, without breaking something the Kit Copy did? If not, draft the verdict *unsound*, saying what it breaks or leaves unfixed, and ask that line nothing more.

## Stage 3 — the four questions

Ask each sound line these, in order, until one holds:

1. **Did the Kit Copy already say this?** Read the original part, in the Kit Version the Kit Copies came from, beside the Copy Change. If the Backend Kit has moved since, read its part as it is now too. Holds: *misread*; or *covered* by a Backend Kit change since that Kit Version.
2. **Is it specific to that Backend Repo's problem?** Read what happened, the Backend Repo's proposal, and its framing of its problem. Holds: *its own*, depth a.
3. **Does the idea above already hold it,** the Problem Domain Idea above the Adapted Case, or the Backbone Idea above that? A part left out on purpose carries a mark; a part lost carries none. Holds: *lost in narrowing*, depth d.
4. **How high is it true?** 4a, still true naming no Adapted Case: a lesson for its Problem Domain Idea, depth c at layer 2. 4b, still true naming no Problem Domain: a lesson for its Backbone Idea, depth c at layer 1. How to answer it is open: draft what you find, and say so.

If none holds: *a lesson for its Adapted Case*, depth b.

Take the depth from the reason, never from the edit. Split a line whose parts answer differently, each part judged alone, keeping its one Change Record.

## Stage 4 — the verdicts

Draft each verdict to its form (Change, in keeping knowledge, §3.3, *The verdict*): the answer, its why, and one line on the proposal, "the proposal holds" or "the proposal does not hold, because …". Lines under one reason share one verdict, and each says how its own Kit Copy is affected. A verdict that cannot be reached yet is *held*, with its trigger. The human decides each.

## Stage 5 — act

For each decided verdict, make what its depth asks (Change, in keeping knowledge, §3.4, *What each verdict asks*), drafting for the human to decide:

- **depth b:** reword the lesson for every Backend Repo; the Backend Kit's Adapted Case gains it; commit it in the Maintainer Repo, the body saying why and quoting the lesson as reworded;
- **misread:** perhaps the Backend Kit's wording, committed as for depth b;
- **depth c, d or e:** not yet walked. Stop, and ask the human;
- **depth a, unsound, covered, held:** nothing changes in the Backend Kit.

## Stage 6 — end the Look for Lessons

1. Remove the Repo Reading.
2. Set the *settled snapshot* to the stop, in the Repo Register.
3. If the human named the Backend Repo to update, the check in Deliver the Kit Update follows.

## Gates

- Every line has a verdict the human decided, or is held with its trigger.
- Each verdict says whether the Backend Repo's proposal holds.
- Each change made is committed, its body saying why.
- The Repo Reading is gone, and the *settled snapshot* is the stop.
- Nothing was written to the Backend Repo.

## What this does not do

- It sends no verdict down to the Backend Repo.
- It makes no Kit Update. Deliver the Kit Update does.

---

## Decisions

- ADR-0087 — written from the simulation alone, whole with its understanding; Judge and Act in one Adapted Case
- ADR-0084 — this repo's own Adapted Cases kept whole in `.claude/`

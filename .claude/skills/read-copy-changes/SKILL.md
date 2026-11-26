---
name: read-copy-changes
description: Read one Backend Repo's Copy Changes since the Maintainer Repo last looked, and list them in a Repo Reading, judging nothing. Use when the human names a Backend Repo, for its lessons or to update it, or asks which Backend Repos have new work.
disable-model-invocation: true
---

# Read Copy Changes

The first part of a Look for Lessons. It ends in one of three cases, and hands Judge Copy Changes a Repo Reading, or nothing to judge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.2, *Read Copy Changes*).

Why each stage is so: `.claude/understanding/read-copy-changes.md`.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Reading | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Register | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Update Take | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## Stage 1 — the two snapshots

1. Take the Backend Repo's *settled snapshot* from the Repo Register: the older snapshot. If an Update Take came since, start at its *version snapshot* instead, found in `.claude/kit-version.md` at the Backend Repo's main.
2. Name the stop: the commit the Backend Repo's main stands at now. Compare everything against that commit, never against main as it moves.

## Stage 2 — did main move

Compare the stop with the *settled snapshot*. If main has not moved, the case is *not moved*: stop here, and hand on to Act on the verdicts.

## Stage 3 — find each Copy Change

Compare each Kit Copy in the Backend Kit's folders, new files among them, between the older snapshot and the stop. Read each difference with the Change Record in the same diff:

- a Copy Change with its Change Record: take what changed, what happened, which work found it, and the Backend Repo's proposal;
- a Copy Change with no Change Record: take it from the comparison alone, and mark it "no entry";
- a Change Record changed with no Copy Change: take it as a changed why.

Open a commit between the two snapshots only to understand something the diff does not show.

If nothing differs, the case is *no Copy Change*: write no Repo Reading, and hand on to Act on the verdicts.

## Stage 4 — write the Repo Reading

The case is *Copy Change read*. Write the Repo Reading to its form (Change, in keeping knowledge, §3.2, *The Repo Reading*): one line per Copy Change, nothing judged; Copy Changes linked by one reason together, under it; its stop named. If a Repo Reading for this Backend Repo is still open, extend it.

Then stop. Ask the human to check that the list is whole. Judging starts only after.

## When the human asks which have new work

Compare every Backend Repo's main with its *settled snapshot* in the Repo Register. Say which have moved, and do nothing more.

## Gates

- The stop is named by its commit.
- Every Copy Change between the older snapshot and the stop has one line, and none is judged.
- Each line with no Change Record says "no entry".
- Nothing in the Backend Repo was written to.
- The human checked the list whole before judging began.

## What this does not do

- It does not judge. Judge Copy Changes does.
- It does not move the *settled snapshot*. Act on the verdicts does, at the end of the Look for Lessons.

---

## Decisions

- ADR-0087 — written from the simulation alone, whole with its understanding
- ADR-0084 — this repo's own Adapted Cases kept whole in `.claude/`
- ADR-0089 — not invoked by the agent on its own, since a CBC Run reads as a Backend Repo by its description

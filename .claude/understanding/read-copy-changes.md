# Read Copy Changes, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Read Copy Changes, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §4.2.2, Read Copy Changes, the part it is written from. It adapts that text, and never retells it.
What stands on it: nothing yet. Its Instruction Text waits for the rewrite; until then, the exchange-read Agent Skill does this work, by the older model (ADR-0087, decision 5).
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Why it carries no Foundation Line: docs/conventions/conventions/ §1.3, The Foundation Line.
How each rule was chosen: temp/common-ground/backend-repo-change-simulation.md §4, Read Copy Changes.
-->

This text says how the Maintainer Repo finds what one Backend Repo changed in its Kit Copies since it last looked, and lists it, judging nothing. What the part hands on, the stop and the Repo Reading, is the layers document's (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §4.2.2, *Read Copy Changes*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Reading | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## 2. How it starts

The human decides which Backend Repo gets a Look for Lessons, and when. The human names a Backend Repo, for its lessons or to update it, and the agent compares its main with its *settled snapshot*. When the human asks which Backend Repos have new work, every one's main is compared with its *settled snapshot*, and nothing more is done. No state is kept: whether a Backend Repo has work comes from its main and the *settled snapshot*, never from a line someone must keep true.

## 3. Two checks at main

Both are on whether there are Copy Changes to judge:
1. **main moved:** the Backend Repo's main against the *settled snapshot*;
2. **Copy Changes:** the Kit Copies, compared between the older snapshot and the stop. It is asked only when main moved.

Their answers sort the Look for Lessons into one of the three cases (the layers document's §4.2.2).

## 4. Finding each Copy Change

Each Kit Copy in the Backend Kit's folders, a new file among them, is compared between the older snapshot and the stop. A Change Record lands in the same diff as its Copy Change, so pairing them is reading one diff. Three things can come out:
- a Copy Change with its Change Record: read with its what, what happened, which work found it, and the Backend Repo's proposal;
- a Copy Change with no Change Record: read from the comparison alone, and marked "no entry";
- a Change Record changed with no Copy Change, as when a why is rewritten: read as a change of its why.

The agent only reads the Backend Repo, and writes only in the Maintainer Repo.

## 5. The list checked whole

The agent writes the Repo Reading (the layers document's §4.2.2). The human checks that the list is whole; then it is judged.

## 6. When its Instruction Text loads

It loads when the human names a Backend Repo, for its lessons or to update it, or asks which have new work, and says everything above.

## 7. Open

A Backend Repo nobody names gets no Look for Lessons until its work resumes. Its trigger: the first lesson found late because a Backend Repo went without one.

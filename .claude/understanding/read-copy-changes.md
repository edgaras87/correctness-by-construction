# Read Copy Changes, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Read Copy Changes, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md §3.2, Read Copy Changes, the part it is written from. It adapts that text, and never retells it.
What stands on it: .claude/skills/read-copy-changes/SKILL.md, its Instruction Text, an Agent Skill.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Why it carries no Foundation Line: docs/conventions/conventions/ §1.3, The Foundation Line.
Its first source, input and not rules: temp/common-ground/backend-repo-change-simulation.md §4, Read Copy Changes, each step's Chosen.
-->

This text says why the Maintainer Repo reads one Backend Repo's Copy Changes the way its Agent Skill does. What the part hands on, the stop and the Repo Reading, and why, is in Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.2, *Read Copy Changes*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Failure Case | `temp/common-ground/common-ground-problem.md`, *Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Reading | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Register | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Update Take | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## 2. Who starts it

The human names a Backend Repo, and the agent compares its main with its *settled snapshot* to see whether it has new work. Two other ways were weighed:

- **The human marks the Repo Register by hand.** It depends on the human remembering, and the Repo Register then says a Backend Repo has nothing new when it has new work (Failure Case 2).
- **A Look for Lessons only when the Backend Repo's work resumes.** A Backend Repo whose work does not resume is never read, and what it learned is lost (Failure Case 1). The Look for Lessons when work resumes still runs: naming a Backend Repo to update starts one.

So no state is kept: whether a Backend Repo has new work is found by comparison when asked, never from a line someone must keep true.

## 3. How a Copy Change is found

Each Kit Copy is compared between two snapshots of the Backend Repo's own, the older snapshot and the stop. Three other ways were weighed:

- **Each Kit Copy against the Kit Version it came from.** At the first Look for Lessons after birth or an Update Take, it finds the same. After it, a Copy Change already judged differs from that Kit Version until the next Update Take, and is found again at every Look for Lessons before it.
- **The Change Records alone, with no comparison.** It misses a Copy Change with no Change Record. The Backend Repo's commit check should stop one, but one can still land (Failure Case 22). So a Copy Change with no Change Record is still listed, marked "no entry".
- **The commits between, walked one by one.** It shows every edit on the way, and Copy Changes the Backend Repo's gate reversed. The gate has settled those; what stands at the stop is what is read.

A Change Record sits in its Kit Copy, so it changes in the same diff as its Copy Change. Pairing them is reading one diff, and nothing else is read.

## 4. The list before the judging

The agent lists each Copy Change, judging none, and the human checks the list whole before judging starts. Two other ways were weighed:

- **Each Copy Change judged as it is listed.** Copy Changes with one reason are then judged apart, and each verdict tends to follow the Backend Repo's proposal (Failure Case 20). Listing is cheap and judging is not, so the list is checked whole first.
- **Only the Copy Changes the Backend Repo proposed as any repo's.** It takes the proposal for the verdict, and a lesson for every repo stays in one Backend Repo (Failure Case 20).

## 5. Only reading

The agent reads the Backend Repo and writes only in the Maintainer Repo. What the Maintainer Repo makes of a Copy Change reaches the Backend Repo only by a Kit Update, on the human's word (Change, in keeping knowledge, §3.5, *Deliver the Kit Update*).

## 6. Why an Agent Skill

Its moment is the human's word: naming a Backend Repo, or asking which have new work. Neither repo can see when a stretch of work ends, so nothing else marks the moment. An Agent Skill fires on such a word, and loads nothing into a session that never reads a Backend Repo.

## 7. Open

- A Backend Repo nobody names gets no Look for Lessons until its work resumes. Its trigger: the first lesson found late because a Backend Repo went without one.

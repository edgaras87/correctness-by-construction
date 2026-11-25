# Deliver the Kit Update, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Deliver the Kit Update, making and staging, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md §3.5, Deliver the Kit Update, the part it is written from. It adapts that text, and never retells it.
What stands on it: .claude/skills/deliver-the-kit-update/SKILL.md, its Instruction Text, an Agent Skill.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Why it carries no Foundation Line: docs/conventions/conventions/ §1.3, The Foundation Line.
Its first source, input and not rules: temp/common-ground/backend-repo-change-simulation.md §7, Deliver the Kit Update, each step's Chosen.
-->

This text says why the Maintainer Repo makes and stages a Kit Update the way its Agent Skill does. When one is due, what it holds, and what crosses to the Backend Repo, and why, are in Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.5, *Deliver the Kit Update*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Paths Rule | `docs/conventions/agent-arrangement/` §5.6, *Rules files* |
| Plan Step | `docs/conventions/project-recording/` §2.1, *What a plan is* |
| Update Note | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Update Take | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## 2. Making and staging in one Adapted Case

Staging is one step of the same work, taken after the human's word. So one Adapted Case holds both, and one Agent Skill runs them as two stages, the human's word between (ADR-0087).

## 3. The order of the check

Each step of the check guards the Update Take that comes later:

1. **A Look for Lessons first.** A Kit Update is built against the *settled snapshot*. A Copy Change not yet taken into account would leave the Backend Repo's main past it, and the Update Take would refuse the Kit Update.
2. **The Kit Versions compared next.** When the Backend Repo's is the newest, there is nothing to carry, and nothing more is done.
3. **No open Plan Step in the Backend Repo.** Finishing an open step would move main, and the Update Take would refuse the Kit Update too. So nothing is made while one is open.

## 4. Checking what was staged

Once staged, each file is compared with the new Kit Version, and the Backend Repo checks the Update Note against the files when it takes them. Two other ways were weighed:

- **A second Adapted Case of the Maintainer Repo's checks it, apart from the one that staged it, as at birth.** Birth chose it because the start becomes the base of every Look for Lessons. Here a wrong file is held in the Backend Repo's `temp/`, never in force, and a comparison of files leaves little mistake to share.
- **Only the Backend Repo's check, at the Update Take.** The Backend Repo cannot open the Backend Kit, so a staged file that differs from it would pass.

## 5. Why an Agent Skill

Its moments are the human's words: naming a Backend Repo to update, once its Look for Lessons has ended, and then the word to deliver. Neither repo can see when the Backend Repo's work resumes, so nothing else marks the moment.

## 6. Open

- A second check of what was staged, as at birth. Its trigger: a staged file found, after an Update Take, to differ from the Backend Kit.
- Where each kind of Backend Kit file lands in a Backend Repo: an Instruction Text where its kind loads, such as a Paths Rule in `.claude/rules/`, an Adapted Understanding Text in `.claude/understanding/`, and the Backend Kit's Defined Terms in a place not yet set. The Agent Skill does not yet say it. Its trigger: the first Kit Update that carries a file from `knowledge/adapted-cases/`.

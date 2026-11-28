# Commit sets, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/commit-sets.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Case for commit sets.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first source, input and not rules (PLAN.md, the commit-plan manual's Plan Step, decision C): the Backend Kit's commit-plan Agent Skill, delivery/container/.claude/skills/commit-plan/SKILL.md, its §3: a module and the architecture paragraph that maps it.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is commit sets in the Backend Repos' Problem Domain, CBC backend design. One thing differs from commit sets here: a repo that builds software stays coherent as software. Nothing else differs. How work larger than one commit is planned is commit sets' (`knowledge/backbone-ideas/commit-sets.md`). The Backend Kit's Adapted Case for commit sets is written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Coherent as software

A Backend Repo builds software. So a commit reverted alone leaves the software coherent, and the text that describes it (`knowledge/backbone-ideas/commit-sets.md` §4, *How the commits are split*). A module and the architecture paragraph that maps it are one commit.

**Rules:**

- A module and the architecture paragraph that maps it land in one commit.

## 3. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

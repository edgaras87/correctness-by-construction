# Visual comparison, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/visual-comparison.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Case for visual comparison.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules:
- the visual-comparison manual, docs/conventions/visual-comparison/README.md, deleted on 2026-11-27, its last state in git at e8edf8f3: The seats; What this does not cover, its first item (PLAN.md, the visual-comparison manual's Plan Step, decision C);
- the Backend Kit's visual-comparison Agent Skill, delivery/container/.claude/skills/visual-comparison/SKILL.md: its step 4, the notations under their condition; its §5, the project's own forms.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is visual comparison in the Backend Repos' Problem Domain: who picks a Backend Repo's notations. How the way a structure is shown is chosen is visual comparison's (`knowledge/backbone-ideas/visual-comparison.md`). The Backend Kit's Adapted Case for visual comparison is written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Its own notations

A Backend Repo runs the comparison on its own pictures. It picks its own notations, and decides whether it holds to plain text that renders with no build step (`knowledge/backbone-ideas/visual-comparison.md` §6, *The buildable notations*).

The Maintainer Repo's Mermaid trial is not delivered (ADR-0027, decision 3). The Mermaid in the Backend Kit's cases is that trial's, not a choice made for the Backend Repo.

**Rules:**

- A Backend Repo picks its own notations, and whether it holds to plain text with no build step.
- The Backend Kit's Adapted Case names no notation as the Backend Repo's choice.

## 3. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

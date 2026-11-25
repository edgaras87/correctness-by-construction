# Defined Terms, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/defined-terms.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's terms text, knowledge/adapted-cases/cbc-backend-design/defined-terms/defined-terms.md.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Why it is written: ADR-0088, decision 9.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says how the Backend Kit's texts mark, define and find their Defined Terms, as a Backend Repo reads them. It is the Backbone Idea of Defined Terms adapted to CBC backend design, from `knowledge/backbone-ideas/defined-terms.md`.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Where a Backend Repo finds one

A Backend Repo works by its Kit Copies, and cannot see the Maintainer Repo (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.5, *Deliver the Kit Update*). A Kit Copy that pointed at a Defined Term's home in the Maintainer Repo would point at nothing it can open.

Defined Terms says a Defined Term is defined in one text, and every other text points there (`knowledge/backbone-ideas/defined-terms.md` §4, *Where it is defined*). Here that rule is narrowed, and marked: a Backend Repo cannot follow a pointer to the Maintainer Repo, so its Kit Copies read each definition in the Backend Kit's terms text, adapted from its one home and checked whenever that home changes (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**).

**Rules:**

- Every Defined Term a Kit Copy uses is defined in the Backend Kit's terms text. A Kit Copy points there, never at the Maintainer Repo.
- Each entry is adapted from its Defined Term's one home, and is never changed on its own. The terms text names that home for each entry, so a change there finds it.
- The terms text holds only the Defined Terms the Backend Kit's texts use. An entry is added with the first Adapted Case that uses it.

## 3. The mark

A Backend Repo's agent and its human read a Kit Copy in Markdown, as plain English, unless something shows a word is not.

**Rules:**

- A Defined Term is two or more words, each capitalized, and written the same at every use.
- It is bold once, where the terms text defines it, and nowhere else.

## 4. Finding one

An agent opens a whole file unless told otherwise, and the terms text grows with the Backend Kit.

**Rules:**

- A definition is found by a search of the terms text for the Defined Term in bold.

## 5. Open questions

A question joins this list when work meets one, and leaves it once its answer is in the text above.

1. **A Defined Term a Backend Repo coins:** where its own texts define it, and whether it goes up as a lesson. Its trigger: the first Defined Term a Backend Repo coins.

# Repo hygiene, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/repo-hygiene.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Case for repo hygiene, its three files at its root.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first source, input and not rules: the repo-hygiene manual, docs/conventions/repo-hygiene/README.md: §3 and The seats.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is repo hygiene in the Maintainer Repo's Problem Domain, keeping knowledge: its own three files, and the Backend Kit's that it keeps. What the files are, and what every repo keeps out, are repo hygiene's (`knowledge/backbone-ideas/repo-hygiene.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Hygiene Base | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Stack Overlay | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |

## 2. No stack

The Maintainer Repo builds nothing: it keeps texts. So it has no stack, and nothing to append a Stack Overlay for. Repo hygiene's Stack Overlay is left out here, and marked so (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**, *Narrowing, never shrinking*).

**Rules:**

- The Maintainer Repo's three files are the Hygiene Base, and the lines its own work adds. They hold no Stack Overlay.

## 3. The Backend Kit's files

The Maintainer Repo keeps the Backend Kit's Hygiene Base and its Stack Overlays, as it keeps every part of the Backend Kit (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3, *The layers*). A Stack Overlay is written for each stack a Backend Repo builds on.

**Rules:**

- A choice in a new stack's Stack Overlay that is not obvious is recorded as a decision, with why.

## 4. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

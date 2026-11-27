# Commit messages, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/commit-messages.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Case for commit messages.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first source, input and not rules: the commit-messages manual, docs/conventions/commit-messages/README.md, deleted on 2026-11-27, its last state in git at 47007e1b: from What it is for, the commits lived under it; from §3, The Concept Deliverer's habit, why the scope carries the signal, its list of scopes left to this repo's own Adapted Case (PLAN.md, the commit-messages manual's Plan Step, decision A); The seats.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is commit messages in the Maintainer Repo's Problem Domain, keeping knowledge: which part of a subject carries the signal in a repo that keeps only text, and when its subjects are counted. How a commit is written is commit messages' (`knowledge/backbone-ideas/commit-messages.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The scope carries the signal

The Maintainer Repo builds nothing: it keeps texts. Nearly every change is to a document, so by type alone nearly every commit is `docs`. A log that reads `docs` on every line says nothing. Commit messages gives the signal to the type (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*). A repo of text can give it back in one of two ways:

- **The type carries it:** `feat` for what the Maintainer Repo ships, `docs` for its own records.
- **The scope carries it:** `docs` for most commits, and a scope that names the area, where one area is the whole commit.

The Maintainer Repo takes the scope. Either way works. What does not work is following neither, and finding the shape afterwards in the log.

**Rules:**

- A change to text is typed `docs`, and the scope carries the signal.
- Each scope names an area of the repo. This repo's own Adapted Case lists them.
- `feat` or `fix` marks a change a Backend Repo would notice: something a Backend Kit file gained or lost.

## 3. When subjects are counted

The Maintainer Repo counts its subjects at each Plan Step's close, against the check's line of 70 (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*). It has lived under commit messages since its start: 480 commits by 2026-09-19. Its subjects miss the aim of 50 often (`knowledge/problem-domain-ideas/keeping-knowledge/how-an-agent-works-in-keeping-knowledge.md` §3, *What the work showed*, A1). The line of 70 lets a small miss pass, and finds a large one.

**Rules:**

- Every subject on a Plan Step's branch is counted by script at the Plan Step's close.

## 4. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

# Records, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/records.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Cases for its records.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first sources, input and not rules: the project-recording manual, docs/conventions/project-recording/README.md: The seats, its items 1 to 6; the map's QUESTION-3, temp/rewrite-map.md §10, Shared questions.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is records in the Maintainer Repo's Problem Domain, keeping knowledge: what its records hold differently, the one it leaves out, and the Backend Kit's that it keeps. Which records a repo keeps, and why each is written as it is, are records' (`knowledge/backbone-ideas/records.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit Update Note | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Record Stub | `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §1, *Its Defined Terms* |

## 2. No end

The Maintainer Repo has no last Plan Step: it keeps knowledge for as long as Backend Repos are worked. So no look back at its end gathers its lessons. Each Plan Step writes its own back when it closes.

**Rules:**

- A Plan Step's lessons are written back where they came from when it closes.

## 3. The plan

No playbook is written from the Maintainer Repo's plan, so its finished Plan Steps are evidence for nothing. They are history, and history is the devlog's.

**Rules:**

- The plan holds the one Plan Step being worked, and beside it any Plan Step stopped for it.
- A finished Plan Step leaves the plan when it closes; the devlog tells it.
- A finding goes to the backlog when it is found, so the plan keeps no list of what was found along the way.
- The decisions list themselves, so the plan keeps no index of them.

## 4. The decisions

The Maintainer Repo's ADRs record how ideas, and the texts made from them, are designed, not one choice in a build. One decision often holds several numbered parts.

**Rules:**

- An ADR has no page limit. Its length is held by cutting what adds nothing.

## 5. The architecture

The Maintainer Repo builds nothing that runs. Its architecture describes its texts, how they tie, and what goes to the Backend Repos.

**Rules:**

- The architecture describes texts and what is delivered, never a running system.

## 6. No changelog

The changelog is left out here, and marked so (`knowledge/backbone-ideas/change.md` §4, *The arrows*, its **Rules**, *Narrowing, never shrinking*). A Backend Repo pins a Backend Kit Version, never this repo's own texts. What changed since the version it holds, and why, reaches it in a Backend Kit Update Note (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms*). No one else takes a version of the Maintainer Repo.

**Rules:**

- The Maintainer Repo keeps no changelog of its own.

## 7. The Backend Kit's records

The Maintainer Repo keeps the Backend Kit's Record Stubs and its playbook, as it keeps every part of the Backend Kit (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3, *The layers*). They are written from records, in CBC backend design (`knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md`), never copied from the Maintainer Repo's own records.

**Rules:**

- The Maintainer Repo's records and the Backend Kit's Record Stubs are written apart, each from its own Problem Domain Idea.

## 8. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

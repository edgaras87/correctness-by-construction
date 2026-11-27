# Repo hygiene, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/repo-hygiene.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Case for repo hygiene.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules:
- the repo-hygiene manual, docs/conventions/repo-hygiene/README.md, deleted on 2026-11-26, its last state in git at ea07c6dd: What it is for, §2, §3 and The seats;
- three Backend Repos that wrote their stack's lines by hand: temp/reading-run-4-2026-11-26.md, FINDING-38; temp/reading-run-5-2026-11-26.md, FINDING-40; temp/reading-run-6-2026-11-26.md, FINDING-26.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is repo hygiene in the Backend Repos' Problem Domain: when a Backend Repo gets its three files, and when its stack's lines come. What the files are, and what every repo keeps out, are repo hygiene's (`knowledge/backbone-ideas/repo-hygiene.md`). The Backend Kit's Adapted Case for repo hygiene is written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Hygiene Base | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Stack Overlay | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |

## 2. At birth

A Backend Repo is born with the Backend Kit's Hygiene Base, so the three files are in its first commit. From then they are its own (`knowledge/backbone-ideas/repo-hygiene.md` §5, *Whose files they are*).

A Backend Repo is worked by an agent and one person. The person's own instructions to the agent are theirs, in their checkout. One Backend Repo ignored that file itself, before the Hygiene Base did. The Hygiene Base has carried it since.

**Rules:**

- A Backend Repo's first commit holds the Backend Kit's Hygiene Base.
- No Kit Update changes a Backend Repo's three files after birth.
- The Hygiene Base ignores the file of one person's own instructions to the agent.

## 3. The stack's lines

A Backend Repo's stack becomes true at one Plan Step: the one that first builds its application on that stack. Its Stack Overlay comes then (`knowledge/backbone-ideas/repo-hygiene.md` §3, *The base and the overlay*). One Backend Repo appended its stack's lines at that Plan Step. The next three wrote them by hand: nothing gave them a Stack Overlay.

**Rules:**

- The Stack Overlay is appended at the Plan Step that first builds the application on its stack.
- The Backend Kit holds a Stack Overlay for each stack a Backend Repo builds on.

## 4. Open questions

A question joins this list when work meets one, and leaves it once its answer is in the text above.

1. **How a Stack Overlay reaches a Backend Repo:** the Backend Kit holds one, and no Adapted Case gives it to a Backend Repo at that Plan Step. Its trigger: the cbc-bootstrap Agent Skill's hygiene step rewritten (`TODO.md`, the item "Decide whether the cbc-bootstrap Agent Skill points at the Spring Stack Overlay").

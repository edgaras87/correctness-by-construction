# Commit messages, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/commit-messages.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Case for commit messages.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules:
- the commit-messages manual, docs/conventions/commit-messages/README.md: from What it is for, CBC Run 3's commits held by the stop; The seats;
- the Backend Kit's commit-messages Agent Skill, delivery/container/.claude/skills/commit-messages/SKILL.md: its Types, and the scope once a repo has more than one area;
- ADR-0038, 1f: the permission gate CBC Run 3 declined.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is commit messages in the Backend Repos' Problem Domain: which part of a subject carries the signal in a repo that builds software, when its subjects are counted, and what the stop at each commit held. How a commit is written is commit messages' (`knowledge/backbone-ideas/commit-messages.md`). The Backend Kit's Adapted Case for commit messages is written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Enforcement Gate | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The type carries the signal

A Backend Repo builds software. Its changes differ in kind: a new capability, a fix, a restructuring, a test, a build change. So the type carries the signal, as commit messages has it (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*), and a release tool derives the version from the types: `feat` a minor version, `fix` a patch, a breaking change a major one.

A scope names the module or area the commit touches. A repo with one area has nothing to name.

**Rules:**

- The type names the kind of change. A change to text only, the records included, is `docs`.
- A scope names the module or area touched, once the repo has more than one.

## 3. When subjects are counted

A Backend Repo counts its subjects at each Plan Step's close, against the check's line of 70 (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*). CBC Run 3's subjects crossed 50 at every Plan Step the Maintainer Repo read, at 52 to 56 (`knowledge/problem-domain-ideas/cbc-backend-design/how-an-agent-works-in-cbc-backend-design.md` §3, *What the work showed*, A1). Each miss was a few characters, which the line of 70 passes.

**Rules:**

- Every subject on a Plan Step's branch is counted by script at the Plan Step's close.

## 4. The stop, with nobody watching

A Backend Repo is the case nobody watches (`knowledge/problem-domain-ideas/cbc-backend-design/how-an-agent-works-in-cbc-backend-design.md` §2, *The case nobody watches*). The stop at each commit reaches it as text, and no Enforcement Gate holds it. It held: CBC Run 3 declined a permission gate, and held forty-four commits on the stop's sentence alone (ADR-0038, 1f).

## 5. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

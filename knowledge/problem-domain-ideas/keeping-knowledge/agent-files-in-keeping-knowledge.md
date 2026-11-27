# Agent files, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/agent-files.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Cases for its agent files: its Entry File, its Decisions Log's form and its Tool Binding (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work).
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first source, input and not rules: the agent-arrangement manual, docs/conventions/agent-arrangement/README.md: What it is for, the handbook's evidence; The seats, The Concept Deliverer's seat; §2.3 and §2.6, this repo's Entry File; §3.4 and §3.7, this repo's Decisions Log and operator's file.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is agent files in the Maintainer Repo's Problem Domain, keeping knowledge: what its work showed, where its Entry File sits and when it is read again, and what its Decisions Log and its operator's file keep differently. Which files a repo keeps for its agent, and what goes in each, are agent files' (`knowledge/backbone-ideas/agent-files.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Decisions Log | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Plan Step Gate | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. What the work showed

The failure agent files answer was measured in the handbook, the repo that held the working arrangement before this one, now history (ADR-0038). It restated its ideas' rules in its Entry File, so they would always be in context. The Entry File grew to 98 lines, split across two files, with three copies of one rule that disagreed. It is reported here, since this repo cannot check it again (ADR-0038, 1c).

## 3. The Entry File

The Maintainer Repo's Entry File sits at the root.

The Maintainer Repo has no end, so no moment at the end of its work can read the Entry File again (`knowledge/backbone-ideas/agent-files.md` §6, *The Entry File's size*). It is read again at each Plan Step's close instead, as a closing item of the Plan Step Gate (ADR-0057).

**Rules:**

- The Entry File sits at the root.
- Every Plan Step Gate holds a closing item: the Entry File read top to bottom, each line passing the three tests again or leaving.

## 4. The Decisions Log

The Maintainer Repo receives no Backend Kit Update, so its Decisions Log holds only the changes to its own agent files. No one reads it but this repo. So an entry that follows from an ADR is one line that points at the ADR (ADR-0042).

**Rules:**

- An entry that follows from an ADR is one line pointing at it.

## 5. The operator's file

The Maintainer Repo tracks its operator's file. It has one operator, and a setting kept out of git is one no reader of the repo can see (ADR-0062). This is why it keeps in history what agent files keep out (`knowledge/backbone-ideas/agent-files.md` §10, *The operator's file*).

**Rules:**

- The operator's file is tracked.

## 6. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

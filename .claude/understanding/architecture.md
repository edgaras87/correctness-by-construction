# The architecture, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for its architecture, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/records-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: its Instruction Text, the header comment and the parts of ARCHITECTURE.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: the project-recording manual, docs/conventions/project-recording/README.md, deleted on 2026-11-27, its last state in git at 3bb95746: The seats, its item 5; ADR-0044; ADR-0068.
-->

This text says who reads each part of this repo's architecture, and when. A part no one reads goes (`knowledge/backbone-ideas/records.md` §10, *The architecture*), so each part names its reader.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| CBC Run | `docs/models/tiers.md` §2.3, *Run Repos* |
| Delivery Note | `docs/conventions/exchange/` §3.7, *The Delivery Note* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Its parts and their readers

| Part | What it holds | Who reads it, and when |
|---|---|---|
| *Overview* | the repo in one view | a newcomer, after the README |
| *What is stated here* | each text that states a fact, beside what is made from it; the ideas; the delivery by group | whoever changes such a text, for what is made from it |
| *The delivery and the CBC Runs* | the table of CBC Runs, each by both its names | the agent writing a Delivery Note |
| *What must stay true* | each rule, where it is stated and what holds it | the reviewer, at commit review |
| *Codemap* | where each thing lives | anyone looking |

**Rules:**

- A new part names its reader when it is added.
- A part whose reader no longer reads it goes.
- The words the architecture uses are a record of their own, `docs/glossary.md`, never a part of it.
- A line found wrong and not fixed at once is a known issue in `TODO.md` until it is.

## 3. Open

None now. A point joins this list when work meets one.

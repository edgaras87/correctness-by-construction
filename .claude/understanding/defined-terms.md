# Defined Terms, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Defined Terms, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: .claude/rules/defined-terms.md, its Instruction Text, a Paths Rule.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Why it carries no Foundation Line: docs/conventions/conventions/ §1.3, The Foundation Line.
-->

This text says how this repo keeps its Defined Terms while its texts stand in two sets, the layers model's and today's. The Paths Rule built on it is what the agent acts on.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Glossary Name | `docs/conventions/writing/` §2, *Why each rule*, rule 9 |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Paths Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Two sets of texts

While the rewrite runs (ADR-0082), this repo's texts stand in two sets. The layers model's set is every text under `knowledge/` or `.claude/understanding/`, and every Agent Skill or Agent Rule built on one there. Defined Terms govern it. Writing rule 9 and the glossary govern the rest (`docs/conventions/writing/` §2, *Why each rule*, rule 9). The agent reads both sets in one session, so a Defined Term and a Glossary Name meet.

**Rules:**

- A text's set is where it sits, not what it is about.

## 3. Twin names

About 20 Defined Terms of the layers model name what a Glossary Name already names. The problem file lists each pair (`temp/common-ground/common-ground-problem.md` §2.2, *Today and what to check*, its table). A pair is one thing with two names, which the Backbone Idea forbids where texts are read together (`knowledge/backbone-ideas/defined-terms.md` §3, *One meaning per Defined Term*). Here it is borne for a while: each name stays in its own set, and the rewrite retires the Glossary Name.

**Rules:**

- A text in the layers model's set uses the Defined Term, never its twin. It borrows a Glossary Name only for a thing with no Defined Term.
- A twin listed in the problem file is no collision.

## 4. The collision search

The Problem Domain Idea searches every text a new Defined Term may be read with (`knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` §5, *Finding a definition*). Here that is both sets.

**Rules:**

- Before a Defined Term is defined, its bold mark is searched for under `knowledge/` and `.claude/understanding/`, and its words in `docs/glossary.md` and the delivered Glossary Names, `delivery/*/docs/glossary/`.
- A hit that is not a listed twin is a collision, and one of the two names changes.

## 5. Why a Paths Rule

The Instruction Text is a Paths Rule on the layers model's folders. Its moment is when the agent reads or writes a text there and meets a Defined Term. Without it, the agent opens a home whole to find one definition, or reads a Defined Term as English (ADR-0085, its consequences). A Paths Rule loads when a file under its paths is read (`docs/conventions/agent-arrangement/` §5.6, *Rules files*):

- an Agent Rule loaded in every session would cost every session that never opens the set;
- an Agent Skill fires only when the agent notices its moment, and the failure here is not noticing: a Defined Term read as English.

**Rules:**

- A text written in the set before the agent reads any file there is written without the Paths Rule. It is checked against it once the Paths Rule has loaded.

# Visual comparison

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules: the visual-comparison manual, docs/conventions/visual-comparison/README.md, deleted on 2026-11-27, its last state in git at e8edf8f3: its opening; What it is for, without its case; §1; §2; What this does not cover, as the neighbours below (PLAN.md, the visual-comparison manual's Plan Step, decisions A to C). The decisions behind them: ADR-0028; ADR-0030.
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- It names no file that carries its rules to the agent: that is each Adapted Case's.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says how the way a structure is shown is chosen: a picture, a table or a plain list. It names no Problem Domain: each Problem Domain Idea adapted from it says which notations its own repos use.

Its neighbours: a choice that is not about how something is shown is decided while building, and corrected at a boundary (`knowledge/backbone-ideas/commit-sets.md` §5, *At each boundary*); whether a picture may carry a fact the prose does not is decided by the text that holds the picture.

## 1. Its Defined Terms

None of its own.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. What a comparison is

The way a structure is shown is chosen by what a reader gets from it, not by what the writer expected a notation to do. A comparison chooses it. Every candidate is built and rendered, and judged against what the reader must get.

A comparison is that, plus the one failure only a picture has: a notation that asserts something the writer did not mean. A table can be unhelpful. A picture can be wrong in a way the reader will believe, because a drawing makes a claim by how it is drawn, before anyone reads a label.

Its subject is a question, not a candidate: how is this shown? "Not a picture" is one of its answers. A subject that named a picture would keep the table and the numbered list out of the set.

**Rules:**

- One comparison is made for each thing being shown.
- Every candidate is built and rendered, and judged against what the reader must get.

## 3. A non-picture in the set

The candidate set holds at least one thing that is not a picture. Otherwise a picture wins by construction, and the comparison cannot return "no picture", which is a real result.

**Rules:**

- The candidate set holds at least one candidate that is not a picture.

## 4. Deciding by the render

The render decides, not the reasoning about the render. What a notation drops, or asserts by accident, shows only once it is drawn. Its documentation does not say it ahead.

**Rules:**

- A candidate is judged by its render.

## 5. Fighting a notation

Fighting a notation is losing. A candidate that needs tricks has already failed: invisible links, spacer nodes, nodes declared out of the order of their meaning. The next person to edit it will not know which parts the layout depends on.

**Rules:**

- A candidate that needs tricks to lay it out has lost.

## 6. The buildable notations

What can be built depends on where a repo's texts are read. The constraint is not aesthetic.

Where a repo holds to plain text that renders on GitHub and in the IDE with no build step, two notations meet it: Mermaid and Unicode box drawing. PlantUML, Graphviz and D2 need a render step or a plugin. A committed SVG renders, but is not text anyone can read in a diff.

Each Problem Domain Idea says whether its repos hold to that constraint.

**Rules:**

- A candidate is built in a notation that meets its repo's constraint on where texts are read.
- Under plain text that renders with no build step, those notations are Mermaid and Unicode box drawing.

## 7. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

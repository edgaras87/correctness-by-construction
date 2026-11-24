# Change

<!--
What it is: a Backbone Idea (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer), and its one home. Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/layers-of-knowledge.md, the layers and what each holds. It points there, and never retells it.
What stands on it: knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md, its Problem Domain Idea of keeping knowledge. Each Problem Domain Idea points here, and never retells it. And, until it is redrawn, the layers of knowledge's picture, whose arrows but worked by are explained here (ADR-0088, decision 8).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: ADR-0088. Its §2 to §4 were the layers of knowledge's §4, How knowledge moves, moved here whole but the arrow worked by, and the arrow change renamed fit.
How it is edited:
- It gives no example from one Problem Domain's work, as the layers of knowledge gives none.
- As in the layers of knowledge, a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says what a change to knowledge is, in any Problem Domain: how knowledge enters the layers, and how it moves between them. The layers, and what each holds, are the layers of knowledge's (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*). How a Problem Domain's changes travel is its own Change idea.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Knowledge on Trial | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. What a change is

A change is knowledge entering the layers, or moving in them: a text found not to fit, or knowledge no text holds yet. It can start in work, or at an idea, at layer 1 or 2.

Knowledge moves along the arrows of the layers of knowledge's picture. Going down, an idea is adapted and taken to where it is used. Going up, what the work taught is judged, and lands in the layer it holds for.

## 3. How the layers fill

Knowledge can enter at any layer. Work meets something new and changes the Adapted Case it works by, or writes one, on trial, where none covers it: Knowledge on Trial. An idea to test may be written first as understanding, in a Problem Domain Idea or in layer 1, and Adapted Cases are then written from it. While a text is written, a part of it may show as the idea above it, and is set apart there: a Problem Domain Idea's backbone in layer 1, or the part of an Adapted Case true for its whole Problem Domain, in its Problem Domain Idea.

**Rules:**

- A text is written in the layer it belongs to, wherever its knowledge entered.
- A lesson from work goes as high as it is true.
- A guess is written as open, with the trigger that tests it. Only what follows from a text already written is stated as a rule.

## 4. The arrows

- **adapt,** layer 1 to layer 2, and layer 2 to layer 3, or to layer 4 for a project's own Adapted Case: a text is written from the idea above it, narrowed to its need, with what the need adds. A part left out on purpose is marked, with why (§4's **Rules**, *Narrowing, never shrinking*).
- **lesson,** layer 3 to layer 2, layer 2 to layer 1, and a project's own Adapted Case in layer 4 to layer 2: a lesson goes up as far as it is true (§3).
- **set apart,** layer 3 to layer 2, layer 2 to layer 1, and layer 4 to layer 3, or to layer 2 from a project's own Adapted Case: while a text is written, a part of it shows as true without what the text adds. The part is written in the layer above, and the text is then adapted from it.
- **fit,** layer 4 to layer 3: where the work shows the Adapted Case does not fit, the work fits it to what happened. Where no Adapted Case covers the work, the project writes its own, on trial (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.4, *The layer of work*). The change is judged, and goes up the arrow *lesson* as far as it holds.

The arrow *worked by*, layer 3 to layer 4, is the layers of knowledge's: it is what layer 4 holds, not a change (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.4, *The layer of work*).

**Rules:**

- When an idea changes, each text built on it is checked, and changes if it must.
- **Narrowing, never shrinking.** An idea changes only where it is wrong for every text built on it. A part that does not fit one text built on it stays in the idea: that text leaves the part out, and marks that it did, with why. The mark is written when the exclusion is decided, never listed ahead. A change to a marked part reopens its why.
- A lesson is reworded to name no Adapted Case at layer 2, and no Problem Domain at layer 1.

## 5. A Problem Domain's Change

Each Problem Domain adapts this idea to how its own changes travel, between its projects and the texts they work by, in a Problem Domain Idea of its own.

## 6. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **A lesson the layer above already holds:** a change is true beyond its own Adapted Case, but the idea above already says it, so nothing comes down the arrow *adapt*. How do the other Adapted Cases built on that idea learn of it? Does whoever judges the change decide this, and tell each one? The change work answers it.
2. **A change that starts at an idea:** when an idea at layer 1 or 2 is written new, or changes, is it carried to every layer below it together, or one layer at a time? A first guess: together, once the idea is clear. Its trigger: depth c simulated, the first such change (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it").
3. **Other starts:** a lesson from the work of the repo that keeps the texts, Knowledge on Trial handed over at a project's close, and new knowledge from the human. Does each travel as a change found in work does? Its trigger: the first change from each.

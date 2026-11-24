# 0088. Change, an idea of its own

Date: 2026-11-24
Status: Proposed, opened under the commit plan for the Change split

## Context

The Backend Kit's Adapted Cases for keeping knowledge need a Problem Domain Idea of CBC backend design above them (ADR-0087, decision 3). Planned as "The layers of knowledge, in CBC backend design" (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2), its draft held only change: how a Backend Repo changes a Kit Copy, and how it takes a Kit Update.

The Maintainer Repo's layers document holds two subjects that change for different reasons: where the layers are kept (its §3), and how a change travels (its §4.2 and §4.3, about 200 lines). The Maintainer Repo's three Adapted Cases for a change hang off §4.2. A change to how the layers are kept would read as a change to their parent, and set off a survey of them. The Change move of 2026-11-23 put Change inside the layers document without weighing an idea of its own.

A Problem Domain Idea is a Backbone Idea adapted to one Problem Domain, and its title is the layer-1 title, ", in" and its Problem Domain (the layers document's §3.5, its **Rules**).

The reviewer sees Change as any change to knowledge, wherever it starts: a Copy Change, a lesson from the Maintainer Repo's own work, a new idea, a change made straight to layer 2 or layer 1. Only one case has been worked: a Copy Change, at depth b.

## Options considered

- **The Backend Repo's parent named "The layers of knowledge, in CBC backend design".** Rejected: it holds only change, and a later change to how layers work would read as touching the Backend Kit's Adapted Cases for keeping knowledge.
- **Change kept inside the Maintainer Repo's layers document.** Rejected: two subjects in one parent, as the context says.
- **"Change, in …" as a second adaptation of the layers of knowledge.** Rejected: it breaks the title rule, and Change is about more than the layers.
- **A Backbone Idea Change that takes the general layers document's rules on change now.** Rejected for now: one case is worked, and depth c, the first change that starts at an idea, is not yet simulated. Whether they move is an open question of the Backbone Idea.

## Decision

1. **Change is a Backbone Idea,** `knowledge/backbone-ideas/change.md`: any change to knowledge, wherever it starts. It stands on the layers of knowledge, and points at its rules, never retelling them.
2. **It holds only what is written already.** The reviewer's guesses are its open questions, each with its trigger: a change that starts at an idea, carried to all layers together; the other sources; whether the layers document's rules on change move into it.
3. **Change, in keeping knowledge,** `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`: the Maintainer Repo's §4.2 and §4.3 moved out of its layers document, with the Defined Terms of a change's travel and its open questions on change. The layers document keeps the layers, the arrows and the picture, and points at it.
4. **Change, in CBC backend design,** `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md`: the parent of the Backend Kit's Adapted Cases for keeping knowledge.
5. **Each Adapted Case for a change names its own Change idea as its parent.**

## Consequences

- Every pointer to the layers document's §4.2 or §4.3 follows the move, by the rename grep.
- The Defined Terms of a change's travel have a new home, and every Borrow Table listing them follows.
- Depth c answers the Backbone Idea's first open question (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it").
- "The layers of knowledge, in CBC backend design" is kept as planned, or dropped, when Change, in CBC backend design lands.

# 0088. Change, an idea of its own

Date: 2026-11-24
Status: Proposed, opened under the commit plan for the Change split

## Context

The Backend Kit's Adapted Cases for keeping knowledge need a Problem Domain Idea of CBC backend design above them (ADR-0087, decision 3). Planned as "The layers of knowledge, in CBC backend design" (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3.2.2), its draft held only change: how a Backend Repo changes a Kit Copy, and how it takes a Kit Update.

The Maintainer Repo's layers document holds two subjects that change for different reasons: where the layers are kept (its §3), and how a change travels (its §4.2 and §4.3, about 200 lines). The Maintainer Repo's three Adapted Cases for a change hang off §4.2. A change to how the layers are kept would read as a change to their parent, and set off a survey of them. The Change move of 2026-11-23 put Change inside the layers document without weighing an idea of its own.

A Problem Domain Idea is a Backbone Idea adapted to one Problem Domain, and its title is the layer-1 title, ", in" and its Problem Domain (the layers document's §3.5, its **Rules**).

The reviewer sees Change as any change to knowledge, wherever it starts: a Copy Change, a lesson from the Maintainer Repo's own work, a new idea, a change made straight to layer 2 or layer 1. Only one case has been worked: a Copy Change, at depth b.

The general layers document's §4, *How knowledge moves*, holds how knowledge enters the layers, the arrows between them, and the rules on moving. Its arrow named *change*, layer 4 to layer 3, reads as if change came only from a project's work.

## Options considered

- **The Backend Repo's parent named "The layers of knowledge, in CBC backend design".** Rejected: it holds only change, and a later change to how layers work would read as touching the Backend Kit's Adapted Cases for keeping knowledge.
- **Change kept inside the Maintainer Repo's layers document.** Rejected: two subjects in one parent, as the context says.
- **"Change, in …" as a second adaptation of the layers of knowledge.** Rejected: it breaks the title rule, and Change is about more than the layers.
- **A Backbone Idea Change that leaves the general layers document's §4 where it is,** until depth c is simulated. Rejected: moving a rule is not writing a new one, and depth c will change these rules. Moved first, each line changes once, in its home. Left, the arrow named *change* keeps reading as if change came only from work.
- **Change as one section of the layers of knowledge, each Change idea at layer 2 adapted from that section.** Rejected: a text's header lists what stands on it by document, so a change to the layers part would flag the Change ideas; and the title rule names a layer-2 idea after a document, not a section. It would keep the arrows next to the picture that draws them, and move less now.
- **A picture in Change repeating the layers picture with its arrows.** Rejected: two pictures of the same thing drift. Each picture shows one thing.

## Decision

1. **Change is a Backbone Idea,** `knowledge/backbone-ideas/change.md`: any change to knowledge, wherever it starts. It stands on the layers of knowledge.
2. **The boundary:** a sentence still true if nothing ever changed belongs to the layers; one about something added, moved or changed belongs to Change. Change holds how a text is checked when an idea above it changes; the layers hold what that text must hold.
3. **Change takes the general layers document's §4:** how the layers fill, the arrows, their rules, and its open question on change. *worked by* stays in the layers, as part of what layer 4 holds. The arrow named *change* is renamed in Change. The layers document keeps a short section pointing at Change.
4. **Change holds only what is written already.** The reviewer's guesses are its open questions, each with its trigger: a change that starts at an idea, carried to all layers together; the other starts.
5. **Change, in keeping knowledge,** `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`, takes the Maintainer Repo's layers document's §4 whole: the arrows between the repos, how a change travels, the Maintainer Repo's own lessons, with the Defined Terms of a change's travel and its open questions on change. The layers document keeps the layers and where each is kept, and points at it.
6. **Change, in CBC backend design,** `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md`: the parent of the Backend Kit's Adapted Cases for keeping knowledge.
7. **Each Adapted Case for a change names its own Change idea as its parent.**
8. **Each picture shows one thing,** chosen by the visual-comparison Agent Skill: the layers pictures what is where, the Change pictures how knowledge moves. Until they are drawn, the layers pictures keep their arrows, a key line naming Change.

## Consequences

- Every pointer into either layers document's §4 follows the move, by the rename grep.
- The Defined Terms of a change's travel have a new home, and every Borrow Table listing them follows.
- Depth c answers the Backbone Idea's first open question, and changes its rules in their home (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it").
- "The layers of knowledge, in CBC backend design" is kept as planned, or dropped, when Change, in CBC backend design lands.

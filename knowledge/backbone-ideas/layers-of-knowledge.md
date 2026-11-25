# The layers of knowledge

<!--
What it is: a Backbone Idea (§3.1), and its one home.
What stands on it: knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md, its Problem Domain Idea of keeping knowledge. knowledge/backbone-ideas/change.md, a Backbone Idea standing on it. Each Problem Domain Idea points here, and never retells it.
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
How it is edited:
- The picture and the text are checked against each other at every change: each label in the picture is explained in the text, each part the text names is in the picture, and what the text says moves where matches the arrows. Until the picture is redrawn, its arrows but *worked by* are explained in Change, knowledge/backbone-ideas/change.md §4 (ADR-0088, decision 8).
- It gives no example from one Problem Domain's work. §1 names one kind of project only to show what a Problem Domain is.
- A trial, here only: a section's rules close it, in a last paragraph marked Rules, and govern that section. A rule may be split across a section and its subsections.
-->

This document says what the layers of knowledge are, in any Problem Domain, and what each holds. How knowledge enters them and moves between them is Change's (`knowledge/backbone-ideas/change.md`). It names no repo: each Problem Domain's instance says where its layers are kept and how its texts travel.

## 1. Its Defined Terms

- **Adapted Case:** a Problem Domain Idea written for one piece of work, or for what all of a project's work uses, as its Adapted Understanding Text, with the Instruction Texts built on it.
- **Adapted Understanding Text:** the Understanding Text of an Adapted Case. It says why the Adapted Case's Instruction Texts are as they are.
- **Backbone Idea:** an idea bound to no Problem Domain: its backbone, without the details a Problem Domain adds.
- **Instruction Text:** a text built on an Understanding Text, to apply it: what the agent acts on.
- **Knowledge on Trial:** new knowledge used before it is judged: a way of working, an Understanding Text, or a text's form.
- **Problem Domain:** a kind of project, set by the problem its projects share, such as CBC backend design. A different problem is a different Problem Domain.
- **Problem Domain Idea:** a Backbone Idea adapted to one Problem Domain, with what the Problem Domain adds.
- **Understanding Text:** a text that holds what is known, and how it is understood.

## 2. The picture

```
          ┌───────────────────────────────────────────────────────────────────────────────────┐
          │ Backbone Ideas, bound to no Problem Domain:                                       │
          │ understanding                                                                     │
 Layer 1  │   ┌──────────┐            ┌──────────┐            ┌──────────┐                    │
          │   │ Idea 1   │            │ Idea 2   │            │ Idea 3   │                    │
          │   └──────────┘            └──────────┘            └──────────┘                    │
          └───────────────────────────────────────────────────────────────────────────────────┘
                │      ▲       ▲                │      ▲       ▲
                │      │       │                │      │       │
              adapt lesson set apart          adapt lesson set apart
          ┌╌╌╌╌╌│╌╌╌╌╌╌│╌╌╌╌╌╌╌│╌╌╌╌╌╌╌┐  ┌╌╌╌╌╌│╌╌╌╌╌╌│╌╌╌╌╌╌╌│╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐
          ╎     ▼      │       │       ╎  ╎     ▼      │       │                              ╎
          ╎ ┌────────────────────────┐ ╎  ╎ ┌───────────────────────────────────────────────┐ ╎
          ╎ │ Problem Domain Ideas:  │ ╎  ╎ │ Problem Domain Ideas: understanding           │ ╎
          ╎ │ understanding          │ ╎  ╎ │                                               │ ╎
          ╎ │ ┌───────────────┐      │ ╎  ╎ │ ┌───────────────┐  ┌───────────────┐          │ ╎
 Layer 2  ╎ │ │ from Idea 1   │      │ ╎  ╎ │ │ from Idea 1   │  │ from Idea 1   │          │ ╎
          ╎ │ └───────────────┘      │ ╎  ╎ │ └───────────────┘  └───────────────┘          │ ╎
          ╎ │ ┌───────────────┐      │ ╎  ╎ │                                               │ ╎
          ╎ │ │ from Idea 2   │      │ ╎  ╎ │                                               │ ╎
          ╎ │ └───────────────┘      │ ╎  ╎ │                                               │ ╎
          ╎ └────────────────────────┘ ╎  ╎ └───────────────────────────────────────────────┘ ╎
          ╎     │      ▲       ▲       ╎  ╎     │      ▲       ▲        │      ▲       ▲      ╎
          ╎   adapt lesson set apart   ╎  ╎   adapt lesson set apart  adapt lesson set apart  ╎
          ╎     ▼      │       │       ╎  ╎     ▼      │       │        │      │       │      ╎
          ╎ ┌────────────────────────┐ ╎  ╎ ┌──────────────────────┐    │      │       │      ╎
          ╎ │ Adapted Cases:         │ ╎  ╎ │ Adapted Cases:       │    │      │       │      ╎
 Layer 3  ╎ │ understanding and      │ ╎  ╎ │ understanding and    │    │      │       │      ╎
          ╎ │ instructions           │ ╎  ╎ │ instructions         │    │      │       │      ╎
          ╎ └────────────────────────┘ ╎  ╎ └──────────────────────┘    │      │       │      ╎
          ╎     │        ▲       ▲     ╎  ╎     │        ▲       ▲      │      │       │      ╎
          ╎ worked by   fit  set apart ╎  ╎ worked by   fit  set apart  │      │       │      ╎
          ╎     ▼        │       │     ╎  ╎     ▼        │       │      ▼      │       │      ╎
          ╎ ┌────────────────────────┐ ╎  ╎ ┌───────────────────────────────────────────────┐ ╎
          ╎ │ a project: its work,   │ ╎  ╎ │ a project: its work, by understanding and     │ ╎
          ╎ │ by copies of its       │ ╎  ╎ │ instructions:                                 │ ╎
          ╎ │ Problem Domain's       │ ╎  ╎ │ ┌───────────────────┐  ┌────────────────────┐ │ ╎
          ╎ │ Adapted Cases:         │ ╎  ╎ │ │ copies of its     │  │ its own            │ │ ╎
 Layer 4  ╎ │ understanding and      │ ╎  ╎ │ │ Problem Domain's  │  │ Adapted Cases      │ │ ╎
          ╎ │ instructions           │ ╎  ╎ │ │ Adapted Cases     │  │                    │ │ ╎
          ╎ │                        │ ╎  ╎ │ └───────────────────┘  └────────────────────┘ │ ╎
          ╎ └────────────────────────┘ ╎  ╎ └───────────────────────────────────────────────┘ ╎
          ╎ Problem Domain A           ╎  ╎ Problem Domain B                                  ╎
          └╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘  └╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘
```

Key: the arrows but *worked by* are Change's, and explained there (`knowledge/backbone-ideas/change.md` §4, *The arrows*). Each dashed frame holds one Problem Domain: its Problem Domain Ideas, its set of Adapted Cases, and a project of it. Each Problem Domain Idea names the Backbone Idea it is adapted from (§3.2). The arrows on the right serve a project's own Adapted Case, written where none of its Problem Domain's covers a piece of its work (§3.4). Problem Domain A's project has none.

## 3. The layers

Knowledge sits in four layers. The higher the layer, the closer its text is to an idea's backbone.

Each Problem Domain adapts the Backbone Ideas it needs to its own problem.

Text comes in two kinds, Understanding Texts and Instruction Texts, and the kind runs across the layers. Layers 1 and 2 hold understanding only. Layers 3 and 4 each hold understanding and instructions.

### 3.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas. A Backbone Idea may stand under several Problem Domain Ideas, one, or none, as the picture's Ideas 1, 2 and 3 do. A Backbone Idea with none is adapted by no Problem Domain yet, and is kept as understanding.

**Rules:**

- It holds no instruction (§3): an instruction applies an idea to some piece of work, and work always belongs to a Problem Domain.
- A Backbone Idea may stand on another: it points at it, and never retells it.

### 3.2 The Problem Domain layer

Layer 2 holds a Problem Domain's understanding, as Problem Domain Ideas. In each, the backbone stays; its details differ.

One Backbone Idea may be adapted more than once in the same Problem Domain, as the picture's Idea 1 is. Each Problem Domain that needs a Backbone Idea writes its own adaptation, never one shared with other Problem Domains.

**Rules:**

- Each adaptation is a Problem Domain Idea of its own: written whole, read alone, and changed alone. A change to one does not reach the other.
- A Problem Domain Idea names the Problem Domain it is adapted to, and the Backbone Idea it is adapted from.
- Text shared by several Problem Domains, but not by all, is written into each one's own adaptation. Only what is true for every Problem Domain goes up to layer 1.
- A Defined Term is the one exception: one several Problem Domains share is defined in one adaptation and borrowed by the others. A change to it is checked against every text that borrows it (`knowledge/backbone-ideas/defined-terms.md` §4, *Where it is defined*).

### 3.3 The Adapted Case layer

Layer 3 holds Adapted Cases, one set for each Problem Domain. An Adapted Case holds both kinds of text: its Adapted Understanding Text, and the Instruction Texts built on it.

A Problem Domain's Adapted Cases are true for every project of it, and name none. Its set is written from that Problem Domain's own ideas. An Adapted Case's owner says its layer: a Problem Domain's is layer 3, and a project's own is layer 4 (§3.4).

**Rules:**

- An Adapted Case is tied to another only through the nearest idea above them both: their Problem Domain Idea, if they share one, or else their Backbone Idea. A change to one reaches another only when it goes up the arrow *lesson* to that idea and comes down the arrow *adapt*: it is then true beyond its own Adapted Case.

### 3.4 The layer of work

Layer 4 is one project: the work it does, and the texts it works by. Those texts are its copies of its Problem Domain's Adapted Cases, and its own Adapted Cases, written where none of its Problem Domain's covers a piece of its work. Its own are true for it alone. A project whose Problem Domain has no set yet works by its own alone. Work is done by an Adapted Case, kept where the work is done, or as a copy there: the picture's arrow *worked by*, layer 3 to layer 4. What the work teaches changes the text it was done by, where the text does not fit, by the arrow *fit*.

**Rules:**

- A text true only for its project stays in layer 4. A part of it true for every project of its Problem Domain goes up to layer 3, by the arrow *set apart*.
- A project's own Adapted Case is written from the Problem Domain Idea above it, on the arrow *adapt*.

## 4. How knowledge moves

How knowledge enters the layers and moves between them, and the picture's arrows but *worked by*, are Change's (`knowledge/backbone-ideas/change.md`).

## 5. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **When a second adaptation is worth it:** how differently must a Backbone Idea be understood in one Problem Domain before two Problem Domain Ideas are clearer than one? Practice decides (§3.2).
2. **A second adaptation or a second Adapted Case:** where does a second Problem Domain Idea end, and a second Adapted Case of one Problem Domain Idea begin?

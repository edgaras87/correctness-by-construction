# The layers of knowledge, in general

<!--
What it is: a Backbone Idea (§2.1), and its one home.
What stands on it: temp/common-ground/knowledge-layers.md, the Maintainer Repo's Problem Domain Idea. Each Problem Domain Idea points here, and never retells it.
Its place in the repo: decided with that document's.
How it is edited:
- The picture and the text are checked against each other at every change: each label in the picture is explained in the text, each part the text names is in the picture, and what the text says moves where matches the arrows.
- It gives no example from one Problem Domain's work. §2 names one kind of project only to show what a Problem Domain is.
- A trial, here only: a section's rules close it, in a last paragraph marked Rules, and govern that section. A rule may be split across a section and its subsections.
-->

This document says what the layers of knowledge are, in any Problem Domain, and how knowledge moves between them. It names no repo: each Problem Domain's instance says where its layers are kept and how its texts travel.

## 1. The picture

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
          ╎ worked by change set apart ╎  ╎ worked by change set apart  │      │       │      ╎
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

Key: each dashed frame holds one Problem Domain: its Problem Domain Ideas, its set of Adapted Cases, and a project of it. Each Problem Domain Idea names the Backbone Idea it is adapted from (§2.2). The arrows on the right serve a project's own Adapted Case, written where none of its Problem Domain's covers a piece of its work (§2.4). Problem Domain A's project has none.

## 2. The layers

Knowledge sits in four layers. The higher the layer, the closer its text is to an idea's backbone.

A **Problem Domain** is a kind of project, set by the problem its projects share, such as CBC backend design. Each Problem Domain adapts the Backbone Ideas it needs to its own problem. A different problem is a different Problem Domain.

Text comes in two kinds, and the kind runs across the layers. An **Understanding Text** holds what is known, and how it is understood. An **Instruction Text** is built on an Understanding Text, to apply it: what the agent acts on. Layers 1 and 2 hold understanding only. Layers 3 and 4 each hold understanding and instructions.

### 2.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas. A **Backbone Idea** is an idea bound to no Problem Domain: its backbone, without the details a Problem Domain adds. It may stand under several Problem Domain Ideas, one, or none, as the picture's Ideas 1, 2 and 3 do. A Backbone Idea with none is adapted by no Problem Domain yet, and is kept as understanding.

**Rules:**

- It holds no instruction (§2): an instruction applies an idea to some piece of work, and work always belongs to a Problem Domain.
- A Backbone Idea may stand on another: it points at it, and never retells it.

### 2.2 The Problem Domain layer

Layer 2 holds a Problem Domain's understanding, as Problem Domain Ideas. A **Problem Domain Idea** is a Backbone Idea adapted to one Problem Domain, with what the Problem Domain adds. The backbone stays; its details differ.

One Backbone Idea may be adapted more than once in the same Problem Domain, as the picture's Idea 1 is. Each Problem Domain that needs a Backbone Idea writes its own adaptation, never one shared with other Problem Domains.

**Rules:**

- Each adaptation is a Problem Domain Idea of its own: written whole, read alone, and changed alone. A change to one does not reach the other.
- A Problem Domain Idea names the Problem Domain it is adapted to, and the Backbone Idea it is adapted from.
- Text shared by several Problem Domains, but not by all, is written into each one's own adaptation. Only what is true for every Problem Domain goes up to layer 1.

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases, one set for each Problem Domain. An **Adapted Case** is a Problem Domain Idea written for one piece of work, or for what all of a project's work uses, as its **Adapted Understanding Text**, with the Instruction Texts built on it. Its Adapted Understanding Text says why its Instruction Texts are as they are. So it holds both kinds of text.

A Problem Domain's Adapted Cases are true for every project of it, and name none. Its set is written from that Problem Domain's own ideas. An Adapted Case's owner says its layer: a Problem Domain's is layer 3, and a project's own is layer 4 (§2.4).

**Rules:**

- An Adapted Case is tied to another only through the nearest idea above them both: their Problem Domain Idea, if they share one, or else their Backbone Idea. A change to one reaches another only when it goes up the arrow *lesson* to that idea and comes down the arrow *adapt*: it is then true beyond its own Adapted Case.

### 2.4 The layer of work

Layer 4 is one project: the work it does, and the texts it works by. Those texts are its copies of its Problem Domain's Adapted Cases, and its own Adapted Cases, written where none of its Problem Domain's covers a piece of its work. Its own are true for it alone. A project whose Problem Domain has no set yet works by its own alone. What the work teaches changes the text it was done by, where the text does not fit.

**Rules:**

- A text true only for its project stays in layer 4. A part of it true for every project of its Problem Domain goes up to layer 3, by the arrow *set apart*.
- A project's own Adapted Case is written from the Problem Domain Idea above it, on the arrow *adapt*.

## 3. How knowledge moves

Knowledge moves along the picture's arrows. Going down, an idea is adapted and taken to where it is used. Going up, what the work taught is judged, and lands in the layer it holds for.

### 3.1 How the layers fill

Knowledge can enter at any layer. Work meets something new and changes the Adapted Case it works by, or writes one, on trial, where none covers it. New knowledge used before it is judged is **Knowledge on Trial**: a way of working, an Understanding Text, or a text's form. An idea to test may be written first as understanding, in a Problem Domain Idea or in layer 1, and Adapted Cases are then written from it. While a text is written, a part of it may show as the idea above it, and is set apart there: a Problem Domain Idea's backbone in layer 1, or the part of an Adapted Case true for its whole Problem Domain, in its Problem Domain Idea.

**Rules:**

- A text is written in the layer it belongs to, wherever its knowledge entered.
- A lesson from work goes as high as it is true.
- A guess is written as open, with the trigger that tests it. Only what follows from a text already written is stated as a rule.

### 3.2 The arrows

- **adapt,** layer 1 to layer 2, and layer 2 to layer 3, or to layer 4 for a project's own Adapted Case: a text is written from the idea above it, narrowed to its need, with what the need adds. A part left out on purpose is marked, with why (§3.2's **Rules**, *Narrowing, never shrinking*).
- **lesson,** layer 3 to layer 2, layer 2 to layer 1, and a project's own Adapted Case in layer 4 to layer 2: a lesson goes up as far as it is true (§3.1).
- **set apart,** layer 3 to layer 2, layer 2 to layer 1, and layer 4 to layer 3, or to layer 2 from a project's own Adapted Case: while a text is written, a part of it shows as true without what the text adds. The part is written in the layer above, and the text is then adapted from it.
- **worked by,** layer 3 to layer 4: work is done by an Adapted Case, kept where the work is done, or as a copy there.
- **change,** layer 4 to layer 3: where the work shows the Adapted Case does not fit, the work changes it. Where no Adapted Case covers the work, the project writes its own, on trial (§2.4). The change is judged, and goes up the arrow *lesson* as far as it holds.

**Rules:**

- When an idea changes, each text built on it is checked, and changes if it must.
- **Narrowing, never shrinking.** An idea changes only where it is wrong for every text built on it. A part that does not fit one text built on it stays in the idea: that text leaves the part out, and marks that it did, with why. The mark is written when the exclusion is decided, never listed ahead. A change to a marked part reopens its why.
- A lesson is reworded to name no Adapted Case at layer 2, and no Problem Domain at layer 1.

## 4. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **When a second adaptation is worth it:** how differently must a Backbone Idea be understood in one Problem Domain before two Problem Domain Ideas are clearer than one? Practice decides (§2.2).
2. **A second adaptation or a second Adapted Case:** where does a second Problem Domain Idea end, and a second Adapted Case of one Problem Domain Idea begin?
3. **A lesson the layer above already holds:** a change is true beyond its own Adapted Case, but the idea above already says it, so nothing comes down the arrow *adapt*. How do the other Adapted Cases built on that idea learn of it? Does whoever judges the change decide this, and tell each one? The change work answers it.

# The layers of knowledge, in general

<!--
What it is: a Backbone Idea (§2.1), and its one home.
What stands on it: temp/common-ground/knowledge-layers.md, the Maintainer Repo's Work Domain Idea. Each Work Domain Idea points here, and never retells it.
Its place in the repo: decided with that document's.
How it is edited:
- The picture and the text are checked against each other at every change: each label in the picture is explained in the text, each part the text names is in the picture, and what the text says moves where matches the arrows.
- It gives no example from one Work Domain's work. §2 names two sorts of work only to show what a Work Domain is.
- A trial, here only: a section's rules close it, in a last paragraph marked Rules, and govern that section. A rule may be split across a section and its subsections.
-->

This document says what the layers of knowledge are, in any Work Domain, and how knowledge moves between them. It names no repo: each Work Domain's instance says where its layers are kept and how its texts travel.

## 1. The picture

```
 Layer 1   ┌────────────────────────────────────────────────────┐
           │ Backbone Ideas, bound to no Work Domain:           │
           │ understanding                                      │
           │ ┌──────────────────┐    ┌──────────────────┐       │
           │ │ Idea 1           │    │ Idea 2           │       │
           │ └──────────────────┘    └──────────────────┘       │
           │ ┌──────────────────┐                               │
           │ │ Idea 3           │                               │
           │ └──────────────────┘                               │
           └────────────────────────────────────────────────────┘
                  │          ▲           ▲             │
                adapt     lesson     set apart       adapt
                  ▼          │           │             ▼
 Layer 2   ┌────────────────────────────────────────────────────┐
           │ Each Work Domain: understanding                    │
           │ ┌──────────────────┐    ┌──────────────────┐       │
           │ │ Work Domain Idea │    │ Work Domain Idea │       │
           │ │ from Idea 1      │    │ from Idea 1      │       │
           │ └──────────────────┘    └──────────────────┘       │
           │ ┌──────────────────┐                               │
           │ │ Work Domain Idea │                               │
           │ │ from Idea 2      │                               │
           │ └──────────────────┘                               │
           └────────────────────────────────────────────────────┘
                        │            ▲            ▲
                      adapt       lesson      set apart
                        ▼            │            │
 Layer 3   ┌────────────────────────────────────────────────────┐
           │ Adapted Cases                                      │
           │ an idea written for one use:                       │
           │ understanding and instructions                     │
           └────────────────────────────────────────────────────┘
                            │                 ▲
                        worked by          change
                            ▼                 │
 Layer 4   ┌────────────────────────────────────────────────────┐
           │ Work                                               │
           │ done by an Adapted Case                            │
           └────────────────────────────────────────────────────┘
```

Key: each Work Domain Idea names the Backbone Idea it is adapted from (§2.2).

## 2. The layers

Knowledge sits in four layers. The higher the layer, the closer its text is to an idea's backbone.

A **Work Domain** is a sort of work, such as keeping knowledge, or designing a backend. Each Work Domain adapts the Backbone Ideas it needs to its own work. Different work is a different Work Domain.

The model uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*).

The kind of text runs across the layers (`temp/common-ground/common-ground-problem.md` §3.3, *The kind of text*). Layers 1 and 2 hold understanding only. Layers 3 and 4 each hold understanding and instructions.

### 2.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas. A **Backbone Idea** is an idea bound to no Work Domain: its backbone, without the details a Work Domain adds. It may stand under several Work Domain Ideas, one, or none, as the picture's Ideas 1, 2 and 3 do. A Backbone Idea with none is adapted by no Work Domain yet, and is kept as understanding.

**Rules:**

- It holds no instruction (§2): an instruction applies an idea to some piece of work, and work always belongs to a Work Domain.

### 2.2 The Work Domain layer

Layer 2 holds a Work Domain's understanding, as Work Domain Ideas. A **Work Domain Idea** is a Backbone Idea adapted to one Work Domain, with what the Work Domain adds. The backbone stays; its details differ.

One Backbone Idea may be adapted more than once in the same Work Domain, as the picture's Idea 1 is.

**Rules:**

- Each adaptation is a Work Domain Idea of its own: written whole, read alone, and changed alone. A change to one does not reach the other.
- A Work Domain Idea names the Work Domain it is adapted to, and the Backbone Idea it is adapted from.

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases. An Adapted Case is an idea of layer 2 written for one use, with the Instruction Texts built on it. So it holds both kinds of text.

**Rules:**

- An Adapted Case is tied to another only through the nearest idea above them both: their Work Domain Idea, if they share one, or else their Backbone Idea. A change to one reaches another only when it goes up the arrow *lesson* to that idea and comes down the arrow *adapt*: it is then true beyond its own Adapted Case.

### 2.4 The layer of work

Layer 4 is work done by an Adapted Case. The text is the Adapted Case itself, or a copy of it where the work is done. What puts it in layer 4 is the use: the work shows where the text does not fit, and the text is changed.

## 3. How knowledge moves

Knowledge moves along the picture's arrows. Going down, an idea is adapted and taken to where it is used. Going up, what the work taught is judged, and lands in the layer it holds for.

### 3.1 How the layers fill

Knowledge can enter at any layer. Work meets something new and changes the Adapted Case it works by. An idea to test may be written first as understanding, in a Work Domain Idea or in layer 1, and Adapted Cases are then written from it. While a text is written, a part of it may show as the idea above it, and is set apart there: a Work Domain Idea's backbone in layer 1, or the part of an Adapted Case true for its whole Work Domain, in its Work Domain Idea.

**Rules:**

- A text is written in the layer it belongs to, wherever its knowledge entered.
- A lesson from work goes as high as it is true.
- Once a higher text is written, a change to it spreads down, to each text built on it.

### 3.2 The arrows

- **adapt,** layer 1 to layer 2, and layer 2 to layer 3: a text is written from the idea above it, narrowed to its need, with what the need adds. When the idea above changes, each text built on it is checked, and changes if it must. A part left out on purpose is marked, with why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*).
- **lesson,** layer 3 to layer 2, and layer 2 to layer 1: a lesson goes up as far as it is true (§3.1). It is reworded to name no Adapted Case at layer 2, and no Work Domain at layer 1.
- **set apart,** layer 3 to layer 2, and layer 2 to layer 1: while a text is written, a part of it shows as true without what the text adds. The part is written in the layer above, and the text is then adapted from it.
- **worked by,** layer 3 to layer 4: work is done by an Adapted Case, kept where the work is done, or as a copy there.
- **change,** layer 4 to layer 3: where the work shows the Adapted Case does not fit, the work changes it. The change is judged, and goes up the arrow *lesson* as far as it holds.

## 4. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **Text shared across Work Domains, but not by all:** what holds it? It fits neither one Work Domain nor layer 1.
2. **When a second adaptation is worth it:** how differently must a Backbone Idea be understood in one Work Domain before two Work Domain Ideas are clearer than one? Practice decides (§2.2).
3. **Where a skipped part is marked:** a Work Domain may leave out a part of a Backbone Idea it does not need, and the part stays in layer 1. Is it marked in the Backbone Idea, as optional, ahead of any Work Domain? Or in the Work Domain Idea that leaves it out, when it decides to, with why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*)?
4. **A lesson for one adaptation:** where does a lesson go that holds for only one of a Backbone Idea's Work Domain Ideas? And since each changes alone (§2.2), is a lesson for both written into each?
5. **A second adaptation or a second Adapted Case:** where does a second Work Domain Idea end, and a second Adapted Case of one Work Domain Idea begin?
6. **What layer 4 holds:** only work done by an Adapted Case, or also the knowledge the work makes of its own (§2.4)?
7. **A lesson the layer above already holds:** a change is true beyond its own Adapted Case, but the idea above already says it, so nothing comes down the arrow *adapt*. How do the other Adapted Cases built on that idea learn of it? Does whoever judges the change decide this, and tell each one? The change work answers it.

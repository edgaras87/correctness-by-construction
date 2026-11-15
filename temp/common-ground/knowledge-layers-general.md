# The layers of knowledge, in general

<!-- A layer-1 idea: the layers knowledge sits in, in any Work Domain, and
     how it moves between them. Its one home: each Work Domain's instance
     points here, and never retells it. What stands on it: the
     Maintainer Repo's instance,
     temp/common-ground/knowledge-layers.md. Its place in the repo is
     decided with that document's. A trial of a way of writing rules,
     here only: a section's rules close it, in a last paragraph marked
     Rules, and govern that section; a rule may be split across a
     section and its subsections. The picture and the text are
     checked against each other at every change: each label in the
     picture is explained in the text, each part the text names is in
     the picture, and what the text says moves where matches the
     arrows. -->

This document says what the layers of knowledge are, in any Work Domain, and how knowledge moves between them. It names no repo: each Work Domain's instance says where its layers are kept and how its texts travel.

## 1. The picture

```
 Layer 1   ┌────────────────────────────────────────────────────┐
           │ Bound to no Work Domain                            │
           │ ideas for any work: understanding                  │
           └────────────────────────────────────────────────────┘
                  │          ▲           ▲             │
                adapt     lesson     set apart       adapt
                  ▼          │           │             ▼
 Layer 2   ┌────────────────────────────────────────────────────┐
           │ Each Work Domain: understanding                    │
           │ ┌──────────────────┐  ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐ │
           │ │ Work Domain Idea │  ┆ Work Domain Idea Variant ┆ │
           │ └──────────────────┘  └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘ │
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

Key: a dotted box inside a layer is a Work Domain Idea Variant (§2.2.2).

## 2. The layers

Knowledge sits in four layers. The higher the layer, the closer its text is to an idea's backbone. A **Work Domain** is a sort of work, such as keeping knowledge, or designing a backend by CBC. Each Work Domain adapts the layer-1 ideas it needs to its own work.

The model uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*).

The kind of text runs across the layers (`temp/common-ground/common-ground-problem.md` §3.3, *The kind of text*). Layers 1 and 2 hold understanding only. Layers 3 and 4 each hold understanding and instructions.

### 2.1 The layer above Work Domains

Layer 1 holds ideas bound to no Work Domain: an idea's backbone, without the details a Work Domain adds. It may stand under one Work Domain Idea, several, or none: an idea kept as understanding, which no Work Domain needs yet.

**Rules:**

- It holds no instruction (§2): an instruction applies an idea to some piece of work, and work always belongs to a Work Domain.

### 2.2 The Work Domain layer

Layer 2 holds a Work Domain's understanding, in two kinds. A Work Domain Idea is the Work Domain's default (§2.2.1). A Work Domain Idea Variant is another version of it, for one situation inside the Work Domain (§2.2.2).

#### 2.2.1 Work Domain Ideas

A **Work Domain Idea** is an idea of layer 1 narrowed to one Work Domain, with what the Work Domain adds. The idea's backbone stays; its details differ. It is used everywhere in the Work Domain, except in a situation that has its own Work Domain Idea Variant.

#### 2.2.2 Work Domain Idea Variants

A **Work Domain Idea Variant** is another version of a Work Domain Idea, for one situation inside the Work Domain: the dotted box.

**Rules:**

- It is written when, in one situation, the idea itself is understood differently enough that it is clearer read and changed on its own, whole. A difference only in one use is not that: it is a second Adapted Case.
- It is written whole, adapted from the same layer-1 idea as its Work Domain Idea. Each is read whole and changed alone: a change to one does not reach the other.

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases. An Adapted Case is an idea of layer 2 written for one use, with the Instruction Texts built on it. So it holds both kinds of text.

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
- **lesson,** layer 3 to layer 2, and layer 2 to layer 1: a lesson goes up as far as it is true (§3.1). It is reworded to fit every text below the layer it enters: no single Adapted Case at layer 2, no single Work Domain at layer 1.
- **set apart,** layer 3 to layer 2, and layer 2 to layer 1: while a text is written, a part of it shows as true without what the text adds. The part is written in the layer above, and the text is then adapted from it.
- **worked by,** layer 3 to layer 4: work is done by an Adapted Case, kept where the work is done, or as a copy there.
- **change,** layer 4 to layer 3: where the work shows the Adapted Case does not fit, the work changes it. The change is judged, and goes up the arrow *lesson* as far as it holds.

## 4. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **Text shared across Work Domains, but not by all:** what holds it? It fits neither one Work Domain nor layer 1.
2. **When a Work Domain Idea Variant is worth it:** how differently must the idea be understood in one situation before a variant is clearer than the Work Domain Idea alone? Practice decides (§2.2.2).
3. **Where a skipped part is marked:** a Work Domain may leave out a part of a layer-1 idea it does not need, such as a gate, and the part stays in layer 1. Is it marked in the layer-1 idea, as optional, ahead of any Work Domain? Or in the Work Domain Idea that leaves it out, when it decides to, with why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*)?
4. **A lesson for a Work Domain Idea Variant:** where does a lesson go that holds only in a variant's situation? And since each changes alone (§2.2.2), is a lesson for both written into each?

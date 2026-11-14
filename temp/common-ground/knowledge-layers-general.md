# The layers of knowledge, in general

<!-- A layer-1 idea: the layers knowledge sits in, in any domain, and
     how it moves between them. Its one home: each domain's instance
     points here, and never retells it. Written from one domain, the
     Maintainer Repo's, so it is on trial until a second domain uses
     it (§3.1). What stands on it: the Maintainer Repo's instance,
     temp/common-ground/knowledge-layers.md. Its place in the repo is
     decided with that document's. The picture and the text are
     checked against each other at every change: each label in the
     picture is explained in the text, each part the text names is in
     the picture, and what the text says moves where matches the
     arrows. -->

This document says what the layers of knowledge are, in any domain, and how knowledge moves between them. It names no repo: each domain's instance says where its layers are kept and how its texts travel.

## 1. The picture

```
 Layer 1   ┌──────────────────────────────────────────┐
           │ Domain-agnostic                          │
           │ ideas bound to no domain: understanding  │
           └──────────────────────────────────────────┘
                    │        ▲           │
                  adapt    lesson      adapt
                    ▼        │           ▼
 Layer 2   ┌──────────────────────────────────────────┐
           │ Each domain: understanding               │
           │ ┌─────────────┐  ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐ │
           │ │ Domain Idea │  ┆ Domain Idea Variant ┆ │
           │ └─────────────┘  └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘ │
           └──────────────────────────────────────────┘
                │                     ▲
              adapt                 lesson
                ▼                     │
 Layer 3   ┌──────────────────────────────────────────┐
           │ Adapted Cases                            │
           │ an idea written for one use:             │
           │ understanding and instructions           │
           └──────────────────────────────────────────┘
                │                     ▲
            worked by               change
                ▼                     │
 Layer 4   ┌──────────────────────────────────────────┐
           │ Work                                     │
           │ done by an Adapted Case                  │
           └──────────────────────────────────────────┘
```

Key: a dotted box inside a layer is a Domain Idea Variant, written only when needed.

## 2. The layers

Knowledge sits in four layers. The higher the layer, the more domains its text fits. A domain is a field of work with needs of its own, such as building a system, or keeping knowledge. What a domain is, exactly, is open (§4).

The model uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*).

The kind of text runs across the layers (`temp/common-ground/common-ground-problem.md` §3.3, *The kind of text*). Layers 1 and 2 hold understanding only. Layers 3 and 4 each hold understanding and instructions.

### 2.1 The domain-agnostic layer

Layer 1 holds ideas bound to no domain.

It holds understanding only. An instruction applies an idea to some piece of work, and work always belongs to a domain.

### 2.2 The domain layer

Layer 2 holds a domain's understanding, in two kinds: Domain Ideas (§2.2.1) and Domain Idea Variants (§2.2.2). It holds understanding only.

The two differ by reach. A Domain Idea is the domain's default. A Domain Idea Variant serves one situation inside the domain.

A difference in one use is not a Domain Idea Variant: it is a second Adapted Case. A Domain Idea Variant is written when several Adapted Cases differ for one reason, so that the reason has one home (§3.1).

#### 2.2.1 Domain Ideas

A **Domain Idea** is an idea of layer 1 narrowed to one domain, with what the domain adds. The idea's backbone stays; its details differ.

#### 2.2.2 Domain Idea Variants

A **Domain Idea Variant** is another version of a Domain Idea, for one situation inside the domain: the dotted box. It is written whole, adapted from the same layer-1 idea as its Domain Idea. Each is read whole and changed alone: a change to one does not reach the other. The Domain Idea is the default, the version used outside that situation.

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases. An Adapted Case is an idea of layer 2 written for one use, with the Instruction Texts built on it. So it holds both kinds of text.

### 2.4 The layer of work

Layer 4 is work done by an Adapted Case. The text is the Adapted Case itself, or a copy of it where the work is done. What puts it in layer 4 is the use: the work shows where the text does not fit, and the text is changed.

## 3. How knowledge moves

Knowledge moves along the picture's arrows. Going down, an idea is adapted and taken to where it is used. Going up, what the work taught is judged, and lands in the layer it holds for.

### 3.1 How the layers fill

The layers are filled from below. New knowledge mostly comes from work: work meets something new, tries it, and changes what it works by. Judged, it is written as high as it holds: in an Adapted Case; in its Domain Idea, if the domain shares it; in layer 1, if every domain does.

A higher layer is written when the layers below show the need: a second text below needs the idea, or a text being written says something true for every text below that layer, and would otherwise sit lower. Written from one text below, it stays on trial until a second one uses it.

Writing from the top is rare, and is a trial: an idea written before work has tested it. It stays on trial until work does. Once a higher layer is written, a change to it spreads down, to each text built on it.

### 3.2 The arrows

- **adapt,** layer 1 to layer 2, and layer 2 to layer 3: a text is written from the idea above it, narrowed to its need, with what the need adds. When the idea above changes, each text built on it is checked, and changes if it must. A part left out on purpose is marked, with why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*).
- **lesson,** layer 3 to layer 2, and layer 2 to layer 1: a lesson goes up as far as it holds. It enters its Domain Idea if the whole domain shares it, and layer 1 if every domain does, reworded to fit every text below the layer it enters: no single Adapted Case at layer 2, no single domain at layer 1.
- **worked by,** layer 3 to layer 4: work is done by an Adapted Case, kept where the work is done, or as a copy there.
- **change,** layer 4 to layer 3: where the work shows the Adapted Case does not fit, the work changes it. The change is judged, and goes up the arrow *lesson* as far as it holds.

## 4. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **What a domain is:** a field of work, a sort of repo, a kind of system, or more than one of these.
2. **Text shared across domains, but not by all:** what holds it? It fits neither one domain nor layer 1.
3. **When a difference is a Domain Idea Variant:** can one use alone need one, when its difference changes how the idea is understood (§2.2)?

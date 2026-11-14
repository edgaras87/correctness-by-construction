# The layers of knowledge

<!-- A draft for temp/common-ground/common-ground-problem.md §3, *The
     Knowledge Axes*: a model of the layers knowledge sits in, and
     how it moves between them. Drawn from TODO-CONVERSATION-MEMORY.md
     §35, *The layers of knowledge*, as the TODO item on the layers
     asks. Its sources are input, not rules, and the model may differ
     from each: the problem file's §2.1 and §3; the simulation's six
     parts and depths, temp/common-ground/system-repo-change-simulation.md;
     temp/model-example/idea-model-problem.md §1 and
     temp/model-example/layers.md; docs/models/tiers.md. The picture
     and the text are checked against each other at every change: each
     label in the picture is explained in the text, each part the text
     names is in the picture, and what the text says moves where
     matches the arrows. It goes once written back into the problem
     file, and git keeps every version. -->

This document models the layers knowledge sits in, from an idea bound to no project down to a repo working by it, and how knowledge moves between them. The picture comes first; the text explains each of its labels.

## 1. The picture

```
          ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
          ┆ the Maintainer Repo                                 ┆
          ┆  ┌───────────────────────────────────────────────┐  ┆
 Layer 1  ┆  │ Project-agnostic                              │  ┆
          ┆  │ ideas bound to no project: understanding      │  ┆
          ┆  └───────────────────────────────────────────────┘  ┆
          ┆      │          ▲               ▲         │         ┆
          ┆    adapt      lesson          lesson    adapt       ┆
          ┆      ▼          │               │         ▼         ┆
          ┆  ┌─────────────────────┐   ┌─────────────────────┐  ┆
          ┆  │ the System Kit's    │   │ its own             │  ┆
 Layer 2  ┆  │ Adapted Cases       │   │ Adapted Cases       │  ┆
          ┆  │ understanding and   │   │ understanding and   │  ┆
          ┆  │ instructions        │   │ instructions        │  ┆
          ┆  └─────────────────────┘   └─────────────────────┘  ┆
          ┆      │          ▲                     ║             ┆
          └┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┐            ║             ┆
               birth,    Change,     ┆      used in place       ┆
               Update   read back    ┆            ║             ┆
                 ▼          │        ┆            ║             ┆
             ┌─────────────────────┐ ┆ ┌─────────────────────┐  ┆
 Layer 3     │ each System Repo's  │ ┆ │ its own work        │  ┆
             │ work, by its Copies │ ┆ │                     │  ┆
             └─────────────────────┘ ┆ └─────────────────────┘  ┆
                                     └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
```

Key: the dotted frame holds what the Maintainer Repo keeps. A double line joins two layers kept as one text.

## 2. The layers

Knowledge sits in three layers. The higher the layer, the more projects its text fits. How knowledge moves between them is §3.

The model uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*). The picture shortens three: Copy for System Kit Copy, Change for System Kit Copy Change, Update for System Kit Update.

The kind of text runs across the layers (`temp/common-ground/common-ground-problem.md` §3.3, *The kind of text*). Layer 1 holds understanding only. Layers 2 and 3 each hold understanding and instructions.

### 2.1 The project-agnostic layer

Layer 1 holds ideas bound to no project. So far there are two groups: how work is done with an agent, and how a CBC system is designed (`temp/common-ground/common-ground-problem.md` §2.1, *As intended*). Each is a Project-Agnostic Understanding Text.

It holds understanding only. An instruction applies an idea to some piece of work, and work always belongs to a project.

It is kept in the Maintainer Repo, and stays there. A System Repo receives it only adapted, in the System Kit.

### 2.2 The Adapted Case layer

Layer 2 holds Adapted Cases. An Adapted Case is an idea of layer 1 narrowed to one sort of need, with what that need adds, and the Instruction Texts built on it. So it holds both kinds of text.

So far an idea is adapted for two places, the picture's two boxes:

- **The System Kit's Adapted Cases:** for System Repos. Two groups so far: agent work, adapted for System Repos, and CBC system design, adapted for one kind of system, backends so far. Each System Repo works from Copies of them.
- **The Maintainer Repo's own Adapted Cases:** for itself. Agent work only, adapted to keeping this knowledge.

Both are kept in the Maintainer Repo.

### 2.3 The layer of a repo's work

Layer 3 is a repo working by an Adapted Case. The text is the Adapted Case of layer 2, or a Copy of it. What puts it in layer 3 is the use: the work shows where the text does not fit, and the repo changes it.

- **Each System Repo's work, by its Copies:** a System Repo is born with Copies of the System Kit and works by them. As its work needs, it makes Changes, so its Copies differ from layer 2 on purpose. It is kept outside the Maintainer Repo, so every arrow between it and layer 2 crosses from one repo to the other.
- **The Maintainer Repo's own work:** the Maintainer Repo works by its own Adapted Cases in place, with no Copy. There, layers 2 and 3 are one text, the double line *used in place*. A change its work makes is, at once, a change to its Adapted Case. Its problem is keeping this knowledge, as a System Repo's is designing one system.

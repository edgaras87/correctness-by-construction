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

## 3. How knowledge moves

Knowledge moves along the picture's arrows. Going down, an idea is adapted and sent to where it is used. Going up, what the work taught is read back and judged, and lands in the layer it holds for.

### 3.1 The arrows

- **adapt,** layer 1 to layer 2: an Adapted Case is written from an idea of layer 1, narrowed to its need, with what the need adds. When layer 1 changes, each Adapted Case built on that idea is checked, and changes if it must. A part of layer 1 left out on purpose is marked, with why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*).
- **lesson,** layer 2 to layer 1: a lesson true for every repo enters layer 1, reworded to name no project. It can come from either column.
- **birth,** layer 2 to layer 3: a new System Repo receives Copies of the System Kit, at one System Kit Version.
- **Update,** layer 2 to layer 3: the System Kit's changes since a System Repo's Copies were taken. The System Repo takes them by its own Copy of the Adapted Case for taking them.
- **Change, read back,** layer 3 to layer 2: a System Repo changes a Copy and records why. The Maintainer Repo reads it back and judges it against the Adapted Case the Copy came from.
- **used in place,** layer 2 and layer 3 as one text: the Maintainer Repo's own work changes its own Adapted Cases directly.

### 3.2 How a Change moves

The simulation follows one System Repo's Change through six parts (`temp/common-ground/system-repo-change-simulation.md` §1, *How it is worked*). Each part sits at a layer, or on an arrow:

| Part | Who | Where in the picture |
|---|---|---|
| Change | System Repo | layer 3, in a Copy |
| Read | Maintainer Repo | the arrow *Change, read back* |
| Judge | Maintainer Repo | layer 2: which layer the Change holds for |
| Act on the verdicts | Maintainer Repo | the layer the verdict names; the arrows *lesson* and *adapt* |
| Deliver | Maintainer Repo | the arrow *Update* |
| Take | System Repo | layer 3, its Copies |

So the six parts are one movement: up from layer 3, as high as the Change holds, and back down.

The simulation's depths say how high a Change goes (`temp/common-ground/system-repo-change-simulation.md` §2, *The cases*):

| Depth | Highest layer it changes | Arrows it travels |
|---|---|---|
| a. it stays in the System Repo | layer 3 | *Change, read back*; nothing comes down |
| b. the System Kit's Adapted Case changes | layer 2 | *Change, read back*; *Update* |
| c. the project-agnostic text changes | layer 1 | *Change, read back*; *lesson*; *adapt*, to every Adapted Case on that idea, the Maintainer Repo's own among them; *Update* |
| d. the project-agnostic text already holds it | layer 2, fixed from layer 1 | *Change, read back*; *adapt*; *Update* |
| e. it asks to narrow the project-agnostic text | layer 2, marked; layer 1 stays | *Change, read back*; *Update* |
| f. several Adapted Cases need it, but not all | none | no layer holds it: it lies between layer 1 and layer 2 |

Depth f is where the model has a gap: text shared by some Adapted Cases, but not all, has no layer of its own.

### 3.3 The Maintainer Repo's lessons

A lesson from the Maintainer Repo's own work starts in layer 3 of the right column. Since that layer is one text with its own Adapted Cases, the lesson changes layer 2 at once. It is then judged by the same questions 3 and 4 as a Change read back, and if it is true for every repo it goes up the arrow *lesson* (`temp/common-ground/common-ground-problem.md` §2.1, *Judging a change read back*). From layer 1 it comes down the arrow *adapt*, to the System Kit's Adapted Cases too, and reaches System Repos by an Update.

It has no Read, Deliver or Take of its own: nothing crosses between repos until an Update carries it to a System Repo.

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

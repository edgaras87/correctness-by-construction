# The layers of knowledge

<!-- The model of the layers knowledge sits in, and how it moves
     between them: a Work Domain Idea of the Maintainer Repo's own
     Work Domain, keeping knowledge (§2.2), and its one home. It adapts
     temp/common-ground/knowledge-layers-general.md, the layers in any
     Work Domain, and never retells it. Other texts
     point here, and never retell it. Still a draft and a trial:
     practice changes it. Its place in the repo is decided when
     today's Maintainer Repo is brought into it (TODO.md, the item on
     the layers of knowledge). Started from TODO-CONVERSATION-MEMORY.md
     §35, *The layers of knowledge*. Its first sources, input and not
     rules:
     temp/common-ground/common-ground-problem.md §2.1 and §3; the
     simulation's six parts and depths,
     temp/common-ground/system-repo-change-simulation.md;
     temp/model-example/idea-model-problem.md §1 and
     temp/model-example/layers.md; docs/models/tiers.md. The picture
     and the text are checked against each other at every change: each
     label in the picture is explained in the text, each part the text
     names is in the picture, and what the text says moves where
     matches the arrows. -->

This document is the layers of knowledge in the Maintainer Repo's Work Domain: where each layer is kept, and how knowledge travels between the Maintainer Repo and the System Repos. The layers themselves, and how knowledge moves between them, are the general document's (`temp/common-ground/knowledge-layers-general.md`). The picture comes first; the text explains each of its labels.

## 1. The picture

```
          ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
          ┆ the Maintainer Repo                                 ┆
          ┆  ┌───────────────────────────────────────────────┐  ┆
 Layer 1  ┆  │ Backbone Ideas, bound to no Work Domain:      │  ┆
          ┆  │ understanding                                 │  ┆
          ┆  └───────────────────────────────────────────────┘  ┆
          ┆    │      ▲        ▲           ▲        ▲      │    ┆
          ┆  adapt lesson  set apart   set apart lesson  adapt  ┆
          ┆    ▼      │        │           │        │      ▼    ┆
          ┆  ┌─────────────────────┐   ┌─────────────────────┐  ┆
          ┆  │ the System Repos'   │   │ its own             │  ┆
          ┆  │ Work Domain:        │   │ Work Domain:        │  ┆
 Layer 2  ┆  │ designing a backend │   │ keeping knowledge   │  ┆
          ┆  │ by CBC              │   │                     │  ┆
          ┆  │ understanding       │   │ understanding       │  ┆
          ┆  └─────────────────────┘   └─────────────────────┘  ┆
          ┆    │      ▲        ▲           ▲        ▲      │    ┆
          ┆  adapt lesson  set apart   set apart lesson  adapt  ┆
          ┆    │      │        │           │        │      │    ┆
          ┆ ┌╌╌▼╌╌╌╌╌╌│╌╌╌╌╌╌╌╌│╌╌╌╌┐      │        │      ▼    ┆
          ┆ ╎┌─────────────────────┐╎  ┌─────────────────────┐  ┆
          ┆ ╎│ the System Repos'   │╎  │ its own             │  ┆
          ┆ ╎│ Adapted Cases       │╎  │ Adapted Cases       │  ┆
 Layer 3  ┆ ╎│ understanding and   │╎  │ understanding and   │  ┆
          ┆ ╎│ instructions        │╎  │ instructions        │  ┆
          ┆ ╎└─────────────────────┘╎  └─────────────────────┘  ┆
          ┆ ╎ the System Kit        ╎             ║             ┆
          ┆ └╌╌╌╌│╌╌╌╌╌╌╌╌╌╌▲╌╌╌╌╌╌╌┘             ║             ┆
          └┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┐            ║             ┆
               birth,    Change,     ┆      used in place       ┆
               Update   read back    ┆            ║             ┆
                 ▼          │        ┆            ║             ┆
             ┌─────────────────────┐ ┆ ┌─────────────────────┐  ┆
 Layer 4     │ each System Repo's  │ ┆ │ its own work        │  ┆
             │ work, by its Copies │ ┆ │                     │  ┆
             └─────────────────────┘ ┆ └─────────────────────┘  ┆
                                     └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
```

Key: the dotted frame holds what the Maintainer Repo keeps. The dashed frame holds what the System Kit copies to each System Repo. A double line joins two layers kept as one text.

## 2. The layers

Knowledge sits in four layers (`temp/common-ground/knowledge-layers-general.md` §2, *The layers*). This section says where each is kept here, and what each holds so far.

The model uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*). The picture shortens three: Copy for System Kit Copy, Change for System Kit Copy Change, Update for System Kit Update.

The System Kit is not a layer. It is what is copied to each System Repo, the picture's dashed frame: so far, the System Repos' Adapted Cases of layer 3.

### 2.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas (`temp/common-ground/knowledge-layers-general.md` §2.1, *The Backbone Idea layer*). Which of today's project-agnostic ideas are Backbone Ideas is open (§4).

It is kept in the Maintainer Repo, and stays there. A System Repo receives it only adapted, in the System Kit.

### 2.2 The Work Domain layer

Layer 2 holds Work Domain Ideas (`temp/common-ground/knowledge-layers-general.md` §2.2, *The Work Domain layer*).

So far there are two Work Domains, the picture's two boxes.

- **The System Repos' Work Domain:** designing a backend by CBC.
- **The Maintainer Repo's own Work Domain:** keeping knowledge. This model is one of its Work Domain Ideas.

Both are kept in the Maintainer Repo.

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases (`temp/common-ground/knowledge-layers-general.md` §2.3, *The Adapted Case layer*).

So far an idea is adapted for two places, the picture's two boxes:

- **The System Repos' Adapted Cases:** two groups so far: agent work, adapted for System Repos, and CBC system design, adapted for one kind of system, backends so far. They are the System Kit, and each System Repo works from Copies of them.
- **The Maintainer Repo's own Adapted Cases:** for itself. Agent work only, adapted to keeping this knowledge.

Both are kept in the Maintainer Repo.

### 2.4 The layer of a repo's work

Layer 4 is work done by an Adapted Case (`temp/common-ground/knowledge-layers-general.md` §2.4, *The layer of work*). Here the work is a repo's:

- **Each System Repo's work, by its Copies:** a System Repo is born with Copies of the System Kit and works by them. As its work needs, it makes Changes, so its Copies differ from layer 3 on purpose. It is kept outside the Maintainer Repo, so every arrow between it and layer 3 crosses from one repo to the other.
- **The Maintainer Repo's own work:** the Maintainer Repo works by its own Adapted Cases in place, with no Copy. There, layers 3 and 4 are one text, the double line *used in place*. A change its work makes is, at once, a change to its Adapted Case. Its problem is keeping this knowledge, as a System Repo's is designing one system.

## 3. How knowledge moves

How knowledge enters the layers and moves between them is the general document's (`temp/common-ground/knowledge-layers-general.md` §3, *How knowledge moves*). This section adds the arrows between the Maintainer Repo and the System Repos, and how a Change travels them.

### 3.1 The arrows

- **adapt,** **lesson** and **set apart,** between layers 1, 2 and 3: as the general document has them (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*). A lesson, or a part set apart, can come from either column.
- **birth,** layer 3 to layer 4: a new System Repo receives Copies of the System Kit, at one System Kit Version.
- **Update,** layer 3 to layer 4: the System Kit's changes since a System Repo's Copies were taken. The System Repo takes them by its own Copy of the Adapted Case for taking them.
- **Change, read back,** layer 4 to layer 3: a System Repo changes a Copy and records why. The Maintainer Repo reads it back and judges it against the Adapted Case the Copy came from.
- **used in place,** layer 3 and layer 4 as one text: the Maintainer Repo's own work changes its own Adapted Cases directly.

### 3.2 How a Change moves

The simulation follows one System Repo's Change through six parts (`temp/common-ground/system-repo-change-simulation.md` §1, *How it is worked*). Each part sits at a layer, or on an arrow:

| Part | Who | Where in the picture |
|---|---|---|
| Change | System Repo | layer 4, in a Copy |
| Read | Maintainer Repo | the arrow *Change, read back* |
| Judge | Maintainer Repo | layer 3: which layer the Change holds for |
| Act on the verdicts | Maintainer Repo | the layer the verdict names; the arrows *lesson* and *adapt* |
| Deliver | Maintainer Repo | the arrow *Update* |
| Take | System Repo | layer 4, its Copies |

So the six parts are one movement: up from layer 4, as high as the Change holds, and back down.

The simulation's depths say how high a Change goes (`temp/common-ground/system-repo-change-simulation.md` §2, *The cases*). They name the project-agnostic text, which here is layer 2 or layer 1:

| Depth | Highest layer it changes | Arrows it travels |
|---|---|---|
| a. it stays in the System Repo | layer 4 | *Change, read back*; nothing comes down |
| b. the System Kit's Adapted Case changes | layer 3 | *Change, read back*; *Update* |
| c. the project-agnostic text changes | layer 2 or layer 1 | *Change, read back*; *lesson*; *adapt*, to every text built on that idea, the Maintainer Repo's own among them; *Update* |
| d. the project-agnostic text already holds it | layer 3, fixed from the layer above | *Change, read back*; *adapt*; *Update* |
| e. it asks to narrow the project-agnostic text | layer 3, marked; the layer above stays | *Change, read back*; *Update* |
| f. several Adapted Cases need it, but not all | layer 2, if they share a Work Domain | *Change, read back*; *lesson*; *adapt*; *Update* |

The Work Domain layer fills part of depth f's gap: text shared by the Adapted Cases of one Work Domain has a layer. Text shared across Work Domains, but not by all, still has none.

### 3.3 The Maintainer Repo's lessons

A lesson from the Maintainer Repo's own work starts in layer 4 of the right column. Since that layer is one text with its own Adapted Cases, the lesson changes layer 3 at once. It is then judged by the same questions 3 and 4 as a Change read back, and goes up the arrow *lesson* as far as it holds (`temp/common-ground/common-ground-problem.md` §2.1, *Judging a change read back*). If it reaches layer 1, it comes down the arrow *adapt*, to the System Repos' Adapted Cases too, and reaches System Repos by an Update.

It has no Read, Deliver or Take of its own: nothing crosses between repos until an Update carries it to a System Repo.

## 4. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **A Maintainer Kit:** should there be a kit a new Maintainer Repo is born from, as a System Repo is born from the System Kit? There is one Maintainer Repo so far. The Tiers Model has a rule for a second Concept Repo (`docs/models/tiers.md` §2.1, *The empty top tier*), and `cbc-concept`, built by the stopped Plan Step *Rebuild in cbc-concept*, is close to a second Maintainer Repo.
2. **What layer 4 holds:** the general document's question (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 6). Here it is met at a System Repo's design of its system and its own Knowledge on Trial.
3. **A name for the movement:** what runs from a Change to the take of the next Update, as one thing (§3.2), so the simulation can name it.
4. **The depths and the layers:** is how deep a Change goes the same as how high it goes (§3.2)? Text shared across Work Domains, but not by all, is the general document's question (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 1). Here it is met when the open Plan Step's stage 2 labels which parts of `concept/` are which.
5. **Where Judge sits:** §3.2 puts it at layer 3, since a Change is judged against the Adapted Case its Copy came from. The sources say only that it runs in the Maintainer Repo.
6. **Depth d and the layer above:** if several Adapted Cases lost the same part, the layer above may be reworded clearer (`temp/common-ground/system-repo-change-simulation.md` §2, *The cases*). §3.2's row leaves it out.
7. **What then points at it:** the simulation's opening and the problem file's §2.1. Then `temp/`'s old files, one by one, and how today's ways are written across the drafts.
8. **What the System Kit holds:** layer 3 only, or the System Repos' Work Domain Ideas too. CBC system design adapted for backends (`temp/common-ground/common-ground-problem.md` §2.1, *What the System Kit holds*, item 2) may already be layer 2.
9. **Which ideas are Backbone Ideas:** of today's project-agnostic ideas, how work is done with an agent may be; how a CBC system is designed may belong to the Work Domain of designing a backend by CBC.

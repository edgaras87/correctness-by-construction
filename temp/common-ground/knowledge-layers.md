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

This document models the layers knowledge sits in, from an idea bound to no domain down to a repo working by it, and how knowledge moves between them. The picture comes first; the text explains each of its labels.

## 1. The picture

```
          ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
          ┆ the Maintainer Repo                                 ┆
          ┆  ┌───────────────────────────────────────────────┐  ┆
 Layer 1  ┆  │ Domain-agnostic                               │  ┆
          ┆  │ ideas bound to no domain: understanding       │  ┆
          ┆  └───────────────────────────────────────────────┘  ┆
          ┆      │          ▲               ▲         │         ┆
          ┆    adapt      lesson          lesson    adapt       ┆
          ┆      ▼          │               │         ▼         ┆
          ┆  ┌─────────────────────┐   ┌─────────────────────┐  ┆
          ┆  │ the System Repos'   │   │ its own domain:     │  ┆
          ┆  │ domain: building    │   │ keeping knowledge   │  ┆
 Layer 2  ┆  │ a system            │   │                     │  ┆
          ┆  │ understanding       │   │ understanding       │  ┆
          ┆  │ ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐ │   │                     │  ┆
          ┆  │ ┆a case, if needed┆ │   │                     │  ┆
          ┆  │ └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘ │   │                     │  ┆
          ┆  └─────────────────────┘   └─────────────────────┘  ┆
          ┆    │                 ▲          ▲         │         ┆
          ┆  adapt             lesson     lesson    adapt       ┆
          ┆    │                 │          │         │         ┆
          ┆ ┌╌╌▼ the System Kit ╌│╌╌┐       │         ▼         ┆
          ┆ ╎┌─────────────────────┐╎  ┌─────────────────────┐  ┆
          ┆ ╎│ the System Repos'   │╎  │ its own             │  ┆
          ┆ ╎│ Adapted Cases       │╎  │ Adapted Cases       │  ┆
 Layer 3  ┆ ╎│ understanding and   │╎  │ understanding and   │  ┆
          ┆ ╎│ instructions        │╎  │ instructions        │  ┆
          ┆ ╎└─────────────────────┘╎  └─────────────────────┘  ┆
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

Key: the dotted frame holds what the Maintainer Repo keeps. The dashed frame holds what the System Kit copies to each System Repo. A dotted box inside a layer is a narrower case, written only when needed. A double line joins two layers kept as one text.

## 2. The layers

Knowledge sits in four layers. The higher the layer, the more domains its text fits. How knowledge moves between them is §3.

The model uses the Common Ground Problem's Defined Terms (`temp/common-ground/common-ground-problem.md`, *Defined Terms*). The picture shortens three: Copy for System Kit Copy, Change for System Kit Copy Change, Update for System Kit Update.

The kind of text runs across the layers (`temp/common-ground/common-ground-problem.md` §3.3, *The kind of text*). Layers 1 and 2 hold understanding only. Layers 3 and 4 each hold understanding and instructions.

The System Kit is not a layer. It is what is copied to each System Repo, the picture's dashed frame: so far, the System Repos' Adapted Cases of layer 3.

### 2.1 The domain-agnostic layer

Layer 1 holds ideas bound to no domain. Which of today's project-agnostic ideas belong here is open (§4).

It holds understanding only. An instruction applies an idea to some piece of work, and work always belongs to a domain.

It is kept in the Maintainer Repo, and stays there. A System Repo receives it only adapted, in the System Kit.

### 2.2 The domain layer

Layer 2 holds ideas narrowed to one domain, with what the domain adds. The idea's backbone stays; its details differ. It holds understanding only.

So far there are two domains, the picture's two boxes. What a domain is, exactly, is open (§4).

- **The System Repos' domain:** building a system.
- **The Maintainer Repo's own domain:** keeping knowledge. This model is one of its ideas.

Inside a domain, an idea may be narrowed again for one case, such as a piece of work while slicing: the dotted box. A case is written only when work shows it differs from its domain's idea.

Both are kept in the Maintainer Repo.

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases. An Adapted Case is an idea of layer 2 written for one use, with the Instruction Texts built on it. So it holds both kinds of text.

So far an idea is adapted for two places, the picture's two boxes:

- **The System Repos' Adapted Cases:** two groups so far: agent work, adapted for System Repos, and CBC system design, adapted for one kind of system, backends so far. They are the System Kit, and each System Repo works from Copies of them.
- **The Maintainer Repo's own Adapted Cases:** for itself. Agent work only, adapted to keeping this knowledge.

Both are kept in the Maintainer Repo.

### 2.4 The layer of a repo's work

Layer 4 is a repo working by an Adapted Case. The text is the Adapted Case of layer 3, or a Copy of it. What puts it in layer 4 is the use: the work shows where the text does not fit, and the repo changes it.

- **Each System Repo's work, by its Copies:** a System Repo is born with Copies of the System Kit and works by them. As its work needs, it makes Changes, so its Copies differ from layer 3 on purpose. It is kept outside the Maintainer Repo, so every arrow between it and layer 3 crosses from one repo to the other.
- **The Maintainer Repo's own work:** the Maintainer Repo works by its own Adapted Cases in place, with no Copy. There, layers 3 and 4 are one text, the double line *used in place*. A change its work makes is, at once, a change to its Adapted Case. Its problem is keeping this knowledge, as a System Repo's is designing one system.

## 3. How knowledge moves

Knowledge moves along the picture's arrows. Going down, an idea is adapted and sent to where it is used. Going up, what the work taught is read back and judged, and lands in the layer it holds for.

The layers are filled from below. New knowledge mostly comes from work: a repo meets something new, tries it, and changes what it works by. Read back and judged, it is written as high as it holds: in an Adapted Case; in its domain's idea, if the domain shares it; in layer 1, if every domain does. A higher layer is written only when the layers below show the need.

Writing from the top is rare, and is a trial: an idea written before work has tested it, such as this model. It stays on trial until work does. Once a higher layer is written, a change to it spreads down, to each text built on it.

### 3.1 The arrows

- **adapt,** layer 1 to layer 2, and layer 2 to layer 3: a text is written from the idea above it, narrowed to its need, with what the need adds. When the idea above changes, each text built on it is checked, and changes if it must. A part left out on purpose is marked, with why (`temp/common-ground/common-ground-problem.md` §2.1, *Narrowing, never shrinking*).
- **lesson,** layer 3 to layer 2, and layer 2 to layer 1: a lesson goes up as far as it holds. It enters its domain's idea if the whole domain shares it, and layer 1 if every domain does, reworded to name no domain. It can come from either column.
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
| f. several Adapted Cases need it, but not all | layer 2, if they share a domain or a case | *Change, read back*; *lesson*; *adapt*; *Update* |

The domain layer fills part of depth f's gap: text shared by the Adapted Cases of one domain, or of one case, has a layer. Text shared across domains, but not by all, still has none.

### 3.3 The Maintainer Repo's lessons

A lesson from the Maintainer Repo's own work starts in layer 4 of the right column. Since that layer is one text with its own Adapted Cases, the lesson changes layer 3 at once. It is then judged by the same questions 3 and 4 as a Change read back, and goes up the arrow *lesson* as far as it holds (`temp/common-ground/common-ground-problem.md` §2.1, *Judging a change read back*). If it reaches layer 1, it comes down the arrow *adapt*, to the System Repos' Adapted Cases too, and reaches System Repos by an Update.

It has no Read, Deliver or Take of its own: nothing crosses between repos until an Update carries it to a System Repo.

## 4. Questions for after the draft

Each is answered once the draft stands, one at a time. None is answered by the text above.

1. **A Maintainer Kit:** should there be a kit a new Maintainer Repo is born from, as a System Repo is born from the System Kit? There is one Maintainer Repo so far. The Tiers Model has a rule for a second Concept Repo (`docs/models/tiers.md` §2.1, *The empty top tier*), and `cbc-concept`, built by the stopped Plan Step *Rebuild in cbc-concept*, is close to a second Maintainer Repo.
2. **What layer 4 holds:** a repo's use of Adapted Cases only, or also its own knowledge, such as a System Repo's design of its system and its own Knowledge on Trial?
3. **A name for the movement:** what runs from a Change to the take of the next Update, as one thing (§3.2), so the simulation can name it.
4. **The depths and the layers:** is how deep a Change goes the same as how high it goes (§3.2)? What holds text shared across domains, but not by all?
5. **Where Judge sits:** §3.2 puts it at layer 3, since a Change is judged against the Adapted Case its Copy came from. The sources say only that it runs in the Maintainer Repo.
6. **Depth d and the layer above:** if several Adapted Cases lost the same part, the layer above may be reworded clearer (`temp/common-ground/system-repo-change-simulation.md` §2, *The cases*). §3.2's row leaves it out.
7. **How it joins §3:** does the model join §3.3, *The kind of text*, and §3.4, *Where the text is*, or stand beside them? Is the layer a Knowledge Axis of its own? Or is its home elsewhere, since it is a layer-2 idea of the Maintainer Repo's own domain?
8. **What then points at it:** the simulation's opening and the problem file's §2.1. Then `temp/`'s old files, one by one, and how today's ways are written across the drafts.
9. **What a domain is:** the sort of repo, the kind of system, or both. Backends may be a domain, or a case inside the domain of building a system.
10. **What the System Kit holds:** layer 3 only, or the System Repos' domain ideas too. CBC system design adapted for backends (`temp/common-ground/common-ground-problem.md` §2.1, *What the System Kit holds*, item 2) may already be layer 2.
11. **Which ideas are domain-agnostic:** of today's project-agnostic ideas, how work is done with an agent may be; how a CBC system is designed may belong to the domain of building a system.

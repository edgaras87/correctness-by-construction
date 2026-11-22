# The layers of knowledge

<!--
What it is: a Work Domain Idea of the Maintainer Repo's own Work Domain, keeping knowledge (§2.2), and its one home. Still a draft and a trial: practice changes it.
What it stands on: temp/common-ground/knowledge-layers-general.md, the layers in any Work Domain. It adapts that document, and never retells it.
What stands on it: other texts point here, and never retell it.
Its place in the repo: decided when today's Maintainer Repo is brought into it (TODO.md, the item on the layers of knowledge).
Where it started: TODO-CONVERSATION-MEMORY.md §35, *The layers of knowledge*.
Its first sources, input and not rules:
- temp/common-ground/common-ground-problem.md §2.1 and §3;
- the simulation's six parts and depths, temp/common-ground/system-repo-change-simulation.md;
- temp/model-example/idea-model-problem.md §1 and temp/model-example/layers.md;
- docs/models/tiers.md.
How it is edited: the picture and the text are checked against each other at every change, as the general document's header says.
-->

This document is the layers of knowledge in the Maintainer Repo's Work Domain: where each layer is kept, and how knowledge travels between the Maintainer Repo and the System Repos. The layers themselves, and how knowledge moves between them, are the general document's (`temp/common-ground/knowledge-layers-general.md`). The picture comes first; the text explains each of its labels.

## 1. The picture

```
          ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
          ┆ the Maintainer Repo                                                           ┆
          ┆  ┌─────────────────────────────────────────────────────────────────────────┐  ┆
 Layer 1  ┆  │ Backbone Ideas, bound to no Work Domain:                                │  ┆
          ┆  │ understanding                                                           │  ┆
          ┆  └─────────────────────────────────────────────────────────────────────────┘  ┆
          ┆     │      ▲       ▲                                    ▲        ▲      │     ┆
          ┆   adapt lesson set apart                            set apart lesson  adapt   ┆
          ┆     ▼      │       │                                    │        │      ▼     ┆
          ┆  ┌──────────────────────┐  ┌───────────────────────────────────────────────┐  ┆
          ┆  │ designing a backend  │  │ keeping knowledge,                            │  ┆
 Layer 2  ┆  │ by CBC: the System   │  │ in every repo                                 │  ┆
          ┆  │ Repos' problem       │  │                                               │  ┆
          ┆  │ understanding        │  │ understanding                                 │  ┆
          ┆  └──────────────────────┘  └───────────────────────────────────────────────┘  ┆
          ┆     │      ▲       ▲          │      ▲       ▲          │      ▲       ▲      ┆
          ┆   adapt lesson set apart    adapt lesson set apart    adapt lesson set apart  ┆
          ┆ ┌╌╌╌▼╌╌╌╌╌╌│╌╌╌╌╌╌╌│╌╌╌╌╌╌╌╌╌╌▼╌╌╌╌╌╌│╌╌╌╌╌╌╌│╌╌╌╌╌┐    ▼      │       │      ┆
          ┆ ╎┌──────────────────────┐  ┌──────────────────────┐╎ ┌─────────────────────┐  ┆
          ┆ ╎│ the System Repos'    │  │ the System Repos'    │╎ │ its own             │  ┆
          ┆ ╎│ Adapted Cases for    │  │ Adapted Cases for    │╎ │ Adapted Cases       │  ┆
 Layer 3  ┆ ╎│ designing a backend  │  │ keeping knowledge    │╎ │                     │  ┆
          ┆ ╎│ understanding and    │  │ understanding and    │╎ │ understanding and   │  ┆
          ┆ ╎│ instructions         │  │ instructions         │╎ │ instructions        │  ┆
          ┆ ╎└──────────────────────┘  └──────────────────────┘╎ └─────────────────────┘  ┆
          ┆ ╎ the System Kit                                   ╎            ║             ┆
          ┆ └╌╌╌╌╌╌╌╌╌╌╌╌│╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌▲╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘            ║             ┆
          └┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐           ║             ┆
                      birth,            Copy Change,            ┆     used in place       ┆
                    Kit Update           read back              ┆           ║             ┆
                         ▼                   │                  ┆           ║             ┆
              ┌─────────────────────────────────────┐           ┆ ┌────────────────────┐  ┆
 Layer 4      │ each System Repo's work,            │           ┆ │ its own work       │  ┆
              │ by its Kit Copies                   │           ┆ │                    │  ┆
              └─────────────────────────────────────┘           ┆ └────────────────────┘  ┆
                                                                └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
```

Key: the dotted frame holds what the Maintainer Repo keeps. The dashed frame holds what the System Kit copies to each System Repo. A double line joins layer 3 to the work done by it in the same repo, with no Kit Copy between.

## 2. The layers

Knowledge sits in four layers (`temp/common-ground/knowledge-layers-general.md` §2, *The layers*). This section says where each is kept here, and what each holds so far. Layers 1 to 3 are kept in the Maintainer Repo; where inside it is decided when today's Maintainer Repo is brought into this model (`TODO.md`, the item on the layers of knowledge).

Its repos, and what travels between them:

- **Maintainer Repo:** the repo that keeps the understanding and the System Kit, and reads back what each System Repo learns.
- **System Repo:** a repo where a real system is built by the concept, working from copies of the System Kit.
- **System Kit:** what the Maintainer Repo keeps for System Repos to work from, shared by the System Repos it serves; what it holds is listed below. Its originals stay in the Maintainer Repo, beside the Work Domain Ideas they are adapted from; each System Repo works from copies, and takes the System Kit's changes by a System Kit Update.
- **System Kit Version:** the System Kit as it stood at one Maintainer Repo commit. Each System Repo records the one its System Kit Copies came from.
- **System Kit Copy:** a copy of a System Kit file, as it lives in a System Repo.
- **System Kit Copy Change:** a System Repo's change to a System Kit Copy, made against the System Kit Version that copy came from.
- **System Kit Copy Change Record:** what a System Repo writes with each System Kit Copy Change, saying what changed and why. What it holds and where it sits are §3.2.1's.
- **System Kit Attention Note:** what a System Repo writes for the Maintainer Repo to look at in the System Kit, when no System Kit Copy Change carries it.
- **Maintainer Repo Register:** the Maintainer Repo's list of its System Repos: where each lives, and its *settled snapshot*, the System Repo's snapshot up to which the Maintainer Repo has read, judged and acted on. The *settled snapshot* holds the System Kit Version the System Repo had then, which may be behind the newest.
- **Look for Lessons:** the Maintainer Repo taking one System Repo's work since its *settled snapshot* into account: read, judged and acted on. How it runs is §3.2's.
- **System Repo Reading:** the draft that lists the System Kit Copy Changes one Look for Lessons found in a System Repo, nothing judged. With none found, none is written.
- **System Kit Update:** what the Maintainer Repo sends a System Repo: a copy of every System Kit file at one System Kit Version, with its System Kit Update Note.
- **System Kit Update Note:** what the Maintainer Repo writes with a System Kit Update, for the System Repo that takes it.
- **System Kit Update Take:** a System Repo taking a System Kit Update into its System Kit Copies. How it runs is the simulation's (`temp/common-ground/system-repo-change-simulation.md` §8, *Take the Kit Update*). Its *version snapshot* is the System Repo's commit where the System Kit Update Take put every System Kit Copy at the new System Kit Version, its hash written beside that System Kit Version.

This document shortens ten of these Defined Terms to their last two words:

| Short form | Defined Term |
|---|---|
| Kit Version | System Kit Version |
| Kit Copy | System Kit Copy |
| Copy Change | System Kit Copy Change |
| Change Record | System Kit Copy Change Record |
| Attention Note | System Kit Attention Note |
| Repo Register | Maintainer Repo Register |
| Repo Reading | System Repo Reading |
| Kit Update | System Kit Update |
| Update Note | System Kit Update Note |
| Update Take | System Kit Update Take |

An *italic* word is a label inside the Defined Term it belongs to. Its other Defined Terms are the general document's, or the Common Ground Problem's (`temp/common-ground/common-ground-problem.md`, *Defined Terms*).

The System Kit is not a layer. It is what is copied to each System Repo, the picture's dashed frame. Each of its parts is an Adapted Case of layer 3: an Adapted Understanding Text with its Instruction Text (§2.3). A part that has only one of the two is open (§4, question 7). So far it holds:

1. the System Repos' Adapted Cases for keeping knowledge, such as taking a Kit Update (§2.3.1);
2. their Adapted Cases for designing a backend: agent work, and CBC system design (§2.3.2);
3. the Defined Terms the Adapted Cases use;
4. the forms a System Repo's records start from. They go once, at birth, and are the System Repo's own after it;
5. a description of CBC system design for the System Repo's readers, as adapted to its kind of system. Its form is decided when the concept is split, and so is whether a System Repo may change it.

### 2.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas (`temp/common-ground/knowledge-layers-general.md` §2.1, *The Backbone Idea layer*). Each row's description is a summary; the idea's home holds it.

| Backbone Idea | What it says | Home |
|---|---|---|
| The layers of knowledge | the layers knowledge sits in, and how it moves between them | `temp/common-ground/knowledge-layers-general.md` |
| How an agent works | what one piece of agent work is: what the agent does, when, where and how | planned, from `docs/models/agent.md` (`TODO.md`, the item that rewrites the Agent Model) |
| CBC design | how a system is designed by CBC, for no one kind of system | planned, from `concept/` (`TODO.md`, the item that splits the concept) |

Which other of today's project-agnostic ideas are Backbone Ideas is open (§4).

It is kept in the Maintainer Repo, and stays there. A System Repo receives it only adapted, in the System Kit.

### 2.2 The Work Domain layer

Layer 2 holds Work Domain Ideas (`temp/common-ground/knowledge-layers-general.md` §2.2, *The Work Domain layer*), each a Backbone Idea of §2.1 adapted to one Work Domain.

The Maintainer Repo works in one Work Domain, keeping knowledge. A System Repo works in two so far: designing a backend by CBC, its problem, and keeping its own knowledge. So keeping knowledge is worked in every repo. The Maintainer Repo keeps the texts of both Work Domains, the picture's two boxes. Keeping the System Repos' texts is part of its own work (§3.2).

In each table, a row's description is a summary; the idea's home holds it. Whether the two Work Domain Ideas of how an agent works differ is open (§4).

#### 2.2.1 Keeping knowledge

Worked in every repo. The Maintainer Repo works its Work Domain Ideas by its own Adapted Cases, in place, and each System Repo by its Kit Copies (§2.4).

| Work Domain Idea | Adapted from | What it adds | Home |
|---|---|---|---|
| The layers of knowledge, in the Maintainer Repo | The layers of knowledge | where each layer is kept; how knowledge travels between the repos | this document |
| How an agent works, keeping knowledge | How an agent works | open (§4, question 10) | planned (`TODO.md`, the item that rewrites the Agent Model) |

#### 2.2.2 Designing a backend by CBC

The System Repos' problem, a Work Domain worked in them alone. The Maintainer Repo keeps its Work Domain Ideas and writes the System Kit's Adapted Cases for designing a backend from them. The work is done in each System Repo, by its Kit Copies (§2.4).

| Work Domain Idea | Adapted from | What it adds | Home |
|---|---|---|---|
| How an agent works, designing a backend | How an agent works | open (§4, question 10) | planned (`TODO.md`, the item that rewrites the Agent Model) |
| CBC design for backends | CBC design | backends as the kind of system | planned, from `concept/` (`TODO.md`, the item that splits the concept) |

### 2.3 The Adapted Case layer

Layer 3 holds Adapted Cases (`temp/common-ground/knowledge-layers-general.md` §2.3, *The Adapted Case layer*), each written from a Work Domain Idea of §2.2.

Here an Adapted Case is written for one piece of agent work, such as reading a System Repo, working one step of its Plan Step, or writing a commit message, or for what all of the agent's work uses, such as the Defined Terms. Its Instruction Text is anything the agent acts on in that work: an Agent Skill, an Agent Rule, the Defined Terms it writes by, or a record form it fills. How many one Adapted Case holds is open (§4). Its Adapted Understanding Text says why the Instruction Text is as it is. The agent uses the Instruction Text in the work, and reads the Adapted Understanding Text only when the Instruction Text is changed. The two travel together: a System Repo's Kit Copy holds both.

Layer 3 is split like layer 2: one part for each Work Domain. The Maintainer Repo keeps both. Keeping knowledge's part holds two groups, the picture's two right boxes (§2.3.1). An Agent Skill or Agent Rule found in two groups is two Adapted Cases, one in each. The two are tied only through the nearest idea above them both (`temp/common-ground/knowledge-layers-general.md` §2.3, *The Adapted Case layer*).

An Adapted Case may also be written by work no Adapted Case covers, on trial: one kind of Knowledge on Trial (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*, the arrow *change*). Either repo writes it. A System Repo's Knowledge on Trial is kept in the System Repo, comes from no Kit Copy, and is handed over at its close.

#### 2.3.1 Keeping knowledge

Two groups so far:

- **Its own,** the Maintainer Repo's, for itself. So far, apart from its Approaches on Trial, all are written from one Work Domain Idea of §2.2.1: how an agent works, keeping knowledge. The Maintainer Repo works by them in place, with no Kit Copy (§2.4). If a Maintainer Kit is wanted, it is made from them (§4, question 1).
- **The System Repos',** for keeping a System Repo's own knowledge, such as taking a Kit Update. They are written from §2.2.1's Work Domain Ideas, and are part of the System Kit (§2.3.2).

#### 2.3.2 Designing a backend by CBC

The System Repos' Adapted Cases for designing a backend, in two groups so far, one for each Work Domain Idea of §2.2.2:

- **Agent work,** from how an agent works, designing a backend.
- **CBC system design,** from CBC design for backends. How it meets agent work in one Adapted Case is open (§4).

With the System Repos' group of §2.3.1, they are part of the System Kit (§2). Each System Repo works from Kit Copies of them (§2.4).

### 2.4 The layer of a repo's work

Layer 4 is work done by an Adapted Case (`temp/common-ground/knowledge-layers-general.md` §2.4, *The layer of work*). The text it works by is a layer-3 text, wherever it is kept. Whether what the work makes is layer 4 is open (§4). Here the work is a repo's:

- **Each System Repo's work, by its Kit Copies:** a System Repo is born with Kit Copies of the System Kit and works by them. A Kit Copy is a layer-3 text kept in the System Repo. As its work needs, it makes Copy Changes, so its Kit Copies differ from the System Kit on purpose. It is kept outside the Maintainer Repo, so every arrow between it and layer 3 crosses from one repo to the other.
- **The Maintainer Repo's own work:** the Maintainer Repo works by its own Adapted Cases in place, with no Kit Copy: they are kept where the work is done, so nothing is delivered. There, layer 3 and the work are in one repo, the double line *used in place*. A change its work makes is, at once, a change to its Adapted Case. Its problem is keeping this knowledge, as a System Repo's is designing one system.

## 3. How knowledge moves

How knowledge enters the layers and moves between them is the general document's (`temp/common-ground/knowledge-layers-general.md` §3, *How knowledge moves*). This section adds the arrows between the Maintainer Repo and the System Repos, and how a Copy Change travels them.

### 3.1 The arrows

- **adapt,** **lesson** and **set apart,** between layers 1, 2 and 3: as the general document has them (`temp/common-ground/knowledge-layers-general.md` §3.2, *The arrows*). A lesson, or a part set apart, can come from either column.
- **birth,** layer 3 to layer 4: a new System Repo receives Kit Copies of the System Kit, at one System Kit Version.
- **Kit Update,** layer 3 to layer 4: a System Kit Update (§2) brings a System Repo's Kit Copies to a newer System Kit Version. The System Repo takes it by its own Kit Copy of the Adapted Case for taking a Kit Update.
- **Copy Change, read back,** layer 4 to layer 3: a System Repo changes a Kit Copy and records why. The Maintainer Repo reads it back and judges it against the Adapted Case the Kit Copy came from.
- **used in place,** layer 3 and layer 4 in one repo, with no Kit Copy: the Maintainer Repo's own work changes its own Adapted Cases directly.

### 3.2 How a change travels

A Copy Change travels through six parts, each done by one repo. Each part sits at a layer, or on an arrow:

| Part | Who | Where in the picture |
|---|---|---|
| Change a Kit Copy | System Repo | layer 4, in a Kit Copy |
| Read Copy Changes | Maintainer Repo | the arrow *Copy Change, read back* |
| Judge Copy Changes | Maintainer Repo | layer 3: which layer the Copy Change holds for |
| Act on the verdicts | Maintainer Repo | the layer the verdict names; the arrows *lesson* and *adapt* |
| Deliver the Kit Update | Maintainer Repo | the arrow *Kit Update* |
| Take the Kit Update | System Repo | layer 4, its Kit Copies |

So the six parts are one movement: up from layer 4, as high as the Copy Change holds, and back down.

**The Look for Lessons.** Read Copy Changes, Judge Copy Changes and Act on the verdicts make one pass over one System Repo, the Look for Lessons. It starts when the human names a System Repo, for its lessons or to update it. It ends once Act on the verdicts is done, which sets the *settled snapshot* to the stop (`temp/common-ground/system-repo-change-simulation.md` §4, step 2, *When the stop moves*). Its first step, two checks at main, sorts it into one of three cases (`temp/common-ground/system-repo-change-simulation.md` §4, step 1, *Two checks at main*). Deliver the Kit Update and Take the Kit Update are outside it.

**Bringing a System Repo up to date.** It is a second job, which needs the first. It runs only when the human names the System Repo to update, and starts with a Look for Lessons. Its check, whether a Kit Update is due, belongs to Deliver the Kit Update. It comes after Act on the verdicts, since the System Kit moves for a Copy Change only once it is judged and acted on (`temp/common-ground/system-repo-change-simulation.md` §7, step 1, *When one is due*).

Each of the simulation's depths names the highest layer a Copy Change reaches (`temp/common-ground/system-repo-change-simulation.md` §2, *The cases*). The arrows each travels:

| Depth | Arrows it travels |
|---|---|
| a. it stays in the System Repo | *Copy Change, read back*; nothing comes down |
| b. the System Kit's Adapted Case changes | *Copy Change, read back*; *Kit Update* |
| c, at layer 2. the idea above changes: its Work Domain Idea | *Copy Change, read back*; *lesson*; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| c, at layer 1. the idea above changes: its Backbone Idea | *Copy Change, read back*; *lesson*, twice; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| d. the idea above already holds it | *Copy Change, read back*; *adapt*; *Kit Update* |
| e. it asks to narrow the idea above | *Copy Change, read back*; *Kit Update* |
| f. several Adapted Cases need it, but not all | *Copy Change, read back*; *Kit Update* |

Depth f's gap, text shared by several Adapted Cases but not all, is the simulation's (`temp/common-ground/system-repo-change-simulation.md` §2, *The cases*, its row f). Its second case, across Work Domains, is met when `concept/` is labelled general or backend, for the concept's split (`TODO.md`, the item that splits the concept).

#### 3.2.1 Change a Kit Copy

The System Repo changes a Kit Copy during its own work, and the gate of its Plan Step decides each Copy Change. How each rule was chosen is the simulation's (`temp/common-ground/system-repo-change-simulation.md` §3, *Change a Kit Copy*).

**When a Kit Copy changes.** A Kit Copy changes only when the System Repo's work shows it does not fit what happened, never ahead. The human decides the Copy Change, the agent proposing. It is made then, with its Change Record. A Copy Change may be edited or reversed later, its Change Record with it.

**Where the Change Record sits.** In a footer of the Kit Copy's Adapted Understanding Text, which is not loaded for work. So the Copy Change and its why land in one diff, and the why cannot lose its Kit Copy. When only an Instruction Text changes, its Change Record goes there too.

**What the Change Record holds:**
- what changed, by meaning: the part, and what it says now. When some of the Adapted Case's texts were left as they were, it also says whether they still match the Copy Change (`temp/common-ground/common-ground-problem.md` §4, Failure Case 8);
- what happened, concretely, in the System Repo's own words. It is never written to sound general: rewording it is the Maintainer Repo's, after judging;
- which work found it;
- the System Repo's proposal, marked as one: its own problem, or one any repo would meet. The Maintainer Repo judges every Copy Change, and says whether it agrees, and why if not.

**When it is rewritten.** The Change Record says the Copy Change as it stands. A later edit rewrites it, and git keeps the old one.

**The commit.** A Copy Change and its Change Record go in the same commit. A commit that changes a Kit Copy and not its Change Record is stopped there. An Update Take is not a Copy Change, so its commits pass: together they replace every Kit Copy with the System Kit's, and clear every Change Record. Work never committed is lost, the Copy Change and its Change Record together.

**At the gate.** At the close of the System Repo's Plan Step, its Copy Changes are seen together, now that the whole step is seen. The agent compares the Kit Copies against where the step began, checks that each Copy Change has a Change Record that says it, and shows each with its Change Record. The human decides each, the agent proposing: kept, edited or reversed, its Change Record with it. One edited gets its Change Record rewritten. Copy Changes that share one reason are linked: the reason is written in full in one Change Record, and each other one says how its own Kit Copy was affected and points at that one. If the one holding the reason is reversed, the reason moves to one that stays, and the others point there.

**Its Adapted Cases:**
- the System Repo's, for changing a Kit Copy, itself a Kit Copy. It loads when a Kit Copy is touched, and says everything above but *At the gate*;
- the System Repo's gate list, for closing one of its Plan Steps. It loads when the step closes, and says *At the gate*.

**Open:**
- where the Change Record goes when the Kit Copy has no Adapted Understanding Text: §4, question 7, with its first guess;
- whether a reversed Copy Change leaves a trace for the Maintainer Repo. One tried and undone may be evidence that the Kit Copy was right. Its trigger: the first Copy Change reversed at a gate.

### 3.3 The Maintainer Repo's lessons

A lesson from the Maintainer Repo's own work starts in layer 4 of the right column. Since that work is done by its own Adapted Cases in place, the lesson changes layer 3 at once. It is then judged by the same questions 3 and 4 as a Copy Change read back, and goes up the arrow *lesson* as far as it holds (`temp/common-ground/system-repo-change-simulation.md` §5, *Judge Copy Changes*). If it reaches layer 1, it comes down the arrow *adapt*, to the System Repos' Adapted Cases too, and reaches System Repos by a Kit Update.

It has no Read Copy Changes, Deliver the Kit Update or Take the Kit Update of its own: nothing crosses between repos until a Kit Update carries it to a System Repo.

## 4. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **A Maintainer Kit:** should there be a kit a new Maintainer Repo is born from, as a System Repo is born from the System Kit? There is one Maintainer Repo so far. The Tiers Model has a rule for a second Concept Repo (`docs/models/tiers.md` §2.1, *The empty top tier*), and `cbc-concept`, once close to a second Maintainer Repo, ended as a rebuild and is kept only as a source (ADR-0082). §2.3.1 says what a Maintainer Kit would be made from.
2. **What layer 4 holds:** the general document's question (`temp/common-ground/knowledge-layers-general.md` §4, *Open questions*, question 5). Here it is met at a System Repo's design of its system and its own Knowledge on Trial.
3. **A name for the movement:** what runs from a Copy Change to the Update Take of the next Kit Update, as one thing (§3.2), so the simulation can name it.
4. **Where Judge Copy Changes sits:** §3.2 puts it at layer 3, since a Copy Change is judged against the Adapted Case its Kit Copy came from. The sources say only that it runs in the Maintainer Repo.
5. **Depth d and the layer above:** which other texts are checked for a loss that question 3 of Judge Copy Changes finds, and whether the idea above is reworded clearer when several lost the same part. Its first guess and its trigger are the simulation's (`temp/common-ground/system-repo-change-simulation.md` §5, *Judge Copy Changes*, step 1, *Open*).
6. **What then points at it:** the simulation's opening and the problem file's §2.1. Then `temp/`'s old files, one by one, and how today's ways are written across the drafts.
7. **What the System Kit holds:** layer 3 only, or the System Repos' Work Domain Ideas too. CBC system design adapted for backends (§2, the System Kit's item 2) may already be layer 2. Three cases the rule that each part is an Adapted Case (§2) does not yet cover:
   - an Instruction Text with no Adapted Understanding Text. A first guess: its System Kit Copy Change Record goes in a footer of the Instruction Text itself, as a record file carries its instructions in its header comment;
   - an Understanding Text with no Instruction Text, such as the description of CBC system design for a System Repo's readers (§2, the System Kit's item 5);
   - Knowledge on Trial in the System Kit: an Approach on Trial is one text of both kinds, not yet split, and today's deliveries carry it.
8. **Which other ideas are Backbone Ideas:** of today's project-agnostic ideas, beyond how an agent works and CBC design (§2.1).
9. **What one Adapted Case holds:** one Agent Skill or Agent Rule under its understanding text, or several. One understanding text may stand under more than one, as the facts-in-sync manual stands under two Agent Rules.
10. **Two Work Domain Ideas of how an agent works:** does an agent's work differ enough between keeping knowledge and designing a backend by CBC to need two texts, or would they be one text written twice (§2.2)?
11. **An Adapted Case from two ideas:** the cbc-framing Agent Skill holds CBC design's content, written as a piece of agent work. Is it adapted from two Work Domain Ideas, or from one, with the other giving only its form?
12. **When a change is judged:** a System Repo's Copy Change is judged before it reaches layer 3 (§3.2). The Maintainer Repo's own change reaches layer 3 at once, and is judged after (§3.3). Does the difference matter? The change work answers it.
13. **Knowledge on Trial offered back:** a System Repo's Knowledge on Trial is handed over at its close (§2.3). It is not a Copy Change, so the arrow *Copy Change, read back* does not carry it, and the picture has no arrow that does. The change work answers it, when the simulation takes its other sources.

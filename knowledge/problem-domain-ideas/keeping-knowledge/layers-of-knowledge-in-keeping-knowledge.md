# The layers of knowledge, in keeping knowledge

<!--
What it is: a Problem Domain Idea of the Maintainer Repo's own Problem Domain, keeping knowledge (§3.2), and its one home. Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/layers-of-knowledge.md, the layers in any Problem Domain. It adapts that document, and never retells it.
What stands on it: other texts point here, and never retell it.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Where it started: TODO-CONVERSATION-MEMORY.md §35, *The layers of knowledge*.
Its first sources, input and not rules:
- temp/common-ground/common-ground-problem.md §2.1 and §3;
- the simulation's six parts and depths, temp/common-ground/backend-repo-change-simulation.md;
- temp/model-example/idea-model-problem.md §1 and temp/model-example/layers.md;
- docs/models/tiers.md.
How it is edited: the picture and the text are checked against each other at every change, as the general document's header says.
-->

This document is the layers of knowledge in the Maintainer Repo's Problem Domain: where each layer is kept, and how knowledge travels between the Maintainer Repo and the Backend Repos. The layers themselves, and how knowledge moves between them, are the general document's (`knowledge/backbone-ideas/layers-of-knowledge.md`). The picture comes first; the text explains each of its labels.

## 1. Its Defined Terms

- **Backend Kit:** the Backend Repos' set of Adapted Cases at layer 3, which the Maintainer Repo keeps for them to work from; what it holds is listed in §3. Its originals stay in the Maintainer Repo, beside the Problem Domain Ideas they are adapted from; each Backend Repo works from copies, and takes the Backend Kit's changes by a Backend Kit Update.
- **Backend Kit Attention Note:** what a Backend Repo writes for the Maintainer Repo to look at in the Backend Kit, when no Backend Kit Copy Change carries it. Short form: **Attention Note**.
- **Backend Kit Copy:** a copy of a Backend Kit file, as it lives in a Backend Repo. Short form: **Kit Copy**.
- **Backend Kit Copy Change:** a Backend Repo's change to a Backend Kit Copy, made against the Backend Kit Version that copy came from. Short form: **Copy Change**.
- **Backend Kit Copy Change Record:** what a Backend Repo writes with each Backend Kit Copy Change, saying what changed and why. What it holds and where it sits are §4.2.1's. Short form: **Change Record**.
- **Backend Kit Update:** what the Maintainer Repo sends a Backend Repo: a copy of every Backend Kit file at one Backend Kit Version, with its Backend Kit Update Note. Short form: **Kit Update**.
- **Backend Kit Update Note:** what the Maintainer Repo writes with a Backend Kit Update, for the Backend Repo that takes it. Short form: **Update Note**.
- **Backend Kit Update Take:** a Backend Repo taking a Backend Kit Update into its Backend Kit Copies. How it runs is §4.2.6's. Its *version snapshot* is the Backend Repo's commit where the Backend Kit Update Take put every Backend Kit Copy at the new Backend Kit Version, its hash written beside that Backend Kit Version. Short form: **Update Take**.
- **Backend Kit Version:** the Backend Kit as it stood at one Maintainer Repo commit. Each Backend Repo records the one its Backend Kit Copies came from. Short form: **Kit Version**.
- **Backend Repo:** a repo of CBC backend design, where a real system is built by the concept, working from copies of the Backend Kit.
- **Backend Repo Reading:** the draft that lists the Backend Kit Copy Changes one Look for Lessons found in a Backend Repo, nothing judged. With none found, none is written. Short form: **Repo Reading**.
- **Look for Lessons:** the Maintainer Repo taking one Backend Repo's work since its *settled snapshot* into account: read, judged and acted on. How it runs is §4.2's.
- **Maintainer Repo:** the repo that keeps the understanding and the Backend Kit, and reads back what each Backend Repo learns.
- **Maintainer Repo Register:** the Maintainer Repo's list of its Backend Repos: where each lives, and its *settled snapshot*, the Backend Repo's snapshot up to which the Maintainer Repo has read, judged and acted on. The *settled snapshot* holds the Backend Kit Version the Backend Repo had then, which may be behind the newest. Short form: **Repo Register**.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Model | `docs/models/agent.md` |
| Agent Rule | `docs/conventions/agent-arrangement/` §3.2, *`.claude/rules/`* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Borrow Table | `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Failure Case | `temp/common-ground/common-ground-problem.md`, *Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Knowledge on Trial | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `docs/conventions/project-recording/` §2.1, *What a plan is* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Tiers Model | `docs/models/tiers.md` |
| Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The picture

```
          ┌┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐
          ┆ the Maintainer Repo                                                           ┆
          ┆  ┌─────────────────────────────────────────────────────────────────────────┐  ┆
 Layer 1  ┆  │ Backbone Ideas, bound to no Problem Domain:                             │  ┆
          ┆  │ understanding                                                           │  ┆
          ┆  └─────────────────────────────────────────────────────────────────────────┘  ┆
          ┆     │      ▲       ▲                                    ▲        ▲      │     ┆
          ┆   adapt lesson set apart                            set apart lesson  adapt   ┆
          ┆     ▼      │       │                                    │        │      ▼     ┆
          ┆  ┌───────────────────────────────────────────────┐  ┌──────────────────────┐  ┆
          ┆  │ CBC backend design,                           │  │ keeping knowledge,   │  ┆
 Layer 2  ┆  │ the Backend Repos'                            │  │ the Maintainer Repo's│  ┆
          ┆  │                                               │  │                      │  ┆
          ┆  │ understanding                                 │  │ understanding        │  ┆
          ┆  └───────────────────────────────────────────────┘  └──────────────────────┘  ┆
          ┆     │      ▲       ▲          │      ▲       ▲          │      ▲       ▲      ┆
          ┆   adapt lesson set apart    adapt lesson set apart    adapt lesson set apart  ┆
          ┆ ┌╌╌╌▼╌╌╌╌╌╌│╌╌╌╌╌╌╌│╌╌╌╌╌╌╌╌╌╌▼╌╌╌╌╌╌│╌╌╌╌╌╌╌│╌╌╌╌╌┐    │      │       │      ┆
          ┆ ╎┌──────────────────────┐  ┌──────────────────────┐╎    │      │       │      ┆
          ┆ ╎│ the Backend Repos'   │  │ the Backend Repos'   │╎    │      │       │      ┆
          ┆ ╎│ Adapted Cases for    │  │ Adapted Cases for    │╎    │      │       │      ┆
 Layer 3  ┆ ╎│ designing a backend  │  │ keeping knowledge    │╎    │      │       │      ┆
          ┆ ╎│ understanding and    │  │ understanding and    │╎    │      │       │      ┆
          ┆ ╎│ instructions         │  │ instructions         │╎    │      │       │      ┆
          ┆ ╎└──────────────────────┘  └──────────────────────┘╎    │      │       │      ┆
          ┆ ╎ the Backend Kit                                  ╎    │      │       │      ┆
          ┆ └╌╌╌╌╌╌╌╌╌╌╌╌│╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌▲╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘    │      │       │      ┆
          └┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄│┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐   │      │       │      ┆
                      birth,            Copy Change,            ┆   │      │       │      ┆
                    Kit Update           read back              ┆   │      │       │      ┆
                         ▼                   │                  ┆   ▼      │       │      ┆
              ┌─────────────────────────────────────┐           ┆ ┌────────────────────┐  ┆
 Layer 4      │ each Backend Repo's work,           │           ┆ │ its own work, by   │  ┆
              │ by its Kit Copies                   │           ┆ │ its own Adapted    │  ┆
              └─────────────────────────────────────┘           ┆ │ Cases, in .claude/:│  ┆
                                                                ┆ │ understanding and  │  ┆
                                                                ┆ │ instructions       │  ┆
                                                                ┆ └────────────────────┘  ┆
                                                                └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
```

Key: the dotted frame holds what the Maintainer Repo keeps. The dashed frame holds what the Backend Kit copies to each Backend Repo. On the right, the Maintainer Repo's own Adapted Cases sit in layer 4 with its work, in `.claude/`: they are written for this repo alone, and no Adapted Case of layer 3 holds them (§3.4).

## 3. The layers

Knowledge sits in four layers (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*). This section says where each is kept here, and what each holds so far. Layers 1 to 3 are kept in the Maintainer Repo, under `knowledge/`. Where each is kept, and how a new text is placed, is §3.5.

Each repo is a project of a Problem Domain (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*): a Backend Repo's is CBC backend design, and the Maintainer Repo's is keeping knowledge.

The Backend Kit is layer 3's set for the Backend Repos' Problem Domain, the picture's dashed frame, and what is copied to each Backend Repo. Each of its parts is an Adapted Case: an Adapted Understanding Text with its Instruction Text (§3.3). A part that has only one of the two is open (§5, question 6). So far it holds:

1. the Backend Repos' Adapted Cases for keeping knowledge, such as taking a Kit Update (§3.3.1);
2. their Adapted Cases for designing a backend: agent work, and CBC system design (§3.3.2);
3. the Defined Terms the Adapted Cases use;
4. the forms a Backend Repo's records start from. They go once, at birth, and are the Backend Repo's own after it;
5. a description of CBC system design for the Backend Repo's readers, as adapted to its kind of system. Its form is decided when the concept is split, and so is whether a Backend Repo may change it.

### 3.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.1, *The Backbone Idea layer*). Each row's description is a summary; the idea's home holds it.

| Backbone Idea | What it says | Home |
|---|---|---|
| The layers of knowledge | the layers knowledge sits in, and how it moves between them | `knowledge/backbone-ideas/layers-of-knowledge.md` |
| How an agent works | what one piece of agent work is: what the agent does, when, where and how | planned, from `docs/models/agent.md` (`TODO.md`, the item that rewrites the Agent Model) |
| CBC design | how a system is designed by CBC, for no one kind of system | planned, from `concept/` (`TODO.md`, the item that splits the concept) |
| Defined Terms | what a Defined Term is, and what keeps its meaning exact | `knowledge/backbone-ideas/defined-terms.md` |

Which other of today's project-agnostic ideas are Backbone Ideas is open (§5).

It is kept in the Maintainer Repo, and stays there. A Backend Repo receives it only adapted, in the Backend Kit.

### 3.2 The Problem Domain layer

Layer 2 holds Problem Domain Ideas (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The Problem Domain layer*), each a Backbone Idea of §3.1 adapted to one Problem Domain.

The Maintainer Repo keeps the Problem Domain Ideas of both Problem Domains so far, the picture's two boxes: its own, keeping knowledge, and the Backend Repos', CBC backend design. Keeping the Backend Repos' texts is part of its own work (§4.2). Each Problem Domain writes its own adaptation of a Backbone Idea, so both hold one of how an agent works.

In each table, a row's description is a summary; the idea's home holds it.

#### 3.2.1 Keeping knowledge

The Maintainer Repo's own Problem Domain. It works by its own Adapted Cases, written from these ideas (§3.4).

| Problem Domain Idea | Adapted from | What it adds | Home |
|---|---|---|---|
| The layers of knowledge, in keeping knowledge | The layers of knowledge | where each layer is kept; how knowledge travels between the repos | this document |
| Defined Terms, in keeping knowledge | Defined Terms | the mark; where each is defined; the Borrow Table; finding one | `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` |
| How an agent works, in keeping knowledge | How an agent works | not yet known | planned (`TODO.md`, the item that rewrites the Agent Model) |

#### 3.2.2 CBC backend design

The Backend Repos' Problem Domain. The Maintainer Repo keeps its Problem Domain Ideas and writes the Backend Kit's Adapted Cases from them. The work is done in each Backend Repo, by its Kit Copies (§3.4).

| Problem Domain Idea | Adapted from | What it adds | Home |
|---|---|---|---|
| CBC design, in CBC backend design | CBC design | backends as the kind of system | planned, from `concept/` (`TODO.md`, the item that splits the concept) |
| How an agent works, in CBC backend design | How an agent works | not yet known | planned (`TODO.md`, the item that rewrites the Agent Model) |
| Defined Terms, in CBC backend design | Defined Terms | the Backend Kit's Defined Terms, read in a Backend Repo without layers 1 and 2 | planned, with the first Adapted Case for the Backend Repos (ADR-0085, decision 4) |
| The layers of knowledge, in CBC backend design | The layers of knowledge | how a Backend Repo keeps its own knowledge, and takes the Backend Kit's changes | planned, with the first Adapted Case for the Backend Repos (`TODO.md`, the item "Split the Change idea") |

### 3.3 The Adapted Case layer

Layer 3 holds Adapted Cases (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.3, *The Adapted Case layer*), each written from a Problem Domain Idea of §3.2.

Here an Adapted Case is written for one piece of agent work, such as reading a Backend Repo, working one step of its Plan Step, or writing a commit message, or for what all of the agent's work uses, such as the Defined Terms. Its Instruction Text is anything the agent acts on in that work: an Agent Skill, an Agent Rule, the Defined Terms it writes by, or a record form it fills. How many one Adapted Case holds is open (§5). Its Adapted Understanding Text says why the Instruction Text is as it is. The agent uses the Instruction Text in the work, and reads the Adapted Understanding Text only when the Instruction Text is changed. The two travel together: a Backend Repo's Kit Copy holds both.

Layer 3 holds one set for each Problem Domain. So far there is one, the Backend Kit, for the Backend Repos'. The Maintainer Repo's Problem Domain has none, so its own Adapted Cases are layer 4 (§3.4). §3.3.1 and §3.3.2 list the Backend Kit's Adapted Cases in two groups: for keeping a Backend Repo's own knowledge, and for designing its backend. An Agent Skill or Agent Rule found both in the Backend Kit and among the Maintainer Repo's own is two Adapted Cases, one in each. The two are tied only through the nearest idea above them both (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.3, *The Adapted Case layer*).

Work no Adapted Case covers may write one of the repo's own, on trial: one kind of Knowledge on Trial (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*, the arrow *change*). It is layer 4, the repo's own (§3.4). A Backend Repo's Knowledge on Trial is kept in the Backend Repo, comes from no Kit Copy, and is handed over at its close.

#### 3.3.1 Keeping knowledge

The Backend Repos' Adapted Cases for keeping a Backend Repo's own knowledge, such as taking a Kit Update. They are written from §3.2.2's Problem Domain Ideas, and are part of the Backend Kit (§3.3.2).

#### 3.3.2 Designing a backend by CBC

The Backend Repos' Adapted Cases for designing a backend, in two groups so far, one for each Problem Domain Idea of §3.2.2 they are written from:

- **Agent work,** from how an agent works, designing a backend.
- **CBC system design,** from CBC design for backends. How it meets agent work in one Adapted Case is open (§5).

With the Backend Repos' group of §3.3.1, they are part of the Backend Kit (§3). Each Backend Repo works from Kit Copies of them (§3.4).

### 3.4 The layer of a repo's work

Layer 4 is one repo's work, and the repo's own texts (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.4, *The layer of work*). Here the work is a repo's:

- **Each Backend Repo's work, by its Kit Copies:** a Backend Repo is born with Kit Copies of the Backend Kit and works by them. A Kit Copy is a layer-3 text kept in the Backend Repo. As its work needs, it makes Copy Changes, so its Kit Copies differ from the Backend Kit on purpose. It is kept outside the Maintainer Repo, so every arrow between it and layer 3 crosses from one repo to the other.
- **The Maintainer Repo's own work, by its own Adapted Cases:** each is written for this repo alone, from a Problem Domain Idea of §3.2.1, mostly how an agent works, in keeping knowledge, so it is layer 4. They are kept in `.claude/`, where the agent loads them, and nothing is delivered. A change its work makes is, at once, a change to its own Adapted Case. If a kit for new Maintainer Repos is wanted, the part of them true for every Maintainer Repo is set apart up to layer 3 (§5, question 1). Its problem is keeping this knowledge, as a Backend Repo's is designing one system.

### 3.5 Where each layer is kept

Each layer has one folder, so a text's path says its layer:

- layer 1: `knowledge/backbone-ideas/`;
- layer 2: `knowledge/problem-domain-ideas/<Problem Domain>/`, such as `keeping-knowledge/`;
- layer 3: `knowledge/adapted-cases/<Problem Domain>/`, one set for each Problem Domain, not made until the first Adapted Case for the Backend Repos is written;
- layer 4, this repo's own Adapted Cases: whole in `.claude/`. The Instruction Text sits where its kind loads, such as `.claude/rules/`. The Adapted Understanding Text sits in `.claude/understanding/`, which never loads.

A Backend Repo's layer 4 is kept in the Backend Repo.

**Rules:**

- One folder per layer, and no number in a folder's name.
- A folder is made when its first file lands.
- A file is named after its idea, and its title matches. A layer-2 title is its layer-1 title, ", in" and its Problem Domain.
- A new idea gets its row in §3.1's or §3.2's table, with its Home.

## 4. How knowledge moves

How knowledge enters the layers and moves between them is the general document's (`knowledge/backbone-ideas/layers-of-knowledge.md` §4, *How knowledge moves*). This section adds the arrows between the Maintainer Repo and the Backend Repos, and how a Copy Change travels them.

### 4.1 The arrows

- **adapt,** **lesson** and **set apart,** between layers 1, 2 and 3: as the general document has them (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*). A lesson, or a part set apart, can come from either column.
- **birth,** layer 3 to layer 4: a new Backend Repo receives Kit Copies of the Backend Kit, at one Backend Kit Version.
- **Kit Update,** layer 3 to layer 4: a Backend Kit Update (§3) brings a Backend Repo's Kit Copies to a newer Backend Kit Version. The Backend Repo takes it by its own Kit Copy of the Adapted Case for taking a Kit Update.
- **Copy Change, read back,** layer 4 to layer 3: a Backend Repo changes a Kit Copy and records why. The Maintainer Repo reads it back and judges it against the Adapted Case the Kit Copy came from.
- **adapt,** **lesson** and **set apart,** between layer 2 and layer 4, in the right column: the Maintainer Repo's own Adapted Cases are written from its Problem Domain Ideas, and its lessons, and the parts it sets apart, go up to them (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*).

### 4.2 How a change travels

A Copy Change travels through six parts, each done by one repo. Each part sits at a layer, or on an arrow:

| Part | Who | Where in the picture |
|---|---|---|
| Change a Kit Copy | Backend Repo | layer 4, in a Kit Copy |
| Read Copy Changes | Maintainer Repo | the arrow *Copy Change, read back* |
| Judge Copy Changes | Maintainer Repo | layer 3: which layer the Copy Change holds for |
| Act on the verdicts | Maintainer Repo | the layer the verdict names; the arrows *lesson* and *adapt* |
| Deliver the Kit Update | Maintainer Repo | the arrow *Kit Update* |
| Take the Kit Update | Backend Repo | layer 4, its Kit Copies |

So the six parts are one movement: up from layer 4, as high as the Copy Change holds, and back down.

**The Look for Lessons.** Read Copy Changes, Judge Copy Changes and Act on the verdicts make one pass over one Backend Repo, the Look for Lessons. It starts when the human names a Backend Repo, for its lessons or to update it. It ends once Act on the verdicts is done, which sets the *settled snapshot* to the stop (§4.2.2). Its first step, two checks at main, sorts it into one of three cases (§4.2.2). Deliver the Kit Update and Take the Kit Update are outside it.

**Bringing a Backend Repo up to date.** It is a second job, which needs the first. It runs only when the human names the Backend Repo to update, and starts with a Look for Lessons. Its check, whether a Kit Update is due, belongs to Deliver the Kit Update. It comes after Act on the verdicts, since the Backend Kit moves for a Copy Change only once it is judged and acted on (§4.2.5).

Each of the simulation's depths names the highest layer a Copy Change reaches (§4.2.7). The arrows each travels:

| Depth | Arrows it travels |
|---|---|
| a. it stays in the Backend Repo | *Copy Change, read back*; nothing comes down |
| b. the Backend Kit's Adapted Case changes | *Copy Change, read back*; *Kit Update* |
| c, at layer 2. the idea above changes: its Problem Domain Idea | *Copy Change, read back*; *lesson*; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| c, at layer 1. the idea above changes: its Backbone Idea | *Copy Change, read back*; *lesson*, twice; *adapt*, to every text built on that idea, the Maintainer Repo's own when they stand on it; *Kit Update* |
| d. the idea above already holds it | *Copy Change, read back*; *adapt*; *Kit Update* |
| e. it asks to narrow the idea above | *Copy Change, read back*; *Kit Update* |
| f. several Adapted Cases need it, but not all | *Copy Change, read back*; *Kit Update* |

Depth f's gap, text shared by several Adapted Cases of one Problem Domain but not all, is the simulation's (§4.2.7, its row f).

#### 4.2.1 Change a Kit Copy

The Backend Repo changes a Kit Copy during its own work, and the gate of its Plan Step decides each Copy Change. How each rule was chosen is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §3, *Change a Kit Copy*).

**When a Kit Copy changes.** A Kit Copy changes only when the Backend Repo's work shows it does not fit what happened, never ahead. The human decides the Copy Change, the agent proposing. It is made then, with its Change Record. A Copy Change may be edited or reversed later, its Change Record with it.

**Where the Change Record sits.** In a footer of the Kit Copy's Adapted Understanding Text, which is not loaded for work. So the Copy Change and its why land in one diff, and the why cannot lose its Kit Copy. When only an Instruction Text changes, its Change Record goes there too.

**What the Change Record holds:**
- what changed, by meaning: the part, and what it says now. When some of the Adapted Case's texts were left as they were, it also says whether they still match the Copy Change (`temp/common-ground/common-ground-problem.md` §4, Failure Case 8);
- what happened, concretely, in the Backend Repo's own words. It is never written to sound general: rewording it is the Maintainer Repo's, after judging;
- which work found it;
- the Backend Repo's proposal, marked as one: its own problem, or one any repo would meet. The Maintainer Repo judges every Copy Change, and says whether it agrees, and why if not.

**When it is rewritten.** The Change Record says the Copy Change as it stands. A later edit rewrites it, and git keeps the old one.

**The commit.** A Copy Change and its Change Record go in the same commit. A commit that changes a Kit Copy and not its Change Record is stopped there. An Update Take is not a Copy Change, so its commits pass: together they replace every Kit Copy with the Backend Kit's, and clear every Change Record. Work never committed is lost, the Copy Change and its Change Record together.

**At the gate.** At the close of the Backend Repo's Plan Step, its Copy Changes are seen together, now that the whole step is seen. The agent compares the Kit Copies against where the step began, checks that each Copy Change has a Change Record that says it, and shows each with its Change Record. The human decides each, the agent proposing: kept, edited or reversed, its Change Record with it. One edited gets its Change Record rewritten. Copy Changes that share one reason are linked: the reason is written in full in one Change Record, and each other one says how its own Kit Copy was affected and points at that one. If the one holding the reason is reversed, the reason moves to one that stays, and the others point there.

**Its Adapted Cases:**
- the Backend Repo's, for changing a Kit Copy, itself a Kit Copy. It loads when a Kit Copy is touched, and says everything above but *At the gate*;
- the Backend Repo's gate list, for closing one of its Plan Steps. It loads when the step closes, and says *At the gate*.

**Open:**
- where the Change Record goes when the Kit Copy has no Adapted Understanding Text: §5, question 6, with its first guess;
- whether a reversed Copy Change leaves a trace for the Maintainer Repo. One tried and undone may be evidence that the Kit Copy was right. Its trigger: the first Copy Change reversed at a gate.

#### 4.2.2 Read Copy Changes

The Maintainer Repo finds what changed in one Backend Repo since it last looked, and lists it, judging nothing. How each rule was chosen is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §4, *Read Copy Changes*).

**How it starts.** The human decides which Backend Repo gets a Look for Lessons, and when. The human names a Backend Repo, for its lessons or to update it, and the agent compares its main with its *settled snapshot*. When the human asks which Backend Repos have new work, every one's main is compared with its *settled snapshot*, and nothing more is done. No state is kept: whether a Backend Repo has work comes from its main and the *settled snapshot*, never from a line someone must keep true.

**Where a stretch ends.** At the gate where one of the Backend Repo's Plan Steps closed, the last one on main. Main moves only at a gate's close, so main is always at a closed gate. Work past it, in a branch or not yet committed, is left for the next Look for Lessons. An open Plan Step changes nothing here: its work waits for the next Look for Lessons, and a Kit Update waits for the step's gate (§4.2.5). If a stretch's history is cleaned before main moves, the Change Records are unharmed: they are in the Kit Copies, not in the commits.

**Two snapshots.** Read Copy Changes compares two snapshots of the Backend Repo, the older snapshot and the stop, and never walks its commits. The commits between them are history, opened only to understand something deeper.
- **The older snapshot** is the Repo Register's *settled snapshot*, and it is never empty. At birth, the Maintainer Repo's check of the delivery writes the Backend Repo's row, its *settled snapshot* set to the start: the commit holding the Kit Copies as they arrived (`temp/common-ground/between-repos-simulation.md` §5.1, step 2). Nothing before the start is the Backend Repo's own Copy Change. So every Look for Lessons, the first among them, starts at the *settled snapshot*.
- **After an Update Take,** the first Look for Lessons starts at the *version snapshot* instead, found at main (§4.2.6, *At the Update Take, in order*, item 4). The *settled snapshot* still holds the Kit Copies of the previous Kit Version, and starting there would read the Update Take's changes as the Backend Repo's. The *version snapshot*'s Kit Copies are not checked against the new Kit Version: Deliver the Kit Update and the Update Take check the files three times before (§4.2.5; §4.2.6, items 2 and 6).
- **The stop** is the Backend Repo's main as it stands when the Look for Lessons begins, named by its commit. Everything is compared against that commit, never against main as it moves, so a commit landing during the Look for Lessons falls into the next one.
- **The Backend Repo's Kit Version** is read from the *settled snapshot*, never stored anywhere else. It may be behind the newest.

**Two checks at main,** both on whether there are Copy Changes to judge:
1. **main moved:** the Backend Repo's main against the *settled snapshot*;
2. **Copy Changes:** the Kit Copies, compared between the older snapshot and the stop. It is asked only when main moved.

A Look for Lessons ends in one of three cases:

| Case | Main moved | Kit Copy changed | What follows |
|---|---|---|---|
| *not moved* | no | — | nothing new; Act on the verdicts sets the *settled snapshot* to the stop, as it was |
| *no Copy Change* | yes | no | nothing is judged, no Repo Reading is written, and Act on the verdicts sets the *settled snapshot* to the stop |
| *Copy Change read* | yes | yes | the Copy Changes are listed in a Repo Reading, judged and acted on |

When the human named the Backend Repo to update, the check in Deliver the Kit Update follows, once Act on the verdicts is done.

**Finding each Copy Change.** Each Kit Copy in the Backend Kit's folders, a new file among them, is compared between the older snapshot and the stop. A Change Record lands in the same diff as its Copy Change, so pairing them is reading one diff. Three things can come out:
- a Copy Change with its Change Record: read with its what, what happened, which work found it, and the Backend Repo's proposal;
- a Copy Change with no Change Record: read from the comparison alone, and marked "no entry";
- a Change Record changed with no Copy Change, as when a why is rewritten: read as a change of its why.

The agent only reads the Backend Repo, and writes only in the Maintainer Repo.

**The Repo Reading.** One line per Copy Change, nothing judged. A line holds the Kit Copy and its part, what it says now, what happened, which work found it, and the Backend Repo's proposal, marked as one. A Copy Change with no Change Record says "no entry". Copy Changes linked by one reason are listed together, under it. The Repo Reading names its stop. When the list is empty, none is written. The human checks that the list is whole; then it is judged. The Repo Reading stays a draft, and goes once its work is done.

**When the stop moves.** Act on the verdicts sets the *settled snapshot* to the stop, in the Repo Register, at every Look for Lessons, whether or not a Copy Change was found. With no verdicts, that is right after judging. It never moves before: a Look for Lessons left half done must not mark its Copy Changes taken into account. Whether the Backend Repo takes the Kit Update does not hold it back.

**Its Adapted Cases:**
- the Backend Repo's gate list: main moves only at a gate's close. It is there today;
- the Maintainer Repo's, for reading a Backend Repo's Copy Changes. It loads when the human names a Backend Repo, for its lessons or to update it, or asks which have new work, and says everything above.

**Open:** a Backend Repo nobody names gets no Look for Lessons until its work resumes. Its trigger: the first lesson found late because a Backend Repo went without one.

#### 4.2.3 Judge Copy Changes

The Maintainer Repo judges each line of the Repo Reading, and writes its verdict. How each rule was chosen is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §5, *Judge Copy Changes*).

**Who judges.** The agent proposes an answer to each question, with what it read; the human decides each line. The Backend Repo's own view of its Copy Change is input, never the verdict. An empty list gives no verdicts, and only the stop goes on to Act on the verdicts.

**Question 0, first.** Is the Copy Change sound? It reads what happened, the Copy Change and the original part: does the Copy Change fix what happened, without breaking something the Kit Copy did? An unsound Copy Change goes no further: the depth questions are not asked, and the verdict says why.

**The four questions.** A sound line is judged by four questions, in order, the cheapest first, until one holds:
1. **Did the Kit Copy already say this?** Then it is a misreading (`temp/common-ground/common-ground-problem.md` §4, Failure Case 7), and nothing changes but, perhaps, the Backend Kit's wording. It reads the original part, in the Kit Version the Kit Copies came from, beside the Copy Change. When the Backend Kit has moved since, its part as it is now is read too: a change the Backend Kit has since made the same way covers it, and nothing new is made, so one lesson is not made twice.
2. **Is it specific to that Backend Repo's problem?** Then nothing changes here. It reads what happened, the Backend Repo's proposal, and its framing of its problem.
3. **Does the idea above already hold it,** the Problem Domain Idea above the Adapted Case, or the Backbone Idea above that? Then the Adapted Case lost it in narrowing, and is fixed from the idea above. When only the Backbone Idea holds it, the Problem Domain Idea lost it too: the loss sits at layer 2, and the Problem Domain Idea is fixed first. A part lost in narrowing has no mark, and one left out on purpose has its mark, so the two are told apart (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*, its **Rules**, *Narrowing, never shrinking*).
4. **How high is it true?** A lesson goes as high as it is true (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.1, *How the layers fill*). 4a, still true naming no Adapted Case: a lesson for its Problem Domain Idea, layer 2. 4b, still true naming no Problem Domain: a lesson for its Backbone Idea, layer 1 (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*, its **Rules**).

If none holds, it is a lesson for its Adapted Case, depth b: the Adapted Case gains it, and the idea above stays as it is. For depth c, how question 4 is answered is not yet done: its first guess is under *Open*.

**From the reason, never the wording.** The depth comes from the reason, never the edit. A cap raised from 50 to 60 is the Backend Repo's own, depth a, when its reason is "our scope names are long". The same edit is a lesson for its Problem Domain Idea, depth c at layer 2, when its reason is "the cap counts the scope, which any repo with scopes meets". A Copy Change worded for one project may still be a lesson for every repo: the Backend Repo writes in its own words on purpose (§4.2.1), and making a lesson general is rewording, after judging (§4.2.4). The agent's answer to question 2 says whether it agrees with the Backend Repo's proposal, and why if not.

**Lines together, lines split.** Lines listed together under one reason are judged together, and the reason is judged once. A line whose parts answer differently is split, each part judged on its own; the parts keep their one Change Record.

**A line with no Change Record.** Its why is looked for in the Backend Repo first, in the commit that made the Copy Change and in the Backend Repo's records, then asked of the human. The line says where its why was found, and is held while neither gives it.

**The verdict.** Each judged line, or part of one, gets a verdict, the agent drafting and the human deciding. It holds the answer, its why, and one line on the proposal: "the proposal holds" or "the proposal does not hold, because …". It is the Maintainer Repo's decision, written for its own work: what it changes starts from it. A verdict is one of:
- unsound, saying what the Copy Change breaks or leaves unfixed;
- misread, question 1;
- covered by a Backend Kit change since the Backend Repo's Kit Version, question 1;
- its own, question 2, depth a;
- lost in narrowing, question 3, depth d;
- a lesson for its Problem Domain Idea, question 4a, depth c at layer 2;
- a lesson for its Backbone Idea, question 4b, depth c at layer 1;
- a lesson for its Adapted Case, depth b;
- held, with its trigger.

Lines under one reason share one verdict, and each line says how its own Kit Copy is affected. No verdict goes down to the Backend Repo, and what becomes of a Copy Change the Backend Kit does not take is not ruled (§4.2.7, *Known, not ruled*). What the Backend Repo gets reaches it with the next Kit Update.

**Its Adapted Case.** The Maintainer Repo's, for judging a Repo Reading. It loads when the human starts judging a Repo Reading whose list was checked whole, and says everything above.

**Open:**
- how question 4 is answered, and by whom. A first guess, not a rule: 4a first, and 4b only if 4a holds. 4a is the cheaper check, inside one Problem Domain, and a lesson still true naming no Problem Domain is true across its own. Its trigger: depth c checked against these rules (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it"), or the first lesson judged at layer 1;
- which other texts are checked for a loss question 3 finds. Nothing comes down the arrow *adapt*, since the idea above did not change (`knowledge/backbone-ideas/layers-of-knowledge.md` §5, *Open questions*, question 3). A first guess: the texts built on the idea that holds the part, as the survey asks (§4.2.4). If several lost it, the idea's wording may be too weak, and is reworded clearer, never narrower. Its trigger: the first depth-d verdict;
- whether an unsound verdict offers a fix. Its trigger: the first unsound verdict.

#### 4.2.4 Act on the verdicts

The Maintainer Repo makes what each verdict asks, then moves the *settled snapshot*. How each rule was chosen is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §6, *Act on the verdicts*).

**What each verdict asks.** From each verdict, the Maintainer Repo makes what its depth asks, the agent drafting and the human deciding. For depth b, the lesson is reworded for every Backend Repo, and the Backend Kit's Adapted Case gains it. It is committed in the Maintainer Repo, and the Backend Kit stands at a new Kit Version. The Backend Repo the lesson came from gets it back with the next Kit Update, though its Kit Copy already holds the Copy Change in its own words.

**The other depths, not yet done.** This part holds their work too, each checked here later:
- depth c changes the idea above at its layer, after the survey: its Problem Domain Idea at layer 2, its Backbone Idea at layer 1;
- depth d fixes the Adapted Case from the idea above, after fixing the Problem Domain Idea from its Backbone Idea when the loss sits at layer 2;
- depth e marks a narrowing with its why, in the text just below the idea that does not fit.

**The survey.** Before a lesson enters the idea above, every other text built on that idea is asked whether it fits, the one the lesson came from excepted (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*, its **Rules**; §3.3, *The Adapted Case layer*). At layer 2, that is the other Adapted Cases of that Problem Domain Idea, the Maintainer Repo's own only when they share it. At layer 1, it is every Problem Domain Idea on that Backbone Idea. It is the arrow *adapt*'s check, run before the idea changes, so a conflict shows first. Each text answers "holds as it is", "must change", with what and why, or "conflicts", with why. A conflict is input to the human's decision, never a veto, and what the survey finds must change, changes. Its answers are also evidence for question 4: if every answer conflicts, the lesson is not true that high.

**Rewording.** A lesson is reworded here, never before: for every Backend Repo at depth b; at depth c, naming no Adapted Case at layer 2, and no Problem Domain at layer 1 (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*, its **Rules**).

**Then the stop moves.** Once the verdicts are acted on, the Repo Reading goes: nothing in the Kit Update is read from it. Act on the verdicts sets the *settled snapshot* to the stop, in the Repo Register (§4.2.2). With no verdicts, as in cases *not moved* and *no Copy Change*, that is all it does.

**Its Adapted Case.** The Maintainer Repo's, for judging a Repo Reading, which says everything above.

**Open:**
- at layer 1, how far down the survey reaches before the change: only the Problem Domain Ideas, each checking its own Adapted Cases when it changes, or every Adapted Case below them at once. The first is cheaper; the second may catch a conflict two layers down. Its trigger: the first lesson judged at layer 1;
- how a part of a Backbone Idea is known not to fit a whole Problem Domain, when one Backend Repo's Copy Change shows one Adapted Case. A first guess: the same survey, over that Problem Domain Idea's Adapted Cases. Its trigger: the first depth-e verdict;
- whether a Look for Lessons is one of the Maintainer Repo's Plan Steps, and whether Act on the verdicts gets an Adapted Case of its own, apart from the one for judging a Repo Reading. Today a Repo Reading is one of the Maintainer Repo's Plan Steps, and its work follows it. Its trigger: the Adapted Case texts written from these rules.

#### 4.2.5 Deliver the Kit Update

The Maintainer Repo makes a Kit Update for one Backend Repo, when its work resumes, and stages it there. How each rule was chosen is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §7, *Deliver the Kit Update*).

**When one is due.** A Kit Update is due when the Backend Repo's Kit Version, which the Backend Repo holds, is behind the newest. It goes only when it carries a Backend Kit change. Two Kit Versions are compared by the Backend Kit's files at their two commits, never by the commits themselves: a Maintainer Repo commit that touches no Backend Kit file leaves every Backend Repo where it was. A Backend Repo cannot see the Maintainer Repo, so it cannot learn this itself. For depth b, the Backend Kit has moved for the Copy Change, so a Kit Update is due: it carries the Backend Kit's Adapted Case at the new Kit Version, with the lesson as its why. Depth c is not yet walked through this part (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it").

**When the check runs.** Only when work resumes. Work resumes when the human, about to open the Backend Repo's next Plan Step, names it to update; neither repo can see that moment itself (§4.2.6). Nothing is made for, or sent to, a Backend Repo whose work has not resumed. Then, in order:
1. a Look for Lessons runs (§4.2.2). It comes first: a Kit Update is built against the *settled snapshot*, and a Copy Change not yet taken into account would make the Update Take refuse it;
2. the Kit Versions are compared. When the Backend Repo's is the newest, nothing follows;
3. the agent checks that none of the Backend Repo's Plan Steps is open. If one is, it says so, and makes nothing: finishing that step would move main, and the Update Take would refuse the Kit Update too;
4. the Kit Update is made, the agent drafting and the human deciding.

When the human only asks which Backend Repos are behind, the Kit Versions are compared, and nothing is made.

**What a Kit Update is.** Two things: every Kit Copy, whole, at the newest Kit Version, and an Update Note. The Backend Repo then has the new version of each file, and finds its old one in its own history. The Update Note holds:
- the new Kit Version;
- the Backend Repo's *settled snapshot* it was built against, whether a Repo Reading was written or not. The Update Take checks it before anything moves. The Update Note names the check, so a Backend Repo whose Adapted Case for taking is older still meets it;
- what changed since the Backend Repo's Kit Version, from the same comparison of files: each path changed, new, gone or renamed, and how many. The Backend Repo checks the files against it when they arrive, and a file that is gone cannot say so itself;
- the why of each Backend Kit change since then, whatever its source: a Look for Lessons at this Backend Repo or at another, or the Maintainer Repo's own work. It is read from the bodies of the Maintainer Repo's commits that changed a Backend Kit file between the two Kit Versions, since a body says why (`docs/conventions/commit-messages/` §1, *What a commit message is*). Each why stands on its own, and names no other repo; a change that comes from a lesson, at any depth, quotes the lesson as it was reworded (§4.2.4). With it, the Backend Repo judges a change against its own needs without seeing the Maintainer Repo;
- which files are taken first: the Adapted Case for taking a Kit Update, so a Kit Update is never taken by instructions older than it (`temp/common-ground/common-ground-problem.md` §4, Failure Case 10);
- the Kit Update it replaces, when one was waiting.

The Update Note is no summary of the Maintainer Repo's work, which the Backend Repo cannot check. It is not a record either: it goes once the Kit Update is taken, and what the Backend Repo decides goes in its records. Nothing in it cites what the Backend Repo cannot open: no path, record or word of the Maintainer Repo's own.

**One at a time.** A Repo Reading stays open until its verdicts are acted on. One Repo Reading is open per Backend Repo at a time: a Repo Reading made while one is open extends it, and its lines are judged with the rest, so judging already done is kept. One Kit Update waits for the Backend Repo at a time: a newer one replaces one not yet taken, since it carries every Backend Kit change since the Kit Copies' Kit Version.

**Staging.** A Kit Update reaches the Backend Repo on the human's word, in a step of its own: nothing crosses without that word. It is staged by the human, or by the agent, which never stages unasked. The Backend Repo's tree is checked clean first, with no work under way; when it is not, the agent says what it found and waits for the word. The Kit Update is written only into the Backend Repo's `temp/`, nowhere else there, and replaces one already waiting. Nothing in `temp/` is in force until the Backend Repo takes it. The Kit Update is named by the Maintainer Repo's commit at which its files and Update Note were final, so its Kit Version is exact. Once staged, each file is compared with the new Kit Version; the Backend Repo checks the Update Note against the files when it takes them.

**Its Adapted Cases:**
- the Maintainer Repo's, for making a Kit Update. It loads on the human's word to update a Backend Repo, and says everything above but *Staging*;
- the Maintainer Repo's, for delivering a Kit Update. It loads on the human's word to deliver, and says *Staging*.

#### 4.2.6 Take the Kit Update

The Backend Repo takes a waiting Kit Update, at the opening of its next Plan Step. How each rule was chosen is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §8, *Take the Kit Update*).

**Before the Update Take.** A Kit Update is taken between two of the Backend Repo's Plan Steps, when the next is about to open, never in the middle of one, the agent proposing and the human deciding. Before that step opens, in a fixed order: a Look for Lessons runs to main, and the Backend Repo's Kit Update, when one is due, is made, delivered and taken. Then the step opens on the new Kit Copies, or on the same ones when no Kit Update was due. An open Repo Reading is extended. The human works on one project at a time, so the Backend Repo waits at little cost. A Backend Repo's Plan Step open when the human returns finishes on the old Kit Copies first, and the human names the Backend Repo to update at the next opening (§4.2.5). The Update Take checks first, from the Update Note, what the Backend Repo itself can see:
- case 1, its main is still the *settled snapshot* the Update Note names: the Kit Update is taken. Its Kit Version needs no check of its own: it is recorded in main, so it cannot change while main stands still;
- case 2, anything else: there is no Update Take, and the Backend Repo says so. The human names it to update again, and the Look for Lessons finds that main has moved (§4.2.2). The check in Deliver the Kit Update then finds a new Kit Update due, made against the Backend Kit as it is now, and it replaces the waiting one (§4.2.5).

**When the Backend Kit moves on.** The Backend Kit may move after the Kit Update is made. That is no reason to refuse the Kit Update: it is correct, if not the latest, and the next brings the rest.

**At the Update Take, in order.** Once the check finds case 1, the Update Take cuts a branch from main, the *settled snapshot*. Its first commit is the Kit Update as it arrived, in `temp/`, not yet in force: a record of what came, before the Update Take changes anything. Each item below is then a commit of its own, but item 2, a check. Main moves to the branch's last commit by fast-forward at the gate's close, so it still moves only at a gate's close (§4.2.2).
1. the Adapted Case for taking a Kit Update is taken first, on its own, so the rest is taken by the new one (`temp/common-ground/common-ground-problem.md` §4, Failure Case 10);
2. the files are checked against the Update Note: what changed, and how many (§4.2.5). A mismatch is said before anything moves;
3. every Kit Copy is taken whole, at the new Kit Version; each path gone is removed, and each renamed is moved. A part the Backend Repo never changed is taken, and work shows whether it fits (§4.2.1). A Kit Copy taken whole takes its Change Records away with it, so clearing them is no act of its own. Nothing is lost: main is the *settled snapshot*, so each was read and judged;
4. the new Kit Version is recorded, with the commit that holds it: item 3's, the *version snapshot*, every Kit Copy at the new Kit Version. So the check in Deliver the Kit Update can compare it with the newest. It names item 3's commit because a commit cannot hold its own hash, and item 3's is the last before it;
5. the Kit Update and its Update Note are removed from `temp/`;
6. the Update Take's gate, last. It checks that the Update Take finished: the files matched the Update Note, every Kit Copy is at the new Kit Version, the Kit Version is recorded, and `temp/` holds no Kit Update.

**What a Change Record stands against.** Every Change Record stands against the last Kit Version taken, or birth's, and every Change Record goes at an Update Take. This is confirmed at the first Kit Update to reach a Backend Repo whose Kit Copies have Change Records.

**Its Adapted Case.** The Backend Repo's, for taking a Kit Update, itself in the Kit Update and taken first. It loads when the Backend Repo's next Plan Step opens with a Kit Update waiting, and says everything above.

**Open:**
- finished work done under a rule the Kit Update changed may now be wrong. New work follows the new Kit Copy; the Backend Repo lists which Backend Kit changes touch rules its finished work followed, and the human decides. Its trigger: the first Kit Update that changes a rule one of the Backend Repo's finished Plan Steps followed;
- postponing an Update Take after its Kit Update is staged, so the step opens on the old Kit Copies and the Kit Update waits. For now there is no such choice: a staged Kit Update is taken at the opening, unless the Update Take's check finds main moved (case 2). Once an Update Take can be postponed, main can move before it, so decide then whether the Maintainer Repo must check main before delivery, and whether main alone is enough: a Plan Step on a branch leaves main where it is. Its trigger: the first staged Kit Update the human does not want taken;
- dropping or restarting the Backend Repo's open Plan Step so the Kit Update is taken sooner, when the Kit Update changes a rule the step rests on. Its trigger: the first Kit Update the human wants taken before an open step finishes;
- whether each opening of the Backend Repo's Plan Steps asks: was this Backend Repo named to update? Without that question, a Backend Repo nobody names opens each step on the old Kit Copies, and falls further behind each time. Its trigger: the first time one of the Backend Repo's Plan Steps opens on old Kit Copies because nobody named the Backend Repo to update;
- where in the Backend Repo the Kit Version and the *version snapshot*'s hash are written. Today an Update Take writes one entry with the new Kit Version (`delivery/container/.claude/rules/delivered-copies.md`, rule 5). Its trigger: the Adapted Case for taking a Kit Update written from these rules.

#### 4.2.7 The cases

A Copy Change varies in two ways. What was changed varies how the Backend Repo records it, and how the Maintainer Repo finds it; it is the same however deep the Copy Change turns out to go, since that is known only once it is judged. How deep it goes varies how the Maintainer Repo decides, and how the Kit Update is written. The rules above are worked for the first case and depth b. Each row not yet checked is checked when practice first meets it, depth c's by its own item (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it"). How each case was weighed is the simulation's (`temp/common-ground/backend-repo-change-simulation.md` §2, *The cases*).

| Kind | Case | Status | Differs so far |
|---|---|---|---|
| what changed | one Adapted Case, any of its texts | worked, §4.2.1 to §4.2.6 | — |
| what changed | a Defined Term | not yet checked | — |
| what changed | delivered Knowledge on Trial | not yet checked | read: compared like any Kit Copy; decided: the original was never proven, so the Copy Change is evidence for its trial |
| what changed | one reason behind Copy Changes to several Adapted Cases | not yet checked | recorded: one why, naming every Kit Copy it changed; read: the Copy Changes are listed together |
| how deep | b. the Backend Kit's Adapted Case changes: layer 3 | worked, §4.2.3 to §4.2.6 | — |
| how deep | c, at layer 2. the idea above changes: its Problem Domain Idea | not yet checked | the other Adapted Cases of that Problem Domain Idea are surveyed, the Maintainer Repo's own only when they share it (§4.2.4) |
| how deep | c, at layer 1. the idea above changes: its Backbone Idea | not yet checked | every Problem Domain Idea on that Backbone Idea is surveyed; how far down the survey reaches is open (§4.2.4) |
| how deep | d. the idea above already holds it: layer 3, or layer 2 | not yet checked | the loss sits at layer 2 when the Problem Domain Idea lost a part its Backbone Idea holds: the Problem Domain Idea is fixed from its Backbone Idea, then the Adapted Case from the Problem Domain Idea. Which other texts are checked for the same loss is open (§4.2.3) |
| how deep | e. it asks to narrow the idea above: layer 3, or layer 2 | not yet checked | the narrowing goes into the text just below the idea that does not fit, marked with its why (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.2, *The arrows*, its **Rules**, *Narrowing, never shrinking*): the Adapted Case, or the Problem Domain Idea when a part of its Backbone Idea does not fit its whole Problem Domain. How that is known is open (§4.2.4) |
| how deep | f. several Adapted Cases need it, but not all: no layer | not yet checked | it cannot enter the idea above. When it holds for every Adapted Case of one Problem Domain, it is depth c, at layer 2. One case is left: several Adapted Cases of one Problem Domain, but not all. Across Problem Domains, each writes it into its own adaptation (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The Problem Domain layer*, its **Rules**). Each Adapted Case gains it, and the same text has no shared home. Open; its trigger: the first change two Adapted Cases need, but not every one |

How deep a Copy Change goes is how high it goes: each depth names the highest layer it changes, since a lesson goes as high as it is true (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.1, *How the layers fill*). The idea above is the Problem Domain Idea an Adapted Case is written from, or the Backbone Idea that one is adapted from.

A stretch of work may hold several Copy Changes, alike or mixed. Each is recorded and read on its own, so they add no row but one: one reason behind Copy Changes to several Adapted Cases.

New text of the Backend Repo's own, on trial, is not a case here. It comes from no Kit Copy, so it is not a Copy Change. It is Knowledge on Trial, handed over at the Backend Repo's close (§3.3). It is one of the other sources, below.

**Known, not ruled.** These can happen, and have no rules until practice meets them. Rules once written for them are in git. Each says what can happen, and its trigger:

- **an Attention Note:** a Backend Repo has something for the Maintainer Repo that no Copy Change carries: a misfit worked around with no Copy Change made, a doubt about a line left as it is, something the Backend Kit lacked, a Kit Copy no longer used. Its trigger: the first such thing a Backend Repo needs to tell.
- **a Copy Change the Backend Kit does not take:** judged its own, depth a, the Copy Change staying in the Backend Repo at layer 4; or unsound, misread or held. It stays only in the Backend Repo's Kit Copy, and the Update Take takes every Kit Copy whole. Whether the Kit Copy keeps it past the Update Take is not ruled. Only such a verdict lets a Look for Lessons end in *Copy Change read* with no Kit Update due after (§4.2.5). Its trigger: the first such verdict.
- **a verdict sent down:** a verdict the Backend Repo would act on: unsound, misread, or a proposal that did not hold. In the case worked, every Copy Change is taken, and the Kit Update brings it back with the lesson as its why. A proposal that did not hold is cleared with its Change Record at the Update Take, and the human already decided it when it judged Copy Changes (§4.2.3). Today's Update Note sends every verdict (`docs/conventions/exchange/` §6.5, *Verdicts*). Its trigger: the first Copy Change the Backend Kit does not take, or a Backend Repo that needs a verdict it was not sent.

**Other sources.** A Copy Change is one source of new knowledge. Others exist, and are not yet taken into account here, each left on purpose until Change is finished:
- a lesson found in the Maintainer Repo's own work (§4.3). Its start may differ (`TODO.md`, the item "Simulate depth c, then bring the Change idea to it");
- Knowledge on Trial a Backend Repo hands over at its close (§5, question 11);
- new knowledge from the human.

Birth stays outside, as the start: it gives a Backend Repo its first Kit Copies and its *settled snapshot* (§4.2.2).

### 4.3 The Maintainer Repo's lessons

A lesson from the Maintainer Repo's own work starts in layer 4 of the right column. Since that work is done by its own Adapted Cases, kept with it, the lesson changes its own Adapted Case at once. It is then judged by the same questions 3 and 4 as a Copy Change read back, and goes up the arrow *lesson* as far as it holds (§4.2.3). If it reaches layer 1, it comes down the arrow *adapt*, to the Backend Repos' Adapted Cases too, and reaches Backend Repos by a Kit Update.

It has no Read Copy Changes, Deliver the Kit Update or Take the Kit Update of its own: nothing crosses between repos until a Kit Update carries it to a Backend Repo.

## 5. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **A kit for new Maintainer Repos:** should there be a kit a new Maintainer Repo is born from, as a Backend Repo is born from the Backend Kit? There is one Maintainer Repo so far. The Tiers Model has a rule for a second Maintainer Repo (`docs/models/tiers.md` §2.1, *The empty top tier*), and `cbc-concept`, once close to a second Maintainer Repo, ended as a rebuild and is kept only as a source (ADR-0082). §3.4 says what such a kit would be made from.
2. **A name for the movement:** what runs from a Copy Change to the Update Take of the next Kit Update, as one thing (§4.2), so the simulation can name it.
3. **Where Judge Copy Changes sits:** §4.2 puts it at layer 3, since a Copy Change is judged against the Adapted Case its Kit Copy came from. The sources say only that it runs in the Maintainer Repo.
4. **Depth d and the layer above:** which other texts are checked for a loss that question 3 of Judge Copy Changes finds, and whether the idea above is reworded clearer when several lost the same part. Its first guess and its trigger are §4.2.3's, under *Open*.
5. **What then points at it:** the simulation's opening and the problem file's §2.1. Then `temp/`'s old files, one by one, and how today's ways are written across the drafts.
6. **What the Backend Kit holds:** only its Problem Domain's Adapted Cases, or the Backend Repos' Problem Domain Ideas too. CBC system design adapted for backends (§3, the Backend Kit's item 2) may already be layer 2. Three cases the rule that each part is an Adapted Case (§3) does not yet cover:
   - an Instruction Text with no Adapted Understanding Text. A first guess: its Backend Kit Copy Change Record goes in a footer of the Instruction Text itself, as a record file carries its instructions in its header comment;
   - an Understanding Text with no Instruction Text, such as the description of CBC system design for a Backend Repo's readers (§3, the Backend Kit's item 5);
   - Knowledge on Trial in the Backend Kit: today's, for ways of working, is one text of both kinds, not yet split, and today's Kit Updates carry it.
7. **Which other ideas are Backbone Ideas:** of today's project-agnostic ideas, beyond how an agent works and CBC design (§3.1).
8. **What one Adapted Case holds:** one Agent Skill or Agent Rule under its understanding text, or several. One understanding text may stand under more than one, as the facts-in-sync manual stands under two Agent Rules.
9. **An Adapted Case from two ideas:** the cbc-framing Agent Skill holds CBC design's content, written as a piece of agent work. Is it adapted from two Problem Domain Ideas, or from one, with the other giving only its form?
10. **When a change is judged:** a Backend Repo's Copy Change is judged before it reaches layer 3 (§4.2). The Maintainer Repo's own change reaches its own Adapted Case at once, and is judged after (§4.3). Does the difference matter? The change work answers it.
11. **Knowledge on Trial offered back:** a Backend Repo's Knowledge on Trial is handed over at its close (§3.3). It is not a Copy Change, so the arrow *Copy Change, read back* does not carry it, and the picture has no arrow that does. The change work answers it, when the simulation takes its other sources.
12. **A table of this repo's own Adapted Cases:** §3.1 and §3.2 list their layers' texts in tables, and §3.4 lists none. Should it, beside them? With one, Defined Terms, a table adds little. Its trigger: the second of this repo's own Adapted Cases.

# The layers of knowledge, in keeping knowledge

<!--
What it is: a Problem Domain Idea of the Maintainer Repo's own Problem Domain, keeping knowledge (§3.2), and its one home. Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/layers-of-knowledge.md, the layers in any Problem Domain. It adapts that document, and never retells it.
What stands on it: other texts point here, and never retell it. knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md, Change, in keeping knowledge, borrows where each layer is kept, and so does knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md, Change, in CBC backend design.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Where it started: TODO-CONVERSATION-MEMORY.md §35, *The layers of knowledge*.
Its first sources, input and not rules:
- temp/common-ground/common-ground-problem.md §2.1 and §3;
- the simulation's six parts and depths, temp/common-ground/backend-repo-change-simulation.md;
- temp/model-example/idea-model-problem.md §1 and temp/model-example/layers.md;
- docs/models/tiers.md.
How it is edited: the picture and the text are checked against each other at every change, as the general document's header says. It draws what is where; how knowledge travels between the repos is Change, in keeping knowledge's (ADR-0088, decision 8).
-->

This document is the layers of knowledge in the Maintainer Repo's Problem Domain: where each layer is kept. How knowledge travels between the Maintainer Repo and the Backend Repos is Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`). The layers themselves are the general document's (`knowledge/backbone-ideas/layers-of-knowledge.md`), and how knowledge moves between them is Change's (`knowledge/backbone-ideas/change.md`). The picture comes first; the text explains each of its labels.

## 1. Its Defined Terms

- **Backend Kit:** the Backend Repos' set of Adapted Cases at layer 3, which the Maintainer Repo keeps for them to work from; what it holds is listed in §3. Its originals stay in the Maintainer Repo, beside the Problem Domain Ideas they are adapted from; each Backend Repo works from copies, and takes the Backend Kit's changes by a Backend Kit Update.
- **Backend Kit Copy:** a copy of a Backend Kit file, as it lives in a Backend Repo. Short form: **Kit Copy**.
- **Backend Repo:** a repo of CBC backend design, where a real system is built by the concept, working from copies of the Backend Kit.
- **Maintainer Repo:** the repo that keeps the understanding and the Backend Kit, and reads back what each Backend Repo learns.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Rule | `docs/conventions/agent-arrangement/` §3.2, *`.claude/rules/`* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Borrow Table | `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Knowledge on Trial | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
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
          ┆                                                                               ┆
          ┆  ┌───────────────────────────────────────────────┐  ┌──────────────────────┐  ┆
          ┆  │ CBC backend design,                           │  │ keeping knowledge,   │  ┆
 Layer 2  ┆  │ the Backend Repos'                            │  │ the Maintainer Repo's│  ┆
          ┆  │                                               │  │                      │  ┆
          ┆  │ understanding                                 │  │ understanding        │  ┆
          ┆  └───────────────────────────────────────────────┘  └──────────────────────┘  ┆
          ┆                                                                               ┆
          ┆ ┌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┐                          ┆
          ┆ ╎┌──────────────────────┐  ┌──────────────────────┐╎                          ┆
          ┆ ╎│ the Backend Repos'   │  │ the Backend Repos'   │╎                          ┆
          ┆ ╎│ Adapted Cases for    │  │ Adapted Cases for    │╎                          ┆
 Layer 3  ┆ ╎│ designing a backend  │  │ keeping knowledge    │╎                          ┆
          ┆ ╎│ understanding and    │  │ understanding and    │╎                          ┆
          ┆ ╎│ instructions         │  │ instructions         │╎                          ┆
          ┆ ╎└──────────────────────┘  └──────────────────────┘╎                          ┆
          ┆ ╎ the Backend Kit                                  ╎                          ┆
          ┆ └╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌╌┘                          ┆
          └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┐                         ┆
                                                                ┆                         ┆
              ┌─────────────────────────────────────┐           ┆ ┌────────────────────┐  ┆
 Layer 4      │ each Backend Repo's work,           │           ┆ │ its own work, by   │  ┆
              │ by its Kit Copies                   │           ┆ │ its own Adapted    │  ┆
              └─────────────────────────────────────┘           ┆ │ Cases, in .claude/:│  ┆
                                                                ┆ │ understanding and  │  ┆
                                                                ┆ │ instructions       │  ┆
                                                                ┆ └────────────────────┘  ┆
                                                                └┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┄┘
```

Key: the dotted frame holds what the Maintainer Repo keeps. The dashed frame holds what the Backend Kit copies to each Backend Repo. On the right, the Maintainer Repo's own Adapted Cases sit in layer 4 with its work, in `.claude/`: they are written for this repo alone, and no Adapted Case of layer 3 holds them (§3.4). How knowledge travels between the repos is Change, in keeping knowledge's (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §2, *The arrows*).

## 3. The layers

Knowledge sits in four layers (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*). This section says where each is kept here, and what each holds so far. Layers 1 to 3 are kept in the Maintainer Repo, under `knowledge/`. Where each is kept, and how a new text is placed, is §3.5.

Each repo is a project of a Problem Domain (`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*): a Backend Repo's is CBC backend design, and the Maintainer Repo's is keeping knowledge.

The Backend Kit is layer 3's set for the Backend Repos' Problem Domain, the picture's dashed frame, and what is copied to each Backend Repo. Each of its parts is an Adapted Case: an Adapted Understanding Text with its Instruction Text (§3.3). A part with an Instruction Text and no Adapted Understanding Text, such as the Backend Kit's Defined Terms, carries its Change Record in its own footer (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.1, *Change a Kit Copy*). A part with only an Understanding Text is open (§5, question 3). So far it holds:

1. the Backend Repos' Adapted Cases for keeping knowledge, such as taking a Kit Update (§3.3.1);
2. their Adapted Cases for designing a backend: agent work, and CBC system design (§3.3.2);
3. the Defined Terms the Adapted Cases use;
4. the forms a Backend Repo's records start from. They go once, at birth, and are the Backend Repo's own after it;
5. a description of CBC system design for the Backend Repo's readers, as adapted to its kind of system. Its form is decided when the concept is split, and so is whether a Backend Repo may change it.

### 3.1 The Backbone Idea layer

Layer 1 holds Backbone Ideas (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.1, *The Backbone Idea layer*). Each row's description is a summary; the idea's home holds it.

| Backbone Idea | What it says | Home |
|---|---|---|
| The layers of knowledge | the layers knowledge sits in, and what each holds | `knowledge/backbone-ideas/layers-of-knowledge.md` |
| How an agent works | how a rule written in a repo reaches the agent, and what each channel guarantees | `knowledge/backbone-ideas/how-an-agent-works.md` |
| CBC design | how a system is designed by CBC, for no one kind of system | planned, from `concept/` (`TODO.md`, the item that splits the concept) |
| Defined Terms | what a Defined Term is, and what keeps its meaning exact | `knowledge/backbone-ideas/defined-terms.md` |
| Change | any change to knowledge, wherever it starts, and what holds for every one | `knowledge/backbone-ideas/change.md` |
| Repo hygiene | the files every repo carries from its first commit, and why | `knowledge/backbone-ideas/repo-hygiene.md` |
| Records | which records a repo keeps, what each answers, and how they feed each other | `knowledge/backbone-ideas/records.md` |
| Agent files | which files a repo keeps for the agent that works in it, and what goes in each | `knowledge/backbone-ideas/agent-files.md` |

Which other of today's project-agnostic ideas are Backbone Ideas is open (§5).

It is kept in the Maintainer Repo, and stays there. A Backend Repo receives it only adapted, in the Backend Kit.

### 3.2 The Problem Domain layer

Layer 2 holds Problem Domain Ideas (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.2, *The Problem Domain layer*), each a Backbone Idea of §3.1 adapted to one Problem Domain.

The Maintainer Repo keeps the Problem Domain Ideas of both Problem Domains so far, the picture's two boxes: its own, keeping knowledge, and the Backend Repos', CBC backend design. Keeping the Backend Repos' texts is part of its own work (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3, *How a change travels*). Each Problem Domain writes its own adaptation of a Backbone Idea, so both hold one of how an agent works.

In each table, a row's description is a summary; the idea's home holds it.

#### 3.2.1 Keeping knowledge

The Maintainer Repo's own Problem Domain. It works by its own Adapted Cases, written from these ideas (§3.4).

| Problem Domain Idea | Adapted from | What it adds | Home |
|---|---|---|---|
| The layers of knowledge, in keeping knowledge | The layers of knowledge | where each layer is kept | this document |
| Defined Terms, in keeping knowledge | Defined Terms | the mark; where each is defined; the Borrow Table; finding one | `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` |
| Change, in keeping knowledge | Change | the arrows between the Maintainer Repo and the Backend Repos; how a change travels them | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` |
| How an agent works, in keeping knowledge | How an agent works | the same channels in the repo that writes the rules; what its work and the handbook's showed of the claims | `knowledge/problem-domain-ideas/keeping-knowledge/how-an-agent-works-in-keeping-knowledge.md` |
| Repo hygiene, in keeping knowledge | Repo hygiene | no stack; the Backend Kit's files it keeps | `knowledge/problem-domain-ideas/keeping-knowledge/repo-hygiene-in-keeping-knowledge.md` |
| Records, in keeping knowledge | Records | no end; one Plan Step in the plan; no changelog; the Backend Kit's records it keeps | `knowledge/problem-domain-ideas/keeping-knowledge/records-in-keeping-knowledge.md` |

#### 3.2.2 CBC backend design

The Backend Repos' Problem Domain. The Maintainer Repo keeps its Problem Domain Ideas and writes the Backend Kit's Adapted Cases from them. The work is done in each Backend Repo, by its Kit Copies (§3.4).

| Problem Domain Idea | Adapted from | What it adds | Home |
|---|---|---|---|
| CBC design, in CBC backend design | CBC design | backends as the kind of system | planned, from `concept/` (`TODO.md`, the item that splits the concept) |
| How an agent works, in CBC backend design | How an agent works | the Backend Repo as the case nobody watches; what its work showed of the claims | `knowledge/problem-domain-ideas/cbc-backend-design/how-an-agent-works-in-cbc-backend-design.md` |
| Defined Terms, in CBC backend design | Defined Terms | the Backend Kit's Defined Terms, read in a Backend Repo without layers 1 and 2 | `knowledge/problem-domain-ideas/cbc-backend-design/defined-terms-in-cbc-backend-design.md` |
| Change, in CBC backend design | Change | how a Backend Repo changes a Kit Copy, and takes a Kit Update | `knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` |
| Repo hygiene, in CBC backend design | Repo hygiene | the files at birth; the stack's lines at their Plan Step | `knowledge/problem-domain-ideas/cbc-backend-design/repo-hygiene-in-cbc-backend-design.md` |
| Records, in CBC backend design | Records | the Record Stubs at birth; the plan from the playbook; the playbook | `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` |

### 3.3 The Adapted Case layer

Layer 3 holds Adapted Cases (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.3, *The Adapted Case layer*), each written from a Problem Domain Idea of §3.2.

Here an Adapted Case is written for one piece of agent work, such as reading a Backend Repo, working one step of its Plan Step, or writing a commit message, or for what all of the agent's work uses, such as the Defined Terms. Its Instruction Text is anything the agent acts on in that work: an Agent Skill, an Agent Rule, the Defined Terms it writes by, or a record form it fills. How many one Adapted Case holds is open (§5). Its Adapted Understanding Text says why the Instruction Text is as it is. The agent uses the Instruction Text in the work, and reads the Adapted Understanding Text only when the Instruction Text is changed. The two travel together: a Backend Repo's Kit Copy holds both.

Layer 3 holds one set for each Problem Domain. So far there is one, the Backend Kit, for the Backend Repos'. The Maintainer Repo's Problem Domain has none, so its own Adapted Cases are layer 4 (§3.4). §3.3.1 and §3.3.2 list the Backend Kit's Adapted Cases in two groups: for keeping a Backend Repo's own knowledge, and for designing its backend. An Agent Skill or Agent Rule found both in the Backend Kit and among the Maintainer Repo's own is two Adapted Cases, one in each. The two are tied only through the nearest idea above them both (`knowledge/backbone-ideas/layers-of-knowledge.md` §3.3, *The Adapted Case layer*).

Work no Adapted Case covers may write one of the repo's own, on trial: one kind of Knowledge on Trial (`knowledge/backbone-ideas/change.md` §4, *The arrows*, the arrow *fit*). It is layer 4, the repo's own (§3.4). A Backend Repo's Knowledge on Trial is kept in the Backend Repo, comes from no Kit Copy, and is handed over at its close.

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
- layer 3: `knowledge/adapted-cases/<Problem Domain>/`, one set for each Problem Domain. In it, a folder for each group, such as `keeping-knowledge/`, and in that a folder for each Adapted Case, named after it, its texts together, each named by its kind, such as `understanding.md` and `rule.md`. The Defined Terms sit in `defined-terms/`, beside the groups. Each Instruction Text is written as it loads in a Backend Repo;
- layer 4, this repo's own Adapted Cases: whole in `.claude/`. The Instruction Text sits where its kind loads, such as `.claude/rules/`. The Adapted Understanding Text sits in `.claude/understanding/`, which never loads.

A Backend Repo's layer 4 is kept in the Backend Repo.

**Rules:**

- One folder per layer, and no number in a folder's name.
- A folder is made when its first file lands.
- A file is named after its idea, and its title matches. A layer-2 title is its layer-1 title, ", in" and its Problem Domain.
- A new idea gets its row in §3.1's or §3.2's table, with its Home.

## 4. How knowledge moves

How knowledge enters the layers and moves between them is Change's (`knowledge/backbone-ideas/change.md`). How it travels between the Maintainer Repo and the Backend Repos, the picture's arrows among it, is Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md`).

## 5. Open questions

None is answered by the text above. Each is answered when work reaches it: its answer goes into the text above, and the question leaves this list.

1. **A kit for new Maintainer Repos:** should there be a kit a new Maintainer Repo is born from, as a Backend Repo is born from the Backend Kit? There is one Maintainer Repo so far. The Tiers Model has a rule for a second Maintainer Repo (`docs/models/tiers.md` §2.1, *The empty top tier*), and `cbc-concept`, once close to a second Maintainer Repo, ended as a rebuild and is kept only as a source (ADR-0082). §3.4 says what such a kit would be made from.
2. **What then points at it:** the simulation's opening and the problem file's §2.1. Then `temp/`'s old files, one by one, and how today's ways are written across the drafts.
3. **What the Backend Kit holds:** only its Problem Domain's Adapted Cases, or the Backend Repos' Problem Domain Ideas too. CBC system design adapted for backends (§3, the Backend Kit's item 2) may already be layer 2. Two cases the rule that each part is an Adapted Case (§3) does not yet cover:
   - an Understanding Text with no Instruction Text, such as the description of CBC system design for a Backend Repo's readers (§3, the Backend Kit's item 5);
   - Knowledge on Trial in the Backend Kit: today's, for ways of working, is one text of both kinds, not yet split, and today's Kit Updates carry it.
4. **Which other ideas are Backbone Ideas:** of today's project-agnostic ideas, beyond how an agent works and CBC design (§3.1).
5. **What one Adapted Case holds:** one Agent Skill or Agent Rule under its understanding text, or several. One understanding text may stand under more than one, as the facts-in-sync manual stands under two Agent Rules.
6. **An Adapted Case from two ideas:** the cbc-framing Agent Skill holds CBC design's content, written as a piece of agent work. Is it adapted from two Problem Domain Ideas, or from one, with the other giving only its form?
7. **A table of this repo's own Adapted Cases:** §3.1 and §3.2 list their layers' texts in tables, and §3.4 lists none. Should it, beside them? With one, Defined Terms, a table adds little. Its trigger: the second of this repo's own Adapted Cases.

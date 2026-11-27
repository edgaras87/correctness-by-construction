# Agent files, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/agent-files.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Cases for agent files: the Entry File, the Decisions Log's Record Stub and Claude Code's Tool Binding for the Backend Repos.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules: the agent-arrangement manual, docs/conventions/agent-arrangement/README.md: What it is for, CBC Run 3's evidence; What this is made usable as; The seats, The CBC Run's seat; §2.3 to §2.6, the Backend Repo's Entry File; §3.3, its Output Shapes; §3.4, its Decisions Log; the records' exception, docs/conventions/exchange/README.md §2.4. What a Kit Update records is Change's, in keeping knowledge, not today's exchange manual's.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is agent files in the Backend Repos' Problem Domain: what a Backend Repo is born with, where its Entry File sits and when it is read again, what its Decisions Log holds, and the one kind of agent file it adds. Which files a repo keeps for its agent, and what goes in each, are agent files' (`knowledge/backbone-ideas/agent-files.md`). The Backend Kit's Adapted Cases for agent files are written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Record | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Decisions Log | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Local Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Output Shape | `docs/conventions/shapes/` §1, *What an Output Shape is* |
| Plan Step Gate | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Record Stub | `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §1, *Its Defined Terms* |
| Records Table | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |

## 2. At birth

A Backend Repo is born with its agent files from the Backend Kit. Two kinds come as its own from birth, never as Kit Copies: the Entry File, and the Decisions Log's Record Stub. Each holds what one Backend Repo is and did, so a newer Backend Kit has nothing to say to one already filled, as with the records (`knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §2, *At birth*). Its Agent Skills, Agent Rules and ways of working not yet proven come as Kit Copies.

Every Backend Repo has been born with its agent files so far, and works by them from its first session.

**Rules:**

- A Backend Repo's first commit holds its Entry File and its Decisions Log's Record Stub, its own from then on.
- No Kit Update changes a Backend Repo's Entry File or Decisions Log after birth.
- Its Agent Skills, Agent Rules and ways of working not yet proven are Kit Copies.

## 3. The Entry File

A Backend Repo's Entry File sits in the agent's folder, with its other agent files, so every agent file sits in one place. CBC Run 3, a Backend Repo when Backend Repos were called CBC Runs, moved its Entry File there. It was a rename alone, with no line changed, and the tool read it at the new address from the next session.

It is born with what the repo is, the Records Table and one Local Rule, under *Local rules*. Its *How to work here* heading arrives with its first line. Both headings are spelled so in every Backend Repo, so that two Backend Repos read alike. The born Entry File holds the three tests in a comment (`knowledge/backbone-ideas/agent-files.md` §5, *How the Entry File is written*).

It is read again at the retrospective's close: every line passes the three tests again, or leaves. The Decisions Log's entries are read again then too.

**Rules:**

- The Entry File sits in the agent's folder.
- The two headings are *How to work here* and *Local rules*, spelled so.
- The retrospective's close reads the Entry File again, each line against the three tests, and the Decisions Log's entries again.

## 4. The Decisions Log

A Backend Repo's Decisions Log holds the changes to its agent files that the repo makes for itself, such as a Local Rule added or a setting changed. Two things a Backend Repo records about its Kit Copies sit elsewhere: the Kit Version it works from, in a file of its own, and each Change Record, in a footer of the Kit Copy it changed (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.1, *Change a Kit Copy*). So the Decisions Log holds neither.

At the retrospective, a list of the rules in force now goes on top, each with the rule it replaced, so a reader meets the current rules first. It is the one part of the Decisions Log that is not appended.

**Rules:**

- The Decisions Log holds no Kit Version and no Change Record.
- At the retrospective, the rules in force now go on top, each with what it replaced.

## 5. Output Shapes

A Backend Repo keeps one kind of agent file more:

| File | What it holds | How it reaches the agent |
|---|---|---|
| Output Shapes | each a presumed output, read at a Plan Step Gate to check what was made | nothing loads them: the Plan Step Gate sends the agent to one |

A Backend Repo with no Output Shape has none: the folder arrives with the first, from the Backend Kit or its own.

**Rules:**

- The Output Shapes sit in one folder of their own, which nothing loads.

## 6. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

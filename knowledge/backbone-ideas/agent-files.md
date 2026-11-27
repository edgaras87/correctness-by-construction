# Agent files

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7; PLAN.md, the agent-arrangement manual's Plan Step, decision A).
Its first sources, input and not rules: the agent-arrangement manual, docs/conventions/agent-arrangement/README.md: its opening; What it is for; §1 to §4; from §5, what holds for any tool: a Paths Rule's condition is a place, and a comment the tool drops costs nothing; from Why it arrives this way, the Entry File's rules in its comments.
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- It names no tool's paths: where each file sits, and how the tool loads it, are a Tool Binding's.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says which files a repo keeps for the agent that works in it, and what goes in each. It names no Problem Domain: each Problem Domain Idea adapted from it says what its own repos keep, and where.

It stands on how an agent works: that idea says how text reaches the agent; this one says which file carries it (`knowledge/backbone-ideas/how-an-agent-works.md` §7, *Choosing a channel*). It names no tool's paths. Where each file sits, and how the tool loads it, are a Tool Binding's (`knowledge/backbone-ideas/how-an-agent-works.md` §8, *The Tool Bindings*).

Its neighbours: the records the Entry File's Records Table lists are records' (`knowledge/backbone-ideas/records.md` §12, *The Records Table*); what a repo keeps out of git is repo hygiene's (`knowledge/backbone-ideas/repo-hygiene.md` §4, *What every repo keeps out*); how a commit that touches agent files is made is the commit-messages manual's (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*).

## 1. Its Defined Terms

- **Agent Rule:** a file of instructions the tool loads by itself, not by the agent's choice: in every session, or, as a Paths Rule, when the agent touches a file at a path it names.
- **Agent Skill:** a file of instructions for one kind of work, read when that work begins.
- **Decisions Log:** the record of how a repo's agent files changed: each entry dated, with what changed, why, and what was rejected.
- **Local Rule:** a rule of one repo only that has no moment, written in its Entry File.
- **Paths Rule:** an Agent Rule loaded when the agent touches a file at a path it names.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Ambient Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Enforcement Gate | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pushed Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Records Table | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Told Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Tool Binding | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |

## 2. What agent files are for

Agent files make an agent work in a repo the way the repo needs, from its first session. A repo can drop them and keep its work: a copy without them still holds the whole project.

The failure they answer is a rule restated in the Entry File "so it is always in context". Each restated rule grows the Entry File, and each copy drifts from its source while both look current. Each Problem Domain Idea gives the evidence its own work showed.

## 3. The agent files

| File | What it holds | How it reaches the agent |
|---|---|---|
| The Entry File | what every session needs (§4) | the Ambient Channel |
| Agent Skills | the instructions for one kind of work each (§7) | read when that work begins |
| Agent Rules | a rule for one part of the tree, or for every task (§7) | loaded by the tool: in every session, or when a file is touched |
| Ways of working not yet proven | one file for each kind of work no Agent Skill covers yet | nothing loads them: the agent is sent to one when such work starts |
| The Decisions Log | how the agent files changed, and why (§8) | opened when they change |
| The settings | the tool's settings: the repo's, and one machine's (§9) | the tool acts on them; none is text for the agent |
| The operator's file | one operator's settings (§10) | the Ambient Channel, in one checkout |

**Rules:**

- The list is closed. A kind of file is an agent file only by its row here, or in a Problem Domain Idea's own table for its repos. A new kind joins with its row.
- A file is an agent file when removing it breaks nothing in the project's work.
- Agent files hold no project truth: what the repo decides, plans or ships is in its records, which a copy that drops the agent files still holds. Where a project fact must sit in an agent file, such as the Records Table in the Entry File, the idea that owns the fact states it, and this one holds only the file.

## 4. The Entry File

The Entry File is the one text present before anything is looked up. It holds what every session needs: what the repo is, where its records are, and the little that must be present on every task because no moment would deliver it.

Every other file teaches its own use, at the moment it is opened: a record's form sits in its header (`knowledge/backbone-ideas/records.md` §13, *Where a record's rules sit*), an Agent Skill's steps in its body. That works only if the agent knows the files exist. The Entry File tells it, and holds nothing else.

It is not a map of the code. An overview of a repository did not help agents find the right file (Gloaguen et al., arXiv 2602.11988, 2026, measured). Nor is it the list of which ideas a repo works by: each reaches the agent through its own channel.

It is written when the repo starts. It changes when a record moves, an idea is taken up or a build command changes, and at the re-reading its size asks for (§6). Not otherwise.

**Rules:**

- The Entry File holds what every session needs, and points at the rest.
- One Entry File for each tool in use. None is kept for a tool nobody uses.

## 5. How the Entry File is written

The Entry File is paid for on every task. So what goes in is decided by a test on every line, not by a list of sections. A line stays only if it passes all three tests:

1. **True of this repo and nowhere else.** A line that would be true in another repo belongs to an idea, and lives at its home, once. The Entry File points at it, and never restates it: a summary loses parts on arrival, and then two files disagree while both look current (`knowledge/backbone-ideas/how-an-agent-works.md` §10.7, *On summaries*, claims M1 and M2).
2. **No moment.** A line about a moment goes where the moment is: a record's header, the README, an Agent Skill, or a Paths Rule for a rule true only under one folder. It is read there, when it applies, and not on every task where it does not.
3. **Nothing else would deliver it.** What stays is what no channel fires for: what the repo is, where its records are, a stance, a fact nobody would notice was missing.

What passes is, in practice, five kinds of line:

- what the repo is;
- the Records Table;
- build and test commands, where the repo has them;
- how to work here;
- Local Rules.

That is what the tests leave, not a rule of its own. A line that passes belongs under any heading, and no heading saves a line that fails.

How to work here is the stance a repo expects where it is not the obvious one, such as "decide before building". No idea can hold it, since an idea is true across repos. It is also where restating rules starts most easily, so it holds stance, never rules.

A Local Rule enters only when nothing would tell the agent that its moment has come. A test that needs a running service has a moment, and goes there. Most facts that feel local have one, so Local Rules stay few.

**Rules:**

- Each line passes the three tests, or leaves.
- The Entry File points at a rule, and never restates it "so it is always in context".
- How to work here holds stance, never rules.
- A Local Rule has no moment.
- A heading arrives with its first line. None is kept empty, waiting for content.

## 6. The Entry File's size

The Entry File travels the Ambient Channel, so it is paid on every task, those it does not concern included. Each line added lowers compliance with every other (`knowledge/backbone-ideas/how-an-agent-works.md` §10.1, *On the Ambient Channel*, claim A2, assumed). So its size is a running concern, not a one-time one.

What counts is what the tool delivers, not the file. A part the tool drops on load, such as a comment, costs nothing per task (`knowledge/backbone-ideas/how-an-agent-works.md` §8, *The Tool Bindings*). It is read when the file is opened to edit it, the moment it governs. So the rules for writing the Entry File sit in its own comments, where they are free.

What the tool delivers is kept to a screen. When it is longer, something in it belongs to an idea, a record or an Agent Skill.

Noticing growth has no moment of its own. So a repo names one, at which every line is read again against the three tests (§5). Its Problem Domain Idea says which moment.

**Rules:**

- What the tool delivers of the Entry File fits on a screen.
- Every line is read again at a moment the repo names, and passes the three tests or leaves.
- Removing a line is maintenance, not tidying: every line added dilutes every other.

## 7. Agent Skills and Agent Rules

An Agent Skill holds the instructions for one kind of work, read when that work begins. A repo adds its own for a rule of its own that has a moment, which the Entry File must not hold (§5). Work no Agent Skill covers starts from a way of working not yet proven (§3). How one becomes an Agent Skill is the idea of trying a new way of working's.

An Agent Rule is loaded by the tool, not chosen by the agent. A Paths Rule loads when a file under its paths is touched. It is the home for a rule true only in one part of the tree, which an Agent Skill would carry only if the agent noticed the moment. Its condition is a place, never an action: "when the work is under `generated/`", not "when committing". So it does not replace an Agent Skill. An Agent Skill is the agent's judgment about an action; a Paths Rule is the tool's check on a touched file.

An Agent Rule loaded in every session is the Entry File by another name, and fails its first test (§5), since it is true in any repo. It passes in one case: an idea whose moment is every task, such as every answer and every record written, which no path, Agent Skill or record header reaches at all of them. Then the Agent Rule is that idea's own channel, made from its home. It is paid in every session, like the Entry File (§6), so few ideas qualify.

**Rules:**

- A rule whose moment is an action goes in an Agent Skill. A rule bound to a place goes in a Paths Rule.
- An Agent Rule loaded in every session carries one idea whose moment is every task. Any other rule in one fails the Entry File's tests.
- Each such Agent Rule is one idea's own file, made from its home, never a restatement.

## 8. The Decisions Log

The Decisions Log records how the agent files changed. It is dated and appended to, each entry in three parts: what changed, why, and what was rejected.

A rule for an agent file sits in the file it governs, as a comment. The Decisions Log keeps its why and the options rejected. Neither repeats the other. The log's own form sits in its header (`knowledge/backbone-ideas/records.md` §13, *Where a record's rules sit*).

**Rules:**

- An entry is never edited. A changed mind is a new entry.
- A rule sits in the file it governs; its why and the options rejected sit in the Decisions Log.

## 9. The settings

A tool's settings come in two kinds.

The repo's settings are tracked. They are the one place agent files hold an Enforcement Gate as repo state, such as a permission rule that stops a command at a prompt the human answers. A repo adds them when it has a rule that must not rest on text, or a file to exclude. Where their format holds no comment, the why of each sits in the Decisions Log.

One machine's settings are never the repo's truth. The repo keeps them out of git (`knowledge/backbone-ideas/repo-hygiene.md` §4, *What every repo keeps out*).

**Rules:**

- The repo's settings hold a rule that must not rest on text, or an exclude, and nothing else.
- Their why sits in the Decisions Log, never in the settings.
- One machine's settings stay out of the repo.

## 10. The operator's file

An operator's own file loads beside the Entry File, in one checkout only, and fires and costs like it (`knowledge/backbone-ideas/how-an-agent-works.md` §3.1, *The Ambient Channel*). It stays out of the repo's history there. A Problem Domain Idea that keeps it in says why.

It holds the operator's settings, never rules. A setting is a choice one operator makes where the repo leaves it open: how often the agent stops for review, how far it decides alone, how a session starts. One test sorts a line:

- another operator of the same repo would write it differently: it is a setting, and stays;
- every operator would want it: it is a rule, and goes where the repo keeps its rules; the operator's file only uses it.

"Small commits only where the reviewer grants them" is a rule. "On this branch, commit freely" is a setting.

Its words never enter a record: a record that quotes it lets one operator's preference into the repo's truth. The operator writes it for each repo, and carries it there by hand.

**Rules:**

- The operator's file holds settings, never rules.
- A rule the operator keeps saying is not kept here. Saying it again and again is the Told Channel's diagnostic: an idea is missing, or its channel is not firing (`knowledge/backbone-ideas/how-an-agent-works.md` §7, *Choosing a channel*). Writing the rule here would make the saying permanent and the diagnosis invisible.
- Its words never enter a record.

## 11. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

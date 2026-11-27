# One home, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for one home, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is, where only this repo relies on the reason.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: its Instruction Text, the one-home Agent Rule, .claude/rules/one-home.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: the facts-in-sync manual, docs/conventions/facts-in-sync/README.md: The Concept Deliverer's seat; Why it arrives this way, its half for the one-home Agent Rule; and the one-home Agent Rule's header comment, at 643c2bd6.
-->

This text says why this repo's one-home Agent Rule loads in every session, and why it holds more than the Backend Kit's. Why one home is needed at all is one home's (`knowledge/backbone-ideas/one-home.md` §2, *Why one home*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Agent Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Ambient Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Change Walk | `knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Conversation Memory | `.claude/understanding/conversation-memory.md` §1, *Its Defined Terms* |
| Fact Reference | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Paths Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |

## 2. Why every session

A fact is retold in whatever text is being written. So the rule binds whenever any text is written, which is every task. The form of the record being written says nothing of the record the fact was taken from, so no form that holds the rule is open at that moment. A rule needed at every task reaches the agent through the Ambient Channel (`knowledge/backbone-ideas/how-an-agent-works.md` §7, *Choosing a channel*).

The rule carries no `paths:` list. A Paths Rule loads only when a file under its paths is touched with the agent's tools, and an edit made by script loads nothing (`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md` §6, *Paths Rules*). A fact can be retold in any file, so no list of paths covers the moment.

## 3. Why it holds more than the Backend Kit's

The Backend Kit's rule says one home in a Backend Repo's words: a fact's id, or its path, re-read when the fact changes. This repo writes every Fact Reference by path, section and title, and its Change Walk re-reads each line that carries one (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §2, *Writing a Fact Reference*). So three things in it are its own:

- **Rule 6, each new line asked at the commit.** The Change Walk finds only lines that carry a Fact Reference. A line that should carry one and does not is found by nothing else (ADR-0070).
- **Rule 7's last clause, the footer stripped from every copy delivered.** Only this repo delivers Instruction Texts, and a Backend Repo cannot open the decisions a footer cites (ADR-0078).
- **The history it lists.** Beside the history a Backend Repo keeps, this repo keeps the parts of its Conversation Memory, which no Backend Repo holds.

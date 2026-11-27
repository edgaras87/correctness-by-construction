# Commit messages, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for commit messages, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is, where only this repo relies on the reason.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/commit-messages-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: its Instruction Text, the commit-messages Agent Skill, .claude/skills/commit-messages/SKILL.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: the commit-messages manual, docs/conventions/commit-messages/README.md, deleted on 2026-11-27, its last state in git at 47007e1b: §3, The Concept Deliverer's habit, its list of scopes; Why it arrives this way; this repo's log, by script on 2026-11-27 (PLAN.md, the commit-messages manual's Plan Step, decisions B and E).
-->

This text says why this repo's commit-messages Agent Skill lists its scopes, why the agent's own files take `docs(agent)`, and why it is an Agent Skill. Why the scope carries the signal here at all is commit messages, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/commit-messages-in-keeping-knowledge.md` §2, *The scope carries the signal*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pulled Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |

## 2. Why the list is here

The scopes are used at the commit, and the Agent Skill is opened there. Until 2026-11-27 the list sat only in the commit-messages manual, which no commit opens, and the agent took the scopes from the log. So it drifted: from 2026-11-26, 12 commits of the agent's files beyond a commit plan took `docs(agent)`, and none took the `chore(agent)` the Agent Skill named.

**Rules:**

- The Agent Skill lists this repo's scopes.

## 3. Why the agent's files are `docs(agent)`

In a repo of text, a change to text is `docs`, and the scope carries the signal. The agent's files are text too. So the type stays `docs`, and `agent` says whose files they are. The Backend Kit's Agent Skill keeps `chore(agent)`: a Backend Repo builds software, and there the agent's files are not the work.

**Rules:**

- Every commit of the agent's own files is `docs(agent)`.
- The `chore(agent)` commits before 2026-11-26 stay as they are: history is not rewritten.

## 4. Why an Agent Skill

A rule for writing a commit message binds at one moment: the commit. The Agent Skill is opened there, through the Pulled Channel (`knowledge/backbone-ideas/how-an-agent-works.md` §3.2, *The Pulled Channel*). Opened at every commit here, it still did not keep each subject to its aim: 125 of 233 commits ran over 50 (`knowledge/problem-domain-ideas/keeping-knowledge/how-an-agent-works-in-keeping-knowledge.md` §3, *What the work showed*, A1). So a check counts the subjects too, at each Plan Step's close (`knowledge/problem-domain-ideas/keeping-knowledge/commit-messages-in-keeping-knowledge.md` §3, *When subjects are counted*).

**Rules:**

- The commit-messages Agent Skill is opened before every commit message is written.

## 5. Open

None is open now.

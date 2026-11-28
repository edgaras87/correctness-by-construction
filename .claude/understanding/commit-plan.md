# Commit sets, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for commit sets, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is, where only this repo relies on the reason.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/commit-sets-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: its Instruction Text, the commit-plan Agent Skill, .claude/skills/commit-plan/SKILL.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first source, input and not rules: the commit-plan manual, docs/conventions/commit-plan/README.md: Why it arrives this way.
-->

This text says why this repo's commit-plan Agent Skill reaches the agent as an Agent Skill, and why the stop at each commit is not in it. What a repo of texts meets in its Commit Sets is commit sets, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/commit-sets-in-keeping-knowledge.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Commit Plan | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Commit Set | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pulled Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |

## 2. Why an Agent Skill

A Commit Plan is needed at one moment: work turns out to need more than one commit. The agent knows the moment by the work in front of it. The Agent Skill is read then, whole, through the Pulled Channel (`knowledge/backbone-ideas/how-an-agent-works.md` §3.2, *The Pulled Channel*). Nothing in a record puts the Commit Plan in front of the agent when the work turns out larger.

**Rules:**

- The commit-plan Agent Skill is opened when work turns out to need more than one commit.

## 3. Why the stop is not here

The stop at each commit must hold at every commit. An Agent Skill read only for work of more than one commit cannot carry it. So the stop is the commit-messages Agent Skill's, opened at every commit (`knowledge/backbone-ideas/commit-messages.md` §5, *Commit on the word*).

## 4. Open

None is open now.

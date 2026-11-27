# Visual comparison, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for visual comparison, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is, where only this repo relies on the reason.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/visual-comparison-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: its Instruction Text, the visual-comparison Agent Skill, .claude/skills/visual-comparison/SKILL.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: the visual-comparison manual, docs/conventions/visual-comparison/README.md: Why it arrives this way; .claude/decisions.md, its entry of 2026-11-19 on the visual-comparison Agent Skill.
-->

This text says why this repo's visual-comparison Agent Skill has the reviewer render, why a small outcome is recorded in a commit body, and why it is an Agent Skill. Which notations this repo uses is visual comparison, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/visual-comparison-in-keeping-knowledge.md` §2, *Plain text, no build step*).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Paths Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pulled Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |

## 2. Why the reviewer renders

The reviewer always looks at the render, and suggests changes. The Mermaid renderer was refused here: it runs Chrome with its sandbox off. So the agent checks each candidate's syntax, and the reviewer renders and judges the look.

**Rules:**

- The reviewer renders the candidates and judges how they look.
- The agent marks its own verdicts on the look as predictions until the reviewer has seen them.

## 3. Where a small outcome goes

An outcome too small for an ADR is recorded in the body of the commit that places the winner. That body is already its record, as the commit-messages Agent Skill has it. A devlog line would say it a second time.

**Rules:**

- The draft goes in the commit that places the winner, and its body names the commit that holds the draft.

## 4. Why an Agent Skill

A comparison is needed at one moment: a structure is hard to see, and more than one way of showing it could work. The agent knows the moment by the question it faces. The Agent Skill is read then, through the Pulled Channel (`knowledge/backbone-ideas/how-an-agent-works.md` §3.2, *The Pulled Channel*). No file is touched that a Paths Rule could load on, and nothing in a record names the moment.

**Rules:**

- The visual-comparison Agent Skill is opened when a structure is hard to see and more than one way of showing it could work.

## 5. Open

None is open now.

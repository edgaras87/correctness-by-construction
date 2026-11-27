# The Entry File, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for its Entry File, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is, where only this repo relies on the reason.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/agent-files-in-keeping-knowledge.md, the Problem Domain Idea nearest it. How the Entry File is written, and why, are agent files' (knowledge/backbone-ideas/agent-files.md §5, How the Entry File is written); this text never retells it.
What stands on it: its Instruction Text, CLAUDE.md at the root.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first source, input and not rules: the Local Rule's own line in CLAUDE.md, and the agent-arrangement manual, docs/conventions/agent-arrangement/README.md, deleted on 2026-11-27, its last state in git at bd6941d6: §2.4, Local rules; §5.6, the first limit of a rules file.
-->

This text says why the Entry File's one Local Rule is a Local Rule. Its other lines need no reason of their own: what the repo is, and the Records Table, whose rows are records'.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Local Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Paths Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Records Table | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |

## 2. Why the layers' rule is a Local Rule

The Local Rule says: before writing a new text for the layers of knowledge, read where it goes, in the layers document's §3.5. A text placed in the wrong folder is a text at the wrong layer, since a text's path says its layer.

The rule has a moment: the choice of where a new text goes. But nothing delivers it then. A Paths Rule on the layers' folders loads only when a file there is touched, and a new file is touched first in the call that writes it, after its folder was chosen (`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md` §6, *Paths Rules*, the first limit). No Agent Skill is invoked for writing a text, and noticing the moment is the failure.

So it is a rule that no moment would deliver, and it passes the Entry File's third test (`knowledge/backbone-ideas/agent-files.md` §5, *How the Entry File is written*).

**Rules:**

- The Local Rule stays while nothing else can put it in front of the agent before a new text's folder is chosen.

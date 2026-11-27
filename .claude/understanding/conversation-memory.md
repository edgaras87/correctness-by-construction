# Conversation Memory, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for Conversation Memory, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work), and Knowledge on Trial (§3.3 there). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/records-in-keeping-knowledge.md, the Problem Domain Idea nearest it. It adds a record that text does not hold, and never retells it.
What stands on it: its Instruction Text, the header comment of TODO-CONVERSATION-MEMORY.md.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: the project-recording manual, docs/conventions/project-recording/README.md, deleted on 2026-11-27, its last state in git at 3bb95746: §14 and The seats, its item 7; ADR-0060.
-->

This text says what Conversation Memory is, why it is kept beside the backlog, and how its trial ends. Only this repo keeps one.

## 1. Its Defined Terms

- **Conversation Memory:** the talk that shaped an item of the backlog: what was asked, the options weighed, what was said for and against, and the reviewer's own words.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Knowledge on Trial | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Why a record of its own

An item of the backlog keeps what sorting it needs, and its story is the devlog's (`knowledge/backbone-ideas/records.md` §7, *The backlog*). The talk that shaped it is neither. Left in the chat, it is lost when the session ends. So it is kept beside the backlog, in `TODO-CONVERSATION-MEMORY.md` at the root, next to `TODO.md`.

**Rules:**

- One file, a section for each item: an item of the backlog, or an open question another record holds. How a section and its parts are kept, when one is read and when it goes, is the file's header.
- It decides nothing and tells no story: the item's ADR decides, and the devlog tells.
- The item stands alone. Its context is enough to sort it, and it names its section. A lost section breaks no record.
- The reviewer decides what is kept, each time a talk raises or shapes an item, on the agent's recommendation: the talk is the reviewer's.
- A section is read before the item's ideas are weighed, so the talk shapes the weighing.
- A section goes with its item, so nothing outlives what it was about.

## 3. The trial

Conversation Memory is on trial since 2026-10-21. The evidence is in the devlog: each item worked with its section in hand, and whether the section changed the work. The trial is judged at the moment named by TODO's item "Judge the Conversation Memory trial".

**Rules:**

- If the trial holds, Conversation Memory reaches the Backend Repos as any lesson does (`knowledge/backbone-ideas/change.md` §4, *The arrows*, the arrow *lesson*). If not, it goes.

## 4. Open

None now. A point joins this list when work meets one.

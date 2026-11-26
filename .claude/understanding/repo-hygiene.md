# Repo hygiene, in this repo

<!--
What it is: the Adapted Understanding Text of this repo's own Adapted Case for repo hygiene, at layer 4 (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work). It says why its Instruction Text is as it is.
What it stands on: knowledge/problem-domain-ideas/keeping-knowledge/repo-hygiene-in-keeping-knowledge.md, the Problem Domain Idea it is written from. It adapts that text, and never retells it.
What stands on it: its Instruction Text, this repo's three files at its root: .gitignore, .gitattributes and .editorconfig.
Its place in the repo: .claude/understanding/ (ADR-0084). It never loads; it is read when its Instruction Text changes.
Its first sources, input and not rules: ADR-0062; temp/README.md.
-->

This text says why this repo's three files differ from the Hygiene Base they start from. Each line of its own sits in the "this repo" section of `.gitignore`.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Hygiene Base | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Stack Overlay | `knowledge/backbone-ideas/repo-hygiene.md` §1, *Its Defined Terms* |

## 2. Why the reviewer's file is tracked

The Hygiene Base ignores the file of one person's own instructions to the agent, `CLAUDE.local.md`. This repo has one reviewer, and that file holds the settings that shape how the agent works here. Ignored, no reader of the repo would see them, and they would have no history. So this repo tracks it (ADR-0062).

**Rules:**

- `.gitignore` un-ignores `CLAUDE.local.md` in its own section, and leaves the Hygiene Base's line as it is.

## 3. Why `temp/` is tracked

`temp/` holds drafts and kept files. They are tracked so the shaping of a draft shows as diffs, and git keeps every version once one is deleted (`temp/README.md`).

## 4. No Stack Overlay

This repo has no stack, so its files hold no Stack Overlay (`knowledge/problem-domain-ideas/keeping-knowledge/repo-hygiene-in-keeping-knowledge.md` §2, *No stack*).

## 5. Open

- **A second reviewer:** the reviewer's file would be one person's again, and §2's reason would no longer hold. Its trigger: a second reviewer of this repo.

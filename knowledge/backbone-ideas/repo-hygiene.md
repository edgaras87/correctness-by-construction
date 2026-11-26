# Repo hygiene

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules:
- the repo-hygiene manual, docs/conventions/repo-hygiene/README.md, its What it is for and §1 to §3;
- the Hygiene Base's three files, delivery/container/.gitignore, .gitattributes and .editorconfig.
What stands on it: knowledge/problem-domain-ideas/keeping-knowledge/repo-hygiene-in-keeping-knowledge.md, its Problem Domain Idea of keeping knowledge, and knowledge/problem-domain-ideas/cbc-backend-design/repo-hygiene-in-cbc-backend-design.md, its Problem Domain Idea of CBC backend design. Each Problem Domain Idea points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says which files every repo carries from its first commit, and why. It names no Problem Domain: each Problem Domain Idea adapted from it says what its own repos add.

## 1. Its Defined Terms

- **Hygiene Base:** the three files of §2 as every repo starts with them, true for any repo, one that holds only text included. Each ends at a marked line, for its Stack Overlay.
- **Stack Overlay:** the lines a repo's stack adds to each file of the Hygiene Base, appended below its marked line.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The three files

A file committed by mistake stays in history, even after an ignore line is added. Line endings normalized after the first clone on another platform leave noise in history. So the files that prevent both come first.

| File | What it governs |
|---|---|
| `.gitignore` | what never enters history: built output, machine-local editor state, the operating system's scratch files, secrets |
| `.gitattributes` | the line-ending rule, `* text=auto eol=lf`, and each file kind's exception |
| `.editorconfig` | what the editor does to a file: its charset, line ending, final newline, trailing spaces and indent |

`.editorconfig` and `.gitattributes` are a pair: the editor writes LF, and git guarantees it. Neither alone is enough. An `.editorconfig` rule acts only when a file is created, typed in, saved or formatted. A file nobody touches keeps its bytes.

**Rules:**

- The three files are in a repo's first commit.
- `.editorconfig` and `.gitattributes` state the same line ending.

## 3. The base and the overlay

A repo exists before it builds anything, so its files cannot wait for its stack. The Hygiene Base comes with the first commit. The Stack Overlay comes when the stack does.

**Rules:**

- The Hygiene Base names no stack.
- A Stack Overlay is appended as it is, below each file's marked line, when the repo first builds on its stack, never before.
- Each stack has its own Stack Overlay, one part for each of the three files.

## 4. What every repo keeps out

**Rules:**

- Machine-local state of the editor and other tools, such as `.idea/` or an agent's local settings, is ignored whole. Sharing a part of it, such as run configurations, is a decision, recorded where the repo records its decisions, never a silent edit.
- Secrets are ignored. What is committed is an example file with no real values, such as `.env.example` beside `.env`.

## 5. Whose files they are

A repo's three files are its own from its first commit. It changes them when its work needs to. A fix found in one repo that is true of any repo travels as every change does (`knowledge/backbone-ideas/change.md` §4, *The arrows*, the arrow *lesson*), so the next repo starts corrected.

## 6. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

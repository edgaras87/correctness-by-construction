# Defined Terms, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer).
What it stands on: knowledge/backbone-ideas/defined-terms.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Why it is an idea of its own: ADR-0085.
What stands on it: .claude/understanding/defined-terms.md, this repo's own Adapted Case for Defined Terms, its Adapted Understanding Text.
Its first sources, input and not rules:
- temp/common-ground/common-ground-problem.md, Defined Terms, the rules its own Defined Terms follow;
- writing rule 9 (docs/conventions/writing/ §2, Why each rule, rule 9);
- the TODO item "Decide which names go in the glossary", closed on 2026-11-23 by the Defined Terms texts, its last state in git.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says how the texts of keeping knowledge mark, define, share and find their Defined Terms. It is the Backbone Idea of Defined Terms adapted to keeping knowledge, the Maintainer Repo's Problem Domain (`knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §3, *The layers*), from `knowledge/backbone-ideas/defined-terms.md`. Another Problem Domain writes its own adaptation.

## 1. Its Defined Terms

- **Borrow Table:** the table in a text's definitions section that lists each Defined Term the text uses but does not define: the Defined Term, and a Fact Reference to its definition. Nothing of the definition is retold.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Adapted Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Fact Reference | `docs/conventions/facts-in-sync/` §3.1, *What a Fact Reference is* |
| Glossary Name | `docs/conventions/writing/` §2, *Why each rule*, rule 9 |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. The mark

A Defined Term is read by people and by an agent, in Markdown. Each Markdown mark already has a job, so the capitals mark a Defined Term at every use, and the bold marks the one place it is defined.

**Rules:**

- A Defined Term is two or more words, its owner or kind first, each word capitalized: Problem Domain Idea, never Idea. A lowercase word is English.
- A Defined Term built on another carries it whole: Adapted Understanding Text, never Understanding. A short form is the one exception, defined as one (§3).
- A Defined Term of more than 4 words is a trigger to look for a shorter true one. When none is found, the long one stands.
- It is bold on its own once, where it is defined, and nowhere else.
- A bold lead, of a list item or a paragraph, may hold a Defined Term. It is never a Defined Term or a short form alone, so a search for a definition never finds it.
- An *italic* word is a label inside the Defined Term it belongs to, and is defined there.

## 3. Where it is defined

A Defined Term is defined in the text whose idea it belongs to. A text sits at one layer, so a Defined Term true for a whole Backbone Idea is defined there, not in each Problem Domain Idea under it.

**Rules:**

- A Defined Term is defined at the highest layer it holds, as a lesson goes as high as it is true (`knowledge/backbone-ideas/layers-of-knowledge.md` §4.1, *How the layers fill*).
- A text keeps its definitions together in one section, its first, titled *Its Defined Terms*, in alphabetical order, its Borrow Table after them. The plain words it keeps in a narrow sense are written there too. A text that defines and borrows nothing has no such section.
- Each definition is a list item: the Defined Term in bold, a colon, then its definition.
- The Borrow Table follows under the line "Borrowed:", in two columns, *Defined Term* and *Defined in*.
- A short form is written at the end of its full term's definition, as "Short form: **<short form>**.": in bold, with no colon.

## 4. Borrowing a Defined Term

A text often uses Defined Terms another text defines. Its Borrow Table points at each, so its reader knows where to look, and so a change to a definition finds every text that relies on it.

**Rules:**

- Every Defined Term a text uses is defined in it, or listed in its Borrow Table. A name defined in a text not yet brought into the layers of knowledge, such as a Glossary Name, is borrowed the same way.
- A short form is borrowed as any Defined Term is, by its own row. A text never defines a short form another text defines.
- A Borrow Table names the section where each Defined Term is defined, by its number and title, never by its line.
- When a definition changes, the Borrow Tables that list its Defined Term name every text to read again.

## 5. Finding a definition

An agent reads whatever it opens, and opens a file whole unless told otherwise. A text may run to hundreds of lines, and a definition is one of them. The bold mark appears once for each Defined Term, so a search for it finds the definition without reading the text whole. The definitions sit together, so the Defined Terms a definition builds on are usually beside it.

**Rules:**

- A definition is found by a search for its bold mark, and a short form by a search for `**<short form>**`, which finds its full term's definition. Its section is read only when the definition alone is not enough.
- Before a new Defined Term or short form is written, both searches are run across every text it may be read with. A hit is a collision, and one of the two changes.

## 6. Open questions

A question joins this list when work meets one, and leaves it once its answer is in the text above.

1. **A hyphenated word:** does it count as one word, toward a Defined Term's two words and its 4? Writing rule 9 says so outside `knowledge/` (`docs/conventions/writing/` §2, *Why each rule*, rule 9). Answered when the first hyphenated Defined Term is defined.

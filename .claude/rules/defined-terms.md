---
paths:
  - "knowledge/**"
  - ".claude/understanding/**"
---

<!-- This repo's own Adapted Case for Defined Terms: its Instruction
     Text. Why it is as it is: .claude/understanding/defined-terms.md.
     It carries no Foundation Line (docs/conventions/conventions/ §1.3,
     The Foundation Line). -->

# Defined Terms

**Governs:** the Defined Terms of a text under `knowledge/` or `.claude/understanding/`, or of an Agent Skill or Agent Rule built on one there: how each is found, defined and borrowed. Not the Backend Kit's files under `knowledge/adapted-cases/`: they find each Defined Term in the Backend Kit's Defined Terms (`knowledge/problem-domain-ideas/cbc-backend-design/defined-terms-in-cbc-backend-design.md` §2, *Where a Backend Repo finds one*). How a text reads is the writing rule's.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Agent Rule | `docs/conventions/agent-arrangement/` §3.2, *`.claude/rules/`* |
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Borrow Table | `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Defined Term | `knowledge/backbone-ideas/defined-terms.md` §1, *Its Defined Terms* |
| Glossary Name | `docs/conventions/writing/` §2, *Why each rule*, rule 9 |

## The rules

Each rule's source is `knowledge/problem-domain-ideas/keeping-knowledge/defined-terms-in-keeping-knowledge.md`, by section.

1. **Find a definition by its bold mark.** Search for `**<Defined Term>:**`, or `**<short form>**` for a short form, under `knowledge/` and `.claude/understanding/`, or follow the text's Borrow Table. Read the section only when the definition alone is not enough (§5, *Finding a definition*).
2. **Never write a twin.** A Glossary Name that names the same thing is its twin (`temp/common-ground/common-ground-problem.md` §2.2, *Today and what to check*, its table). A Glossary Name with no twin is borrowed like a Defined Term.
3. **Define or borrow every term you use.** Each Defined Term or short form a text uses is defined in it, or listed in its Borrow Table, by the name used. Never define a short form another text defines (§4, *Borrowing a Defined Term*).
4. **Search for a collision before you define one,** a short form too: its bold mark, with and without the colon, under `knowledge/` and `.claude/understanding/`, its words in `docs/glossary.md` and `delivery/*/docs/glossary/`. A hit that is not a listed twin is a collision: one of the two names changes (§5).
5. **Define it at the highest layer it holds,** in the text's first section, *Its Defined Terms*: alphabetical, each a list item, the Defined Term in bold, a colon, its definition, a short form at its end as "Short form: **<short form>**.". The Borrow Table follows, under "Borrowed:" (§3, *Where it is defined*).
6. **Write it by the mark:** two or more words, owner or kind first, each capitalized; a Defined Term it is built on carried whole; bold on its own only where it is defined; a bold lead may hold it, but is never a Defined Term or a short form alone; a short form defined as one (§2, *The mark*).

---

## Decisions

- ADR-0085 — Defined Terms at their homes; this Paths Rule is this repo's Instruction Text for them
- ADR-0084 — this repo's own Adapted Cases kept whole in `.claude/`
- ADR-0088 — the Backend Kit's files find their Defined Terms in its own terms text, so this Paths Rule leaves them out

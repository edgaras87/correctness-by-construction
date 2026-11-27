# One home, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/one-home.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Cases for one home and for the check at the commit.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first source, input and not rules: the facts-in-sync manual, docs/conventions/facts-in-sync/README.md: from What it is for, the handbook's evidence; §3.1, how a Fact Reference is written; §3.2 (PLAN.md, the facts-in-sync manual's Plan Step, decision D); from §3.3, the move of a trial's text and the commit plan's sweep; from §4, its greps; from §5, where a disagreement is raised; The Concept Deliverer's seat, each new line asked at the commit. A finding declined only for not being general is held already, by Change, in keeping knowledge §3.3, and one home §8 (decision F). A Backend Kit file's pointer at a Maintainer Repo text takes the form its rewritten files use (decision G). The decisions behind them: ADR-0059; ADR-0070; ADR-0072.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is one home in the Maintainer Repo's Problem Domain, keeping knowledge: how a Fact Reference is written here, how a part is numbered so a reference lands on it, how a change finds what relies on it, and where a disagreement is raised. Where a fact is written, and why, is one home's (`knowledge/backbone-ideas/one-home.md`).

## 1. Its Defined Terms

- **Change Walk:** what a change to a text others stand on sets off here: the searches for what points at it and what stands on it, and the re-read of each line they find.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Fact Reference | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Foundation Line | `docs/conventions/conventions/` §1.3, *The Foundation Line* |
| Instruction Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Knowledge on Trial | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Repo Reading | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Repo Tag | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Understanding Text | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. What the work showed

The handbook, the repo before this one, kept three copies of one rule in its Entry File, and they disagreed (`knowledge/problem-domain-ideas/keeping-knowledge/agent-files-in-keeping-knowledge.md` §2, *What the work showed*).

## 3. Writing a Fact Reference

A Fact Reference here is written in one form, always in parentheses:

- **in the same repo:** (`<path>` §<number>, *<title>*), such as (`knowledge/backbone-ideas/one-home.md` §3, *A fact and its home*);
- **in the same document:** (§<number>, *<title>*);
- **to another repo:** that repo's Repo Tag first;
- **a section with no number:** its title alone;
- **a whole document:** its path alone;
- **a numbered step inside a section:** the step after the title, such as "step 3";
- **a numbered rule in a file of rules:** the rule's number, then its bold lead as the title;
- **from a Backend Kit file to a Maintainer Repo text:** the text's name, "kept in the Maintainer Repo", then its section, such as (commit messages, kept in the Maintainer Repo, §3, *The subject*).

The path runs from the repo root, so one search finds everything that points at a document. A text names the files beside it the same way: two folders may hold a file of the same name. The number lands the reader on a paragraph, not on the whole document. The title says what is there without opening it, and a number and title that no longer match show a stale reference. The parentheses give the Change Walk and the reader one pattern to find. The sentence says its point in words, and the reference gives only the address.

A Backend Repo cannot open a Maintainer Repo text. So a Backend Kit file's line that points at one says what the Backend Repo needs without it, and the reference serves the Maintainer Repo's Change Walk alone.

**Rules:**

- A Fact Reference is written in the form above, in parentheses.
- In a comment, an HTML one or a line of YAML or SQL, the title takes no asterisks: there they show as written.
- In a list whose items are only addresses, the address stands without parentheses. A section in it still carries its title.
- A section's title is carried whole. Titles are 30 characters or fewer (`docs/conventions/writing/` §2, *Why each rule*, rule 10). A numbered rule's bold lead over 30 characters is cut at a word boundary, to 30 or fewer, ending in "…".

## 4. Numbering a section's parts

A Fact Reference names a section's number. So a section divided into labelled parts numbers them, `### N.M`, and so does every section of the same form in the text, whether anything points there yet or not. A reader then meets one structure throughout.

This reaches the texts whose parts are pointed at: the Understanding Texts. In an Instruction Text a rule stays a bullet, however long.

**Rules:**

- A section divided into labelled parts numbers them, and so does every section of the same form in the text.
- Bold emphasis inside running prose is not a part. A bold-led bullet is a part when it holds a paragraph of its own, with its own reason or story. A short list item, a phrase and a line, is not.
- A label repeated in every section of one form is that form's fixed label, not a part.
- In any text, a part that a Fact Reference points at is numbered.

## 5. The Change Walk

A text others stand on changes. The Change Walk finds what relies on it, in the same commit, or in the next when one side is an agent file and the other is not (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*).

It finds only lines that carry a Fact Reference. A line that relies on a fact written elsewhere and carries none is found by nothing. So each new or changed line is asked, at the commit, whether it relies on a fact written elsewhere, and whether it says where.

A home that moves is searched for by each old path, number and title (`knowledge/backbone-ideas/one-home.md` §5, *When a home moves*). Here, Knowledge on Trial placed into a lasting text is such a move. A commit plan's sweep looks again before its close (`docs/conventions/commit-plan/` §2.10, *The sweep*).

**Rules:**

- The Change Walk searches for the text's path, to find what points at it.
- It searches for the text's name in Foundation Lines, to find what stands on it: `the <name> convention`, `the <name> model`, or `concept v1`. A text of the layers lists what stands on it in its header, and the walk reads that list.
- Each retelling whose Fact Reference names a changed section is re-read, with the paragraph around it. Each text that stands on the changed one is re-read whole.
- A text that changes for it has its own Change Walk.
- At each commit, each new or changed line is asked whether it relies on a fact written elsewhere, and whether it says where.

## 6. Where a disagreement is raised

**Rules:**

- A disagreement is raised where it is found, in one of three places: a Copy Change, read back in a Repo Reading; a question at a Plan Step's or a commit plan's boundary; or this repo's own check at the commit.
- It is recorded in the commit body that settles it, or in an ADR when options were weighed.

## 7. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

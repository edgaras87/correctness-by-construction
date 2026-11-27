# One home, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/one-home.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Case for one home.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules:
- the facts-in-sync manual, docs/conventions/facts-in-sync/README.md: from What it is for, CBC Run 3's four records; The CBC Run's seat; from §3.4, the copy delivered without its footer, and the Record Stub that cites nothing;
- the Backend Kit's one-home Agent Rule, delivery/container/.claude/rules/one-home.md: its rule 2, the id and its first example.
The decisions behind them: ADR-0070; ADR-0078.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is one home in the Backend Repos' Problem Domain, CBC backend design: what the work showed, how a Fact Reference is written in a Backend Repo, and what a Backend Repo's texts may cite. Where a fact is written, and why, is one home's (`knowledge/backbone-ideas/one-home.md`). The Backend Kit's Adapted Case for one home is written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Copy Change | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Fact Reference | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Record Stub | `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §1, *Its Defined Terms* |

## 2. What the work showed

CBC Run 3, a Backend Repo when Backend Repos were called CBC Runs, told one Plan Step's story in four records: its plan, its devlog, its record of the slice, and its commits (CBC Run 3's RETRO D1).

## 3. A Fact Reference here

A Backend Repo names its pieces of work by ids, such as SLICE-4 or KILL-12. An id is a Backend Repo's Fact Reference, written bare. A retelling beside its id saves a lookup where the reader needs it: "SLICE-4, a retried order makes one order." Elsewhere, a line points, and does not retell.

**Rules:**

- A Fact Reference is the fact's id, written bare, or else its path, section and title, in parentheses.
- When a fact changes at its home, the Backend Repo searches for its id or path, and re-reads each line that carries it, with its paragraph, in the same commit.

## 4. What a Backend Repo may cite

A Backend Repo holds its Kit Copies, and none of the Maintainer Repo's texts. What one home says of a text sent to a repo that cannot open its decisions holds here (`knowledge/backbone-ideas/one-home.md` §6, *Where a decision is cited*).

**Rules:**

- A Kit Copy's line that relies on a Maintainer Repo text stands alone: it says what the Backend Repo needs. Its pointer there serves only the Maintainer Repo.
- A Kit Copy carries no footer of decisions: its decisions are the Maintainer Repo's.
- A Record Stub cites nothing.

## 5. A disagreement

A Backend Repo finds a disagreement when its Kit Copy says other than its work needs. It settles it in its own repo, by a Copy Change (`knowledge/problem-domain-ideas/cbc-backend-design/change-in-cbc-backend-design.md` §2, *Changing a Kit Copy*). The Maintainer Repo meets that disagreement when it reads the Copy Change back.

## 6. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

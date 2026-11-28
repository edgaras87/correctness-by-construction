# Commit sets, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/commit-sets.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Case for commit sets.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules (PLAN.md, the commit-plan manual's Plan Step, decision C):
- the Pure Seed, delivery/installs/pure-seed.md: the Commit Plan of a Backend Repo's birth;
- the Backend Kit's apply-retrospective Agent Skill, delivery/container/.claude/skills/apply-retrospective/SKILL.md: its Stage 2, and its close's item 3;
- the Backend Kit's commit-plan Agent Skill, delivery/container/.claude/skills/commit-plan/SKILL.md: its §3, a module and its architecture paragraph;
- devlog 2026-11-01, the last read's work, pass 1 and most of pass 2: CBC Run 3's SL-3 plan;
- TODO-CONVERSATION-MEMORY.md §9, A commit plan's look-back at the way: CBC Run 4's tries;
- TODO.md at a93f7311, the item "Decide whether a commit plan's look-back also asks if the work could have been done better": CBC Runs 5 and 6.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is commit sets in the Backend Repos' Problem Domain, CBC backend design: when a Backend Repo plans a Commit Set, and what a repo that builds software meets in one. How work larger than one commit is planned is commit sets' (`knowledge/backbone-ideas/commit-sets.md`). The Backend Kit's Adapted Case for commit sets is written from this document.

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Commit Plan | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Commit Set | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Decisions Log | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Two moments open one

A Backend Repo opens a Commit Set at two moments the Backend Kit names:

- **At its birth.** Its first work is a Commit Plan whose order of commits is chosen and justified: where the Entry File lands, when the records enter history, whether the Agent Skills land whole or split. The human approves the Commit Plan before it is committed, then each commit.
- **When it applies a retrospective.** The rows applied, and their sizes, are its commits, ordered by influence: repeats removed before anything is rewritten, and regrouping before rewriting. The human approves the Commit Plan before any change.

CBC Run 4 opened a Commit Set only for its retrospective, twice.

## 3. Coherent as software

A Backend Repo builds software. So a commit reverted alone leaves the software coherent, and the text that describes it (`knowledge/backbone-ideas/commit-sets.md` §4, *How the commits are split*). A module and the architecture paragraph that maps it are one commit.

**Rules:**

- A module and the architecture paragraph that maps it land in one commit.

## 4. Agent files at the retrospective

A Backend Repo's agent files are copies of the Backend Kit's. They change mostly when a retrospective is applied: the Agent Skills it taught are edited then, each with its Decisions Log entry. So the split of agent files from records comes up there. CBC Run 3's plan for its SL-3 work put two changes to agent files inside a records commit, and a revision split them out.

## 5. A try before the choice

A question the Backend Repo must not decide alone is tried before the choice, each option on a branch of its own (`knowledge/backbone-ideas/commit-sets.md` §5, *At each boundary*). CBC Run 4 tried 14 options this way, and 2 changed the answer. A look for a better way after the work was handed to CBC Runs 5 and 6, and found nothing: CBC Run 5 wrote 13 lines of it and tried nothing, and CBC Run 6 found nothing 12 times and struck it.

## 6. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

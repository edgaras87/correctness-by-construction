# Commit sets, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/commit-sets.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Case for commit sets.
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first sources, input and not rules (PLAN.md, the commit-plan manual's Plan Step, decision C):
- the commit-plan manual, docs/conventions/commit-plan/README.md: What it is for, the Commit Set revised four times; §2.4, its story;
- devlog 2026-11-01, round 3 worked and closed: the close read's followers, and the rename grep that missed a wrapped quote.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is commit sets in the Maintainer Repo's Problem Domain, keeping knowledge: what a repo that keeps only texts meets in its Commit Sets. How work larger than one commit is planned is commit sets' (`knowledge/backbone-ideas/commit-sets.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Rule | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Commit Plan | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Commit Set | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Fact Reference | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. Found in the material

In a repo that keeps texts, what a text should say often shows only once it is written. The reviewer reads it at the boundary, and finds there what they want. So here the decision usually lives in the material (`knowledge/backbone-ideas/commit-sets.md` §4, *How the commits are split*). A Commit Plan expects revisions at its boundaries, and a revision is the Commit Plan working, not failing. On 2026-09-27 and 28, one Commit Set was revised four times at its boundaries, on the reviewer's readings, each revision in its own commit.

## 3. A follower for the agent files

The agent files here are text, like the ideas they come from. A change to an idea often reaches an Agent Skill or Agent Rule built on it. The two cannot share a commit (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*). So one change lands as two commits: the text's, then the agent file's, which follows it. Round 3's close read planned 19 commits and landed 31; 5 of them were such followers.

**Rules:**

- A Commit Plan plans an agent file's follower as a commit of its own, after the text it follows.

## 4. The sweep weighs most

A text here is pointed at by Fact References from many others. A moved home reaches them all, and older text is often wrapped. So the sweep before the close finds most here (`knowledge/backbone-ideas/commit-sets.md` §6, *The close*). In Round 3, a commit relabelled a part, and its own search missed a quote of the old label broken across two lines. The next commit's search, with the lines joined, found it.

## 5. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

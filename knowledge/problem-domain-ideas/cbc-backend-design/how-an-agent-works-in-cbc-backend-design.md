# How an agent works, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/how-an-agent-works.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Cases, written from it for a Backend Repo's agent work (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.3, The Adapted Case layer).
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules: the Agent Model, docs/models/agent.md, deleted on 2026-11-27, its last state in git at 703ff7ca: §1; P2's test; §12's evidence seen in the Backend Repos. The Tiers Model, docs/models/tiers.md §3.2, The Told Channel, for §2's warning told by hand.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is how an agent works in the Backend Repos' Problem Domain, CBC backend design: why a Backend Repo is the case the channels must be got right for, and what the Backend Repos' work showed of the claims. The parts, the channels and the claims themselves are how an agent works's (`knowledge/backbone-ideas/how-an-agent-works.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pure Seed | `delivery/installs/pure-seed.md` |
| Told Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |

## 2. The case nobody watches

A Backend Repo works by the Kit Copies it took from the Backend Kit. The rules are written for it, and it is the case nobody watches: what reaches its agent, and what does not, shows only when the Maintainer Repo reads it back. So the question how an agent works answers matters most here: given a rule sitting in a Backend Repo, how does it reach the agent meant to follow it?

A rule can also reach the agent through the Told Channel (`knowledge/backbone-ideas/how-an-agent-works.md` §3.4, *The Told Channel*). The human hands the Backend Repo's agent a warning in the session, after the Backend Repo's own work has missed it and the miss is on record. The warning comes with no Kit Copy, and no Kit Version holds it. The Backend Repo's records say it was told. A Backend Repo that leans on such warnings shows the Told Channel's diagnostic: a rule is missing from its Kit Copies, or one there is not firing.

## 3. What the work showed

The evidence seen in the Backend Repos, then called CBC Runs, under each claim's label (`knowledge/backbone-ideas/how-an-agent-works.md` §10, *Claims*).

**A1. Presence is not compliance.** CBC Run 3's commit subjects crossed 50 characters at every Plan Step the Maintainer Repo read, at 52 to 56 (the Maintainer Repo's devlog, 2026-09-10 to 09-14).

**P2. Placement decides whether a pointer fires.** The test that can run: the Maintainer Repo reads a Backend Repo that holds one rule both ways, pointed at from an Agent Skill at its moment, and from the Entry File alone.

**W2. Roles rank.** Three CBC Runs of the Pure Seed, reported 2026-09-10, two incidents among them:
- a stop the change-plans Agent Skill of the time asked for, skipped on an instruction the prompt never gave;
- a checkout opened because the prompt's "stay inside this repository" had not fired yet, while the CBC Run's own procedure named a checkout on disk.

## 4. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

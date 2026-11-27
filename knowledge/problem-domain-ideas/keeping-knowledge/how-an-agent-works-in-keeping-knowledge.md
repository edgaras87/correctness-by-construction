# How an agent works, in keeping knowledge

<!--
What it is: a Problem Domain Idea of keeping knowledge, the Maintainer Repo's Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/how-an-agent-works.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: this repo's own Adapted Cases, written mostly from it (knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md §3.4, The layer of a repo's work).
Its place in the repo: knowledge/problem-domain-ideas/keeping-knowledge/ (ADR-0084).
Its first source, input and not rules: the Agent Model, docs/models/agent.md, deleted on 2026-11-27, its last state in git at 703ff7ca: §1's last line; §12's evidence seen in this repo and in the handbook.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is how an agent works in the Maintainer Repo's Problem Domain, keeping knowledge: how the Maintainer Repo meets the channels, and what its own work showed of the claims. The parts, the channels and the claims themselves are how an agent works's (`knowledge/backbone-ideas/how-an-agent-works.md`).

## 1. Its Defined Terms

Borrowed:

| Defined Term | Defined in |
|---|---|
| Agent Skill | `docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`* |
| Ambient Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Enforcement Gate | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Entry File | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Pulled Channel | `knowledge/backbone-ideas/how-an-agent-works.md` §1, *Its Defined Terms* |
| Record Stub | `knowledge/problem-domain-ideas/cbc-backend-design/records-in-cbc-backend-design.md` §1, *Its Defined Terms* |

## 2. The same channels

The rules are written for the Backend Repos, where nobody watches the agent work. An agent in the Maintainer Repo, the repo that writes them, meets the same channels all the same.

## 3. What the work showed

The evidence seen in this repo's history and in the handbook's, under each claim's label (`knowledge/backbone-ideas/how-an-agent-works.md` §10, *Claims*). The handbook is the repo that held the working arrangement before this one, now history (ADR-0038).

**A1. Presence is not compliance.**
- The commit-subject limit, 50 characters or fewer, was in the handbook's Entry File, its Ambient Channel, from its Step 6, and in its commit-messages Agent Skill, its Pulled Channel, from its Step 5. 15 of the handbook's first 20 commits exceed it. Present, correct, unfollowed.
- Here too: 125 of this repo's 233 commits from 2026-09-20 to 09-29 run over 50 characters, though the commit-messages Agent Skill is opened at every commit here. Seven of the eight revisions of commit plans of 2026-09-29 ran over too, the longest at 67.
- The question it raises, for the commit-messages idea when the rewrite reaches it: is the limit only unenforced, or set wrong? `docs(handbook):` takes 15 of the 50 characters before the verb. Here the commit-plan Agent Skill's own revision form, `docs(agent): revise commit plan — `, takes 34 before saying what changed.

**O1. Divergence is invisible without a comparison.** Here, three divergences were missed until a comparison was run for another reason:
- ADR-0024 decision 4 said `fills/` retires, and it still held one file, added 2026-09-18; found on 2026-09-29 while PLAN's Step 8 was being shrunk.
- PLAN's decision index went stale twice, found each time while something else was being written.
- The project-recording manual said the Maintainer Repo kept its records "under the same stubs" after ADR-0041 had split its PLAN from the Record Stub; found at the reviewer's question.

Earlier, a hygiene change the handbook needed in three places was caught by hand (the handbook's devlog, entry k).

**M1. A hand-written summary is lossy on arrival.** The handbook's commit-messages manual of the time stated "≤50 chars, imperative, **no period**". The handbook's Entry File of the time rendered it as "imperative subject ≤50 chars, body explains why, footers link ADRs/issues". "No period" was gone on arrival.

**G1. Text does not enforce.** The same measurement as A1. The rule existed in two channels in the handbook's first 20 commits. No Enforcement Gate existed. It was broken 15 times. Here too: nothing gates a subject's length, and A1's count is 125 of 233.

## 4. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

# Records, in CBC backend design

<!--
What it is: a Problem Domain Idea of CBC backend design, the Backend Repos' Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.2, The Problem Domain layer). Still a draft and a trial: practice changes it.
What it stands on: knowledge/backbone-ideas/records.md, the Backbone Idea it is adapted from. It adapts that document, and never retells it.
What stands on it: the Backend Kit's Adapted Cases for the records, the Record Stubs and the playbook, and for the scratch space, its README.
Its place in the repo: knowledge/problem-domain-ideas/cbc-backend-design/ (ADR-0084). It is kept in the Maintainer Repo, and never copied to a Backend Repo.
Its first sources, input and not rules: the project-recording manual, docs/conventions/project-recording/README.md, deleted on 2026-11-27, its last state in git at 3bb95746: What this is made usable as; The seats, The CBC Run's seat, and its items 4 to 6; §2.4, §3.3, §3.4, §7.5, §8.1, §8.4 and §9; the records' exception, docs/conventions/exchange/README.md §2.4.
How it is edited: a trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document is records in the Backend Repos' Problem Domain: how a Backend Repo gets its records, what they hold differently, and the playbook its plan starts from. Which records a repo keeps, and why each is written as it is, are records' (`knowledge/backbone-ideas/records.md`). The Backend Kit's Adapted Cases for the records are written from this document.

## 1. Its Defined Terms

- **Record Stub:** a record as a Backend Repo is born with it: the Backend Kit's file, its form in its header, its content still to be filled.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Plan Step Gate | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. At birth

A Backend Repo is born with a Record Stub for each of its records. Each holds its form in its header, so the rule is in front of the agent when it opens the record (`knowledge/backbone-ideas/records.md` §13, *Where a record's rules sit*). From then each record is the Backend Repo's own. A record holds what one Backend Repo did, so a newer Record Stub has nothing to say to a record already filled. The README of its scratch space comes the same way (`knowledge/backbone-ideas/records.md` §15, *The scratch space*).

**Rules:**

- A Backend Repo's first commit holds a Record Stub for each of its records, and the README of its scratch space.
- No Kit Update changes a Backend Repo's records, or its scratch space's README, after birth.

## 3. The plan

A Backend Repo's Plan Steps arrive whole at birth, from the playbook (§4). Its finished Plan Steps are the evidence the playbook is written from, so they stay in its plan.

**Rules:**

- The plan's Plan Steps are filled in from the playbook at birth, and its plan names which playbook, at which version.
- A finished Plan Step stays in the plan, closed to one line that says what diverged from the plan.
- The plan holds "Discovered along the way": what a Plan Step finds and does not do.
- The plan holds an index of the decisions, one line each.
- The look back at the end is not the plan's: it is the retrospective's (`docs/conventions/retrospective/`).

## 4. The playbook

The playbook is the Plan Steps every Backend Repo starts from: their whole sequence, their Plan Step Gates, and what past Backend Repos taught each. It is written from their finished plans. It turns one Backend Repo's experience into the next one's head start: the first plan is already written, and a past mistake stands as a warning at the Plan Step where it happened.

It is part of the Backend Kit, kept in the Maintainer Repo. A Backend Repo holds only the copy in its plan.

The playbook holds every Plan Step, from the first to the last. The plan's Record Stub prescribes none. Each Plan Step keeps the plan's form, and what past Backend Repos taught it as its *Known already*. Its release Plan Step carries the release facts of a backend. It meets four moments, and each says where its doer reads how:

1. **At birth:** its Plan Steps fill the plan, and the plan records which playbook, at which version. A Backend Repo born without one fills the placeholders of its plan's Record Stub in place, as that Record Stub says.
2. **Once the problem is framed:** the Backend Repo confirms its Plan Steps against the framing. It fills in specifics, deletes what it has no use for, adds what it needs, and renumbers. Each later Plan Step is read against what the framing gives out, and reworded where it no longer fits. Born without a playbook, the Backend Repo writes its Plan Steps now.
3. **Before the release Plan Step:** the retrospective writes its record, each decision naming where its lesson lands (`docs/conventions/retrospective/`).
4. **Written back:** each lesson that survives lands in the playbook, as every lesson travels (`knowledge/backbone-ideas/change.md` §4, *The arrows*, the arrow *lesson*). How it lands is the playbook's own header.

**Rules:**

- The playbook is written after the second Backend Repo, never from theory before one is done.
- It is updated from every retrospective; a playbook that stops learning is only bureaucracy.
- The framing and the release Plan Steps have their own place in it, so their lessons have a home.
- Its Plan Step Gates stay light enough that no one works around them.

## 5. The other records

A Backend Repo builds a running system, released in versions, so four records hold more than the Backbone Idea says, and it keeps one record more.

**Rules:**

- The changelog logs releases of the system.
- An ADR records one choice in the build, in under a page: an ADR not written because it is heavy is worse than a short one.
- The architecture describes the modules, the invariants the system holds while it runs, and a map of the code. Its invariants are a table, one row each; how one was proved is the record of the work that proved it.
- The release Plan Step's Plan Step Gate holds "the README is checked on a clean machine".
- What the system promises, and what must never happen, sit in `docs/system/`, written by CBC design (`concept/03-cbc-framing.md`).

## 6. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

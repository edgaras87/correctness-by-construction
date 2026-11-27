---
name: deliver-the-kit-update
description: Make a Kit Update for one Backend Repo, then stage it into the Backend Repo's temp/ on the human's word. Use when the human names a Backend Repo to update, once its Look for Lessons has ended, or asks which Backend Repos are behind.
disable-model-invocation: true
---

# Deliver the Kit Update

Making a Kit Update, then staging it. When one is due, what it holds, and what crosses to the Backend Repo are in Change, in keeping knowledge (`knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §3.5, *Deliver the Kit Update*).

Why each stage is so: `.claude/understanding/deliver-the-kit-update.md`.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Adapted Case | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Agent Skill | `knowledge/backbone-ideas/agent-files.md` §1, *Its Defined Terms* |
| Backend Kit | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Backend Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Copy | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Update | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Kit Version | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Look for Lessons | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Maintainer Repo | `knowledge/problem-domain-ideas/keeping-knowledge/layers-of-knowledge-in-keeping-knowledge.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Update Note | `knowledge/problem-domain-ideas/keeping-knowledge/change-in-keeping-knowledge.md` §1, *Its Defined Terms* |

## Stage 1 — is one due

1. Check that a Look for Lessons ran at this Backend Repo, to its end, since the human named it to update. If not, run it first: the read-copy-changes Agent Skill, then the judge-copy-changes Agent Skill.
2. Compare the Backend Repo's Kit Version, read from `.claude/kit-version.md` at its *settled snapshot*, with the newest. Compare the Backend Kit's files at the two commits, never the commits themselves. If the Backend Repo's is the newest, say so, and stop.
3. Check that none of the Backend Repo's Plan Steps is open. If one is, say so, and stop: make nothing.

## Stage 2 — make it

1. Take every Kit Copy, whole, at the newest Kit Version.
2. Write the Update Note, holding each item Change, in keeping knowledge, lists (§3.5, *What a Kit Update is*). Read each why from the bodies of the Maintainer Repo's commits that changed a Backend Kit file between the two Kit Versions. Cite nothing the Backend Repo cannot open: no path, record or word of the Maintainer Repo's own.
3. Name the Kit Update by the Maintainer Repo's commit at which its files and Update Note are final.
4. Show it to the human, who decides it.

## Stage 3 — stage it, on the human's word

1. Wait for the human's word to deliver. Never stage unasked.
2. Check that the Backend Repo's tree is clean, with no work under way. If it is not, say what you found, and wait for the word.
3. Write the Kit Update into the Backend Repo's `temp/`, nowhere else there. It replaces a Kit Update already waiting.
4. Compare each staged file with the new Kit Version.

## When the human asks which are behind

Compare each Backend Repo's Kit Version with the newest, as in Stage 1, step 2. Say which are behind, and make nothing.

## Gates

- A Look for Lessons ended at this Backend Repo before the Kit Update was made.
- No Plan Step of the Backend Repo's was open.
- The Update Note holds each item Change, in keeping knowledge, lists, and cites nothing of the Maintainer Repo's own.
- The Kit Update was staged only on the human's word, only into the Backend Repo's `temp/`.
- Each staged file matches the new Kit Version.

## What this does not do

- It does not take the Kit Update. The Backend Repo does, at the opening of its next Plan Step.
- It writes nothing in the Backend Repo outside `temp/`.

---

## Decisions

- ADR-0087 — written from the simulation alone, whole with its understanding; making and staging in one Adapted Case
- ADR-0084 — this repo's own Adapted Cases kept whole in `.claude/`
- ADR-0089 — not invoked by the agent on its own, since a CBC Run reads as a Backend Repo by its description

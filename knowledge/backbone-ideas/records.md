# Records

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules: the project-recording manual, docs/conventions/project-recording/README.md, deleted on 2026-11-27, its last state in git at 3bb95746: its What it is for; §1; each record's what, why and where, and the reasons for its form that every repo shares, from §2 to §8; §11 to §13; Why it arrives this way. A Plan Step's stages as the plan of its commits, from both Problem Domains' work: the Plan Steps of the Maintainer Repo's rewrite into the layers, from 2026-11-26, which opened no Commit Plan; CBC Run 4's Plan Steps, which opened one only for its retrospective (TODO-CONVERSATION-MEMORY.md §9, A commit plan's look-back at the way; PLAN.md, the commit-plan manual's Plan Step, decision E). A Plan Step Gate item's commit, from the commit-plan Agent Skill, .claude/skills/commit-plan/SKILL.md, its §3 (ADR-0038, 1d; PLAN.md, the same Plan Step, decision G).
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says which records a repo keeps, what each answers, and how they feed each other. It names no Problem Domain: each Problem Domain Idea adapted from it says what its own repos keep differently, and what they add.

## 1. Its Defined Terms

- **Local Map:** a folder's README that says how the parts of that folder relate. `ARCHITECTURE.md` points into it.
- **Plan Step:** one piece of a repo's plan: the work it holds, its Plan Step Gate and its live status.
- **Plan Step Gate:** a Plan Step's exit criteria: facts that can be checked. The Plan Step is done only when every one is true.
- **Records Table:** the table, in the text read before any work in a repo, that gives each record one row: the moment it is opened, what it holds, and its path.
- **Repo Tag:** the short upper-case name a repo's decisions carry when another repo cites them, such as `ABC ADR-0012`.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Commit Plan | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Commit Set | `knowledge/backbone-ideas/commit-sets.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |

## 2. What records are for

A repo keeps records so that what it decided, where it stands, what it tried and what it learned can be read by someone who was not there: a newcomer, the same person months later, or another repo that reads this one through its records alone. A fact that is only remembered is lost when its holder forgets or leaves.

## 3. The records

| Record | Where | What it answers |
|---|---|---|
| The README | `README.md` | what this is, who it is for, how to use it, where the rest is |
| The plan | `PLAN.md` | where the work stands, what is next, what *done* means |
| The backlog | `TODO.md` | what is known and not yet done |
| The decisions | `docs/adr/` | why it is built this way |
| The devlog | `devlog/` | what happened, the dead ends, where to resume |
| The architecture | `ARCHITECTURE.md` | what stands now, and how its parts tie |
| The changelog | `CHANGELOG.md` | what changed in each version, for whoever takes it |

The table gives each record's usual place. §4 to §10 say what each is and why it is written as it is.

## 4. The plan

A plan is its Plan Steps. The whole of the work is sketched coarsely, and the next one or two Plan Steps in detail. The detail moves forward as Plan Steps close. Each Plan Step has a live status and a Plan Step Gate. The plan answers, at any moment, where the work stands, what is next and what *done* means. Without it, those three answers live only in someone's head.

A Plan Step whose stages each land as one commit or a few needs no Commit Plan: its stages already list its commits. A stage that takes many commits opens a Commit Plan of its own (`knowledge/backbone-ideas/commit-sets.md` §3, *The Commit Plan*).

**Rules:**

- A Plan Step Gate holds facts that can be checked, never intentions: "tests pass on a clean clone", not "the code is good". So no Plan Step is declared done from fatigue.
- A closed Plan Step says what diverged from the plan.
- A Plan Step links out to its decisions and its history, so the plan is the record the others point back to.
- A Plan Step that stops is neither done nor dropped. It keeps its place and the work it did, and resumes where it stopped.
- A Plan Step's goal is one piece of work. A goal that grows past one is re-cut: the Plan Step Gate's items that moved are struck, each naming the backlog item it went to, and the Plan Step closes.
- Updating the plan is part of the work, so no status goes stale.
- No Plan Step is detailed long before the ones ahead of it are done.
- A stage of a Plan Step that takes many commits opens a Commit Plan. Stages of one commit or a few need none.
- A Plan Step Gate item closed inside a Commit Set names the commit that closes it.

## 5. The decisions

An ADR, an architecture decision record, is one short document for each significant decision: the context that forced it, the options considered, the decision, and its consequences, the downsides knowingly accepted among them. The work shows what was built; the ADRs keep why. "We already considered that, and rejected it because…" stops the same debate from coming back.

ADRs sit in `docs/adr/`, one file each, `NNNN-short-title.md`, numbered in order.

**Rules:**

- An ADR keeps the options it rejected: they are half its value.
- A decided ADR is never edited. A changed mind is a new ADR, and the old one stays.
- An ADR is never renumbered.
- What needs an ADR is a question a later reader would ask, not a size: a variable's name, no; a database, a framework, build or buy, yes.
- An ADR written before its decision is taken, as Proposed, is better still: the writing often changes the decision.
- A bare ADR number names a decision of the repo where it is read. A decision of another repo is cited with that repo's Repo Tag before its number. A text written to be read in another repo carries the Repo Tag on every citation.
- Each repo declares its own Repo Tag once, in its README.

## 6. The devlog

The devlog is the repo's journal: dated, informal entries of what was worked on, what was tried, what failed and why, open questions and hunches. It pays three ways:

1. A dead end is recorded, so it is not explored again. "Tried caching at the storage layer; it caused stale reads" saves the next attempt.
2. Resuming after a break takes minutes, not an hour of reading.
3. The records above it are written from it: a struggle in the devlog becomes an ADR's context, or a lesson.

It sits in `devlog/`, a file per month, such as `devlog/2026-08.md`. A small repo may keep one `devlog.md` and split it by month once it passes 300 lines. The newest entry is on top.

**Rules:**

- An entry is written for whoever resumes the work, in short plain sentences, and honest: "I don't understand why this works" is a valid entry.
- An entry names the work it was part of, and marks a dead end loudly, so both can be found by search.
- A session ends with a "Resume:" line. It marks a place in the work, not a time: work resumes after hours, days or weeks.
- Failures are recorded, not only successes: the failures are the valuable part.
- An entry is never cleaned up afterwards.
- The devlog never stands in for an ADR: a decision found in it is written up as one.

## 7. The backlog

The backlog holds everything known and not yet done: work not yet in a Plan Step, bugs, ideas, and problems put off on purpose. A thing known and not written down costs attention. Written down and sorted, it costs nothing until its time. It also makes putting off explicit: "we know, and chose not yet" is a decision, recorded here.

It sits in `TODO.md` at the root. A team may keep it in an issue tracker instead: the form is the same, the tool differs.

**Rules:**

- An item goes in when it is found, so no one has to remember it.
- Open work only. A closed item goes: the devlog, the ADRs and history already say what closed.
- It is pruned. A list too long to read is no plan, and deleting an idea that would come back anyway, if it mattered, costs nothing.
- An item says enough to be sorted without opening anything else, and no more: told tighter, it lost meaning; looser, it grew back into its story.
- An item's story is written where the repo keeps its history, when the item is added, and the item points at it.
- An idea on an item is noted, never weighed, until the item is due. It is then not lost to the session that had it, and not mistaken for a decision.
- An item that changes is rewritten true for today. A dated update stacked on it is history.
- A to-do note left in the work itself names its item, or it is forgotten.
- The backlog is not the plan: it has no Plan Step Gates and no order.

## 8. The changelog

The changelog is the record of notable changes in each version, written for those who take the repo, not for those who build it. "What changed between 1.3 and 1.5, and will it break me?" is answered without reading history. Commits are too fine and in the builders' words; the changelog is the curated digest.

It sits in `CHANGELOG.md` at the root, in the Keep a Changelog form (keepachangelog.com), with Semantic Versioning. What a version is depends on what the repo gives out, and the changelog says so at its start.

**Rules:**

- An entry is written when its change is made, never put together at release. `[Unreleased]` gathers the entries, so a release is a rename.
- A breaking change is called out, so whoever takes the version sees it first.
- It speaks to its readers: "creating an order is about three times faster", never "refactored the order service".
- It is never a dump of the commit log.

## 9. The README

The README is the first page a person reads: what this is, who it is for, how to use it, and where everything else is. Whether the other records are found at all depends on it. A newcomer reads it first, then the architecture, then the plan, then the ADRs as needed. The devlog and the backlog are working records, never read cover to cover.

It is for people. A repo an agent works in gives the agent its own first file, and the two share no text.

It sits at the root, in every repo.

**Rules:**

- It has a table of the repo's records, how a newcomer finds them. Its row for the decisions declares the Repo Tag.
- It says only what is already true. A section arrives when it becomes true, never ahead.
- A Plan Step whose Plan Step Gate makes true something the README should say updates the README in that Plan Step. It is never a standing item on every Plan Step Gate: an item that is usually empty trains ticking it unread.
- What changes often lives elsewhere, and the README links to it: a wrong README is worse than a sparse one.
- How to set it up works on any machine, not only the author's.

## 10. The architecture

The architecture is a short description of the repo as it stands now: its main parts, what each is responsible for, how they talk to each other, where its important invariants are held, and where each part is found. Later work may rely on it. The ADRs are a history of single choices; this is the present, put together. (The form was made popular by matklad's essay "ARCHITECTURE.md".)

It sits in `ARCHITECTURE.md`, at the root or in `docs/`.

**Rules:**

- One or two pages: a newcomer reads it second, after the README. It describes the whole; each part's detail is in the part.
- It states, and never argues: the why behind a choice is its ADR's, linked.
- It is checked when a Plan Step closes, since that is when the structure it describes can have moved.
- It describes the repo as built, never as hoped.
- A part of it that no one reads goes.
- An area gets a Local Map when its parts relate in ways the architecture should not carry: how they connect, hand work to each other, or land elsewhere. A Local Map holds those relations only: no count or list the architecture holds, and nothing a part says about itself. Its first lines say what it maps, and point at the rest.
- Not every folder's README is a Local Map: a README that holds a folder's rules is another kind.

## 11. How records feed each other

Each record is written from the one below it. The devlog holds what happened; the records above it keep what lasts:

```
devlog (raw, daily)
  → ADR           when a struggle ends in a decision
  → backlog       when it shows work for later
  → plan notes    when it explains why a Plan Step diverged
       → changelog      when a Plan Step gives out something its readers see
       → architecture   when a Plan Step changed the repo's structure
```

**Rules:**

- Each fact has one home, and the other records point at it (`knowledge/backbone-ideas/one-home.md` §3, *A fact and its home*).
- What matters is written up, never left to memory. A dead end noted in the devlog is safe; one only remembered will be repeated. The same holds for decisions, written up as ADRs, and lessons.
- Records are updated at moments in the work, never on a schedule. Bound to events, recording never becomes a chore of its own to skip. Each record's moment is stated once, in the Records Table (§12).
- Cheap at the bottom, lasting at the top. The devlog may be rough; the ADRs must be clean. Effort goes where a record will be read again.
- Records are Markdown, in the repo, versioned with it, so they branch, are reviewed and roll back with the work they describe.

## 12. The Records Table

The Records Table gives each record one row of three things: the moment it is opened, what the record holds, and its path. Adding a record adds its row. What the record holds is a short summary of its row in §3.

The moment is the part that is new, and the part that carries the weight. With it, the table reads both ways. "I just did X: where does it go?" reads down the moments. "Where is Y recorded?" reads down what each holds. A rule written only inside the record it governs teaches how to write it, never when: "write a devlog entry at a session's end" sits in the devlog, and opening the devlog at a session's end is what needed saying.

It sits in the text read before any work, so every session meets it.

**Rules:**

- Each row names the moment, what the record holds, and its path.
- A moment says when to open the record, and nothing about what to write.
- It holds no status: where the work stands is the plan's, and the plan's row says so.

## 13. Where a record's rules sit

A record's form is how its entries are written, and when one goes. It sits in the record's own header. Acting on the record puts its rule in front of the writer: there is no reminder to fire and nothing to remember. Timing is the one exception, since a rule saying when to open a record cannot sit inside it. So the Records Table carries a moment for each record (§12). A reminder that fires when the worker sees the moment would not do: not seeing the moment is the failure it is meant to fix.

**Rules:**

- A record's form sits in its own header.
- When to open a record sits in the Records Table, and only there.
- A record's rules are never restated in the text read before any work, "so they are always there": that text then grows past what is read.

## 14. The fewest records

Not every repo needs every record. They scale with the stakes:

- a throwaway or an experiment: the devlog only, and even that is worth it;
- a real repo, worked alone: the README, the plan, the backlog, the devlog, and an ADR when a real decision is taken;
- anything with users or other workers: add the changelog and the architecture.

**Rules:**

- A record is added when someone, probably its own writer later, will need its answer and be unable to rebuild it. It is then written once, at its home.

## 15. The scratch space

A repo's work makes things it needs for a while and then drops: a draft of a text whose home is elsewhere, notes taken while working, a tool's output, a file kept for work still to come. They sit in one folder, `temp/`, with a README that says what it holds.

**Rules:**

- Nothing in the scratch space is a record, and nothing there is in force.
- What must last moves out to its home: a decision to an ADR, work for later to the backlog, a fact to where its kind lives.
- It is tracked, so what was drafted shows in history.
- A file is deleted once it has served; history keeps it.
- The devlog tells what a draft was for: made, passed or deleted.

## 16. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

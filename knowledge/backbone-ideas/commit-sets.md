# Commit sets

<!--
What it is: a Backbone Idea, bound to no Problem Domain, and its one home (knowledge/backbone-ideas/layers-of-knowledge.md §3.1, The Backbone Idea layer).
Its place in the repo: knowledge/backbone-ideas/ (ADR-0084).
Why it is an idea of its own: both Problem Domains work by it (temp/rewrite-map.md §10, Shared questions, QUESTION-7).
Its first sources, input and not rules: the commit-plan manual, docs/conventions/commit-plan/README.md: its opening; What it is for, without its lived history; §1; §2.1 to §2.12; What this does not cover, as the neighbours below. From the commit-plan Agent Skill, .claude/skills/commit-plan/SKILL.md: when a Commit Plan is needed; divergence; an ADR opened Proposed. Read for ideas: temp/model-example/idea/commit-set.md. No Commit Plan where a Plan Step's stages list the commits: records holds the rule (PLAN.md, the commit-plan manual's Plan Step, decision E). The decisions behind them: ADR-0038, 1b, 1d and 1e; ADR-0049, 1 and 3; ADR-0050; PLAN.md, the commit-plan manual's Plan Step, decisions A, B, D, E and F.
What stands on it: its Problem Domain Ideas, one for each Problem Domain. Each points here, and never retells it.
How it is edited:
- It gives no example from one Problem Domain's work.
- It names no file that carries its rules to the agent: that is each Adapted Case's.
- A trial, as in the layers of knowledge: a section's rules close it, in a last paragraph marked Rules, and govern that section.
-->

This document says how work larger than one commit is planned as commits, reviewed as they land, and closed. It names no Problem Domain: each Problem Domain Idea adapted from it says when its own repos plan one.

Its neighbours: how a commit is written, what may share one, and the stop at every commit are commit messages' (`knowledge/backbone-ideas/commit-messages.md`); which records a repo keeps, and what a decision record is, are records' (`knowledge/backbone-ideas/records.md` §3, *The records*); which files are agent files is agent files' (`knowledge/backbone-ideas/agent-files.md` §3, *The agent files*); the order of the work inside a set is the instructions' for that kind of work.

## 1. Its Defined Terms

- **Commit Plan:** the list of a Commit Set's commits, agreed before the first lands: one file at the repo's root, deleted at the close.
- **Commit Set:** a body of work that needs more than one commit, planned as commits before it starts, reviewed as they land, and closed.

Borrowed:

| Defined Term | Defined in |
|---|---|
| Backbone Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Living Text | `knowledge/backbone-ideas/one-home.md` §1, *Its Defined Terms* |
| Plan Step | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Plan Step Gate | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |
| Problem Domain | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Problem Domain Idea | `knowledge/backbone-ideas/layers-of-knowledge.md` §1, *Its Defined Terms* |
| Records Table | `knowledge/backbone-ideas/records.md` §1, *Its Defined Terms* |

## 2. What a Commit Set is

A Commit Set is a patch series, carried into a repo where work is committed directly instead of mailed. Each commit is one logical change, ordered so each applies on the last. The series is reviewed commit by commit, not as a lump. What it adds is a Commit Plan, agreed before the series is written, and its disposal afterwards.

The Commit Plan lets the work be inspected commit by commit before it lands. When a commit turns out to need something the Commit Plan did not foresee, the commits left are weighed again. They are not carried on by a Commit Plan that no longer holds.

A Commit Plan plans the commits, not the change. What the work is to do is settled before it opens. It costs commits of its own, so it pays only across a sequence. It pays most when the split could turn out wrong halfway, or when someone other than the author reviews as the work lands.

**Rules:**

- Work worth more than one commit is a Commit Set. A change of one commit has no Commit Plan.
- A Commit Set's commits are agreed before the first lands: in a Commit Plan, or in a Plan Step's stages (§3).

## 3. The Commit Plan

A Commit Plan is one file at the repo's root, one at a time. It is committed once it is agreed, and deleted at the close. Everything lasting in it survives as the commit messages it produced. Where a Plan Step's stages already list the commits, in the plan, the record of Plan Steps, no Commit Plan is opened (`knowledge/backbone-ideas/records.md` §4, *The plan*).

- **Not a record.** It is temporary. Nothing in it is meant to be read a year later, except through the log. So it sits outside the records (`knowledge/backbone-ideas/records.md` §3, *The records*), which are all added to or kept up to date.
- **Not an agent file.** It is the trail of one piece of work, as a commit message is. It tells the agent nothing about how to work. So a commit of the Commit Plan is a commit of the work.
- **At the root.** A set half landed can be seen from a clean clone: where it stopped is answered without the working tree.
- **No status in it.** Tracking status there ties every commit of the work to an edit of the Commit Plan, and one not edited goes stale. The log is the status: the commits that exist are the Commit Plan done so far.
- **Commits, never Plan Steps.** A Commit Plan counts commits. "Step" belongs to the plan, the record of Plan Steps (`knowledge/backbone-ideas/records.md` §4, *The plan*), and one word would carry two meanings.
- **Numbers that stay.** A Commit Plan's numbers are cited, in its notes, its revisions and its commit bodies. So a commit inserted later takes a letter, and none is renumbered. Where one change reaches many records, one planned commit repeats over them, naming its order and what stops it.
- **Subjects counted when written.** A Commit Plan writes every subject before any lands, so each is counted against the subject's aim then (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*). Counted only as each lands, a long one lands long, or is rewritten with nothing in the Commit Plan saying why.

**Rules:**

- A Commit Plan is one file at the repo's root, committed once agreed, deleted at the close.
- Each planned commit has its subject and a note saying why it is a commit of its own. Its body is written when it is committed.
- The Commit Plan holds no status.
- A commit inserted later takes a letter after the number it follows.
- A planned commit may repeat over a series of records. It names their order, and, if it may run again, the rule that stops it.
- Each subject is counted when the Commit Plan is written. A commit it left provisional gets its subject at its commit, counted there before it lands.

## 4. How the commits are split

**Split by change, not by file.** One commit is one thing the repo needs, whatever files that touches. One file may appear in as many commits as it has distinct changes. The test is to revert: undo one commit, and the repo still makes sense. Commits grouped by kind of file look tidy, and revert into nonsense.

**Order follows where the decision lives.** A decision settled in talk is recorded first, then carried out. A decision that shows only in the material is found by touching the material, and the lasting record is written from what held. One Commit Plan may mix both, one decision at a time. With the second kind, its last commits are provisional, and it says so. Provisional commits, a revision commit and a decision record opened as proposed are then the normal course, not a sign the Commit Plan failed.

**The records are planned with the work.** While the Commit Plan is drafted, the Records Table is walked. A Commit Set reaches the moments its records name, and a record's moment can come midway, before the fact it records is true. Walking the table while drafting catches it.

**Agent files apart.** A commit that touches agent files touches nothing else (`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*). So a records commit planned to carry a correction to an agent file is split when it opens.

**Rules:**

- Each commit, reverted alone, leaves the repo coherent.
- A decision settled in talk is recorded before it is carried out. A decision found in the material is recorded from what held.
- No commit refers to what does not yet exist. The lasting records are caught up before the close.
- Every record whose moment the Commit Set reaches gets a commit, where its truth exists. A Commit Set that closes a Plan Step Gate item names the commit that closes it.
- A decision record opened inside a Commit Set is proposed until the set's last records commit, never accepted earlier.

## 5. At each boundary

Each commit is a boundary. The stop there is commit messages' rule (`knowledge/backbone-ideas/commit-messages.md` §5, *Commit on the word*), and holds at every commit, inside a Commit Set or not.

**When the Commit Plan no longer holds,** work stops before the commit. The commits left are weighed again, and it is revised in a commit of its own that says what forced it. A provisional commit given its final shape goes the same way: that is planned refinement, not divergence.

**A second way, while the choice is open.** At a boundary, the agent may see another way worth trying. It names it beside the diff. On the human's word, it tries it on a branch of its own, and the two are compared before one is kept. A second way pays while the choice is still open. Looked for after the work, when every commit stands on the first way, it is not part of a Commit Set.

**Small commits.** On the human's grant, a planned commit may be built as several small ones: a try, a fix, a way abandoned. Before its boundary they are folded into the one commit the Commit Plan names, so the human still sees one commit there. When each planned commit lands as one, there is no room to try. The grant is the human's because a small commit is still a commit. Without it, every commit is a boundary.

**Rules:**

- A commit that needs other than the Commit Plan says waits. The Commit Plan is revised first, in a commit of its own, saying why.
- A second way worth trying is named at the boundary, and tried only on the human's word, on a branch of its own.
- Small commits come only on the human's grant, and are folded into their planned commit before its boundary. What was tried is kept on a branch.
- Each small commit is counted when it is written, as a planned subject is.

## 6. The close

The close commit deletes the Commit Plan. Its body is the set's look back, the cheapest that exists: what diverged, and why. A set abandoned closes the same way, with its reason.

**The sweep.** Before the close, every name the Commit Set moved is looked for again, all at once. A commit that moves a home searches for the names it meant to move (`knowledge/backbone-ideas/one-home.md` §5, *When a home moves*), and misses the rest. A search reads line by line, and older text may be wrapped, so a name broken across two lines is never found. The sweep reads the text with its lines joined.

**The look back.** Each boundary shows one commit; nothing shows the set. So before the close, the landed commits are looked at whole. Two can turn out to be one change, or one commit two. They are regrouped on the human's word. The look back judges the grouping, not the way the work was done.

**Rules:**

- The close commit deletes the Commit Plan, and its body says what diverged and why, or that nothing did.
- Before the close, Living Text is searched for every old name, path, number and title the set moved, all at once, with its lines joined.
- Before the close, the landed commits are looked at whole, and regrouped only on the human's word. The Commit Plan is revised to match what landed.

## 7. Open questions

None is open now. A question joins this list when work meets one, and leaves it once its answer is in the text above.

# Commit plan

**How work larger than one commit is planned as commits, reviewed
as they land, and closed.**

## What it is for

So that a change set can be inspected commit
by commit before it lands, and a divergence at commit *k* forces the
remaining commits to be re-evaluated rather than continued on a
plan that no longer holds. Adopted with the container
(ADR-0038, 1b): the failure it answered was lived elsewhere — a
commit sequence kept by hand in a scratch file across four
sessions, fitting no record — and is not ours to restate. Lived
here since: every set since 2026-08-27 has run under it, and on
2026-09-27 and 28 one set was revised four times at its boundaries
on the reviewer's readings, each revision on its own commit — the
failure it guards against, doing otherwise than the plan and
fixing it afterwards or not at all, has not happened here.

## What this is made usable as

- **`delivery/container/.claude/skills/commit-plan/SKILL.md` — the
  skill, shipped**, held at `.claude/skills/commit-plan/` and opened
  when work turns out to need several commits. The rules, one
  sentence each, with the decisions it rests on in its footer.
- **`.claude/skills/commit-plan/SKILL.md` — the Concept Deliverer's**,
  derived from this page like the container's, neither copied from
  the other, and written for this Convention Seat (ADR-0042, ADR-0069).

This page explains; the skill states. What derives from this page
is that list. A change here walks it; a change forced in one of
them is checked back against this page.

## The seats

A CBC Run runs its change sets under the skill, the plan file at its
root its own. The Concept Deliverer runs its change sets under the same
skill, the plan file at its root its own.

## 1. What a commit plan is

The unit is the change set: the scope between one commit and a
whole project.

A patch series, carried into a repo where work is committed
directly instead of mailed: one logical change per commit, ordered
so each applies on the last, reviewed commit by commit rather than
as a lump. What is added is the plan agreed before the series is
written, and its disposal afterwards. The plan is one file at the
repo root, `COMMIT-PLAN.md`, committed after it is agreed and
deleted at the close; everything durable in it survives as the
commit messages it produced, and the close commit's body is the
cheapest retrospective that exists.

Two ideas carry the rest. **Commits are split by change, not by
file**, and the test is revert: undo one commit and the repo must
still make sense. **Order follows where the decision lives**: a
decision settled in conversation is recorded first and implemented
second; a decision only visible in the material is found by
touching the material, with the durable record written from what
held. The second kind makes the tail of a plan provisional, and the
plan says so.

## 2. Why it is shaped this way

### 2.1 A convention, not a record

It is a scaffold, not a record: nothing about it is meant to be read a year later except
through `git log`, so it sits outside
`docs/conventions/project-recording/`, whose records are all
append-or-evolve (ADR-0038, 1b).

### 2.2 Root placement

An in-flight change set is visible from a
clean clone, so "is work half-landed, and where did it stop?" is
answerable without the working tree.

### 2.3 Status in the file

Tracking status there couples every work commit to a plan edit and reintroduces the staleness that
makes a neglected plan lie. Git history is the status.

### 2.4 Material-first

Some decisions show only in the material: no conversation can
settle them before the work is touched. For them, the provisional
tail, the revision commit and the Proposed-then-Accepted ADR are the
normal road, not a sign the plan failed (ADR-0038, 1e). *Its story: devlog 2026-09-27, afternoon; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.5 The records commits

A change set batches record moments, and a record's trigger can fire mid-set before its truth
exists. Walking the entry file's records table while drafting the
commit list is what catches it (ADR-0038, 1d).

### 2.6 What a plan counts

"Step" is `PLAN.md`'s word; a plan that called its commits steps
would give one word two meanings (ADR-0049, 1). *Its story: devlog 2026-10-08; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.7 Inserted and repeated commits

A plan's numbers are cited, in its notes, its revisions and its
commit bodies, so a commit inserted later takes a letter rather
than renumbering the rest. Where one change reaches many records,
one planned commit repeats over them, naming its order and the
rule that stops it. *CBC Run 3's Step 10 inserted 8b, 22b and E2.1 to
E2.12 after its plan was written, and ran one plain pass three
times over its records, the third only over what the second
changed (ADR-0050, 4 and 5).*

### 2.8 Counting subjects

A plan writes every subject before any lands; counted only at each
boundary, a long one lands long, or is rewritten there with
nothing in the plan saying why. *Its story: devlog 2026-10-08; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.9 The agent's files

A commit that touches them is kept apart from everything else
(`docs/conventions/commit-messages/` §2.3, *The `agent` scope*), so
a records commit planned to carry a skill's correction has to be
split when it opens. *The same plan put two changes under
`.claude/` inside its records Plan Step, and split it by revision.*

### 2.10 The sweep

A commit that renames a file, renumbers or retitles a section, or
moves a fact greps for the old names in that commit
(`docs/conventions/facts-in-sync/` §3.3, *The rename grep*). Before the close,
the sweep looks again for every name the set moved, all at once: a
commit's own grep looks for the names it meant to move, and misses
the rest. It reads the text unwrapped. A grep matches line by
line, and a manual wraps its prose, so a name broken across two
lines is never found. *Its story: ADR-0049; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.11 Small commits

Each planned commit landing as one leaves no room to try: two
ways meant reworking a commit in place. Small commits give the
room, and are folded into the planned commit before its boundary,
so the reviewer still sees one commit there. The grant is the
reviewer's because a small commit is still a commit, and the stop
at every commit is commit-messages' rule (§2.13, *The stop at every boundary*);
without the
grant, every commit is a boundary. Each small commit is counted
when it is written, as a planned subject is. *Its story: ADR-0050.*

### 2.12 The look back

Each boundary shows one commit; nothing showed the set. Looked at whole, two commits can turn out
one change, or one two, and are regrouped on the reviewer's word.
*CBC Run 3's polish regrouped 36 small commits into 7, after the fact
(ADR-0050, 3).*

### 2.13 The stop at every boundary

It is commit-messages' rule, and this convention points at it
(`docs/conventions/commit-messages/` §2.4, *Commit on the word*). *Its story: ADR-0038; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## Why it arrives this way

A skill, because its moment is one the agent recognises — work turning
out to need several commits — and nothing in a record would put the
plan in front of it then (`docs/models/agent.md` §4.2, *pulled*). The one rule
that must fire at every commit, the stop, is not here: a skill that
opens only for multi-commit work cannot carry it, so it is
commit-messages' (`docs/conventions/commit-messages/` §2.4, *Commit on the word*).

## What this does not cover

- **The commit boundary itself, and the `agent` scope** —
  `docs/conventions/commit-messages/`.
- **The records a plan is walked against, and what an ADR is** —
  `docs/conventions/project-recording/`.
- **The order of the work inside a plan** — the domain skill that
  knows the work; the index's chain, `docs/conventions/README.md`,
  says which.

## Where to look

- The commit boundary and the `agent` scope:
  `docs/conventions/commit-messages/`.
- The records table the plan is walked against:
  `docs/conventions/project-recording/`.

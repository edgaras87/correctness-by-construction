# Commit plan

**How work larger than one commit is planned as commits, reviewed
as they land, and closed.**

## What it is for

So that a Change Set can be inspected commit
by commit before it lands, and a divergence at commit *k* forces the
remaining commits to be re-evaluated rather than continued on a
plan that no longer holds. Adopted with the Container Group
(ADR-0038, 1b). The failure it answered was lived in the handbook,
the repo this convention came from, now history (ADR-0038): a commit
sequence kept by hand in a scratch file across four sessions,
fitting no record. Lived here
since: every Change Set since 2026-08-27 has run under it. On
2026-09-27 and 28 one Change Set was revised four times at its
boundaries on the reviewer's readings, each revision on its own
commit. The failure it guards against, doing otherwise than the plan
and fixing it afterwards or not at all, has not happened here.

## What this is made usable as

- **`delivery/container/.claude/skills/commit-plan/SKILL.md` — the
  Agent Skill, shipped**, held at `.claude/skills/commit-plan/` and opened
  when work turns out to need several commits. The rules, one
  sentence each, with the decisions it rests on in its footer.
- **`.claude/skills/commit-plan/SKILL.md` — the Concept Deliverer's**,
  derived from this page like the Container Group's, neither copied from
  the other, and written for this Convention Seat (ADR-0042, ADR-0069).

This page explains; the Agent Skill states. What derives from this page
is that list. A change here runs the Change Walk on it; a change forced in one of
them is checked back against this page.

## The seats

A CBC Run and the Concept Deliverer each run their Change Sets under
the Agent Skill, the plan file at their own root.

## 1. What a commit plan is

The unit is the Change Set: the scope between one commit and a
whole project.

A patch series, carried into a repo where work is committed
directly instead of mailed. One logical change per commit, ordered
so each applies on the last. Reviewed commit by commit rather than
as a lump. What is added is the plan agreed before the series is
written, and its disposal afterwards. The plan is one file at the
repo root, `COMMIT-PLAN.md`, committed after it is agreed and
deleted at the close. Everything durable in it survives as the
commit messages it produced. The close commit's body is the cheapest
retrospective that exists.

Two ideas carry the rest. **Commits are split by change, not by
file**, and the test is revert: undo one commit and the repo must
still make sense. **Order follows where the decision lives.** A
decision settled in conversation is recorded first and implemented
second. A decision only visible in the material is found by
touching the material, and the durable record is written from what
held. The second kind makes the plan's last commits provisional, and the plan says so.

## 2. Why it is shaped this way

### 2.1 Not a record

It is temporary, not a record. Nothing about it is meant to be read a
year later except through `git log`. So it sits outside
the records (`knowledge/backbone-ideas/records.md` §3, *The records*), which are all
append-or-evolve (ADR-0038, 1b).

### 2.2 Root placement

An in-flight Change Set is visible from a
clean clone, so "is work half-landed, and where did it stop?" is
answerable without the working tree.

### 2.3 Status in the file

Tracking status there couples every work commit to a plan edit and reintroduces the staleness that
makes a neglected plan wrong. Git history is the status.

### 2.4 Material-first

Some decisions show only in the material: no conversation can
settle them before the work is touched. For them, the provisional commits, the revision commit and the Proposed-then-Accepted ADR are the
normal course, not a sign the plan failed (ADR-0038, 1e). *Its story: devlog 2026-09-27, afternoon; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.5 The records commits

The records table is walked while the commit list is drafted. A
Change Set gathers the moments its records name. A record's moment
can come mid-set, before the fact it records is true. Walking the Entry File's records
table while drafting is what catches it (ADR-0038, 1d).

### 2.6 What a plan counts

A plan counts commits, never Plan Steps. "Step" is `PLAN.md`'s word; a
plan that called its commits steps would give one word two meanings
(ADR-0049, 1). *Its story: devlog 2026-10-08; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.7 Inserted and repeated commits

A plan's numbers are cited, in its notes, its revisions and its
commit bodies, so a commit inserted later takes a letter rather
than renumbering the rest. Where one change reaches many records,
one planned commit repeats over them, naming its order and the
rule that stops it. *Its story: ADR-0050, 4 and 5.*

### 2.8 Counting subjects

A subject's characters are counted against the subject's 50-character
aim (`knowledge/backbone-ideas/commit-messages.md` §3, *The subject*)
when it is written. A plan writes every subject
before any lands. Counted only at each boundary, a long one lands
long, or is rewritten there with nothing in the plan saying why. *Its story: devlog 2026-10-08; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

A plan whose later commits are provisional gives them no subject yet.
Each is then written at its commit, and counted there, by script,
before it lands.
*Its story: devlog 2026-11-02, the refinement Plan Step's lessons.*

### 2.9 The agent's files

A commit that touches them is kept apart from everything else
(`knowledge/backbone-ideas/commit-messages.md` §4, *What shares a commit*), so
a records commit planned to carry an Agent Skill's correction has to be
split when it opens.
*Its story: devlog 2026-11-01, the last read's work, pass 1 and most of pass 2.*

`COMMIT-PLAN.md` is one of them. A plan opened or revised beside a
TODO line or an ADR is two commits: the plan's, then the record's.
*Its story: devlog 2026-11-02, the refinement Plan Step's lessons.*

### 2.10 The sweep

Before the close, the sweep looks again for every name the Change
Set moved, all at once. A commit that renames a file, renumbers or
retitles a section, or moves a fact greps for the old names in that
commit (`docs/conventions/facts-in-sync/` §3.3, *The rename grep*).
But a commit's own grep looks for the names it meant to move, and
misses the rest. The sweep reads the text unwrapped. A grep matches line by line, and a line of older text may be wrapped,
so a name broken across two lines is never found. *Its story: ADR-0049; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

### 2.11 Small commits

Small commits, on the reviewer's grant, are folded into the planned
commit before its boundary, so the reviewer still sees one commit
there. When each planned commit lands as one, there is no room to
try. Trying two ways meant reworking a commit in place. Small commits give the room.
The grant is the reviewer's because a small commit is still a
commit. The stop at every commit is commit messages' rule
(`knowledge/backbone-ideas/commit-messages.md` §5, *Commit on the word*). Without the grant, every
commit is a boundary. Each small commit is counted
when it is written, as a planned subject is. *Its story: ADR-0050.*

### 2.12 The look back

The Change Set is looked at whole, and regrouped on the reviewer's
word. Each boundary shows one commit; nothing showed the Change Set.
Looked at whole, two commits can turn out to be one change, or one
commit two changes. *Its story: ADR-0050, 3.*

### 2.13 The stop at every boundary

It is commit messages' rule, and this convention points at it
(`knowledge/backbone-ideas/commit-messages.md` §5, *Commit on the word*). *Its story: ADR-0038; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## Why it arrives this way

An Agent Skill, because the agent recognises its moment: work
turning out to need several commits. Nothing in a record would put
the plan in front of it then (`knowledge/backbone-ideas/how-an-agent-works.md` §3.2, *The Pulled Channel*). The one rule
that must fire at every commit, the stop, is not here: an Agent Skill that
opens only for multi-commit work cannot carry it, so it is
commit messages' (`knowledge/backbone-ideas/commit-messages.md` §5, *Commit on the word*).

## What this does not cover

- **The commit boundary itself, and the `agent` scope** —
  `knowledge/backbone-ideas/commit-messages.md`.
- **The records a plan is walked against, and what an ADR is** —
  `knowledge/backbone-ideas/records.md`.
- **The order of the work inside a plan** — the domain Agent Skill that
  knows the work; the order in the conventions' Local Map,
  `docs/conventions/README.md`, says which.

## Where to look

- The commit boundary and the `agent` scope:
  `knowledge/backbone-ideas/commit-messages.md`.
- The records table the plan is walked against:
  `knowledge/backbone-ideas/records.md` §12, *The Records Table*.

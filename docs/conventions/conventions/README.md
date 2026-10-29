---
foundation: the idea-to-output model
---

# Conventions

**How a way of working is written down once, in a manual, and made
into the Agent Rules and skills a project acts on.**

## What it is for

So that a way of working has one place that says why it is so, and
everything an agent acts on can be traced back to it. A rule can
then be questioned against its reason. A change to a reason reaches
every rule made from it.

What went wrong without it: the rules for conventions lived in the
conventions index, against that index's scope, and two of them
were rules nobody had followed (ADR-0039). The trigger: the
descriptions item filed on 2026-09-27, and the index read against
it the next day.

## What this is made usable as

Nothing shipped of its own; what a repo holds is:

- **the Foundation Line in every shipped skill, Agent Rule and Output Shape**
  — a CBC Run's, and this convention's artifact there (§1.3, *The Foundation Line*);
- **`.claude/rules/convention-manual.md` — the form of a manual,
  the Concept Deliverer's**, loading whenever a manual is opened;
- **the index, `docs/conventions/README.md`** — it points: the chain, relations only (ADR-0032), and one line sending a reader here and to the map
  (`ARCHITECTURE.md` §1.2, *The conventions…*).

What derives from this page is that list. A change here walks it;
a change forced in one of them is checked back against this page.

## The seats

A CBC Run holds artifacts and writes no manuals. The Concept
Deliverer writes the manuals and holds the Master Copy of every
artifact. This page is written from the Concept Deliverer's
Convention Seat.

## 1. A convention's artifacts

What a convention is, a manual and its artifacts, is the Idea Model's
(`docs/models/idea-to-output.md` §6, *A convention*). Here, a convention's artifacts
are what a project holds: a CBC Run, or this repo, which keeps its own
under `.claude/`. A skill file for a rule bound to a moment; an Agent
Rule for a rule bound to a path, or, with no path, to every task;
Record Stubs and templates for rules that ride in the files a project is
born with. The Master Copies are real files in the Container Group,
`delivery/container/`. Which copy of an artifact is the Master Copy, and
how every other copy changes, is the Exchange Convention's
(`docs/conventions/exchange/` §1, *What cannot change*, and §4, *The Delivery Take*). The Concept Deliverer's own skills
and Agent Rules are not copies: it writes its own
(`docs/conventions/agent-arrangement/` §3.1, *`.claude/skills/`*).

The reader is an agent in a project, holding a pinned copy and
opening it at the moment of use.

### 1.1 How a rule is written

- A rule is one sentence in the imperative. Its why is the manual's
  or the ADR's.
- Cite no decision mid-sentence. A skill or an Agent Rule lists the decisions
  it rests on once, in a footer headed *Decisions*: each as
  `CBC ADR-nnnn` in one that ships, `ADR-nnnn` in one that stays
  here, the Repo Tag being `project-recording`'s rule
  (`docs/conventions/project-recording/` §3.5, *Numbers across repos*), and a decision this
  repo inherited is adopted before a shipped file cites it
  (ADR-0038). A footer line names the section it
  backs, unless it backs the whole file. A Record Stub cites nothing.
- Say what a rule is not only when a consumer lived the misreading,
  and then name the CBC Run.
- A worked example in a code block is exempt from all of this.

### 1.2 A skill's frontmatter

A skill file opens with YAML frontmatter, which is what a skill
loader reads:

```yaml
---
name: <the convention's name, or with its act: exchange-read>
description: <when to read this file — the trigger>
foundation: the <name> convention
---
```

- `description` says when to read the file, never what the rule is.
- `name` equals the directory name.
- `foundation` is the next section's (§1.3, *The Foundation Line*).

### 1.3 The Foundation Line

`foundation` says what the whole file stands on *now* — a live
claim, never history — and a file has one
(`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 2).

Which files carry it, and where:

- every skill and Agent Rule, shipped or this repo's own, in its
  frontmatter;
- every shipped Output Shape, in frontmatter of its own;
- a manual whose idea an Idea Model states, in frontmatter of its own;
- a record whose header holds its form, such as the Plan Step
  Form or `TODO.md`'s item form, as a Foundation Line, `foundation:`, in that
  header's comment. Both Convention Seats, the CBC Run's Record Stubs included.

An Approach on Trial carries none: it is first-time work, and stands
on no Canonical Description until an evaluation places it
(`docs/models/idea-to-output.md` §4.2, *Up, work to an idea*).

What it holds:

- for the method, the concept and its version, `concept v1`;
- for the stack practice, the concept it was checked against,
  `practice, checked against concept v1`;
- for a convention's artifact, the convention by name, `the
  exchange convention`;
- for an Output Shape, the convention it lives under, `practice, under the
  shapes convention`;
- for a record's form, the convention it comes from, `the
  project-recording convention`;
- for a manual, the Idea Model that states its idea, by name, `the agent
  model`.

The value carries the relation where it is not derivation. Concept
chapters and Idea Models carry none; they are the top. That the line
travels with a copy is the Exchange Convention's
(`docs/conventions/exchange/` §3.5, *The Foundation Line in a copy*).

### 1.4 Skill Stages

A skill's phases are Skill Stages, numbered from Stage 0, each under its
own heading: `## Stage 1 — specify-correctness`. "Step" is PLAN's:
a Plan Step's Now line names the Skill Stage it is in, and one word for both
would read "Now: Step 3" inside Step 1. A numbered instruction
inside a Skill Stage is not a phase, and its list may call it a step.

*Its story: devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

## 2. The Convention Manual

A Convention Manual is `docs/conventions/<name>/README.md`,
written for a person and for the maintainer. It never ships
(`docs/conventions/exchange/` §3.2, *What goes*) and is never loaded into an
agent by default. When a CBC Run ignores a convention with no reason
and comes to no harm (`docs/models/idea-to-output.md` §6.2, *What a convention asserts*), its
manual records it. None has yet.

The manual is free prose: the convention stated, from which the
artifact is made usable (`ARCHITECTURE.md` §1, *What is stated here*). It explains and
points at the ADRs; the artifact says what a project does, and its
`foundation` line names the manual it derives from. How a manual
and what points at it or derives from it stay in agreement is
`docs/conventions/facts-in-sync/`.

**The form** is the sections a manual has, each a heading after
the opening, in the order of the parts below, from (§2.1, *The opening statement*)
to (§2.9, *Where to look*). It fixes where a reader
finds each section, not a manual's length, its tone, or how many
sections its body has. Whether a section is needed is each
manual's to decide. Whether the form becomes an Output Shape is the TODO
item "Decide whether our own forms become Output Shapes".

The form grows from what manuals already hold. The list is the
floor, and content that fits none of it takes its own heading in
the body. A section two manuals need becomes the next candidate:
a pair recurred, the test an Output Shape is written by
(`docs/conventions/shapes/` §1.2, *How an Output Shape is born*). The list grows no other way.

*Its story: ADR-0039.*

### 2.1 The opening statement

The manual's subject, in one sentence, so a reader can tell from
one line whether this is the page they need. Not a summary of how
it works, nor its boundary or its channel, which have sections of
their own.

*Its story: devlog 2026-10-19; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

### 2.2 What it is for

The need: the work it makes possible, the failure lived without
it, and the trigger, as evidence. Or as intent marked on trial,
with what would make it evidence and when to look again, after
which the need is rewritten from what was seen or the convention
goes. Or as adopted, taken whole from elsewhere: where it came
from, and what has been lived under it since. Never intent dressed
as evidence.

### 2.3 The list of derived artifacts

The list a change to the page walks: every derived artifact, by
path from the repo root, each marked shipped or the Concept Deliverer's,
with the moment it opens at, placed as the answer to the need. When
nothing ships, it says so, and lists what a repo holds. It ends
with the sentence that a change here walks that list.

### 2.4 The seats

A convention has two Convention Seats, the CBC Run's and the Concept
Deliverer's, and a manual names both: what each does under it, the CBC Run first — what
each holds is the list in *what this is made usable as*. One
paragraph when they are alike, a section per Convention Seat when they are
not, and "no Convention Seat" said outright when one side has none, so a
reader does not hunt for it. When the body is already written per
Convention Seat, the section is a paragraph naming which body sections are
whose, as `docs/conventions/exchange/` does. Placed after *what
this is made usable as*.

*Its story: ADR-0039.*

### 2.5 The body

Numbered sections, free prose. Each numbered section holds one
subject, and a subject has one section: other sections point at
it, and do not tell it again. The facts-in-sync manual asks the same of a convention's subject across the manuals
(`docs/conventions/facts-in-sync/` §2, *Point and derive*); this asks it inside
one. When a section gets a number, and its parts too, is that manual's
(`docs/conventions/facts-in-sync/` §3.2, *Numbering a section's parts*).

*Its story: devlog 2026-10-19; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

### 2.6 A lesson taken

A finding taken into a manual is written as what it teaches, not as
the case that taught it. The body states the lesson in general, in
the convention's own terms, as a new section or a change to one.
The case goes to the history that tells it, an ADR or a devlog
entry, and the manual keeps one italic line pointing there: "*Its
story: ADR-0059.*". A case told nowhere else is first written into
a devlog entry. Once the case has left, the section is read again:
where the lesson no longer reads clearly without it, it gains a
short plain example (ADR-0073). Another convention, or one
project's detail, may appear as an example. The statement never
stands on it, so it still holds when the example is gone.

*Its story: devlog 2026-10-18; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

### 2.7 Why it arrives this way

The channel, a skill, an Agent Rule, a Record Stub or a file, and why that one.
Where it reasons from the Agent Model, a Fact Reference to that
part (`docs/models/agent.md`).

### 2.8 What this does not cover

The boundary against its neighbours: a list, each neighbour's
subject in bold, then the path it belongs to.

### 2.9 Where to look

Optional: Fact References only, as root paths.

## 3. Adding a convention

A new convention can come from an Approach on Trial, ours or a
CBC Run's, when its evaluation places a piece as a convention of its
own (`.claude/approaches-on-trial/approach-evaluation.md`). The
placing takes these steps:

1. An ADR for the decisions behind it, opened Proposed when it lands
   inside a change set.
2. The manual at `docs/conventions/<name>/README.md`, in the form
   (§2, *The Convention Manual*).
3. Its artifacts in the Container Group, if it ships any. A convention
   entering or leaving the Container Group updates the birth entry in the
   Decisions Log's Record Stub there, in the same commit: a CBC Run holds
   that list, and cannot open this repo's.
4. The index's chain, only if the convention acts in sequence
   during a piece of work.
5. The convention's line in the map: a phrase and its manual's path
   (`ARCHITECTURE.md` §1.2, *The conventions…*).
6. What the Concept Deliverer holds of it, derived from the manual: for a
   skill, its own under `.claude/skills/`, in its own agent-scoped
   commit, with an entry in `.claude/decisions.md` when it changes
   how this repo's agent works. No registry entry: the Concept Deliverer
   receives no conventions (ADR-0042).

*Its story: devlog 2026-10-18; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

No CHANGELOG line and no Plan Step. The CHANGELOG logs the concept's
versions and has no place for a convention's entry (`CHANGELOG.md`'s
standing comment); the PLAN has no per-convention Plan Steps. *Its story: devlog 2026-09-28; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

## Why it arrives this way

The manual reaches no agent: a maintainer reads it. The form of a
manual is an Agent Rule, loading when a manual is read, so it is in view
while one is worked; a manual written new is written without it
(`docs/conventions/agent-arrangement/` §5.6, *Rules files*). The
Foundation Line rides in the frontmatter of every shipped skill
and Agent Rule, read by whoever opens the file, because a claim about
what a file stands on has to travel with the file.

## What this does not cover

- **Which copy is the Master Copy, how a copy changes, and what
  ships** — `docs/conventions/exchange/`.
- **How a fact keeps one home, and how what points at it or derives
  from it stays in agreement** — `docs/conventions/facts-in-sync/`.
- **The Repo Tag a citation carries, and the records a project keeps** —
  `docs/conventions/project-recording/`.
- **How an Agent Rule or a skill reaches an agent, and which paths are the
  arrangement's** — `docs/conventions/agent-arrangement/`.
- **What an Output Shape is and how one lives** — `docs/conventions/shapes/`.
  The form of a manual is an Agent Rule held here, not an Output Shape.
- **The concept's edges, its version and its changelog** —
  ADR-0003 and `CHANGELOG.md`'s standing comment.
- **A CBC Run's own Canonical Descriptions and what derives from them** — the
  CBC Run's, and not yet a rule of ours.

## Where to look

- The chain: `docs/conventions/README.md`.
- The rule for every description: `docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*.
- What `foundation` holds for each kind of file: §1.3, *The Foundation Line*, above; that
  it travels with a copy, `docs/conventions/exchange/` §3.5, *The Foundation Line in a copy*.
- A convention whose artifact is an Agent Rule, not a skill:
  `docs/conventions/shapes/`.

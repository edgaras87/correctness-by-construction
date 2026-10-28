---
foundation: the idea-to-output model
---

# Conventions

**How a way of working is written down once, in a manual, and made
into the rules and skills a project acts on.**

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

- **the `foundation` line in every shipped skill, rule and shape**
  — a run's, and this convention's artifact there (§1.3, *The `foundation` line*);
- **`.claude/rules/convention-manual.md` — the form of a manual,
  the deliverer's**, loading whenever a manual is opened;
- **the index, `docs/conventions/README.md`** — it points: the chain, relations only (ADR-0032), and one line sending a reader here and to the map
  (`ARCHITECTURE.md` §1.2, *The conventions…*).

What derives from this page is that list. A change here walks it;
a change forced in one of them is checked back against this page.

## The seats

A run holds artifacts and writes no manuals. The deliverer writes
the manuals and holds the master of every artifact. This page is
written from the deliverer's seat.

## 1. The artifact

What a convention is, a manual and its artifacts, is the model's
(`docs/models/idea-to-output.md` §6, *A convention*). Here, a convention's artifacts
are what a project holds: a run, or this repo, which keeps its own
under `.claude/`. A skill file for a rule bound to a moment; a rule
file for a rule bound to a path, or, with no path, to every task;
stubs and templates for rules that ride in the files a project is
born with. The masters are real files in the container,
`delivery/container/`. Which copy of an artifact is the master, and
how every other copy changes, is the exchange's
(`docs/conventions/exchange/` §1, *What cannot change*, and §4, *The take*). The deliverer's own skills
and rules are not copies: it writes its own
(`docs/conventions/agent-arrangement/` §3.1, *`skills/`*).

The reader is an agent in a project, holding a pinned copy and
opening it at the moment of use.

### 1.1 How a rule is written

- A rule is one sentence in the imperative. Its why is the manual's
  or the ADR's.
- Cite no decision mid-sentence. A skill or rule lists the decisions
  it rests on once, in a footer headed *Decisions*: each as
  `CBC ADR-nnnn` in one that ships, `ADR-nnnn` in one that stays
  here, the tag being project-recording's rule
  (`docs/conventions/project-recording/` §3.5, *A number is local to one repo*), and a decision this
  repo inherited is adopted before a shipped file cites it
  (ADR-0038). A footer line names the section it
  backs, unless it backs the whole file. A stub cites nothing.
- Say what a rule is not only when a consumer lived the misreading,
  and then name the run.
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
- `foundation` is the next section's (§1.3, *The `foundation` line*).

### 1.3 The `foundation` line

`foundation` says what the whole file stands on *now* — a live
claim, never history — and a file has one
(`docs/conventions/facts-in-sync/` §4, *The rule for every description*, step 2).

Which files carry it, and where:

- every skill and rule, shipped or this repo's own, in its
  frontmatter;
- every shipped shape, in frontmatter of its own;
- a manual whose idea a model states, in frontmatter of its own;
- a record whose header holds its form, such as `PLAN.md`'s step
  form or `TODO.md`'s item form, as a `foundation:` line in that
  header's comment. Both seats, the run's stubs included.

An approach on trial carries none: it is first-time work, and stands
on no description until an evaluation places it
(`docs/models/idea-to-output.md` §4.2, *Up, work to an idea*).

What it holds:

- for the method, the concept and its version, `concept v1`;
- for the stack practice, the concept it was checked against,
  `practice, checked against concept v1`;
- for a convention's artifact, the convention by name, `the
  exchange convention`;
- for a shape, the convention it lives under, `practice, under the
  shapes convention`;
- for a record's form, the convention it comes from, `the
  project-recording convention`;
- for a manual, the model that states its idea, by name, `the agent
  model`.

The value carries the relation where it is not derivation. Concept
chapters and models carry none; they are the top. That the line
travels with a copy is the exchange's
(`docs/conventions/exchange/` §3.5, *Every shipped skill, rule…*).

### 1.4 Stages

A skill's phases are stages, numbered from Stage 0, each under its
own heading: `## Stage 1 — specify-correctness`. "Step" is PLAN's:
a step's Now line names the stage it is in, and one word for both
would read "Now: Step 3" inside Step 1. A numbered instruction
inside a stage is not a phase, and its list may call it a step.

*Found 2026-10-15: `cbc-framing` called its phases steps, inside
PLAN's Step 1, and run 3 asked for a word of their own;
`infra-establish`'s walk did the same inside Step 3. Both say stage
since 2026-10-17, as the other skills did.*

## 2. The manual

A convention's manual is `docs/conventions/<name>/README.md`,
written for a person and for the maintainer. It never ships
(`docs/conventions/exchange/` §3.2, *What goes*) and is never loaded into an
agent by default. When a run ignores a convention with no reason
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
manual's to decide. Whether the form becomes a shape is the TODO
item "Decide whether our own forms become shapes".

The form grows from what manuals already hold. The list is the
floor, and content that fits none of it takes its own heading in
the body. A section two manuals need becomes the next candidate:
a pair recurred, the test a shape is written by
(`docs/conventions/shapes/` §1.2, *How one is born*). The list grows no other way.

*Found 2026-09-28, when the form was first written:
`docs/conventions/exchange/` and `docs/conventions/shapes/` had
grown the same sections with nothing telling either writer to. The
form was not designed; it was read off the two (ADR-0039).*

### 2.1 The opening statement

The manual's subject, in one sentence, so a reader can tell from
one line whether this is the page they need. Not a summary of how
it works, nor its boundary or its channel, which have sections of
their own.

*Found 2026-10-19: of the fourteen manuals' opening statements,
five said the subject in one sentence, five added claims that have
other homes, and four summed up how the work goes. "What the
convention is" allowed all three. The conventions manual's own
said what a convention claims, not its subject.*

### 2.2 What it is for

The need: the work it makes possible, the failure lived without
it, and the trigger, as evidence. Or as intent marked on trial,
with what would make it evidence and when to look again, after
which the need is rewritten from what was seen or the convention
goes. Or as adopted, taken whole from elsewhere: where it came
from, and what has been lived under it since. Never intent dressed
as evidence.

### 2.3 What this is made usable as

The list a change to the page walks: every derived artifact, by
path from the repo root, each marked shipped or the deliverer's,
with the moment it opens at, placed as the answer to the need. When
nothing ships, it says so, and lists what a repo holds. It ends
with the sentence that a change here walks that list.

### 2.4 The seats

A convention has two seats, the run's and the deliverer's, and a
manual names both: what each does under it, the run first — what
each holds is the list in *what this is made usable as*. One
paragraph when they are alike, a section per seat when they are
not, and "no seat" said outright when one side has none, so a
reader does not hunt for it. When the body is already written per
seat, the section is a paragraph naming which body sections are
whose, as `docs/conventions/exchange/` does. Placed after *what
this is made usable as*.

*Found 2026-09-28: twice a manual had grown seat sections because
the two sides do different things, and nothing told the writer of
the next one to ask. Six manuals had never said. Every manual
gained the section, so the asking is built in (ADR-0039,
decision 3).*

### 2.5 The body

Numbered sections, free prose. Each numbered section holds one
subject, and a subject has one section: other sections point at
it, and do not tell it again. Facts-in-sync asks the same of a convention's subject across the manuals
(`docs/conventions/facts-in-sync/` §2, *Point and derive*); this asks it inside
one. When a section gets a number, and its parts too, is facts-in-sync's
(`docs/conventions/facts-in-sync/` §3.2, *A section's parts are numbered*).

*Found 2026-10-19: in this manual, §3 held two subjects, how a
manual is written and how everything stays in step. Nothing said a
section holds one subject, so a walk through the manual had no
rule to name.*

### 2.6 A lesson taken

A finding taken into a manual is written as what it teaches, not as
the case that taught it. The body states the lesson in general, in
the convention's own terms, as a new section or a change to one.
The case goes beside it as a dated italic: what happened, when, and
what changed. Another convention, or one project's detail, may
appear as an example. The statement never stands on it, so it still
holds when the example is gone.

*Learned 2026-10-18, at `docs/conventions/agent-arrangement/` §3.7, `CLAUDE.local.md`.
Its first draft said what `CLAUDE.local.md` holds through
`commit-plan`'s grant of small commits. The reviewer asked for it
without that dependency and beyond commits. It became a test any
line can be sorted by, with the commit grant as one example.*

### 2.7 Why it arrives this way

The channel, a skill, a rule, a stub or a file, and why that one.
Where it reasons from the agent model, a fact reference to that
part (`docs/models/agent.md`).

### 2.8 What this does not cover

The boundary against its neighbours: a list, each neighbour's
subject in bold, then the path it belongs to.

### 2.9 Where to look

Optional: fact references only, as root paths.

## 3. Adding a convention

A new convention can come from an approach on trial, ours or a
run's, when its evaluation places a piece as a convention of its
own (`.claude/approaches-on-trial/approach-evaluation.md`). The
placing takes these steps:

1. An ADR for the decisions behind it, opened Proposed when it lands
   inside a change set.
2. The manual at `docs/conventions/<name>/README.md`, in the form
   (§2, *The manual*).
3. Its artifacts in the container, if it ships any. A convention
   entering or leaving the container updates the birth entry in the
   container's decisions-log stub, in the same commit: a run holds
   that list, and cannot open this repo's.
4. The index's chain, only if the convention acts in sequence
   during a piece of work.
5. The convention's line in the map: a phrase and its manual's path
   (`ARCHITECTURE.md` §1.2, *The conventions…*).
6. What the deliverer holds of it, derived from the manual: for a
   skill, its own under `.claude/skills/`, in its own agent-scoped
   commit, with an entry in `.claude/decisions.md` when it changes
   how this repo's agent works. No registry entry: the deliverer
   receives no conventions (ADR-0042).

*Written 2026-09-28 from how the last three conventions had been
added, not from what the index said. By 2026-10-18 seven had come
this way: `visual-comparison`, the exchange, shapes, this one,
writing, the retrospective and first-time work.*

No CHANGELOG line and no PLAN step. The CHANGELOG logs the concept's
versions and has no place for a convention's entry (`CHANGELOG.md`'s
standing comment); the PLAN has no per-convention steps. *The
index asked for both until 2026-09-28, and the last seven
conventions took neither — a rule kept where nobody reads it
(ADR-0039).*

## Why it arrives this way

The manual reaches no agent: a maintainer reads it. The form of a
manual is a rule, loading when a manual is read, so it is in view
while one is worked; a manual written new is written without it
(`docs/conventions/agent-arrangement/` §5.6, *Rules files*). The
`foundation` line rides in the frontmatter of every shipped skill
and rule, read by whoever opens the file, because a claim about
what a file stands on has to travel with the file.

## What this does not cover

- **Which copy is the master, how a copy changes, and what
  ships** — `docs/conventions/exchange/`.
- **How a fact keeps one home, and how what points at it or derives
  from it stays in agreement** — `docs/conventions/facts-in-sync/`.
- **The tag a citation carries, and the records a project keeps** —
  `docs/conventions/project-recording/`.
- **How a rule or a skill reaches an agent, and which paths are the
  arrangement's** — `docs/conventions/agent-arrangement/`.
- **What a shape is and how one lives** — `docs/conventions/shapes/`.
  The form of a manual is a rule held here, not a shape.
- **The concept's edges, its version and its changelog** —
  ADR-0003 and `CHANGELOG.md`'s standing comment.
- **A run's own descriptions and what derives from them** — the
  run's, and not yet a rule of ours.

## Where to look

- The chain: `docs/conventions/README.md`.
- The rule for every description: `docs/conventions/facts-in-sync/` §4, *The rule for every description*.
- What `foundation` holds for each kind of file: §1.3, *The `foundation` line*, above; that
  it travels with a copy, `docs/conventions/exchange/` §3.5, *Every shipped skill, rule…*.
- A convention whose artifact is a rule, not a skill:
  `docs/conventions/shapes/`.

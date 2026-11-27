---
foundation: the idea-to-output model
---

# Conventions

**How a way of working is written down once, in a manual, and made
into the Agent Rules and Agent Skills a project acts on.**

## What it is for

So that a way of working has one place that says why it is so, and
everything an agent acts on can be traced back to it. A rule can
then be questioned against its reason. A change to a reason reaches
every rule made from it.

What went wrong without it: the rules for conventions lived in the
conventions index, against that index's scope, and two of them
were rules nobody had followed (ADR-0039). The trigger: a TODO
item, filed on 2026-09-27, that asked for a description of each
convention, and the index read against it the next day (devlog
2026-09-28).

## What this is made usable as

Nothing shipped of its own; what a repo holds is:

- **the Foundation Line in every shipped Agent Skill, Agent Rule and Output Shape**, but those §1.3 exempts
  — held in a CBC Run, where it is this convention's one Work Approach, read whenever its file is opened (§1.3, *The Foundation Line*);
- **`.claude/rules/convention-manual.md` — the form of a manual,
  the Concept Deliverer's**, loading whenever a manual is opened;
- **the index, `docs/conventions/README.md` — the Concept Deliverer's**,
  opened when a reader looks for the order the conventions act in
  during a piece of work. It holds that order, relations only
  (ADR-0032). One line sends a reader here, and to `ARCHITECTURE.md`
  for which conventions there are (`ARCHITECTURE.md` §1.2, *The conventions*).

What derives from this page is that list. A change here runs the Change Walk on it;
a change forced in one of them is checked back against this page.

## The seats

A CBC Run holds Work Approaches and writes no manuals. The Concept
Deliverer writes the manuals and holds the Master Copy of every
shipped Work Approach. This page is written from the Concept Deliverer's
Convention Seat.

## 1. A convention's Work Approaches

What a convention is, its manual, with its Work Approaches one level down, is the Idea-to-Output Model's
(`docs/models/idea-to-output.md` §6, *A convention*). Here, a convention's Work Approaches
are what a project holds: a CBC Run, or this repo, which keeps its own
under `.claude/`. A convention's Work Approach is one of three
(`docs/models/idea-to-output.md` §2, *The kinds*):

- an Agent Skill, for a rule bound to a moment;
- an Agent Rule, for a rule bound to a path, or, with no path, to
  every task;
- an Output Form, a record's form in its header comment, for rules
  that sit in the files a project is born with. It ships in a Record
  Stub.

An Agent Skill Template is part of its Agent Skill, not a Work
Approach of its own.

The Master Copies are real files in the Container Group,
`delivery/container/`. Which copy of a Work Approach is the Master Copy, and
how every other copy changes, is the Exchange Convention's
(`docs/conventions/exchange/` §1, *What cannot change*, and §4, *The Delivery Take*). The Concept Deliverer's own Agent Skills
and Agent Rules are not copies: it writes its own
(`knowledge/backbone-ideas/agent-files.md` §7, *Agent Skills and Agent Rules*).

A Work Approach's reader is an agent in a project, opening it at the
moment of use. In a CBC Run, that agent holds a pinned copy.

### 1.1 How a rule is written

- A rule is one sentence in the imperative. Its why is the manual's
  or the ADR's.
- A decision is cited as one home says for every text, in both
  Convention Seats: in a Work Approach, once, in its *Decisions*
  footer (`knowledge/backbone-ideas/one-home.md` §6, *Where a decision is cited*).
- Say what a rule is not only when a consumer lived the misreading,
  and then name the CBC Run.
- A worked example in a code block is exempt from all of this.

### 1.2 An Agent Skill's frontmatter

An Agent Skill's `SKILL.md` opens with YAML frontmatter, which is
what the tool reads to load it:

```yaml
---
name: <its act, a verb, never a name already used: exchange-read>
description: <when to read this file — the trigger>
foundation: <what the file stands on, as §1.3 gives it>
---
```

- `description` says when to read the file, never what the rule is.
- `name` equals the directory name.
- `foundation` is the next section's (§1.3, *The Foundation Line*).

### 1.3 The Foundation Line

`foundation` says what the whole file stands on *now*. It is a live
claim, never history. A file has one
(`knowledge/backbone-ideas/one-home.md` §7, *What stands on a text*).

Which files carry it, and where:

- every Agent Skill and Agent Rule, shipped or this repo's own, in its
  frontmatter;
- every shipped Output Shape, in frontmatter of its own;
- a manual whose idea an Idea Model states, in frontmatter of its own;
- a record whose header holds its form, such as the Plan Step
  Form or `TODO.md`'s item form: a `foundation:` line in that
  header's comment, in both Convention Seats, the CBC Run's Record Stubs included.

An Approach on Trial carries none: it is first-time work, and stands
on no Canonical Description until an evaluation places it
(`docs/models/idea-to-output.md` §3.1, *The four Chain Links*).

An Agent Skill or Agent Rule whose understanding is written beside it, in `.claude/understanding/` or in the Backend Kit's Adapted Case under `knowledge/adapted-cases/`, carries none either. It stands on that text, and that text on one under `knowledge/`, which no value above names. That text's header says what it stands on, and what stands on it. It carries one when the rewrite of today's texts into `knowledge/` brings the Foundation Line there.

What it holds:

- for the method, the concept and its version, `concept v1`;
- for the Stack Group's Agent Skills, the concept they were checked against,
  `practice, checked against concept v1`;
- for a convention's Work Approach, the convention by name, `the
  exchange convention`;
- for an Output Shape, the convention it lives under, `practice, under the
  shapes convention`;
- for a record's form, the convention it comes from, `the
  writing convention`;
- for a manual, the Idea Model that states its idea, by name, `the tiers
  model`.

Where a file is not derived from what it names, the value says how
the two relate: `checked against`, `under`. Concept
chapters and Idea Models carry none; they are the top. That the line
travels with a copy is the Exchange Convention's
(`docs/conventions/exchange/` §3.5, *The Foundation Line in a copy*).

### 1.4 Agent Skill Stages

An Agent Skill's phases are Agent Skill Stages, each under its own
heading, the words after the dash in lowercase:
`## Stage 1 — specify-correctness`. They are numbered from Stage 0 when the first
opens the work or checks that it can start, and from Stage 1 when the
first is the work itself. "Step" is PLAN's:
a Plan Step's Now line names the Agent Skill Stage it is in, and one word for both
would read "Now: Step 3" inside Step 1. A numbered instruction
inside an Agent Skill Stage is not a phase, and its list may call it a step.

*Its story: devlog 2026-10-17, later; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

### 1.5 Naming a Work Approach

A new name never repeats a manual's, an Agent Skill's or an Agent
Rule's: a grep for it, before it is given, finds none. A shared name
makes every grep for one find both. A new Agent Skill is named by
its act, a verb: exchange-read, infra-establish.

In text, a Work Approach is always written with its kind: the
commit-plan Agent Skill, the one-home Agent Rule. A manual is written
the same way, the commit-plan manual. A sentence that points at where a fact is written gives the path, as a
Fact Reference (`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §2, *Writing a Fact Reference*).

Four names older than this part are shared: commit-plan,
visual-comparison and retrospective, each a manual and an Agent
Skill; writing, a manual and an Agent Rule. The kind keeps
them apart in text (ADR-0078).

## 2. The Convention Manual

A Convention Manual is `docs/conventions/<name>/README.md`,
written for a person and for the maintainer. It never ships
(`docs/conventions/exchange/` §3.2, *What goes*) and is never loaded into an
agent by default. When a CBC Run ignores a convention with no reason
and comes to no harm (`docs/models/idea-to-output.md` §6.2, *What a convention asserts*), its
manual records it. None has yet.

The manual is free prose: the convention stated, from which its Work
Approaches are made usable (`docs/models/idea-to-output.md` §6.1, *The manual's level*). It explains and
points at the ADRs. A Work Approach says what a project does, and its
`foundation` line names the manual it derives from. How a manual
and what points at it or derives from it stay in agreement is
one home's, `knowledge/backbone-ideas/one-home.md`.

**The form** is the sections a manual has, each a heading after the
opening, but for §2.6, a rule for the body. They come in the order of §2.1 to §2.9 below. It fixes where a reader
finds each section, not a manual's length, its tone, or how many
sections its body has. Whether a section is needed is each
manual's to decide. Whether the form becomes an Output Shape is held
on the rewrite's map (`temp/rewrite-map.md` §8, *Items from TODO*).

The form grows from what manuals already hold. The list is the
least a manual has, and content that fits none of it takes its own
heading in the body. A section that two manuals need becomes a
candidate for the list. It is the same test by which an Output Shape
is written: a pair of outputs that recur
(`docs/conventions/shapes/` §1.2, *How an Output Shape is born*). The list grows no other way.

*Its story: ADR-0039.*

### 2.1 The opening statement

The manual's subject, in one sentence, so a reader can tell from
one line whether this is the page they need. Not a summary of how
it works, nor its boundary or its channel, which have sections of
their own.

*Its story: devlog 2026-10-19; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

### 2.2 The need

*What it is for* says the need: the work it makes possible, the
failure lived without it, and the trigger. It is stated as one of
three:

- evidence;
- intent marked on trial, saying what would make it evidence and when
  to look again. Then the need is rewritten from what was seen, or the
  convention goes;
- adopted, taken whole from elsewhere: where it came from, and what
  has been lived under it since.

Never a wish written as evidence.

### 2.3 The list of what derives

*What this is made usable as* is the list the Change Walk runs on when
the page changes, placed as the answer to the need. Each entry has:

1. its path from the repo root;
2. its mark, shipped or the Concept Deliverer's;
3. the moment it opens at.

When nothing ships, it says so, and lists what a repo holds. It ends
with the sentence that a change here runs the Change Walk on that
list.

### 2.4 The seats

A convention has two Convention Seats, the CBC Run's and the Concept
Deliverer's. The manual says what each does under it, the CBC Run
first. What each holds is the list in *What this is made usable
as*. It takes one of four forms:

- one paragraph, when they are alike;
- a section per Convention Seat, when they are not;
- "no Convention Seat" said outright, when one side has none, so a
  reader does not hunt for it;
- a paragraph naming which body sections are whose, when the body is
  already written per Convention Seat, as `docs/conventions/exchange/`
  does.

It is placed after *What this is made usable as*.

*Its story: ADR-0039.*

### 2.5 The body

Numbered sections, free prose. Each numbered section holds one
subject, and a subject has one section: other sections point at
it, and do not tell it again. One home asks the same of a fact across texts
(`knowledge/backbone-ideas/one-home.md` §4, *Pointing at a home*); this asks it inside
one. When a section gets a number, and its parts too, is one home's, in keeping knowledge
(`knowledge/problem-domain-ideas/keeping-knowledge/one-home-in-keeping-knowledge.md` §3, *Numbering a section's parts*).

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

### 2.7 The channel

*Why it arrives this way* names the channel, an Agent Skill, an Agent
Rule, a Record Stub or a file, and why that one.
Where it reasons from how an agent works, it carries a Fact Reference to
the part it rests on, such as (`knowledge/backbone-ideas/how-an-agent-works.md` §7, *Choosing a channel*).

### 2.8 The boundary

*What this does not cover* is the boundary against its neighbours: a list, each neighbour's
subject in bold, then the path it belongs to.

### 2.9 Where to look

Optional: Fact References only, as root paths.

## 3. Adding a convention

A new convention can come from an Approach on Trial, ours or a
CBC Run's, when its evaluation, by the approach-evaluation Approach
on Trial, places a piece as a convention of its own
(`knowledge/backbone-ideas/change.md` §4, *The arrows*). The
placing takes these steps:

1. An ADR for the decisions behind it, opened Proposed when it lands
   inside a Change Set.
2. The manual at `docs/conventions/<name>/README.md`, in the form
   (§2, *The Convention Manual*).
3. Its Work Approaches in the Container Group, if it ships any. A Work Approach
   entering or leaving the Container Group updates the birth entry in the
   Decisions Log's Record Stub there, in the same commit: a CBC Run holds
   that list, and cannot open this repo's (`knowledge/backbone-ideas/agent-files.md` §8, *The Decisions Log*).
4. Its place in the index's order of the conventions, only if the
   convention acts in sequence during a piece of work.
5. The convention's line in `ARCHITECTURE.md`: a phrase and its
   manual's path (`ARCHITECTURE.md` §1.2, *The conventions*).
6. What the Concept Deliverer holds of it, derived from the manual: for an
   Agent Skill, its own under `.claude/skills/`. That Agent Skill lands
   in its own agent-scoped commit, with an entry in
   `.claude/decisions.md` when it changes how this repo's agent works.
   A CBC Run's Decisions Log lists, in its birth entry, the
   Work Approaches it received. The Concept Deliverer's lists none,
   since it receives none (`knowledge/problem-domain-ideas/keeping-knowledge/agent-files-in-keeping-knowledge.md` §4, *The Decisions Log*; ADR-0042).

*Its story: devlog 2026-10-18; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

No CHANGELOG line and no Plan Step. The CHANGELOG logs the concept's
versions, and has no place for a convention's entry (`CHANGELOG.md`'s
header comment). The PLAN has no Plan Step per convention.

*Its story: devlog 2026-09-28; devlog 2026-10-29, the lessons' own stories: conventions and facts-in-sync.*

## Why it arrives this way

The manual reaches no agent: a maintainer reads it. The form of a
manual is an Agent Rule. It loads when a manual is read, so it is in
view while one is worked. A manual written new is written without it
(`knowledge/adapted-cases/cbc-backend-design/keeping-knowledge/claude-code-tool-binding/understanding.md` §6, *Paths Rules*). The
Foundation Line sits in every file §1.3 names, in its frontmatter or
its header comment, read by whoever opens the file, because a claim about
what a file stands on has to travel with the file.

## What this does not cover

- **Which copy is the Master Copy, how a copy changes, and what
  ships** — `docs/conventions/exchange/`.
- **How a fact keeps one home, and how what points at it or derives
  from it stays in agreement** — `knowledge/backbone-ideas/one-home.md`.
- **The Repo Tag a citation carries, and the records a project keeps** —
  `knowledge/backbone-ideas/records.md`.
- **How an Agent Rule or an Agent Skill reaches an agent, and which files
  are the agent's** — `knowledge/backbone-ideas/agent-files.md`.
- **What an Output Shape is and how one lives** — `docs/conventions/shapes/`.
  The form of a manual is an Agent Rule held here, not an Output Shape.
- **The concept's edges, its version and its changelog** —
  ADR-0003 and `CHANGELOG.md`'s header comment.
- **A CBC Run's own Canonical Descriptions and what derives from them** — the
  CBC Run's, and not yet a rule of ours.

## Where to look

- The order the conventions act in: `docs/conventions/README.md`.
- The rule for every description: `knowledge/backbone-ideas/one-home.md` §7, *What stands on a text*.
- What `foundation` holds for each kind of file: `docs/conventions/conventions/` §1.3, *The Foundation Line*.
- That it travels with a copy: `docs/conventions/exchange/` §3.5, *The Foundation Line in a copy*.
- A convention whose Work Approach is an Agent Rule, not an Agent Skill:
  `docs/conventions/shapes/`.

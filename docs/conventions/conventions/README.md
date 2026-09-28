# Conventions

**A convention is a rule the work may break only with a reason —
stated once, in a manual that never ships, and made usable as
artifacts a project holds.**

## What it is for

A convention is written when something made
usable is needed, and the need is written down first: what work
it makes possible, what went wrong without it, and the event that
made it — as evidence, with the run or the date; or as intent,
marked *on trial* with what would make it evidence and when to
look again, after which the need is rewritten from what was seen
or the convention goes. What went wrong without this one: the rules for
conventions lived in the index, against its scope, and two of them
were dead letters nobody had followed (CBC ADR-0039). The trigger:
the descriptions item filed on 2026-09-27, and the index read
against it the next day.

## What this is made usable as

Nothing shipped of its own; what a repo holds is:

- **the `foundation` line in every shipped file** — a run's, and
  this convention's artifact there (§2);
- **`.claude/rules/convention-manual.md` — the shape of a manual,
  the deliverer's**, loading whenever a manual is opened;
- **the index, `docs/conventions/README.md`** — a pointer: the
  table and the chain, relations only (CBC ADR-0032), and one line
  sending a reader to `docs/conventions/conventions/`.

What derives from this page is that list. A change here walks it;
a change forced in one of them is checked back against this page.

## The seats

A run holds artifacts and writes no manuals. The deliverer writes
the manuals and holds the master of every artifact. This page is
written from the deliverer's seat.

## 1. What a convention is

Each one is two things, kept apart — and from everywhere else,
only pointers (§3):

- **A manual**, `docs/conventions/<name>/README.md`. What this is,
  how it works, why, with pointers to the decisions. Written for a
  person and for the maintainer. Never shipped, never loaded into an
  agent by default.
- **Its artifacts**: what a project actually holds — a run, or this
  repo, whose own `.claude/` holds seven. A skill file for
  a rule bound to a moment; a rule file for a rule bound to a path;
  stubs and templates for rules that ride in the files a project is
  born with. The rules live there, one sentence each. The artifacts
  are real files in the container, `delivery/container/`.

Which copy of an artifact is the master, and how every other copy
changes — this repo's own `.claude/skills/` included — is the
exchange's, `docs/conventions/exchange/` §1 and §4.

**What a convention asserts**, and what falsifies it (CBC
ADR-0031): that this is a rule and not a method — *the work may
ignore this, with a reason it can give*. That freedom is the
worker's, in one case, with the reason where that repo's records
live; an artifact derived from the manual says what the manual
says, and a pointer says nothing of its own (§3). A run that
ignores a convention, gives no reason and comes to no harm has
found one nobody owes anything to, which is a method filed in the
wrong place. The manual is where that is recorded when it happens;
none has failed the test yet.

## 2. The artifact

The reader is an agent in a project, holding a pinned copy and
opening it at the moment of use.

- A rule is one sentence in the imperative. Its why is the manual's
  or the ADR's.
- Cite no decision mid-sentence. A skill lists the decisions it
  rests on once, in a footer headed *Decisions*, each as
  `CBC ADR-nnnn` — the tag is project-recording's rule,
  `docs/conventions/project-recording/` §3, and a decision this
  repo inherited is adopted before a shipped file cites it (CBC
  ADR-0038). A stub cites nothing.
- Say what a rule is not only when a consumer lived the misreading,
  and then name the run.
- A worked example in a code block is exempt from all of this.

**A skill file** opens with YAML frontmatter, which is what a skill
loader reads:

```yaml
---
name: <the convention's name>
description: <when to read this file — the trigger>
requires: <conventions this one delegates to; omit if none>
foundation: the <name> convention
---
```

- `description` says when to read the file, never what the rule is.
- `name` equals the directory name; registry entries and `requires`
  lines refer to the convention by it.
- `requires` names the conventions this one delegates rules to; a
  receiver lands a convention together with its chain.
- `foundation` says what the file stands on *now* — a live claim,
  never history. Every derived file carries one, shipped or this
  repo's own: for the method, the concept and its version,
  `concept v1`; for the stack practice, the concept it was checked
  against, `practice, checked against concept v1`; for a
  convention's artifact, the convention by name, `the exchange
  convention`. The value carries the relation where it is not
  derivation. Concept chapters carry none; they are the top. That
  the line travels with a copy is `docs/conventions/exchange/` §3.

## 3. The manual

The manual is free prose: the convention stated, from which the
artifact is made usable (`docs/master.md` §1). It explains and
points at the ADRs; the artifact says what a project does, and its
`foundation` line names the manual it derives from.

**One place.** A convention's subject is stated in its manual and
nowhere else. Text that touches the subject points at the manual
and does not restate it: another manual, the index, the master, an
ADR's context, an entry file. Text that makes the subject usable
derives from the manual and names it in `foundation`. Two
relations, two verbs — point and derive — and a reader who finds
the subject stated twice has found a defect. Measured once: 98
lines, two files, three disagreeing copies of one rule.

**A pointer is a path.** Text that points names the manual by its
directory with the slash, `<name>/` — as a path from the repo root,
`docs/conventions/<name>/`, or as a relative link between manuals,
which resolves and carries the same token — so that the manual can
find everything pointing at it with one grep. A pointer that leaves
a convention's directory is written from the repo root, because a
relative path means a different thing the moment a file is read
from a different root, which is every copy and every shipped file.
A name in prose is not a pointer, because names are words. A rename
is the case `docs/conventions/commit-plan/` §4's sweep covers:
every old path, before the close.

**Its shape** is a rule under `.claude/rules/`, loading when a
manual is opened (how a rule loads is
`docs/conventions/agent-arrangement/` §3), and lists the sections
one has, each a heading after the opening: an opening statement;
*what it is for* — the
need, the failure lived without it, and the trigger, as evidence
or as intent marked on trial, never intent dressed as evidence;
*what this is made usable as* — the list a change to the page
walks, each item marked shipped or the deliverer's, with the
moment it opens at, placed as the answer to the need; the seats,
what each side does; lessons as dated italics; and *what this
does not cover*, the boundary against its neighbours by path. The
shape was not designed. `docs/conventions/exchange/` and
`docs/conventions/shapes/` grew
the same six sections with nothing telling either writer to, which
is a shape by the test in `docs/conventions/shapes/` §2: a pair
recurred. It grows the same way and no other: the list is the
floor, and content that fits none of it takes its own heading in
the body, where a section two manuals need becomes the next
candidate.

**The seats.** A convention has two seats, the run's and the
deliverer's, and a manual names both: what each holds and does
under it, the run first. One paragraph when they are alike, a
section per seat when they are not, and "no seat" said outright
when one side has none, so a reader does not hunt for it. Placed
after *what ships*. Twice a manual grew seat sections because the
two sides do different things, and nothing told the writer of the
next one to ask; the paragraph is where the asking is now built
in.

**One rule for every description**, this page included. A
description is how we understand a thing today, written down: the
concept, each manual, the master. It may be wrong or incomplete,
and it is canonical regardless — everything derived from it agrees
with it until it changes, and it changes only for a reason
recorded, practice being the evidence. What derives from it is not
a description: it applies, it does not explain. The rule is the
same for all of them, and this is where it is stated:

1. A description lists what derives from it.
2. Each derived thing names its description — in a shipped file,
   the `foundation` line.
3. A change to the description walks the list in the same commit,
   and greps for the description's path to find what points at it.
4. A change forced in a derived thing is checked back against the
   description.
5. A disagreement is raised and decided, practice the evidence; if
   the description changes, the walk runs again.

Steps 1, 2 and the grep in 3 are checkable today: every shipped
file carries `foundation`, `docs/conventions/exchange/` and
`docs/conventions/shapes/` close with their lists, and a path is a
token. The rest ran twice by hand
before this was a rule — the correspondence check of 2026-09-25,
and the walk of `docs/master.md` at the exchange plan's close —
both because the reviewer asked, not because anything made anyone
look. Where a manual and the concept are handled differently —
versioning, shipping, the kind of derivative, the seats, what each
asserts — is CBC ADR-0039; the concept's edges are CBC ADR-0003,
the CHANGELOG's standing comment and `docs/master.md` §1.1.

## 4. Adding a convention

As the last three were added — `visual-comparison`, the exchange,
shapes — and not as the index once said:

1. An ADR for the decisions behind it, opened Proposed when it lands
   inside a change set.
2. The manual at `docs/conventions/<name>/README.md`, in the shape.
3. Its artifacts in the container, if it ships any. A convention
   entering or leaving the container updates the index's table, the
   shipped-conventions table in `delivery/README.md`, and the birth
   entry in the container's decisions-log stub, in the same commit.
4. A row in the index's table.
5. A registry entry in `.claude/decisions.md`, *Convention held:
   \<name\>*, saying what this repo holds of it — and for a skill,
   this repo's own copy under `.claude/skills/`, in its own
   agent-scoped commit.

No CHANGELOG line and no PLAN step. The CHANGELOG is the
concept-version log (CBC ADR-0003) and has no place for a
convention's entry; the PLAN has no per-convention steps. *The
index asked for both until 2026-09-28, and the last three
conventions took neither — a rule kept where nobody reads it (CBC
ADR-0039).*

## What this does not cover

- **Which copy is the master, how a copy changes, and what
  ships** — `docs/conventions/exchange/`.
- **The tag a citation carries, and the records a project keeps** —
  `docs/conventions/project-recording/`.
- **How a rule or a skill reaches an agent, and which paths are the
  arrangement's** — `docs/conventions/agent-arrangement/`.
- **What a shape is and how one lives** — `docs/conventions/shapes/`.
  The shape of a manual is one instance of it, held here.
- **The concept's edges, its version and its changelog** — CBC
  ADR-0003 and `docs/master.md` §1.1.
- **A run's own descriptions and what derives from them** — the
  run's, and not yet a rule of ours.

## Where to look

- The index and the chain: [`../README.md`](../README.md).
- The rule for every description: `docs/master.md` §3.
- What `foundation` holds for each kind of file: the exchange,
  [`../exchange/`](../exchange/) §3.
- A convention whose artifact is a rule, not a skill:
  [`../shapes/`](../shapes/).

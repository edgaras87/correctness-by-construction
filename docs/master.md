<!-- Placed here 2026-09-25, loose under docs/ on purpose: not in
     models/ or conventions/, because either would argue for what
     this should say. A section that outgrows this file becomes its
     own document and leaves a paragraph behind.

     The name: everything here is a master, and everywhere else
     holds copies.

     Written under one rule: state only what is checkable in this
     repo and in the live run, and mark anything merely intended as
     intended. Where we contradict ourselves, say so rather than
     pick a side — the list at the end is where that goes. -->

# Master

**One concept, the delivery a project is born from, and the agent
that keeps both true.**

Nothing is built here. No application, no service, no run — this
repo holds documents and hands them to projects that do build.

## What this is

A picture of what is tied to what in this repo, so that changing
one part shows what else moves.

It is only useful while it is current: a map wrong about what
connects to what is worse than none, because it is believed. What
it already knows is wrong is listed at the end.

## How to read it

Three movements. **The material** — what is stated here (1) and
what ships from it (2), paired row by row. **The motion** — how any
of it changes, and the rule for when a run disagrees with what we
wrote (3). **The actor** — the work arrangement, which the agent
here is made of and which the container ships a second copy of
(4).

At the end: what must stay true, the words, and what this page
knows is wrong.

---

## 1. What is stated here

Two bodies of writing, neither of which ships. Each has something
in the delivery that is it *made usable*, and the pairing is the
spine of this repo:

| stated | made usable |
|---|---|
| the concept (1.1) | the method (2.1) |
| the conventions (1.2) | the container (2.3) |

### 1.1 The concept — `concept/`

**Five chapters in plain words: correctness is built into the
structure of a thing rather than tested in afterwards.**

This is the repo's purpose. Everything else exists because of it,
and is either derived from it or checked against it.

- **Authoritative here.** This is where the concept is true. Every
  copy elsewhere — a run's `docs/concept/` — is a copy, changed
  only by copying anew, never edited in place.
- **Versioned as a whole**, not per chapter. It is at **v1**. The
  bump rule is one question: could this change invalidate something
  derived from it.
- **It demands nothing by itself.** A chapter cannot be run. What
  can be run is the method below, which is where the concept
  becomes work.

### 1.2 The conventions — `docs/conventions/`

**Eight manuals: how work is done here, and why each rule is the
shape it is.** Recording, committing, hygiene, how an agent is
arranged, how a choice between things you look at is settled, the
exchange — how a delivery goes down to a run and how what the run
learned comes back — and shapes, what a kind of output looks like
and where that description sits.

None of it is CbC. The concept is about how a system is built; the
conventions are about how a repo is kept.

- **A manual never ships.** It is written for a person maintaining
  this, not for a project using it. What a project gets is the
  artifact, never the explanation.
- **Each convention is two things kept apart**: the manual at
  `docs/conventions/<name>/README.md`, and its artifacts — real
  files in `delivery/container/`, which is the master.
- **Eight, not ten.** `decide-first`, `option-comparison` and
  `artifact-kinds` were discarded on 2026-09-24 and nothing replaced
  them. `convention-lifecycle` went on 2026-09-26 and the exchange
  took its place (ADR-0036) — the first convention whose artifacts
  split between the two arrangements in section 4. `shapes` arrived
  on 2026-09-27 (ADR-0037), its model reshaped into the manual it
  had been all along.

## 2. The delivery — what a project gets, and where it goes

**The repeatable stub a project is born from, and updated with
afterwards.** Four kinds of thing live here and only three of them
travel; the last subsection is where they go and what comes back.

### 2.1 The method — `delivery/method/`

The concept made usable: `cbc-framing` (turn an idea into one
falsifiable promise, a layered definition, a registry of slices)
and `cbc-slice` (take one invariant through specify, plan, build,
document until a test that creates the adversity proves it holds).

**Derived from the concept**, and each says so in its `foundation`
field: `concept v1`. A change to the concept asks whether these are
still right.

### 2.2 The stack practice — `delivery/spring-postgres/`

What one real Spring and Postgres project taught:
`infra-establish`, `infra-serve`, `cbc-bootstrap`.

**Not derived from the concept — checked against it.** These came
from practice, not from the idea, and their `foundation` field says
so: `practice, checked against concept v1`. A project on another
stack drops this group whole and keeps the rest.

### 2.3 The container — `delivery/container/`

**How a project is kept, not how it is thought.** The records
(`PLAN`, `TODO`, `devlog`, `ARCHITECTURE`, `CHANGELOG`), the entry
file, the agent decisions log, three convention skills, two rules,
the hygiene files.

**This is the conventions made usable**, the way the method is the
concept made usable. Every one of its seventeen files is the
artifact of one of the eight manuals in 1.2 — the records belong to
`project-recording`, the entry file and the decisions log to
`agent-arrangement`, the three dotfiles to `repo-hygiene`, the
three skills to the three conventions named after them,
`.claude/rules/delivered-copies.md` to the exchange, and
`.claude/rules/shapes-lifecycle.md` to shapes.

A project with no correctness-by-construction in it would still want
most of this, which is why it is a group of its own and not part of
the method. Among what it ships is a whole **work arrangement** for
the run's own agent — section 4.

### 2.4 What does not travel — `installs/`, `fills/`

- **`installs/`** — our procedure for the person operating a birth:
  how a run is seeded (`pure-seed.md`). An update is the exchange
  (2.5), held as two skills of ours. A run never sees this.
- **`fills/`** — text written *into* a newborn's own files rather
  than copied as files.

### 2.5 Where it all goes, and what comes back

A **run** is a separate repository that builds a real system using
what we gave it. Run 3, `never-oversold`, is the live one.

**A run is blind to us.** It holds no address for this repo, no
checkout, no remote. It cannot fetch, and nothing here reaches it
by itself. Every delivery is a person copying files into the run's
`temp/`, and the run's own agent taking them from there.

```
          this repo                              a run
   ┌────────────────────────┐            ┌────────────────────────┐
   │ concept/               │            │ docs/concept/   copy   │
   │ delivery/method/       │  ── a  ──▶ │ .claude/skills/ copies │
   │ delivery/spring-…/     │   person   │ .claude/rules/  copies │
   │ delivery/container/    │   copies   │ PLAN, TODO, devlog     │
   │                        │            │ src/  ← the only thing │
   │  masters               │            │        that is its own │
   └────────────────────────┘            └────────────────────────┘
              ▲                                       │
              └───────── we read its repo ────────────┘
                         and take what it learned
```

**Down — delivery.** Files, copied whole, and a **note** beside
them. The note is the only way our reasoning reaches a run; the
files carry none of it. The run records two numbers in its own
decisions log: the **pin**, a commit of ours it cannot resolve, and
the **read-through**, its own commit we last read up to.

**Up — harvest.** No files move. We read the run's repository
directly and write what we learned into our own masters. A run
never pushes anything here, and what it asked us gets its answer in
the next note down.

The mechanism — the take, what a copy may become between pins, what
a copy cannot carry, what a note holds — is the exchange,
`docs/conventions/exchange/`; the run's half of it ships as
`delivered-copies.md`, ours is `exchange-read` and
`exchange-deliver`.

## 3. How anything here changes

**Stated first, made usable second, and both bent by practice.** The
pairing in section 1 reads top-down — a description, then the thing
made from it. That is the order of writing, not the order of truth.

The loop, as it actually runs:

1. We state (concept, conventions) and make usable (method,
   container).
2. We deliver — files copied whole into a run.
3. The run uses them, and where one fails it, **edits its copy** and
   records why.
4. We read the run and find the edit.
5. **Taken:** our master changes, so the next project never meets
   the same failure. **Declined:** we judge it project-specific, an
   exception, or not worth the change — and the run keeps its edit.

**The rule that matters is about step 5.** A finding is declined
only for not being general. It is never declined because the
description says otherwise. A description is downstream of practice
like everything else here, and a run that contradicts one may have
found the description's flaw rather than its own. When practice and
a statement disagree, the statement is a candidate for change, not
the judge.

That includes this document.

**Where it has already happened**, so the rule is read as a record
and not a wish:

- **ADR-0034.** Run 3 argued down a clause of `convention-lifecycle`
  on the day it first ran under it. Taken. A rule of ours changed on
  a run's argument, against the text as we had shipped it.
- **ADR-0035.** Run 3 made a thing our vocabulary had no word for.
  The vocabulary gained one — and the next day the vocabulary itself
  went, on the same evidence read further.
- **`cbc-slice`, three times.** Every in-place edit run 3 made to
  the method was taken whole. The method has bent three times.
- **The concept has not bent.** It is at v1, verbatim from the
  archive; nothing from three runs has reached a chapter. That is
  either evidence it is right or evidence nothing has been read
  against it hard enough. This page does not know which, and says
  so rather than choosing.

*Not a rule yet. Written here first. It becomes one the day a
decline is caught being made "because the manual says" — that is
the trigger, and until it fires this paragraph is the whole of it.*

## 4. The work arrangement

**What tells an agent how to work in a repo — not the work, and not
a record of it.** Four kinds of file, and each reaches the agent a
different way:

- **the entry file**, `CLAUDE.md` — loaded in full on every task,
  relevant or not, which is why every line in it is expensive
- **skills**, `.claude/skills/` — opened at a moment, by name
- **rules**, `.claude/rules/` — loaded when a file matching their
  `paths:` is touched
- **the decisions log**, `.claude/decisions.md` — why the
  arrangement is the shape it is; read at a retrospective, not
  mid-work

Every repo in this workspace has one. **Two of them exist here:**
the one this repo runs under, and the one it ships inside the
container for someone else to run under.

### 4.1 This repo's — a maintainer's

**The maintainer of the concept, the delivery, and the records that
hold both.** It keeps the concept's statement true, derives the
method from it, holds the master of every file any run receives,
delivers to runs, and reads runs back to learn what to change here.
It is not a builder; there is nothing here to build. **Its work is
section 3, run from this side.**

Entry file: *"A concept repo... Documents only — no code, no
runs."* Three convention skills — `commit-messages`, `commit-plan`,
`visual-comparison` — and the exchange's two, `exchange-read` and
`exchange-deliver`. One rule, `exchange-reading.md`: the shape of
the reading, loading while one is written — the exchange's artifact
and the shapes convention's one instance here, since this repo has
no gate and holds shapes exposed only.

*The records it keeps — `PLAN`, `TODO`, the devlog, the ADRs, the
decisions log, `CHANGELOG`, `ARCHITECTURE` — are not on this page.
Records are where things go stale, and `ARCHITECTURE.md` already
describes most of section 2 a second time. Named here, not filled.*

### 4.2 A run's — a builder's

Shipped in `delivery/container/`, so it is something we write and
they receive.

Entry file: `docs/concept/` and everything under `.claude/` are
**delivered copies**, pinned, and until the framing artifacts exist
the only method work is running `cbc-framing` jointly with the
human. The same three convention skills. Two rules,
`shapes-lifecycle` and `delivered-copies` — the exchange's half for
this side. And beside them the records the arrangement refers to.

The work it arranges: build a real system, keep its records, take
deliveries.

### 4.3 What the difference explains

**Nearly identical, and the difference is now designed rather than
accidental.** Three skills are the same files. The records table has
the same shape. The agent/project commit split is the same rule.

What differs is the *job*, and since ADR-0036 the two arrangements
hold different things because of it. The run holds the receiver's
rule, `delivered-copies.md` — how to take a newer copy without
losing its own edits, and what it may do to one meanwhile. We hold
the deliverer's skills, `exchange-read` and `exchange-deliver`, and
the shape of the reading they produce. Neither side holds the
other's half, because neither could run it.

Until 2026-09-26 this repo held the receiver's protocol,
`convention-lifecycle`, and had never once run it — our registry
pinned us to ourselves — while run 3 ran it at every take. Reading a
shared file and assuming a shared job is how a rule ends up held in
the repo it cannot apply to. That is the string this section exists
to show, and it has been pulled once.

---

## What must stay true

The strings, as constraints. Each is already on this page as a
sentence; here they are collected so a change can be checked
against them in one pass.

- **The concept is authoritative here.** Every copy elsewhere is a
  copy, changed only by copying anew.
- **The container is the master** of every file a run receives.
  Our own `.claude/skills/` copies are downstream of it, not beside
  it.
- **A manual never ships.** What a project gets is the artifact,
  never the explanation.
- **Agent side and project side never share a commit** — in this
  repo and in every run.
- **The exchange's five facts** — a run is blind; nothing arrives by
  itself; copies against masters; a run edits a copy when it fails
  it; nothing moves upward as files — and what follows from them:
  one pin per run, both numbers held by the run, bytes matching at
  the pin, absence carried by the note. Stated once, in
  `docs/conventions/exchange/` §1–§3, and checked there.

## The words

Used across both repos, defined here and nowhere else.

- **deliverer** — the repository holding the master of every file a
  project receives. Here, this repo.
- **run** — a separate repository that builds a real system with
  what it was given. Blind to its deliverer.
- **delivery** — files copied whole into a run, with a note. At
  birth, and after.
- **staging** — a person copying the delivery and its note into a
  run's `temp/`. The operator's act; the run does nothing until it
  has happened.
- **take** — the run's act: moving delivered files from `temp/`
  into place and recording the pin.
- **read-through** — the run's own commit the deliverer last read
  up to. Recorded by the run from the note; moved by every note,
  files or not. Read from here forward.
- **pin** — the one hash a run records for a delivery. A commit of
  the deliverer's; the run stores it and cannot resolve it.
- **note** — the text beside a delivery: what changed since the
  run's pin, and a verdict on everything the run asked.
- **harvest** — us reading a run's repository and changing our
  masters from what it learned. No files move.
- **master** — the one copy of a file that is edited. Every other
  copy changes only by being copied anew.
- **made usable** — what a stated body becomes in the delivery:
  the concept as the method, the conventions as the container.
- **description** — any body of writing things derive from: the
  concept, a manual, this page.
- **manual** — a convention's description, at
  `docs/conventions/<name>/README.md`. Never shipped.
- **foundation** — the frontmatter line by which a shipped file
  names the description it derives from. Not *source*: that was a
  run's word for the deliverer, and is not ours.

## What this page knows is wrong

One thing, left standing where it was found:

1. **4.1** — this repo's own records are not on the map, and
   `ARCHITECTURE.md` describes section 2 a second time.

Two left the list on 2026-09-26, with ADR-0036: the asymmetry is
written down in the exchange's manual, and the shipped entry file no
longer forbids what the shipped rule permits. One left on 2026-09-27,
with ADR-0037: `shapes-lifecycle` has a manual behind it.

When one is fixed it leaves this list. When the list is empty, this
page is claiming to be current — and that is the claim to distrust
most.

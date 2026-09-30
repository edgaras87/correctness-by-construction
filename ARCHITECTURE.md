# Architecture

<!-- This repo AS IT IS NOW: what is tied to what, so that changing
     one part shows what else moves. How a part came to be is the
     ADRs' and the devlog's; this page points there and does not
     retell it. The deliverer's map (project-recording, the
     deliverer's seat; ADR-0044): documents and delivery, with its
     words and the list of what it knows is wrong.

     Written under one rule: state only what is checkable in this
     repo and in the live run, and mark anything merely intended as
     intended. Where it contradicts itself, say so in the list at
     the end rather than pick a side. -->

**One concept, the delivery a project is born from, and the agent
that keeps both true.**

Nothing is built here. No application, no service, no run — this
repo holds documents and hands them to projects that do build. It is
the one concept repo on the concepts tier of the workspace
(`docs/models/tiers.md` §2.2).

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
here is made of and which the container ships a run's own
derivation of (4).

Then what must stay true (5), where things are (6), the words, and
what this page knows is wrong.

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

- **Canonical here.** This is where the concept is true. Every
  copy elsewhere — a run's `docs/concept/` — is a copy, changed
  only by copying anew, never edited in place.
- **Versioned as a whole**, not per chapter. It is at **v1**. The
  bump rule is one question: could this change invalidate something
  derived from it.
- **It demands nothing by itself.** A chapter cannot be run. What
  can be run is the method below, which is where the concept
  becomes work.

### 1.2 The conventions — `docs/conventions/`

**Nine manuals: how work is done here, and why each rule is the
shape it is.** Recording, committing, hygiene, how an agent is
arranged, how a choice between things you look at is settled, the
exchange — how a delivery goes down to a run and how what the run
learned comes back — shapes, what a kind of output looks like and
where that description sits — and conventions themselves, what one
is and how it is made.

None of it is CbC. The concept is about how a system is built; the
conventions are about how a repo is kept.

- **What a convention is, its two parts, and that a manual never
  ships** — `docs/conventions/conventions/` §1.
- **How they hand work to each other** —
  `docs/conventions/README.md`, the index, a local map.

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
`infra-establish`, `infra-serve`, `cbc-bootstrap`. Two of them carry
copy-and-fill templates beside their references, which a run fills
and then owns (ADR-0008).

**Not derived from the concept — checked against it.** These came
from practice, not from the idea, and their `foundation` field says
so: `practice, checked against concept v1`. A project on another
stack drops this group whole and keeps the rest; it then has no
ground or bootstrap skill, and another stack's are that stack's to
harvest, as a group beside this one (ADR-0029).

### 2.3 The container — `delivery/container/`

**How a project is kept, not how it is thought.** The records
(`PLAN`, `TODO`, `devlog`, `ARCHITECTURE`, `CHANGELOG`), the entry
file, the agent decisions log, three convention skills, two rules,
the hygiene files.

**This is the conventions made usable**, the way the method is the
concept made usable. Every one of its seventeen files is the
artifact of one of eight of the nine manuals in 1.2 — `conventions`
ships nothing — the records belong to
`project-recording`, the entry file and the decisions log to
`agent-arrangement`, the three dotfiles to `repo-hygiene`, the
three skills to the three conventions named after them,
`.claude/rules/delivered-copies.md` to the exchange, and
`.claude/rules/shapes-lifecycle.md` to shapes.

A project with no correctness-by-construction in it would still want
most of this, which is why it is a group of its own and not part of
the method. Among what it ships is a whole **work arrangement** for
the run's own agent — section 4.

### 2.4 What does not travel — `installs/`, `fills/`, `README.md`

- **`installs/`** — our procedure for the person operating a birth:
  how a run is seeded (`pure-seed.md`). An update is the exchange
  (2.5), held as two skills of ours. A run never sees this.
- **`fills/`** — text written *into* a newborn's own files rather
  than copied as files: the playbook's steps, into its `PLAN.md`.
- **`README.md`** — the delivery's local map: how its parts land in
  a run.

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

**The rule that holds all of this** — a description lists what
derives from it, each derivative names it, a change walks the list,
a forced change is checked back, a disagreement is decided with
practice as the evidence — is stated once, in the conventions
manual, `docs/conventions/conventions/` §3.5, for every description
this page names: the concept, each manual, and this page. Why step
5 declines a finding only for not being general, and where practice
has already bent a description, is its §3.6. This page is a map and
states no rule of its own. Where a manual and the
concept are handled differently is that manual's *What this does
not cover* and CBC ADR-0039.

## 4. The work arrangement

**What tells an agent how to work in a repo — not the work, and not
a record of it.** Two exist here, derived from the same manuals and
neither from the other (ADR-0042): the one this repo runs under as
the deliverer, a maintainer's, and the one it ships in the
container for a run to work under, a builder's. They are nearly the
same files and differ by design in their job, each side holding
only the half it can run. What the files are, how
each reaches an agent, and what each seat holds is
`docs/conventions/agent-arrangement/`, its seats.

---

## 5. What must stay true

Each rule, and where it is held. This repo has no runtime, so a
rule is held by a header that travels with a file, a standing
comment, a procedure, the shape of the tree, or a check at commit
review, and each entry names which.

- **The concept is canonical here**, and the archive it came from
  is a frozen snapshot, never consulted as a source — §1.1 and
  `docs/conventions/conventions/` §3.5; held in each chapter's
  provenance header.
- **A substantive concept change never lands without a version
  entry** — CHANGELOG's standing comment and ADR-0003; checked at
  commit review, a review-grade wall, named as such.
- **An execution never lands without stating which concept version
  it derives from** — each skill's `foundation` field, which travels
  with every copy (ADR-0004, ADR-0036).
- **The container is the master of every file a run receives** —
  `docs/conventions/exchange/` §1 and §2.
- **A manual never ships** — `docs/conventions/conventions/` §1.
- **A manual never outlives the rule it explains**: a rule changed
  in `delivery/container/` moves its manual in the same commit —
  `docs/conventions/conventions/` §3.5 (ADR-0025).
- **Agent side and project side never share a commit** —
  `docs/conventions/commit-messages/` §2.
- **A pin never claims more than was checked**: reading a run is a
  reading over two diffs, and its verdict is written every time,
  including "taught nothing" — `docs/conventions/exchange/` §6.3
  and §6.5 (ADR-0023).
- **A skill never spans two groups, and nothing that needs Spring,
  PostgreSQL, Maven or podman sits under `method/`** — held by the
  shape of the tree, since a group is a directory and a misfiled
  file shows as a path (ADR-0029). The test is what the skill
  assumes, not what a sentence mentions.
- **A record stub is never re-delivered to a live run** — the run's
  `delivered-copies.md` rule 1 and `docs/conventions/exchange/`
  §2.4 (ADR-0036).
- **The exchange's five facts, and what follows from them** —
  `docs/conventions/exchange/` §1 to §3.

## 6. Codemap

<!-- Where to find things. Descriptions start at column 22; a path
     too long for that column moves every line, so a new one is
     fitted to it (ADR-0044). -->

```
README.md            the front door: what this is, how to use it
ARCHITECTURE.md      this map
PLAN.md              open milestones and their gates
TODO.md              what's next, and the backlog
CHANGELOG.md         the concept-version log (ADR-0003)
devlog/              work history, session by session
concept/             the concept: five chapters, 00-cbc.md first (§1.1)
docs/
├── adr/             decisions and why
├── conventions/     nine manuals and their index (§1.2)
├── models/          the agent model and the tiers model; neither ships
└── baselines/       trial evidence withheld from runs (ADR-0035)
delivery/
├── container/       what a run is born into (§2.3)
├── method/          cbc-framing, cbc-slice (§2.1)
├── spring-postgres/ the stack practice (§2.2)
├── fills/           text written into a newborn's own files (§2.4)
├── installs/        how a run is seeded (§2.4)
└── README.md        the delivery's local map (§2.4)
temp/                working drafts, tracked, deleted when served
CLAUDE.md, .claude/  this repo's work arrangement (§4)
.editorconfig        hygiene: editor settings
.gitattributes       hygiene: line endings and diffs
.gitignore           hygiene: what git leaves untracked
COMMIT-PLAN.md       an in-flight change set, when present
```

---

## The words

Used across both repos, defined here and nowhere else.

- **deliverer** — the repository holding the master of every file a
  project receives. Here, this repo.
- **run** — a separate repository that builds a real system with
  what it was given. Blind to its deliverer.
- **project** — whichever repository is doing the work under a
  convention or making an output: a run, or this one.
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
- **description** — how we understand a thing today, written down:
  the concept, a manual, this page. It may be wrong or incomplete
  and is canonical regardless; what derives from it applies it and
  does not explain. One rule for all of them,
  `docs/conventions/conventions/` §3.5; they differ at the edges
  (ADR-0039).
- **canonical** — of a description or a copy: the one that counts,
  from which every other is derived or copied. Says reference,
  never correctness — a canonical description is today's
  understanding and changes only for a reason recorded. In plain
  engineering words, a source of truth, where the truth is ours
  today; that phrase is a gloss on this word, not a second term. If
  it reads as settled where the stance is today, *standing* is the
  runner-up, recorded here rather than decided.
- **local map** — a directory's `README.md` that says how the parts
  of that area relate, which this page points into. Relations only;
  not every README is one (ADR-0045).
- **manual** — a convention's description, at
  `docs/conventions/<name>/README.md`. Never shipped.
- **seats** — the sides a convention has, this repo's and a run's.
  A manual says whether the two use it the same way.
- **foundation** — the frontmatter line by which a shipped file
  names the description it derives from. Not *source*: that was a
  run's word for the deliverer, and is not ours.

## What this page knows is wrong

Nothing is listed today.

When one is fixed it leaves this list. When the list is empty, this
page is claiming to be current — and that is the claim to distrust
most.

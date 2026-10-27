# Architecture

<!-- This repo AS IT IS NOW: what is tied to what, so that changing
     one part shows what else moves. How a part came to be is the
     ADRs' and the devlog's; this page points there and does not
     retell it. The deliverer's map
     (docs/conventions/project-recording/, its deliverer's seat;
     ADR-0044, ADR-0068): about two pages, owning the pairing, the
     table of runs, how each rule is held and the codemap, and
     pointing at the home of everything else.

     Written under one rule: state only what is checkable in this
     repo and in the live run, and mark anything merely intended as
     intended. A line found wrong, or two that contradict, and not
     fixed at once, is a TODO known issue until it is.
     foundation: the project-recording convention -->

## Overview

**This repo states a concept and its conventions, ships each made
usable to runs, and reads back what the runs learn.**

Two bodies of writing are stated here and never ship: the concept,
`concept/`, and the conventions, `docs/conventions/`, under the
models in `docs/models/`. Each is made usable as something that
does ship: the concept as the method, the conventions as the
container (§1). A run is born from that delivery, takes newer copies
at each pin, and is read back here; what it learned changes our
masters (§2). A few rules must hold across all of it (§5), and the
codemap says where each thing lives (§6). What this repo is for, and
how to use it, is `README.md`.

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
  copy elsewhere — a run's `docs/concept/` — is a copy; what a run
  may do to it is `docs/conventions/exchange/` §5.6. The concept
  changes only here.
- **Versioned as a whole**, not per chapter. It is at **v1**, and
  CHANGELOG's [Unreleased] holds a change that makes the next
  release v2 (ADR-0048). The bump rule is one question: could this
  change invalidate something derived from it.
- **It demands nothing by itself.** A chapter cannot be run. What
  can be run is the method below, which is where the concept
  becomes work.

### 1.2 The conventions — `docs/conventions/`

**Twelve manuals: how work is done here, and why each rule is the
shape it is.** Recording, committing, hygiene, how an agent is
arranged, how a choice between things you look at is settled, the
exchange — how a delivery goes down to a run and how what the run
learned comes back — shapes, what a kind of output looks like and
where that description sits — writing, how a text reads — the
retrospective, how a finished run looks back and applies what it
found — facts in sync, how each fact keeps one home and every text
relying on it stays in agreement with it — and conventions
themselves, what one is and how it is made.

None of it is CbC. The concept is about how a system is built; the
conventions are about how a repo is kept.

- **What a convention is, and its two parts** —
  `docs/models/idea-to-output.md` §6.
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
Beside them, at `delivery/method/.claude/shapes/`, the shapes their
gates read: what a record or a test of the method looks like, read
at a step's close and never while it is written. They come from
practice, under the shapes convention, and their `foundation` line
says so (`docs/conventions/shapes/`).

**Derived from the concept**, and each says so in its `foundation`
field: `concept v1`. A change to the concept asks whether these are
still right. They live at `delivery/method/.claude/skills/cbc-framing/`
and `delivery/method/.claude/skills/cbc-slice/`. With 2.2 and 2.4,
this is the concept's list of what derives from it; the chapters
carry none (`docs/conventions/facts-in-sync/` §4, step 1).

### 2.2 The stack practice — `delivery/spring-postgres/`

What one real Spring and Postgres project taught:
`infra-establish`, `infra-serve`, `cbc-bootstrap`. Two of them carry
copy-and-fill templates beside their references, which a run fills
and then owns (ADR-0008).

**Not derived from the concept — checked against it.** These came from
practice, not from the idea, and their `foundation` field says so:
`practice, checked against concept v1`. They live at
`delivery/spring-postgres/.claude/skills/infra-establish/`,
`delivery/spring-postgres/.claude/skills/infra-serve/` and
`delivery/spring-postgres/.claude/skills/cbc-bootstrap/`. A project on
another stack drops this group whole and keeps the rest; it then has
no ground or bootstrap skill, and another stack's are that stack's to
harvest, as a group beside this one (ADR-0029).

### 2.3 The container — `delivery/container/`

**How a project is kept, not how it is thought.** The records
(`README`, `PLAN`, `TODO`, `devlog`, `ARCHITECTURE`, `CHANGELOG`,
the first ADR), the entry file, the agent decisions log, five
convention skills, four rules, one approach on trial, the hygiene
files, and the README of its scratch space, `temp/`.

**This is the conventions made usable**, the way the method is the
concept made usable. Every one of its twenty-three files but one is the
artifact of one of eleven of the twelve manuals in 1.2 — `conventions`
ships nothing — the records belong to `project-recording`,
`delivery/container/.claude/rules/one-home.md` to facts-in-sync,
the entry file and the decisions log to
`agent-arrangement`, the three dotfiles to `repo-hygiene`,
`commit-messages`, `commit-plan` and `visual-comparison` to the
conventions named after them, `retrospective` and
`apply-retrospective` to the retrospective,
`delivery/container/.claude/rules/delivered-copies.md` and
`delivery/container/temp/README.md` to the exchange,
`delivery/container/.claude/rules/shapes-lifecycle.md` to
shapes, and `delivery/container/.claude/rules/writing.md` to
writing. The one is
`delivery/container/.claude/approaches-on-trial/approach-drafting.md`,
an approach on trial: a manual's artifact only once an evaluation
places it.

A project with no correctness-by-construction in it would still want
most of this, which is why it is a group of its own and not part of
the method. Among what it ships is a whole **work arrangement** for
the run's own agent — section 4.

### 2.4 What does not travel — `installs/`, `fills/`, `README.md`

- **`installs/`** — our procedure for the person operating a birth:
  how a run is seeded (`pure-seed.md`). An update is the exchange
  (2.5), held as two skills and two rules of ours. A run never sees
  this.
- **`fills/`** — text written *into* a newborn's own files rather
  than copied as files: the playbook's steps, into its `PLAN.md`.
  The playbook, `delivery/fills/cbc-run-pure-playbook.md`, is
  checked against concept v1, as the stack practice is.
- **`README.md`** — the delivery's local map: how its parts land in
  a run.

### 2.5 Where it all goes, and what comes back

A **run** is a separate repository that builds a real system using
what we gave it. We call a run by its ordinal. It names itself at its
Identity step, and until then has only ours:

| ours | its own | where | state |
|---|---|---|---|
| run 1 | — | `~/IdeaProjects/cbc-pure-run` | frozen |
| run 2 | — | `~/IdeaProjects/cbc-pure-run-2` | idle since its Step 0 |
| run 3 | `never-oversold` | `~/IdeaProjects/cbc-pure-run-3` | live |
| run 4 | `safe-reservation-2` | `~/IdeaProjects/cbc-pure-run-4` | through Release, not yet read |
| run 5 | `event-tickets` | `~/IdeaProjects/cbc-pure-run-5` | through Release, read, not yet answered |

**A run is blind to us.** It holds no address for this repo, no
checkout, no remote. It cannot fetch, and nothing here reaches it
by itself. Every delivery is copied into the run's `temp/`, by the
reviewer or by the agent when told to, and the run's own agent
takes it from there (`docs/conventions/exchange/` §3.1).

```
          this repo                              a run
   ┌────────────────────────┐            ┌────────────────────────┐
   │ concept/               │            │ docs/concept/   copy   │
   │ delivery/method/       │  staged ─▶ │ .claude/skills/ copies │
   │ delivery/spring-…/     │  into its  │ .claude/rules/  copies │
   │ delivery/container/    │   temp/    │ .claude/shapes/ copies │
   │                        │            │ .claude/approaches-on- │
   │                        │            │  trial/         copies │
   │                        │            │ PLAN, TODO, devlog,    │
   │  masters               │            │ src/ … its own         │
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
`docs/conventions/exchange/`. The run's half of it ships as
`delivery/container/.claude/rules/delivered-copies.md`. Ours is two
skills, `exchange-read` and `exchange-deliver`, and two rules,
`.claude/rules/exchange-reading.md` and
`.claude/rules/working-a-reading.md`.

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
   exception, or not worth the change — and the edit goes, its need
   to the run's own records (`docs/conventions/exchange/` §4).

**The rule that holds all of this** — a description lists what
derives from it, each derivative names it, a change walks the list,
a forced change is checked back, a disagreement is decided with
practice as the evidence — is stated once, in
`docs/conventions/facts-in-sync/` §4, for every description this
page names: the concept, each model, each manual.
Why step 5 declines a finding only for not being general, and where
practice has already bent a description, is
`docs/conventions/facts-in-sync/` §5. This page is a map and
states no rule of its own. Where a manual and the
concept are handled differently is that manual's *What this does
not cover* and ADR-0039.

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
  `docs/conventions/facts-in-sync/` §4; held by CHANGELOG's `[v1]`
  entry, which names the archive copy a snapshot, and checked at
  commit review.
- **A substantive concept change never lands without a version
  entry** — CHANGELOG's standing comment and ADR-0003; checked at
  commit review, a review-grade wall, named as such.
- **An execution never lands without stating which concept version
  it derives from** — each skill's `foundation` field, which travels
  with every copy (ADR-0004, ADR-0036).
- **Every file a run receives has its master here,** in the group
  that ships it: the method, the container, a stack practice, the
  concept — `docs/conventions/exchange/` §1 and §3.2; held by a
  procedure, `exchange-deliver`, which stages only from these
  masters.
- **A manual never ships** — `docs/conventions/exchange/` §3.2;
  held by the shape of the tree: the manuals sit under `docs/`, and
  a delivery stages only from `delivery/` and `concept/`.
- **A manual never outlives the rule it explains**: a rule changed
  in `delivery/container/` is checked back against its manual, and
  whichever side is wrong changes —
  `docs/conventions/facts-in-sync/` §4 and §5 (ADR-0025); checked
  at commit review by the foundation check,
  `.claude/rules/foundation-check.md`.
- **Agent side and project side never share a commit** —
  `docs/conventions/commit-messages/` §2; held by a procedure, the
  `commit-messages` skill, and checked at commit review.
- **A pin never claims more than was checked**: a read takes the
  run's decisions log, its backlog and the diff of every copy it
  holds, and every read ends with a note, even one that says
  nothing was learned — `docs/conventions/exchange/` §6.1 and §6.6
  (ADR-0023); held by procedures, `exchange-read` and
  `exchange-deliver`.
- **A skill never spans two groups, and nothing that needs Spring,
  PostgreSQL, Maven or podman sits under `method/`** — held by the
  shape of the tree, since a group is a directory and a misfiled
  file shows as a path (ADR-0029). The test is what the skill
  assumes, not what a sentence mentions.
- **A record stub is never re-delivered to a live run** — the run's
  `delivered-copies.md` rule 1 and `docs/conventions/exchange/`
  §2.4 (ADR-0036).
- **The exchange's five facts, and what follows from them** —
  `docs/conventions/exchange/` §1 to §3; held by procedures,
  `exchange-read` and `exchange-deliver` on our side, and the rule
  shipped from `delivery/container/.claude/rules/delivered-copies.md`
  on the run's.

## 6. Codemap

<!-- Where to find things. Descriptions start at column 22; a path
     too long for that column moves every line, so a new one is
     fitted to it (ADR-0044). -->

```
README.md            the front door: what this is, how to use it
ARCHITECTURE.md      this map
PLAN.md              the step form, and the step being worked
TODO.md              what's next, and the backlog
TODO-CONVERSATION-MEMORY.md
                     the talk behind TODO items, on trial (ADR-0060)
CHANGELOG.md         the concept-version log (ADR-0003)
devlog/              work history, one file per month
concept/             the concept: five chapters, 00-cbc.md first (§1.1)
docs/
├── adr/             decisions and why
├── conventions/     twelve manuals and their index (§1.2)
├── glossary.md      what each coined word means
├── models/          agent, tiers, idea-to-output; none ships
└── baselines/       trial evidence withheld from runs (ADR-0035)
delivery/
├── container/       what a run is born into (§2.3)
├── method/          cbc-framing, cbc-slice, their shapes (§2.1)
├── spring-postgres/ the stack practice (§2.2)
├── fills/           text written into a newborn's own files (§2.4)
├── installs/        how a run is seeded (§2.4)
└── README.md        the delivery's local map (§2.4)
temp/                drafts and kept files, tracked, deleted when served
CLAUDE.md, .claude/  this repo's work arrangement (§4)
.editorconfig        hygiene: editor settings
.gitattributes       hygiene: line endings and diffs
.gitignore           hygiene: what git leaves untracked
COMMIT-PLAN.md       an in-flight change set, when present
```

---

## The words

What each coined word means is `docs/glossary.md`.

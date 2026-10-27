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
masters (§2). A few rules must hold across all of it (§3), and the
codemap says where each thing lives (§4). What this repo is for, and
how to use it, is `README.md`.

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

Where each group lands, and which files are copies, is
`delivery/README.md` §1 and §2; the cycle of pins and readings is
`docs/conventions/exchange/` §2.5.

---

## 1. What is stated here

Two bodies of writing, neither of which ships. Each has something
in the delivery that is it *made usable*, and the pairing is the
spine of this repo. The models ship nothing either:

| stated | made usable |
|---|---|
| the concept (§1.1) | the method (§2.1) |
| the conventions (§1.2) | the container (§2.3) |
| the models (§1.3) | nothing: a manual may stand on one |

### 1.1 The concept — `concept/`

Five chapters, `concept/00-cbc.md` first.

- **Canonical here.** Every copy elsewhere, a run's `docs/concept/`,
  is a copy; what a run may do to it is
  `docs/conventions/exchange/` §5.6. The concept changes only here.
- **Versioned as a whole**, not per chapter. It is at **v1**, and
  CHANGELOG's [Unreleased] holds a change that makes the next
  release v2 (ADR-0048). When its version moves is `CHANGELOG.md`'s
  standing comment.
- **It demands nothing by itself.** A chapter cannot be run; the
  method can (§2.1).

### 1.2 The conventions — `docs/conventions/`

How work is done here, and why each rule is as it is. None of it is
CbC: the concept is about how a system is built, the conventions
about how a repo is kept. What a convention is, and its two parts,
is `docs/models/idea-to-output.md` §6; how they hand work to each
other is the index, `docs/conventions/README.md`.

- **agent-arrangement** — the files that make an agent work in a
  repo: `docs/conventions/agent-arrangement/`.
- **commit-messages** — how a commit is written:
  `docs/conventions/commit-messages/`.
- **commit-plan** — how work larger than one commit is planned:
  `docs/conventions/commit-plan/`.
- **conventions** — how a way of working is written down and made
  usable: `docs/conventions/conventions/`.
- **exchange** — what passes between a deliverer and a run:
  `docs/conventions/exchange/`.
- **facts-in-sync** — how each fact keeps one home, and what relies
  on it agrees: `docs/conventions/facts-in-sync/`.
- **project-recording** — the records, and how each is kept:
  `docs/conventions/project-recording/`.
- **repo-hygiene** — the three files every repo carries:
  `docs/conventions/repo-hygiene/`.
- **retrospective** — how a finished run looks back:
  `docs/conventions/retrospective/`.
- **shapes** — what a kind of output looks like:
  `docs/conventions/shapes/`.
- **visual-comparison** — how the way a structure is shown is
  chosen: `docs/conventions/visual-comparison/`.
- **writing** — how a text reads: `docs/conventions/writing/`.

### 1.3 The models — `docs/models/`

Ideas any repo can adapt, their rules varying by repo
(`docs/models/idea-to-output.md` §2): the agent, the tiers, and idea
to output. A manual that stands on one names it in its `foundation`
line.

## 2. The delivery, and the runs it reaches

What ships, by group. How each group lands in a run is the
delivery's local map, `delivery/README.md`. The concept's list of
what derives from it is §2.1, §2.2 and the playbook in §2.4; the
chapters carry none (`docs/conventions/facts-in-sync/` §4, step 1).

### 2.1 The method — `delivery/method/`

The concept made usable: `cbc-framing` and `cbc-slice`, under
`.claude/skills/`, and the shapes their gates read, under
`.claude/shapes/`. Each skill is derived from the concept, and its
`foundation` line says `concept v1`.

### 2.2 The stack practice — `delivery/spring-postgres/`

What one real Spring and Postgres project taught: `infra-establish`,
`infra-serve` and `cbc-bootstrap`. Not derived from the concept but
checked against it: `practice, checked against concept v1`. A run on
another stack takes no `spring-postgres/`; another stack's practice
would be a group beside this one (ADR-0029).

### 2.3 The container — `delivery/container/`

The conventions made usable: the record stubs, the entry file, the
decisions log, the convention skills and rules, an approach on
trial, the hygiene files, and `temp/README.md`. Which convention a
file belongs to is its `foundation` line. A project with no
correctness-by-construction in it would still want most of this,
which is why it is a group of its own.

### 2.4 What does not travel — `installs/`, `fills/`, `README.md`

- **`installs/`** — how a run is seeded,
  `delivery/installs/pure-seed.md`. A run never sees it.
- **`fills/`** — text written into a newborn's own files: the
  playbook's steps, into its `PLAN.md`. The playbook,
  `delivery/fills/cbc-run-pure-playbook.md`, is checked against
  concept v1.
- **`README.md`** — the delivery's local map.

### 2.5 The runs

A run builds a real system with what we gave it. We call a run by
its ordinal. It names itself at its Identity step, and until then
has only ours:

| ours | its own | where | state |
|---|---|---|---|
| run 1 | — | `~/IdeaProjects/cbc-pure-run` | frozen |
| run 2 | — | `~/IdeaProjects/cbc-pure-run-2` | idle since its Step 0 |
| run 3 | `never-oversold` | `~/IdeaProjects/cbc-pure-run-3` | live |
| run 4 | `safe-reservation-2` | `~/IdeaProjects/cbc-pure-run-4` | through Release, not yet read |
| run 5 | `event-tickets` | `~/IdeaProjects/cbc-pure-run-5` | through Release, read, not yet answered |

How a delivery goes down and what a run learned comes back is the
exchange, `docs/conventions/exchange/`: a run is blind to us (§1),
records a pin and a read-through (§2.2), takes each delivery (§4),
and is read back here (§6). What each side holds for it is the
exchange's *What this is made usable as*.

## 3. What must stay true

Each rule that must hold across this repo, where it is stated, and
what holds it. This repo has no runtime, so a rule is held by a line
that travels with a file, a standing comment, a procedure, the shape
of the tree, or a check at commit review.

| Rule | Stated in | Held by |
|---|---|---|
| The concept is canonical here; the archive it came from is a frozen snapshot, never a source | §1.1; `CHANGELOG.md`'s `[v1]` entry | commit review |
| A concept change that could invalidate what derives from it lands with a version entry | `CHANGELOG.md`'s standing comment (ADR-0003) | commit review |
| Every execution states the concept version it derives from | `docs/conventions/conventions/` §1.3 (ADR-0004, ADR-0036) | its `foundation` line, which travels with every copy |
| Every file a run receives has its master here, in the group that ships it | `docs/conventions/exchange/` §1 and §3.2 | `exchange-deliver`, which stages only from the masters |
| A manual never ships | `docs/conventions/exchange/` §3.2 | the tree: manuals sit under `docs/`, and a delivery stages only from `delivery/` and `concept/` |
| A manual never outlives the rule it explains | `docs/conventions/facts-in-sync/` §4 and §5 (ADR-0025) | the foundation check, `.claude/rules/foundation-check.md`, at each commit |
| Agent side and project side never share a commit | `docs/conventions/commit-messages/` §2 | the `commit-messages` skill, and commit review |
| A pin never claims more than was checked | `docs/conventions/exchange/` §6.1 and §6.6 (ADR-0023) | `exchange-read` and `exchange-deliver` |
| A skill never spans two groups, and nothing that needs Spring, PostgreSQL, Maven or podman sits under `method/` | ADR-0029 | the tree: a group is a directory, so a misfiled file shows as a path |
| A record stub is never re-delivered to a live run | `docs/conventions/exchange/` §2.4 (ADR-0036) | the run's `delivered-copies.md`, rule 1 |
| The exchange's five facts hold | `docs/conventions/exchange/` §1 | `exchange-read` and `exchange-deliver`; the run's `delivered-copies.md` |

## 4. Codemap

<!-- Where to find things. Descriptions start at column 22; a path
     too long for that column moves every line, so a new one is
     fitted to it (ADR-0044). -->

A line marked *record* is one of the records; what each answers is
`docs/conventions/project-recording/` §1.

```
README.md            record
ARCHITECTURE.md      record: this map
PLAN.md              record
TODO.md              record
TODO-CONVERSATION-MEMORY.md
                     record
CHANGELOG.md         record
devlog/              record
concept/             the concept: five chapters, 00-cbc.md first (§1.1)
docs/
├── adr/             record
├── conventions/     the manuals and their index (§1.2)
├── glossary.md      record
├── models/          the models (§1.3)
└── baselines/       trial evidence withheld from runs (ADR-0035)
delivery/
├── container/       what a run is born into (§2.3)
├── method/          cbc-framing, cbc-slice, their shapes (§2.1)
├── spring-postgres/ the stack practice (§2.2)
├── fills/           text written into a newborn's own files (§2.4)
├── installs/        how a run is seeded (§2.4)
└── README.md        the delivery's local map (§2.4)
temp/                drafts and kept files, tracked, deleted when served
CLAUDE.md, .claude/  this repo's work arrangement; .claude/decisions.md
                     is a record
.editorconfig        hygiene: editor settings
.gitattributes       hygiene: line endings and diffs
.gitignore           hygiene: what git leaves untracked
COMMIT-PLAN.md       record, when present
```

---

## The words

What each coined word means is `docs/glossary.md`.

# Architecture

<!-- This repo AS IT IS NOW: what is tied to what, so that changing
     one part shows what else moves. How a part came to be is the
     ADRs' and the devlog's; this page points there and does not
     retell it. The Concept Deliverer's ARCHITECTURE.md
     (.claude/understanding/architecture.md;
     ADR-0044, ADR-0068): aiming at about two pages, owning the pairing of
     stated and made usable, the table of CBC Runs, how each rule is held and the codemap, and
     pointing at the home of everything else.

     Written under one rule: state only what is checkable in this
     repo and in the CBC Runs, and mark anything merely intended as
     intended. A line found wrong, or two that contradict, and not
     fixed at once, is a TODO known issue until it is.
     Why the form is as it is: (records, knowledge/backbone-ideas/records.md
     §10, The architecture; and records, in keeping knowledge,
     knowledge/problem-domain-ideas/keeping-knowledge/records-in-keeping-knowledge.md §5). -->

## Overview

**This repo states a concept and its conventions, ships each made
usable to CBC Runs, and reads back what the CBC Runs learn.**

Two bodies of writing are stated here and never ship: the concept,
`concept/`, and the conventions, `docs/conventions/`, under the
Idea Models in `docs/models/`. Each is made usable as something that
does ship: the concept as the method, the conventions as the
Container Group (§1, *What is stated here*). A CBC Run is born from
that delivery. It takes newer copies at each Delivery Pin, and is
read back here. What it learned changes our Master Copies (§2, *The
delivery and the CBC Runs*). Eleven rules must hold across all of it (§3, *What must stay true*), and the
codemap says where each thing lives (§4, *Codemap*). What this repo is for, and
how to use it, is `README.md`.

```
          this repo                              a CBC Run
   ┌────────────────────────┐            ┌────────────────────────┐
   │ concept/               │            │ docs/concept/   copy   │
   │ delivery/method/       │  staged ─▶ │ .claude/skills/ copies │
   │ delivery/spring-…/     │  into its  │ .claude/rules/  copies │
   │ delivery/container/    │   temp/    │ .claude/shapes/ copies │
   │                        │            │ .claude/approaches-on- │
   │                        │            │  trial/         copies │
   │                        │            │ docs/glossary/  copies │
   │                        │            │ PLAN, TODO, devlog,    │
   │  Master Copies         │            │ src/ … its own         │
   └────────────────────────┘            └────────────────────────┘
              ▲                                       │
              └───────── we read its repo ────────────┘
                         and take what it learned
```

Where each group lands, and which files are copies, is the delivery's
Local Map's
(`delivery/README.md` §1, *The groups and the tree*, and §2, *Three ways a file lands*).
The cycle of Delivery Pins and CBC Run Readings is the Exchange Convention's
(`docs/conventions/exchange/` §2.5, *One cycle*).

---

## 1. What is stated here

Two bodies of writing, neither of which ships. Each is made usable as
something in the delivery, and this pairing is what this repo is
built around. The Idea Models ship nothing either:

| stated | made usable |
|---|---|
| the concept (§1.1, *The concept*) | the Method Group (§2.1, *The Method Group*) |
| the conventions (§1.2, *The conventions*) | the Container Group (§2.3, *The Container Group*) |
| the Idea Models (§1.3, *The Idea Models*) | nothing: a manual may stand on one |

### 1.1 The concept

`concept/`: five chapters, `concept/00-cbc.md` first.

- **Canonical here.** The concept's one canonical text is here. A CBC
  Run's `docs/concept/` holds a copy. What a CBC Run may do to it is the Exchange Convention's
  (`docs/conventions/exchange/` §5.6, *Editing a chapter*). The concept changes only here.
- **Imported once.** The chapters came from the archive repo,
  `system-design-method`, at its commit `fe0075d`. The copy there is
  a frozen snapshot, never a source.
- **Versioned as a whole**, not per chapter. It is at **v1**, and
  CHANGELOG's [Unreleased] holds a change that makes the next
  release v2 (ADR-0048). When its version moves is `CHANGELOG.md`'s
  header comment.
- **It demands nothing by itself.** A chapter cannot be run; the
  method can (§2.1, *The Method Group*).

### 1.2 The conventions

`docs/conventions/`: how work is done here, and why each rule is as
it is. None of it is about correctness by construction: the concept
is about how a system is built,
the conventions about how a repo is kept. What a convention is, its
manual and the Work Approaches made from it, is the Idea-to-Output
Model's (`docs/models/idea-to-output.md` §6, *A convention*). How
they hand work to each other is the conventions' Local Map,
`docs/conventions/README.md`.

- `docs/conventions/agent-arrangement/` — the files that make an
  agent work in a repo.
- `docs/conventions/commit-messages/` — how a commit is written.
- `docs/conventions/commit-plan/` — how work larger than one commit
  is planned.
- `docs/conventions/conventions/` — how a way of working is written
  down and made usable.
- `docs/conventions/exchange/` — what passes between a Concept
  Deliverer and a CBC Run.
- `docs/conventions/facts-in-sync/` — how each fact keeps one home,
  and what relies on it agrees.
- `docs/conventions/retrospective/` — how a finished CBC Run looks
  back.
- `docs/conventions/shapes/` — what a kind of output looks like.
- `docs/conventions/visual-comparison/` — how the way a structure is
  shown is chosen.
- `docs/conventions/writing/` — how a text reads.

### 1.3 The Idea Models

`docs/models/`: ideas any repo can adapt, their rules varying by repo
(`docs/models/idea-to-output.md` §2, *The kinds*): the Agent Model,
the Tiers Model and the Idea-to-Output Model. A manual that stands on
one names it in its Foundation Line.

## 2. The delivery and the CBC Runs

What ships, by group. How each group lands in a CBC Run is the
delivery's Local Map, `delivery/README.md`. What stands on the
concept is the method, derived from it, and the Stack Group and the
playbook, checked against it (§2.1, *The Method Group*, §2.2, *The
Stack Group* and §2.4, *What does not ship*). This list is kept here: the chapters carry none
(`docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule*, step 1).

### 2.1 The Method Group

`delivery/method/`: the concept made usable. The cbc-framing and
cbc-slice Agent Skills, under `.claude/skills/`, the Output Shapes their Plan
Step Gates read, under `.claude/shapes/`, and the concept's and the
method's Glossary Names, `docs/glossary/method.md`. Each Agent Skill is derived
from the concept, as its
Foundation Line says (`docs/conventions/conventions/` §1.3, *The Foundation Line*).

### 2.2 The Stack Group

`delivery/spring-postgres/`: what one real Spring and Postgres
project taught: the infra-establish, infra-serve and cbc-bootstrap
Agent Skills. Not derived from the concept but
checked against it, as their Foundation Lines say
(`docs/conventions/conventions/` §1.3, *The Foundation Line*). Beside
them, the stack's Glossary Names, `docs/glossary/stack.md`. A CBC Run on
another stack takes no `spring-postgres/` (`docs/conventions/exchange/` §3.4, *One group per file*); another stack's Agent
Skills would be a group beside this one.

### 2.3 The Container Group

`delivery/container/`: the conventions made usable. The plan's and
the glossary's Record Stubs, the Entry File, the Decisions Log, the convention Agent Skills
and Agent Rules, an Approach on Trial, and the shared
Glossary Names, `docs/glossary/container.md`. Which convention a
file belongs to is its Foundation Line. A project with no
correctness-by-construction in it would still want most of this,
which is why it is a group of its own.

### 2.4 What does not ship

`installs/`, `fills/` and `README.md`:

- **`installs/`** — how a CBC Run is seeded,
  `delivery/installs/pure-seed.md`. A CBC Run never sees it.
- **`fills/`** — the Delivery Fills, text written into a Newborn CBC Run's own files: the
  playbook's Plan Steps, into its `PLAN.md`. The playbook,
  `delivery/fills/cbc-run-pure-playbook.md`, is checked against
  concept v1.
- **`README.md`** — the delivery's Local Map.

### 2.5 The CBC Runs

A CBC Run builds a real system with what we gave it. We call a CBC Run by
its ordinal. It names itself at one of its Plan Steps, and until
then has only ours:

| ours | its own | where | state |
|---|---|---|---|
| CBC Run 1 | — | `~/IdeaProjects/cbc-pure-run` | frozen |
| CBC Run 2 | — | `~/IdeaProjects/cbc-pure-run-2` | idle since its Step 0 |
| CBC Run 3 | `never-oversold` | `~/IdeaProjects/cbc-pure-run-3` | live |
| CBC Run 4 | `safe-reservation-2` | `~/IdeaProjects/cbc-pure-run-4` | through Release, judged (ADR-0089) |
| CBC Run 5 | `event-tickets` | `~/IdeaProjects/cbc-pure-run-5` | through Release, judged (ADR-0089) |
| CBC Run 6 | `checkout` | `~/IdeaProjects/cbc-pure-run-6` | through Release, judged (ADR-0089) |

How a delivery goes down and what a CBC Run learned comes back is the
Exchange Convention's, `docs/conventions/exchange/`. A CBC Run:

- is blind to us (`docs/conventions/exchange/` §1, *What cannot change*);
- records a Delivery Pin and a Read-Through Commit
  (`docs/conventions/exchange/` §2.2, *The CBC Run*);
- takes each delivery (`docs/conventions/exchange/` §4, *The Delivery Take*);
- is read back here (`docs/conventions/exchange/` §6, *Up from the CBC Run*).

What each side holds for the exchange is the Exchange Convention's
(`docs/conventions/exchange/`, *What this is made usable as*).

## 3. What must stay true

Each rule that must hold across this repo, where it is stated, and
what holds it. This repo has no runtime, so a rule is held by a line
kept in a file, a header comment, a procedure, the
layout of the tree, or a check at commit review.

| Rule | Stated in | Held by |
|---|---|---|
| The concept is canonical here; the archive repo it came from, `system-design-method`, is a frozen snapshot, never a source | §1.1, *The concept* | commit review |
| A concept change that could invalidate what derives from it lands with a version entry | `CHANGELOG.md`'s header comment (ADR-0003) | commit review |
| Every Agent Skill of the method states the concept version it derives from | `docs/conventions/conventions/` §1.3, *The Foundation Line* (ADR-0004, ADR-0036) | its Foundation Line, which every copy carries |
| Every file a CBC Run receives has its Master Copy here, in the group that ships it | `docs/conventions/exchange/` §1, *What cannot change* and §3.2, *What goes* | the exchange-deliver Agent Skill, which stages a delivery only from the Master Copies |
| A manual never ships | `docs/conventions/exchange/` §3.2, *What goes* | the tree: manuals sit under `docs/`, and a delivery is staged only from `delivery/` and `concept/` |
| No manual explains a rule that no longer holds | `docs/conventions/facts-in-sync/` §4, *A Canonical Description's rule* and §5, *A disagreement* (ADR-0025) | the Foundation Check, `.claude/rules/foundation-check.md`, at each commit |
| Agent side and project side never share a commit | (`docs/conventions/commit-messages/` §2.3, *The `agent` scope*) | the commit-messages Agent Skill, and commit review |
| A Delivery Pin never claims more than was checked | `docs/conventions/exchange/` §6.1, *Reading a CBC Run* and §6.6, *The Delivery Note after a read* (ADR-0023) | the exchange-read and exchange-deliver Agent Skills |
| An Agent Skill never spans two groups, and nothing that needs Spring, PostgreSQL, Maven or podman sits under `method/` | `docs/conventions/exchange/` §3.4, *One group per file* | the tree: a group is a directory, so a misfiled file shows as a path |
| A Record Stub is never re-delivered to a live CBC Run | `docs/conventions/exchange/` §2.4, *The records' exception* (ADR-0036) | the CBC Run's delivered-copies rule 1 |
| The five facts of every flow hold between this repo and its CBC Runs | (`docs/models/tiers.md` §3.5, *What holds on every flow*); here, `docs/conventions/exchange/` §1, *What cannot change* | the exchange-read and exchange-deliver Agent Skills; the CBC Run's delivered-copies Agent Rule |

## 4. Codemap

<!-- Where to find things. Descriptions start at column 22; a path
     too long for that column moves every line, so a new one is
     fitted to it (ADR-0044). -->

A line marked *record* is one of the records; what each answers is records'
(`knowledge/backbone-ideas/records.md` §3, *The records*).

```
README.md            record
ARCHITECTURE.md      record: this page
PLAN.md              record
TODO.md              record
TODO-CONVERSATION-MEMORY.md
                     record
CHANGELOG.md         record
devlog/              record
concept/             the concept: five chapters, 00-cbc.md first (§1.1)
knowledge/           the layers model, one folder per layer (ADR-0084)
├── backbone-ideas/  layer 1: the Backbone Ideas
└── problem-domain-ideas/
                     layer 2: the Problem Domain Ideas, by Problem Domain
docs/
├── adr/             record
├── conventions/     the manuals and their index (§1.2)
├── glossary.md      record
├── models/          the Idea Models (§1.3)
└── baselines/       trial evidence withheld from CBC Runs (ADR-0035)
delivery/
├── container/       what a CBC Run is born into (§2.3)
├── method/          the cbc-framing and cbc-slice Agent Skills, their Output Shapes and Glossary Names (§2.1)
├── spring-postgres/ the Stack Group (§2.2)
├── fills/           text written into a Newborn CBC Run's own files (§2.4)
├── installs/        how a CBC Run is seeded (§2.4)
└── README.md        the delivery's Local Map (§2.4)
temp/                drafts and kept files, tracked, deleted once the work that needed them is done
CLAUDE.md, .claude/  this repo's work arrangement; .claude/decisions.md
                     is a record; .claude/understanding/ holds why an
                     Agent Rule or Agent Skill built on it is as it is,
                     and never loads (ADR-0084)
.editorconfig        hygiene: editor settings
.gitattributes       hygiene: line endings and diffs
.gitignore           hygiene: what git leaves untracked
COMMIT-PLAN.md       record, when present
```

---

## The words

The Glossary Names, and what each means, are `docs/glossary.md`.

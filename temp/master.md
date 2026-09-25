<!-- DRAFT, 2026-09-24. It lives in temp/ and is edited in place
     until it is worth placing; where it finally sits, and what kind
     of document it is, are decided from what it ends up containing
     rather than before. A section that outgrows this file becomes
     its own document and leaves a paragraph behind.

     The name is provisional: everything here is a master, and
     everywhere else holds copies.

     Written under one rule: state only what is checkable in this
     repo and in run 3 today, and mark anything that is merely
     intended as intended. Where we contradict ourselves, say so
     rather than pick a side. -->

# Master

**One concept, the delivery a project is born from, and the agent
that keeps both true.**

Nothing is built here. No application, no service, no run — this
repo holds documents and hands them to projects that do build.

## What this is for

**Not a description to be right about — a picture of what is tied
to what, so that changing one part shows the others move.**

The strings are real and none of them is visible from inside a
single file. Change the work arrangement and the container may have
to change, because it ships one. Change the concept and everything
derived from it is in question. Change what a run may edit to its
copies and three documents in two repos start disagreeing.

**Today those strings get noticed afterwards**, usually by the run,
usually after something has already shipped wrong. Three such
findings are on this page, left written as contradictions rather
than smoothed away.

So the use is: **before a change, read this to see what else it
pulls.** If a change would make something else here untrue, that
gets said at the time — with what would have to move — instead of
being discovered a week later. Then the change can be taken, taken
differently, or dropped, which is a decision and not a discovery.

The cost of that is this page being current. A map that is wrong
about what connects to what is worse than no map, because it is
believed.

## The parts

- **The concept** — why the repo exists. The design idea itself, in
  plain words.
- **The delivery** — the repeatable stub a project is born from and
  updated with. The concept made usable, plus everything else a
  project needs to be kept.
- **The agent as maintainer** — who keeps the first two true, and
  what it is made of.

Each has a section below. What a run is, and how the two repos
reach each other, sits inside the delivery — it is where the
delivery goes.

And one thing that is **not** a part, because it appears in two of
them: the **work arrangement**. The agent is made of one, and the
container ships another. It gets its own section so both can point
at it.

---

## 1. The concept — `concept/`

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

## 2. The delivery — what a project gets, and where it goes

**The repeatable stub a project is born from, and updated with
afterwards.** Four kinds of thing live here and only three of them
travel; the last subsection is where they go and what comes back.

### 2.1 The method — `delivery/method/`

The concept made usable: `cbc-framing` (turn an idea into one
falsifiable promise, a layered definition, a registry of slices)
and `cbc-slice` (take one invariant through specify, plan, build,
document until a test that creates the adversity proves it holds).

**Derived from the concept**, and each states which version it
derives from. A change to the concept asks whether these are still
right.

### 2.2 The stack practice — `delivery/spring-postgres/`

What one real Spring and Postgres project taught:
`infra-establish`, `infra-serve`, `cbc-bootstrap`.

**Not derived from the concept — checked against it.** These came
from practice, not from the idea, and the phrasing in their headers
says so. A project on another stack drops this group whole and
keeps the rest.

### 2.3 The container — `delivery/container/`

**How a project is kept, not how it is thought.** The records
(`PLAN`, `TODO`, `devlog`, `ARCHITECTURE`, `CHANGELOG`), the entry
file, the agent decisions log, four convention skills, one rules
file, the hygiene files.

None of it is CbC. A project with no correctness-by-construction in
it would still want most of this — which is why it is a group of
its own and not part of the method.

Among what it ships is a whole **work arrangement** for the run's
own agent — section 4.

### 2.4 What does not travel — `installs/`, `fills/`

- **`installs/`** — our procedures, for the person operating the
  delivery. How a run is seeded (`pure-seed.md`), how an update is
  staged and handed over (`bundle-update.md`). A run never sees
  these.
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

**Down — delivery.** Files, copied whole. The run records one hash
for the whole delivery in its own decisions log. That hash is a
commit of ours; the run stores it without being able to resolve it.

**Up — harvest.** No files move. We read the run's repository
directly and write what we learned into our own masters. A run
never pushes anything here.

*Intended, not yet true: that this asymmetry is written down
anywhere but here. Today it is spread across `delivery/README.md`,
`delivery/installs/bundle-update.md`, the `convention-lifecycle`
skill, and a rules file run 3 wrote for itself because ours did not
reach that far.*

## 3. The agent as maintainer

**The maintainer of the concept, the delivery, and the records that
hold both.**

It keeps the concept's statement true, derives the method from it,
holds the master of every file any run receives, delivers to runs,
and reads runs back to learn what to change here.

It is not a builder. There is nothing here to build.

What it is made of is a **work arrangement**, which is section 4 —
the one it runs under is described there as 4.1.

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

Entry file: *"A concept repo... Documents only — no code, no
runs."* Four convention skills — `commit-messages`, `commit-plan`,
`convention-lifecycle`, `visual-comparison`. No rules.

The work it arranges: hold masters, decide, record, deliver,
harvest.

### 4.2 A run's — a builder's

Shipped in `delivery/container/`, so it is something we write and
they receive.

Entry file: `docs/concept/` and the method skills are **pinned
copies**, and until the framing artifacts exist the only method
work is running `cbc-framing` jointly with the human. The same four
convention skills. One rule, `shapes-lifecycle`. And beside them
the records the arrangement refers to.

The work it arranges: build a real system, keep its records, take
deliveries.

### 4.3 What the difference explains

**Nearly identical, and that is the trap.** The four skills are the
same files. The records table has the same shape. The agent/project
commit split is the same rule.

What differs is the *job*, and therefore which parts ever fire.
`convention-lifecycle` is the **receiver's** protocol — how a
project takes a newer copy without losing its own edits. A run uses
it constantly: eight takes recorded, three receipt branches, four
in-place edits. This repo has no deliverer, so it has never fired
here at all.

Reading a shared file and assuming a shared job is how a rule ends
up held in the repo it cannot apply to.

*Contradiction, stated rather than resolved: the entry file we ship
says the method skills are "never edited in place — a change is a
new copy from the source". Run 3 has edited `cbc-slice` in place
three times, we took every edit into our masters, and on 2026-09-17
we adopted the seven rules run 3 wrote to govern such edits. We
never shipped those rules. A project born today gets the
prohibition and nothing else.*

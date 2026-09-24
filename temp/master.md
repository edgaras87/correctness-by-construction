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

**One concept, the work derived from it, and the agent that keeps
both true.**

Nothing is built here. No application, no service, no run — this
repo holds documents and hands them to projects that do build.

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

## 2. The delivery — `delivery/`

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

**What the agent is in this repo: the maintainer of the concept,
the delivery, and the records that hold both.**

It keeps the concept's statement true, derives the method from it,
holds the master of every file any run receives, delivers to runs,
and reads runs back to learn what to change here.

It is not a builder. There is nothing here to build.

What it is made of is a **work arrangement** — an entry file, a set
of conventions, rules, and a decisions log — which is the next
section, because there are two of them and the difference is the
part worth writing down.

## 4. Work arrangements — two of them

**The same machinery, in both repos, doing two different jobs.** In
each it is `CLAUDE.md`, `.claude/skills/`, `.claude/rules/` and
`.claude/decisions.md`.

**Here, the arrangement is a maintainer's.** Its entry file opens:
*"A concept repo... Documents only — no code, no runs."* The work
is holding masters, deciding, recording, delivering, harvesting.

**In a run, the arrangement is a builder's.** It ships inside the
container, so it is something we write and they receive. Its entry
file says the opposite thing about the same files: `docs/concept/`
and the method skills are *pinned copies*, and until the framing
artifacts exist the only method work is running `cbc-framing`
jointly with the human.

The same four convention skills sit in both — `commit-messages`,
`commit-plan`, `convention-lifecycle`, `visual-comparison` — but
they are not equally ours. `convention-lifecycle` is the
**receiver's** protocol: how a project takes a newer copy without
losing its own edits. A run uses it constantly. This repo has no
deliverer, so it has never fired here.

*Contradiction, stated rather than resolved: the entry file we ship
says the method skills are "never edited in place — a change is a
new copy from the source". Run 3 has edited `cbc-slice` in place
three times, we took every edit into our masters, and on 2026-09-17
we adopted the seven rules run 3 wrote to govern such edits. We
never shipped those rules. A project born today gets the
prohibition and nothing else.*

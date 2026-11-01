# Tiers Model

A structured description of how the workspace's repos relate: three
tiers, the top one empty today, each answering a different question,
with delivery flowing down and learning flowing up. Its job is to
answer, for any lesson or file, *which repo does this belong
to* — instead of each session re-deriving the picture.

A draft: revised when the Concept Garden earns machinery (§2.2, *Concept Repos*).

This is an Idea Model: the top Canonical Description of its chain. It binds
what stands on it. When the two disagree, either side may be
the wrong one (`docs/models/idea-to-output.md` §3.3, *Settling a disagreement*).

---

## 1. A drawing of the tiers

In the drawing, "conventions, container, models" are the
conventions, the Container Group and the Idea Models; a Concept
Repo's "mental layer" is its Canonical Descriptions, and its
"container and execution copies" are what is made usable from them.

```
(no repo)     how you work      method: conventions, container, models —
                                held by the Concept Repo below until
                                three repos have lived (ADR-0038)
concepts      what you know     one repo per concept: mental layer,
   │ container and execution        ▲ harvest: a Run Repo's surprises
   ▼ copies, pinned at a commit     │ become concept changes
runs          what you try      projects, experiments
```

## 2. The tiers

### 2.1 The empty top tier

The top tier is empty: today the Concept Repo holds the method its
Run Repos are born with, as its own. A second Concept Repo that
needs the method copies parts. A third does the same. Only after
three is a repo above them considered, from what the three lived.
Until then the upward flows end at the Concept Repo.

A repo that owned the working arrangement was built once, ahead of
its evidence, and is history (ADR-0038). It held how projects are
recorded, how conventions are written and delivered, and what an
agent is.

### 2.2 Concept Repos

A **Concept Repo** is one repo per concept. It keeps the full records
any project keeps, derived from the manuals (ADR-0042). It holds two
layers:

1. Its Canonical Descriptions: the plain-words statement of the idea,
   its rationale, its open questions, and the log of what changed it
   and why.
2. What is made usable from them: Agent Skills, checklists,
   templates, birth materials for projects that follow the concept.

Each states which concept version it derives from. No Run Repo's
work is done here.

The **Concept Garden** is whatever holds the Concept Repos together.
It is a plain folder with no records, no arrangement, and no agent of
its own, until something exists that belongs to no single concept. The
trigger is concrete: the second Concept Repo, and the first rule
written twice. This Idea Model, which maps the Concept Garden, moves there then.

### 2.3 Run Repos

A **Run Repo** is where a concept meets reality: a project or experiment that
took what a Concept Repo made usable and a Container Group copy, pinned to the versions it
took. A Run Repo's records are its own. What it learns about *the
concept* does not stay in the Run Repo: it is harvested.

## 3. The flows

What moves between tiers, and in which direction. Five facts hold
on every flow (§3.5, *What holds on every flow*). How it moves is
each repo's own convention:
here, for example, the Exchange Convention (`docs/conventions/exchange/`).

### 3.1 Downward delivery

Down is delivery, in two forms:

1. a copy, always pinned at a commit of the tier above: that pin is
   what "a concept version" is;
2. a Delivery Fill: text written at birth into a file the Run Repo
   owns from then on. It is never re-copied. At the Run Repo's
   retrospective it is merged back by name into the playbook it came
   from. Here, for example, a playbook's Plan
Steps are written into a CBC Run's plan (`delivery/README.md` §2,
*Three ways a file lands*).

At a Run Repo's birth the two meet. Both are input to the Run Repo's
first decisions, which choose what to keep of them. Neither binds
it.

### 3.2 The Told Channel

The Told Channel is not delivery, and is unpinned by design
(`docs/models/agent.md` §4.4, *Told Channel*). A tier above may hand a
Run Repo a warning as session input, after the Run Repo's own work
has missed it and is on record. The Run Repo's records say it was
told. A Run Repo that leans on it has the Told Channel's diagnostic.
A copy the Run Repo has edited between two Delivery Pins is not a
form of delivery either (§3.5, *What holds on every flow*, fact 4):
delivery comes down, and an edit goes up.

### 3.3 Upward harvest

Up is harvest, and only through records: the tier above reads a
Run Repo's records, read-only, and the Run Repo sends nothing. A Run Repo's
surprise about the concept becomes a concept change, and what is
made usable is re-derived from it. A method lesson stops at the
Concept Repo while it holds the method. Work in one repo never edits
another as a side effect, up or down.

### 3.4 The Delivery Pin and documents

The Delivery Pin, the commit of the tier above that a delivery's
copies equal, follows the documents the tiers exchange.
No tier's agent reads a tier above it, so every delivery is a
document, and its Delivery Pin moves with it. A document taken
without its Delivery Pin moving leaves the Run Repo's record of what
it holds wrong. That is why the Delivery Pin moves with every
Delivery Take (§3.5, *What holds on every flow*; ADR-0036).

### 3.5 What holds on every flow

Five facts hold between a tier and the one below it. A design that
ignores one describes a different system.

1. **The tier below is blind.** It holds no address for the tier
   above, and cannot fetch (§3.4, *The Delivery Pin and documents*).
2. **Nothing arrives by itself.** Every delivery is decided above
   and carried across by a person, or by an agent on a person's
   word. Never automatic, never started below.
3. **Below holds copies; above holds Master Copies.** A copy changes only
   by being copied anew, or by the tier below editing it.
4. **A copy is edited when it fails.** The tier below edits its copy
   where the copy did not foresee what happened. That is where
   learning starts, and the edit is read from above as the diff.
5. **Nothing moves up as files.** The tier above reads; the tier
   below never sends (§3.3, *Upward harvest*).

And one number, the Delivery Pin: the commit of the tier above that a
delivery's copies equal, kept by the tier below. One Delivery Pin for a
delivery, never one per part, so the tier below cannot hold two
answers to what it was given.

*Its story: ADR-0071; devlog 2026-09-26; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 4. What the Idea Model answers

### 4.1 Where a lesson lands

- **About how to work:** the tier above, which today is the Concept
  Repo that holds the method.
- **About what is true of a concept:** that concept's repo, as a
  Record Harvest.
- **About this particular attempt:** the Run Repo's own records, and
  nowhere else unless harvested.

### 4.2 The dependency rule

Downward: only pinned copies and Delivery Fills. Upward: only
records. A repo lives in exactly one tier. A Concept Repo that keeps
its own records, and today its method, does the concepts tier's
work, not a Run Repo's.

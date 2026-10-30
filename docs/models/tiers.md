# Tiers Model

A draft: revised when the Concept Garden earns machinery (§2.2, *Concept Repos*).

A structured description of how the workspace's repos relate: three
tiers, the top one empty today, each answering a different question,
with delivery flowing down and learning flowing up. Its job is to
answer, for any lesson or artifact, *which repo does this belong
to* — instead of each session re-deriving the picture.

This is an **Idea Model**: the top Canonical Description of its chain. It binds
what stands on it, and when the two disagree, either side may be
the wrong one (`docs/models/idea-to-output.md` §3.3, *Settling a disagreement*).

---

## 1. The tiers, drawn

```
(no repo)     how you work      method: conventions, container, models —
                                held by the Concept Repo below until
                                three repos have lived (ADR-0038)
concepts      what you know     one repo per concept: mental layer,
   │ container and execution        ▲ harvest: a run's surprises
   ▼ copies, pinned at a commit     │ become concept changes
runs          what you try      projects, experiments
```

## 2. The tiers

### 2.1 The empty top tier

A repo that owns the working arrangement — how projects are
recorded, how conventions are authored and delivered, what an agent
is — was built once, ahead of its evidence, and is history
(ADR-0038). Today the Concept Repo holds the method its Run Repos are
born with, as its own. A second repo that needs it copies parts; a
third does the same; only after three is a repo above them
considered, from what the three lived. Until then the upward
channels end at the Concept Repo.

### 2.2 Concept Repos

A **Concept Repo**: one repo per concept, each keeping the full records any project
keeps, derived from the manuals (ADR-0042), and holding two layers:
its Canonical Descriptions (the plain-words statement of the idea, its
rationale, open questions, and the log of what changed it and why)
and what is Made Usable from them (agent skills, checklists,
templates, birth materials for projects that follow the concept),
each stating which concept version it derives from. Run Repos never
happen here.

The **Concept Garden** — whatever holds the Concept Repos together — is a
plain folder with no records, no arrangement, and no agent of its
own, until something exists that belongs to no single concept. The
trigger is concrete: the second Concept Repo, and the first rule
written twice. This Idea Model, which maps the Concept Garden, moves there then.

### 2.3 Run Repos

A **Run Repo** is where a concept meets reality: a project or experiment that
consumed what a Concept Repo Made Usable and a container copy, pinned to the versions it
took. A Run Repo's records are its own; what it learns about *the
concept* does not stay in the Run Repo — it is harvested.

## 3. The flows

What moves between tiers, and in which direction. Five facts hold
on every flow (§3.5, *What holds on every flow*). How it moves is
each repo's own convention:
here, for example, the Exchange Convention (`docs/conventions/exchange/`).

### 3.1 Downward delivery

Down is delivery, in two forms. A copy, always pinned at a commit of the tier above,
which is what "a concept version" is. And a Delivery Fill: text written at
birth into a file the Run Repo owns from then on, never re-copied
(here, for example, a playbook's Plan Steps written into a CBC Run's plan:
`delivery/README.md` §2, *Three ways a file lands*), and folded back by name at the Run Repo's retrospective, into
the playbook that seeded it. At a Run Birth the two
meet, both input to Framing rather than agreement.

### 3.2 The told channel

Told is not delivery. A tier above may hand a Run Repo something as session input — a warning the
Run Repo's own derivation missed, given after that derivation is on record,
as an experiment's instrument. That is the told channel, unpinned by
design (`docs/models/agent.md` §4.4, *told*), and the Run Repo's records say it was
told; it is not a third form of delivery, and a Run Repo that leans on it
has the diagnostic told carries. Nor is a copy the Run Repo has edited
between two Delivery Pins (§3.5, *What holds on every flow*, fact 4):
delivery comes down, and an edit goes up.

### 3.3 Upward harvest

Up is harvest, through records. Learning moves up only through records: the tier above reads a
Run Repo's records, read-only, and the Run Repo sends nothing. A Run Repo's
surprise about the concept becomes a concept change, and what is
Made Usable is re-derived from it; a method lesson stops at the
Concept Repo while it holds the method. Nothing edits an upstream
repo as a side effect of downstream work, in either direction.

### 3.4 The Delivery Pin and the talk

The Delivery Pin follows the talk. No tier's agent reads a tier above it, so every delivery is a
document, and its Delivery Pin moves with it. A document absorbed without
its Delivery Pin moving leaves the registry lying — lived once, and the
reason the Delivery Pin moves with every Delivery Take (§3.5, *What holds on every
flow*).

### 3.5 What holds on every flow

Five facts hold between a tier and the one below it. A design that
ignores one describes a different system.

1. **The tier below is blind.** It holds no address for the tier
   above, and cannot fetch (§3.4, *The Delivery Pin and the talk*).
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

And one number, **the Delivery Pin**: the commit of the tier above that a
delivery's copies equal, kept by the tier below. One Delivery Pin for a
delivery, never one per part, so the tier below cannot hold two
answers to what it was given.

*Its story: ADR-0071; devlog 2026-09-26; devlog 2026-10-29, the lessons' own stories: the other manuals and the tiers model.*

## 4. What the Idea Model answers

### 4.1 Where a lesson lands

About how to work → the tier above, which today is the Concept Repo
that holds the method. About what is true of a concept → that
concept's repo, as a Record Harvest. About this particular attempt → the
Run Repo's own records, and nowhere else unless harvested.

### 4.2 The dependency rule

Downward: only pinned copies. Upward: only records. A repo lives in
exactly one tier; a Concept Repo maintaining its own records, and
today its method, is tier-two work, and not a Run Repo.

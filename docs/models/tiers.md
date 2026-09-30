<!-- This repo's, edited as ours (ADR-0026, ADR-0043); where it
     came from is ADR-0038's record. -->

# Tiers Model

A draft: revised when the garden earns machinery (§2.2).

A structured description of how the workspace's repos relate: three
tiers, the top one empty today, each answering a different question,
with delivery flowing down and learning flowing up. Its job is to
answer, for any lesson or artifact, *which repo does this belong
to* — instead of each session re-deriving the picture.

This is a **model**: you could disagree with all of it and violate
nothing. It binds nothing.

---

## 1. The shape

```
(no repo)     how you work      method: conventions, container, models —
                                held by the concept repo below until
                                three repos have lived (ADR-0038)
concepts      what you know     one repo per concept: mental layer,
   │ container and execution        ▲ harvest: a run's surprises
   ▼ copies, pinned at a commit     │ become concept changes
runs          what you try      projects, experiments
```

## 2. The tiers

### 2.1 The top tier is empty

A repo that owns the working arrangement — how projects are
recorded, how conventions are authored and delivered, what an agent
is — was built once, ahead of its evidence, and is history
(ADR-0038). Today the concept repo holds the method its runs are
born with, as its own. A second repo that needs it copies parts; a
third does the same; only after three is a repo above them
considered, from what the three lived. Until then the upward
channels end at the concept repo.

### 2.2 Concepts

One repo per concept, each keeping the full records any project
keeps, derived from the manuals (ADR-0042), and holding two layers:
the **mental** layer (the plain-words statement of the idea, its
rationale, open questions, and the log of what changed it and why)
and the **executions** derived from it (agent skills, checklists,
templates, birth materials for projects that follow the concept),
each stating which concept version it derives from. Runs never
happen here.

The **garden** — whatever holds the concept repos together — is a
plain folder with no records, no arrangement, and no agent of its
own, until something exists that belongs to no single concept. The
trigger is concrete: the second concept repo, and the first rule
written twice. This model, which maps the garden, moves there then.

### 2.3 Runs

Where a concept meets reality: a project or experiment that
consumed executions and a container copy, pinned to the versions it
took. A run's records are its own; what it learns about *the
concept* does not stay in the run — it is harvested.

## 3. The flows

What moves between tiers, and in which direction. How it moves —
the note, the pin, the read — is `ARCHITECTURE.md` §2.5 and
`docs/conventions/exchange/`.

### 3.1 Down is delivery

Two forms. A copy, always pinned at a commit of the tier above,
which is what "a concept version" is. And a fill: what a run owns
from its birth on — the steps written into its plan, its entry
file, whatever the birth materials left for it to author — never
re-copied, and folded back by name at the run's retrospective, into
the playbook or the concept that seeded it. At a run's birth the two
meet, both input to Framing rather than agreement.

### 3.2 Told is not delivery

A tier above may hand a run something as session input — a warning
the run's own derivation missed, given after that derivation is on
record, as an experiment's instrument. That is the told channel,
unpinned by design (agent model §4.4), and the run's records say it
was told; it is not a third form of delivery, and a run that leans
on it has the diagnostic told carries. Nor is a copy the run has
edited between two pins (`docs/conventions/exchange/` §5): delivery
comes down, and an edit goes up.

### 3.3 Up is harvest, through records

Learning moves up only through records: the tier above reads a
run's records, read-only, and the run sends nothing. A run's
surprise about the concept becomes a concept change, and the
executions are re-derived from it; a method lesson stops at the
concept repo while it holds the method. Nothing edits an upstream
repo as a side effect of downstream work, in either direction.

### 3.4 The pin follows the talk

No tier's agent reads a tier above it, so every delivery is a
document, and its pin moves with it. A document absorbed without
its pin moving leaves the registry lying — lived once, and the
reason the pin moves with every take (`docs/conventions/exchange/`
§2).

## 4. What the model answers

### 4.1 Where does this lesson land?

About how to work → the tier above, which today is the concept repo
that holds the method. About what is true of a concept → that
concept's repo, as a harvest. About this particular attempt → the
run's own records, and nowhere else unless harvested.

### 4.2 What may depend on what?

Downward: only pinned copies. Upward: only records. A repo lives in
exactly one tier; a concept repo maintaining its own records, and
today its method, is tier-two work, and not a run.

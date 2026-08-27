<!-- Vendored copy — engineering-handbook models/tiers.md @ 4fe8083
     (copied 2026-08-27, same commit as this repo's kit birth pin).
     Pinned: do not edit here — changes happen in the handbook and
     arrive as a fresh pinned copy. See ADR-0002. -->

# Tiers Model

DRAFT (named from one worked instance — this handbook, one concept
repo being born, no runs yet; revise when the garden tier earns
machinery).

A structured description of how the workspace's repos relate: three
tiers, each answering a different question, with delivery flowing down
and learning flowing up. Its job is to answer, for any lesson or
artifact, *which repo does this belong to* — instead of each session
re-deriving the picture.

This is a **model**, not a convention (artifact-kinds: *could you
disagree with it and violate nothing?* — yes). It binds nothing.

---

## 1. The shape

```
handbook      how you work      method: conventions, kit, models
   │ kit copy, injection —          ▲ promotion: decisions.md queue,
   ▼ pinned at a commit             │ retrospectives, friction lists
concepts      what you know     one repo per concept: mental layer
   │ execution copies —             ▲ harvest: a run's surprises
   ▼ pinned at a concept version    │ become concept changes
runs          what you try      projects, experiments
```

## 2. The tiers

1. **Handbook** — the single owner of the working arrangement: how
   projects are recorded, how conventions are authored and delivered,
   what an agent is. Every repo in every tier consumes it through the
   kit and injection; nothing else owns method. A method lesson found
   anywhere lands here, and only through the upward channels.

2. **Concepts** — one repo per concept, each with the full recording
   machinery of any kit-born project, holding two layers: the
   **mental** layer (the plain-words statement of the idea, its
   rationale, open questions, and the log of what changed it and why)
   and the **executions** derived from it (agent skills, checklists,
   templates, birth materials for projects that follow the concept),
   each stating which concept version it derives from. Runs never
   happen here.

   The **garden** — whatever holds the concept repos together — is a
   plain folder with no records, no arrangement, and no agent of its
   own, until something exists that belongs to no single concept. The
   trigger is concrete: the second concept repo, and the first rule
   written twice.

3. **Runs** — where a concept meets reality: a project or experiment
   that consumed executions and a kit copy, pinned to the versions it
   took. A run's records are its own; what it learns about *the
   concept* does not stay in the run — it is harvested.

## 3. The flows

**Down is delivery.** Always a copy, always pinned — a kit copy at a
handbook commit, an execution at a concept version. At a repo's birth
the two deliveries meet: the kit births the container, a concept's
birth materials — a playbook, a startup snippet — birth the shape,
both pinned, both input to Framing rather than agreement (ADR-0024).
Nothing downstream tracks upstream by reference; how copies are made
and tracked is the convention-lifecycle's, not this model's.

**Up is harvest.** Learning moves only through records: a run's
surprise becomes a concept change (and the executions are re-derived
from the updated concept); a method lesson or arrangement experiment
anywhere rides the promotion queue (`.claude/decisions.md`, read at
retrospective) or a friction list back to the handbook. Nothing edits
an upstream repo as a side effect of downstream work.

## 4. What the model answers

*Where does this lesson land?* About how to work → handbook. About
what is true of a concept → that concept's repo, as a harvest. About
this particular attempt → the run's own records, and nowhere else
unless harvested.

*What may depend on what?* Downward: only pinned copies. Upward: only
records. A repo lives in exactly one tier; the handbook maintaining
itself is tier-one work, a concept repo maintaining its own records is
tier-two work, and neither is a run.

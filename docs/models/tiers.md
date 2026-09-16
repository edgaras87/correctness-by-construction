<!-- Vendored copy — engineering-handbook models/tiers.md @ ba7eaa4
     (copied 2026-09-17; before that @ ab916a1 2026-09-11, first
     copied 2026-08-27 @ 4fe8083, this repo's kit birth pin, and
     unchanged there through af16eb7). Pinned: do not edit here —
     changes happen in the handbook and arrive as a fresh pinned
     copy. See ADR-0002. -->

# Tiers Model

DRAFT (named 2026-08-25 from one worked instance — the handbook,
one concept repo being born, no runs; §3 revised 2026-09-10 from
five lived runs, on the concept repo's report. The garden tier is
still a folder; revise again when it earns machinery).

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

**Down is delivery, in two forms.** The first is a copy, always
pinned — a kit copy at a handbook commit, an execution at a
concept-repo commit, which is what "a concept version" is. The second
is a fill: what the run owns from its seed commit on — the steps
written into its plan, its entry file, whatever the birth materials
left for it to author — which is never re-copied and is folded back
by name at the retrospective, into the playbook or the concept that
seeded it. At a repo's birth the two meet: the kit births the
container, the concept's birth materials birth the shape, both
pinned, both input to Framing rather than agreement
(HANDBOOK ADR-0024). Nothing downstream tracks upstream by reference;
how copies are made and tracked is the convention-lifecycle's, not
this model's.

**Told is not delivery.** A tier above may hand a run something as
session input — a warning the run's own derivation missed, given
after that derivation is on record, as an experiment's instrument.
That is the told channel, unpinned by design (agent model §4), and
the run's records say it was told; it is not a third form of
delivery, and a run that leans on it has the diagnostic told
carries. Nor is a copy the run has edited between two pins
(convention-lifecycle §3): delivery comes down, and an edit goes up.

**Up is harvest, through records.** Learning moves only through
records, and the run sends nothing: the tier above reads the run's
records, read-only, at step boundaries during the run or whole at its
end; or the records travel as a handoff document, one repo's `temp/`
to another's. An edited copy's diff against its pin is one of those
records — the tier above reads it at the next update and answers in
its own text, never in the copy (HANDBOOK ADR-0038). A run's surprise
becomes a concept change (and the executions are re-derived from the
updated concept); a method lesson or arrangement experiment anywhere
reaches the handbook the same two ways — read at the retrospective
from the promotion queue (`.claude/decisions.md`), or carried in a
handoff. Nothing edits an upstream repo as a side effect of downstream
work, in either direction.

**Tiers talk in documents, and the pin follows the talk.** No tier's
agent reads another tier's repo: a run reads only its own, and a
concept repo opens a handbook checkout only for the lifecycle update
(convention-lifecycle §3). So every exchange is a document, and a
document absorbed without its pin moving leaves the registry lying —
the update procedure's own warning, lived once.

## 4. What the model answers

*Where does this lesson land?* About how to work → handbook. About
what is true of a concept → that concept's repo, as a harvest. About
this particular attempt → the run's own records, and nowhere else
unless harvested.

*What may depend on what?* Downward: only pinned copies. Upward: only
records. A repo lives in exactly one tier; the handbook maintaining
itself is tier-one work, a concept repo maintaining its own records is
tier-two work, and neither is a run.

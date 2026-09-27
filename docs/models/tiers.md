<!-- This repo's (ADR-0026); where it came from is ADR-0038's
     record. Edit when something lived here contradicts the text;
     the body is otherwise as taken. -->

# Tiers Model

DRAFT (named 2026-08-25 from one worked instance — the handbook,
one concept repo being born, no runs; §3 revised 2026-09-10 from
five lived runs, on the concept repo's report; §1, §2 and §4
revised 2026-09-27, the top tier emptied, CBC ADR-0038. The garden
tier is still a folder; revise again when it earns machinery).

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
                                three repos have lived (CBC ADR-0038)
concepts      what you know     one repo per concept: mental layer,
   │ container and execution        ▲ harvest: a run's surprises
   ▼ copies, pinned at a commit     │ become concept changes
runs          what you try      projects, experiments
```

## 2. The tiers

1. **The top tier is empty.** A repo that owns the working
   arrangement — how projects are recorded, how conventions are
   authored and delivered, what an agent is — was built once, ahead
   of its evidence, and is history (CBC ADR-0038). Today the concept
   repo holds the method its runs are born with, as its own. A
   second repo that needs it copies parts; a third does the same;
   only after three is a repo above them considered, from what the
   three lived. Until then the upward channels end at the concept
   repo.

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
pinned — the container and the executions, at a concept-repo
commit, which is what "a concept version" is. The second
is a fill: what the run owns from its seed commit on — the steps
written into its plan, its entry file, whatever the birth materials
left for it to author — which is never re-copied and is folded back
by name at the retrospective, into the playbook or the concept that
seeded it. At a repo's birth the two meet: the container and the
concept's birth materials, both pinned, both input to Framing
rather than agreement. Nothing downstream tracks upstream by
reference; how copies are made and tracked is the exchange's
(`docs/conventions/exchange/`), not this model's.

**Told is not delivery.** A tier above may hand a run something as
session input — a warning the run's own derivation missed, given
after that derivation is on record, as an experiment's instrument.
That is the told channel, unpinned by design (agent model §4), and
the run's records say it was told; it is not a third form of
delivery, and a run that leans on it has the diagnostic told
carries. Nor is a copy the run has edited between two pins
(the exchange, §5): delivery comes down, and an edit goes up.

**Up is harvest, through records.** Learning moves only through
records, and the run sends nothing: the tier above reads the run's
records, read-only, at step boundaries during the run or whole at its
end; or the records travel as a handoff document, one repo's `temp/`
to another's. An edited copy's diff against its pin is one of those
records — the tier above reads it at the next update and answers in
its own text, never in the copy (CBC ADR-0036). A run's surprise
becomes a concept change (and the executions are re-derived from the
updated concept); a method lesson or arrangement experiment anywhere
reaches the tier above the same two ways — read at the retrospective
from the promotion queue (`.claude/decisions.md`), or carried in a
handoff — and stops at the concept repo while it holds the method.
Nothing edits an upstream repo as a side effect of downstream work,
in either direction.

**Tiers talk in documents, and the pin follows the talk.** No tier's
agent reads a tier above it: a run reads only its own, and the
deliverer reads a run's repo read-only to harvest (the exchange,
§6). So every delivery is a document, and a
document absorbed without its pin moving leaves the registry lying —
the update procedure's own warning, lived once.

## 4. What the model answers

*Where does this lesson land?* About how to work → the tier above,
which today is the concept repo that holds the method. About
what is true of a concept → that concept's repo, as a harvest. About
this particular attempt → the run's own records, and nowhere else
unless harvested.

*What may depend on what?* Downward: only pinned copies. Upward: only
records. A repo lives in exactly one tier; a concept repo
maintaining its own records, and today its method, is tier-two
work, and not a run.

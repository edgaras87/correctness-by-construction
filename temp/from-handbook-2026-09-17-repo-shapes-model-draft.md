# Repo Shapes — model draft

DRAFT, 2026-09-16, from one design conversation. Not a record. Sits
in `temp/` until it is either folded into the tiers model or
discarded; substance belongs in TODO and the devlog either way.

Provenance: written after the handbook adopted its own kit
(HANDBOOK ADR-0041), when the question "what is a convention, now
that it is a directory and not a file" turned out to be a question
about what each repo in the workspace is for.

This is a **model**, not a convention (artifact-kinds: *could you
disagree with it and violate nothing?* — yes). It binds nothing.
Its job is to answer two questions without re-deriving them every
session: *what shape should this repo be*, and *does this thing
belong in it*.

---

## 1. Two dimensions, not one

The tiers model already cuts the workspace by **what a repo owns**:
method, a concept, or an attempt. That cut answers *where does this
lesson land*.

It does not answer *what shape should my repo be*. A second cut
does, by **how a repo operates**:

- A **maintainer** repo holds parts meant to be used by repos other
  than itself. Its output is reuse. It never solves a domain
  problem.
- A **spender** repo consumes those parts and spends them on one
  problem. Its output is the solved problem. It maintains nothing
  for anyone else.

The two dimensions are independent and both are always true. A repo
has a tier and a function.

```
                 owns (tier)          operates as (function)
handbook         method               maintainer
concept repo     a concept            maintainer
run / project    an attempt           spender
```

The handbook and a concept repo are the same shape. That is the
fact the tiers model states only in passing, and the one a concept
repo needs before it can be structured.

## 2. The three shapes

**The handbook** owns method: how work is recorded, how conventions
are authored and delivered, what an agent is. Everything it ships
is agent behaviour setup, in the sense the agent model gives the
word — a thing that arrives as files and changes how the agent
works, whether by instruction (a skill), by carrying its rule where
the action is (a stub's comments, HANDBOOK ADR-0004), or by shaping
what the agent can perceive at all (the hygiene base, the strongest
delivery available because nothing has to read it).

**A concept repo** owns a concept, and has two layers that must not
collapse into each other:

- The **mental layer**: the plain-words statement of the idea, its
  rationale, its open questions, and the log of what changed it.
  This is knowledge. It would still be true if no agent ever read
  it.
- The **executions**: skills, checklists, templates, birth
  materials, derived from the mental layer and each naming the
  concept version it derives from. This is agent behaviour, in the
  same sense as the handbook's.

A concept repo is therefore *a concept repo that also ships agent
behaviour*, never *an agent-behaviour repo that happens to keep
notes*. The direction matters: change the concept and the
executions are re-derived; change an execution with no concept
behind it and the drift has no source to correct against.

**A run** owns a problem. It is born with the kit, takes a concept's
bundle on top (kit first, bundle second — HANDBOOK ADR-0024), and
adapts both to what it actually needs. It maintains nothing for
anyone else. What it learns about the concept is harvested; what it
learns about method goes to the handbook; what is true of this
attempt alone stays in its own records and nowhere else.

## 3. What a maintainer repo is made of

The same three things, whichever maintainer repo it is.

**Buckets.** One directory per topic. Inside it, a manual and its
artifacts (HANDBOOK ADR-0040). The manual explains and never ships.
The artifacts instruct and do ship. The rules live in the
artifacts; the manual points at them and states none of them.

A bucket is not itself a document. In the handbook a bucket is a
convention; the convention is the agreement, and the directory is
where its manual and artifacts are kept. Compare artifact-kinds'
treatment of *concept*: an idea that lives inside documents and is
never a document kind itself.

**A delivered set.** The artifacts of every bucket, assembled into
one thing that is copied whole: the kit here, the bundle in a
concept repo. The set is the master of what it holds; the buckets
link into it (HANDBOOK ADR-0040). Only the set is copied. Anything
about the set stays beside it, not in it (HANDBOOK ADR-0016).

**Bases, not stubs.** What a receiver gets is complete and usable
as delivered, and designed to be extended locally — the shape
repo-hygiene already ships as a base with overlays appended, and
the shape a skill copy already has under the edit-between-pins rule
(HANDBOOK ADR-0038). This is deliberately *not* the word "stub":
artifact-kinds defines a stub as a document whose content is holes,
awaiting specifics, which the record stubs are and a skill file is
not.

## 4. What a spender repo does with them

It adapts. A run holds copies at a pin and may edit them between
pins, from lived work only, in a form any project would want
(HANDBOOK ADR-0038). What this project alone needs never goes into
a copy; it goes into the project's own records.

The distinction that makes this workable is the one in §1. A
maintainer asks *does this serve any project in my domain*. A
spender asks *does this solve my problem*. The same sentence can be
right for one and wrong for the other.

## 5. The tests this gives you

**Does this belong in my repo?** Does it serve any project in my
domain, or only one? Only one, and it belongs to that project.

**Manual or artifact?** Would a person changing or judging this
need it — manual. Does an agent need it at the moment of work —
artifact. A manual that states a rule has taken the artifact's job.

**Method or concept?** About how work is done at all — the
handbook. About what is true of the domain — the concept repo's
mental layer. Behaviour derived from that truth — the concept
repo's executions.

**Maintainer or spender?** If you are writing it so that a future
repo can use it, you are maintaining. If you are writing it to get
this problem solved, you are spending. A repo doing both at once
has a boundary problem.

## 6. What this model is not

**The handbook is not a tool-configuration repo.** The agent model
is deliberately vendor-neutral, and one tool's mechanisms are a
separate binding. Reading `conventions/` as "agent behaviour" makes
room for hooks, permissions and settings files to drift in. They
are a binding, not method.

**Recording is not fundamentally about agents.** The record
conventions exist so a project has memory. An agent maintaining
them is the current mechanism, not the purpose; the practices
predate agents and are cited from outside. Agent behaviour is how
the handbook delivers them, not what they are.

**A concept repo's mental layer is not agent behaviour.** §2.

**This does not replace the tiers model.** It adds the second
dimension of §1. Tiers still answers where a lesson lands, which
this says nothing about.

## 7. Status and what would refute it

Unobserved. One maintainer repo has this shape by construction, and
it is the repo that wrote the model. A second, a concept repo,
has not been restructured yet.

What would refute it:

- A concept repo restructured this way finds the bucket shape does
  not fit executions, because an execution's manual has nothing to
  say that the mental layer does not already say. That would mean
  the split is a property of conventions, not of maintainer repos.
- A run turns out to need a manual for a convention it holds,
  which would mean the manual's "never ships" is wrong and the
  reader axis is not the right cut.
- The maintainer/spender line turns out to be a spectrum rather
  than a boundary, with a long-lived run maintaining parts for its
  own future selves.

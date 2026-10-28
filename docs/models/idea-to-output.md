# Idea-to-Output Model

A draft: written from one full chain, the agent's, and checked
against the concept's and a record's.

A structured description of the kinds of text this repo holds, how
each links to the others, and the two directions text moves: down
from an idea to what work produces, and up from work to a new idea.
Its job is to answer, for any text, *what kind is this, and what
does it stand on* — instead of each session re-deriving the picture.

This is a **model**: the top description of its chain. It binds
what stands on it, and when the two disagree, either side may be
the wrong one (§3.3, *A disagreement is settled*).

---

## 1. The chain

```
  model ──► description ──► approach ──► output
            (a manual,      (a skill,      ▲
             the concept)    a rule,       │ governs, at the gate
                             a form)     shape ◄── written from outputs
```

Read left to right, it is the idea-to-output chain: each kind is
written from the one before it. A chain may start below a model:
most manuals stand on none.

## 2. The kinds

| Kind | What it is | Here |
|---|---|---|
| model | an idea any repo can adapt; its rules vary by repo, like an interface | `docs/models/`: agent, tiers, this one |
| description | how one thing is understood today, written down | a convention's manual; the concept, `concept/` |
| approach | how a piece of work is done | a skill, a rule, an approach on trial, a record's form in its header comment |
| output | what the work produces | a record's entries, a run's slices and code |
| shape | a presumed output, written from outputs that exist | `.claude/shapes/`, read only at the gate |

A shape is not a step after the approach. It is written from
outputs, and governs the next one; written from the approach, it
would describe intent, as a template does.

## 3. The links

### 3.1 The four links

| Link | From, the lower text | To, the upper text |
|---|---|---|
| stands on | a file | what the whole of it was written from |
| points | a line | the home of a fact it relies on: the one place that fact is written |
| governs | an output | the shape it is checked against, at the gate |
| written from | an output or approach | the kind written from it (§4.2, *Up, work to an idea*) |

A file stands on one thing; a line may point at a fact's home in
any document at its own level or above (§3.2, *Every link points
up*).

An approach stands on a description, never on a model directly.

### 3.2 Every link points up

A lower text relies on an upper one; an upper text at most lists
what stands on it.

A line that relies on a fact points at its home at its own level or
above, never below. Sideways is a fact whose home sits beside the
line. A line that only names or lists a text, such as the record a
description is about or what stands on it, may name any level:
naming is not a link.

A reference down is placed upward. Where the lower text holds an
idea general enough, the idea is written into the upper text in
general words, and the lower text stands on it. Where it holds only
one repo's specifics, the upper text says one general line. A marked
example, which the claim does not rest on, may stay (ADR-0071).

### 3.3 A disagreement is settled

When two linked texts disagree, the disagreement is settled, never
left standing. Either may be the wrong one: the upper binds the
lower, but being upper doesn't make it right. It ends when the two
agree again, by changing the lower, the upper, or both.

## 4. The two directions

### 4.1 Down, an idea to an output

A model is adapted by a manual; the manual is made usable as
skills, rules and forms; work done with them leaves outputs. Each
stands on the one above.

### 4.2 Up, work to an idea

New things are born the other way:

```
unfamiliar work ──► approach on trial ──► convention ──► model
outputs ──► shape
```

- **An approach on trial** comes from work no approach covers.
- **A convention** comes from approaches whose rules hold across
  projects.
- **A model** comes from a convention whose idea is general enough
  to be used elsewhere. Here, for example, the tiers model took the
  exchange's general facts on 2026-10-28, by an approach still on
  trial, `.claude/approaches-on-trial/model-placing.md`; the models
  before this one came from the handbook.
- **A shape** comes from outputs that exist.

So a new text finds its foundation by looking up this path for the
description whose idea it applies. Where none states it, the text is
first-time work, and the step up writes the description it will
stand on.

The steps between repos, a run's lesson reaching the deliverer, are the tiers model's
(`docs/models/tiers.md` §3, *The flows*).

### 4.3 After a birth

The lower text is rewritten to stand on the new one. A skill
drafted as an approach on trial is rewritten from the convention
written out of it. A manual whose idea became a model stands on
that model. Birth goes up; afterwards, reliance goes up too.

## 5. A model and a concept

Both sit at the top of a chain. They differ in where things vary:

- **A model's rules vary by repo.** Each repo adapts it in its own
  manual.
- **A concept has one form and one home.** It is copied whole, and
  only its outputs vary. A run edits its copy only from a mistake
  lived, and the edit goes home.

No model sits above correctness by construction. What a concept is
waits for a second concept repo.

## 6. A convention

### 6.1 Two texts

A convention is a way of working written down once, as two texts
kept apart:

- **its manual,** a description: what the way of working is, how
  it works and why, with the decisions behind it. Written for a
  person, and for whoever keeps the convention.
- **its artifacts,** the approaches made from the manual: the
  skills, rules and forms a project acts on. They state the rules,
  one sentence each, and explain nothing.

A project holds the artifacts. The manual stays with whoever keeps
the convention.

### 6.2 What a convention asserts

That its rules are rules, not a method the work must follow: the
work may ignore one, with a reason it can give. That freedom is the
worker's, in one case, and the reason is written where that
project's records live.

What falsifies it: a project ignores a convention, gives no reason,
and comes to no harm. That convention is one nobody owes anything
to: a method filed in the wrong place.

## 7. One chain here

Each file names what it stands on, so the chains are not listed
here. The agent's is the worked example. The agent model stands
above agent-arrangement, which stands above the entry file's guard
and the decisions log's header; their content is the output. Each
manual's *Why it arrives this way* points at the part of the agent
model it reasons from.

## 8. What it does not answer

- **Which repo a text belongs to** — `docs/models/tiers.md`.
- **How a text reaches an agent** — `docs/models/agent.md`.
- **How a link is written and checked, and a disagreement found
  and decided** — this repo's conventions, not this model.

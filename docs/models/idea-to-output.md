# Idea-to-Output Model

A draft: written from one full chain, the agent's, and checked
against the concept's and a record's.

A structured description of the kinds of text this repo holds, how
each links to the others, and the two directions text moves: down
from an idea to what work produces, and up from work to a new idea.
Its job is to answer, for any text, *what kind is this, and what
does it stand on* — instead of each session re-deriving the picture.

This is an **Idea Model**: the top Canonical Description of its chain. It binds
what stands on it, and when the two disagree, either side may be
the wrong one (§3.3, *Settling a disagreement*).

---

## 1. The chain

```
  model ──► description ──► approach ──► output
            (a manual,      (a skill,      ▲
             the concept)    a rule,       │ governs, at the gate
                             a form)     shape ◄── written from outputs
```

Read left to right, it is the idea-to-output chain: each kind is
written from the one before it. A chain may start below an Idea Model:
most manuals stand on none.

## 2. The kinds

| Kind | What it is | Here |
|---|---|---|
| Idea Model | an idea any repo can adapt; its rules vary by repo, like an interface | `docs/models/`: agent, tiers, this one |
| Canonical Description | how one thing is understood today, written down | a convention's manual; the concept, `concept/` |
| Work Approach | how a piece of work is done | a skill, an Agent Rule, an Approach on Trial, a record's form in its header comment |
| output | what the work produces | a record's entries, a CBC Run's slices and code |
| Output Shape | a presumed output, written from outputs that exist | `.claude/shapes/`, read only at the gate |

An Output Shape is not a step after the Work Approach. It is written from
outputs, and governs the next one; written from the Work Approach, it
would describe intent, as a template does.

## 3. The Chain Links

### 3.1 The four Chain Links

| Link | From, the lower text | To, the upper text |
|---|---|---|
| stands on | a file | what the whole of it was written from |
| points | a line | the home of a fact it relies on: the one place that fact is written |
| governs | an output | the Output Shape it is checked against, at the gate |
| written from | an output or Work Approach | the kind written from it (§4.2, *Up, work to an idea*) |

A file stands on one thing; a line may point at a fact's home in
any document at its own level or above (§3.2, *The direction of a
link*).

A Work Approach stands on a Canonical Description, never on an Idea Model directly.

### 3.2 The direction of a link

A lower text relies on an upper one; an upper text at most lists
what stands on it.

A line that relies on a fact points at its home at its own level or
above, never below. Sideways is a fact whose home sits beside the
line. A line that only names or lists a text, such as the record a
Canonical Description is about or what stands on it, may name any level:
naming is not a link.

A reference down is placed upward. Where the lower text holds an
idea general enough, the idea is written into the upper text in
general words, and the lower text stands on it. Where it holds only
one repo's specifics, the upper text says one general line. A marked
example, which the claim does not rest on, may stay (ADR-0071).

### 3.3 Settling a disagreement

When two linked texts disagree, the disagreement is settled, never
left standing. Either may be the wrong one: the upper binds the
lower, but being upper doesn't make it right. It ends when the two
agree again, by changing the lower, the upper, or both.

## 4. The two directions

### 4.1 Down, an idea to an output

An Idea Model is adapted by a manual; the manual is made usable as
skills, Agent Rules and forms; work done with them leaves outputs. Each
stands on the one above.

### 4.2 Up, work to an idea

New things are born the other way:

```
unfamiliar work ──► Approach on Trial ──► convention ──► model
outputs ──► shape
```

- **An Approach on Trial** comes from work no Work Approach covers.
- **A convention** comes from Work Approaches whose rules hold across
  projects.
- **An Idea Model** comes from a convention whose idea is general enough
  to be used elsewhere. Here, for example, the Tiers Model took the
  Exchange Convention's general facts on 2026-10-28, by an Approach still on
  Trial, `.claude/approaches-on-trial/model-placing.md`; the Idea Models
  before this one came from the handbook.
- **An Output Shape** comes from outputs that exist.

So a new text finds its foundation by looking up this path for the
Canonical Description whose idea it applies. Where none states it, the text is
first-time work, and the step up writes the Canonical Description it will
stand on.

The steps between repos, a CBC Run's lesson reaching the Concept Deliverer, are the Tiers Model's
(`docs/models/tiers.md` §3, *The flows*).

### 4.3 After a birth

The lower text is rewritten to stand on the new one. A skill
drafted as an Approach on Trial is rewritten from the convention
written out of it. A manual whose idea became an Idea Model stands on
it. Birth goes up; afterwards, reliance goes up too.

## 5. An Idea Model and a concept

Both sit at the top of a chain. They differ in where things vary:

- **An Idea Model's rules vary by repo.** Each repo adapts it in its own
  manual.
- **A concept has one form and one home.** It is copied whole, and
  only its outputs vary. A CBC Run edits its copy only from a mistake
  lived, and the edit goes home.

No Idea Model sits above correctness by construction. What a concept is
waits for a second Concept Repo.

## 6. A convention

### 6.1 Two texts

A convention is a way of working written down once, as two texts
kept apart:

- **its manual,** a Canonical Description: what the way of working is, how
  it works and why, with the decisions behind it. Written for a
  person, and for whoever keeps the convention.
- **its artifacts,** the Work Approaches made from the manual: the
  skills, Agent Rules and forms a project acts on. They state the rules,
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
here. The agent's is the worked example. The Agent Model stands
above `agent-arrangement`, which stands above the entry file's guard
and the Decisions Log's header; their content is the output. Each
manual's *Why it arrives this way* points at the part of the Agent
Model it reasons from.

## 8. What it does not answer

- **Which repo a text belongs to** — `docs/models/tiers.md`.
- **How a text reaches an agent** — `docs/models/agent.md`.
- **How a link is written and checked, and a disagreement found
  and decided** — this repo's conventions, not this Idea Model.

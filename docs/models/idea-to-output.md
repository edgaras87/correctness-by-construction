# Idea-to-Output Model

A structured description of the kinds of text this repo holds, how
each links to the others, and the two directions text moves: down
from an idea to what work produces, and up from work to a new idea.
Its job is to answer, for any text, *what kind is this, and what
does it stand on* — instead of each session re-deriving the picture.

A draft: written from one full chain, the Agent Model's (§7, *One
chain here*), and checked against the concept's and one record's.

This is an Idea Model: the top Canonical Description of its chain. It binds
what stands on it. When the two disagree, either side may be
the wrong one (§3.3, *Settling a disagreement*).

---

## 1. The chain

```
  Idea Model ──► Canonical Description ──► Work Approach ──► output
                 (a manual,                (an Agent Skill,     ▲
                  the concept)              an Agent Rule,      │ governs, at the
                                            an Output Form)     │ Plan Step Gate
                                                           Output Shape ◄── written from outputs
```

Read left to right, it is the idea-to-output chain: each kind is
written from the one before it. A chain may start below an Idea Model:
8 of the 12 manuals stand on none (2026-11-01).

## 2. The kinds

| Kind | What it is | Here |
|---|---|---|
| Idea Model | an idea any repo can adapt; its rules vary by repo, like an interface | `docs/models/`: the Tiers Model, this one |
| Canonical Description | how one thing is understood today, written down | a convention's manual; the concept, `concept/` |
| Work Approach | how a piece of work is done | an Agent Skill, an Agent Rule, an Approach on Trial, an Output Form |
| output | what the work produces | a record's entries, a CBC Run's Invariant Slices and code |
| Output Shape | a presumed output, written from outputs that exist | a CBC Run's `.claude/shapes/`, read only at a Plan Step Gate |

An **Output Form** is how one output is written, read while it is
written, such as a record's header comment.

An Output Shape is not a step after the Work Approach. It is written from
outputs and governs the next one. Written from the Work Approach, it
would describe intent, as a template does.

## 3. The Chain Links

### 3.1 The four Chain Links

| Link | From, the lower text | To, the upper text |
|---|---|---|
| stands on | a file | what the whole of it was written from |
| points | a line | the home of a fact it relies on: the one place that fact is written |
| governs | an output | the Output Shape it is checked against, at a Plan Step Gate |
| written from | an output or Work Approach | the kind written from it (`knowledge/backbone-ideas/change.md` §4, *The arrows*) |

A file stands on one thing; a line may point at a fact's home in
any document at its own level or above
(`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*).

A placed Work Approach stands on a Canonical Description, never on an
Idea Model directly. An Approach on Trial stands on none yet
(`knowledge/backbone-ideas/change.md` §4, *The arrows*).

### 3.2 The direction of a link

Which way a link points is the layers document's
(`knowledge/backbone-ideas/layers-of-knowledge.md` §3, *The layers*).

### 3.3 Settling a disagreement

When two linked texts disagree, the disagreement is settled, never
left standing. Either may be the wrong one: the upper binds the
lower, but being upper doesn't make it right. It ends when the two
agree again, by changing the lower, the upper, or both.

## 4. The two directions

How a text is written from the one above it, and how new knowledge
goes up, is Change's (`knowledge/backbone-ideas/change.md` §3, *How
the layers fill*, and §4, *The arrows*).

## 5. An Idea Model and a concept

Both sit at the top of a chain. They differ in where things vary:

- **An Idea Model's rules vary by repo.** Each repo adapts it in its own
  manual.
- **A concept has one form and one home.** It is copied whole, and
  only its outputs vary. A project edits its copy of a concept only
  from a mistake it met, and the concept's repo reads the edit.

No Idea Model sits above correctness by construction. An Idea Model
of what a concept is waits for a second Concept Repo.

## 6. A convention

### 6.1 The manual's level

A convention is the Canonical Description of a way of working: its
manual. The manual says what the way of working is, how it works and
why, with the decisions behind it. It is written for a person, and
for whoever keeps the convention.

The Work Approaches made from it sit one level down, as for any
Canonical Description (§2, *The kinds*): the Agent Skills, Agent Rules
and Output Forms a project acts on. They state the rules, one
sentence each, and explain nothing. Each names the manual in its
Foundation Line.

### 6.2 What a convention asserts

That its rules are rules, not a method the work must follow: the
work may ignore one, with a reason it can give. The worker may use
that freedom one case at a time, and writes the reason in that
project's records.

What falsifies it: a project ignores a convention, gives no reason,
and comes to no harm. Then the convention asked for nothing a
project needs: it is a method filed in the wrong place.

### 6.3 A convention and the concept

Both are Canonical Descriptions with Work Approaches below them. They
differ in four things:

| | A convention | The concept |
|---|---|---|
| Its description | stays with whoever keeps the convention | copied whole into each project born from it (§5, *An Idea Model and a concept*) |
| What a project holds | the Work Approaches only | the description, and the Work Approaches made from it |
| What it asserts | rules: the work may break one, with a reason it gives (§6.2, *What a convention asserts*) | a method the work follows; a project edits its copy only from a mistake lived (§5, *An Idea Model and a concept*) |
| A version | none (ADR-0039) | versioned as a whole (ADR-0039) |

A project holds no convention, only the Work Approaches made from one.

## 7. One chain here

Each file names what it stands on, so the chains are not listed
here. The Agent Model was deleted on 2026-11-27, its last state in
git at `703ff7ca`, and this chain is told as it stood then. The Agent Model's chain is the worked example. The Agent Model stands
above the agent-arrangement manual. That manual stands above the
Entry File's guard, the comment in it that says what the file must
not become, and the Decisions Log's header. What the Entry File and
the Decisions Log hold is the output. Each
manual's *Why it arrives this way* points at the part of the Agent
Model it reasons from.

## 8. What it does not answer

- **Which repo a text belongs to** — `docs/models/tiers.md`.
- **How a text reaches an agent** — `knowledge/backbone-ideas/how-an-agent-works.md`.
- **How a link is written and checked, and a disagreement found
  and decided** — `docs/conventions/facts-in-sync/`, not this Idea Model.

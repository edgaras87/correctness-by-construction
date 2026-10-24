# Idea-to-Output Model

A draft: written from one full chain, the agent's, and checked
against the others named in §6.

A structured description of the kinds of text this repo holds, how
each links to the others, and the two directions text moves: down
from an idea to what work produces, and up from work to a new idea.
Its job is to answer, for any text, *what kind is this, and what
does it stand on* — instead of each session re-deriving the picture.

This is a **model**: the top description of its chain. It binds
what stands on it, and when the two disagree, either side may be
the wrong one (`.claude/rules/foundation-check.md`, step 5).

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

| Link | From, to | Written as | Upkeep |
|---|---|---|---|
| stands on | a file, to what the whole of it was written from | its one `foundation` line | the foundation check, at each commit |
| points | a line, to a part of any document | a path and section, a tag | the walk re-reads the line when the part changes |
| governs | a shape, to an output | the shape's path, read at the gate | a difference ends one of four ways |
| written from | an output or approach, to the kind above it | the evaluation or reading that moved it | the up direction, §4 |
| requires | a skill, to another convention it delegates to | the skill's `requires` line | none yet |

**One root, tags for parts.** A file names one `foundation`: in
frontmatter, or in a record's header comment. Every line that uses
a part of any document, its root included, carries a tag. The root
tells the foundation check which document to open; a tag tells the
walk which line to re-read. A second root in one file is a tag.

No link runs from a model straight to an approach. An approach
stands on a description. The trigger for such a link: an approach
whose rules no convention could hold.

## 4. The two directions

**Down, an idea to an output.** A model is adapted by a manual;
the manual is made usable as skills, rules and forms; work done
with them leaves outputs. Each step names the one above in its
`foundation`.

**Up, work to an idea.** New things are born the other way:

```
unfamiliar work ──► approach on trial ──► convention ──► model
outputs ──► shape
```

- **An approach on trial** is drafted for work no approach covers,
  and evaluated after use.
- **A convention** is written when an evaluation finds its rules
  hold across projects.
- **A model** is written when the idea behind a convention is
  general enough to be used elsewhere. Not yet lived: both models
  before this one came from the handbook (ADR-0038).
- **A shape** is written from outputs that exist, and changes when
  they show it wrong.

The steps between repos, a run's lesson reaching the deliverer, are
`docs/models/tiers.md` §3.

## 5. A model and a concept

Both sit at the top of a chain. They differ in where things vary:

- **A model's rules vary by repo.** Each repo adapts it in its own
  manual.
- **A concept has one form and one home.** It is copied whole, and
  only its outputs vary. A run edits its copy only from a mistake
  lived, and the edit goes home.

No model sits above correctness by construction. What a concept is
waits for a second concept repo.

## 6. The chains here

- **The agent's.** The agent model stands above agent-arrangement,
  which stands above the entry file's guard and the decisions log's
  header; their content is the output. Each manual's *Why it
  arrives this way* tags the part of the agent model it reasons
  from.
- **The concept's.** The chapters under `concept/` stand on
  nothing. The method's skills stand on `concept v1`, and the
  method's shapes on `practice, under the shapes convention`. A
  run's slices and code are the output, and the shapes govern them.
- **A record's.** project-recording stands above a record's form in
  its header comment, named by its `foundation:` line. The entries
  are the output.

## 7. What it does not answer

- **Which repo a text belongs to** — `docs/models/tiers.md`.
- **How a text reaches an agent** — `docs/models/agent.md`.
- **The rules for writing a `foundation` line or a tag** —
  `docs/conventions/conventions/` §2 and §3.5.

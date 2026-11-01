---
paths:
  - ".claude/shapes/**"
foundation: the shapes convention
---

# Output Shapes

An **Output Shape** says what a kind of output looks like in this project:
its form, never its content. It opens with one line naming what it
covers:

> **Governs:** how `<which parts>` of `<which artifact>` are
> written. Their form, never their content.

A Plan Step finds the Output Shapes that apply to its work by that line. A file
without it is not an Output Shape. An Output Shape says nothing about when it is
written or changed. That is this file's.

## 1. Written from work that exists

An Output Shape is written from outputs that already exist: a pair that
recurred, or one piece worth keeping. Never from an idea of how the
work should go. If no Output Shape covers what a Plan Step made, its Plan Step Gate checks
nothing for it.

Before an Output Shape is written, its examples are read side by side, with
two questions:

- **Where do they differ?** Each difference ends as one form for
  all, a variant the Output Shape names and allows, or a better form
  neither example had.
- **What could they all do better?** Read against the project's
  rules and decisions, and what went wrong. A weakness every
  example shares never shows up by comparing them. Example: twenty
  entries that all lack a worked example with numbers.

The reviewer settles what this reading finds; anything the writer adds
beyond it is named as theirs. Then the Output Shape is tried on the
examples it came from, and on an earlier version where a miss is
known. An Output Shape catches a part that is missing, not a part that kept
its place but lost half its meaning: only reading the output itself shows that.

## 2. Where an Output Shape lives

Every Output Shape lives in `.claude/shapes/`. Nothing loads it while the
work is written. It is read at the Plan Step Gate, when the Plan Step
closes.

Why: work written without the Output Shape in view can show that it
is wrong, or that a new one is needed. What must hold while the work
is written is not an Output Shape. It belongs to the Agent Skill or the Agent Rule that
runs the work.

## 3. A difference at the close

At the Plan Step Gate, what the Plan Step made is read against every
Output Shape that governs it. The comparison is by judgment, not by text: does the output
have the parts the Output Shape names, in its order, reading as it says?
Each difference is named, with the line from the output and the
line from the Output Shape. It ends one of four ways, judged one
difference at a time. Any change it leads to, in the output or in
the Output Shape, is shown before it is made, never applied silently:

- **The output drifted.** The Output Shape stands; the output is brought
  to it.
- **The Output Shape was wrong here.** The output stands; the Output Shape
  changes: a project's own with a dated line, a delivered one under
  the delivered-copies Agent Rule.
- **Each had something.** The Output Shape takes what the output found,
  and the output is brought to the changed Output Shape.
- **The output is a different kind.** Both stand, and a new Output Shape
  starts from the output (§1, *Written from work that exists*). Either of the last three can name
  new work (§4, *An Output Shape naming work*).

Outputs closed before a change are not reopened.

## 4. An Output Shape naming work

An Output Shape mostly names form: the order of parts, how they read. Some
parts need work done during the Plan Step. Example: a Structural Wall
Backstop "seen at the Red Run" can only be known by looking during
the Red Run.

When an Output Shape is written or changed so that it names such a part,
the Agent Skill that runs the work is checked. If the Agent Skill does not ask
for that part, it is changed too, under the delivered-copies Agent Rule.
Otherwise the Plan Step Gate finds the part missing when it is too late to
produce, and the work must be redone.

## 5. Offering an Output Shape back

An Output Shape this project wrote reaches the Concept Deliverer when a CBC Run Ask under
TODO's *To the deliverer* offers it. The Concept Deliverer reads it at its
next CBC Run Reading. An Output Shape marks what any project would want (its
skeleton) apart from this project's example (its illustration), so
the Concept Deliverer can take one and leave the other. How an edit reaches
the Concept Deliverer is the delivered-copies Agent Rule's.

## 6. What this does not govern

The Plan Step Gate items themselves, and how a Plan Step carries them.

---

## Decisions

- ADR-0035 — written in CBC Run 3 from its own lived work
  and taken here reshaped: the holder is named as the Concept Deliverer,
  which the CBC Run's `delivered-copies.md` names, and the role-name it
  arrived under is not adopted
- ADR-0037 — shapes are a convention; this Agent Rule derives from its
  manual, keeps the definition because a CBC Run cannot open the manual,
  and says that an Output Shape states form and never its lifecycle
- ADR-0052 — one place, read at the Plan Step Gate; Output Shapes travel as
  copies; the look before an Output Shape is written; four endings; an Output Shape
  that names work is asked for by its Agent Skill

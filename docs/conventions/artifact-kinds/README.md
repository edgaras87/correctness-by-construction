# Artifact kinds

A shared vocabulary for the kinds of documents we make: convention,
model, guide, playbook, plan, and a few more. It exists so that the
one word settled early in a conversation, "draft a guide", "this
needs a playbook", means the same thing to everyone, humans and
agents alike.

**What ships:** [`SKILL.md`](SKILL.md), which a project holds at
`.claude/skills/artifact-kinds/` and an agent opens when a
document's kind has to be named. This page explains it; the skill
states it.

## What it is

Nine kinds, each located by two questions and anchored by an
exemplar. *Force*: does the document describe, advise, bind or
execute? *Reuse*: is it a template copied per instance, or the
instance itself carrying live state? A third question, whether it
is studied once or consulted repeatedly, helps when shaping one.
The definitions are prototypes: a document that does not fit
cleanly is a finding, not a violation, and a hybrid is named by its
dominant force. A convention's reference document is such a hybrid,
reference doc in shape and convention in force.

This convention is a metamodel, a convention about what conventions
and their sibling kinds are. A context may specialise a kind: in
the handbook, a convention is a manual and its artifacts under
`conventions/<name>/`.

## Why it is shaped this way

- **Own words, stolen axes.** The force axis comes from the
  governance hierarchy (policy, standard, guideline, procedure) and
  RFC 2119; reader mode from Diátaxis. Their word lists were not
  imported: we formalise the words actually spoken here, DDD's
  ubiquitous language, and use the frameworks only as definition
  machinery (ADR-0009).
- **Loose definitions on purpose.** Prototype theory is why loose
  definitions survive edge cases and strict membership criteria do
  not.
- **Exemplars by role, not by path.** Each exemplar names its
  document by the role it holds for the reader, so the same words
  point at the right file from the handbook's seat and from a born
  project's, where some roles are empty. They are illustration, not
  dependency (ADR-0017, ADR-0037).

## An open question

No run in five reached for these words. Whether the convention
earns its place in the kit, and whether the axes need a third
reader-mode value and a lifetime axis, are Step 10 gate items in
the handbook's plan. Until then the skill ships as it is.

## Where to look

- The rules: [`SKILL.md`](SKILL.md).
- The frameworks named above: governance document hierarchies,
  RFC 2119, Diátaxis (Procida), DDD's ubiquitous language.

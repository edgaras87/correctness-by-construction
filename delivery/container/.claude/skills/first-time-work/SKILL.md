---
name: first-time-work
description: Start work that nothing yet says how to do, from a provisional manual the work corrects, and end it in a lasting form or none. Use when a step or a piece of work opens and no skill, and no earlier step or run, says how to do it; a PLAN step's opening items ask this. Do NOT use for work a skill covers, even a skill with a gap (edit that copy instead). A new skill for such work is written at this skill's close, never first.
requires: commit-messages
foundation: the first-time-work convention
---

# First-time work

A skill written before the work describes a guess. So the work
starts from a provisional manual, the work corrects it, and at the
close the manual becomes what lasts.

The reviewer decides. The agent finds the ways, writes the manual,
keeps it true, and proposes the lasting form.

## 0. Is it first-time work?

Ask both before anything else:

1. **Is it new, or a gap in a skill this project holds?** A gap is
   an edit to that copy, under `.claude/rules/delivered-copies.md`
   rule 2. Stop here.
2. **Is it general, or only this project's?** Say which. Only this
   project's, it still goes on below, but nothing is offered at the
   close.

## 1. Open

1. **The reviewer says what the work should do or be.**
2. **Find the ways it could be done,** and recommend one. The
   reviewer chooses. Keep the others, each with the reviewer's
   reason, for the decisions log at the close.
3. **Write the manual** at `.claude/<name>/manual.md`, `<name>` the
   kind of work in a word or two. It holds:
   - what the work is for;
   - its stages, in order;
   - what is not known yet.
4. **If the work is a PLAN step,** its Notes list the same stages,
   and its gate is written now, as the step form says.

## 2. Work

- **When the work shows the manual wrong, change the manual first,**
  then go on. The manual is always what is being done now.
- **Each change to the manual is its own commit.** Its body says
  what the work taught, and names the commit where the work showed
  it. The manual is an agent file and the work a project file, so
  the two never share a commit.

## 3. Close

1. **Propose the lasting form,** with the reason. The reviewer
   chooses:
   - a skill, for a procedure bound to a moment:
     `.claude/skills/<name>/SKILL.md`;
   - a rule, for what is true at a path or in every session:
     `.claude/rules/<name>.md`;
   - a shape, for the form of one kind of output:
     `.claude/shapes/<name>.md`;
   - a section of a record, for a fact, not a procedure;
   - nothing, when nothing in it is worth keeping: the work will
     not come again, or what it taught already lives elsewhere.
2. **Look back first:** read the manual's history, one commit per
   lesson, against what the work did. Then write the lasting form
   from both, plainly. What the work never did does not go in.
3. **Delete the manual** and its folder. History keeps it.
4. **One decisions-log entry:** what was made, why that form, and
   the ways rejected at the opening.
5. **If it is general,** one line under TODO's *To the deliverer*
   offers it, naming its path.

## When the way fails

Drop the manual. The devlog says why, as a dead end. Then ask the
reviewer whether to start again from a new way.

---

## Decisions

- CBC ADR-0056 — first-time work starts from a provisional manual,
  taken from never-oversold's way of working

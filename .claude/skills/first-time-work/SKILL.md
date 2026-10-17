---
name: first-time-work
description: Start work here that nothing yet says how to do, from a provisional manual written where manuals live and marked on trial, and end it in a lasting form or none. Use when a step opens, or a work item inside one, or a small TODO item comes due, and no skill, rule or earlier work here says how to do it; a step's opening items in PLAN.md ask this. Do NOT use for work a skill covers, even one with a gap (edit it instead). A new skill is written at this skill's close, never first.
foundation: the first-time-work convention
---

# First-time work

A skill written before the work describes a guess. So the work
starts from a provisional manual, the work corrects it, and at the
close the manual becomes what lasts.

The reviewer decides. The agent finds the ways, writes the manual,
keeps it true, and proposes the lasting form.

## 0. Is it first-time work?

1. **Is it new, or a gap in a skill or rule we hold?** A gap is an
   edit to that file. Stop here.
2. **Will a run do it too, or only this repo?** Only this repo, its
   trial is our own next use. A run too, its trial is the first
   run's reading after it ships.

## 1. Open

1. **The reviewer says what the work should do or be.**
2. **Find the ways it could be done,** and recommend one. The
   reviewer chooses. Keep the others, each with the reviewer's
   reason, for the ADR.
3. **Write the manual where it will live:** a convention's
   `docs/conventions/<name>/README.md`, in the manual form, or a
   concept chapter. Its *What it is for* marks it *on trial*, with
   what would make it evidence and when to look again. It holds the
   work's stages in order, and what is not known yet. Nothing is
   drafted elsewhere first.

## 2. Work

- **When the work shows the manual wrong, change the manual first,**
  then go on.
- **Each change to the manual is its own commit.** Its body says
  what the work taught, and names the commit where the work showed
  it.

## 3. Close

1. **Look back first:** read the manual's history, one commit per
   lesson, against what the work did.
2. **Propose the lasting form,** with the reason. The reviewer
   chooses:
   - the manual stays, its *on trial* mark rewritten from what was
     seen, and what derives from it is written: a skill of ours
     under `.claude/skills/`, a rule, or a shipped artifact in
     `delivery/`, as `docs/conventions/conventions/` §4 lists;
   - a section of a manual or record we keep, for a fact, not a
     procedure;
   - nothing, when nothing in it is worth keeping: the manual goes,
     and the devlog says why.
3. **An ADR** for the choice, with the ways rejected at the opening.

## When the way fails

Drop the manual. The devlog says why, as a dead end. Then ask the
reviewer whether to start again from a new way.

---

## Decisions

- ADR-0056 — first-time work starts from a provisional manual; ours
  sits where manuals live, on trial
- ADR-0057 — it opens at a step too, as a run's does

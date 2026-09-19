# Option comparison

A choice is settled by building every option and looking at it,
judged against requirements written down first. The unit is the
choice; the constraint is that each option can be made real cheaply
enough to look at.

**What ships:** [`SKILL.md`](SKILL.md), which a project holds at
`.claude/skills/option-comparison/` and an agent opens when more
than one option could work and the argument has become about taste.
This page explains it; the skill states it.

## What it is

A method for replacing a table of opinions with a table of
verdicts. Requirements are written before any candidate exists, so
they cannot be shaped to fit the favourite; every candidate is
built, including the one expected to lose; each is judged against
each requirement with the reason named.

What it is *not* is a way of choosing between things you cannot
build. That boundary is the whole of its scope, and it is why
"should we ship this to runs" is out — there are no two futures to
render and compare, so the method would degrade into the argument
it exists to replace.

It began as a method for one kind of question and was separated
from one on 2026-09-19. The specialised half,
[`../visual-comparison/`](../visual-comparison/), keeps the part
that only applies to things you look at. What is here is the spine.

## Why it is shaped this way

- **Requirements before candidates, always, and stated so a
  candidate can fail one.** A requirement written after the
  candidates is a description of the winner. The order is the only
  thing standing between this method and a justification.

- **Every candidate is built, including the ones expected to
  lose.** Three of the four runs so far changed a verdict that
  reasoning had already reached. The losers are where the findings
  come from: what a shape *cannot express* is invisible until it
  exists.

- **A verdict reached by reasoning is marked a prediction until
  something is built.** Not a formality — it is the difference
  between a comparison and a rationalisation, and the mark is what
  lets a later reader tell which one they are holding.

- **Buildability is the scope, not the subject.** The constraint
  was originally written as *a question of form*, which excluded a
  structure question this repo had already settled by building —
  the `stack/` quarantine of CBC ADR-0029, built, looked at, and
  found wrong. The subject was never the point; the ability to make
  candidates real was.

- **The findings list is things to check, not rules to obey**, and
  each entry names the case it came from. The danger is specific: a
  lesson from one comparison hardening into a boundary that stops
  the next from reaching a correct answer. An entry that cannot
  name its case is not an entry.

## An open question

Whether the split from `visual-comparison` earns two artifacts. CBC
ADR-0030 decision 10 names what would say it did not: if the
specialised half never gains a finding from a comparison whose
winner was *not* a picture, the split was decoration and the two
merge back.

## Where to look

- The rule: [`SKILL.md`](SKILL.md).
- The specialised half: [`../visual-comparison/`](../visual-comparison/).
- What routes here: [`../decide-first/`](../decide-first/), though
  the question arrives from wherever it arrives.
- The decisions: CBC ADR-0027, CBC ADR-0028, CBC ADR-0030.

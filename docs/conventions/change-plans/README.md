# Change plans

How work larger than one commit is planned before it starts,
reviewed at every commit boundary, and closed with a note of what
diverged. The unit is the change set: the scope between one commit
and a whole project.

**What ships:** [`SKILL.md`](SKILL.md), which a project holds at
`.claude/skills/change-plans/` and an agent opens when work turns
out to need several commits. This page explains it; the skill
states it.

## What it is

A patch series, carried into a repo where work is committed
directly instead of mailed: one logical change per commit, ordered
so each applies on the last, reviewed commit by commit rather than
as a lump. What is added is the plan agreed before the series is
written, and its disposal afterwards. The plan is one file at the
repo root, `CHANGE-PLAN.md`, committed after it is agreed and
deleted at the close; everything durable in it survives as the
commit messages it produced, and the close commit's body is the
cheapest retrospective that exists.

Two ideas carry the rest. **Steps are split by change, not by
file**, and the test is revert: undo one step and the repo must
still make sense. **Order follows where the decision lives**: a
decision settled in conversation is recorded first and implemented
second; a decision only visible in the material is found by
touching the material, with the durable record written from what
held. The second kind makes the tail of a plan provisional, and the
plan says so.

## Why it is shaped this way

- **Its own convention, and not a record.** It is a scaffold, not a
  record: nothing about it is meant to be read a year later except
  through `git log`, so it sits outside project-recording, whose
  records are all append-or-evolve (ADR-0010).
- **Root placement.** An in-flight change set is visible from a
  clean clone, so "is work half-landed, and where did it stop?" is
  answerable without the working tree (ADR-0010).
- **No status in the file.** Tracking status there couples every
  work commit to a plan edit and reintroduces the staleness that
  makes a neglected plan lie. Git history is the status.
- **Material-first is a first-class mode, not a failure.** The CbC
  seed's third run found four shapes in staged material that no
  conversation could have settled first; ADR-0027 made the
  provisional tail, the revision commit and the Proposed-then-
  Accepted ADR the normal road for it.
- **The records steps are planned.** A change set batches record
  moments, and a record's trigger can fire mid-set before its truth
  exists. Walking the entry file's records table while drafting the
  commit list is what catches it (ADR-0025).
- **The stop at every boundary is commit-messages' rule.** It was
  stated here first, in §6, a file that opens only for multi-commit
  work, and the reviewer's pace had to be said every session; the
  sentence moved to commit-messages, which opens at every commit,
  and this convention points at it (ADR-0035).

## Where to look

- The rules: [`SKILL.md`](SKILL.md).
- The commit boundary and the `agent` scope:
  [`../commit-messages/`](../commit-messages/).
- The records table the plan is walked against:
  [`../project-recording/`](../project-recording/).

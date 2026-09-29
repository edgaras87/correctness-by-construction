# Commit plan

**How work larger than one commit is sequenced into commits before
it starts, reviewed at every commit boundary, and closed with a
note of what diverged. The unit is the change set: the scope
between one commit and a whole project.**

## What it is for

So that a change set can be inspected commit
by commit before it lands, and a divergence at step *k* forces the
remaining steps to be re-evaluated rather than continued on a
plan that no longer holds. Adopted with the container (CBC
ADR-0038, 1b): the failure it answered was lived elsewhere — a
commit sequence kept by hand in a scratch file across four
sessions, fitting no record — and is not ours to restate. Lived
here since: every set since 2026-08-27 has run under it, and on
2026-09-27 and 28 one set was revised four times at its boundaries
on the reviewer's readings, each revision on its own commit — the
failure it guards against, doing otherwise than the plan and
fixing it afterwards or not at all, has not happened here.

## What this is made usable as

- **`delivery/container/.claude/skills/commit-plan/SKILL.md` — the
  skill, shipped**, held at `.claude/skills/commit-plan/` and opened
  when work turns out to need several commits. The rules, one
  sentence each, with the decisions it rests on in its footer.
- **`.claude/skills/commit-plan/SKILL.md` — the deliverer's copy**,
  a copy of the container's (`docs/conventions/exchange/`
  §1).

This page explains; the skill states. What derives from this page
is that list. A change here walks it; a change forced in one of
them is checked back against this page.

## The seats

A run runs its change sets under the skill, the plan file at its
root its own. The deliverer runs its change sets under the same
skill, the plan file at its root its own.

## 1. What it is

A patch series, carried into a repo where work is committed
directly instead of mailed: one logical change per commit, ordered
so each applies on the last, reviewed commit by commit rather than
as a lump. What is added is the plan agreed before the series is
written, and its disposal afterwards. The plan is one file at the
repo root, `COMMIT-PLAN.md`, committed after it is agreed and
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

## 2. Why it is shaped this way

- **Its own convention, and not a record.** It is a scaffold, not a
  record: nothing about it is meant to be read a year later except
  through `git log`, so it sits outside
  `docs/conventions/project-recording/`, whose records are all
  append-or-evolve (CBC ADR-0038, 1b).
- **Root placement.** An in-flight change set is visible from a
  clean clone, so "is work half-landed, and where did it stop?" is
  answerable without the working tree.
- **No status in the file.** Tracking status there couples every
  work commit to a plan edit and reintroduces the staleness that
  makes a neglected plan lie. Git history is the status.
- **Material-first is a first-class mode, not a failure.** The CbC
  seed's third run found four shapes in staged material that no
  conversation could have settled first, which made the
  provisional tail, the revision commit and the Proposed-then-
  Accepted ADR the normal road for it (CBC ADR-0038, 1e).
- **The records steps are planned.** A change set batches record
  moments, and a record's trigger can fire mid-set before its truth
  exists. Walking the entry file's records table while drafting the
  commit list is what catches it (CBC ADR-0038, 1d).
- **The stop at every boundary is commit-messages' rule**,
  `docs/conventions/commit-messages/`; this convention points at
  it. *Until 2026-09-08 the sentence was stated here, in §6, a file
  that opens only for multi-commit work, and the reviewer's pace
  had to be said every session; it moved to where every commit
  opens (CBC ADR-0038, 1f).*

## Why it arrives this way

A skill, because its moment is one the agent recognises — work
turning out to need several commits — and nothing in a record
would put the plan in front of it then. The one rule that must
fire at every commit, the stop, is not here: a skill that opens
only for multi-commit work cannot carry it, and it moved to
`docs/conventions/commit-messages/` for that reason (§2).

## What this does not cover

- **The commit boundary itself, and the `agent` scope** —
  `docs/conventions/commit-messages/`.
- **The records a plan is walked against, and what an ADR is** —
  `docs/conventions/project-recording/`.
- **The order of the work inside a plan** — the domain skill that
  knows the work; the index's chain, `docs/conventions/README.md`,
  says which.

## Where to look

- The commit boundary and the `agent` scope:
  `docs/conventions/commit-messages/`.
- The records table the plan is walked against:
  `docs/conventions/project-recording/`.

# Sketch — the order of work for one chain to a run

**Orientational only.** This is a sketch to think with, not a plan
of record and not a decision. `PLAN.md` holds the plan; ADRs hold
decisions; a change-plan holds a set. Nothing here binds any of
them, and a step below may turn out wrong the moment it is
started.

Written 2026-09-17 at the end of the session that stripped the
harvest notes out of the bundle, alongside
`draft-one-chain-to-a-run.md`, which holds the argument and the
evidence. This file holds only the order.

---

## The goal, in one picture

    now                     wanted
    handbook → run          handbook → cbc → run
    cbc      → run

A run has two upstreams and two pins. One chain instead.

---

## 1. Send the two documents already written

Both sit in `temp/`, both are finished, both are owed:

- `note-to-run-3-2026-09-17.md`
- `handoff-to-handbook-2026-09-17.md`

Nothing below should start first. They answer things that are
waiting, and they go stale.

## 2. Build the bundle's kit

The handbook's kit, adapted for a CbC project, held here.

Half of it exists already: `starter/fills/` is this, started and
never named as such — two of its files carry the kit's own text
verbatim with a re-verify duty attached.

Missing: the record stubs, the three hygiene files, the four
convention skills, and the PLAN frame the steps sit inside.

The largest step. Needs an ADR and a change set of its own.

## 3. Cut the cord in `pure-seed.md`

Today step 2 of the seed runs the handbook's install blocks in our
own shell, sharing variable names, at whatever commit their
checkout happens to be on, with no pin between us.

Once the bundle has a kit, that step is deleted and the birth is
written here.

This is the payoff: one delivery, one pin, no invisible dependency.

## 4. Tell the handbook

An observation, not a request. Four things:

- what we built, and why our runs now have one upstream
- what we found: their generic `ARCHITECTURE` stub says "list your
  invariants" and points at `src/` — our concept's vocabulary and
  an app repo's shape, in a kit meant for anyone
- the cost they are about to pay: runs are their only field data
  about the kit outside their own repo, and interposing removes it
- the constraint: whatever "pure" becomes later, ours should be
  derivable from it

## 5. Use it for a project or two

Then stop. Design nothing further until there is a second shape to
design from.

## 6. Purify upstream — only when a second shape needs it

The trigger is a project that wants the handbook's conventions and
is not a CbC project. Not a date.

Their own rule, applied back to them: do not guess a general form
from a single instance.

---

## What to decide before step 2

From the day the bundle has a kit, **every handbook update is
evaluated here twice** — once for this repo's agent, once for the
bundle's copy. That work starts immediately and does not stop.

Everything above assumes that is worth one chain to a run. If it is
not, the whole sketch fails at step 2 and the honest fallback is to
leave the two upstreams and write down why.

## What this sketch does not settle

- Where the bundle's kit physically lives, and what happens to
  `starter/fills/` when it is absorbed.
- Which CbC-flavoured slots move out of the handbook's stubs and
  into ours, beyond the `ARCHITECTURE` one already found.
- How run 3 migrates from two pins to one, and when.
- Whether one composed pin is honest, given it hides the kit hash
  inside it.

Each of those is a decision, and none of them is made here.

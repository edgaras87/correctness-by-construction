# 0061. A newborn reads its shapes at the gate, not at birth

Date: 2026-10-21
Status: Accepted (2026-10-21, inside the step that births run 5).

## Context

A shape is read at a step's closing gate, never while the work it
judges is written (`docs/conventions/shapes/` §3; ADR-0052). The
seed's prompt told every newborn to "read the whole repository
first, every file", and the method's shapes are among those files.
TODO held the question since 2026-10-17.

Run 4 answered it. Its birth commit `5485de9` copied
`kill.md`, `registry-entry.md` and `evidence-test.md`, whose
examples were then run 3's real work: kills 1, 9 and 20 and a whole
closed registry entry. Run 4 read them at birth, and wrote its
framing in 15 minutes, committed between 04:50 and 04:51; its
KILL-1 and KILL-5 match run 3's word for word, and its SLICE-4
entry is near verbatim. Its slices, judged by the shapes only at
their gates, tried walls on branches and rejected run 3's design.

## Options considered

- **Leave the prompt as it is,** and run 5's gate item says the
  shapes were read at birth. Rejected: run 4 shows what that costs,
  and a gate item cannot undo a read.
- **Remove the shapes from run 5's delivery.** Rejected by the
  reviewer: the shapes stay, read where they belong.
- **Strip every example from the delivery for run 5.** Rejected by
  the reviewer as too much work for one run; whether the concept,
  the conventions and the approaches keep examples is a question
  of its own.

## Decision

The seed's prompt keeps `.claude/shapes/` out of the newborn's
first read: "a shape is read at a step's closing gate, never before
the work it judges". The shapes are delivered as before.

## Consequences

- `delivery/installs/pure-seed.md`, step 6, says so; run 5 is the
  first newborn born under it.
- The worked examples in `cbc-framing` and `cbc-slice` are still
  read at birth. Run 5's hand-off asks its analysis to be visible
  instead: each probe committed before its verdict.
- Whether the shapes' examples should be the method's own rather
  than a run's is left to the question on examples.

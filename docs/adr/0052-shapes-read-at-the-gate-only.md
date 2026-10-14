# 0052. Shapes are read at the gate only, and travel as copies

Date: 2026-10-15
Status: Proposed (2026-10-15, under the commit plan for gate shapes)

## Context

ADR-0035 and ADR-0037 gave a shape two places, and the place was its
force. Exposed, under `.claude/rules/` with `paths:`, it loads while
the work is written and ships as a pinned copy. Unexposed, under
`.claude/shapes/`, nothing loads it and it is read at a gate; it is
in no birth copy, because it "would spend the only independence
there is", and reaches a run only staged in `temp/` for one gate, a
third act of the exchange named and never built. This repo holds no
shape of its own.

Run 3, never-oversold, lived both places and judged them at its
retrospective (its RETRO.md):

- **Its slice-record shape was read at the gate**, from SL-2's
  record, and revised three times, each from a real miss. A backstop
  that never held, named and not seen, taught "seen at the red run"
  or "unproven" (D12).
- **Its evidence-test shape was exposed from SL-3**, loading on
  every test file, after a lesson written in a record went unread
  while tests were written. SL-4's tests followed it (D13).
- **The `temp/` staging was never used**: looked in at two closes,
  nothing there (D18).
- **At Step 10 its reviewer moved every shape to the gate**: a test
  written without the shape in view can show the shape wrong, or a
  new kind. And what must hold while work is written is not a shape:
  it belongs to the skill or rule that runs the work. A part a shape
  names that only work can produce, a backstop seen at the red run,
  must therefore be asked for by the skill too (D18).
- **Two more shapes were written for framing's records**, a kill and
  a registry entry, each after a look at its examples for where they
  differ and what all of them lack. None of twenty kills had a
  worked example with numbers; a shape copied from them would never
  have asked for one (D29).
- **It asks that run 4 meet its shapes from the first slice**, not
  the third (D12, D13), and offers all four, each with its skeleton
  marked apart from its illustration. It names gate-only a trial for
  run 4 to judge at its second slice's close (D22).

Run 4 rebuilds never-oversold from the bundle. Run 3's illustrations
are its own answers to that problem.

## Options considered

- **Hold every shape back**, as ADR-0035 had it: run 4 gets none,
  and its first outputs are read against run 3's by this repo at a
  reading. Rejected: run 4 repeats run 3's misses for a measurement
  its own gate can take, and run 3's D12, D13 and D29 go unanswered.
- **Ship them as rules that load while writing.** Rejected: the
  first output of a kind is then written to the shape, and nothing
  shows what the method alone produces.
- **Ship them gate-only, as run 3 wrote them.** Rejected for the
  illustrations: run 4 would read run 3's slice records, numbers and
  classes for the problem it is about to solve.
- **Keep `temp/` staging for a later shape.** Rejected: never used on
  either side, and with shapes in the delivery there is nothing left
  for it to carry.

## Decision

1. **A shape is read at a step's closing gate and nowhere else.** In a
   run every shape lives in `.claude/shapes/`, and nothing loads it.
   What must hold while work is written belongs to the skill or rule
   that runs the work.
2. **Shapes travel as copies**, with the group of what they shape, at
   birth and at every delivery, under one pin with the skills and
   rules. Supersedes ADR-0035 decisions 3, 4 and 5, and ADR-0037
   decision 5: no exposed place ships, no unexposed stock is held
   apart, and nothing is staged in `temp/` for a gate.
3. **The rule takes run 3's lessons:** before a shape is written, its
   examples are read for where they differ and what they all lack,
   and it is tried on them; a difference at the gate ends one of four
   ways, the fourth a new shape; a shape that names work is asked for
   by the skill that runs it.
4. **The method ships run 3's four shapes, taken reshaped:** the
   slice record, the evidence test, the kill and the registry entry,
   each with run 3's skeleton, tags in full words, and an
   illustration from the worked example's order service.
5. **At the deliverer no shape is in use.** It has no steps and no
   gates; its rules with a Governs line are rules. Supersedes
   ADR-0037 decision 3.

## Consequences

- The shapes manual, the shipped `shapes-lifecycle.md` and
  `delivered-copies.md`, the exchange's §3.2 and §3.5,
  `exchange-deliver`, the run playbook and the method change.
- ADR-0035 decision 6 stands: trial evidence never ships. A shape is
  not trial evidence; it is withheld from view only until a gate.
- The measurement the evidence-test shape was held for moves into
  run 4: its first test, written without the shape in view, is read
  against it at its own gate. Nothing stops an agent from opening
  `.claude/shapes/` early; run 4's second slice close judges whether
  gate-only cost rework or taught something (group C).
- Run 3's `.claude/shapes/` sit at the paths the method now ships.
  Its next take lands ours over them, and its illustrations stay in
  its history; the note says so before anything is staged.

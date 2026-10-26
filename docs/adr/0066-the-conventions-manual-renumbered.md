# 0066. The conventions manual renumbered

Date: 2026-10-26
Status: Proposed (opened under the commit plan for layer 1's work).

## Context

ADR-0063 decision 7 gave round 2 of the refinement two moves out
of the conventions manual. The rules for keeping facts in sync went
to their own convention before round 2 read (ADR-0065). The other,
§1, what a convention is, was to go to the idea-to-output model.

ADR-0065 kept the manual's numbers. Its §3 then held §3.3, §3.4
and §3.7, with a gap where the moved sections had been.

Round 2's read found the manual's layout breaking its own rule,
that each numbered section holds one subject:

- §3.3, the form, told nine sections of a manual in one paragraph
  of 22 lines. Two had parts of their own, and two were missing
  (FINDING-136);
- §3.3 also held the channel, a shape's open question, how the form
  grows and two layout rules (FINDING-137);
- §2 held three subjects in unnumbered parts, and nine pointers
  landed on it for different ones (FINDING-138).

Which files carry a `foundation` line was told in conventions §2
and in `docs/conventions/facts-in-sync/` §4 step 2 (FINDING-141).

The reviewer chose on 2026-10-25 (the refinement's DECISION-9):
since moving §1 shifts every number anyway, renumber once.

## Options considered

- **Keep the gap, as ADR-0065 did.** Rejected: §3.3's parts still
  need numbers, and the gap would then sit beside a third level.
- **`### 3.3.1` and on, under §3.3.** Every pointer to §3.3 still
  lands. Rejected: a third level, under a number with a gap before
  it.
- **New numbers after §3.7, out of order.** Rejected: a reader
  meets the form's parts after the lesson taken.
- **Two conventions,** one for the artifact and one for the manual.
  Rejected: the `foundation` line ties the two halves, and a second
  manual adds its own frame.

## Decision

1. **What a convention is moves to the idea-to-output model:** a
   description, its manual, and the approaches made from it, its
   artifacts; and what a convention asserts, a rule and not a
   method (ADR-0031). What belongs to this repo stays in the
   manual: the manual's path, the kinds of artifact and where they
   live.
2. **The conventions manual stands on the model,** in frontmatter
   of its own, as a manual whose idea a model states.
3. **The manual is renumbered once,** with no gap and no third
   level:
   - §1 the artifact: 1.1 how a rule is written, 1.2 a skill's
     frontmatter, 1.3 the `foundation` line, 1.4 stages;
   - §2 the manual: 2.1 to 2.9, one part for each section of the
     form;
   - §3 adding a convention.

   ADR-0065 rejected a renumbering that changed no meaning. This
   one gives each part of the form a home.
4. **The `foundation` line has one home:** conventions §1.3 says
   which files carry it and what each holds. Facts-in-sync §4 step
   2 keeps what the line is for, and points there.

## Consequences

- Every living pointer into the manual moves, 28 of them, in the
  commit that renumbers it. History keeps the old numbers.
- The model gains a section, and its labelled parts are numbered.
- TODO's "Move conventions §1 to the idea-to-output model" closes.

# 0027. The architecture diagram is Mermaid, provisionally

Date: 2026-09-18
Status: Accepted, provisional — decision 2 names what reverts it

## Context

`ARCHITECTURE.md`'s diagram is hand-placed Unicode box art. It is
exact, it renders everywhere including a terminal diff, and every
character in it was positioned by counting. Changing it twice in
one evening — the container's label, then the removal of the
handbook's two arrows — cost three rounds of re-wrapping borders to
keep the box square. That is the whole case against it: not that it
reads badly, but that editing it is a chore paid every time, which
is a quiet argument for not editing it.

Against that, the file is a record that must not go stale, and this
repo's review surface is the diff.

The question was settled by rendering rather than by argument. A
draft in `temp/` stated what the picture must carry, and three
candidates were rendered against it:

1. three layers stacked **in derivation order** — the order is the
   meaning, not decoration;
2. all three **inside one boundary**;
3. two flows to the runs tier, **opposite directions**, each
   labelled;
4. the handbook **present and attached to nothing** — origin, not
   upstream, and not mistakable for a channel.

## Options considered

1. **Keep hand-placed ASCII.** Holds all four requirements exactly,
   because every character is placed on purpose. Rejected only on
   the editing cost, which is real and recurring.

2. **Keep ASCII, author it in AsciiFlow.** Removes the counting
   without changing the output or adding anything to the repo. Not
   rejected on merit — it stays the fallback in decision 2, because
   it is what we return to if Mermaid fails.

3. **Mermaid `block-beta`.** The dialect meant for stacked blocks,
   so it should have been the fit. Rendered and rejected on the
   evidence: it lost the arrow labels and did not hold the vertical
   order. Requirements 1 and 3 both failed.

4. **Mermaid flowchart with a subgraph.** Chosen. Rendered and
   held all four, with labelled arrows placed by the engine.

5. **D2.** The strongest layout engine of the four, and containers
   are its native model. Rejected on shape, not quality: it cannot
   live in a `.md`, so it means a source file, a generated image, a
   build step this repo does not have, and two artifacts that can
   silently disagree. A picture that can go quietly wrong is the
   exact failure this repo's manual-and-rule invariant exists to
   prevent.

## Decision

1. **`ARCHITECTURE.md`'s diagram is a Mermaid flowchart with a
   subgraph.** The ASCII goes; git history keeps it.

2. **It is provisional, and two things revert it.** First: if
   holding the four requirements ever needs the layout hand-nudged
   — direction hints, invisible links, spacer nodes — then we have
   traded counting characters for fighting a layout engine and
   gained nothing. Second: if a surface we actually read this file
   in shows source instead of a picture. On either, we return to
   option 2, ASCII authored in AsciiFlow, and this ADR is
   superseded rather than amended.

3. **It does not travel.** `starter/kit/ARCHITECTURE.md` keeps its
   ASCII placeholder. Provisional means the trial is ours to run; a
   run born from the kit must not inherit a renderer dependency we
   have not finished testing. The stub follows only if decision 2
   goes unfired long enough to stop calling this provisional — and
   that is a separate decision, because it is the one that reaches
   other repos.

4. **The other two ASCII diagrams stay.** `docs/models/agent.md` is
   taken verbatim (ADR-0026 decision 4), and
   `docs/conventions/project-recording/README.md` was not part of
   this question. Neither is touched by a trial of one file.

5. **The comparison is recorded, not adopted.** Writing down what a
   picture must carry, rendering candidates against it, and letting
   the render decide is a method that worked once. One instance is
   not a shape — this repo's own rule, and the one it applies to
   the handbook's work. The trigger for making it a convention is
   the second diagram whose format is in question; two instances
   can be compared, one can only be generalised from.

## Consequences

Good: the diagram can be edited without re-squaring a box, which
makes it likelier to stay true — the point of the change, since a
record nobody wants to edit is a record that goes stale. The four
requirements are now written down, so a future change to the
picture has something to fail against.

Bad: the diff no longer shows the picture, only the instructions
for it. Judged acceptable because this file is read in a preview
far more often than in a bare terminal, but it is a real loss and
decision 2's second clause exists because of it.

Also: one more format in the repo, and a dependency on a renderer
we do not control. Contained to one file by decision 3, which is
most of why the trial is affordable.

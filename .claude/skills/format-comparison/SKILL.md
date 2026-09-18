---
name: format-comparison
description: Settle a question of form — a diagram's dialect, a document's shape, a layout — by writing down what the artifact must carry and rendering candidates against it. Use when more than one form could work and the argument is about which.
---

# Format Comparison

A question of form is settled by rendering, not by argument. Write
what the artifact must carry *before* looking at candidates, build
each one, judge it line by line, and let the render decide.

Kind: playbook — copied into a fresh draft each time, never
executed in place.

## 1. When this fires

More than one form could work and the discussion has become about
taste. Typically: a diagram's dialect, the shape of a document, a
layout, a table against a picture.

It does not fire for a form with one obvious answer, and it does
not fire twice for the same question — the ADR from last time is
the answer.

## 2. The method

1. **Write the requirements first, in a `temp/` draft.** What the
   artifact must *carry*, not what it should look like. Each one
   stated so a candidate can fail it. Name the defect the artifact
   is answering, so a later reader can tell whether it was fixed.

2. **Write them as what a reader must get, not what a form must
   show.** A requirement phrased as "the picture shows X" has
   already decided that it is a picture. This matters whenever the
   candidate set includes a non-picture, and the set usually
   should.

3. **List the candidates, including the plain ones.** A numbered
   list and a table are candidates. So is the form you already
   have — leaving it in gives "nothing wins" somewhere to land.

4. **Build every candidate for real.** Not a sketch, not a
   description. The findings come from building.

5. **Render them where they will actually be read**, and judge
   pass or fail per requirement with the reason. A verdict reached
   by reasoning is a *prediction*; mark it as one until the render
   confirms it. Both times this method has run, the render changed
   a verdict that reasoning had got wrong.

6. **Decide, and record it in an ADR** — the requirements, the
   candidates, and why each lost. Then delete the draft; it has
   served, and git history keeps it.

## 3. Gates

- Every requirement is stated before any candidate is built.
- Every candidate is built and rendered, including the ones
  expected to lose.
- Every verdict cites the requirement it turns on.
- A verdict not yet rendered is marked as a prediction.
- The outcome is in an ADR before the draft is deleted.

## 4. What the render has caught

Kept because it is the evidence this method works, and because a
list that stops growing is the sign it was written too early.

- **The dialect built for the job can be the one that fails.**
  Mermaid `block-beta` is meant for stacked blocks and lost both
  the arrow labels and the vertical order. `sequenceDiagram` is
  meant for handoffs between actors and had to draw a read-only
  reading as an arrow into the other repo — asserting the opposite
  of the rule the procedure existed to keep. A picture that states
  the opposite of the truth is worse than no picture (ADR-0027,
  ADR-0028).

- **A requirement no candidate can hold is evidence about the
  requirement.** Struck, not failed — and say so in the ADR, so
  the next comparison starts from a corrected spec (ADR-0028).

- **Building is what finds the modelling error.** The two-subgraph
  flowchart could not place the operator, who works in both repos.
  The fix was not a third box but the recognition that the
  operator is transport, not a place (ADR-0028).

- **Using a dialect is not fighting it.** Ordinary syntax is
  ordinary. Invisible links, spacer nodes and nodes declared out
  of meaning order are the fight, and a candidate needing them has
  lost (ADR-0027 decision 2).

## 5. What this does not do

- It does not choose a format for another repo. This repo's
  Mermaid trial is provisional and does not travel (ADR-0027
  decision 3); a run decides its own forms.
- It does not run on a schedule, and it is not a review of forms
  already settled.

---

## Decisions

- CBC ADR-0027 — the comparison is a method that worked once;
  recorded, not adopted, with the second format question as the
  trigger for asking whether it becomes a rule
- CBC ADR-0028 — the trigger fired and was answered here. The
  recommendation was to wait for a third instance: two uses by one
  author in one week is thin evidence. If that objection was
  right, §4 is where it shows, by not growing

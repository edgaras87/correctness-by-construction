---
name: visual-comparison
description: Settle how a structure is shown: a picture, a table or a plain list. Write down what the reader must get, and render every candidate against it. Use when a diagram might be the answer, including deciding it should not be.
foundation: the visual-comparison convention
---

# Visual Comparison

How a structure is shown is settled by rendering, not by argument.
Write what the reader must get *before* looking at candidates.

The steps are:

1. requirements first;
2. every candidate built;
3. each judged per requirement;
4. the outcome recorded.

What sets the comparison apart is the
failure mode only a picture has: *a notation that asserts something
you did not mean*, and what that has cost.

Kind: an Agent Skill copied into a fresh draft each time, never
run in place.

## 1. When this fires

A structure is hard to see and more than one way of showing it
could work. A Mermaid dialect against another, a table against a
picture, a numbered list against both.

It does not fire for a form with one obvious answer, and it does
not fire twice for the same question — the record from last time
is the answer. An obvious answer means a clear one, not a simple
form: when what the work needs is already clear, the comparison does not
fire, however large the form.

## 2. The comparison's steps

Why they are so: (the Concept Deliverer's docs/conventions/visual-comparison/ §2.1, *A non-picture in the set*; §2.2, *Deciding by the render*; §2.4, *The buildable notations*).

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
   The set must contain at least one thing that is not a picture.
   Otherwise a picture wins by construction and the comparison
   cannot return *no picture*, which is a real answer.

4. **Build every candidate for real.** Not a sketch, not a
   description. The findings come from building. Where a project
   holds to plain text that renders on GitHub and in the IDE with no
   build step, the buildable notations are Mermaid and Unicode box
   drawing. PlantUML, Graphviz and D2 all need a render step or a
   plugin and are out; a committed SVG renders but is not text anyone
   can read in a diff.

5. **The reviewer renders them where they will actually be read**,
   and judges how each looks. The agent makes sure each candidate's
   syntax is valid, and marks its own verdicts on the look as
   predictions until the reviewer has seen them.

6. **Decide, and record it** where the Entry File's records table
   puts a decision of its kind — the requirements, the candidates,
   and why each lost. Then delete the draft; it has served, and git
   history keeps it.
   An outcome too small for an ADR is recorded in the body of the
   commit that places the winner, and the draft goes in that commit.
   The body names the commit that holds the draft
   (`.claude/skills/commit-messages/SKILL.md`, *Rules*).

## 3. The comparison's checks

- Every requirement is stated before any candidate is built.
- Every candidate is built, its syntax checked, and rendered by the
  reviewer, including the ones expected to lose.
- Every verdict cites the requirement it turns on.
- A verdict not yet rendered is marked as a prediction.
- The outcome is recorded before the draft is deleted.

## 4. What the render has caught

Kept because it is the evidence the comparison works, and because a
list that stops growing is the sign it was written too early.

**These are things to check, not rules to obey.** Each names the
case it came from, so you can judge whether yours is like it. An
entry that would give the wrong answer on a different real case is
too broad — narrow it to what was actually observed. If you cannot
name the case, it is not an entry yet.

- **The dialect built for the job can be the one that fails.**
  Mermaid `block-beta` is meant for stacked blocks and lost both
  the arrow labels and the vertical order. `sequenceDiagram` is
  meant for handoffs between actors and had to draw a read-only
  CBC Run Reading as an arrow into the other repo. That asserted the opposite
  of the rule the exchange existed to keep: a CBC Run Reading writes nothing in the CBC Run. A picture that states
  the opposite of the truth is worse than no picture.

- **A requirement no candidate can hold is evidence about the
  requirement.** Struck, not failed — and say so in the record, so
  the next comparison starts from a corrected spec.

- **Building is what finds the modelling error.** The two-subgraph
  flowchart could not place the reviewer, who works in both repos.
  The fix was not a third box: it showed the reviewer as what
  carries text between them, not as a place.

- **Asked for a picture, the comparison is not always what is wanted.**
  An Idea Model written in prose was asked for a diagram of it. The comparison
  was reached for, and most of it was not run:
  - no non-picture candidate;
  - requirements written after the first candidate was built;
  - no verdict settled by looking.

  What the work actually
  needed was to build one picture, ask what it was *for*, and build
  the second picture that question produced. The Agent Skill's own "it does not fire for a form with one obvious answer"
  (§1, *When this fires*) covers this, and was read as
  being about simple forms rather than about clear answers. Adding
  two pictures to one document is ordinary work; it earned no ADR,
  and writing one would have been ceremony over a comparison that
  did not happen.

- **Using a dialect is not fighting it** (the Concept Deliverer's docs/conventions/visual-comparison/ §2.3, *Fighting a notation*). Ordinary syntax is
  ordinary. Invisible links, spacer nodes and nodes declared out
  of meaning order are the fight, and a candidate needing them has
  lost.

## 5. What this does not do

- It does not choose a notation for this project. The Mermaid in
  its cases is the Concept Deliverer's provisional trial. It is
  not delivered. This project decides its own forms.
- It does not run on a schedule, and it is not a review of forms
  already settled.

---

## Decisions

- ADR-0027 — the comparison is a method that worked once;
  recorded, not adopted, with the second format question as the
  trigger for asking whether it becomes a rule
- ADR-0027, decision 2 — §4's "using a dialect is not fighting
  it": a candidate that needs the layout fought has lost
- ADR-0027, decision 3 — §5's Mermaid trial, provisional and not
  delivered
- ADR-0028 — the trigger fired; this Agent Skill is its answer, and §4
  growing or not is the test of the objection it records
- ADR-0030 — the general method separated out; §4's discipline
  line and §1's rule that the set holds a non-picture are from it

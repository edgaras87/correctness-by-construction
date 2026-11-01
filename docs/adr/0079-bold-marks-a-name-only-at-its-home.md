# 0079. Bold marks a Name only at its home

Date: 2026-11-01
Status: Proposed, opened under the commit plan for the rules' fix

## Context

Writing rule 9 says no Markdown mark marks a Name: every mark
already has a job here, and the capitals show a Name at every use
(ADR-0076). Refinement Round 3 found Names bold at the line that
defines them, in FINDING-405, 474, 494, 626, 639 and 722. The
reviewer chose, as the refinement's DECISION-22 on 2026-10-30, to
allow bold there and nowhere else. The decision said rule 9 would
gain the line at Refinement Round 3's close. It did not, and the
round's close read found the rule still bare.

Two more questions reached the last read's rule check:

- **A list item's bold lead.** Some list items open with a bold lead
  that begins with a Name, such as "**Catalog Check:**", in the Stack
  Group's Agent Skills and references. FINDING-1384 asked whether
  DECISION-22 reaches them. No decision answered it.
- **A parenthesis after a title.** Rule 10 says a title has no gloss
  after a dash or colon. The refinement's DECISION-38, on 2026-11-01,
  counted a parenthesis after a title as a gloss (FINDING-1369). The
  rule does not say so.

A fourth question needed no change: FINDING-1388 asked whether the
labels "Stage 1 Gate" to "Stage 6 Gate" may stand beside the Name
Plan Step Gate. Rule 9 already lets a label inside its owner keep its
case, and these sit inside the infra-establish Agent Skill's walk.

The last read reads all Living Text against these rules. A rule that
says less than was decided makes every bold home a finding the
reviewer then declines.

## Options considered

**Bold on a Name** (DECISION-22's options):
1. **No mark at all, as rule 9 says.** Rejected by the reviewer: the
   capitals show that a word is a Name, but not where it is defined.
2. **Bold once, at the line that defines it.** Taken. The bold makes
   the Name's one home visible, and a retelling does not bold. A
   script can check it: each bold Name is bold once in Living Text,
   in the file its glossary entry points at.

**A list item's bold lead that begins with a Name:**
1. **The lead loses its bold, or is reworded.** Rejected: the bold
   marks where the item starts, as a numbered rule's bold lead does,
   and rule 10 already treats such a lead as form.
2. **The bold marks the item, not the Name, and stands.** Taken. The
   glossary's entries are such leads too, so the glossary needs no
   exception of its own.

**A parenthesis after a title** (DECISION-38's options):
1. **A parenthesis is not a gloss.** Rejected by the reviewer, as
   recommended: the brackets change the mark, not what the words do.
   A gloss opens the body, whatever marks it off.
2. **A parenthesis is a gloss.** Taken.

## Decision

1. **Writing rule 9:** a Name is bold once, at the line that defines
   it. No other Markdown mark marks it, and it is bold nowhere else.
2. **Writing rule 9:** a bold lead that opens a list item marks the
   item, not the Name, and may begin with one.
3. **Writing rule 10:** a title has no gloss after a dash or colon,
   or in parentheses.

## Consequences

- The writing manual's §2 gains the lines and their why; both
  `writing.md`, ours and the container's, follow, each in a commit of
  its own.
- The bold homes Refinement Round 3 left in place now meet the rule.
- The Stack Group's bold leads stand.
- Rule 10 already says a title stands alone without its parent, so
  DECISION-38's first half changes no text.
- The labels "Stage 1 Gate" to "Stage 6 Gate" stand, under rule 9 as
  written.

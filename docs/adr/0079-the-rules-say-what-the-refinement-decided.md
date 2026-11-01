# 0079. The rules say what the refinement decided

Date: 2026-11-01
Status: Accepted (2026-11-01, at commit 6 of the commit plan for the
rules' fix; decision 4 narrowed since proposed, from every comma to a
comma that joins a gloss, so a list in a title stays allowed)

## Context

The refinement's decisions settle findings, and some of them change
what a rule allows. Two such decisions said their rule would gain
the line at Refinement Round 3's close, and it never did. Two more
read a rule wider than its words, and the rule took no line. Two
questions no decision answered. The last read reads all
Living Text against these rules. A rule that says less than was
decided makes every line the decision allows a finding the reviewer
then declines.

**Bold on a Name.** Writing rule 9 says no Markdown mark marks a
Name: every mark already has a job here, and the capitals show a
Name at every use (ADR-0076). Refinement Round 3 found Names bold at
the line that defines them, in FINDING-405, 474, 494, 626, 639 and
722. The reviewer chose, as the refinement's DECISION-22 on
2026-10-30, to allow bold there and nowhere else. The decision said
rule 9 would gain the line at Refinement Round 3's close. It did not.

**A list item's bold lead.** Some list items open with a bold lead
that begins with a Name, such as "**Catalog Check:**", in the Stack
Group's Agent Skills and references. FINDING-1384 asked whether
DECISION-22 reaches them. No decision answered it.

**A gloss after a title.** Rule 10 says a title has no gloss after
a dash or colon. Two decisions counted more as a gloss, and the
rule took neither:
- DECISION-20, on 2026-10-30: a comma that joins a gloss, as in
  *The tiers, drawn* (FINDING-368, 454, 471, 517 and 665);
- DECISION-38, on 2026-11-01: a parenthesis after a title
  (FINDING-1369).

**A released CHANGELOG entry.** The refinement's DECISION-18, on
2026-10-30, counted a released CHANGELOG entry as history: it keeps
the words it was released with (FINDING-568). The decision said the
one-home rule's *Not a second home* and facts-in-sync §1 would name
it at Refinement Round 3's close. Neither does.

**A Foundation Line's value.** The conventions manual gives the
value's forms, such as `the exchange convention` and `the agent
model` (`docs/conventions/conventions/` §1.3, *The Foundation Line*).
Each spells a Name in lowercase. The Change Walk greps for these
values exactly (`docs/conventions/facts-in-sync/` §4, *A Canonical
Description's rule*, step 3). A reader of Refinement Round 3's close
read met it, outside its rule, and no decision answered it.

Two more questions needed no change:
- FINDING-1388 asked whether the labels "Stage 1 Gate" to "Stage 6
  Gate" may stand beside the Name Plan Step Gate. Rule 9 already lets
  a label inside its owner keep its case, and these sit inside the
  infra-establish Agent Skill's walk.
- `devlog/README.md` and project-recording §4 say a devlog entry may
  be fragments. The writing rule covers every new record line, so
  those two lines are findings for the last read, not a rule in
  doubt.

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

**A gloss after a title** (DECISION-20's and DECISION-38's options):
1. **Only a dash or colon marks a gloss.** Rejected by the reviewer,
   as recommended: the mark changes, not what the words do. A gloss
   opens the body, whatever marks it off.
2. **A comma that joins a gloss, and a parenthesis, mark one too.**
   Taken.

**A released CHANGELOG entry** (DECISION-18's options):
1. **Living, fixed like any line.** Rejected by the reviewer. The
   decision's test was who reads a text: an agent works from an
   Approach on Trial's notes, so those are living. Nobody works from
   a released entry; it records what that version said.
2. **History, as the devlog is.** Taken.

**A Foundation Line's value:**
1. **The value takes the Names:** `the Exchange Convention`, `the
   Agent Model`. Rejected: every Foundation Line in both Convention
   Seats changes, with the conventions manual's forms and every grep
   that finds them, for a value no one reads as prose.
2. **The value is written as the conventions manual gives it,** as a
   path is written as it is. Taken.

## Decision

1. **Writing rule 9:** a Name is bold once, at the line that defines
   it. No other Markdown mark marks it, and it is bold nowhere else.
2. **Writing rule 9:** a bold lead that opens a list item marks the
   item, not the Name, and may begin with one.
3. **Writing rule 9:** a Foundation Line's value is written as the
   conventions manual gives it, like a path.
4. **Writing rule 10:** a title has no gloss after a dash or colon,
   joined by a comma, or in parentheses.
5. **History:** a released CHANGELOG entry is history, in facts-in-sync
   §1 and both `one-home.md`.

## Consequences

- The writing manual's §2 and facts-in-sync §1 gain the lines; both
  `writing.md` and both `one-home.md`, ours and the container's,
  follow, each in a commit of its own.
- The bold homes Refinement Round 3 left in place now meet the rule.
- The Stack Group's bold leads stand.
- Every Foundation Line stands as it is.
- Rule 10 already says a title stands alone without its parent, so
  DECISION-38's first half changes no text.
- The labels "Stage 1 Gate" to "Stage 6 Gate" stand, under rule 9 as
  written.
- A decision that changes what a rule allows is not done until the
  rule says it. The refinement's way of working (its file,
  `.claude/approaches-on-trial/refinement.md`) does not check this;
  its evaluation, at the refinement's close, weighs whether it should.

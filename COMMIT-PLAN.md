# Commit plan: the rules' fix before the last read

## Summary — the state after all commits

Writing rules 9 and 10 say what the refinement decided, in the
writing manual and in both copies of `writing.md`, ours and the
container's. Rule 9 lets a Name be bold once, at the line that
defines it, as DECISION-22 chose. A bold lead that opens a list item
may begin with a Name, since the bold marks the item, not the Name
(FINDING-1384's question). Rule 10 counts a parenthesis after a title
as a gloss, as DECISION-38 chose. ADR-0079 records the three, and
the refinement file records the last read's rule check, its four
doubts and how each ended. The last read can then start against
rules that say what was decided.

## Commits

**1. `docs(agent): add commit plan for the rules' fix`**
This plan.

**2. `docs: ADR-0079 proposed, bold at a Name's home`**
The decision first, Proposed: rule 9's bold at the defining line and
its list-lead clause, rule 10's parenthesis. Its options are
DECISION-22's and DECISION-38's, and the two answers to FINDING-1384
and FINDING-1388.

**3. `docs: writing rules 9 and 10 take the decisions`**
The writing manual's §2, *Why each rule*: rule 9's line on Markdown
marks, with why; rule 10's gloss line. The Canonical Description
changes, so the Change Walk runs on what derives from it, in
commits 4 and 5.

**4. `chore(agent): our writing.md takes rules 9 and 10`**
Our copy follows the manual: two lines, and the footer cites
ADR-0079. A commit of its own, as an agent file.

**5. `fix(delivery): shipped writing.md, rules 9 and 10`**
The container's copy follows the manual, the same two lines.

**6. `docs: the last read's rules checked, ADR-0079`**
The refinement file opens *The last read* with its rule check: each
Finding Kind's rule at its home now, what changed since each was
last read, the TODO search, the four doubts and how each ended.
ADR-0079 turns Accepted.

**7. `docs(agent): close commit plan for the rules' fix`**
Deletes this file; the body says what diverged.

## Decisions taken inside this plan

- **An ADR for three lines.** The refinement file goes at the close,
  and with it DECISION-22 and DECISION-38 leave Living Text; every
  earlier change to rules 9 to 11 has an ADR (ADR-0074 to ADR-0078).
  Struck on the reviewer's word, commit 2 goes and commit 6 records
  the check alone.
- **One clause for list leads, not two exceptions.** The glossary's
  own entries open with a bold Name. The list-lead clause covers
  them, so the rule needs no second exception for the glossary.
- **Rule 10's "standing alone" is already written.** DECISION-38's
  first half needs no change; only the parenthesis is added.
- **FINDING-1388 changes no rule.** "Stage 1 Gate" to "Stage 6 Gate"
  are labels inside their owner, which rule 9 already allows. The
  answer is recorded in commit 6.
- **TODO's "Decide whether writing rule 10 reaches unnumbered
  headings" stays as written.** It speaks of numbered titles' rule
  as it was read in Refinement Round 3, and stays true.

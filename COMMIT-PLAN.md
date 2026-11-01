# Commit plan: the rules' fix before the last read

## Summary — the state after all commits

Writing rules 9 and 10 and the one-home rule say what the refinement
decided, in their manuals and in both copies of each Agent Rule, ours
and the container's. Rule 9 lets a Name be bold once, at the line
that defines it, as DECISION-22 chose. A bold lead that opens a list
item may begin with a Name, since the bold marks the item, not the
Name (FINDING-1384's question). A Foundation Line's value is written
as conventions §1.3 gives it, as a path is. Rule 10 counts a
parenthesis or a comma after a title as a gloss, as DECISION-38 and
DECISION-20 chose. Facts-in-sync §1 and both `one-home.md` count a
released CHANGELOG entry as history, as DECISION-18 chose.
ADR-0079 records them all, and the refinement file records the last
read's rule check, its eight doubts and how each ended. The last read
can then start against rules that say what was decided.

## Commits

**1. `docs(agent): add commit plan for the rules' fix`**
This plan.

**2. `docs: ADR-0079 proposed, bold at a Name's home`**
The decision first, Proposed: rule 9's bold at the defining line and
its list-lead clause, rule 10's parenthesis. Its options are
DECISION-22's and DECISION-38's, and the two answers to FINDING-1384
and FINDING-1388.

**2b. `docs: ADR-0079 revised, three more decisions`**
Inserted: the close read's *Met at the close read, of other kinds*
held three more decisions the rules never took. ADR-0079 gains
DECISION-20's comma, DECISION-18's released CHANGELOG entry, and the
Foundation Line's value written as conventions §1.3 gives it. Its
title widens to "The rules say what the refinement decided", and
its file is renamed with it.

**3. `docs: writing rules 9 and 10 take the decisions`**
The writing manual's §2, *Why each rule*: rule 9's line on Markdown
marks, with why, and the Foundation Line's value among what is
written otherwise; rule 10's gloss line, with the parenthesis and
the comma. The Canonical Description changes, so the Change Walk
runs on what derives from it, in commits 4 and 5.

**3b. `docs: a released CHANGELOG entry is history`**
Inserted. Facts-in-sync §1, *One home*: a released CHANGELOG entry
joins the list of history. The Change Walk runs on both
`one-home.md`, in commits 4b and 5b.

**4. `chore(agent): our writing.md takes rules 9 and 10`**
Our copy follows the manual: its rule 9 and rule 10 lines, and the
footer cites ADR-0079. A commit of its own, as an agent file.

**4b. `chore(agent): our one-home rule names the CHANGELOG`**
Inserted. Our `one-home.md`'s *Not a second home* follows
facts-in-sync §1, and the footer cites ADR-0079.

**5. `fix(delivery): shipped writing.md, rules 9 and 10`**
The container's copy follows the manual, the same lines.

**5b. `fix(delivery): shipped one-home, released entries`**
Inserted. The container's `one-home.md` follows facts-in-sync §1.

**6. `docs: the last read's rules checked, ADR-0079`**
The refinement file opens *The last read* with its rule check: each
Finding Kind's rule at its home now, what changed since each was
last read, the TODO search, the eight doubts and how each ended.
It names *Met at the close read, of other kinds* as the read's
input, beside the list in *The work*. ADR-0079 turns Accepted.

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
- **One ADR, not two.** DECISION-18's line is on the one-home rule,
  not the writing rule. It is one more decision the rules never took,
  the same cause as the rest, so ADR-0079 takes it under a wider
  title.
- **The container's `one-home.md` follows too.** Facts-in-sync §1 is
  both Convention Seats' rule. A CBC Run's CHANGELOG has released
  entries as ours does, and they record what shipped then.
- **"Fragments fine" changes no rule.** `devlog/README.md` and
  project-recording §4 say a devlog entry may be fragments. The
  writing rule covers every new record line, so those two lines are
  findings for the last read.

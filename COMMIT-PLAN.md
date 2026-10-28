# Commit plan: the story behind a lesson

## Summary — the state after all commits

A manual keeps its rules, and one line where each rule's story was:
"*Its story: devlog 2026-10-19, later.*". The story lives in the
history that tells it. TODO's "Decide whether a manual keeps the
story behind a lesson" is worked, and leaves TODO. Decided
2026-10-28, in three steps:

1. **A dated note becomes one line pointing at its story.** Then the
   section is read again: where its lesson no longer reads clearly
   without the case, it gains a plain example.
2. **The story's home is the history that already tells it:** an
   ADR, or a devlog entry. A story told nowhere else is written,
   word for word, into one devlog entry on the day it moves.
3. **Now, before round 3's rule check,** so round 3 reads the
   manuals in the shape they keep.

Measured 2026-10-28: 70 dated notes, about 290 lines, in the 12
manuals (7% of them) and one model. About 50 are told already in an
ADR or the devlog; about 20 are not.

Out of scope, by design:
- a manual's *What it is for*, whose evidence the need asks for
  (`docs/conventions/conventions/` §2.2, *What it is for*);
- an approach's dated *Uses*, its evidence for evaluation.

A live claim found inside a note moves into the body, as round 2's
Lessons kind asked.

## Commits

**0. `docs(agent): add commit plan for lesson stories`**
Opens the set.

**1. `docs: ADR-0073 a lesson's story lives in history`**
Proposed. The three decisions, and what each rejected.

**2. `docs: the lesson rule points at its story`**
Conventions §2.6: the case goes to the history that tells it, and
the manual keeps the line that points there; the section is read
again after. Facts-in-sync §4's list of where history lives loses
"a lesson's dated italic".

**3. `chore(agent): our files follow the lesson rule`**
`convention-manual.md` item 6; `approach-evaluation.md` stage 6,
which likens a use note to a lesson's; `model-placing.md` stage 3
and its *Not known yet*, where a model's dated note becomes the same
one line.

**4. `docs: devlog keeps the lessons' own stories`**
One entry, dated 2026-10-28, holding the ~20 notes told nowhere else,
word for word, each under its manual and section. Written before the
manuals move, so each pointer lands.

**5. `docs: the exchange's lessons point at stories`**
16 notes.

**6. `docs: two manuals' lessons point at stories`**
Conventions and facts-in-sync: 17 notes.

**7. `docs: records' manuals point at their stories`**
Project-recording and agent-arrangement: 14 notes.

**8. `docs: the other lessons point at stories`**
Commit-messages, commit-plan, shapes, retrospective, repo-hygiene,
visual-comparison, writing, and the tiers model: 23 notes.

In each of 5 to 8, every note is read beside its candidate home
first; its line names the exact entry; a live claim moves into the
body; the section is read again for the safeguard.

**9. `docs: ADR-0073 accepted, the story item worked`**
The TODO item leaves, and conversation-memory §18 goes with it.

**10. `docs(agent): close commit plan for lesson stories`**
Deletes this file; the body says what diverged.

**Provisional, after any commit: the walk's inserts.** A commit
that changes a description walks what stands on it; a derived file
that then disagrees gets a lettered commit after it.

## Decisions for you to object to

- **The line's form:** "*Its story: ADR-0059.*", "*Its story:
  devlog 2026-10-19, later.*". A note told in several places names
  each. It stays in italics, set apart from the rule, as the note
  was.
- **The orphans' entry first,** so no line points at nothing. Its
  heading names what it is: "2026-10-28, the lessons' own stories".
- **A note an ADR tells only in part** points at the ADR, and what
  the ADR leaves out goes, word for word, into the orphans' entry.
- **Examples are not decided here.** The safeguard adds one only
  where a section needs it; whether the conventions keep examples
  at all is TODO's own item.
- **Nothing ships.** No run holds a manual, so no run's file changes.

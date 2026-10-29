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
   word for word, into a devlog entry in the commit that moves its
   manual's notes.
3. **Now, before round 3's rule check,** so round 3 reads the
   manuals in the shape they keep.

Measured 2026-10-28, and again 2026-10-29 when the plan returned:
72 dated notes, about 310 lines, in the 12 manuals (8% of them) and
one model. About 50 are told already in an ADR or the devlog; about
21 are not.

Out of scope, by design:
- a manual's *What it is for*, whose evidence the need asks for
  (`docs/conventions/conventions/` §2.2, *What it is for*);
- an approach's dated *Uses*, its evidence for evaluation.

A live claim found inside a note moves into the body, as round 2's
Lessons kind asked.

## Commits

**0. `docs(agent): add commit plan for lesson stories`**
Opens the set: first as `ed876b0`, parked as `b6d9e79` before any
work, and opened again after run 6's birth.

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

**4. Dropped, 2026-10-29.** It was one devlog entry for every story
told nowhere else, written first. Which stories those are shows only
when each note is read beside its home, which 5 to 8 do. So each of
them writes its own.

**5. `docs: the exchange's lessons point at stories`**
16 notes.

**6. `docs: two manuals' lessons point at stories`**
Conventions and facts-in-sync: 17 notes.

**7. `docs: records' manuals point at their stories`**
Project-recording and agent-arrangement: 15 notes.

**8. `docs: the other lessons point at stories`**
Commit-messages, commit-plan, shapes, retrospective, repo-hygiene,
visual-comparison, writing, and the tiers model: 24 notes.

In each of 5 to 8, every note is read beside its candidate home
first; its line names the exact entry; a live claim moves into the
body; the section is read again for the safeguard. A story told
nowhere else goes, word for word, into a devlog entry in the same
commit, headed "<its date>, the lessons' own stories: <the
manuals>", so its pointer lands at once.

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
- **Each commit's orphans land with their pointers,** so no line
  points at nothing: one devlog entry per commit, its heading
  naming what it is.
- **A note an ADR tells only in part** points at the ADR, and what
  the ADR leaves out goes, word for word, into that commit's entry.
- **Examples are not decided here.** The safeguard adds one only
  where a section needs it; whether the conventions keep examples
  at all is TODO's own item.
- **Nothing ships.** No run holds a manual, so no run's file changes.

# 0051. A run fixes what it lived, chapters included

Date: 2026-10-15
Status: Accepted (2026-10-15, at the set's records commit; opened
Proposed under the commit plan for chapter edits)

## Context

The exchange lets a run edit a delivered copy in place when
something happened that the copy did not foresee, and the edit is
one any run would want (`docs/conventions/exchange/` §5.1). Two
exceptions stood. The concept chapters were never edited: a chapter
is not run, so nothing in it can fail a step, and a lesson about one
went to the deliverer as a prose line (§5.6). That clause came with
run 3's own first rule, from which the shipped rule was built on
2026-09-25. And a copy the run had finished with was edited "the
same way" (§5.2), but nothing said when.

Run 3, never-oversold, met both in its Step 10, applying its
retrospective (its RETRO.md, D28):

- **Fixes kept as notes.** Through Step 10's triage its agent kept
  every fix to a finished skill for "next run only": framing's
  copying, the slice record's outline, the harness's form, the
  ground's levers, the bootstrap's requirements. No rule asked for
  that. The reviewer pointed it out when the definition's six losses
  were traced to `cbc-framing`'s close, which composed the exports by
  copying: the run that saw the mistake was leaving the fix for us to
  translate. Fixed in place instead, four skills reached us edited
  and marked untried, and this repo's reading of 2026-10-15 took all
  four, reading those hunks hardest; one clause of one was held.
- **The chapters asked about.** The reviewer then asked why the
  chapters are blocked at all, since the deliverer decides either
  way. Run 3 edited no chapter: its chapter wishes were preferences,
  not mistakes.

## Options considered

- **Keep the chapter clause, held until a run lives a chapter
  mistake** (this repo's agent, 2026-10-15). No run has lived one,
  and the prose line has carried a concept lesson before: run 3's
  SL-3 reached chapter 02 as ADR-0048. Rejected by the reviewer: the
  deliverer decides either way, and an exact hunk is judged where a
  note must first be translated, the reason the exchange already
  gives for finished copies. Held, the first lived mistake would
  arrive as a note.
- **Chapters editable for wording too.** Rejected, by run 3: a
  preference is not evidence, and the chapters are the method's
  statement, shared by every run.
- **Finished copies' fixes kept as notes for a later run** (run 3's
  agent through its triage). Rejected: the deliverer translates a
  note, and the run that lived the mistake does not write the fix.
- **A note asking the deliverer to reconsider the clause, nothing
  more.** Rejected, by run 3: the deliverer would write the change it
  is asked to judge.

## Decision

1. **A run may edit its copy of a concept chapter as it edits any
   copy, and only from a mistake lived in the run** — never from a
   preference for other wording. Its hand-off goes as any copy's.
2. **A copy the run has finished with is fixed whenever the evidence
   is in the run**, never kept as a note for a later run.
3. **Its hand-off line says so:** "untried here: written from this
   run's evidence, never run", so the deliverer reads those hunks
   hardest.

## Consequences

- The exchange manual's §5.1, §5.2 and §5.6, `ARCHITECTURE.md` §1.1
  and the shipped `delivered-copies.md` change. Run 3's copy already
  says all three; the next take brings every run the same text.
- The concept stays canonical here. A run's chapter edit is its
  copy's; the concept changes only when the deliverer takes the
  edit, and whether that bumps its version is ADR-0003's question,
  asked then.
- An untried edit is taken when it is sound, and the next run is its
  trial.
- §5.1's dated lesson, which names "the never-edited concept", is
  history and stays.
